# getpaseo/paseo — Muse integration findings

## Source

- **Title:** getpaseo/paseo — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-10-07–2026-10-23
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/getpaseo_paseo_issues_6342.txt`.
- **Source URL / scope:** https://github.com/getpaseo/paseo/issues/6342 — Importing a Muse Code session fails with "Invalid plugin provider persistence handle" (2026-10-07); 2026-10-07

## Grade

**C** — Detailed practitioner issue/PR evidence, including proposed fixes and controls; excerpts are weaker than full threads and lifecycle is not inferred.

## Product/version covered

Muse Code

## Summary

Session import/persistence handles fail; the reported original app path was not fully reproduced in the captured tests. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"> I have been trying to import a muse code session on paseo, but it fails every time, claude code sessions work fine."` (getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; gh2/getpaseo_paseo_issues_6342.txt L4).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"Importing Claude Code sessions works for the same user."` (getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; gh2/getpaseo_paseo_issues_6342.txt L6).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"- A newly created session’s native ID produced `Invalid plugin provider persistence handle` when passed directly to Paseo’s import adapter, matching the reported error text."`` (getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; comment by paseo-bot[bot], 2026-10-09; gh2/getpaseo_paseo_issues_6342.txt L46).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. `"- The handle returned by Paseo’s session list imported successfully through that adapter."` (getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; comment by paseo-bot[bot], 2026-10-09; gh2/getpaseo_paseo_issues_6342.txt L47).
- Concerns API/runtime configuration or behavior; preserve provider and harness scope. ``"The CLI path passes the argument to `decodePersistenceId` in `packages/server/src/server/agent/plugin-provider.ts`, which accepts only the `plugin:`-prefixed handle that the session list returns, so a provider's own session ID is"`` (getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; comment by paseo-bot[bot], 2026-10-23; gh2/getpaseo_paseo_issues_6342.txt L63).

## Data/numbers

- No quantitative measurement is retained for this source; source dates and identifiers are metadata, not performance data.

## How it relates to other sources

- **Specification versus integration:** [Muse Spark 1.3 — Meta model documentation](dev-spark13.md) — First-party model capability does not guarantee this client’s transport, parser, session or UI implements it correctly.
- **Excerpt cross-reference:** [Muse GitHub failures — search excerpt compilation](gh-search-failures.md) — Related search hits are partial and may duplicate a full thread; they do not add independent reporters.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
