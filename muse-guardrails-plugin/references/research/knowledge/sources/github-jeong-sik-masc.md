# jeong-sik/masc — Muse integration findings

## Source

- **Title:** jeong-sik/masc — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-12
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/jeong-sik_masc_issues_42597.txt`.
- **Source URL / scope:** https://github.com/jeong-sik/masc/issues/42597 — Muse/Antigravity Start seeds the whole canonical history and exceeds host limits (2026-10-12); 2026-10-12

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse ecosystem; exact model/version not specified in retained evidence

## Summary

Seeding complete canonical history exceeds host context limits and feeds a recovery loop; smaller-context controls identify the harness contribution. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"Fresh sessions on the Muse and Antigravity lanes seed the entire canonical history and rely on the host to compact it."` (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); gh2/jeong-sik_masc_issues_42597.txt L3).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. ``"`context compaction replacement still exceeds the hard threshold (1285213 >= 460800 tokens)`"`` (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); gh2/jeong-sik_masc_issues_42597.txt L7).
- Concerns safety/refusal evidence under the stated conditions, not universal security. `"Constraint recorded: the fix must not cut or refuse by byte numbers (2026-10-06 operator decision, reaffirmed 2026-10-12). #42598 took the byte-cap approach and is closed."` (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); comment by jeong-sik, 2026-10-12; gh2/jeong-sik_masc_issues_42597.txt L28).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"- Each failed attempt persists a ~21 MB poisoned session; the next resume fails with `session/resume (code -32603): response exceeds the outbound frame limit`."`` (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); gh2/jeong-sik_masc_issues_42597.txt L8).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. ``"- Recovery (`restart_fresh`) re-sends the same oversized seed: infinite fail loop, one ~22 MB session dir per turn (2.1 GB accumulated)."`` (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); gh2/jeong-sik_masc_issues_42597.txt L9).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"The failure itself stands: 4.4 MB / 1100-atom seeds fail every fresh muse session."` (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); comment by jeong-sik, 2026-10-12; gh2/jeong-sik_masc_issues_42597.txt L28).

## Data/numbers

- ``"`context compaction replacement still exceeds the hard threshold (1285213 >= 460800 tokens)`"``  (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); gh2/jeong-sik_masc_issues_42597.txt L7).
- ``"- Each failed attempt persists a ~21 MB poisoned session; the next resume fails with `session/resume (code -32603): response exceeds the outbound frame limit`."``  (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); gh2/jeong-sik_masc_issues_42597.txt L8).
- ``"- Recovery (`restart_fresh`) re-sends the same oversized seed: infinite fail loop, one ~22 MB session dir per turn (2.1 GB accumulated)."``  (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); gh2/jeong-sik_masc_issues_42597.txt L9).
- `"Constraint recorded: the fix must not cut or refuse by byte numbers (2026-10-06 operator decision, reaffirmed 2026-10-12). #42598 took the byte-cap approach and is closed."`  (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); comment by jeong-sik, 2026-10-12; gh2/jeong-sik_masc_issues_42597.txt L28).
- `"The failure itself stands: 4.4 MB / 1100-atom seeds fail every fresh muse session."`  (jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); comment by jeong-sik, 2026-10-12; gh2/jeong-sik_masc_issues_42597.txt L28).

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
