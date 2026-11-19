#!/usr/bin/env python3
"""Audit a unified diff for test gaming: deleted or skipped tests, weakened assertions, hard-coded answers.

Usage: test_tamper_check.py CHANGES.diff [--tests-glob test]
Exit 1 when tamper patterns are found, 2 on bad input. Heuristic; read the flagged hunks.
"""
import re
import sys

TEST_PATH = re.compile(r"(^|/)(tests?|spec|__tests__)(/|_|\.|$)|_test\.|\.test\.|\.spec\.", re.I)
SKIP = re.compile(r"^\+.*(@pytest\.mark\.skip|@unittest\.skip|\.skip\(|xit\(|xdescribe\(|test\.skip|@Ignore|@Disabled|pytest\.xfail|t\.Skip\()", re.M)
WEAKEN = re.compile(r"^\+.*(assert\s+True\b|assertTrue\(True\)|expect\(true\)|return\s+True\s*#|pass\s*#?\s*$|assert\s+.*\bor\s+True\b|try:\s*$)", re.M)
HARDCODE = re.compile(r"^\+.*(return\s+(\"[^\"]{1,40}\"|'[^']{1,40}'|\d+(\.\d+)?)\s*(#.*)?$|if\s+.*==\s*(\"|')?(test|expected|fixture))", re.M | re.I)
MOCK = re.compile(r"^\+.*(mock\.patch|monkeypatch\.setattr|jest\.mock\(|sinon\.stub|unittest\.mock)", re.M)


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    try:
        diff = open(argv[1], encoding="utf-8", errors="replace").read()
    except OSError as exc:
        print(f"cannot read: {exc}"); return 2
    files = re.split(r"^diff --git ", diff, flags=re.M)[1:]
    out = []
    for f in files:
        header = f.split("\n", 1)[0]
        m = re.search(r"b/(\S+)", header)
        path = m.group(1) if m else header
        is_test = bool(TEST_PATH.search(path))
        removed = sum(1 for ln in f.splitlines() if ln.startswith("-") and not ln.startswith("---"))
        added = sum(1 for ln in f.splitlines() if ln.startswith("+") and not ln.startswith("+++"))
        if "deleted file mode" in f and is_test:
            out.append(("error", f"{path}: test file deleted"))
        if is_test and removed > added + 5:
            out.append(("warn", f"{path}: test file shrank by {removed - added} lines"))
        if is_test:
            for rx, label in ((SKIP, "test skipped"), (WEAKEN, "assertion weakened")):
                for mm in rx.finditer(f):
                    out.append(("error", f"{path}: {label}: {mm.group(0).strip()[:80]}"))
            for mm in re.finditer(r"^-.*\bassert", f, re.M):
                out.append(("warn", f"{path}: assertion removed: {mm.group(0).strip()[:80]}"))
        else:
            for mm in HARDCODE.finditer(f):
                out.append(("warn", f"{path}: possible hard-coded expected value: {mm.group(0).strip()[:80]}"))
            for mm in MOCK.finditer(f):
                out.append(("info", f"{path}: mocking added in non-test code: {mm.group(0).strip()[:60]}"))
    for lvl, msg in out:
        print(f"{lvl.upper():5} {msg}")
    errors = sum(1 for lvl, _ in out if lvl == "error")
    print(f"summary: {len(files)} file(s), {errors} error(s), {len(out) - errors} other finding(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
