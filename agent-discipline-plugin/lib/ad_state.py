"""State layer: read manifest (S2/P2), autonomy ledger (S6), checkpoint + reinjection (S5/P5)."""
import os, re, json, sys
from ad_core import (state_dir, now, sha256_file, load_json, save_json, append_line, read_text,
                     human_size, read_hook_input, allow, emit_context, tool_command)

FETCH_RE = re.compile(r"\b(curl|wget|aria2c|scp|rsync|gsutil cp|aws s3 cp|gdown|git clone|pip download|Invoke-WebRequest)\b", re.I)
URL_RE = re.compile(r"https?://[^\s'\"`<>]+")

# ---------------- manifest ----------------
def manifest_record(path, ranges=None, summary=None, source="read"):
    m = load_json("manifest.json", {})
    key = os.path.abspath(path) if os.path.exists(path) else path
    ent = m.get(key, {"ranges": [], "summary": "", "source": source, "first_ts": now()})
    if os.path.exists(key) and os.path.isfile(key):
        ent["size"] = os.path.getsize(key)
        ent["sha256"] = sha256_file(key)
    if ranges:
        for r in ranges:
            if r not in ent["ranges"]: ent["ranges"].append(r)
    if summary: ent["summary"] = summary[:600]
    ent["ts"] = now(); ent["reads"] = ent.get("reads", 0) + 1
    m[key] = ent
    save_json("manifest.json", m)
    return key, ent

def manifest_lookup(target):
    """Match by absolute path, basename, or URL filename. Returns (key, entry) or (None, None)."""
    m = load_json("manifest.json", {})
    if not target: return None, None
    cands = {os.path.abspath(target), target, os.path.basename(target.rstrip("/"))}
    for k, e in m.items():
        if k in cands or os.path.basename(k) in cands or e.get("url") == target:
            return k, e
    return None, None

def manifest_check(path):
    """Return a status line the model can act on."""
    key, ent = manifest_lookup(path)
    if not ent: return "NOT IN MANIFEST — first read; record it afterwards."
    changed = ""
    if os.path.isfile(key):
        changed = "UNCHANGED" if sha256_file(key) == ent.get("sha256") else "CHANGED since last read"
    rngs = ", ".join(f"{a}-{b}" for a, b in ent.get("ranges", [])[:8]) or "whole file"
    return (f"{changed or 'KNOWN'} | {human_size(ent.get('size', 0))} | read {ent.get('reads', 1)}x, last {ent.get('ts')} | "
            f"ranges: {rngs} | summary: {ent.get('summary') or '(none recorded)'}")

def manifest_summary(max_items=40):
    m = load_json("manifest.json", {})
    if not m: return ""
    items = sorted(m.items(), key=lambda kv: kv[1].get("ts", ""), reverse=True)[:max_items]
    lines = ["## Read manifest (what you already read — do not re-read unchanged files; use ranges)"]
    for k, e in items:
        lines.append(f"- {k} ({human_size(e.get('size', 0))}, {e.get('reads', 1)}x, {e.get('ts', '')[:16]}): {e.get('summary') or 'no summary'}")
    return "\n".join(lines)

# ---------------- ledger ----------------
LEDGER_KINDS = ("GRANT", "FORBID", "STOP", "ACCEPT", "SCOPE", "NOTE")

def ledger_add(kind, text):
    kind = kind.upper()
    if kind not in LEDGER_KINDS: raise SystemExit(f"kind must be one of {LEDGER_KINDS}")
    append_line("ledger.md", f"- {now()} {kind}: {text.strip()}")
    return f"{kind} recorded."

def ledger_entries():
    out = []
    for ln in read_text("ledger.md").splitlines():
        m = re.match(r"- (\S+) (GRANT|FORBID|STOP|ACCEPT|SCOPE|NOTE): (.*)", ln)
        if m: out.append({"ts": m.group(1), "kind": m.group(2), "text": m.group(3)})
    return out

def ledger_check(action):
    """Before asking permission: is this action already granted or forbidden? Keyword overlap, latest wins."""
    words = set(re.findall(r"[a-z0-9_./-]{3,}", action.lower()))
    best = None
    for e in ledger_entries():
        if e["kind"] not in ("GRANT", "FORBID"): continue
        ew = set(re.findall(r"[a-z0-9_./-]{3,}", e["text"].lower()))
        score = len(words & ew)
        if score and (best is None or score >= best[0]): best = (score, e)
    if not best: return "NO LEDGER ENTRY — if this is reversible, proceed and label the assumption; if confirm-first, ask once."
    e = best[1]
    verb = "ALREADY GRANTED — proceed; cite the ledger line, do not ask again" if e["kind"] == "GRANT" else "FORBIDDEN by ledger — do not do it"
    return f"{verb}: [{e['ts']}] {e['text']}"

def ledger_show():
    es = ledger_entries()
    if not es: return ""
    lines = ["## Autonomy ledger (standing permissions, limits, stop conditions, acceptance criteria)"]
    for e in es[-40:]: lines.append(f"- {e['kind']}: {e['text']}")
    return "\n".join(lines)

# ---------------- checkpoint + reinjection ----------------
def checkpoint_write(text):
    with open(os.path.join(state_dir(), "CHECKPOINT.md"), "w", encoding="utf-8") as f:
        f.write(f"# CHECKPOINT {now()}\n\n{text.strip()}\n")
    return "checkpoint written"

def reinject(budget_chars=6000):
    """Text to append to context on SessionStart / PostCompact: ledger + manifest + checkpoint, trimmed to budget (~1.5K tokens)."""
    parts = [p for p in (ledger_show(), read_text("CHECKPOINT.md").strip(), manifest_summary()) if p]
    if not parts: return ""
    text = "<!-- agent-discipline reinjection: this is state you recorded earlier; trust it over memory -->\n" + "\n\n".join(parts)
    if len(text) > budget_chars:
        text = text[:budget_chars - 60] + "\n… (truncated; run `ad.py reinject --full` for everything)"
    return text

# ---------------- hook entrypoints ----------------
def hook_read_cache():
    """PreToolUse on Read: tell the model what it already knows about this file. Never blocks."""
    inp = read_hook_input()
    target = tool_command(inp)
    if not target or target.startswith("{"): allow()
    key, ent = manifest_lookup(target)
    if ent and os.path.isfile(key) and sha256_file(key) == ent.get("sha256") and ent.get("reads", 0) >= 1:
        allow(f"read-cache: {os.path.basename(key)} is UNCHANGED since {ent.get('ts')} (read {ent.get('reads')}x). "
              f"Summary: {ent.get('summary') or 'none'}. Prefer a line range or the summary; say `force` to justify a full re-read.")
    allow()

def hook_record_read():
    """PostToolUse on Read: record path and ranges into the manifest."""
    inp = read_hook_input()
    ti = inp.get("tool_input") or {}
    target = tool_command(inp)
    if target and not target.startswith("{") and os.path.isfile(target):
        rng = None
        if "offset" in ti or "limit" in ti:
            a = int(ti.get("offset") or 1); rng = [[a, a + int(ti.get("limit") or 0)]]
        manifest_record(target, rng)
    sys.exit(0)

def hook_reinject():
    """SessionStart / PostCompact: emit state."""
    txt = reinject()
    emit_context(txt) if txt else sys.exit(0)
