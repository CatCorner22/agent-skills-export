# visual-build-loop on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./visual-build-loop --scope user`, or copy the whole folder to `~/.agents/skills/visual-build-loop/` (user) or `.agents/skills/visual-build-loop/` (project).
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "When you build a visual product by rendering and comparing it to a target, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Tool mapping

| The skill says | On Muse |
|---|---|
| `templates/visual-target.md` | Copy it into the workspace and fill it in there. |

## Run rules

1. **Check the route supports images.** Image or tool-call turns crash on some Muse routes, and a vision capability flag is stale (section 4, item 8). Send one test image before the loop.
2. **Cap the loop.** Muse repeats loops (F8). Set the iteration limit before you start.
3. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
