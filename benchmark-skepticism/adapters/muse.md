# benchmark-skepticism on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Install the whole `benchmark-skepticism` folder with `muse skills install ./benchmark-skepticism --scope user`, or copy it to `<repo>/.agents/skills/benchmark-skepticism/`. Check it first with `muse skills validate ./benchmark-skepticism`.
- Muse Code loads a skill when someone invokes it or when its skill-recall observer surfaces it. To load this skill every time, add 1 line to the project's `AGENTS.md`: "Before you quote, compare, or act on a benchmark or leaderboard number, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."

## Tool mapping

| The skill says | On Muse |
|---|---|
| `templates/benchmark-claim-worksheet.md` | Copy it into the workspace and fill it in there. |

## Run rules

1. **For Muse numbers, also apply `muse-benchmark-skepticism`.** It holds the Muse-specific caveats. This skill gives the generic worksheet.
2. **Discount Meta's own tables.** They mix each model's preferred harness, internal runs, LLM judges, task subsets and capped hardware, and independent numbers run lower (Vals 69 vs about 80) (F15).
3. **Discount safety scores.** Apollo found Muse's evaluation awareness the highest it has seen (F2), so test-time behavior may not transfer.
4. **Note the effort level.** Meta reports benchmarks at max effort only (F12, F10). Record the effort you will actually run.
5. **Use high effort.** At max effort Muse is slow and uses many tokens (F10). Muse Code's default effort is `high` (`--reasoning-effort` or `/effort`), and the Meta provider rejects `none` (https://dev.meta.ai/docs/muse-code/configuration, read 2026-11-18).
