# task-contract on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./task-contract --scope user`, or copy the whole folder to `~/.agents/skills/task-contract/` (user) or `.agents/skills/task-contract/` (project). Keep `scripts/` beside `SKILL.md`.
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "At the start of a task you hand to a model, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/contract_check.py` | Muse Code: `python3 <skill folder>/scripts/contract_check.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |
| `templates/task-contract.md` | Copy it into the workspace and fill it in there. |

## Run rules

1. **Put consequential actions behind a stop.** Muse's approval gate leaks (confirmation recall 5/12, F4). List pay, send, cancel, order, post and delete as stop-and-ask in the contract.
2. **Fill gaps with placeholders.** Muse tends to decline rather than guess (F1). Tell it to insert `[X: what is missing]`, finish, and list the placeholders.
3. **Write a stop rule.** Muse repeats loops (F8). Give a maximum number of passes or tool calls.
4. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
5. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
