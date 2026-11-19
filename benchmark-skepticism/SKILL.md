---
name: benchmark-skepticism
description: "Read any model benchmark, leaderboard or vendor comparison without being misled: exact model ids, who ran it, same harness or not, effort and thinking settings, fallbacks and retries, benchmark and index versions, then translate scores into cost per solved task and first-try pass rate and grade the claim. Use when someone cites a score, says model A beats model B, or a purchase or routing decision rests on a table. Ships a claim worksheet. Scope boundary: your own regression set is skill:model-sanity-regression; routing is skill:model-router."
---

# Benchmark skepticism

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
A post, vendor table or leaderboard compares models and someone wants to act on it.

## Steps
1. Fill `templates/benchmark-claim-worksheet.md` for each row: exact model ids on both sides ("Claude" or "GPT" alone is not a model), who ran it, benchmark and version, harness, effort setting, fallbacks or retries or compaction, index version and date.
2. Mark asymmetric rows: vendor harness for its own model vs "best harness" for others; max effort vs default; one side with retries; scores "with fallback" to older models.
3. Compare index values only from the same index version and date; the same model can move 10+ points between versions.
4. Translate to what you care about: cost per solved task, time per task, first-try pass rate, pass with retries.
5. Run your own probe: 10-20 real tasks from your work through each candidate, same harness and settings, repeated once to measure noise.
6. State the conclusion with a grade (established, probable, contested, single-source, vendor-only) and the row-level caveats that drive it.

## Evidence
- A vendor's launch table used its own harness for its model and "best harness" for others; some competitor rows were marked "with fallback". Vendor footnotes via journalism.
- Same model, different harness: 85.4% vs 91% on Terminal-Bench 2.1. Practitioner report.
- Artificial Analysis index values for one model ranged from 44 to 57 across index versions. Independent.
- Full notes: [references/evidence.md](references/evidence.md)
