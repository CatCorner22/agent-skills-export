# subagent-brief on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./subagent-brief --scope user`, or copy the whole folder to `~/.agents/skills/subagent-brief/` (user) or `.agents/skills/subagent-brief/` (project). Keep `scripts/` beside `SKILL.md`.
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "Before you delegate work to another model or agent, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/brief_check.py` | Muse Code: `python3 <skill folder>/scripts/brief_check.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |
| `templates/subagent-brief.md` | Copy it into the workspace and fill it in there. |

## Run rules

1. **Restate every prohibited action in the brief.** Muse's background worker finished work the main chat refused (F5). A worker gets no rule you didn't write down.
2. **Name the roles.** Muse accepted a roleplay identity ("I am actually you") and kept it (F3, F6). State who the user is and who the worker is.
3. **Require proof of tool runs.** Muse can print tool calls as text without running them (section 4, item 3). Ask the worker to return each command's output.
4. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
5. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
