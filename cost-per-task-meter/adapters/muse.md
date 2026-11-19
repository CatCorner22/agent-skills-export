# cost-per-task-meter on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Install the whole `cost-per-task-meter` folder with `muse skills install ./cost-per-task-meter --scope user`, or copy it to `<repo>/.agents/skills/cost-per-task-meter/`. Check it first with `muse skills validate ./cost-per-task-meter`. Keep `scripts/` beside `SKILL.md`.
- Muse Code loads a skill when someone invokes it or when its skill-recall observer surfaces it. To load this skill every time, add 1 line to the project's `AGENTS.md`: "When you price a model, compare routes, or report what a task cost, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/cost_meter.py` | Muse Code: `python3 <skill folder>/scripts/cost_meter.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |

## Run rules

1. **Count empty replies as failures.** Reasoning tokens can use up `max_tokens` and return empty `content` with HTTP 200, and routers count that as success (section 4, item 1). Count the tokens and the retry.
2. **Expect high token use at max effort.** Muse used 123M tokens on the AA Index against a 72.8M median (report section 7, F2). Meter each effort level separately.
3. **Usage fields may be blank.** Muse usage meters and `/usage` return no data on several routes (section 4, item 9). Fall back to token counts from the response body, and say so.
4. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
5. **Use high effort.** At max effort Muse is slow and uses many tokens (F10). Muse Code's default effort is `high` (`--reasoning-effort` or `/effort`), and the Meta provider rejects `none` (https://dev.meta.ai/docs/muse-code/configuration, read 2026-11-18).
