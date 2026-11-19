# tool-inventory-control on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Install the whole `tool-inventory-control` folder with `muse skills install ./tool-inventory-control --scope user`, or copy it to `<repo>/.agents/skills/tool-inventory-control/`. Check it first with `muse skills validate ./tool-inventory-control`. Keep `scripts/` beside `SKILL.md`.
- Muse Code loads a skill when someone invokes it or when its skill-recall observer surfaces it. To load this skill every time, add 1 line to the project's `AGENTS.md`: "When you choose the tools a model sees, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/tool_inventory_check.py` | Muse Code: `python3 <skill folder>/scripts/tool_inventory_check.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |

## Run rules

1. **Declare every tool the model may call.** Muse called tools the client never declared (section 4, item 4). Reject undeclared calls.
2. **Keep the set small.** Tool misuse is Muse's best-documented failure family (report section 7, F10).
3. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
4. **Use high effort.** At max effort Muse is slow and uses many tokens (F10). Muse Code's default effort is `high` (`--reasoning-effort` or `/effort`), and the Meta provider rejects `none` (https://dev.meta.ai/docs/muse-code/configuration, read 2026-11-18).
