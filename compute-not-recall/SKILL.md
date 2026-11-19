---
name: compute-not-recall
description: "Route every count, sum, percentage, difference, unit conversion and date span through code instead of the model's head, and recompute the arithmetic stated in a finished draft (inline equations, percent-of statements, from-to changes, table total rows, day counts) to flag mismatches. Use when a model produces numbers, before delivering reports or analyses with figures, and when a model counts items in text or images. Ships recompute_check.py. Scope boundary: statistical reasoning quality is skill:statistical-literacy; numbers unsupported by sources are skill:restraint-pass."
---

# Compute, do not recall

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
A model is about to state a number it derived rather than quoted.

## Steps
1. In the prompt: "For any arithmetic, counting, unit conversion or date math, write and run code (or call the calculator tool) and show the computed value; do not compute in prose." Give the model a code tool when the harness allows.
2. For counting in images or long text, have code count (OCR + script, regex, DOM query) and have the model interpret; frontier models score poorly on counting in cluttered scenes.
3. Before delivery: `python3 scripts/recompute_check.py draft.md`. It recomputes `a + b = c`, `X% of Y is Z`, `Z is X% of Y`, `from A to B, a change of C`, `from DATE to DATE (N days)` and markdown table Total rows, with 1% or 1-unit tolerance for rounding.
4. Fix every mismatch at the source number, not the displayed one; a wrong total usually means a wrong row.
5. Keep the computed values and the code in an appendix or log so a reviewer can re-run them.

## Evidence
- Vision evals: counting is a weak category across models (one frontier model 46%). https://playground.roboflow.com/
- Lowest reasoning effort dropped one model's multi-step arithmetic from 3/3 to 0/6 in a gateway measurement; code execution removes the dependence on effort. Single measurement.
- OpenAI and Anthropic system cards report residual arithmetic and counting errors. Vendor.
- Full notes: [references/evidence.md](references/evidence.md)
