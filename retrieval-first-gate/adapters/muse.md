# retrieval-first-gate on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Install the whole `retrieval-first-gate` folder with `muse skills install ./retrieval-first-gate --scope user`, or copy it to `<repo>/.agents/skills/retrieval-first-gate/`. Check it first with `muse skills validate ./retrieval-first-gate`. Keep `scripts/` beside `SKILL.md`.
- Muse Code loads a skill when someone invokes it or when its skill-recall observer surfaces it. To load this skill every time, add 1 line to the project's `AGENTS.md`: "Before you state a number, date, name, price, version, quote or law that a tool could check, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/retrieval_gate_check.py` | Muse Code: `python3 <skill folder>/scripts/retrieval_gate_check.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |

## Run rules

1. **Retrieve instead of declining.** Muse declines more often than it guesses (attempt rate 95% to 67%, F1). When a tool can answer, call it first; don't answer "I can't determine that".
2. **Check, don't recall.** When Muse does answer from memory, its remaining errors are still confident (F1). Run the audit on the transcript before delivery.
3. **Count only tool results you saw.** Muse Code can print a tool call as text without running it (section 4, item 3). A fact counts as retrieved only when a real tool result in the transcript holds it.
4. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
5. **Use high effort.** At max effort Muse is slow and uses many tokens (F10). Muse Code's default effort is `high` (`--reasoning-effort` or `/effort`), and the Meta provider rejects `none` (https://dev.meta.ai/docs/muse-code/configuration, read 2026-11-18).
