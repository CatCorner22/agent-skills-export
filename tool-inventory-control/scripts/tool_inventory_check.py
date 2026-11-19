#!/usr/bin/env python3
"""Audit the tool definitions sent to a model.

Usage: tool_inventory_check.py TOOLS.json [--max-tools 30] [--max-tokens 8000]
TOOLS.json is a request body with "tools", or a bare list of tool definitions (OpenAI function
or Anthropic shape). Exit 0 = within budget, 1 = over budget or defects, 2 = bad input.
"""
import difflib
import json
import re
import sys


def load(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        data = data.get("tools", [])
    return data


def norm(tool):
    fn = tool.get("function", tool)
    return {
        "name": fn.get("name", "?"),
        "description": fn.get("description", "") or "",
        "params": fn.get("parameters", fn.get("input_schema", {})) or {},
        "raw": json.dumps(tool, sort_keys=True),
    }


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    max_tools = int(argv[argv.index("--max-tools") + 1]) if "--max-tools" in argv else 30
    max_tokens = int(argv[argv.index("--max-tokens") + 1]) if "--max-tokens" in argv else 8000
    try:
        tools = [norm(t) for t in load(argv[1])]
    except (OSError, json.JSONDecodeError, AttributeError) as exc:
        print(f"cannot read tools: {exc}")
        return 2
    findings = []
    total_chars = sum(len(t["raw"]) for t in tools)
    est_tokens = total_chars // 4
    print(f"tools: {len(tools)}, estimated tokens: {est_tokens} (chars/4)")
    if len(tools) > max_tools:
        findings.append(("error", f"{len(tools)} tools exceeds budget of {max_tools}; load tools per step instead"))
    if est_tokens > max_tokens:
        findings.append(("error", f"~{est_tokens} tokens of tool definitions exceeds budget of {max_tokens}"))
    names = [t["name"] for t in tools]
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if a == b:
                findings.append(("error", f"duplicate tool name {a!r}"))
            elif difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio() > 0.85:
                findings.append(("warn", f"near-duplicate names {a!r} and {b!r}; the model may confuse them"))
    for t in tools:
        d = t["description"].strip()
        if not d:
            findings.append(("error", f"{t['name']}: no description"))
        elif len(d) < 25:
            findings.append(("warn", f"{t['name']}: description under 25 chars; say when to use it and what it returns"))
        elif len(d) > 1200:
            findings.append(("warn", f"{t['name']}: description over 1200 chars; move detail to the tool result"))
        if not re.fullmatch(r"[a-zA-Z0-9_-]{1,64}", t["name"]):
            findings.append(("error", f"{t['name']!r}: name must be 1-64 chars of letters, digits, _ or -"))
        props = (t["params"] or {}).get("properties", {}) or {}
        if len(props) > 12:
            findings.append(("warn", f"{t['name']}: {len(props)} parameters; split the tool or group options"))
        for p, spec in props.items():
            if isinstance(spec, dict) and not spec.get("description") and not spec.get("enum"):
                findings.append(("info", f"{t['name']}.{p}: parameter has no description"))
    desc_pairs = [(t["name"], t["description"][:200].lower()) for t in tools]
    for i, (na, da) in enumerate(desc_pairs):
        for nb, db in desc_pairs[i + 1:]:
            if da and db and difflib.SequenceMatcher(None, da, db).ratio() > 0.9:
                findings.append(("warn", f"{na} and {nb} have near-identical descriptions"))
    for lvl, msg in findings:
        print(f"{lvl.upper():5} {msg}")
    errors = sum(1 for lvl, _ in findings if lvl == "error")
    print(f"summary: {errors} error(s), {len(findings) - errors} other finding(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
