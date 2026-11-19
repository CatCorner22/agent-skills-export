# Chicken Little Overwatch Plugin

Chicken Little Overwatch checks work that an AI helped produce: apps, documents, policies, procedures, research summaries, and prompts. It runs requirement, evidence, and execution checks. It enforces a plain-language, active-voice writing standard (Ken Adams style and the R1-R30 ambiguity rubric). Then it runs a red-team swarm that raises every alarm it can back with evidence. A Defender and an Arbiter test whether each alarm holds up, and only the owner accepts a risk.

The plugin works with any model. Its skill follows the Agent Skills format, its root `plugin.json` follows the Agent Plugins standard, and it adds manifests for Claude Code, Cursor, Gemini CLI, and Devin.

## Contents

| Path | Purpose |
|---|---|
| `skills/chicken-little-overwatch/` | The skill: `SKILL.md`, references, scanners, and tests. It also ships alone as `chicken-little-overwatch.zip`. |
| `agents/clo-*.md` | 8 swarm roles: A1-A6, the Arbiter, and the Defender. `tools/build.py` generates them. |
| `commands/overwatch-review.*` | Full review. The `.md` file serves Claude Code and Cursor; the `.toml` file serves Gemini CLI. |
| `commands/overwatch-red-team.*` | Red-team swarm only |
| `plugin.json` | Agent Plugins manifest (Codex, VS Code, Cursor, and other hosts that follow the standard) |
| `.claude-plugin/`, `.cursor-plugin/`, `.devin-plugin/`, `gemini-extension.json` | Host manifests |
| `tools/build.py`, `tools/validate.py` | Rebuild the generated files and the zips; check the package |
| `assets/icon.png` | Plugin icon |

## Use

- Claude Code: `claude --plugin-dir ./chicken-little-overwatch-plugin`, then `/chicken-little-overwatch-plugin:overwatch-review FILE` or `/chicken-little-overwatch-plugin:overwatch-red-team FILE`.
- Gemini CLI: `gemini extensions install ./chicken-little-overwatch-plugin`, then `/overwatch-review FILE`.
- Other hosts, and the skill alone: see `skills/chicken-little-overwatch/references/hosts.md`.
- Any host: ask for a review, QC, audit, fact-check, proofread, plain-language rewrite, or red team, and the skill's description routes the request.

## Edit and rebuild

Edit only the sources: `SKILL.md`, the files in `references/`, the scripts, and `commands/*.md`. Then run:

    python3 tools/build.py --dist ../dist
    python3 tools/validate.py

`build.py` regenerates `agents/` and `commands/*.toml`. `validate.py` fails when a generated file is stale.

## Known limits

- The bundled active-voice scanner uses the writing standard's fallback patterns. It flags more than it needs to, so the eye check stays mandatory.
- The writing standard's legal statements, research figures, and benchmark results are source claims with a last-check date of 9 November 2026. This package does not re-verify them.
- One model that plays every swarm role shares its own blind spots.
- The Defender calibration thresholds in D13 are judgment calls. Tune them after real runs.
- Each agent file carries only `name` and `description`, because Gemini CLI (tested on version 0.68.0) rejects any other key. Rule S1 states the read-only limit in words. For a Claude-only install, run `python3 tools/build.py --claude-tools` to add `tools` lines that Claude Code enforces.
