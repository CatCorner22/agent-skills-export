# long-context-placement on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./long-context-placement --scope user`, or copy the whole folder to `~/.agents/skills/long-context-placement/` (user) or `.agents/skills/long-context-placement/` (project). Keep `scripts/` beside `SKILL.md`.
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "When you lay out a long prompt with documents, instructions, and a question, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/context_layout.py` | Muse Code: `python3 <skill folder>/scripts/context_layout.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |

## Run rules

1. **Retrieval is not session memory.** Meta's MRCR 98% tests retrieval; users report drift over a session (report section 7, F4). Place the instructions and the question as the skill says, and restate them after a compaction.
2. **Trim raw tool output.** Raw JSON floods Muse's window (F6). Summarize or cut tool output before it enters the context.
3. **On Muse, also apply `muse-long-session-hygiene`** for loops and compaction.
4. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
5. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
