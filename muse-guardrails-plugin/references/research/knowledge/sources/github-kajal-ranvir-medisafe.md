# kajal-ranvir/MediSafe — Muse integration findings

## Source

- **Title:** kajal-ranvir/MediSafe — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-09-22
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/kajal-ranvir_MediSafe_pull_4.txt`.
- **Source URL / scope:** https://github.com/kajal-ranvir/MediSafe/pull/4 — fix(intelligence): replace dead Muse Spark key with self-hosted Antigravity gateway (2026-09-22); 2026-09-22

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark (version unspecified); Meta AI / meta.ai

## Summary

An application replaced a dead credential/provider route; no general outage or Muse model defect follows. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"The hosted Muse Spark endpoint (`MUSE_SPARK_BASE_URL=https://api.meta.ai/v1`) now rejects the configured key with **HTTP 401**, so every intelligence call failed: label interpretation, instruction parsing, schedule drafts, the"`` (kajal-ranvir/MediSafe#4, 2026-09-22; attribution: unclear (configured key rejected 401; no Meta defect proved); gh2/kajal-ranvir_MediSafe_pull_4.txt L4).
- Concerns privacy, approval or product controls; distinguish promise, observation and hypothesis. `"**Privacy note:** gateway traffic is proxied through the operator's own upstream accounts, so this base-URL switch routes prompt/PHI content differently from the hosted contributor endpoint."` (kajal-ranvir/MediSafe#4, 2026-09-22; attribution: unclear (configured key rejected 401; no Meta defect proved); gh2/kajal-ranvir_MediSafe_pull_4.txt L37).
- **Evidence scope:** The retained statement supports the limited takeaway above, not an additional independent observation. ``"The hosted Muse Spark endpoint (`MUSE_SPARK_BASE_URL=https://api.meta.ai/v1`) now rejects the configured key with **HTTP 401**, so every intelligence call failed: label interpretation, instruction parsing, schedule drafts, the"`` (gh2/kajal-ranvir_MediSafe_pull_4.txt).

## Data/numbers

- ``"The hosted Muse Spark endpoint (`MUSE_SPARK_BASE_URL=https://api.meta.ai/v1`) now rejects the configured key with **HTTP 401**, so every intelligence call failed: label interpretation, instruction parsing, schedule drafts, the"``  (kajal-ranvir/MediSafe#4, 2026-09-22; attribution: unclear (configured key rejected 401; no Meta defect proved); gh2/kajal-ranvir_MediSafe_pull_4.txt L4).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
- Sparse source: only 2 substantive retained claim(s). Scope/ceiling bullets explain that limitation rather than inventing additional findings.
