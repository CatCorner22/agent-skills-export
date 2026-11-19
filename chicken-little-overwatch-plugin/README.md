# Chicken Little Overwatch Plugin

Chicken Little Overwatch checks work that an AI helped produce: apps, documents, policies, procedures, research summaries, and prompts. It runs requirement, evidence, and execution checks. It enforces a plain-language, active-voice writing standard (Ken Adams style and the R1-R30 ambiguity rubric). Then it runs a red-team swarm that raises every alarm it can back with evidence. A Defender and an Arbiter test whether each alarm holds up, and only the owner accepts a risk.

This edition runs on Muse Code. Its skill follows the Agent Skills format, and `agents.json` defines the swarm roles as Muse Code custom agents.

## Contents

| Path | Purpose |
|---|---|
| `skills/chicken-little-overwatch/` | The skill: `SKILL.md`, references, scanners, and tests. It also ships alone as `chicken-little-overwatch.zip`. |
| `agents/clo-*.md` | 8 swarm roles: A1-A6, the Arbiter, and the Defender. `tools/build.py` generates them. |
| `agents.json` | The same 8 roles as Muse Code custom agents, each barred from `write_file` and `edit_file`. `tools/build.py` generates it. |
| `commands/overwatch-review.md` | Prompt for a full review. Replace `$ARGUMENTS` with the target. |
| `commands/overwatch-red-team.md` | Prompt for the red-team swarm only |
| `plugin.json` | Plugin manifest |
| `tools/build.py`, `tools/validate.py` | Rebuild the generated files and the zips; check the package |
| `assets/icon.png` | Plugin icon |

## Use on Muse Code

- Install the skill: `muse skills install ./chicken-little-overwatch-plugin/skills/chicken-little-overwatch --scope user`, or copy the folder to `<repo>/.agents/skills/chicken-little-overwatch/`. Check it first with `muse skills validate`.
- Start Muse Code with the swarm roles: `muse --agents "$(cat chicken-little-overwatch-plugin/agents.json)"`. For a headless run, pass the same flag to every `muse exec`. Muse Code doesn't save the definitions between runs.
- Ask for a review, QC, audit, fact-check, proofread, plain-language rewrite, or red team, or invoke the skill with its slash shortcut. The skill's description routes the request.
- `skills/chicken-little-overwatch/references/hosts.md` covers runs without subagents, without a shell, or in the Meta AI app.

## Edit and rebuild

Edit only the sources: `SKILL.md`, the files in `references/`, the scripts, and `commands/*.md`. Then run:

    python3 tools/build.py --dist ../dist
    python3 tools/validate.py

`build.py` regenerates `agents/` and `agents.json`. `validate.py` fails when a generated file is stale.

## Known limits

- The bundled active-voice scanner uses the writing standard's fallback patterns. It flags more than it needs to, so the eye check stays mandatory.
- The writing standard's legal statements, research figures, and benchmark results are source claims with a last-check date of 9 November 2026. This package does not re-verify them.
- One model that plays every swarm role shares its own blind spots. Set a different `model` for the Defender and the Arbiter in `agents.json` when your account offers one.
- The Defender calibration thresholds in D13 are judgment calls. Tune them after real runs.
- Nobody has run `agents.json` on Muse Code yet. Muse Code starts with an invalid definition but can't spawn that agent, so check `/subagents` after the first spawn.
