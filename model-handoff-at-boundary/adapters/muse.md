# model-handoff-at-boundary on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Install the whole `model-handoff-at-boundary` folder with `muse skills install ./model-handoff-at-boundary --scope user`, or copy it to `<repo>/.agents/skills/model-handoff-at-boundary/`. Check it first with `muse skills validate ./model-handoff-at-boundary`.
- Muse Code loads a skill when someone invokes it or when its skill-recall observer surfaces it. To load this skill every time, add 1 line to the project's `AGENTS.md`: "When work moves from one model, session, or agent to another, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."

## Tool mapping

| The skill says | On Muse |
|---|---|
| `templates/handoff-checkpoint.md` | Copy it into the workspace and fill it in there. |

## Run rules

1. **Hand off in a file, not in memory.** Muse's memory files drift, and it once took the user's name as its own (F6). Write the checkpoint file; tell the next model to read it first.
2. **State roles by name.** Write who the user is and who the agent is in the checkpoint, so a roleplay or identity claim can't carry over (F6, F3).
3. **Check the protocol.** Some Muse routes take only the Responses API, others only Chat Completions (section 4, item 2). Name the route and protocol in the checkpoint.
4. **Use high effort.** At max effort Muse is slow and uses many tokens (F10). Muse Code's default effort is `high` (`--reasoning-effort` or `/effort`), and the Meta provider rejects `none` (https://dev.meta.ai/docs/muse-code/configuration, read 2026-11-18).
