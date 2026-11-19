# TableProApp/TablePro — Muse integration findings

## Source

- **Title:** TableProApp/TablePro — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-11-06
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh/TableProApp_TablePro_issues_4070.txt`.
- **Source URL / scope:** https://github.com/TableProApp/TablePro/issues/4070 — Meta Model API (Muse Spark, Muse Wonder) as an AI provider (2026-11-06); 2026-11-06

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark (version unspecified); Muse Wonder / Full where specified; Meta Model API

## Summary

Provider-integration gaps and model presets concern the TablePro client, not demonstrated Muse model defects. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Missing TablePro preset; harness/router-side integration gap, not a model defect. `"Using them today means adding a Custom provider and typing the endpoint and model ID by hand."` (TableProApp/TablePro#4070, 2026-11-06; attribution: harness/router-side (provider-preset feature request; not observed model defect); gh/TableProApp_TablePro_issues_4070.txt L4).
- API reasoning restriction reported in feature request. ``"`none` returns 400."`` (TableProApp/TablePro#4070, 2026-11-06; attribution: harness/router-side (provider-preset feature request; not observed model defect); gh/TableProApp_TablePro_issues_4070.txt L18).
- Contributor privacy tradeoff reported, not independently measured. ``"`-contributor` variants are cheaper but Meta may train on the content."`` (TableProApp/TablePro#4070, 2026-11-06; attribution: harness/router-side (provider-preset feature request; not observed model defect); gh/TableProApp_TablePro_issues_4070.txt L17).

## Data/numbers

- ``"`none` returns 400."`` API reasoning restriction reported in feature request. (TableProApp/TablePro#4070, 2026-11-06; attribution: harness/router-side (provider-preset feature request; not observed model defect); gh/TableProApp_TablePro_issues_4070.txt L18).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
- gh/TableProApp_TablePro_issues_4070.txt: Provider feature request, not evidence of a Meta-side defect. API details below are the request author’s statements.
