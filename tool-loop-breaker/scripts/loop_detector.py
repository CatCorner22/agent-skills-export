#!/usr/bin/env python3
"""Find repeated-tool-call loops in an agent transcript.

Input: a JSON list of OpenAI-style messages, an object with "messages", or JSONL (one message per line).
Usage: loop_detector.py TRANSCRIPT [--run N] [--total N]
Flags a loop when the same tool call (name + normalized arguments) repeats N times in a row
(default 3) or appears N times overall (default 5). Exit 1 when a loop is found, 2 on bad input.
"""
import json
import re
import sys
from collections import Counter

WRITE_HINTS = ("edit", "write", "create", "patch", "apply", "replace", "insert", "delete", "move")
DEDUP_HINTS = re.compile(r"wasted call|file unchanged|already (read|viewed)|duplicate call|no changes since", re.I)


def load(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = [json.loads(line) for line in text.splitlines() if line.strip()]
    if isinstance(data, dict):
        data = data.get("messages", [])
    if not isinstance(data, list):
        raise ValueError("no message list found")
    return data


def normalize_args(raw):
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except json.JSONDecodeError:
            return raw.strip()
    return json.dumps(raw, sort_keys=True)


def tool_calls(messages):
    for idx, m in enumerate(messages):
        if not isinstance(m, dict) or m.get("role") != "assistant":
            continue
        for tc in m.get("tool_calls") or []:
            fn = tc.get("function", tc)
            yield idx, fn.get("name", "?"), normalize_args(fn.get("arguments", fn.get("input", "")))
        content = m.get("content")
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    yield idx, block.get("name", "?"), normalize_args(block.get("input", {}))


def analyze(messages, run_limit=3, total_limit=5):
    calls = list(tool_calls(messages))
    report = {"tool_calls": len(calls), "loops": [], "notes": []}
    run, prev = 0, None
    for idx, name, args in calls:
        key = (name, args)
        run = run + 1 if key == prev else 1
        prev = key
        if run == run_limit:
            report["loops"].append(f"{run_limit}+ identical consecutive calls to {name} starting near message {idx}")
    counts = Counter((n, a) for _, n, a in calls)
    for (name, args), n in counts.most_common():
        if n >= total_limit:
            report["loops"].append(f"{name} called {n}x with identical arguments: {args[:120]}")
    writes = sum(1 for _, n, _ in calls if any(h in n.lower() for h in WRITE_HINTS))
    if calls and writes == 0 and len(calls) >= 20:
        report["notes"].append(f"{len(calls)} tool calls and 0 write/edit calls: possible read-only stall")
    for i, m in enumerate(messages):
        if not isinstance(m, dict):
            continue
        text = m.get("content") if isinstance(m.get("content"), str) else json.dumps(m.get("content"))
        if m.get("role") == "tool" and text and DEDUP_HINTS.search(text):
            report["notes"].append(f"message {i}: harness dedup/rejection text; models read it as failure and re-call")
        if m.get("role") == "user" and not str(m.get("content") or "").strip():
            report["notes"].append(f"message {i}: empty user message (reported loop trigger after interrupts)")
    return report


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    run_limit = int(argv[argv.index("--run") + 1]) if "--run" in argv else 3
    total_limit = int(argv[argv.index("--total") + 1]) if "--total" in argv else 5
    try:
        messages = load(argv[1])
    except (OSError, ValueError) as exc:
        print(f"cannot read transcript: {exc}")
        return 2
    rep = analyze(messages, run_limit, total_limit)
    print(f"tool calls: {rep['tool_calls']}")
    for line in rep["loops"]:
        print(f"LOOP  {line}")
    for line in rep["notes"]:
        print(f"NOTE  {line}")
    print("verdict: LOOP" if rep["loops"] else "verdict: ok")
    return 1 if rep["loops"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
