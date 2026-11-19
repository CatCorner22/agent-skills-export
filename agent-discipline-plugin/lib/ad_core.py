"""Shared core for the agent-discipline plugin. Standard library only. Python 3.8+.

State lives in one directory (default: ./.agent, override with $AGENT_STATE_DIR):
  manifest.json     files read/fetched: path -> {size, sha256, ranges, summary, ts, source}
  ledger.md         autonomy ledger: GRANT / FORBID / STOP / ACCEPT lines with timestamps
  CHECKPOINT.md     context-budget checkpoint written by the agent
  toollog.jsonl     one line per tool call (written by the PostToolUse `log` hook)
  provenance.jsonl  deliverable section -> evidence pointers
  outputs/          full tool outputs that were trimmed, keyed by hash
  regress/          regression set + results
Every public function is defensive: a state-file problem never raises out of the hook (fail-open),
except scope-fence, which fails CLOSED on destructive patterns by design.
"""
import os, sys, json, time, hashlib, re, datetime

def state_dir(create=True):
    d = os.environ.get("AGENT_STATE_DIR") or os.path.join(os.getcwd(), ".agent")
    if create:
        os.makedirs(os.path.join(d, "outputs"), exist_ok=True)
    return d

def now():
    return datetime.datetime.now().replace(microsecond=0).isoformat()

def sha256_file(path, limit=None):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(1 << 20)
            if not chunk: break
            h.update(chunk)
    return h.hexdigest()

def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()

def load_json(name, default):
    p = os.path.join(state_dir(), name)
    try:
        with open(p, encoding="utf-8") as f: return json.load(f)
    except Exception:
        return default

def save_json(name, data):
    p = os.path.join(state_dir(), name)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f: json.dump(data, f, indent=1, sort_keys=True)
    os.replace(tmp, p)

def append_line(name, line):
    with open(os.path.join(state_dir(), name), "a", encoding="utf-8") as f: f.write(line.rstrip("\n") + "\n")

def read_text(name, default=""):
    try:
        with open(os.path.join(state_dir(), name), encoding="utf-8") as f: return f.read()
    except Exception:
        return default

def human_size(n):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB": return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024.0

# ---------------- hook I/O (Claude Code / Devin hook contract) ----------------
def read_hook_input():
    """Parse the JSON the host writes to stdin. Returns {} on any problem (fail-open)."""
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}

def deny(reason, event="PreToolUse"):
    """Block a tool call. Emits both the JSON form and exit 2 + stderr, so any host honors it."""
    out = {"hookSpecificOutput": {"hookEventName": event, "permissionDecision": "deny",
                                   "permissionDecisionReason": reason}}
    print(json.dumps(out))
    sys.stderr.write(reason + "\n")
    sys.exit(2)

def allow(context=None, event="PreToolUse"):
    """Allow; optionally add context the model will see."""
    if context:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": context}}))
    sys.exit(0)

def stop_block(reason):
    """Stop hook: send the agent back to work."""
    print(json.dumps({"decision": "block", "reason": reason}))
    sys.exit(0)

def emit_context(text):
    """SessionStart / PreCompact / PostCompact: plain stdout is appended to the model's context."""
    sys.stdout.write(text if text.endswith("\n") else text + "\n")
    sys.exit(0)

def tool_command(inp):
    """Best-effort extraction of the shell command / URL / path from a tool_input dict."""
    ti = inp.get("tool_input") or {}
    for k in ("command", "cmd", "url", "file_path", "path", "filePath", "target_file", "notebook_path"):
        if isinstance(ti.get(k), str): return ti[k]
    return json.dumps(ti)[:2000]

def tool_paths(inp):
    """All path-like strings in tool_input (for scope-fence)."""
    ti = inp.get("tool_input") or {}
    found = []
    def walk(v):
        if isinstance(v, str):
            for tok in re.findall(r"(?:~|/)[^\s'\"`;|&<>()]+|\.\./[^\s'\"`;|&]*", v):
                found.append(tok)
            if inp.get("tool_name", "").lower() in ("write", "edit", "read", "multiedit", "notebookedit") and v and " " not in v:
                found.append(v)
        elif isinstance(v, dict):
            for x in v.values(): walk(x)
        elif isinstance(v, list):
            for x in v: walk(x)
    walk(ti)
    return found

def log_tool(inp, extra=None):
    """Append a compact record of a tool call to toollog.jsonl (used by completion-gate and provenance)."""
    try:
        rec = {"ts": now(), "tool": inp.get("tool_name"), "cmd": tool_command(inp)[:500]}
        resp = inp.get("tool_response")
        if resp is not None:
            s = resp if isinstance(resp, str) else json.dumps(resp)
            rec["resp_sha"] = sha256_text(s)[:12]; rec["resp_len"] = len(s)
            m = re.search(r"exit(?: code)?[:= ]+(\d+)", s, re.I)
            if m: rec["exit"] = int(m.group(1))
        if extra: rec.update(extra)
        append_line("toollog.jsonl", json.dumps(rec))
        return rec
    except Exception:
        return None
