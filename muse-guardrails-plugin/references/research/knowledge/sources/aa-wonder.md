# Muse Wonder Full — Artificial Analysis

## Source

- **Title:** Muse Wonder Full — Artificial Analysis
- **Author/origin:** Artificial Analysis
- **Date:** publication date not captured; accessed 2026-11-10
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `aa-wonder.txt`.
- **Source URL / scope:** https://artificialanalysis.ai/models/muse-wonder-full — Muse Wonder Full — Artificial Analysis; publication date not captured; accessed 2026-11-10

## Grade

**B** — Independent benchmark or deployment measurement; vendor facts repeated in the article retain vendor provenance.

## Product/version covered

Muse Wonder / Full where specified

## Summary

Wonder Full and regular Wonder are distinct configurations; Full lacks public API speed/cost in this capture. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Presents a capability or task result; its strength depends on the stated test and provenance. `"Muse Wonder Full (Max) is amongst the leading models in intelligence when comparing to other models."` (aa-wonder.txt L42).
- Concerns cost, speed, memory or usage; preserve workload and billing assumptions. `"When evaluating the Intelligence Index, it generated 112M tokens, which is somewhat verbose in comparison to the median of 77.5M."` (aa-wonder.txt L44).
- Concerns factual reliability; compare accuracy and abstention rather than hallucination alone. `"AA-Omniscience v1.1 Net Score (higher is better) measures knowledge reliability and hallucination."` (aa-wonder.txt L1133).
- Concerns factual reliability; compare accuracy and abstention rather than hallucination alone. `"It rewards correct answers, penalizes hallucinations, and has no penalty for refusing to answer."` (aa-wonder.txt L1133).
- Presents a capability or task result; its strength depends on the stated test and provenance. `"The model supports text, image, speech, and video input, outputs text, and has a 1M tokens context window."` (aa-wonder.txt L42).
- Presents a capability or task result; its strength depends on the stated test and provenance. `"Muse Wonder Full (Max) scores 50 on the Artificial Analysis Intelligence Index, placing it well above average among comparable models (median: 31)."` (aa-wonder.txt L44).
- Presents a capability or task result; its strength depends on the stated test and provenance. `"Artificial Analysis Intelligence Index v5.0.1 incorporates 9 evaluations: AA-Briefcase v1.1, AutomationBench-AA, Terminal-Bench 4.0, FrontierCode 2.0, AA-Omniscience v1.1, GDP.pdf, HLE-Diamond, CritPt v2 (Hard Subset), and"` (aa-wonder.txt L156).
- Full Max 41%, regular Wonder Max 38%; non-hallucination Full 82%, regular 79% (therefore 18%/21% hallucination by subtraction). Updated evaluation, not directly comparable with older AA-Omniscience versions. `"AA-Omniscience v1.1 Accuracy"` (aa-wonder.txt L405).

## Data/numbers

- `"The model supports text, image, speech, and video input, outputs text, and has a 1M tokens context window."`  (aa-wonder.txt L42).
- `"Muse Wonder Full (Max) scores 50 on the Artificial Analysis Intelligence Index, placing it well above average among comparable models (median: 31)."`  (aa-wonder.txt L44).
- `"When evaluating the Intelligence Index, it generated 112M tokens, which is somewhat verbose in comparison to the median of 77.5M."`  (aa-wonder.txt L44).
- `"Artificial Analysis Intelligence Index v5.0.1 incorporates 9 evaluations: AA-Briefcase v1.1, AutomationBench-AA, Terminal-Bench 4.0, FrontierCode 2.0, AA-Omniscience v1.1, GDP.pdf, HLE-Diamond, CritPt v2 (Hard Subset), and"`  (aa-wonder.txt L156).
- `"AA-Omniscience v1.1 Net Score (higher is better) measures knowledge reliability and hallucination."`  (aa-wonder.txt L1133).
- `"AA-Omniscience v1.1 Accuracy"` Full Max 41%, regular Wonder Max 38%; non-hallucination Full 82%, regular 79% (therefore 18%/21% hallucination by subtraction). Updated evaluation, not directly comparable with older AA-Omniscience versions. (aa-wonder.txt L405).
- `"No publicly available API"` Full has no public API performance/cost in captured page; comparison chart regular Wonder Max ~12.9min/task and $6.95/task must NOT be attributed to Full. (aa-wonder.txt L72).
- `"AA-Briefcase v1.1"` Chart reading: Full Max 1729 Elo versus regular Max 1659; AutomationBench-AA 71%/68%, FrontierCode 38%/28%; same AA source, not separate measurements by this extractor. (aa-wonder.txt L156).

## How it relates to other sources

- **Qualifies:** [Introducing Muse Wonder — Meta](wonder-blog.md) — Independent results distinguish Wonder Full from the regular launch/API configuration.
- **Contrasts, not a numerical refutation:** [HN: Muse Wonder discussion](hn-50059115.md) — Mixed user results concern different workloads and sometimes different models.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- Versions, benchmark revisions, precision, context length, effort and runtime must match before comparing numbers. Vendor restatements inside an independent article remain vendor claims.
- aa-wonder.txt: Live model page captured 2026-11-10; current Index v5 scores must not be compared numerically with July/August Index versions as a regression.
