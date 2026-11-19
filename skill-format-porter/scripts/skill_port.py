#!/usr/bin/env python3
"""Port an agent skill folder between Claude, Cursor, Codex and Kimi Code formats, and lint it.

Usage: skill_port.py SKILL_DIR --target kimi|claude|cursor|codex [--out OUT_DIR] [--lint-only]
Exit 0 = ported/linted clean, 1 = lint errors, 2 = bad input.

All targets read SKILL.md with YAML frontmatter. Differences handled here:
- Kimi Code: fields name, description, type, whenToUse, disableModelInvocation, arguments;
  supporting files are referenced as ${KIMI_SKILL_DIR}/path. Unknown fields are dropped.
- Claude: fields name, description, license, allowed-tools, metadata; relative paths.
- Cursor / Codex: name, description (plus metadata passthrough); relative paths.
"""
import json
import re
import shutil
import sys
from pathlib import Path

KIMI_FIELDS = {"name", "description", "type", "whenToUse", "disableModelInvocation", "arguments"}
CLAUDE_FIELDS = {"name", "description", "license", "allowed-tools", "metadata"}
GENERIC_FIELDS = {"name", "description", "metadata"}
KIMI_ALIASES = {"when-to-use": "whenToUse", "when_to_use": "whenToUse",
                "disable-model-invocation": "disableModelInvocation",
                "disable_model_invocation": "disableModelInvocation"}
REL_PATH = re.compile(r"(?<![\w/$.{-])((?:scripts|references|templates|assets|examples)/[\w./-]+)")
KIMI_PATH = re.compile(r"\$\{KIMI_SKILL_DIR\}/")


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if ":" not in line:
            return None, text
        k, v = line.split(":", 1)
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        elif v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
        elif v.lower() in ("true", "false"):
            v = v.lower() == "true"
        fm[k.strip()] = v
    return fm, m.group(2)


def dump_frontmatter(fm):
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, list):
            lines.append(f"{k}: [{', '.join(json.dumps(x) for x in v)}]")
        else:
            s = str(v)
            lines.append(f"{k}: {json.dumps(s) if re.search(r'[:#\"\\n]|^\\s|\\s$', s) else s}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def lint(skill_dir, fm, body, target):
    out = []
    name = fm.get("name")
    if not name:
        out.append(("error", "frontmatter missing 'name'"))
    else:
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", str(name)):
            out.append(("error", f"name {name!r} is not lowercase kebab-case"))
        if len(str(name)) > 64:
            out.append(("error", "name longer than 64 characters"))
        if str(name) != skill_dir.name:
            out.append(("warn", f"name {name!r} differs from folder {skill_dir.name!r}"))
    desc = fm.get("description")
    if not desc:
        out.append(("error", "frontmatter missing 'description'"))
    else:
        d = str(desc)
        if len(d) > 1024:
            out.append(("error", f"description is {len(d)} chars; max 1024"))
        if "<" in d or ">" in d:
            out.append(("error", "description contains angle brackets"))
        if target == "kimi" and len(d) > 240:
            out.append(("warn", "description over 240 chars; Kimi Code shows a one-line summary"))
    for ref in set(REL_PATH.findall(body)) | {p.split("}/", 1)[1] for p in re.findall(r"\$\{KIMI_SKILL_DIR\}/[\w./-]+", body)}:
        ref = ref.rstrip(".,)")
        if not (skill_dir / ref).exists():
            out.append(("error", f"body references missing file {ref}"))
    if target == "kimi" and fm.get("type") not in (None, "prompt", "inline", "flow"):
        out.append(("error", f"type {fm.get('type')!r} is not prompt, inline or flow; Kimi skips the skill"))
    if target != "kimi" and KIMI_PATH.search(body):
        out.append(("warn", "body mentions ${KIMI_SKILL_DIR}; convert it unless it is documentation"))
    if len(body.splitlines()) > 500:
        out.append(("warn", "body over 500 lines; move detail to references/"))
    return out


def convert(fm, body, target):
    notes = []
    fm = dict(fm)
    for k, v in list(fm.items()):
        if k in KIMI_ALIASES:
            fm[KIMI_ALIASES[k]] = fm.pop(k)
    if target == "kimi":
        keep = KIMI_FIELDS
        for k in list(fm):
            if k not in keep:
                notes.append(f"dropped field {k!r} (not read by Kimi Code)")
                fm.pop(k)
        fm.setdefault("type", "prompt")
        body, n = REL_PATH.subn(r"${KIMI_SKILL_DIR}/\1", body)
        if n:
            notes.append(f"rewrote {n} relative path(s) to ${{KIMI_SKILL_DIR}}/...")
    else:
        keep = CLAUDE_FIELDS if target == "claude" else GENERIC_FIELDS
        if fm.get("whenToUse") and "whenToUse" not in keep:
            fm["description"] = f"{fm.get('description', '')} Use when: {fm['whenToUse']}".strip()
            notes.append("merged whenToUse into description")
        if fm.get("disableModelInvocation") and target == "claude":
            notes.append("disableModelInvocation dropped; Claude has no equivalent, add a note in the body")
        for k in list(fm):
            if k not in keep:
                notes.append(f"dropped field {k!r} (not read by {target})")
                fm.pop(k)
        body, n = KIMI_PATH.subn("", body)
        if n:
            notes.append(f"rewrote {n} ${{KIMI_SKILL_DIR}} path(s) to relative")
    ordered = {k: fm[k] for k in ("name", "description") if k in fm}
    ordered.update({k: v for k, v in fm.items() if k not in ordered})
    return ordered, body, notes


def main(argv):
    if len(argv) < 2 or "--target" not in argv:
        print(__doc__)
        return 2
    skill_dir = Path(argv[1])
    target = argv[argv.index("--target") + 1]
    if target not in ("kimi", "claude", "cursor", "codex"):
        print(f"unknown target {target}")
        return 2
    out_dir = Path(argv[argv.index("--out") + 1]) if "--out" in argv else None
    lint_only = "--lint-only" in argv
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        print(f"{skill_md} not found")
        return 2
    fm, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if fm is None:
        print("ERROR cannot parse YAML frontmatter (expected simple key: value lines)")
        return 1
    notes = []
    if not lint_only:
        fm, body, notes = convert(fm, body, target)
    findings = lint(skill_dir, fm, body, target)
    for n in notes:
        print(f"NOTE  {n}")
    for lvl, msg in findings:
        print(f"{lvl.upper():5} {msg}")
    errors = sum(1 for lvl, _ in findings if lvl == "error")
    if not lint_only and out_dir and not errors:
        dest = out_dir / skill_dir.name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(skill_dir, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        (dest / "SKILL.md").write_text(dump_frontmatter(fm) + body.lstrip("\n"), encoding="utf-8")
        print(f"wrote {dest}")
    print(f"summary: target={target} {errors} error(s), {len(findings) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
