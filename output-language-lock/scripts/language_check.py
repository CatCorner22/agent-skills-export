#!/usr/bin/env python3
"""Check that a model answer is written in the target language (by script), ignoring code blocks.

Usage: language_check.py TEXT_FILE --target zh|ja|ko|en|ru|ar|he|th|hi [--min-share 0.9]
Exit 0 = target script share >= min-share, 1 = below, 2 = bad input.
"""
import re
import sys
import unicodedata

SCRIPTS = {
    "zh": ("CJK UNIFIED", "CJK"), "ja": ("HIRAGANA", "KATAKANA", "CJK UNIFIED"), "ko": ("HANGUL",),
    "en": ("LATIN",), "ru": ("CYRILLIC",), "ar": ("ARABIC",), "he": ("HEBREW",), "th": ("THAI",), "hi": ("DEVANAGARI",),
}


def strip_code(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`\n]+`", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    return text


def script_counts(text):
    counts = {}
    for ch in text:
        if not ch.isalpha():
            continue
        try:
            name = unicodedata.name(ch)
        except ValueError:
            continue
        key = name.split(" ")[0] if not name.startswith("CJK") else "CJK UNIFIED"
        if name.startswith("LATIN"):
            key = "LATIN"
        counts[key] = counts.get(key, 0) + 1
    return counts


def main(argv):
    if len(argv) < 2 or "--target" not in argv:
        print(__doc__)
        return 2
    target = argv[argv.index("--target") + 1]
    if target not in SCRIPTS:
        print(f"unknown target {target}; choose from {sorted(SCRIPTS)}")
        return 2
    min_share = float(argv[argv.index("--min-share") + 1]) if "--min-share" in argv else 0.9
    try:
        text = open(argv[1], encoding="utf-8").read()
    except OSError as exc:
        print(f"cannot read: {exc}")
        return 2
    counts = script_counts(strip_code(text))
    total = sum(counts.values())
    if total == 0:
        print("no letters found outside code blocks")
        return 2
    want = SCRIPTS[target]
    hit = sum(v for k, v in counts.items() if any(k.startswith(w) for w in want))
    share = hit / total
    print(f"target {target}: {share:.1%} of letters in target script ({hit}/{total})")
    for k, v in sorted(counts.items(), key=lambda kv: -kv[1])[:5]:
        print(f"  {k}: {v}")
    if share < min_share:
        print(f"FAIL below {min_share:.0%}; the answer drifted to another language")
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
