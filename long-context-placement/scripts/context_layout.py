#!/usr/bin/env python3
"""Check how a long prompt is laid out before sending it to any model.

Usage: context_layout.py REQUEST.json [--chunk-tokens 100000] [--window 200000]
REQUEST.json: {"messages": [...]} in OpenAI or Anthropic shape (string or block-list content). Tokens are
estimated at 4 characters per token. Findings: total estimate vs window; a single document larger than
--chunk-tokens (chunk it); the task or question stated only before a large document (repeat it after); instructions
or rules appearing only in the middle; the last message not the user turn; dynamic fields (dates, ids) in the first
message (prefix cache); more than ~40% of the prompt in the middle third with no section headers (lost-in-the-
middle); and many small documents without labels. Exit 1 on findings, 2 on bad input.
"""
import json
import re
import sys

QUESTION = re.compile(r"\?\s*$|^(please|summarize|list|extract|answer|write|compare|find|explain|return)\b", re.I | re.M)
RULE = re.compile(r"\b(must|never|do not|don't|always|only|required|rule|format)\b", re.I)
DYNAMIC = re.compile(r"\b\d{4}-\d\d-\d\d[T ]\d\d:\d\d|\b(run|request|session)[_ -]?id\b|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}", re.I)
HEADER = re.compile(r"^(#{1,6} |<[a-z_]+[^>]*>|={3,}|-{3,}|\[[A-Z][^\]]{2,40}\]$)", re.M)


def text_of(m):
    c = m.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") in ("text", None))
    return ""


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    chunk = int(argv[argv.index("--chunk-tokens") + 1]) if "--chunk-tokens" in argv else 100000
    window = int(argv[argv.index("--window") + 1]) if "--window" in argv else 200000
    try:
        req = json.load(open(argv[1], encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read: {exc}"); return 2
    msgs = req.get("messages", req if isinstance(req, list) else [])
    if req.get("system") if isinstance(req, dict) else False:
        msgs = [{"role": "system", "content": req["system"] if isinstance(req["system"], str) else "\n".join(b.get("text", "") for b in req["system"])}] + msgs
    if not msgs:
        print("no messages"); return 2
    texts = [text_of(m) for m in msgs]
    toks = [len(t) // 4 for t in texts]
    total = sum(toks)
    findings = []
    print(f"messages: {len(msgs)}; estimated tokens: {total:,} ({total / window:.0%} of window {window:,})")
    for i, (m, t, n) in enumerate(zip(msgs, texts, toks)):
        print(f"  [{i}] {m.get('role'):9} ~{n:,} tok")
    if total > window:
        findings.append(f"prompt exceeds the window estimate; cut or chunk before sending")
    big = [i for i, n in enumerate(toks) if n > chunk]
    for i in big:
        findings.append(f"message {i} is ~{toks[i]:,} tokens; split into labeled chunks under {chunk:,} and process in passes, or retrieve the relevant parts")
    if msgs[-1].get("role") not in ("user", "tool"):
        findings.append("the last message is not the user turn; put the newest user turn (or tool result) last, models weight the end of the prompt most")
    doc_idx = [i for i, n in enumerate(toks) if n > 0.25 * total and n > 2000]
    for i in doc_idx:
        before = "\n".join(texts[:i]); after = "\n".join(texts[i + 1:])
        if QUESTION.search(before) and not QUESTION.search(after):
            findings.append(f"the task appears only before the large document in message {i}; restate the question and output format after it")
    rules_pos = [i for i, t in enumerate(texts) if RULE.search(t)]
    if rules_pos and all(0 < i < len(msgs) - 1 for i in rules_pos) and len(msgs) > 2:
        findings.append("rules/instructions appear only in middle messages; put them in the system prompt and repeat the critical ones at the end")
    if texts and DYNAMIC.search(texts[0]):
        findings.append("first message contains a timestamp or id; it breaks prefix caching on every provider, move it to the last message")
    if total > 20000:
        third = total // 3
        acc, mid = 0, 0
        for n in toks:
            lo, hi = acc, acc + n
            mid += max(0, min(hi, 2 * third) - max(lo, third))
            acc = hi
        headers = sum(len(HEADER.findall(t)) for t in texts)
        if mid / total > 0.4 and headers < 3:
            findings.append(f"{mid / total:.0%} of tokens sit in the middle third with {headers} section header(s); add labeled sections or an index so the model can locate content (lost-in-the-middle)")
    smalls = [i for i, n in enumerate(toks) if 500 < n < 0.25 * total and msgs[i].get("role") == "user"]
    if len(smalls) >= 5 and not all(re.match(r"^\s*(#|<|\[|Document|Source|File)", texts[i]) for i in smalls):
        findings.append(f"{len(smalls)} medium documents without a leading label; prefix each with a title/source line the model can cite")
    for f in findings:
        print(f"FINDING {f}")
    print(f"summary: {len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
