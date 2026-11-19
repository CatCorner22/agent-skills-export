#!/usr/bin/env python3
"""Normalize usage/accounting fields from OpenAI, Anthropic, Gemini, Moonshot and gateway responses into one shape.

Usage: usage_normalize.py RESPONSES.jsonl [--out normalized.jsonl]
Each line: a raw API response (or {"usage": ...}). Output per line: {"provider", "model", "input_tokens",
"cached_input_tokens", "cache_write_tokens", "output_tokens", "reasoning_tokens", "finish_reason", "missing": [...]}.
"missing" lists fields the response did not carry (so a migration does not silently zero them). Exit 1 if any
record lacks input or output token counts, 2 on bad input.
"""
import json
import sys


def g(d, *keys):
    for k in keys:
        if isinstance(d, dict) and d.get(k) is not None:
            return d[k]
    return None


def normalize(r):
    u = r.get("usage") or r.get("usageMetadata") or (r if "prompt_tokens" in r or "input_tokens" in r else {})
    provider = "unknown"
    if "usageMetadata" in r or "promptTokenCount" in u:
        provider = "gemini"
    elif "cache_read_input_tokens" in u or r.get("type") == "message":
        provider = "anthropic"
    elif "prompt_tokens" in u:
        provider = "openai-compatible"
    out = {"provider": provider, "model": r.get("model") or r.get("modelVersion")}
    out["input_tokens"] = g(u, "prompt_tokens", "input_tokens", "promptTokenCount")
    out["cached_input_tokens"] = g(u.get("prompt_tokens_details") or {}, "cached_tokens") if isinstance(u.get("prompt_tokens_details"), dict) else None
    if out["cached_input_tokens"] is None:
        out["cached_input_tokens"] = g(u, "cached_tokens", "cache_read_input_tokens", "cachedContentTokenCount")
    out["cache_write_tokens"] = g(u, "cache_creation_tokens", "cache_creation_input_tokens")
    out["output_tokens"] = g(u, "completion_tokens", "output_tokens", "candidatesTokenCount")
    out["reasoning_tokens"] = g(u.get("completion_tokens_details") or {}, "reasoning_tokens") if isinstance(u.get("completion_tokens_details"), dict) else None
    if out["reasoning_tokens"] is None:
        out["reasoning_tokens"] = g(u, "reasoning_tokens", "thoughtsTokenCount")
    fr = None
    if isinstance(r.get("choices"), list) and r["choices"]:
        fr = r["choices"][0].get("finish_reason")
    fr = fr or r.get("stop_reason") or (r.get("candidates", [{}])[0].get("finishReason") if isinstance(r.get("candidates"), list) and r["candidates"] else None)
    out["finish_reason"] = fr
    out["missing"] = [k for k in ("input_tokens", "cached_input_tokens", "cache_write_tokens", "output_tokens", "reasoning_tokens", "finish_reason") if out[k] is None]
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    try:
        rows = [json.loads(l) for l in open(argv[1], encoding="utf-8") if l.strip()]
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read: {exc}"); return 2
    outs = [normalize(r) for r in rows]
    bad = [i for i, o in enumerate(outs) if o["input_tokens"] is None or o["output_tokens"] is None]
    if "--out" in argv:
        with open(argv[argv.index("--out") + 1], "w", encoding="utf-8") as fh:
            for o in outs:
                fh.write(json.dumps(o) + "\n")
    else:
        for o in outs:
            print(json.dumps(o))
    providers = sorted({o["provider"] for o in outs})
    print(f"summary: {len(outs)} record(s); providers {providers}; {len(bad)} without core token counts", file=sys.stderr)
    for i in bad:
        print(f"ERROR record {i}: missing input or output token count", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
