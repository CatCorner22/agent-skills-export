#!/usr/bin/env python3
"""Check a draft against a JSON style-rules file.

Usage: style_check.py DRAFT.md --rules style-rules.json
Rules keys: max_sentence_words, max_paragraph_sentences, banned_words, banned_patterns,
required_terms, preferred (map of bad -> good), passive_voice_max_share, forbid_first_person_plural.
Exit 0 = clean, 1 = violations, 2 = bad input. Prose only: fenced code is skipped.
"""
import json
import re
import sys

PASSIVE = re.compile(r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?\w+(?:ed|en)\b", re.I)
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(])")


def main(argv):
    if len(argv) < 2 or "--rules" not in argv:
        print(__doc__)
        return 2
    try:
        text = open(argv[1], encoding="utf-8").read()
        rules = json.load(open(argv[argv.index("--rules") + 1], encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read: {exc}")
        return 2
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    prose = re.sub(r"^\s*(#+ .*|\|.*\||[-*] .*|\d+\. .*)$", "", prose, flags=re.M)
    findings = []
    paras = [p.strip() for p in re.split(r"\n\s*\n", prose) if p.strip()]
    sentences = []
    for p in paras:
        sents = [s for s in SENT_SPLIT.split(p) if s.strip()]
        sentences += sents
        if rules.get("max_paragraph_sentences") and len(sents) > rules["max_paragraph_sentences"]:
            findings.append(f"paragraph with {len(sents)} sentences (max {rules['max_paragraph_sentences']}): {p[:60]!r}")
    mx = rules.get("max_sentence_words")
    for s in sentences:
        n = len(s.split())
        if mx and n > mx:
            findings.append(f"sentence of {n} words (max {mx}): {s[:70]!r}")
    low = prose.lower()
    for w in rules.get("banned_words", []):
        for m in re.finditer(rf"\b{re.escape(w.lower())}\b", low):
            ctx = prose[max(0, m.start() - 30):m.end() + 30].replace("\n", " ")
            fix = rules.get("preferred", {}).get(w)
            findings.append(f"banned word {w!r}{' -> ' + repr(fix) if fix else ''}: ...{ctx}...")
    for pat in rules.get("banned_patterns", []):
        for m in re.finditer(pat, prose, re.I):
            findings.append(f"banned pattern {pat!r}: {m.group(0)!r}")
    for term in rules.get("required_terms", []):
        if term.lower() not in low:
            findings.append(f"required term missing: {term!r}")
    if sentences and rules.get("passive_voice_max_share") is not None:
        passive = sum(1 for s in sentences if PASSIVE.search(s))
        share = passive / len(sentences)
        if share > rules["passive_voice_max_share"]:
            findings.append(f"passive voice in {share:.0%} of sentences (max {rules['passive_voice_max_share']:.0%}); heuristic")
    if rules.get("forbid_first_person_plural") and re.search(r"\b(we|our|us)\b", prose, re.I):
        findings.append("first-person plural (we/our/us) is forbidden by the rules")
    for f in findings:
        print(f"FAIL  {f}")
    print(f"summary: {len(sentences)} sentences checked, {len(findings)} violation(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
