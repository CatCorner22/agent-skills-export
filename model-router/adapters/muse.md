# model-router on Muse

Read this file at the start of every run on Muse Code, Muse Spark, Muse Wonder, or the Meta Model API. It adds Muse run rules. It changes no rule in `SKILL.md`.

UNVERIFIED: nobody has run this skill on Muse yet. The failure modes (F1 to F15) and defects (section 4) come from the Muse research report in this repo, `muse-guardrails-plugin/references/research/report.md` (2026-11-10). That report uses public sources, and nobody reproduced its findings.

## Install

- Run `muse skills install ./model-router --scope user`, or copy the whole folder to `~/.agents/skills/model-router/` (user) or `.agents/skills/model-router/` (project).
- Muse Code may not surface project skills (t3code#19155). Add 1 line to the project's `AGENTS.md`: "When you choose which model gets a task, read `<skill folder>/SKILL.md` and `<skill folder>/adapters/muse.md` and follow them."
- Run `muse skills validate` on the folder and fix every error it reports.

## Run rules

1. **Closed-book facts:** Muse declines more often (attempt rate 95% to 67%) (F1). Give it a retrieval tool, or route the question elsewhere.
2. **Consequential actions:** Muse's approval gate leaks (confirmation recall 5/12, F4). Don't route unsupervised pay, send, cancel or post work to Muse. If you do, apply `muse-agent-action-gate`.
3. **Latency:** Muse at max effort has a 26 s time-to-first-token and about 12.9 min per Wonder task (F10). Use high effort, or another model, for interactive work.
4. **Data:** on the contributor tier, Meta may use your content for product improvement (F14). Don't route confidential work to that tier.
5. **Use `high` effort if a route rejects `max`** (`reasoning_effort=max` was rejected on one route, hermes#140813; max effort is also slow, F10).
