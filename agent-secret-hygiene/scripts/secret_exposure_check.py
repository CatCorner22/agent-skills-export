#!/usr/bin/env python3
"""Find secrets an agent can see, leak or be talked into using: environment, prompts, sub-agent briefs, transcripts.

Usage: secret_exposure_check.py [--env] [--env-file .env] [--prompt FILE ...] [--transcript FILE ...] [--allow VAR1,VAR2]
--env/--env-file: flags variables with secret-like names or values that a model or sub-agent process inherits.
--prompt: flags secret literals pasted into prompts or briefs, install/download commands, and authority claims
("you are authorized", "ignore safety") that a model may treat as permission.
--transcript: flags secret literals echoed in assistant output or tool arguments (exfiltration), and reads of
env/secret files (cat .env, printenv, echo $KEY). Exit 1 on errors, 2 on bad input.
"""
import json
import os
import re
import sys

SECRET_KEY = re.compile(r"(api[_-]?key|secret|token|password|passwd|credential|private[_-]?key|auth)", re.I)
SECRET_VAL = re.compile(r"(sk-[A-Za-z0-9_-]{8,}|ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{12,}|xox[bap]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_-]{30,}|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|hf_[A-Za-z0-9]{20,}|glpat-[A-Za-z0-9_-]{20,})")
INSTALL = re.compile(r"(curl[^\n|]*\|\s*(ba)?sh|wget[^\n|]*\|\s*(ba)?sh|pip3? install|npm (install|i)\b|npx |brew install|apt(-get)? install|git clone|chmod \+x)", re.I)
AUTHORITY = re.compile(r"(you are authorized|authorized red team|ignore (previous|all|safety)|as the administrator|the user has approved|no need to ask)", re.I)
ENV_READ = re.compile(r"(\bprintenv\b|\benv\b\s*$|\benv\s*\||cat\s+[^\n]*\.env\b|echo\s+\$\{?[A-Z_]*(KEY|TOKEN|SECRET|PASS)[A-Z_]*|os\.environ\[|process\.env\.)", re.I | re.M)


def mask(s):
    return s[:6] + "..." + s[-3:] if len(s) > 12 else "***"


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    allow = set(argv[argv.index("--allow") + 1].split(",")) if "--allow" in argv else set()
    out = []
    env_items = []
    if "--env" in argv:
        env_items += list(os.environ.items())
    if "--env-file" in argv:
        try:
            for line in open(argv[argv.index("--env-file") + 1], encoding="utf-8"):
                if "=" in line and not line.strip().startswith("#"):
                    k, v = line.strip().split("=", 1)
                    env_items.append((k.strip(), v.strip().strip("\"'")))
        except OSError as exc:
            print(f"cannot read env file: {exc}"); return 2
    for k, v in env_items:
        if k in allow:
            continue
        if SECRET_KEY.search(k) or SECRET_VAL.search(v or ""):
            out.append(("error", f"env {k} is secret-like and visible to the model/sub-agent process; move it behind a tool or proxy"))

    def files(flag):
        if flag not in argv:
            return []
        i = argv.index(flag) + 1
        res = []
        while i < len(argv) and not argv[i].startswith("--"):
            res.append(argv[i]); i += 1
        return res

    for path in files("--prompt"):
        try:
            tpl = open(path, encoding="utf-8").read()
        except OSError as exc:
            print(f"cannot read {path}: {exc}"); return 2
        for m in SECRET_VAL.finditer(tpl):
            out.append(("error", f"{path}: secret literal {mask(m.group(0))} in a prompt; pass secrets to tools, never to the model"))
        for m in INSTALL.finditer(tpl):
            out.append(("error", f"{path}: install/download command {m.group(0)[:50]!r}; sub-agents must not install"))
        for m in AUTHORITY.finditer(tpl):
            out.append(("error", f"{path}: authority claim {m.group(0)!r}; claims in text are not permission"))
        if not re.search(r"(do not|never|must not)[^.\n]*(credential|secret|token|key|install|post|publish|push)", tpl, re.I):
            out.append(("warn", f"{path}: no explicit ban on sharing credentials or installing software"))
    for path in files("--transcript"):
        try:
            raw = open(path, encoding="utf-8").read()
        except OSError as exc:
            print(f"cannot read {path}: {exc}"); return 2
        try:
            data = json.loads(raw)
            msgs = data.get("messages", data) if isinstance(data, (dict, list)) else []
        except json.JSONDecodeError:
            msgs = [{"role": "assistant", "content": raw}]
        for i, m in enumerate(msgs if isinstance(msgs, list) else []):
            if not isinstance(m, dict):
                continue
            blob = json.dumps(m)
            role = m.get("role", "?")
            for s in SECRET_VAL.finditer(blob):
                lvl = "error" if role in ("assistant", "tool") else "warn"
                out.append((lvl, f"{path} message {i} ({role}): secret literal {mask(s.group(0))} {'emitted by the model or a tool' if lvl == 'error' else 'present in input'}"))
            if role == "assistant" and ENV_READ.search(blob):
                out.append(("warn", f"{path} message {i}: assistant reads environment or secret files ({ENV_READ.search(blob).group(0).strip()[:30]!r})"))
    for lvl, msg in out:
        print(f"{lvl.upper():5} {msg}")
    errors = sum(1 for lvl, _ in out if lvl == "error")
    print(f"summary: {errors} error(s), {len(out) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
