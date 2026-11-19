#!/usr/bin/env python3
"""Redact personal data from text before it goes to a hosted model, with a local re-identification map.

Usage: pii_redact.py INPUT.txt [--out redacted.txt] [--map map.json] [--names names.txt] [--allow email,phone,...]
Detects emails, phone numbers, US SSNs, credit card numbers (Luhn-checked), IBANs, dates of birth (DOB/born/
birth date + date), street addresses (number + street word), IPv4 addresses, and any names listed in --names
(one per line; the script does not guess names). Each value becomes a stable token like [EMAIL_1]; the same value
gets the same token so the model can still reason about who is who. The map (token -> original) is written only
to --map, which must stay local. --allow skips categories you have a lawful basis to send. Exit 1 if anything was
redacted (so pipelines notice), 0 if clean, 2 on bad input.
"""
import json
import re
import sys

PATTERNS = [
    ("EMAIL", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("SSN", re.compile(r"\b(?!000|666|9\d\d)\d{3}-(?!00)\d{2}-(?!0000)\d{4}\b")),
    ("CARD", re.compile(r"\b(?:\d[ -]?){13,19}\b")),
    ("IBAN", re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b")),
    ("PHONE", re.compile(r"(?<![\w.-])(?:\+?\d{1,3}[ .-]?)?\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}\b")),
    ("DOB", re.compile(r"\b(?:DOB|date of birth|born(?: on)?|birth ?date)\s*[:\-]?\s*((?:\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4})|(?:\d{4}-\d\d-\d\d)|(?:[A-Z][a-z]+ \d{1,2}, \d{4}))", re.I)),
    ("ADDRESS", re.compile(r"\b\d{1,6} [A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+)? (?:Street|St\.?|Avenue|Ave\.?|Road|Rd\.?|Boulevard|Blvd\.?|Lane|Ln\.?|Drive|Dr\.?|Court|Ct\.?|Way|Place|Pl\.?)\b")),
    ("IP", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
]


def luhn(s):
    digits = [int(c) for c in re.sub(r"\D", "", s)]
    if len(digits) < 13:
        return False
    total, parity = 0, len(digits) % 2
    for i, d in enumerate(digits):
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    try:
        text = open(argv[1], encoding="utf-8").read()
    except OSError as exc:
        print(f"cannot read: {exc}"); return 2
    allow = set(a.upper() for a in argv[argv.index("--allow") + 1].split(",")) if "--allow" in argv else set()
    names = []
    if "--names" in argv:
        try:
            names = [n.strip() for n in open(argv[argv.index("--names") + 1], encoding="utf-8") if n.strip()]
        except OSError as exc:
            print(f"cannot read names: {exc}"); return 2
    mapping, counters, counts = {}, {}, {}

    def token(cat, value):
        key = (cat, value.strip().lower())
        if key not in mapping:
            counters[cat] = counters.get(cat, 0) + 1
            mapping[key] = f"[{cat}_{counters[cat]}]"
        counts[cat] = counts.get(cat, 0) + 1
        return mapping[key]

    for name in sorted(names, key=len, reverse=True):
        if "NAME" in allow:
            break
        text, n = re.subn(re.escape(name), lambda m, nm=name: token("NAME", nm), text)
    for cat, rx in PATTERNS:
        if cat in allow:
            continue
        def repl(m, cat=cat):
            val = m.group(1) if cat == "DOB" else m.group(0)
            if cat == "CARD" and not luhn(val):
                return m.group(0)
            if cat == "DOB":
                return m.group(0).replace(val, token(cat, val))
            return token(cat, val)
        text = rx.sub(repl, text)
    for cat, n in sorted(counts.items()):
        print(f"REDACTED {cat}: {n} occurrence(s), {counters[cat]} distinct")
    if "--map" in argv:
        json.dump({v: k[1] for k, v in mapping.items()}, open(argv[argv.index("--map") + 1], "w", encoding="utf-8"), indent=2)
        print(f"map written to {argv[argv.index('--map') + 1]} (keep local; never send)")
    if "--out" in argv:
        open(argv[argv.index("--out") + 1], "w", encoding="utf-8").write(text)
        print(f"wrote {argv[argv.index('--out') + 1]}")
    else:
        sys.stdout.write(text)
    print(f"summary: {sum(counts.values())} redaction(s) in {len(counts)} categor(ies)")
    return 1 if counts else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
