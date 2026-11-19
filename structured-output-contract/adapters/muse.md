# structured-output-contract on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./structured-output-contract --scope user`, or copy the whole folder to `~/.agents/skills/structured-output-contract/` (user) or `.agents/skills/structured-output-contract/` (project). Keep `scripts/` beside `SKILL.md`.
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "When a model must return JSON or another fixed format, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/structured_output.py` | Muse Code: `python3 <skill folder>/scripts/structured_output.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |

## Run rules

1. **Expect strict-schema rejections.** Some Muse backends reject or ignore `json_schema` (section 4, item 6). Validate every reply with the script; don't trust the response format flag.
2. **Strip tool markup.** Muse can print tool-call markup as text (item 3). Treat it as a failed reply, not data.
3. **Treat empty `content` as a failure** and retry with a larger `max_tokens` (item 1).
4. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
5. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
