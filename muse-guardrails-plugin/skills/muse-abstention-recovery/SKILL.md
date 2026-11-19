---
name: muse-abstention-recovery
description: "Recover declines or uncertain answers from Muse, Muse Spark, Muse Wonder, Meta AI, or Meta Model API; Scope boundary: skill:premise-check, skill:ask-or-assume, and skill:claim-evidence-pairing own generic premise, clarification, and citation checks."
---

# Muse abstention recovery

## When it fires
Use when Muse declines, says it cannot determine an answer, or its lower-hallucination claim is treated as proof of greater factual knowledge; also use before trusting a confident math, itinerary or factual answer.

## Steps
1. Apply the existing generic skills named in the scope boundary, then record the exact question, model/version, route and available sources; must distinguish the personal agent from a bare API answer.
2. Classify the decline as missing evidence/access, genuinely unresolved or conflicting evidence, a safety refusal, or possibly recoverable over-abstention; must label an unsupported classification tentative rather than claiming to know Muse's internal reason.
3. For a recoverable case, supply the relevant source excerpts, dates and permitted tool results and re-ask the bounded question; must not repeat an unchanged prompt or pressure Muse to guess or bypass a safety refusal.
4. Request an answer plus a confidence label and pinpoint citation for each material claim, or an explicit unknown plus the missing evidence; must permit a justified abstention if the sources still do not decide the question.
5. Independently recompute important math and verify travel dates, operating hours, routes and factual assertions against authoritative sources; must not treat a confident tone, another unsupported model answer or a plausible citation as corroboration.
6. As a pack policy, cap recovery at two materially different, source-backed attempts, then return the bounded answer or unresolved gap; must retain what changed and must not silently convert an abstention to success.

## Evidence
- **Behavioral F1 (§3), M3 (§7) — Established:** Artificial Analysis plus HN reports; report §1.4 records attempt rate 95→67% alongside lower hallucination and lower accuracy, not improved knowledge across all questions.
- **Behavioral F1 (§3) — Established at theme level:** HN math/travel/Seattle examples remain reported cases, not a measured personal error rate; the recovery cap above is proposed policy, not an evaluated fix.
- [Report](../../references/research/report.md), [evidence index](../../references/research/evidence-index.md), [AA source note](../../references/research/knowledge/sources/aa-12.md). Snapshot 2026-11-10; no local Muse reproduction.
