#!/usr/bin/env python3
"""Flag over-claiming in a draft: absolutes, intensifiers, superlatives, unsourced numbers.

Usage: restraint_check.py DRAFT.md [--facts FACTSHEET.md]
With --facts, every number in the draft must also appear in the fact sheet, or it is flagged.
Exit 0 = clean, 1 = findings, 2 = bad input. Fenced code is skipped.
"""
import re
import sys

ABSOLUTES = r"\b(always|never|all|none|every|no one|everyone|guaranteed?|proven|proves?|undeniabl[ey]|certainly|definitely|impossible|without (?:a )?doubt|the only)\b"
INTENSIFIERS = r"\b(very|extremely|incredibly|hugely|massively|truly|really|clearly|obviously|of course|literally|revolutionary|game-?changing|unprecedented|groundbreaking)\b"
SUPERLATIVES = r"\b(best|worst|fastest|slowest|largest|smallest|most \w+|least \w+|#1|number one|world-?class|industry-?leading|leading)\b"
CITATION_NEAR = re.compile(r"(\[[^\]]+\]|\(https?://[^)]+\)|according to|reported|measured|per |source|study|benchmark|\bsee\b)", re.I)
NUMBER = re.compile(r"(\$\s?\d[\d,.]*\s?(?:[kKmMbB]|million|billion)?|\b\d+(?:\.\d+)?\s?%|\b\d{1,3}(?:,\d{3})+\b|\b\d+(?:\.\d+)?x\b)")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    try:
        text = open(argv[1], encoding="utf-8").read()
        facts = open(argv[argv.index("--facts") + 1], encoding="utf-8").read() if "--facts" in argv else None
    except OSError as exc:
        print(f"cannot read: {exc}")
        return 2
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    findings = []
    for label, rx in (("absolute", ABSOLUTES), ("intensifier", INTENSIFIERS), ("superlative", SUPERLATIVES)):
        for m in re.finditer(rx, prose, re.I):
            ctx = prose[max(0, m.start() - 35):m.end() + 35].replace("\n", " ")
            findings.append(f"{label:11} {m.group(0)!r}: ...{ctx}...")
    sentences = re.split(r"(?<=[.!?])\s+", prose)
    for s in sentences:
        nums = NUMBER.findall(s)
        if not nums:
            continue
        if facts is not None:
            missing = [n for n in nums if re.sub(r"[\s,]", "", n).lower() not in re.sub(r"[\s,]", "", facts).lower()]
            for n in missing:
                findings.append(f"unsupported  number {n!r} not in fact sheet: {s.strip()[:80]!r}")
        elif not CITATION_NEAR.search(s):
            findings.append(f"unsourced    {nums[0]!r} with no source cue in sentence: {s.strip()[:80]!r}")
    for f in findings:
        print(f"FLAG  {f}")
    print(f"summary: {len(findings)} flag(s); keep what the evidence supports, cut or soften the rest")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
