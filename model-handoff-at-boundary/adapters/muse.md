# model-handoff-at-boundary on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./model-handoff-at-boundary --scope user`, or copy the whole folder to `~/.agents/skills/model-handoff-at-boundary/` (user) or `.agents/skills/model-handoff-at-boundary/` (project).
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "When work moves from one model, session, or agent to another, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `templates/handoff-checkpoint.md` | Copy it into the workspace and fill it in there. |

## Run rules

1. **Hand off in a file, not in memory.** Muse's memory files drift, and it once took the user's name as its own (F6). Write the checkpoint file; tell the next model to read it first.
2. **State roles by name.** Write who the user is and who the agent is in the checkpoint, so a roleplay or identity claim can't carry over (F6, F3).
3. **Check the protocol.** Some Muse routes take only the Responses API, others only Chat Completions (section 4, item 2). Name the route and protocol in the checkpoint.
4. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
