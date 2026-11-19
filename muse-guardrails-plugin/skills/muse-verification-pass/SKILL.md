---
name: muse-verification-pass
description: "Use Muse, Muse Spark, Muse Wonder, Meta AI, or Meta Model API to verify drafts against supplied rules; Scope boundary: skill:claim-evidence-pairing and skill:completion-evidence-gate own generic citations and completion proof."
---

# Muse source-text verification pass

## When it fires
Use for a close-reading second pass on another vendor's draft or a multi-vendor merge, and when choosing a bounded cost-efficient knowledge-work verification task rather than assuming frontier coding or autonomous-agent reliability.

## Steps
1. Apply `skill:claim-evidence-pairing` and clear sensitive inputs under the [privacy skill](../muse-privacy-minimization/SKILL.md) before using Muse; must supply the exact authoritative rule text, jurisdiction/version/effective date, draft and bounded question. A model's recollection of a rule is not source text.
2. Line-number the supplied excerpts deterministically and keep their provenance with them; must retain surrounding exceptions, definitions and cross-references or mark those dependencies missing. Do not send irrelevant confidential source material.
3. Ask Muse for a discrepancy table: draft claim/location, quoted rule text with line range, conflict explanation, proposed minimal correction and confidence; must request “no supported discrepancy” when the source does not justify a change, not a quota of criticisms.
4. Check every quotation and line range against the supplied version and independently resolve exceptions/version ambiguity; must accept a correction only when the quoted rule actually supports it. Reject invented quotes, mismatched dates and claims of authority based only on model agreement.
5. In multi-vendor merges retain competing suggestions as proposals, apply only source-supported edits and record rejected proposals/reasons; must not majority-vote a legal/technical fact or let the verifier become the sole authority on an unresolved interpretation.
6. Use `skill:completion-evidence-gate` on the final artifact and required tests, noting the review's exact coverage and remaining uncertainty; must not describe a narrow verification pass as legal advice or proof the whole deliverable is correct.
7. For workload selection, record actual route availability, effort, measured task cost and review burden; must treat the report's Spark knowledge-work value as a benchmark-specific reason to try this bounded workflow, not a guarantee of cheap/correct answers or a claim Wonder Full had an API at capture time.

## Evidence
- **Report §1.7 — Single-source:** the user's prior ethics-suite vendor merges, including Oregon touch-rule versioning, support a close-reading use case; not re-tested and not an independent accuracy benchmark.
- **Report §1.1–2 — Established for the cited benchmarks:** Artificial Analysis and Meta on Spark cost efficiency/knowledge work; not every model/version/task.
- **Behavioral F1 (§3) — Established:** confident residual errors require verification; **behavioral F15 (§3) — Established** for benchmark comparability limits.
- [Report](../../references/research/report.md), [AA Spark note](../../references/research/knowledge/sources/aa-12.md), [evidence index](../../references/research/evidence-index.md). Corrections require source text, not trust in this historical success.
