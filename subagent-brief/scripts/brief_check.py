#!/usr/bin/env python3
"""Check a sub-agent brief before dispatch.

Usage: brief_check.py BRIEF.md [--files f1 f2 ...]
Errors: unfilled {placeholders}; missing Goal, Context, Do not, Inputs, Return format or Budget; no JSON return
format with a status field; budget without numbers; no stop/blocked rule; an input named in backticks that is not
in --files. Warnings: no explicit ban on installs/credentials/push; brief longer than ~1500 words (sub-agents
work better with a tight brief); goal longer than two sentences. Exit 1 on errors, 2 on bad input.
"""
import re
import sys

REQUIRED = ["Goal", "Context", "Do not", "Inputs", "Return format", "Budget"]


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    try:
        text = open(argv[1], encoding="utf-8").read()
    except OSError as exc:
        print(f"cannot read: {exc}"); return 2
    files = argv[argv.index("--files") + 1:] if "--files" in argv else []
    errs, warns = [], []
    for m in re.finditer(r"\{[^}\n]{0,60}\}", text):
        if not re.match(r"\{\s*\"", m.group(0)):
            errs.append(f"placeholder left in: {m.group(0)}")
    for r in REQUIRED:
        if not re.search(rf"^\s*(#+\s*)?(- )?{re.escape(r)}", text, re.I | re.M):
            errs.append(f"missing section: {r}")
    if not re.search(r"\"status\"\s*:", text):
        errs.append("return format has no JSON with a status field")
    bm = re.search(r"Budget:?(.*)", text, re.I)
    if bm and not re.search(r"\d", bm.group(1) + text[bm.end():bm.end() + 200]):
        errs.append("budget has no numbers")
    if not re.search(r"\b(blocked|stop)\b", text, re.I):
        errs.append("no stop/blocked rule")
    if not re.search(r"(do not|never|no)\b[^.\n]*(install|credential|secret|token|push|publish)", text, re.I):
        warns.append("no explicit ban on installs, credentials or pushes")
    words = len(text.split())
    if words > 1500:
        warns.append(f"brief is {words} words; trim to what the sub-agent needs")
    gm = re.search(r"Goal:?\s*(.+)", text, re.I)
    if gm and len(re.findall(r"[.!?](\s|$)", gm.group(1))) > 2:
        warns.append("goal is longer than two sentences")
    im = re.search(r"Inputs[^\n]*\n((?:.*\n?)*?)(?=\n\S|\Z)", text, re.I)
    for m in re.finditer(r"`([^`]+)`", (im.group(0) if im else "")):
        if files and not any(m.group(1) in f or f.endswith(m.group(1)) for f in files):
            errs.append(f"input {m.group(1)!r} named but not among --files")
    for e in errs:
        print(f"ERROR {e}")
    for w in warns:
        print(f"WARN  {w}")
    print(f"summary: {len(errs)} error(s), {len(warns)} warning(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
