#!/usr/bin/env python3
"""Temporal grounding: emit a date header for prompts and flag undated time-relative language in drafts.

Usage: temporal_check.py header [--tz America/New_York] [--cutoff "2026-03"] [--model NAME]
       temporal_check.py scan DRAFT.md [--today YYYY-MM-DD]
header: prints a block to place in the system prompt or at the end of the prefix (never inside the cached
prefix): today's date and weekday, timezone, the model's stated training cutoff, and the rule that anything
after the cutoff or time-sensitive needs a fetched source with its own date.
scan: flags relative-time words with no absolute date nearby ("currently", "latest", "recently", "this year",
"as of now", "to date", "now", "upcoming"), future-dated claims stated as fact, "last updated" without a date,
and years more than one year behind today presented as current. Exit 1 if flags, 2 on bad input.
"""
import datetime as dt
import re
import sys

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None

RELATIVE = re.compile(r"\b(currently|at present|as of (now|today|this writing)|latest|most recent(ly)?|recently|this (year|month|week|quarter)|to date|now available|upcoming|soon|next (year|month|quarter)|last (year|month|week|quarter))\b", re.I)
DATE_NEAR = re.compile(r"\b(20\d\d|19\d\d)(-\d\d(-\d\d)?)?\b|\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.? \d{1,2}(,? \d{4})?\b", re.I)
UPDATED = re.compile(r"\b(last updated|updated on|current as of|version)\b(?!.{0,30}\d)", re.I)


def header(argv):
    tz = argv[argv.index("--tz") + 1] if "--tz" in argv else "UTC"
    cutoff = argv[argv.index("--cutoff") + 1] if "--cutoff" in argv else "unknown"
    model = argv[argv.index("--model") + 1] if "--model" in argv else "the model"
    now = dt.datetime.now(ZoneInfo(tz)) if ZoneInfo and tz != "UTC" else dt.datetime.now(dt.timezone.utc)
    print(f"Today is {now.strftime('%A, %Y-%m-%d')} ({tz}). {model}'s training data ends around {cutoff}; "
          f"it has no clock and no knowledge of events after that date unless they appear in this conversation.\n"
          f"Rules: (1) Treat prices, versions, office-holders, laws, schedules, 'latest' anything and all events after {cutoff} as unknown "
          f"until a fetched source in this conversation states them; cite that source and its date. (2) Compute ages, durations and "
          f"deadlines from today's date above, with code where available. (3) Write absolute dates (YYYY-MM-DD), never 'recently' or 'this year'. "
          f"(4) If a question depends on the current state of something and no source is present, say so and stop.")
    return 0


def scan(argv):
    if len(argv) < 3:
        print(__doc__); return 2
    try:
        text = open(argv[2], encoding="utf-8").read()
    except OSError as exc:
        print(f"cannot read: {exc}"); return 2
    today = dt.date.fromisoformat(argv[argv.index("--today") + 1]) if "--today" in argv else dt.date.today()
    flags = []
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        for m in RELATIVE.finditer(line):
            window = " ".join(lines[max(0, i - 2):i])
            if not DATE_NEAR.search(window):
                flags.append(f"line {i}: relative time {m.group(0)!r} with no absolute date nearby")
        if UPDATED.search(line):
            flags.append(f"line {i}: 'updated/as of/version' without a date or number")
        for y in re.finditer(r"\b(20\d\d)\b", line):
            year = int(y.group(1))
            if year > today.year and re.search(r"\b(is|are|was|has|released|launched|current)\b", line, re.I):
                flags.append(f"line {i}: future year {year} stated as fact")
            if year < today.year - 1 and re.search(r"\b(current|latest|now|today)\b", line, re.I):
                flags.append(f"line {i}: {year} described as current (today is {today})")
    for f in flags:
        print(f"FLAG {f}")
    print(f"summary: {len(flags)} flag(s); today {today}")
    return 1 if flags else 0


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    if argv[1] == "header":
        return header(argv)
    if argv[1] == "scan":
        return scan(argv)
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
