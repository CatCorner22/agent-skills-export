# [00] LLM Failure Modes — Living Reference
_Version 1.1 · Owner: Blake Reagan · Scope: recurring failure modes of LLM assistants and coding agents, their mechanisms, and the remedy class for each. Does not cover model benchmarks or pricing._
_Refresh: run `scripts/refresh_reference.py examples/llm-failure-modes.reference.md --stale-days 120` after every edit._

## [01] Attack sheet
- A memory file that Muse Code lists is not in the model's context; the model must open it. §10.01
- Compaction drops what the agent read; long sessions loop on recovery instead of remembering. §10.02
- AGENTS.md is guidance, not enforcement; hooks are the only deterministic layer. §20.01
- Context files cut tokens but do not raise success rates. §20.02
- Ask-vs-assume: ask once up front; mid-task interruptions carry a measurable cost. §30.01
- Any action that must never happen needs a hook, not a sentence. §20.01

## [02] Contents
<!-- toc:start -->
- [00 LLM Failure Modes — Living Reference](#00-llm-failure-modes-living-reference)
- [01 Attack sheet](#01-attack-sheet)
- [03 How to read this file](#03-how-to-read-this-file)
- [10 Resource blindness and re-work](#10-resource-blindness-and-re-work)
  - [10.01 Memory files load on demand, not whole](#1001-memory-files-load-on-demand-not-whole)
  - [10.02 Compaction causes re-read and recovery loops](#1002-compaction-causes-re-read-and-recovery-loops)
- [20 Guidance versus enforcement](#20-guidance-versus-enforcement)
  - [20.01 AGENTS.md is guidance; hooks are enforcement](#2001-agentsmd-is-guidance-hooks-are-enforcement)
  - [20.02 Context files reduce tokens, not failures](#2002-context-files-reduce-tokens-not-failures)
- [30 Interaction policy](#30-interaction-policy)
  - [30.01 Ask once, up front; label cheap assumptions](#3001-ask-once-up-front-label-cheap-assumptions)
- [80 Glossary](#80-glossary)
- [85 Changelog](#85-changelog)
- [90 Sources](#90-sources)
- [91 Cite index](#91-cite-index)
- [92 Index](#92-index)
- [99 Health](#99-health)
<!-- toc:end -->

## [03] How to read this file
- Headings carry stable IDs in brackets; link to them as `§10.02`, never to page or position.
- Cites are short keys like `[S3]` or `[S3 at 2]`; full citations live in §90.
- `Rule`, `Mechanism`, `Test`, `Example`, `Fix`, `Open` labels start lines so you can scan.
- Every rule section ends with `Last verified: YYYY-MM-DD`.

## [10] Resource blindness and re-work
### [10.01] Memory files load on demand, not whole
{{index: resource blindness | project memory; MEMORY.md; memory index; see also: re-read loop}}
**Rule.** At session start, Muse Code injects `MEMORY.md` and a list of up to 48 memory file paths, not their contents; the agent reads each file on demand. [S1]
**Mechanism.** The folder shows the file; the model sees only its path. Opening it is a tool call the model may skip. [S1]
**Test.** Ask "which files have you opened in this session?" before asking for analysis. If the answer omits the file, the model has not read it.
**Example.** Nebula Genomics project: file present in the Medical folder; the assistant proposed re-downloading it. [S5]
**Fix.** Inventory-before-fetch habit; a hook that blocks downloads of files already in the manifest. §20.01
**Open.** No public rate for missed memory reads on Muse Code. [cite needed]
Last verified: 2026-11-18

### [10.02] Compaction causes re-read and recovery loops
{{index: re-read loop | compaction; context eviction; see also: resource blindness}}
**Rule.** When a long Muse session compacts, the agent loses what it read and repeats work; public reports also describe recovery loops after compaction. [S2]
**Example.** One recovery loop wrote 22 MB per turn and 2.1 GB in all. [S2]
**Fix.** A read manifest on disk; the file remembers what the model forgot. §20.01
Last verified: 2026-11-18

## [20] Guidance versus enforcement
### [20.01] AGENTS.md is guidance; hooks are enforcement
{{index: enforcement | hooks; AGENTS.md; rules files; see also: guidance}}
**Rule.** Muse Code is "designed to follow" `AGENTS.md`; a hook can "block an action before it happens." [S1] [S3]
**Test.** If a failure cost more than ten minutes or any data, it belongs in a hook or on-disk state, not in a rule.
Last verified: 2026-11-18

### [20.02] Context files reduce tokens, not failures
{{index: guidance | AGENTS.md; context files; see also: enforcement}}
**Rule.** Two studies find AGENTS.md-style files lower token use or change style without raising task success. [S4]
**Open.** Whether short, trigger-specific skills behave differently from long always-on files.
Last verified: 2026-11-10

## [30] Interaction policy
### [30.01] Ask once, up front; label cheap assumptions
{{index: clarifying questions | ask or assume; interruption cost}}
**Rule.** Clarifying questions improve outcomes when batched before work starts; mid-task interruptions carry a measurable cost to users. [S6]
**Fix.** Ask all legitimate questions in one block; proceed on reversible guesses with "Assumed: X."
Last verified: 2026-11-10

## [80] Glossary
- **Resource blindness** (UF: ignoring project files) — failure to use information or tools already available. §10.01
- **Compaction** (UF: context eviction) — summarizing or dropping earlier context to free the window. §10.02
- **Enforcement** (UF: hooks) — a mechanism that blocks an action regardless of what the model intends. §20.01

## [85] Changelog
- 2026-11-18 v1.1 — Muse Code edition: §10.01, §10.02 and §20.01 rewritten on Muse Code sources.
- 2026-11-10 v1.0 — created from the exhaustive-research report.

## [90] Sources
- [S1] Meta, *Muse Code: Configuration and context*. https://dev.meta.ai/docs/muse-code/configuration. Accessed 2026-11-18. Grade: A.
- [S2] Muse research report, muse-guardrails plugin, `references/research/report.md`, failure modes F7 and F8 (2026-11-10). Grade: C.
- [S3] Meta, *Muse Code: Extending and automating*. https://dev.meta.ai/docs/muse-code/extending. Accessed 2026-11-18. Grade: A.
- [S4] Two arXiv studies on AGENTS.md effectiveness and efficiency (2025–2026). Accessed 2026-11-10. Grade: B.
- [S5] Blake Reagan, session note, 2026-11-10 (Nebula Genomics project). Grade: D.
- [S6] Studies on clarifying-question timing and interruption budgets (2025). Accessed 2026-11-10. Grade: B.

## [91] Cite index
<!-- authorities:start -->
- [S1] Meta, *Muse Code: Configuration and context* → §10.01, 20.01
- [S2] Muse research report, muse-guardrails plugin, `references/research/report.md`, failure mod → §10.02
- [S3] Meta, *Muse Code: Extending and automating* → §20.01
- [S4] Two arXiv studies on AGENTS.md effectiveness and efficiency (2025–2026) → §20.02
- [S5] Blake Reagan, session note, 2026-11-10 (Nebula Genomics project) → §10.01
- [S6] Studies on clarifying-question timing and interruption budgets (2025) → §30.01
<!-- authorities:end -->

## [92] Index
<!-- index:start -->

**A**
- AGENTS.md — *see* guidance
- ask or assume — *see* clarifying questions

**C**
- **clarifying questions** — §30.01
- compaction — *see* re-read loop
- context eviction — *see* re-read loop
- context files — *see* guidance

**E**
- **enforcement** — §20.01 · *see also* guidance

**G**
- **guidance** — §20.02 · *see also* enforcement

**H**
- hooks — *see* enforcement

**I**
- interruption cost — *see* clarifying questions

**M**
- memory index — *see* resource blindness
- MEMORY.md — *see* resource blindness

**P**
- project memory — *see* resource blindness

**R**
- **re-read loop** — §10.02 · *see also* resource blindness
- **resource blindness** — §10.01 · *see also* re-read loop
- rules files — *see* enforcement
<!-- index:end -->

## [99] Health
<!-- health:start -->
_Refreshed 2026-11-19: 18 sections, 6 sources, 5 index terms._
- §10.01 Memory files load on demand, not whole: [cite needed]
<!-- health:end -->
