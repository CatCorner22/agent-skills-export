# Agent skills for Muse Code

63 skills and plugins for Muse Code, in 3 groups: keeping the agent on track, quality checks, and good databases. Each `.md` file at the top level is 1 skill's `SKILL.md`, renamed to the skill's name. Each folder is a whole skill or plugin with its scripts, templates and manifests.

## Install on Muse Code

- **A folder skill:** `muse skills install ./<folder> --scope user` for every project, or copy the folder to `<repo>/.agents/skills/<folder>/` for 1 repository. Check it first with `muse skills validate ./<folder>`.
- **A single `.md` file:** make a folder with the skill's name, put the file in it, rename the file `SKILL.md`, and install the folder as above.
- **A plugin folder** (the 5 folders that end in `-plugin`): its `README.md` gives the steps; `muse-guardrails-plugin/` uses `./install-muse.sh` instead. Install each folder under its `skills/` folder as a skill.
- **An always-on skill:** Muse Code loads a skill when someone invokes it or when its skill-recall observer surfaces it. For a skill that must apply to every reply, such as `unambiguous-language`, add 1 line to `AGENTS.md`, which Muse Code loads at the start of every session.

Nobody has run these skills on Muse Code yet. The Muse-specific steps come from Meta's Muse Code documentation (https://dev.meta.ai/docs/muse-code, read 2026-11-18).

## Contents

| Item | Group | What it does |
|---|---|---|
| `after-action-review.md` | On track | Debrief after a task: intended vs actual vs gap vs fix, logged for patterns. |
| `agent-discipline-plugin/` | On track | 16 skills plus `ad.py` hooks that keep an agent honest: ask-or-assume, scope/blast-radius check, evidence gates, context checkpoints, narrow reads. |
| `agent-secret-hygiene/` | On track | Keep credentials out of model reach on any platform: scan the environment a model or sub-agent process inherits, prompts and briefs for secret literals, install commands and authority claims, and transcripts for secrets echoed by the model or tools and for env-file reads. `adapters/muse.md` adds Muse run rules. |
| `compound-engineering/` | On track | Brainstorm → plan with definition of done → phased build with checks → senior review → root-cause debug. |
| `cost-per-task-meter/` | On track | Measure what a model actually costs per successful task from usage logs in OpenAI, Anthropic or Gemini shape: reasoning-token share, cache-hit share, cache-write cost, success rate and dollars per success, with flags for reasoning-dominated output, broken prefix caching, failures at the cheapest effort setting and mid-task model switches. `adapters/muse.md` adds Muse run rules. |
| `deliverable-first.md` | On track | Define the final deliverable first, then work backward to the plan. |
| `improve-system.md` | On track | Turns feedback and repeated problems into permanent fixes to the project's knowledge base and skills. |
| `long-context-placement/` | On track | Lay out long prompts so any model can use them: instructions in the system prompt with critical rules repeated at the end, the question restated after large documents, labeled sections and an index for middle content, chunks under a per-model threshold, dynamic fields out of the cached prefix, newest user turn last. `adapters/muse.md` adds Muse run rules. |
| `model-handoff-at-boundary/` | On track | Switch models or providers only at artifact boundaries (a file, diff, report, checkpoint), never mid-thread, because reasoning history is provider-bound and replayed differently; write a handoff checkpoint and start the new model fresh. `adapters/muse.md` adds Muse run rules. |
| `model-router/` | On track | Choose which model gets a task from how the output will be verified, cost per solved task, latency, data constraints and language, using a maintained routing table across Claude, GPT, Gemini, Kimi, GLM and other models. `adapters/muse.md` adds Muse run rules. |
| `ooda-lean-loop.md` | On track | Fused OODA and lean loops: observe, orient on a current-state map, decide, act, cut waste. |
| `pii-minimization-before-send/` | On track | Redact personal data (emails, phones, SSNs, Luhn-valid card numbers, IBANs, dates of birth, street addresses, IPs, and listed names) from text before it goes to any hosted model, replacing each value with a stable token and keeping a local re-identification map, so the model can still reason about who is who. `adapters/muse.md` adds Muse run rules. |
| `pipeline-preflight.md` | On track | Pre-run audit that inputs, files, constraints and tools are present; halt instead of running cold. |
| `proactive-agency.md` | On track | Five-step gate that makes the agent do the work instead of handing tasks back to the user. |
| `prompt-cache-prefix-design/` | On track | Design request layouts that hit provider prompt caches on Anthropic, OpenAI, Kimi and similar APIs: stable prefix first, dynamic fields last, fixed settings, measured hit rate. `adapters/muse.md` adds Muse run rules. |
| `provider-migration-checklist/` | On track | Move an application between model providers or hosts (OpenAI, Anthropic, Google, Moonshot, Bedrock, Foundry, OpenRouter, self-host) without silent regressions: a parity table for context, max tokens, reasoning controls, history round-trip, tool and structured-output rules, caching, usage field names, rate-limit units, unsupported parameters and data terms, plus a repeat-measured probe and a usage-field normalizer. `adapters/muse.md` adds Muse run rules. |
| `rate-limit-budgeter/` | On track | Plan request rates against any provider's TPM/RPM limits (counting max output tokens at admission where the provider reserves on them) and classify 429-class errors into capacity, limit, quota or configuration with the fix for each (OpenAI, Anthropic, Google, Moonshot, gateways), plus a jittered backoff schedule. `adapters/muse.md` adds Muse run rules. |
| `skill-format-porter/` | On track | Convert agent skill folders between Claude, Cursor, Codex and Kimi Code formats and lint them: frontmatter fields, name rules, description length, path placeholders, missing files. `adapters/muse.md` adds Muse run rules. |
| `sterile-cockpit-context.md` | On track | Phase-gated context: parse inputs, work with full history, then validate before landing. |
| `task-contract/` | On track | Write the task to any model as a contract: job, finish line with runnable checks, an effective-instructions block that replaces earlier instructions, boundaries, harness-owned state, inputs present, output shape and a numbered stop rule. `adapters/muse.md` adds Muse run rules. |
| `tool-inventory-control/` | On track | Keep the set of tools sent to a model small, distinct and well described, loading the rest on demand. Works with any tool-calling API or MCP setup. `adapters/muse.md` adds Muse run rules. |
| `tool-loop-breaker/` | On track | Detect and break repeated identical tool-call loops in any agent transcript (OpenAI tool_calls or Anthropic tool_use): the same read over and over, read-only stalls with no edits, and harness rejection messages that provoke re-calls. `adapters/muse.md` adds Muse run rules. |
| `tool-schema-sanitizer/` | On track | Rewrite MCP and function tool definitions so strict providers accept them: invalid or digit-leading names, untyped anyOf/oneOf unions, $ref outside $defs, rejected validation keywords, untyped properties, duplicate names, missing descriptions, with per-provider profiles (strict, openai, anthropic, gemini, moonshot). `adapters/muse.md` adds Muse run rules. |
| `unblock-yourself.md` | On track | When a route is blocked (403, missing tool, failing install), list and try every alternate route before asking. |
| `untrusted-content-quarantine/` | On track | Wrap web pages, PDF extracts, emails, search results and tool outputs as tagged, data-only content before they enter any model's prompt, strip hidden characters, and flag injection-shaped text (override instructions, role markers, tool-call JSON, exfiltration asks, invisible CSS). `adapters/muse.md` adds Muse run rules. |
| `workspace-mise-en-place.md` | On track | Prepare files, folders, env, tools and references before starting work. |
| `ai-transfer-quality-control.md` | Quality checks | Router for the 9 quality-control techniques below. |
| `benchmark-skepticism/` | Quality checks | Read any model benchmark, leaderboard or vendor comparison without being misled: exact model ids, who ran it, same harness or not, effort and thinking settings, fallbacks and retries, benchmark and index versions, then translate scores into cost per solved task and first-try pass rate and grade the claim. `adapters/muse.md` adds Muse run rules. |
| `chain-of-custody-provenance.md` | Quality checks | Tracks which inputs, tools and turns produced each part of an output. |
| `chicken-little-overwatch-plugin/` | Quality checks | QC and red-team review of AI-made work: requirements, evidence, Adams-style plain language, then an alarm swarm tested by a Defender and Arbiter. |
| `citation-liveness-check/` | Quality checks | Verify that the citations in any model-written draft are real, reachable and say what the draft says: static checks for placeholder URLs, duplicate links under different claims, malformed DOIs, quotes and references with no link; optional fetch that reports HTTP status, redirects and whether each quoted passage appears on the page. `adapters/muse.md` adds Muse run rules. |
| `clean-minimal-code.md` | Quality checks | Write clear, minimal code: fewer lines, same behavior, established naming. |
| `compute-not-recall/` | Quality checks | Route every count, sum, percentage, difference, unit conversion and date span through code instead of the model's head, and recompute the arithmetic stated in a finished draft (inline equations, percent-of statements, from-to changes, table total rows, day counts) to flag mismatches. `adapters/muse.md` adds Muse run rules. |
| `five-whys-failure-recovery.md` | Quality checks | On failure, drill five whys to root cause and log a permanent fix. |
| `hinshitsu-plugin/` | Quality checks | 7-skill quality system: user-approved criteria, red cell, 8 independent auditors, coverage ledger, evidence-cited delivery report and progress gauge. |
| `internal-focus-group.md` | Quality checks | Tests a draft on simulated personas of the real recipients before it ships. |
| `mscd-contracts/` | Quality checks | Reviews, redlines, comments on and drafts contracts to Adams's MSCD5 in Blake's house style; lint, coverage and rule-query scripts; `adapters/muse.md` adds Muse run rules. |
| `muse-guardrails-plugin/` | Quality checks | 8 Muse guardrails: abstention, agent actions, injection, privacy, API defects, benchmark claims, long sessions, verification passes. `./install-muse.sh` installs them into `~/.agents` (or a repo's `.agents`) with their research references. |
| `one-way-optimal-language/` | Quality checks | Drafts and reviews one-way medical, dental, pharmacy and research text: active voice, R1-R30 ambiguity rubric, plain language; `scripts/av_scan.py`; `adapters/muse.md` adds Muse run rules. |
| `output-language-lock/` | Quality checks | Keep any model's answer in the requested language and script when prompts, sources or tools are in another language: lock the language in the system prompt, keep code and identifiers out of the rule, and measure the script share of the output, ignoring code blocks and URLs. `adapters/muse.md` adds Muse run rules. |
| `progressive-resistance-critique.md` | Quality checks | Escalating self-critique passes: consistency, alignment, robustness, failure. |
| `proofreading-marks.md` | Quality checks | Annotation pass (QUERY, DELETE, STET, INSERT) between draft and delivery. |
| `real-time-testing.md` | Quality checks | Test continuously while writing: red-green-refactor, watch mode, typecheck and lint. |
| `red-team-lead.md` | Quality checks | Runs an adversarial red-team campaign against a plan, product, prompt, agent or codebase. |
| `restraint-pass/` | Quality checks | Strip over-claiming from a draft before delivery: absolutes, intensifiers, superlatives, numbers the brief does not support, certainty beyond the evidence. Works on any model's output. `adapters/muse.md` adds Muse run rules. |
| `retrieval-first-gate/` | Quality checks | Before stating any fact a tool could check, retrieve it: decide retrieve-or-recall, force the first tool call, and audit transcripts for facts stated from memory. Works with any model and agent framework. `adapters/muse.md` adds Muse run rules. |
| `review-and-ship.md` | Quality checks | Reviews the branch for bugs, intent fit and test coverage, runs or writes tests, then commits and opens a PR. |
| `rumsfelds-binoculars-plugin/` | Quality checks | Risk reconnaissance: sorts known/unknown knowns and unknowns, then hunts black swans with adversarial models and tail statistics. |
| `skill-library-audit/` | Quality checks | Audits a multi-vendor skill library for routing defects; ships `scripts/audit_skill_library.py`. |
| `source-freshness-check/` | Quality checks | Date every source and flag anything older than the topic's half-life or undated before relying on it. `adapters/muse.md` adds Muse run rules. |
| `stable-architecture.md` | Quality checks | Design code with clear module boundaries and dependency direction so it does not collapse like a house of cards. |
| `stress-test-robustness.md` | Quality checks | Contradiction, edge-case, adversarial and scope tests on a draft before delivery. |
| `structured-output-contract/` | Quality checks | Make model JSON output parse and conform on any provider: normalize the schema to the strict subset (all required, additionalProperties false, optional fields nullable, rejected keywords dropped), validate the returned JSON against it, strip fences and prose, and run one bounded repair pass with a generated repair prompt. `adapters/muse.md` adds Muse run rules. |
| `style-guide-lock/` | Quality checks | Load a house style once as a rules file and check every draft against it rule by rule: sentence length, banned words, required terms, passive voice, forbidden patterns. `adapters/muse.md` adds Muse run rules. |
| `survey-triangulation.md` | Quality checks | Requires three independent retrieval paths per fact and scores agreement. |
| `temporal-grounding/` | Quality checks | Give any model the date, its training cutoff and the rule that time-sensitive facts need a fetched, dated source, and scan drafts for undated relative-time language (currently, latest, recently, this year), future years stated as fact and stale years called current. `adapters/muse.md` adds Muse run rules. |
| `test-tamper-audit/` | Quality checks | Audit a diff from any coding agent for test gaming before accepting a pass: deleted or shrunken test files, skip markers, weakened or removed assertions, hard-coded expected values, mocks added to production code. `adapters/muse.md` adds Muse run rules. |
| `unambiguous-language/` | Quality checks | Blake's always-on language rules: active voice, "might" for possibility, and 3 lists of ambiguous words and MSCD usages with replacements; Muse run rules. |
| `verified-retry/` | Quality checks | Run model work as generate, check with an external verifier the model cannot edit, then retry with the failure text, within a budget, so pass@k becomes reliable output on any model; review each passing diff for test gaming before accepting. `adapters/muse.md` adds Muse run rules. |
| `visual-build-loop/` | Quality checks | Run any vision-capable model in a build, render, compare-to-target, fix loop for frontends, dashboards, charts, slides, games and 3D scenes, with behavior and data checks so looks-right does not pass for works-right. `adapters/muse.md` adds Muse run rules. |
| `ingest-source.md` | Good databases | Captures any source (URL, PDF, transcript, file) as a structured, indexed note in a persistent knowledge base. |
| `living-reference/` | Good databases | Builds and maintains rule-organized Markdown reference outlines with stable IDs, a sources ledger and regenerated indexes; ships scripts. |
| `supabase-postgres-best-practices/` | Good databases | Postgres schema, index, query and config best practices (works on any Postgres, not only Supabase). |


## Muse pairs

3 skills share a topic with a Muse guardrail. They split the work: the skill holds the script, and its `adapters/muse.md` sends the run to the guardrail too. The pairs are `benchmark-skepticism` + `muse-benchmark-skepticism`, `pii-minimization-before-send` + `muse-privacy-minimization`, and `untrusted-content-quarantine` + `muse-injection-hygiene`.

## Redundant skills: kept the better one

| Kept | Removed | Why the kept one is as good or better |
|---|---|---|
| `retrieval-first-gate/` (new) | `journalistic-attribution.md` | Both retrieve before writing. The new one also forces the first tool call and ships a transcript audit script. Inline attribution is covered by `claim-evidence-pairing`. |
| `claim-evidence-pairing` (agent-discipline) | `double-entry-claims.md` | Both pair every claim with evidence. The kept one adds a fixed format, a 5-level confidence scale, quoted tool output and `ad.py provenance audit`. |
| `task-contract/` (new) | `subagent-brief` (new) | Both write a stand-alone brief with named inputs, a stop rule and a check script. The kept one adds the effective-instructions block and harness-owned state; it now also has the sub-agent JSON evidence return and the Muse sub-agent rules. |
| `claim-evidence-pairing` (agent-discipline) | `calibrated-abstention` (new, not added) | Same labels and "unknown is valid" rule, with a finer confidence scale and provenance tooling. |
| `deliverable-first.md` | `spec-thickening` (new, not added) | Covers acceptance criteria, contracts and UI state maps before code, in more depth. |
| `scope-and-blast-radius-check` (agent-discipline) | `agent-hooks-guardrails` (new, not added) | Its scope-fence hook blocks the same destructive commands on Muse Code; the other's templates are for Claude Code, Cursor and Kimi. |

Kept both, because each does a different job: `tool-loop-breaker` (finds loops in a transcript) and `tool-call-validator` (checks each call); `source-freshness-check` (dates of sources) and `temporal-grounding` (today's date and time words in a draft); and the 3 Muse pairs above (script vs Muse policy).
