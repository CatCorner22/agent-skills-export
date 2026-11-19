#!/usr/bin/env python3
"""Flag stale or undated sources in a bibliography, notes file or INDEX.md.

Usage: source_freshness.py FILE.md --half-life-days N [--as-of YYYY-MM-DD]
Scans every line that holds a URL or a '[title](link)' and looks for a date on that line
(YYYY-MM-DD, YYYY-MM, 'Month YYYY' or a bare year). Lines without a date are 'undated'.
Lines older than the half-life are 'stale' and need a re-check. Exit 1 if any stale or undated.
"""
import datetime as dt
import re
import sys

MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
DATE_RX = [
    (re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b"), lambda m: dt.date(int(m[1]), int(m[2]), int(m[3]))),
    (re.compile(r"\b(20\d\d)-(\d\d)\b"), lambda m: dt.date(int(m[1]), int(m[2]), 1)),
    (re.compile(r"\b([A-Za-z]{3})[a-z]*\.? (\d{1,2}),? (20\d\d)\b"), lambda m: dt.date(int(m[3]), MONTHS[m[1].lower()[:3]], int(m[2]))),
    (re.compile(r"\b([A-Za-z]{3})[a-z]*\.? (20\d\d)\b"), lambda m: dt.date(int(m[2]), MONTHS[m[1].lower()[:3]], 1)),
    (re.compile(r"\b(20\d\d)\b"), lambda m: dt.date(int(m[1]), 7, 1)),
]
SOURCE_LINE = re.compile(r"https?://|\]\(")


def find_date(line):
    for rx, fn in DATE_RX:
        m = rx.search(line)
        if m:
            try:
                return fn(m)
            except (KeyError, ValueError):
                continue
    return None


def main(argv):
    if len(argv) < 2 or "--half-life-days" not in argv:
        print(__doc__)
        return 2
    half = int(argv[argv.index("--half-life-days") + 1])
    as_of = dt.date.fromisoformat(argv[argv.index("--as-of") + 1]) if "--as-of" in argv else dt.date.today()
    try:
        lines = open(argv[1], encoding="utf-8").read().splitlines()
    except OSError as exc:
        print(f"cannot read: {exc}")
        return 2
    stale = undated = fresh = 0
    for n, line in enumerate(lines, 1):
        if not SOURCE_LINE.search(line):
            continue
        d = find_date(line)
        if d is None:
            undated += 1
            print(f"UNDATED line {n}: {line.strip()[:90]}")
        elif (as_of - d).days > half:
            stale += 1
            print(f"STALE   line {n}: {d.isoformat()} ({(as_of - d).days} days old): {line.strip()[:80]}")
        else:
            fresh += 1
    print(f"summary: {fresh} fresh, {stale} stale (> {half} days), {undated} undated, as of {as_of}")
    return 1 if stale or undated else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
