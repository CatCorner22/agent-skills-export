#!/usr/bin/env python3
"""Validate the Chicken Little Overwatch Plugin: manifests, skill spec, links, generated files, rules, and tests."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "chicken-little-overwatch"
NAME = "chicken-little-overwatch-plugin"
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def front_matter(path):
    match = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not match:
        return None
    try:
        import yaml
        data = yaml.safe_load(match.group(1))
        return data if isinstance(data, dict) else None
    except ImportError:
        return {k: v.strip().strip('"') for k, v in re.findall(r"^([A-Za-z-]+):\s*(.*)$", match.group(1), re.M)}
    except Exception as error:
        errors.append(f"{path.relative_to(ROOT)}: front matter is not valid YAML ({error})")
        return None


# Manifests agree on name, version, and description.
manifests = {p: json.loads((ROOT / p).read_text(encoding="utf-8")) for p in
             ("plugin.json", ".claude-plugin/plugin.json", ".cursor-plugin/plugin.json", ".devin-plugin/plugin.json", "gemini-extension.json")}
for path, data in manifests.items():
    check(data.get("name") == NAME, f"{path}: name must be {NAME}")
    check(re.fullmatch(r"\d+\.\d+\.\d+", str(data.get("version", ""))), f"{path}: version must be semantic")
check(len({d.get("version") for d in manifests.values()}) == 1, "manifests disagree on version")
check(len({d.get("description") for d in manifests.values()}) == 1, "manifests disagree on description")
allowed = {"$schema", "name", "version", "description", "author", "homepage", "repository", "license", "keywords", "extensions"}
check(set(manifests["plugin.json"]) <= allowed, "plugin.json has fields outside the Agent Plugins schema")
check(manifests["plugin.json"].get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "plugin.json lacks the Agent Plugins $schema")
for path, key in ((".claude-plugin/plugin.json", "icon"), (".cursor-plugin/plugin.json", "logo")):
    target = manifests[path].get(key)
    check(target and (ROOT / target).exists(), f"{path}: {key} file missing")

# Skill follows the Agent Skills specification.
meta = front_matter(SKILL / "SKILL.md") or {}
name = meta.get("name", "")
description = str(meta.get("description", ""))
check(name == SKILL.name, "SKILL.md name must match its folder")
check(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) and len(name) <= 64, "SKILL.md name breaks the Agent Skills rules")
check(0 < len(description) <= 1024, f"SKILL.md description must hold 1-1024 characters (has {len(description)})")
check(not re.search(r"[<>]", description), "SKILL.md description must not contain angle brackets")
check(": " not in description, "SKILL.md description must not contain ': ' (some hosts reject it)")
check(len(str(meta.get("compatibility", ""))) <= 500, "compatibility exceeds 500 characters")
check(len((SKILL / "SKILL.md").read_text(encoding="utf-8").splitlines()) <= 500, "SKILL.md exceeds 500 lines")

# Every file that a Markdown file names exists.
for md in list(SKILL.rglob("*.md")) + list((ROOT / "commands").glob("*.md")) + [ROOT / "README.md"]:
    base = SKILL if SKILL in md.parents or md.parent == SKILL else SKILL
    for ref in set(re.findall(r"`((?:references|scripts|tests)/[A-Za-z0-9_.-]+)`", md.read_text(encoding="utf-8"))):
        check((base / ref).exists(), f"{md.relative_to(ROOT)} names missing {ref}")

# Rule sets stay complete.
swarm = (SKILL / "references" / "red-team-swarm.md").read_text(encoding="utf-8")
roles = (SKILL / "references" / "roles.md").read_text(encoding="utf-8")
for prefix, count, text in (("D", 15, swarm), ("L", 14, swarm), ("RT", 10, swarm), ("S", 9, roles)):
    for number in range(1, count + 1):
        check(re.search(rf"\*\*{prefix}{number} ", text), f"rule {prefix}{number} missing")
skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
for number in range(1, 9):
    check(f"**C{number} " in skill_text, f"core rule C{number} missing")
standard = (SKILL / "references" / "one-way-optimal-language.md").read_text(encoding="utf-8")
for number in range(1, 9):
    check(f"**H{number} " in standard, f"hard rule H{number} missing from the writing standard")
for number in range(1, 31):
    check(f"| R{number} " in standard, f"rubric row R{number} missing from the writing standard")

# Agents: generated, read-only, and named in the swarm table.
for name_ in re.findall(r"`(clo-[a-z-]+)`", swarm):
    check((ROOT / "agents" / f"{name_}.md").exists(), f"agent {name_} missing")
for agent in sorted((ROOT / "agents").glob("*.md")):
    data = front_matter(agent) or {}
    check(data.get("name") == agent.stem, f"{agent.name}: name differs from file name")
    check(data.get("description"), f"{agent.name}: needs a description")
    check(set(data) <= {"name", "description"}, f"{agent.name}: only name and description load in every host (Gemini CLI rejects other keys)")
    check("S1 Read only" in agent.read_text(encoding="utf-8"), f"{agent.name}: lacks the read-only rule S1")
for command in sorted((ROOT / "commands").glob("*.md")):
    data = front_matter(command) or {}
    check("description" in data, f"{command.name} lacks a description")
    check(command.with_suffix(".toml").exists(), f"{command.name} lacks its Gemini .toml")
try:
    import tomllib
    for toml in (ROOT / "commands").glob("*.toml"):
        data = tomllib.loads(toml.read_text(encoding="utf-8"))
        check({"description", "prompt"} <= set(data), f"{toml.name}: needs description and prompt")
        check("{{args}}" in data.get("prompt", ""), f"{toml.name}: prompt lacks {{{{args}}}}")
except ImportError:
    pass

build = subprocess.run([sys.executable, str(ROOT / "tools" / "build.py"), "--check"], capture_output=True, text=True)
check(build.returncode == 0, "generated files are stale; run tools/build.py\n" + build.stdout)

tests = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", str(SKILL / "tests")], capture_output=True, text=True, cwd=SKILL)
check(tests.returncode == 0, "scanner tests failed:\n" + tests.stderr[-2000:])

for script in (SKILL / "scripts").glob("*.py"):
    try:
        compile(script.read_text(encoding="utf-8"), str(script), "exec")
    except SyntaxError as error:
        errors.append(f"{script.name}: {error}")

if errors:
    print("FAIL")
    for error in errors:
        print(" -", error)
    sys.exit(1)
ran = re.search(r"Ran (\d+) tests?", tests.stderr)
print(f"OK: package checks passed ({ran.group(1) if ran else '?'} scanner tests)")
