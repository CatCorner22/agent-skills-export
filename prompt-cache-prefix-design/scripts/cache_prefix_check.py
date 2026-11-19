#!/usr/bin/env python3
"""Check chat requests for prompt-cache friendliness.

Usage: cache_prefix_check.py REQUEST.json [REQUEST2.json ...]
Each file is one chat-completions request (OpenAI or Anthropic shape). With two or more files
(consecutive requests of one workflow) the script also measures the shared prefix and reports where
they first diverge. Exit 0 = clean, 1 = findings at error level, 2 = bad input.
"""
import json
import re
import sys

DYNAMIC = [
    (re.compile(r"\b20\d\d-\d\d-\d\d(?:[T ]\d\d:\d\d(?::\d\d)?)?\b"), "date/timestamp"),
    (re.compile(r"\b(?:today is|current date|current time|now is)\b", re.I), "'today is' phrase"),
    (re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I), "UUID"),
    (re.compile(r"\b(?:request|session|trace|run)[_ -]?id\b[:=]?\s*\S+", re.I), "request/session id"),
    (re.compile(r"\b1[6-7]\d{8,11}\b"), "epoch timestamp"),
]


def flatten(req):
    """Return the request as an ordered list of (label, text) blocks in prefix order."""
    blocks = []
    if "system" in req and isinstance(req["system"], (str, list)):
        blocks.append(("system", json.dumps(req["system"]) if not isinstance(req["system"], str) else req["system"]))
    for i, t in enumerate(req.get("tools") or []):
        blocks.append((f"tools[{i}]", json.dumps(t, sort_keys=True)))
    for i, m in enumerate(req.get("messages") or []):
        blocks.append((f"messages[{i}]:{m.get('role', '?')}", json.dumps(m.get("content"), sort_keys=True)))
    return blocks


def check_one(req, label):
    out = []
    blocks = flatten(req)
    if not blocks:
        return [("error", f"{label}: no system, tools or messages found")]
    prefix = [b for b in blocks if b[0] == "system" or b[0].endswith(":system") or b[0].startswith("tools[")] or blocks[:1]
    for name, text in prefix:
        for rx, what in DYNAMIC:
            m = rx.search(text)
            if m:
                out.append(("error", f"{label}: {what} in prefix block {name}: {m.group(0)[:40]!r}"))
    sys_idx = [i for i, (n, _) in enumerate(blocks) if n == "system" or n.endswith(":system")]
    tool_idx = [i for i, (n, _) in enumerate(blocks) if n.startswith("tools[")]
    if sys_idx and tool_idx and min(tool_idx) < min(sys_idx):
        out.append(("info", f"{label}: tools precede system in this flattening; fine if the API orders them this way"))
    if sys_idx and sys_idx[0] != 0 and not tool_idx:
        out.append(("warn", f"{label}: system message is not first; put stable instructions at the top"))
    total = sum(len(t) for _, t in blocks)
    stable = sum(len(t) for n, t in blocks if n == "system" or n.startswith("tools["))
    if total and stable / total < 0.2 and total > 4000:
        out.append(("info", f"{label}: stable prefix is {stable * 100 // total}% of request; caching will save little"))
    return out


def common_prefix_len(a, b):
    n = min(len(a), len(b))
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    return i


def compare(reqs, labels):
    out = []
    flats = [json.dumps([list(b) for b in flatten(r)]) for r in reqs]
    for i in range(1, len(reqs)):
        prev, cur = reqs[i - 1], reqs[i]
        for key in ("model", "reasoning_effort", "thinking", "system"):
            if prev.get(key) != cur.get(key):
                lvl = "error" if key in ("reasoning_effort", "model", "system") else "warn"
                out.append((lvl, f"{labels[i]}: {key} changed from {labels[i-1]} ({prev.get(key)!r} -> {cur.get(key)!r}); prefix cache misses"))
        pb, cb = flatten(prev), flatten(cur)
        k = 0
        while k < min(len(pb), len(cb)) and pb[k] == cb[k]:
            k += 1
        cp = common_prefix_len(flats[i - 1], flats[i])
        pct = cp * 100 // max(1, len(flats[i]))
        if k < len(pb) and k < len(cb) and (pb[k][0].startswith("tools[") or pb[k][0] == "system"):
            out.append(("error", f"{labels[i]}: first difference is in {pb[k][0]}; a stable block changed, cache lost from there"))
        out.append(("info", f"{labels[i]}: shares ~{pct}% of serialized prefix with {labels[i-1]} (first differing block: {cb[k][0] if k < len(cb) else 'none'})"))
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    reqs, labels = [], []
    for path in argv[1:]:
        try:
            with open(path, encoding="utf-8") as fh:
                reqs.append(json.load(fh))
            labels.append(path.rsplit("/", 1)[-1])
        except (OSError, json.JSONDecodeError) as exc:
            print(f"cannot read {path}: {exc}")
            return 2
    findings = []
    for r, l in zip(reqs, labels):
        findings += check_one(r, l)
    if len(reqs) > 1:
        findings += compare(reqs, labels)
    for lvl, msg in findings:
        print(f"{lvl.upper():5} {msg}")
    errors = sum(1 for lvl, _ in findings if lvl == "error")
    print(f"summary: {errors} error(s), {len(findings) - errors} other finding(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
