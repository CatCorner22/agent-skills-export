---
name: citation-liveness-check
description: "Verify that the citations in any model-written draft are real, reachable and say what the draft says: static checks for placeholder URLs, duplicate links under different claims, malformed DOIs, quotes and references with no link; optional fetch that reports HTTP status, redirects and whether each quoted passage appears on the page. Use before delivering research, memos, briefs or reports with sources, and when a model produced references you did not supply. Ships citation_check.py. Scope boundary: claim-to-evidence pairing inside the text is skill:claim-evidence-pairing; citation formatting is skill:citation-literacy; stale sources are skill:source-freshness-check."
---

# Citation liveness check

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
A draft cites URLs, DOIs or named papers that a reader may follow, and a model produced or reformatted them.

## Steps
1. `python3 scripts/citation_check.py draft.md` (no network). Fix placeholder URLs, one-URL-many-claims patterns, quotes with no link, and references with no locator anywhere in the file.
2. `python3 scripts/citation_check.py draft.md --fetch` when you may fetch. Dead links and quotes not found on the page are errors; 403/429 pages are "unverified" and need a manual look.
3. For each error, go back to the real source: replace the URL, correct the quote to the page's text, or remove the claim. Never "fix" a citation by asking the model for another one without opening it.
4. For DOIs, the script resolves `https://doi.org/<doi>`; a 404 there means the DOI is invented.
5. Record the check date in the draft's source list; links rot, and the next reader needs to know when they were live.

## Evidence
- Fabricated references are a documented failure for every model family in legal, medical and academic settings (court sanctions over invented case citations; journal retractions). Cross-vendor; journalism and institutional notices.
- Hallucination indexes across models are highest on citation and attribution tasks. Independent indexes.
- Full notes: [references/evidence.md](references/evidence.md)
