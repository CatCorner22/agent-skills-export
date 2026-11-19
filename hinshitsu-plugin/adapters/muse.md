UNVERIFIED — never run on this surface

# hinshitsu adapter — Muse Code

This file maps tool names. It adds no rule and removes none (rule 0.10). The rules are in `skills/hinshitsu/SKILL.md` (the conductor) and the 6 skills it names; the terms are in `skills/hinshitsu/GLOSSARY.md`.

**Surface this adapter targets:** Muse Code (`muse` in the terminal, and `muse exec` for headless runs).

**Not for:** the Meta AI app and meta.ai. There the model starts sub-agents itself, and neither the user nor the main agent writes their scope, so part 1 fails.

## Capabilities, with sources

Read on 2026-11-18. A vendor changes its product, so rule 0.2 requires a live probe in every run, whatever this table says.

| SWARM-CAPABLE part | What Meta documents | Source |
|---|---|---|
| 1 scope written by the orchestrator | A lead session spawns a subagent and hands it a bounded task. Custom agents are passed with `--agents` as JSON, each with `description`, `prompt`, and optional `model`, `effort`, `tools` and `disallowedTools`. | https://dev.meta.ai/docs/muse-code/extending ; https://dev.meta.ai/docs/muse-code/agents |
| 2 no builder conversation | UNVERIFIED. The task that the lead writes arrives as the subagent's input; the pages don't say whether the subagent also sees the lead's conversation. Test it in the run under rule 0.2. | https://dev.meta.ai/docs/muse-code/agents |
| 3 report returns whole | UNVERIFIED. The lead manages its subagents with native tools; the pages don't say that a report returns unedited. Test it in the run. | https://dev.meta.ai/docs/muse-code/extending |
| 4 identifier | `/subagents` lists running and past subagents, and `muse export` records the model ID each subagent ran on. Whether a report carries a run ID is UNVERIFIED. | https://dev.meta.ai/docs/muse-code/extending ; https://dev.meta.ai/docs/muse-code/agents |
| 5 live test call | UNVERIFIED — never run on this surface. | — |

## Tool mapping

| The skill says | On this surface |
|---|---|
| start a SUB-AGENT (rules 0.2, 1.5) | a subagent spawned by the lead, with the scope as its task; for a fixed role, a custom agent in the `--agents` JSON whose `prompt` is the role file under `templates/roles/` |
| keep an AUDITOR read-only | `disallowedTools` in that agent's definition (for example `write_file` and `edit_file`), or the Read-only permission profile |
| run roles in parallel (rule 13.1) | several subagents at once, or a workflow where the build includes the workflow engine; request worktree isolation for each child that writes |
| read the SUB-AGENT's report (rule 1.6) | the subagent's result; write it to the report file before any other action |
| the identifier of the run (rule 1.6) | the subagent's entry in `/subagents`, or its record in `muse export` |
| RUN FOLDER | `hinshitsu/` at the root of the workspace |
| gauge (rule 24.1) | `python3 skills/hinshitsu-gauge/scripts/gauge.py hinshitsu/` |
| reasoning effort | `--reasoning-effort` or `/effort`; the default is `high`, and the Meta provider rejects `none` |

## Install

- Put the whole `hinshitsu-plugin` folder in the workspace. The 7 skill folders need `scripts/`, `templates/` and `skills/hinshitsu/GLOSSARY.md`; a copy of the skill folders alone is not a supported install.
- Install the plugin with `muse plugins install ./hinshitsu-plugin --scope user` (or `--scope project`); `muse plugins validate ./hinshitsu-plugin` reports `valid` with 7 skills (Muse Code 1.4.23, run 2026-11-18). To use the skills without the plugin, copy each folder under `skills/` to `<repo>/.agents/skills/<skill-id>/`. Check each with `muse skills validate <folder>`.
- `AGENTS.md`: Muse Code loads it at the start of every session (https://dev.meta.ai/docs/muse-code/configuration, read 2026-11-18). Add 1 line: "Before any task that produces something a person will receive, read `skills/hinshitsu/SKILL.md` and follow it."
