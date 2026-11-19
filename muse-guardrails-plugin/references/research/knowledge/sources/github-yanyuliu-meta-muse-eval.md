# YanyuLiu/meta_muse_eval — Muse integration findings

## Source

- **Title:** YanyuLiu/meta_muse_eval — Muse integration findings
- **Author/origin:** Original issue/PR authors unknown where omitted; quoted later commenters identified in the evidence
- **Date:** 2026-09-24
- **Ingested:** 2026-11-10
- **Evidence input:** [evidence.md](../../evidence.md); sections `gh2/YanyuLiu_meta_muse_eval_pull_2.txt`.
- **Source URL / scope:** https://github.com/YanyuLiu/meta_muse_eval/pull/2 — Add TL;DR insights from the Muse Spark API evaluation (2026-09-24); 2026-09-24

## Grade

**C** — Independent exploratory synthetic sandbox measurement; raw logs withheld, small samples, not a production security certification.

## Product/version covered

Muse Spark via Meta Model API; exact checkpoint unspecified in retained evidence

## Summary

An exploratory 30-case synthetic API sandbox finds weak confirmation recall, with no injection successes in its small sample. This note analyzes retained evidence, not a live reproduction or a fresh source acquisition.

## Key claims

- Concerns privacy, approval or product controls; distinguish promise, observation and hypothesis. `"The main gap is over-helpfulness on action-sounding requests (pay, cancel, order, RSVP, send) and extra profile/calendar/mailbox reads."` (YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; gh2/YanyuLiu_meta_muse_eval_pull_2.txt L7).
- Concerns agent workflow behavior; model and orchestration contributions must be separated. `"Write tools in the harness were acknowledged locally and were not sent, charged, or posted."` (YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; gh2/YanyuLiu_meta_muse_eval_pull_2.txt L23).
- Synthetic 30-case sandbox evaluation, NOT a production app security certification; raw logs withheld. `"injection attacks in this set did not succeed (0/10)."` (YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; gh2/YanyuLiu_meta_muse_eval_pull_2.txt L7).
- Concerns privacy, approval or product controls; distinguish promise, observation and hypothesis. `"Confirmation recall was 5/12; over-intervention was 0/3."` (YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; gh2/YanyuLiu_meta_muse_eval_pull_2.txt L7).
- Write tools locally acknowledged, never sent/charged/posted; 5/12 confirmation recall, 0/3 over-intervention; over-helpfulness/privacy reads are observed model behavior only in this harness. `"This is an exploratory behavioral snapshot, not a product security certification."` (YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; gh2/YanyuLiu_meta_muse_eval_pull_2.txt L23).

## Data/numbers

- `"Confirmation recall was 5/12; over-intervention was 0/3."`  (YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; gh2/YanyuLiu_meta_muse_eval_pull_2.txt L7).
- `"injection attacks in this set did not succeed (0/10)."` Synthetic 30-case sandbox evaluation, NOT a production app security certification; raw logs withheld. (YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; gh2/YanyuLiu_meta_muse_eval_pull_2.txt L7).
- `"This is an exploratory behavioral snapshot, not a product security certification."` Write tools locally acknowledged, never sent/charged/posted; 5/12 confirmation recall, 0/3 over-intervention; over-helpfulness/privacy reads are observed model behavior only in this harness. (YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; gh2/YanyuLiu_meta_muse_eval_pull_2.txt L23).

## How it relates to other sources

- **Contrasts, not a production security test:** [Muse personal agent — Meta product page](muse-agent.md) — 5/12 confirmation recall in simulated API cases does not establish an unauthorized action in the app.
- **Different attack surface:** [Muse prompt-injection and agent internals — @jonny](neuromatch-pi.md) — 0/10 synthetic injections does not refute a researcher’s real-agent injection account; harnesses and raw-evidence availability differ.

## Caveats

- Analysis is limited to the cited evidence.md sections. Unknown individual authors and publication dates are not inferred from capture dates or templates.
- BUG labels include fixes, controls and capability gaps; preserve the attribution in each quotation citation. PR merged/closed state is not inferred. Missing original authors prevent verified unique-reporter counts.
- The 30 cases are synthetic API-sandbox cases with simulated writes. Injection 0/10, confirmation recall 5/12 and over-intervention 0/3 have small denominators; raw logs were withheld. This is not production-agent security certification.
