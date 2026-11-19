---
name: temporal-grounding
description: "Give any model the date, its training cutoff and the rule that time-sensitive facts need a fetched, dated source, and scan drafts for undated relative-time language (currently, latest, recently, this year), future years stated as fact and stale years called current. Use at the start of any session or pipeline, before questions about prices, versions, laws, office-holders or schedules, and before delivering a draft that mentions time. Ships temporal_check.py header|scan. Scope boundary: checking whether a cited source is stale is skill:source-freshness-check."
---

# Temporal grounding

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
Every session, and any draft that says "currently", "latest" or names a year.

## Steps
1. `python3 scripts/temporal_check.py header --tz America/New_York --cutoff "2026-03" --model "<model>"` and place the output at the end of the system prompt or the start of the user turn, after the cached prefix (the date changes daily; inside the prefix it kills cache hits).
2. The header tells the model: today's date and weekday; its cutoff; that prices, versions, office-holders, laws, schedules and "latest" anything are unknown until a fetched source in the conversation states them, with that source's date cited; to compute ages and durations from today's date with code; to write absolute dates.
3. Before delivery: `python3 scripts/temporal_check.py scan draft.md`. Fix each flag by adding the absolute date and source, or by removing the claim.
4. In pipelines, set the header once per run from the harness clock, never from the model.

## Evidence
- Every current model has a training cutoff and no clock; all major vendors recommend injecting the date for time-sensitive tasks. Vendor docs.
- Hallucination indexes across models are highest on time-sensitive factual questions (prices, versions, office-holders). Independent indexes.
- Full notes: [references/evidence.md](references/evidence.md)
