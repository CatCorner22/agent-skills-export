# provider-migration-checklist on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./provider-migration-checklist --scope user`, or copy the whole folder to `~/.agents/skills/provider-migration-checklist/` (user) or `.agents/skills/provider-migration-checklist/` (project). Keep `scripts/` beside `SKILL.md`.
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "Before you move a workload to or from Muse or the Meta Model API, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/usage_normalize.py` | Muse Code: `python3 <skill folder>/scripts/usage_normalize.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |
| `templates/migration-probe.md` | Copy it into the workspace and fill it in there. |

## Run rules

1. **Probe each Muse defect** from report section 4: empty `content` with HTTP 200 (1), Responses vs Chat Completions mismatch (2), tool calls printed as text (3), undeclared tool calls (4), whole floats for integers (5), strict-schema rejections (6), reasoning replay errors (7), image or tool turns crashing (8), blank usage meters (9).
2. **Set a large output budget.** Reasoning can use up `max_tokens` (item 1). One router clamps to at least 8000.
3. **Run `muse-api-integration-check`** on sample responses before you switch traffic.
4. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
5. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
