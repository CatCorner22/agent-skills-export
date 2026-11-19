---
name: muse-benchmark-skepticism
description: "Interpret evaluation or leaderboard claims for Muse, Muse Spark, Muse Wonder, Meta AI, or Meta Model API; Scope boundary: skill:claim-evidence-pairing and skill:model-sanity-regression own generic evidence pairing and local regression checks."
---

# Muse benchmark skepticism

## When it fires
Use before citing a Muse number, comparing releases/vendors, interpreting a safety evaluation, or treating a demo/benchmark as production-agent evidence.

## Steps
1. Apply `skill:claim-evidence-pairing`; fill a benchmark record with source/date, exact model/release, route, effort, benchmark version, score/unit, sample/subset, harness, tools, resource limits and judge. Must mark unknown fields and withhold an apples-to-apples ranking until they are resolved.
2. Check whether each model used its own preferred/self-reported harness or a common independent harness and whether results are internal or externally measured; must preserve those differences in the claim rather than averaging incompatible scores.
3. Record max-effort-only reporting and actual availability/cost at the measured time; must not transfer maximum-effort scores to lower-effort/default routes or treat a then-unavailable Wonder API as tested.
4. Inspect LLM judges, partial-credit/pass thresholds and task exclusions. Must label the reported OSWorld 361-task subset without Google Drive, WorldVQA's exclusion of 500 Notable People questions and Terminal-Bench's 6-core/8-GB caps before quoting those tables; do not apply these settings to other runs without checking their methodology.
5. Match Artificial Analysis index versions before calculating a change; must not call a v4→v5 score difference a model regression. Compare within-version, like-for-like runs, then use `skill:model-sanity-regression` for a separate local workload test.
6. For safety/alignment claims, record evaluation awareness and deployment scope; must distinguish Meta's acknowledgement of an effect on a small subset from a claim all scores are invalid. Apollo's full findings were unavailable in this research; do not invent their contents.
7. Publish the qualified number plus missing comparability fields and an appropriately bounded conclusion; must not promote a cost-efficient knowledge-work result into frontier coding, production approval reliability or universal safety.

## Evidence
- **Behavioral F15 (§3) — Established:** Meta evaluation methodology plus independent/practitioner comparisons; mixed harnesses, judges, subsets and resource caps.
- **Behavioral F2 (§3), M1 (§7) — Established:** Meta's acknowledgement of Apollo evaluation-awareness findings; full Apollo report unseen in the research snapshot.
- **Family F12 (§7) — Established; report §5:** route/version trade-offs and index-version non-comparability; **report §2.12 — Probable** for max-effort-only reporting.
- [Report](../../references/research/report.md), [Meta methodology note](../../references/research/knowledge/sources/open-evalmethod.md), [AA Wonder note](../../references/research/knowledge/sources/aa-wonder.md). Numbers are historical evidence, not fresh measurements.
