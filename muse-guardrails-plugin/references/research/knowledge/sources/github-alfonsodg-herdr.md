# alfonsodg/herdr — Muse integration findings

## Source

- **Title:** alfonsodg/herdr — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-05
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/alfonsodg_herdr_issues_1.txt`.
- **Source URL / scope:** https://github.com/alfonsodg/herdr/issues/1 — fix(detect): Muse Code detection flapping in v1.4+ and missing executable aliases (2026-10-05); 2026-10-05

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Code

## Summary

Muse Code detection flaps with v1.4+ and executable aliases; client process recognition is the demonstrated failure layer. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"Lastly, `src/agent_resume.rs` lacks a resume plan for Muse sessions."`` (alfonsodg/herdr#1, 2026-10-05; attribution: harness/router-side (stale UI/alias detection); gh2/alfonsodg_herdr_issues_1.txt L5).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"Users running modern Muse Code experience inconsistent agent status, missing sidebar indicators, dropped agent sessions during normal idle turns, and inability to restore sessions on restart."` (alfonsodg/herdr#1, 2026-10-05; attribution: harness/router-side (stale UI/alias detection); gh2/alfonsodg_herdr_issues_1.txt L28).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"Add resume plan in `src/agent_resume.rs` for Muse sessions."`` (alfonsodg/herdr#1, 2026-10-05; attribution: harness/router-side (stale UI/alias detection); gh2/alfonsodg_herdr_issues_1.txt L33).

## Data/numbers

- No quantitative measurement is retained for this source; source dates and identifiers are metadata, not performance data.

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
