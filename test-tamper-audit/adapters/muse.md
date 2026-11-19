# test-tamper-audit on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./test-tamper-audit --scope user`, or copy the whole folder to `~/.agents/skills/test-tamper-audit/` (user) or `.agents/skills/test-tamper-audit/` (project). Keep `scripts/` beside `SKILL.md`.
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "After an agent changes code and its tests, before you accept that tests pass, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/test_tamper_check.py` | Muse Code: `python3 <skill folder>/scripts/test_tamper_check.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |

## Run rules

1. **Distrust success reports.** Muse harnesses have reported false success, such as empty replies counted as passes (report section 7, F7). Run the audit after every agent pass.
2. **Check that the tests ran.** Muse can print a test command as text without running it (section 4, item 3). Require the runner's output.
3. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
4. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
