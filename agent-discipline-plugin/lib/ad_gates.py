"""Gates and observability: completion-gate (S7/P4), tool-output-trimmer (P6), tool log, provenance-log (S10/P8)."""
import os, re, sys, json
from ad_core import (state_dir, now, load_json, save_json, append_line, read_text, sha256_text, read_hook_input,
                     stop_block, allow, log_tool, tool_command)

DONE_RE = re.compile(r"\b(done|complete[d]?|finished|fixed|resolved|passes|passing|all tests pass|works now|ready for review|implemented)\b", re.I)
EVIDENCE_FIELDS = ["acceptance", "command", "output", "diff", "not verified"]

def find_evidence_block(text):
    """An evidence block has the five labelled lines (any order, case-insensitive). Returns dict or None."""
    found = {}
    for f in EVIDENCE_FIELDS:
        m = re.search(rf"(?im)^\W*(?:{f}|{f.replace(' ', '[ -]')})(?:\s+(?:criteria|run|ran|summary))?\s*[:：]\s*(.+)$", text)
        if m: found[f] = m.group(1).strip()
    return found if len(found) == len(EVIDENCE_FIELDS) else None

def commands_in_log():
    cmds = []
    for l in read_text("toollog.jsonl").splitlines():
        try: cmds.append(json.loads(l).get("cmd") or "")
        except Exception: pass
    return cmds

def completion_gate_decide(last_message, strict=True):
    """Return block reason or None. Checks: (a) claim of done needs evidence block; (b) quoted command appeared in tool log."""
    if not last_message or not DONE_RE.search(last_message): return None
    ev = find_evidence_block(last_message)
    if not ev:
        return ("completion-gate: you claimed completion without an evidence block. Add, in this order: "
                "`Acceptance:` what counts as done · `Command:` exactly what you ran · `Output:` quoted result (not paraphrased) · "
                "`Diff:` files changed · `Not verified:` what you did not check. If nothing was run, say so and run it.")
    cmd = ev["command"].strip("`").strip()
    if strict and cmd and cmd.lower() not in ("none", "n/a", "-"):
        logged = commands_in_log()
        if logged and not any(cmd[:40] in c or c[:40] in cmd for c in logged if c):
            return (f"completion-gate: the evidence block cites `{cmd[:80]}` but no such command appears in this session's tool log "
                    f"({len(logged)} calls logged). Run it now and quote the real output, or change the claim.")
    if re.search(r"(?i)^\W*output\s*:\s*(it worked|success|passed|ok|fine)\W*$", last_message, re.M):
        return "completion-gate: `Output:` must quote the actual tool output, not a paraphrase like 'passed'."
    return None

def last_assistant_text(inp):
    """A Stop hook input may give transcript_path; read the last assistant message. Fallback: inp['last_message']."""
    if inp.get("last_message"): return inp["last_message"]
    tp = inp.get("transcript_path")
    if tp and os.path.isfile(tp):
        try:
            txt = ""
            for line in reversed(open(tp, encoding="utf-8").read().splitlines()):
                try: rec = json.loads(line)
                except Exception: continue
                if rec.get("type") == "assistant" or (rec.get("message") or {}).get("role") == "assistant":
                    msg = rec.get("message") or rec
                    content = msg.get("content")
                    if isinstance(content, list):
                        txt = "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
                    else: txt = str(content or "")
                    if txt.strip(): return txt
        except Exception: pass
    return ""

def hook_completion_gate():
    inp = read_hook_input()
    if inp.get("stop_hook_active"): sys.exit(0)  # never loop forever
    reason = completion_gate_decide(last_assistant_text(inp), strict=os.environ.get("AD_GATE_STRICT", "1") == "1")
    stop_block(reason) if reason else sys.exit(0)

# ---------------- tool-output trimmer ----------------
def trim_output(text, tool="", limit=int(os.environ.get("AD_TRIM_CHARS", "6000"))):
    """Structure-aware trim. Returns (trimmed_text, kind). Full text is stored by the caller."""
    if len(text) <= limit: return text, "passthrough"
    lines = text.splitlines()
    # test output -> failures only
    if re.search(r"(?m)^(FAILED|ERROR|failed|error\[|AssertionError|Traceback)", text) and re.search(r"\b(passed|failed|tests?)\b", text):
        keep = [l for l in lines if re.search(r"(FAIL|ERROR|Error|assert|Traceback|^\s+File |passed|failed|summary|short test)", l)]
        out = "\n".join(keep[:200])
        return out[:limit] + f"\n[trimmed: failures only; {len(lines)} lines total]", "test-failures"
    # grep-like -> file:line only
    if sum(1 for l in lines[:50] if re.match(r"^[^\s:]+:\d+[:-]", l)) > 25:
        keep = sorted({re.match(r"^([^\s:]+:\d+)", l).group(1) for l in lines if re.match(r"^([^\s:]+:\d+)", l)})
        return "\n".join(keep[:300]) + f"\n[trimmed: {len(lines)} hits → file:line only]", "grep"
    # JSON -> shape + sample
    s = text.lstrip()
    if s[:1] in "[{":
        try:
            data = json.loads(s)
            def shape(v, d=0):
                if d > 3: return "…"
                if isinstance(v, dict): return {k: shape(x, d + 1) for k, x in list(v.items())[:12]}
                if isinstance(v, list): return [shape(v[0], d + 1), f"… {len(v)} items"] if v else []
                return type(v).__name__
            return json.dumps(shape(data), indent=1)[:limit] + "\n[trimmed: JSON shape; full output stored]", "json"
        except Exception: pass
    # log / generic -> head + tail
    head, tail = lines[:60], lines[-40:]
    return "\n".join(head) + f"\n… [{len(lines) - 100} lines omitted] …\n" + "\n".join(tail), "head-tail"

def store_full_output(text):
    key = sha256_text(text)[:16]
    p = os.path.join(state_dir(), "outputs", key + ".txt")
    if not os.path.exists(p):
        with open(p, "w", encoding="utf-8") as f: f.write(text)
    return p

def hook_log_and_trim():
    """PostToolUse: log the call; if the response is huge, store it and tell the model where it is + a trimmed view."""
    inp = read_hook_input()
    resp = inp.get("tool_response")
    s = resp if isinstance(resp, str) else (json.dumps(resp) if resp is not None else "")
    log_tool(inp)
    if len(s) > int(os.environ.get("AD_TRIM_CHARS", "6000")):
        p = store_full_output(s)
        trimmed, kind = trim_output(s, inp.get("tool_name") or "")
        allow(f"tool-output-trimmer ({kind}): full output ({len(s)} chars) saved to {p}. Work from this view; grep the file for specifics.\n{trimmed}",
              event="PostToolUse")
    sys.exit(0)

# ---------------- provenance ----------------
def provenance_add(section, source, quote="", confidence="probable"):
    if confidence not in ("established", "probable", "contested", "single-source", "unknown"):
        raise SystemExit("confidence must be established|probable|contested|single-source|unknown")
    append_line("provenance.jsonl", json.dumps({"ts": now(), "section": section, "source": source, "quote": quote[:400], "confidence": confidence}))
    return "provenance recorded"

def provenance_show(section=None):
    rows = []
    for l in read_text("provenance.jsonl").splitlines():
        try: r = json.loads(l)
        except Exception: continue
        if section is None or r["section"] == section: rows.append(r)
    if not rows: return "(no provenance recorded)"
    out = ["| section | source | confidence | quote |", "|---|---|---|---|"]
    for r in rows: out.append(f"| {r['section']} | {r['source']} | {r['confidence']} | {r['quote'][:80]} |")
    return "\n".join(out)

def provenance_audit(deliverable_path):
    """Which sections of a Markdown deliverable have no provenance rows?"""
    txt = open(deliverable_path, encoding="utf-8").read()
    secs = re.findall(r"(?m)^#{1,4}\s+(.+)$", txt)
    have = {json.loads(l)["section"] for l in read_text("provenance.jsonl").splitlines() if l.strip()}
    missing = [s for s in secs if s.strip() not in have]
    return "all sections have provenance" if not missing else "sections without provenance:\n- " + "\n- ".join(missing)
