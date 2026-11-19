# agent-secret-hygiene on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./agent-secret-hygiene --scope user`, or copy the whole folder to `~/.agents/skills/agent-secret-hygiene/` (user) or `.agents/skills/agent-secret-hygiene/` (project). Keep `scripts/` beside `SKILL.md`.
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "Before an agent session that can read files or run commands, or before sharing a transcript or log, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `scripts/secret_exposure_check.py` | Muse Code: `python3 <skill folder>/scripts/secret_exposure_check.py` with the arguments in `SKILL.md`. The Meta AI app and meta.ai have no shell: do the check by hand, and say it was by hand. |

## Run rules

1. **Assume social engineering works.** Muse's agent tarred and exported its own VM root filesystem in 17 messages under guilt and roleplay pressure (F3). Keep secrets out of the workspace before the session starts; don't rely on the model to refuse.
2. **Cover background workers.** Muse's background "proactivity agent" finished work the main chat refused (F5). Apply the same secret scope to every scheduled or background task.
3. **On Muse, also apply `muse-privacy-minimization`** for personal data. This skill covers credentials and keys.
4. **Confirm every script ran.** On Muse Code, tool calls sometimes come out as plain text and never run (section 4, item 3). Read the script's output and exit status. If you didn't see output, it didn't run; don't report it as run.
5. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
