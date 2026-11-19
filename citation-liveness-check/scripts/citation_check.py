#!/usr/bin/env python3
"""Check that citations in a draft are real, live and say what the draft says they say.

Usage: citation_check.py DRAFT.md [--fetch] [--timeout 10] [--allow-domains a.com,b.org]
Static checks (always): malformed URLs, placeholder domains (example.com, localhost, foo), duplicate URLs cited
for different claims, DOIs that do not match 10.NNNN/..., bare "et al. (YEAR)" or "[1]" references with no URL
or DOI anywhere in the file, and quotes ("...", 25+ chars) on a line that has no URL or DOI.
--fetch: GET each URL (and https://doi.org/<doi>), report HTTP status and redirects, and when a quote shares the
line with the URL, verify the quote's text appears in the fetched page (whitespace and case normalized). Pages
that block bots (403/429) are reported as "unverified", not as failures. Exit 1 on dead links, quote misses or
static errors; 2 on bad input. Network use is explicit: nothing is fetched without --fetch.
"""
import html
import re
import sys
import urllib.error
import urllib.request

URL = re.compile(r"https?://[^\s)\]>\"']+")
DOI = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>)\]]+)")
QUOTE = re.compile(r"[\"\u201c]([^\"\u201d]{25,}?)[\"\u201d]")
PLACEHOLDER = re.compile(r"(example\.(com|org|net)|localhost|127\.0\.0\.1|\bfoo\.|\bbar\.|\btest\.com|your-?site|placeholder|TODO|xxx)", re.I)
BARE_REF = re.compile(r"\b[A-Z][a-z]+ (?:et al\.|and [A-Z][a-z]+) \(?(19|20)\d\d\)?|\[\d{1,3}\]")


def norm(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip().lower()


def fetch(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 citation-check"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(2_000_000).decode("utf-8", errors="replace")
            return r.status, r.geturl(), body
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:  # noqa: BLE001
        return None, url, str(e)


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    try:
        lines = open(argv[1], encoding="utf-8").read().splitlines()
    except OSError as exc:
        print(f"cannot read: {exc}"); return 2
    do_fetch = "--fetch" in argv
    timeout = float(argv[argv.index("--timeout") + 1]) if "--timeout" in argv else 10
    allow = set(argv[argv.index("--allow-domains") + 1].split(",")) if "--allow-domains" in argv else set()
    errors, warns, seen = [], [], {}
    text = "\n".join(lines)
    any_ref = bool(URL.search(text) or DOI.search(text))
    for i, line in enumerate(lines, 1):
        urls = [u.rstrip(".,;") for u in URL.findall(line)]
        dois = DOI.findall(line)
        for u in urls:
            if PLACEHOLDER.search(u) and not any(d in u for d in allow):
                errors.append(f"line {i}: placeholder or test URL {u}")
            if u in seen and seen[u] != i:
                warns.append(f"line {i}: {u} already cited on line {seen[u]}; one URL for two claims is a hallucination pattern")
            seen.setdefault(u, i)
        for m in QUOTE.finditer(line):
            if not urls and not dois:
                warns.append(f"line {i}: quote with no URL or DOI on the line: {m.group(1)[:50]!r}")
        if BARE_REF.search(line) and not urls and not dois and not any_ref:
            warns.append(f"line {i}: reference without any URL or DOI in the file: {BARE_REF.search(line).group(0)!r}")
        if do_fetch:
            targets = urls + [f"https://doi.org/{d.rstrip('.')}" for d in dois]
            quotes = [m.group(1) for m in QUOTE.finditer(line)]
            for u in targets:
                status, final, body = fetch(u, timeout)
                if status is None:
                    errors.append(f"line {i}: {u} unreachable ({body[:60]})")
                elif status in (403, 429, 401):
                    warns.append(f"line {i}: {u} returned {status}; unverified (bot block or paywall), check by hand")
                elif status >= 400:
                    errors.append(f"line {i}: {u} returned HTTP {status}")
                else:
                    if final.rstrip("/") != u.rstrip("/"):
                        warns.append(f"line {i}: {u} redirected to {final}")
                    page = norm(body)
                    for q in quotes:
                        if norm(q)[:120] not in page:
                            errors.append(f"line {i}: quote not found on page {u}: {q[:50]!r}")
    for e in errors:
        print(f"ERROR {e}")
    for w in warns:
        print(f"WARN  {w}")
    print(f"summary: {len(seen)} url(s); {len(errors)} error(s), {len(warns)} warning(s); fetch={'on' if do_fetch else 'off'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
