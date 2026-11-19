#!/usr/bin/env python3
"""Plan request rates against any provider's limits and classify 429-class errors with the right fix.

Usage:
  rate_budget.py plan --prompt-tokens N --max-output-tokens N --calls-per-min N --tpm LIMIT [--rpm LIMIT] [--reserve actual|max]
  rate_budget.py classify ERROR.json
  rate_budget.py backoff [--base 1] [--max 60] [--tries 6]
plan: tokens per minute = prompt + (max output if --reserve max, the default, since OpenAI and Moonshot reserve on
max_tokens at admission; use actual when your provider counts generated tokens). Exit 1 when over TPM or RPM.
classify: reads an error body ({"status":429,"error":{...}} or the raw body) and maps OpenAI (rate_limit_exceeded,
insufficient_quota), Anthropic (rate_limit_error, overloaded_error / 529), Google (RESOURCE_EXHAUSTED), Moonshot
(engine_overloaded_error, rate_limit_reached_error, exceeded_current_quota_error) and gateway look-alikes (401/403/404/
503) to a fix. Exit 0 for transient capacity errors (back off), 1 when something must change (quota, limits, config).
backoff: prints a jittered exponential schedule to copy into a client.
"""
import json
import random
import sys

FIXES = {
    "rate_limit_exceeded": ("limit", "org or key hit RPM/TPM; honor Retry-After and x-ratelimit-reset-*, lower calls/min or max_output_tokens, or raise tier"),
    "insufficient_quota": ("quota", "billing quota exhausted; add funds or raise the monthly cap; backoff will not help"),
    "rate_limit_error": ("limit", "Anthropic RPM/ITPM/OTPM hit; read retry-after and anthropic-ratelimit-*-reset headers; lower concurrency"),
    "overloaded_error": ("capacity", "provider capacity (529); retry with backoff; not your limit"),
    "RESOURCE_EXHAUSTED": ("limit", "Google quota or rate limit; check which quota in the message; lower rate or request a quota raise"),
    "engine_overloaded_error": ("capacity", "Moonshot capacity; wait Retry-After, lower concurrency; tier upgrade does not help"),
    "rate_limit_reached_error": ("limit", "Moonshot concurrency/RPM/TPM/TPD; slow down, lower max_completion_tokens, or raise tier"),
    "exceeded_current_quota_error": ("quota", "Moonshot balance or voucher exhausted; top up"),
}


def arg(argv, name, default=None, cast=int):
    return cast(argv[argv.index(name) + 1]) if name in argv else default


def plan(argv):
    p = arg(argv, "--prompt-tokens"); mo = arg(argv, "--max-output-tokens"); cpm = arg(argv, "--calls-per-min"); tpm = arg(argv, "--tpm"); rpm = arg(argv, "--rpm")
    reserve = argv[argv.index("--reserve") + 1] if "--reserve" in argv else "max"
    if None in (p, mo, cpm, tpm):
        print(__doc__); return 2
    per_req = p + (mo if reserve == "max" else 0)
    used = per_req * cpm
    print(f"per request counted: {per_req:,} tokens (prompt {p:,}{' + max output ' + format(mo, ',') if reserve == 'max' else ', output counted after the fact'})")
    print(f"per minute at {cpm} calls: {used:,} of TPM {tpm:,} ({used / tpm:.0%})")
    rc = 0
    if used > tpm:
        print(f"OVER  TPM: cut max output to <= {max(0, tpm // cpm - p):,} or calls/min to <= {tpm // per_req}"); rc = 1
    elif used > 0.8 * tpm:
        print("WARN  above 80% of TPM; bursts will 429")
    if rpm and cpm > rpm:
        print(f"OVER  RPM: {cpm} calls/min > {rpm}"); rc = 1
    return rc


def classify(argv):
    if len(argv) < 3:
        print(__doc__); return 2
    try:
        body = json.load(open(argv[2], encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read: {exc}"); return 2
    err = body.get("error", body)
    etype = str(err.get("type") or err.get("code") or err.get("status") or "")
    status = body.get("status") or body.get("status_code") or err.get("status_code")
    try:
        status = int(status) if status is not None else None
    except (TypeError, ValueError):
        status = None
    if status and status not in (429, 529):
        hint = {401: "bad key", 403: "key lacks access to this model or region", 404: "wrong endpoint or model id", 503: "gateway or provider outage; retry with backoff"}.get(status, "not a rate limit")
        print(f"status {status}: {hint}; do not treat as rate limit"); return 0 if status == 503 else 1
    kind, fix = FIXES.get(etype, ("unknown", "unknown type; read error.message and the rate-limit headers"))
    print(f"type: {etype or 'unknown'}  class: {kind}")
    print(f"fix:  {fix}")
    return 0 if kind == "capacity" else 1


def backoff(argv):
    base = arg(argv, "--base", 1.0, float); mx = arg(argv, "--max", 60.0, float); tries = arg(argv, "--tries", 6)
    random.seed(0)
    sched = [min(mx, base * 2 ** i) * (0.5 + random.random() / 2) for i in range(tries)]
    print("retry only on capacity/limit classes; never on quota or 4xx config errors; always prefer Retry-After when present")
    print("schedule (s): " + ", ".join(f"{s:.1f}" for s in sched))
    return 0


def main(argv):
    if len(argv) < 2 or argv[1] not in ("plan", "classify", "backoff"):
        print(__doc__); return 2
    return {"plan": plan, "classify": classify, "backoff": backoff}[argv[1]](argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
