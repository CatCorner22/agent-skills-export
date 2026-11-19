"""Enforcement layer: fetch-guard (S1/P1), scope-fence (S8/P3), tool-call-validator (S14)."""
import os, re, sys, json
from ad_core import (state_dir, now, load_json, save_json, read_text, human_size, read_hook_input, deny, allow,
                     tool_command, tool_paths)
from ad_state import manifest_lookup, ledger_entries, FETCH_RE, URL_RE

DEFAULT_MAX_FETCH_MB = float(os.environ.get("AD_MAX_FETCH_MB", "100"))

# ---------------- fetch-guard ----------------
def fetch_targets(cmd):
    urls = URL_RE.findall(cmd)
    names = [os.path.basename(u.split("?")[0]) for u in urls]
    m = re.search(r"(?:-o|--output|-O)\s+(\S+)", cmd)
    if m: names.append(os.path.basename(m.group(1)))
    return urls, [n for n in names if n]

def fetch_guard_decide(cmd, tool_name="Bash", max_mb=DEFAULT_MAX_FETCH_MB):
    """Return (deny_reason or None). Pure function for tests."""
    is_fetch = tool_name.lower() in ("webfetch", "fetch", "download") or bool(FETCH_RE.search(cmd))
    if not is_fetch: return None
    urls, names = fetch_targets(cmd)
    for t in urls + names:
        key, ent = manifest_lookup(t)
        if ent:
            return (f"fetch-guard: `{t}` is already available — manifest entry {key} "
                    f"({human_size(ent.get('size', 0))}, recorded {ent.get('ts')}, summary: {ent.get('summary') or 'none'}). "
                    f"Use the existing copy. To re-fetch anyway, record `ledger add GRANT \"re-fetch {t}\"` first.")
    m = re.search(r"(?:expected|size)[=:]\s*(\d+(?:\.\d+)?)\s*(MB|GB)", cmd, re.I)
    if m:
        mb = float(m.group(1)) * (1024 if m.group(2).upper() == "GB" else 1)
        if mb > max_mb:
            return f"fetch-guard: download of ~{mb:.0f} MB exceeds the {max_mb:.0f} MB limit. State the inventory line first (what you already have) and get a GRANT in the ledger."
    for e in ledger_entries():
        if e["kind"] == "GRANT" and ("fetch" in e["text"].lower() or "download" in e["text"].lower()):
            return None
    big_hint = re.search(r"\.(cram|bam|vcf(?:\.gz)?|fastq(?:\.gz)?|iso|tar\.gz|zip|parquet|sqlite|dump)\b", cmd, re.I)
    if big_hint:
        return (f"fetch-guard: fetching a large-type file ({big_hint.group(0)}) with no inventory. Before any download: "
                f"(1) list project knowledge / attachments / manifest; (2) search by filename and 2 synonyms; (3) write the one-line inventory result; "
                f"(4) if truly absent, `ledger add GRANT \"download <name>\"` then retry.")
    return None

def hook_fetch_guard():
    inp = read_hook_input()
    reason = fetch_guard_decide(tool_command(inp), inp.get("tool_name") or "Bash")
    deny(reason) if reason else allow()

# ---------------- scope-fence ----------------
DESTRUCTIVE = [
    (re.compile(r"\brm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r)\b"), "recursive force delete"),
    (re.compile(r"\brm\s+-r\w*\s+(/|~|\$HOME|\.\.)(\s|$|/)"), "recursive delete of root/home/parent"),
    (re.compile(r"\bgit\s+push\s+.*--force(?!-with-lease)"), "force push"),
    (re.compile(r"\bgit\s+(reset\s+--hard|clean\s+-[a-z]*f|checkout\s+--\s+\.)"), "discards uncommitted work"),
    (re.compile(r"\b(drop|truncate)\s+(table|database|schema)\b", re.I), "destructive SQL"),
    (re.compile(r"\bdelete\s+from\s+\w+\s*;?\s*$", re.I), "DELETE without WHERE"),
    (re.compile(r"\b(mkfs|dd\s+if=|shutdown|reboot|:\(\)\s*\{)"), "system-destructive"),
    (re.compile(r"\b(terraform\s+destroy|kubectl\s+delete\s+(ns|namespace)|aws\s+\w+\s+delete-|gcloud\s+.*\s+delete\b|az\s+.*\s+delete\b)"), "infrastructure delete"),
    (re.compile(r"\b(vercel\s+--prod|npm\s+publish|twine\s+upload|gh\s+pr\s+merge|git\s+push\s+\S*\s+(main|master)\b)"), "production / publish / merge"),
    (re.compile(r"\b(chmod|chown)\s+-R\s+\S+\s+/(\s|$)"), "recursive chmod/chown of /"),
]
PROD_HINTS = re.compile(r"\b(prod|production|live|PRODUCTION_DATABASE_URL|DATABASE_URL=postgres://[^\s]*prod)", re.I)

def declared_roots():
    cfg = load_json("scope.json", {})
    roots = cfg.get("roots") or [os.getcwd()]
    return [os.path.abspath(os.path.expanduser(r)) for r in roots], cfg

def scope_set(roots, allow_patterns=None):
    cfg = load_json("scope.json", {})
    cfg["roots"] = roots
    if allow_patterns is not None: cfg["allow"] = allow_patterns
    save_json("scope.json", cfg); return f"scope roots: {roots}"

def has_grant(text):
    words = set(re.findall(r"[a-z0-9_./-]{3,}", text.lower()))
    for e in reversed(ledger_entries()):
        if e["kind"] == "GRANT" and len(words & set(re.findall(r"[a-z0-9_./-]{3,}", e["text"].lower()))) >= 2:
            return e
    return None

def scope_fence_decide(inp, cwd=None):
    """Return deny reason or None. Fails CLOSED on destructive patterns, open elsewhere."""
    tool = (inp.get("tool_name") or "").lower()
    cmd = tool_command(inp) if tool in ("bash", "shell", "exec", "run_terminal_cmd", "terminal") else ""
    roots, cfg = declared_roots()
    cwd = os.path.abspath(cwd or inp.get("cwd") or os.getcwd())
    # 1. destructive patterns
    for rx, label in DESTRUCTIVE:
        if cmd and rx.search(cmd):
            g = has_grant(cmd)
            if g: return None
            return (f"scope-fence: blocked — {label}: `{cmd[:160]}`. This is on the confirm-first list. Stage the reversible prep, "
                    f"show the exact command, and ask for a one-word go-ahead; then `ad.py ledger add GRANT \"{label}: <command>\"` and retry.")
    if cmd and PROD_HINTS.search(cmd) and re.search(r"\b(psql|mysql|mongo|redis-cli|prisma|drizzle|supabase|migrate|alembic|knex|sequelize|rails\s+db)\b", cmd):
        if not has_grant(cmd): return f"scope-fence: command targets what looks like PRODUCTION data: `{cmd[:160]}`. Needs an explicit GRANT in the ledger."
    # 2. path containment for writes/deletes
    write_tool = tool in ("write", "edit", "multiedit", "notebookedit") or (cmd and re.search(r"(\b(rm|mv|cp|tee|truncate|shred|unlink|install|sed\s+-i)\b|>)", cmd))
    if write_tool:
        for p in tool_paths(inp):
            ap = os.path.abspath(os.path.expanduser(p if os.path.isabs(os.path.expanduser(p)) else os.path.join(cwd, p)))
            if any(ap == r or ap.startswith(r + os.sep) for r in roots): continue
            if any(ap.startswith(x) for x in ("/tmp", "/var/tmp", "/dev/null")): continue
            if cfg.get("allow") and any(re.search(a, ap) for a in cfg["allow"]): continue
            if has_grant(ap): continue
            return (f"scope-fence: path `{p}` resolves to `{ap}`, outside declared roots {roots}. "
                    f"Either the path is a mistake (fix it), or widen scope with `ad.py scope set <root> …`, or get a GRANT.")
    return None

def hook_scope_fence():
    inp = read_hook_input()
    try:
        reason = scope_fence_decide(inp)
    except Exception as ex:  # fail closed only for obviously destructive text
        cmd = tool_command(inp)
        reason = f"scope-fence internal error ({ex}); blocking because command matches a destructive pattern" if any(rx.search(cmd) for rx, _ in DESTRUCTIVE) else None
    deny(reason) if reason else allow()

# ---------------- tool-call-validator ----------------
def validate_call_decide(inp):
    """Soft checks: cwd mismatch, repeated identical failing call, empty args. Returns (deny_reason, context)."""
    cmd = tool_command(inp)
    log = [json.loads(l) for l in read_text("toollog.jsonl").splitlines()[-30:] if l.strip()]
    same_fail = [r for r in log if r.get("cmd") == cmd[:500] and r.get("exit") not in (None, 0)]
    if len(same_fail) >= 2:
        return (f"tool-call-validator: this exact call failed {len(same_fail)}x already (last exit {same_fail[-1].get('exit')}). "
                f"Change something — read the stderr you were given, fix the cause, or pick another route — before retrying."), None
    ctx = []
    ti = inp.get("tool_input") or {}
    if isinstance(ti, dict) and not any(v for v in ti.values()):
        ctx.append("tool-call-validator: tool_input is empty — did you mean to pass a path/command?")
    roots, _ = declared_roots()
    cwd = inp.get("cwd")
    if cwd and not any(os.path.abspath(cwd).startswith(r) for r in roots):
        ctx.append(f"tool-call-validator: cwd {cwd} is outside declared roots {roots}; confirm you are in the right workspace.")
    return None, (" ".join(ctx) or None)

def hook_validate_call():
    inp = read_hook_input()
    reason, ctx = validate_call_decide(inp)
    deny(reason) if reason else allow(ctx)
