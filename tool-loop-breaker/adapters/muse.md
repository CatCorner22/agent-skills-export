# tool-loop-breaker on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Install the whole `tool-loop-breaker` folder with `muse skills install ./tool-loop-breaker --scope user`, or copy it to `<repo>/.agents/skills/tool-loop-breaker/`. Check it first with `muse skills validate ./tool-loop-breaker`. Keep `scripts/` beside `SKILL.md`.
- Muse Code loads a skill when someone invokes it or when its skill-recall observer surfaces it. To load this skill every time, add 1 line to the project's `AGENTS.md`: "When an agent repeats a tool call, keeps reading without editing, or burns tokens without progress, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/loop_detector.py` | Muse Code: `python3 <skill folder>/scripts/loop_detector.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |

## Run rules

1. **Expect loops.** Muse repeats thinking, grep, search and review loops in external harnesses (F8), and one recovery loop wrote 22 MB per turn (F7, masc#42597). Run the detector whenever a session passes 20 tool calls without a write.
2. **Restart from a file.** After a LOOP, write what is known and the next action to a checkpoint file, then start a fresh turn from it; Muse compaction loses detail (F7).
3. **On Muse, also apply `muse-long-session-hygiene`** for compaction and memory drift.
4. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
5. **Use high effort.** At max effort Muse is slow and uses many tokens (F10). Muse Code's default effort is `high` (`--reasoning-effort` or `/effort`), and the Meta provider rejects `none` (https://dev.meta.ai/docs/muse-code/configuration, read 2026-11-18).
