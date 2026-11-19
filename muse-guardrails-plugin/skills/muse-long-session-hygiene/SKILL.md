---
name: muse-long-session-hygiene
description: "Recover loops, compaction or memory drift in Muse, Muse Spark, Muse Wonder, Meta AI, or Meta Model API; Scope boundary: skill:context-budget-governor and skill:inventory-before-fetch own generic context budgeting and retrieval inventory."
---

# Muse long-session hygiene

## When it fires
Use on repeated grep/search/thinking/review, compaction/recovery cycles, oversized history seeding, disappearing constraints or identity/memory inconsistencies.

## Steps
1. Apply `skill:context-budget-governor` and `skill:inventory-before-fetch`; record the exact Muse surface/harness, current objective and last durable checkpoint. Must use bounded source slices/tool summaries rather than replaying raw history or large JSON dumps.
2. Maintain a progress ledger of action/query, input fingerprint and new evidence/artifact. As a pack policy, two materially identical cycles without new evidence or changed inputs trigger loop containment; must stop repeating the same reasoning/search/review and identify the stalled dependency.
3. Write a minimal durable checkpoint after every completed subtask, at most every five meaningful tool turns, and before compaction/handoff; must include objective, constraints/approvals, verified artifact paths, source references, tests actually run, open issues and the single next action. This cadence is proposed policy, not a measured Muse optimum.
4. Verify saved memory entries against trusted user instructions and source records; must separate user identity from agent persona, reject roleplay-derived identity/permissions, and correct only entries the user has authorized changing. Do not overwrite a user's facts from a generated summary.
5. On continuity loss, compare the live state with the checkpoint and inspect bounded file/version differences; must not claim memory accurately preserved all context or repeat completed work solely because a summary omitted it.
6. If a bounded retry with changed inputs still stalls, stop the affected worker and start a fresh session with the structured checkpoint plus only necessary source excerpts; must not seed an entire transcript, copy backup history repeatedly or recursively call restart_fresh. Stop the restart path if it repeats the same failure.
7. In the new session verify artifact existence, approvals and open questions before continuing one next action; must keep unknown/lost state explicit and measure new progress rather than count restarts as success.

## Evidence
- **Behavioral F7 (§3) — Established:** masc #42597, Goose/OpenCode and Wang; report describes oversized history/recovery accumulation, not a universal safe context limit.
- **Behavioral F8 (§3) — Established:** OpenCode #51649/#57804 and HN nthypes/ekojs report loops; native-harness superiority is reported, not a controlled universal comparison.
- **Behavioral F6 (§3) — Probable:** @jonny/HN/harness memory drift; **behavioral F9 (§3) — Single-source** for self-damaging backup copying and missing reply referents.
- [Report](../../references/research/report.md), [masc source note](../../references/research/knowledge/sources/github-jeong-sik-masc.md), [OpenCode note](../../references/research/knowledge/sources/github-anomalyco-opencode.md). Section-qualified IDs avoid confusing the report's separate family numbering.
