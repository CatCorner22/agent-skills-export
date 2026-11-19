# CommandCodeAI/command-code — Muse integration findings

## Source

- **Title:** CommandCodeAI/command-code — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-09-03–2026-09-13
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/CommandCodeAI_command-code_issues_799.txt`.
- **Source URL / scope:** https://github.com/CommandCodeAI/command-code/issues/799 — muse spark 1.3 contributor usage bug (2026-09-03); 2026-09-03

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Spark 1.3

## Summary

Contributor accounting appears inconsistent across usage displays; the underlying Meta-versus-client cause is unresolved. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Reporter compares three credits for ~54.1M tokens against previous 1.2B/ten credits on 1.2 contributor; not a verified 666% price change. `"only with 54.1m tokens I hit my limits"` (CommandCodeAI/command-code#799, 2026-09-03; attribution: unclear (contributor caching/metering symptom, no verified provider accounting cause); gh2/CommandCodeAI_command-code_issues_799.txt L5).
- omar391, 2026-09-13: second commenter corroborates symptom; cause/caching/accounting not independently established. `"I can also attest the same issue."` (CommandCodeAI/command-code#799, 2026-09-03; attribution: unclear (contributor caching/metering symptom, no verified provider accounting cause); comment by omar391, 2026-09-13; gh2/CommandCodeAI_command-code_issues_799.txt L57).
- **Evidence scope:** The retained statement supports the limited takeaway above, not an additional independent observation. `"only with 54.1m tokens I hit my limits"` (gh2/CommandCodeAI_command-code_issues_799.txt).

## Data/numbers

- `"only with 54.1m tokens I hit my limits"` Reporter compares three credits for ~54.1M tokens against previous 1.2B/ten credits on 1.2 contributor; not a verified 666% price change. (CommandCodeAI/command-code#799, 2026-09-03; attribution: unclear (contributor caching/metering symptom, no verified provider accounting cause); gh2/CommandCodeAI_command-code_issues_799.txt L5).
- `"I can also attest the same issue."` omar391, 2026-09-13: second commenter corroborates symptom; cause/caching/accounting not independently established. (CommandCodeAI/command-code#799, 2026-09-03; attribution: unclear (contributor caching/metering symptom, no verified provider accounting cause); comment by omar391, 2026-09-13; gh2/CommandCodeAI_command-code_issues_799.txt L57).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
- Sparse source: only 2 substantive retained claim(s). Scope/ceiling bullets explain that limitation rather than inventing additional findings.
