# 1f916-ai/stocks.now — Muse integration findings

## Source

- **Title:** 1f916-ai/stocks.now — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-11-09
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh/1f916-ai_stocks.now_issues_1.txt`.
- **Source URL / scope:** https://github.com/1f916-ai/stocks.now/issues/1 — muse-spark agents are counted as llama in the family indexes (2026-11-09); 2026-11-09

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark (version unspecified)

## Summary

Muse agents are misclassified as llama in family indexes; this is an application catalog bug. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns model honesty, evaluation awareness or identity behavior; causal reach is limited to the reported setting. `"Notes: the FAMILIES list has no muse entry, so this is a mapping gap, not a data problem on 1F916."` (1f916-ai/stocks.now#1, 2026-11-09; attribution: harness/router-side (application model-family classification); gh/1f916-ai_stocks.now_issues_1.txt L8).
- **Evidence scope:** The retained statement supports the limited takeaway above, not an additional independent observation. `"Notes: the FAMILIES list has no muse entry, so this is a mapping gap, not a data problem on 1F916."` (gh/1f916-ai_stocks.now_issues_1.txt).
- **Evidence ceiling:** No broader measurement or root-cause conclusion can be obtained from this statement alone. `"Notes: the FAMILIES list has no muse entry, so this is a mapping gap, not a data problem on 1F916."` (gh/1f916-ai_stocks.now_issues_1.txt).

## Data/numbers

- `"Notes: the FAMILIES list has no muse entry, so this is a mapping gap, not a data problem on 1F916."`  (1f916-ai/stocks.now#1, 2026-11-09; attribution: harness/router-side (application model-family classification); gh/1f916-ai_stocks.now_issues_1.txt L8).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
- Sparse source: only 1 substantive retained claim(s). Scope/ceiling bullets explain that limitation rather than inventing additional findings.
