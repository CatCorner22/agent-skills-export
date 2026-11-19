# verified-retry on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./verified-retry --scope user`, or copy the whole folder to `~/.agents/skills/verified-retry/` (user) or `.agents/skills/verified-retry/` (project).
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "When a model's output must pass a check before you use it, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `templates/retry-log.md` | Copy it into the workspace and fill it in there. |

## Run rules

1. **Count empty `content` as a failure** and raise `max_tokens` on retry (section 4, item 1).
2. **Cap retries.** Muse repeats loops (F8). Stop after the budget the skill sets, and report the last failure.
3. **Retry a decline with a placeholder rule.** If Muse declines (F1), retry once with "insert `[X: what is missing]` and finish".
4. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
