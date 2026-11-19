# Agent skills for Muse Code

36 skills and plugins for Muse Code, in 3 groups: keeping the agent on track, quality checks, and good databases. Each `.md` file at the top level is 1 skill's `SKILL.md`, renamed to the skill's name. Each folder is a whole skill or plugin with its scripts, templates and manifests.

## Install on Muse Code

- **A folder skill:** `muse skills install ./<folder>` for every project, or copy the folder to `<repo>/.agents/skills/<folder>/` for 1 repository. Check it first with `muse skills validate ./<folder>`.
- **A single `.md` file:** make a folder with the skill's name, put the file in it, rename the file `SKILL.md`, and install the folder as above.
- **A plugin folder** (the 4 folders that end in `-plugin`): `muse plugins install ./<folder> --scope user` (or `--scope project`). Its `README.md` gives any extra steps.
- **An always-on skill:** Muse Code loads a skill when someone invokes it or when its skill-recall observer surfaces it. For a skill that must apply to every reply, such as `unambiguous-language`, add 1 line to `AGENTS.md`, which Muse Code loads at the start of every session.

All 57 skills pass `muse skills validate` and all 4 plugins pass `muse plugins validate` on Muse Code 1.4.23. Nobody has run a task with them on Muse Code yet. The Muse-specific steps come from Meta's Muse Code documentation (https://dev.meta.ai/docs/muse-code, read 2026-11-18).

## Contents

| Item | Group | What it does |
|---|---|---|
| `after-action-review.md` | On track | Debrief after a task: intended vs actual vs gap vs fix, logged for patterns. |
| `agent-discipline-plugin/` | On track | 16 skills plus `ad.py` hooks that keep an agent honest: ask-or-assume, scope/blast-radius check, evidence gates, context checkpoints, narrow reads. |
| `compound-engineering/` | On track | Brainstorm → plan with definition of done → phased build with checks → senior review → root-cause debug. |
| `deliverable-first.md` | On track | Define the final deliverable first, then work backward to the plan. |
| `improve-system.md` | On track | Turns feedback and repeated problems into permanent fixes to the project's knowledge base and skills. |
| `ooda-lean-loop.md` | On track | Fused OODA and lean loops: observe, orient on a current-state map, decide, act, cut waste. |
| `pipeline-preflight.md` | On track | Pre-run audit that inputs, files, constraints and tools are present; halt instead of running cold. |
| `proactive-agency.md` | On track | Five-step gate that makes the agent do the work instead of handing tasks back to the user. |
| `sterile-cockpit-context.md` | On track | Phase-gated context: parse inputs, work with full history, then validate before landing. |
| `unblock-yourself.md` | On track | When a route is blocked (403, missing tool, failing install), list and try every alternate route before asking. |
| `workspace-mise-en-place.md` | On track | Prepare files, folders, env, tools and references before starting work. |
| `ai-transfer-quality-control.md` | Quality checks | Router for the 9 quality-control techniques below. |
| `chain-of-custody-provenance.md` | Quality checks | Tracks which inputs, tools and turns produced each part of an output. |
| `chicken-little-overwatch-plugin/` | Quality checks | QC and red-team review of AI-made work: requirements, evidence, Adams-style plain language, then an alarm swarm tested by a Defender and Arbiter. |
| `clean-minimal-code.md` | Quality checks | Write clear, minimal code: fewer lines, same behavior, established naming. |
| `double-entry-claims.md` | Quality checks | Every factual claim must carry paired evidence, or it is cut. |
| `five-whys-failure-recovery.md` | Quality checks | On failure, drill five whys to root cause and log a permanent fix. |
| `hinshitsu-plugin/` | Quality checks | 7-skill quality system: user-approved criteria, red cell, 8 independent auditors, coverage ledger, evidence-cited delivery report and progress gauge. |
| `internal-focus-group.md` | Quality checks | Tests a draft on simulated personas of the real recipients before it ships. |
| `journalistic-attribution.md` | Quality checks | Retrieve evidence per claim before writing; attribute inline. |
| `mscd-contracts/` | Quality checks | Reviews, redlines, comments on and drafts contracts to Adams's MSCD5 in Blake's house style; lint, coverage and rule-query scripts; `adapters/muse.md` adds Muse run rules. |
| `one-way-optimal-language/` | Quality checks | Drafts and reviews one-way medical, dental, pharmacy and research text: active voice, R1-R30 ambiguity rubric, plain language; `scripts/av_scan.py`; `adapters/muse.md` adds Muse run rules. |
| `progressive-resistance-critique.md` | Quality checks | Escalating self-critique passes: consistency, alignment, robustness, failure. |
| `proofreading-marks.md` | Quality checks | Annotation pass (QUERY, DELETE, STET, INSERT) between draft and delivery. |
| `real-time-testing.md` | Quality checks | Test continuously while writing: red-green-refactor, watch mode, typecheck and lint. |
| `red-team-lead.md` | Quality checks | Runs an adversarial red-team campaign against a plan, product, prompt, agent or codebase. |
| `review-and-ship.md` | Quality checks | Reviews the branch for bugs, intent fit and test coverage, runs or writes tests, then commits and opens a PR. |
| `rumsfelds-binoculars-plugin/` | Quality checks | Risk reconnaissance: sorts known/unknown knowns and unknowns, then hunts black swans with adversarial models and tail statistics. |
| `skill-library-audit/` | Quality checks | Audits a multi-vendor skill library for routing defects; ships `scripts/audit_skill_library.py`. |
| `stable-architecture.md` | Quality checks | Design code with clear module boundaries and dependency direction so it does not collapse like a house of cards. |
| `stress-test-robustness.md` | Quality checks | Contradiction, edge-case, adversarial and scope tests on a draft before delivery. |
| `survey-triangulation.md` | Quality checks | Requires three independent retrieval paths per fact and scores agreement. |
| `unambiguous-language/` | Quality checks | Blake's always-on language rules: active voice, "might" for possibility, and 3 lists of ambiguous words and MSCD usages with replacements; Muse run rules. |
| `ingest-source.md` | Good databases | Captures any source (URL, PDF, transcript, file) as a structured, indexed note in a persistent knowledge base. |
| `living-reference/` | Good databases | Builds and maintains rule-organized Markdown reference outlines with stable IDs, a sources ledger and regenerated indexes; ships scripts. |
| `supabase-postgres-best-practices/` | Good databases | Postgres schema, index, query and config best practices (works on any Postgres, not only Supabase). |
