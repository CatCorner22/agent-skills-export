#!/usr/bin/env python3
"""Check a task contract before sending it to a model.

Usage: contract_check.py CONTRACT.md
Requires sections: Job, Finish line, Effective instructions, Boundaries, State, Inputs present, Output shape,
Stop rule. Flags leftover placeholders ("...", TODO, TBD, <...>), a Finish line with no runnable check or named
deliverable, a Stop rule with no number, dynamic fields (dates, timestamps, run ids) above the State section
(they break prefix caching), and Inputs present entries that name files missing from --files. Exit 1 on
errors, 2 on bad input.
"""
import re
import sys

SECTIONS = ["Job", "Finish line", "Effective instructions", "Boundaries", "State", "Inputs present", "Output shape", "Stop rule"]
PLACEHOLDER = re.compile(r"(^|\s)(\.\.\.|TODO|TBD|<[^>]{1,40}>)(\s|$)", re.M)


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    try:
        text = open(argv[1], encoding="utf-8").read()
    except OSError as exc:
        print(f"cannot read: {exc}"); return 2
    files = argv[argv.index("--files") + 1:] if "--files" in argv else []
    errs, warns = [], []
    parts = re.split(r"^##\s+", text, flags=re.M)
    secs = {}
    for p in parts[1:]:
        title, _, body = p.partition("\n")
        secs[title.strip().split(" (")[0]] = body
    for s in SECTIONS:
        hit = next((k for k in secs if k.lower().startswith(s.lower())), None)
        if hit is None:
            errs.append(f"missing section: {s}")
        elif not secs[hit].strip():
            errs.append(f"empty section: {s}")
    for m in PLACEHOLDER.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        errs.append(f"line {line}: placeholder {m.group(2)!r} left in")
    fin = next((v for k, v in secs.items() if k.lower().startswith("finish")), "")
    if fin and not (re.search(r"`[^`]+`", fin) or re.search(r"\.(md|pdf|docx|csv|json|py|ts|zip)\b", fin)):
        warns.append("Finish line has no runnable check (`command`) or named deliverable file")
    stop = next((v for k, v in secs.items() if k.lower().startswith("stop")), "")
    if stop and not re.search(r"\d", stop):
        errs.append("Stop rule has no number (tool calls, minutes or attempts)")
    state_pos = text.lower().find("## state")
    head = text[:state_pos] if state_pos > 0 else ""
    for m in re.finditer(r"\b(\d{4}-\d\d-\d\d[T ]\d\d:\d\d|run[_ -]?id\s*[:=]\s*\S+|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4})", head, re.I):
        if "generation:" in head[max(0, m.start() - 40):m.start()]:
            continue
        warns.append(f"dynamic value {m.group(0)!r} above State section; move it down to keep the prefix cacheable")
    inputs = next((v for k, v in secs.items() if k.lower().startswith("inputs")), "")
    for m in re.finditer(r"`([^`]+)`", inputs):
        if files and not any(m.group(1) in f or f.endswith(m.group(1)) for f in files):
            errs.append(f"Inputs present names {m.group(1)!r} but it is not among --files")
    for e in errs:
        print(f"ERROR {e}")
    for w in warns:
        print(f"WARN  {w}")
    print(f"summary: {len(errs)} error(s), {len(warns)} warning(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
