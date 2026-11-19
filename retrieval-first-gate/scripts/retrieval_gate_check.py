#!/usr/bin/env python3
"""Check a transcript for facts stated before any retrieval.

Usage: retrieval_gate_check.py TRANSCRIPT.json [--allow-memory]
TRANSCRIPT.json: OpenAI-style message list (or {"messages": [...]}), Anthropic tool_use blocks also work.
A "fact" is a number, year, date, price, version, URL or quoted figure in assistant text.
Exit 1 if assistant text with facts appears before the first tool result (unless --allow-memory),
or if the final answer contains facts and no tool was ever called. Exit 2 on bad input.
"""
import json
import re
import sys

FACT = re.compile(r"(\$\s?\d[\d,.]*|\b\d{1,3}(?:,\d{3})+\b|\b\d+(?:\.\d+)?\s?%|\b(?:19|20)\d\d\b|\bv?\d+\.\d+(?:\.\d+)?\b|https?://\S+|\b\d+(?:\.\d+)?\s?(?:million|billion|thousand|tokens|ms|seconds|minutes)\b)", re.I)


def text_of(m):
    c = m.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return " ".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
    return ""


def has_tool_call(m):
    if m.get("tool_calls"):
        return True
    c = m.get("content")
    return isinstance(c, list) and any(isinstance(b, dict) and b.get("type") == "tool_use" for b in c)


def is_tool_result(m):
    if m.get("role") == "tool":
        return True
    c = m.get("content")
    return isinstance(c, list) and any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    allow_memory = "--allow-memory" in argv
    try:
        data = json.load(open(argv[1], encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read: {exc}")
        return 2
    msgs = data.get("messages", []) if isinstance(data, dict) else data
    seen_result, any_call = False, False
    findings = []
    for i, m in enumerate(msgs):
        if not isinstance(m, dict):
            continue
        if is_tool_result(m):
            seen_result = True
        if m.get("role") != "assistant":
            continue
        if has_tool_call(m):
            any_call = True
        facts = FACT.findall(text_of(m))
        if facts and not seen_result:
            lvl = "warn" if allow_memory else "error"
            findings.append((lvl, f"messages[{i}]: {len(facts)} fact-like token(s) before any tool result, e.g. {facts[0]!r}"))
    last = next((m for m in reversed(msgs) if isinstance(m, dict) and m.get("role") == "assistant"), None)
    if last is not None and FACT.findall(text_of(last)) and not any_call:
        findings.append(("error", "final answer contains facts and no tool was called in the whole transcript"))
    for lvl, msg in findings:
        print(f"{lvl.upper():5} {msg}")
    errors = sum(1 for lvl, _ in findings if lvl == "error")
    print(f"tool calls: {'yes' if any_call else 'no'}; summary: {errors} error(s), {len(findings) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
