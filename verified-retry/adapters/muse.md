# verified-retry on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Install the whole `verified-retry` folder with `muse skills install ./verified-retry --scope user`, or copy it to `<repo>/.agents/skills/verified-retry/`. Check it first with `muse skills validate ./verified-retry`.
- Muse Code loads a skill when someone invokes it or when its skill-recall observer surfaces it. To load this skill every time, add 1 line to the project's `AGENTS.md`: "When a model's output must pass a check before you use it, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."

## Tool mapping

| The skill says | On Muse |
|---|---|
| `templates/retry-log.md` | Copy it into the workspace and fill it in there. |

## Run rules

1. **Count empty `content` as a failure** and raise `max_tokens` on retry (section 4, item 1).
2. **Cap retries.** Muse repeats loops (F8). Stop after the budget the skill sets, and report the last failure.
3. **Retry a decline with a placeholder rule.** If Muse declines (F1), retry once with "insert `[X: what is missing]` and finish".
4. **Use high effort.** At max effort Muse is slow and uses many tokens (F10). Muse Code's default effort is `high` (`--reasoning-effort` or `/effort`), and the Meta provider rejects `none` (https://dev.meta.ai/docs/muse-code/configuration, read 2026-11-18).
