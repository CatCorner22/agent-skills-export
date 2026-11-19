#!/usr/bin/env python3
"""Watchlist scanner for Chicken Little Overwatch.

Searches for the words and patterns that the writing standard tells the reviewer to
inspect: banned or risky modal verbs, vague time words, ambiguity triggers (R1-R30),
look-alike medical words (R5), Joint Commission "Do Not Use" items (R6), dose-format
errors (R14), 1 space after a sentence (Typography, a house standard), and long
sentences (S5). Every hit is a prompt to decide, not a verdict.

Usage:  python3 watchlist_scan.py [--limit N] [--no-length] [--no-spacing] [--strict] [--fail] FILE [FILE ...]
        ('-' reads standard input)
Exit:   0 by default (the scan informs; the reviewer decides); 1 with --fail when any hit
        appears; 2 when a file could not be read.
"""
import argparse
import re
import sys

WORDS = {
    "R1/lexicon": r"shall|should|consider|can|cannot|need to|needs to|is to|agrees to|is required to|is responsible for|will be expected to",
    "R9 and/or": r"and/or",
    "R28 slash": r"\b[A-Za-z]+/[A-Za-z]+\b",
    "R13 time": r"within|upon|until|by\s+(?:the\s+)?(?:end|close|date)|between|business day|periodically|daily|twice a day|at least",
    "R16 exceptions": r"provided that|notwithstanding|subject to|may\b[^.]{0,40}\bonly\b",
    "R7/R18 references": r"herein|said|such|the foregoing|the same|above|below",
    "R15 examples": r"such as|e\.g\.|i\.e\.|etc\.|including",
    "R21 respectively": r"respectively",
    "R27 earlier/later": r"whichever",
    "R10/R24 quantifiers": r"\bany\b|\beach\b|\ball\b|\bevery\b",
    "R12 negation": r"unless|not\s+\w+\s+unless|cannot|never|no\s+longer",
    "R25 notice": r"notice|notify",
    "R26 may require": r"may require|may ask",
    "Vague standard": r"sole discretion|satisfactory|acceptable to|good faith|best efforts|reasonable|appropriate|adequate|as clinically indicated|promptly|immediately|as soon as possible|right away|timely|regularly|frequently|significant|substantial|material|soon|normal|usual|as needed|as directed|PRN|mild|moderate|severe|very|extremely",
    "Please": r"please",
    "R17 possibility": r"likely|unlikely|rare|common|very common",
}
LOOKALIKES = r"negative|positive|unremarkable|impressive|progressing|stable|occult|NPO|febrile|acute|chronic|discharge|culture|tolerate|compliance"
DO_NOT_USE = [
    ("R6 Do Not Use: U/IU after a number", r"\b\d+(?:\.\d+)?\s?(?:U|IU)\b"),
    ("R6 Do Not Use: QD/QOD", r"\b(?:Q\.O\.D\.|Q\.D\.|QOD|QD)(?!\w)"),
    ("R6 Do Not Use: MS/MSO4/MgSO4", r"\b(?:MS|MSO4|MgSO4)\b"),
    ("R14 trailing zero", r"\b\d+\.0\s?(?:mg|mcg|g|mL|units?)\b"),
    ("R14 missing leading zero", r"(?<![\d.])\.\d+\s?(?:mg|mcg|g|mL|units?)\b"),
]
ABBREVIATIONS = {"dr", "mr", "mrs", "ms", "prof", "st", "vs", "no", "u.s", "e.g", "i.e", "etc", "inc", "jr", "sr"}
ONE_SPACE = re.compile(r"(\S*)[.?!][\"\u201d\u2019)]? (?=[\"\u201c\u2018(]?[A-Z0-9])")
SENTENCE = re.compile(r"(?<=[.?!])\s+(?=[A-Z0-9\"\u201c(])")
EXACT = ("R9 and/or", "R28 slash", "R16 exceptions")
WORD_RX = [(label, re.compile(pattern if label in EXACT else rf"\b(?:{pattern})\b", re.I)) for label, pattern in WORDS.items()]
LOOK_RX = re.compile(rf"\b(?:{LOOKALIKES})\b", re.I)
DNU_RX = [(label, re.compile(pattern)) for label, pattern in DO_NOT_USE]


# --- Markdown reader (shared verbatim by av_scan.py and watchlist_scan.py; tests check that the copies match) ---
MARK = re.compile(r"<!--\s*(/?)av:(verbatim|mention)\s*-->")
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
YAML_LINE = re.compile(r"^(?:\s*$|\s*#|[A-Za-z0-9_-]+\s*:|\s+\S|\s*-\s)")
BLOCK_START = re.compile(r"^\s*(?:#{1,6}\s|\||[-*+]\s|\d+[.)]\s|>)")
SINGLE_LINE = re.compile(r"^\s*(?:#{1,6}\s|\|)")


class InputError(Exception):
    """A file that the scanner cannot read as UTF-8 text."""


def read_lines(path):
    """Return the lines of PATH ('-' means standard input) without line endings."""
    if path == "-":
        return sys.stdin.read().lstrip("\ufeff").splitlines()
    try:
        with open(path, encoding="utf-8-sig") as handle:
            return handle.read().splitlines()
    except FileNotFoundError:
        raise InputError(f"{path}: no such file")
    except IsADirectoryError:
        raise InputError(f"{path}: is a folder; pass the files inside it")
    except UnicodeDecodeError as error:
        raise InputError(f"{path}: not UTF-8 text (byte {error.start}); convert it to UTF-8 first")
    except OSError as error:
        raise InputError(f"{path}: {error.strerror}")


def front_matter_end(lines):
    """Return the index of the closing front-matter line, or -1 if the file has no front matter."""
    if not lines or lines[0].strip() != "---":
        return -1
    for index in range(1, len(lines)):
        if lines[index].strip() in ("---", "..."):
            return index
        if not YAML_LINE.match(lines[index]):
            return -1
    return -1


def fence_lines(lines, start):
    """Return the set of line indexes inside closed code fences, and the index of each unclosed opener."""
    inside, unclosed, index = set(), [], start
    while index < len(lines):
        opener = FENCE.match(lines[index])
        if not opener:
            index += 1
            continue
        mark = opener.group(1)
        close = next((j for j in range(index + 1, len(lines))
                      if re.match(rf"^\s{{0,3}}{re.escape(mark[0])}{{{len(mark)},}}\s*$", lines[j])), None)
        if close is None:
            unclosed.append(index)
            index += 1
            continue
        inside.update(range(index, close + 1))
        index = close + 1
    return inside, unclosed


def paragraphs(lines, include_code=False):
    """Yield (zone, first_line_number, text) for each paragraph, and collect warnings.

    Zone is TEXT, VERBATIM, or MENTION. A paragraph joins wrapped lines with a newline,
    so a pattern can match across a line break.
    """
    warnings = []
    end = front_matter_end(lines)
    if lines and lines[0].strip() == "---" and end == -1:
        warnings.append("line 1: '---' opens no valid front matter; the scanner reads the file as text")
    start = end + 1
    fenced, unclosed = (set(), []) if include_code else fence_lines(lines, start)
    for index in unclosed:
        warnings.append(f"line {index + 1}: code fence never closes; the scanner reads the rest as text")
    out, zone, buffer, first = [], "TEXT", [], 0

    def flush():
        if buffer:
            out.append((zone, first, "\n".join(buffer)))
        buffer.clear()

    for index in range(start, len(lines)):
        line = lines[index]
        marker = MARK.search(line)
        if marker:
            flush()
            closing, kind = marker.group(1), marker.group(2).upper()
            if closing and zone != kind:
                warnings.append(f"line {index + 1}: closing av:{kind.lower()} marker has no matching opener")
            if not closing and zone != "TEXT":
                warnings.append(f"line {index + 1}: av:{kind.lower()} opens inside an open av:{zone.lower()} zone")
            zone = "TEXT" if closing else kind
            continue
        if index in fenced or not line.strip() or line.lstrip().startswith("<!--") or re.match(r"^\s*\|?\s*:?-{3,}", line):
            flush()
            continue
        if BLOCK_START.match(line):
            flush()
        if not buffer:
            first = index + 1
        buffer.append(line)
        if SINGLE_LINE.match(line):
            flush()
    flush()
    if zone != "TEXT":
        warnings.append(f"end of file: av:{zone.lower()} zone never closes")
    return out, warnings, zone != "TEXT"


def line_of(first, text, offset):
    return first + text.count("\n", 0, offset)
# --- end Markdown reader ---


def scan_text(first, text, limit, check_length, check_spacing):
    """Return (line, label, fragment) hits for one paragraph."""
    plain = re.sub(r"[*_`]", "", text)
    hits = []
    for label, rx in WORD_RX:
        hits += [(line_of(first, plain, m.start()), label, m.group(0)) for m in rx.finditer(plain)]
    hits += [(line_of(first, plain, m.start()), "R5 look-alike word", m.group(0)) for m in LOOK_RX.finditer(plain)]
    for label, rx in DNU_RX:
        hits += [(line_of(first, plain, m.start()), label, m.group(0)) for m in rx.finditer(plain)]
    if check_spacing:
        for m in ONE_SPACE.finditer(plain):
            if m.group(1).lower().strip("\"\u201c(") in ABBREVIATIONS:
                continue
            context = " ".join(plain[max(0, m.start() - 12): m.end() + 6].split())
            hits.append((line_of(first, plain, m.start()), "Typography: 1 space after sentence (house)", context))
    if check_length:
        offset = 0
        for sentence in SENTENCE.split(plain):
            start = plain.find(sentence, offset)
            offset = max(start, offset)
            words = len(re.findall(r"[A-Za-z0-9'\u2019-]+", sentence))
            if words > limit:
                hits.append((line_of(first, plain, offset), f"S5 length {words} > {limit}", " ".join(sentence[:60].split()) + "..."))
    return hits


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("files", nargs="+", help="Markdown or text files; '-' reads standard input")
    parser.add_argument("--limit", type=int, default=25, help="sentence word limit for S5; use 15 for patient instructions")
    parser.add_argument("--no-length", action="store_true", help="skip the sentence-length check")
    parser.add_argument("--no-spacing", action="store_true", help="skip the 2-spaces-after-a-sentence house check")
    parser.add_argument("--strict", action="store_true", help="also scan av:mention and av:verbatim zones")
    parser.add_argument("--fail", action="store_true", help="exit 1 when any hit appears")
    args = parser.parse_args(argv)
    if args.limit < 1:
        parser.error("--limit must be 1 or more")
    total = failed = 0
    for path in args.files:
        try:
            lines = read_lines(path)
        except InputError as error:
            print(f"ERROR {error}", file=sys.stderr)
            failed += 1
            continue
        found, warnings, _ = paragraphs(lines)
        for warning in warnings:
            print(f"{path}: WARNING {warning}", file=sys.stderr)
        hits = []
        for zone, first, text in found:
            if zone != "TEXT" and not args.strict:
                continue
            hits += scan_text(first, text, args.limit, not args.no_length, not args.no_spacing)
        for number, label, fragment in sorted(set(hits)):
            print(f"{path}:{number}: [{label}] {fragment}")
            total += 1
    print(f"hits={total} unreadable={failed}", file=sys.stderr)
    if failed:
        return 2
    return 1 if (args.fail and total) else 0


if __name__ == "__main__":
    sys.exit(main())
