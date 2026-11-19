---
name: cost-per-task-meter
description: "Measure what a model actually costs per successful task from usage logs in OpenAI, Anthropic or Gemini shape: reasoning-token share, cache-hit share, cache-write cost, success rate and dollars per success, with flags for reasoning-dominated output, broken prefix caching, failures at the cheapest effort setting and mid-task model switches. Use when comparing models or providers, tuning reasoning effort or thinking budgets, or when a bill is higher than list prices suggested. Ships cost_meter.py. Scope boundary: picking the model is skill:model-router; prefix layout is skill:prompt-cache-prefix-design."
---

# Cost per task meter

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
Any decision based on price per token. Per-token price ignores reasoning tokens, cache hits and failed runs.

## Steps
1. Log one JSON line per API call with the raw `usage` object plus `task`, `success` (set by your checker, not by the model), `model` and the effort/thinking setting.
2. `python3 scripts/cost_meter.py usage.jsonl --in 3.00 --out 15.00 --cached 0.30 --cache-write 3.00` with your model's prices per million tokens. Output: per-task tokens, cache share, reasoning share, cost; total; success rate; cost per successful task.
3. Act on flags: reasoning share over 85% -> try a lower effort or thinking budget and re-measure success, never assume; cache share under 30% across calls -> the prefix is changing (timestamps, effort switch, compaction trimming the head); failure at the lowest effort -> the cheap setting is not cheap; two models in one task -> see skill:model-handoff-at-boundary.
4. Compare models on cost per successful task at equal success rate, or on success rate at equal cost; never on list price.
5. Re-run after provider updates; the same model id can change token behavior.

## Evidence
- One gateway measurement: 69-93% of a reasoning model's output tokens were reasoning; the lowest effort setting cut cost 6.3x and broke multi-step arithmetic (3/3 -> 0/6). Single measurement.
- OpenAI, Anthropic and Moonshot bill reasoning/thinking as output tokens and discount cached prefix reads; cache writes may be billed. Vendor docs.
- Harness alone moved one model from 85.4% to 91% on Terminal-Bench 2.1; cost per success depends on harness as much as model. Practitioner report.
- Full notes: [references/evidence.md](references/evidence.md)
