#!/usr/bin/env python3
"""Recompute arithmetic stated in a draft and flag mismatches.

Usage: recompute_check.py DRAFT.md [--tolerance 0.01]
Checks: inline equations "a + b = c", "a - b = c", "a x b = c", "a / b = c" (numbers may carry $, %, commas, k/M/B
suffixes); percentage statements "X% of Y is/= Z" and "Z is X% of Y"; "from A to B, a change of C" and "A to B (+C%)";
markdown tables whose last row is Total/Sum/Subtotal (per numeric column); date spans "from YYYY-MM-DD to
YYYY-MM-DD (N days)". Tolerance is relative (default 1%) or absolute 1 unit for integers, whichever is larger,
so rounded figures pass. Exit 1 on a mismatch, 2 on bad input. Heuristic: read each flagged line.
"""
import datetime as dt
import re
import sys

NUM = r"[-+]?\$?\s?\d[\d,]*(?:\.\d+)?\s?(?:%|k|K|M|B|bn|m|million|billion|thousand)?"
MULT = {"k": 1e3, "K": 1e3, "thousand": 1e3, "M": 1e6, "m": 1e6, "million": 1e6, "B": 1e9, "bn": 1e9, "billion": 1e9}


def num(s):
    s = s.strip().replace("$", "").replace(",", "").replace(" ", "")
    pct = s.endswith("%")
    s = s.rstrip("%")
    mult = 1.0
    for suf in sorted(MULT, key=len, reverse=True):
        if s.endswith(suf):
            mult = MULT[suf]; s = s[: -len(suf)]; break
    try:
        return float(s) * mult, pct
    except ValueError:
        return None, pct


def close(a, b, tol):
    return abs(a - b) <= max(tol * max(abs(a), abs(b)), 1.0 if float(a).is_integer() and float(b).is_integer() else 0.0)


def check_line(line, tol, out, i):
    for m in re.finditer(rf"({NUM})\s*([+\-xX×*/÷])\s*({NUM})\s*(?:=|equals|is)\s*({NUM})", line):
        a, _ = num(m.group(1)); b, _ = num(m.group(3)); c, _ = num(m.group(4))
        if None in (a, b, c):
            continue
        op = m.group(2)
        try:
            r = a + b if op == "+" else a - b if op == "-" else a * b if op in "xX×*" else a / b
        except ZeroDivisionError:
            continue
        if not close(r, c, tol):
            out.append(f"line {i}: {m.group(0).strip()} -> recomputed {r:g}")
    for m in re.finditer(rf"({NUM})\s*(?:%|percent)\s+of\s+({NUM})\s*(?:is|=|equals)\s*({NUM})", line, re.I):
        p, _ = num(m.group(1)); y, _ = num(m.group(2)); z, _ = num(m.group(3))
        if None not in (p, y, z) and not close(p / 100 * y, z, tol):
            out.append(f"line {i}: {m.group(0).strip()} -> recomputed {p / 100 * y:g}")
    for m in re.finditer(rf"({NUM})\s+is\s+({NUM})\s*(?:%|percent)\s+of\s+({NUM})", line, re.I):
        z, _ = num(m.group(1)); p, _ = num(m.group(2)); y, _ = num(m.group(3))
        if None not in (p, y, z) and y and not close(z / y * 100, p, tol):
            out.append(f"line {i}: {m.group(0).strip()} -> recomputed {z / y * 100:g}%")
    for m in re.finditer(rf"from\s+({NUM})\s+to\s+({NUM})\s*[,(]?\s*(?:a |an )?(?:change|increase|decrease|drop|rise|gain|up|down|growth)\s+of\s+({NUM})", line, re.I):
        a, _ = num(m.group(1)); b, _ = num(m.group(2)); c, cpct = num(m.group(3))
        if None in (a, b, c):
            continue
        exp = (b - a) / a * 100 if cpct and a else b - a
        if not close(abs(exp), abs(c), tol):
            out.append(f"line {i}: {m.group(0).strip()} -> recomputed {exp:g}{'%' if cpct else ''}")
    for m in re.finditer(r"from\s+(\d{4}-\d\d-\d\d)\s+(?:to|until|through)\s+(\d{4}-\d\d-\d\d)\s*\(?\s*(\d+)\s*days?", line, re.I):
        try:
            d = (dt.date.fromisoformat(m.group(2)) - dt.date.fromisoformat(m.group(1))).days
        except ValueError:
            continue
        if abs(d - int(m.group(3))) > 1:
            out.append(f"line {i}: {m.group(0).strip()} -> recomputed {d} days")


def check_tables(lines, tol, out):
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i]); i += 1
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in block if not re.match(r"^\s*\|?\s*:?-{2,}", r)]
            if len(rows) >= 3 and re.match(r"(total|sum|subtotal|grand total)", rows[-1][0], re.I):
                body, tot = rows[1:-1], rows[-1]
                for c in range(1, min(len(tot), min(len(r) for r in rows))):
                    vals = [num(r[c])[0] for r in body]
                    tv, _ = num(tot[c])
                    if tv is None or any(v is None for v in vals) or not vals:
                        continue
                    if not close(sum(vals), tv, tol):
                        out.append(f"table ending line {i}: column {c} total {tot[c]} -> recomputed {sum(vals):g}")
        else:
            i += 1


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    tol = float(argv[argv.index("--tolerance") + 1]) if "--tolerance" in argv else 0.01
    try:
        lines = open(argv[1], encoding="utf-8").read().splitlines()
    except OSError as exc:
        print(f"cannot read: {exc}"); return 2
    out = []
    for i, line in enumerate(lines, 1):
        check_line(line, tol, out, i)
    check_tables(lines, tol, out)
    for f in out:
        print(f"MISMATCH {f}")
    print(f"summary: {len(out)} mismatch(es) in {len(lines)} line(s)")
    return 1 if out else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
