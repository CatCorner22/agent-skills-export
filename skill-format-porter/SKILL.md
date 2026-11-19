---
name: skill-format-porter
description: "Convert agent skill folders between Claude, Cursor, Codex and Kimi Code formats and lint them: frontmatter fields, name rules, description length, path placeholders, missing files. Use when installing one skill library in several tools, when a skill does not load in one tool, or before publishing a skill. Ships a converter and linter."
---

# Skill format porter

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
A skill written for one agent tool must run in another, or a skill fails to load.

## Steps
1. Lint first: `python3 scripts/skill_port.py <skill-dir> --target <claude|cursor|codex|kimi> --lint-only`. Errors: missing name or description, non-kebab name, description over 1024 chars or with angle brackets, referenced files that do not exist, unsupported `type` values.
2. Convert: add `--out <dest>`. The script keeps `name` and `description`, maps field aliases, drops fields the target does not read (with a note), and rewrites paths: relative `scripts/...` for Claude, Cursor and Codex; `${KIMI_SKILL_DIR}/scripts/...` for Kimi Code.
3. Read the notes. Where a field was dropped (`allowed-tools`, `disableModelInvocation`, `whenToUse`), move the intent into the body text if it matters.
4. Install in the target's scope: Claude Code `.claude/skills/` or `~/.claude/skills/`; Kimi Code `.agents/skills/` or `~/.agents/skills/`; Cursor and Codex per their docs; `.agents/skills/` is the shared location several tools read.
5. Test one invocation in the target tool before converting the whole library. Then loop the script over every skill folder.
6. Keep one source of truth per skill and regenerate ports; do not hand-edit ports.

## Evidence
- Kimi Code Agent Skills docs: fields, scopes, placeholders. Vendor. https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html
- Kimi resource page on the shared SKILL.md format across tools. Vendor. https://www.kimi.ai/resources/agent-skills
- Claude skill rules (name and description required, 1024-char description) from Anthropic's skill documentation; confirm current limits before publishing.
- Converter tested on this pack's own skills, not inside each target tool.
- Full research notes: [references/evidence.md](references/evidence.md)
