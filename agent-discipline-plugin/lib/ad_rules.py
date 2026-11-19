"""rule-compiler (S9/S12/P7): lint rules files, rewrite negatives as positive checks, emit hook configs. test-impact-selector (S13)."""
import os, re, sys, json, subprocess
from ad_core import now

RULE_FILES = ("CLAUDE.md", "AGENTS.md", ".cursorrules", "GEMINI.md", ".windsurfrules", "copilot-instructions.md")
NEG_RE = re.compile(r"\b(never|don't|do not|must not|shouldn't|should not|avoid|no\s+\w+ing)\b", re.I)
HOOKABLE = [  # (pattern in rule text, regex for command to deny, label)
    (r"rm\s*-rf|delete.*(recursive|files)|remove.*director", r"\\brm\\s+-[a-zA-Z]*r", "recursive delete"),
    (r"force[- ]push", r"git\\s+push\\s+.*--force", "force push"),
    (r"(push|commit).*(main|master)", r"git\\s+push\\s+\\S*\\s+(main|master)\\b", "push to main"),
    (r"(drop|truncate).*(table|database)|production\s+(db|database)", r"\\b(drop|truncate)\\s+(table|database)", "destructive SQL"),
    (r"npm\s+publish|publish.*package", r"npm\\s+publish|twine\\s+upload", "publish"),
    (r"(\.env|secrets?|credentials?).*(commit|log|print)|commit.*\.env", r"git\\s+add\\s+.*\\.env", "commit secrets"),
    (r"deploy.*prod|vercel\s+--prod", r"vercel\\s+--prod|deploy\\s+--prod", "prod deploy"),
    (r"(edit|modify|touch|change).*(migrations?/|generated|vendor|node_modules)", None, "protected paths (use scope.json allow/roots)"),
]

def find_rule_files(root="."):
    out = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ("node_modules", ".git", ".venv", "venv", "dist", "build")]
        for f in fn:
            if f in RULE_FILES or f.endswith(".mdc") and ".cursor" in dp: out.append(os.path.join(dp, f))
        if dp.count(os.sep) - root.count(os.sep) > 3: dn[:] = []
    return out

def positive_rewrite(line):
    """Heuristic: 'Never X' -> 'Before X-ing, check: ...'. Keeps the original intent explicit."""
    s = line.strip().lstrip("-*0123456789. ").strip()
    m = re.match(r"(?i)^(never|don't|do not|must not|avoid)\s+(.*)", s)
    if not m: return None
    act = m.group(2).rstrip(".")
    return f"Before any step that would {act}: stop and pick the allowed alternative; if none exists, ask once. (was: {s})"

def lint_rules(path, max_lines=150):
    txt = open(path, encoding="utf-8").read()
    lines = txt.splitlines()
    findings, hooks, rewrites = [], [], []
    if len(lines) > max_lines:
        findings.append(f"{path}: {len(lines)} lines (>{max_lines}). Context files cost ~20% more tokens and do not raise success; move task-specific sections to on-demand skills.")
    for i, l in enumerate(lines, 1):
        if NEG_RE.search(l):
            rw = positive_rewrite(l)
            hooked = False
            for pat, rx, label in HOOKABLE:
                if re.search(pat, l, re.I):
                    hooked = True
                    hooks.append({"line": i, "label": label, "deny_regex": rx, "rule": l.strip()})
            if rw: rewrites.append({"line": i, "positive": rw})
            if not hooked:
                findings.append(f"{path}:{i}: negation-only rule with no hook equivalent — keep it to one line and make the positive check explicit.")
    vague = [i for i, l in enumerate(lines, 1) if re.search(r"\b(be careful|use best judgment|as appropriate|when needed|try to)\b", l, re.I)]
    for i in vague: findings.append(f"{path}:{i}: vague rule (no testable trigger/condition).")
    return {"file": path, "lines": len(lines), "findings": findings, "hooks": hooks, "rewrites": rewrites}

def compile_hooks(results, script_path="python3 ${CLAUDE_PLUGIN_ROOT}/lib/ad.py"):
    """Emit a Claude-format hooks.json fragment with one deny regex per hookable negative rule."""
    patterns = sorted({h["deny_regex"] for r in results for h in r["hooks"] if h["deny_regex"]})
    if not patterns: return {"hooks": {}}
    return {"hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [
        {"type": "command", "command": f"{script_path} deny-regex " + " ".join(json.dumps(p) for p in patterns)}]}]}}

def deny_regex_hook(patterns):
    """Generic PreToolUse deny: block Bash commands matching any compiled pattern."""
    from ad_core import read_hook_input, tool_command, deny, allow
    inp = read_hook_input(); cmd = tool_command(inp)
    for p in patterns:
        if re.search(p, cmd): deny(f"rule-compiler: command matches a compiled rule (`{p}`): {cmd[:120]}")
    allow()

# ---------------- test-impact-selector ----------------
def changed_files(base=None):
    try:
        args = ["git", "diff", "--name-only"] + ([base] if base else []) 
        out = subprocess.run(args, capture_output=True, text=True, timeout=20).stdout.split()
        out += subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], capture_output=True, text=True, timeout=20).stdout.split()
        return sorted(set(out))
    except Exception:
        return []

SHARED_RE = re.compile(r"(^|/)(package(-lock)?\.json|pnpm-lock\.yaml|yarn\.lock|pyproject\.toml|setup\.(py|cfg)|requirements.*\.txt|Cargo\.toml|go\.mod|tsconfig.*\.json|jest\.config.*|pytest\.ini|conftest\.py|vite\.config.*|webpack.*|\.github/|Dockerfile|Makefile|src/(lib|utils|shared|common|core)/)", re.I)

def test_impact(files, root="."):
    """Map changed files -> candidate test files. Returns dict(run=[...], full_suite_reason=str|None, skipped=[...])."""
    all_tests = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ("node_modules", ".git", ".venv", "venv", "dist", "build", "__pycache__")]
        for f in fn:
            if re.search(r"(^test_.*\.py$|_test\.py$|\.(test|spec)\.[jt]sx?$|_test\.go$|Test\.java$|\.rs$)", f) and ("test" in f.lower() or "spec" in f.lower() or dp.endswith("tests")):
                all_tests.append(os.path.relpath(os.path.join(dp, f), root))
    run, reason = set(), None
    for f in files:
        if SHARED_RE.search(f): reason = f"shared/config file changed: {f}"
        stem = re.sub(r"\.(py|[jt]sx?|go|rs|java)$", "", os.path.basename(f))
        stem = re.sub(r"^(test_)|(_test|\.test|\.spec)$", "", stem)
        if not stem: continue
        for t in all_tests:
            tb = os.path.basename(t).lower()
            if stem.lower() in tb: run.add(t); continue
            try:
                if re.search(rf"\b{re.escape(stem)}\b", open(os.path.join(root, t), encoding="utf-8", errors="ignore").read()): run.add(t)
            except Exception: pass
        if re.search(r"(^|/)tests?/", f) or re.search(r"\.(test|spec)\.", f): run.add(f)
    skipped = sorted(set(all_tests) - run)
    return {"changed": files, "run": sorted(run), "full_suite_reason": reason, "skipped_count": len(skipped), "total_tests": len(all_tests)}
