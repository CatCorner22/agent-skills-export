---
name: model-router
description: "Choose which model gets a task from how the output will be verified, cost per solved task, latency, data constraints and language, using a maintained routing table across Claude, GPT, Gemini, Kimi, GLM and other models. Use at the start of any job that could go to more than one model, when planning batch or agent runs, or when someone asks which model to use."
---

# Model router

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
More than one model is available and the task has not been assigned.

## Steps
1. Write one line: task type, how the output will be checked (tests, person, nothing), latency need, data class, output language, budget.
2. Read `references/routing-table.md` and pick the first row that fits. Note the evidence grade on that row.
3. If the output cannot be checked, prefer the model with the best first-shot reliability and abstention record. If it can be checked and retries are cheap, prefer the cheapest model with near-parity at pass@2 and run a verify-and-retry loop.
4. Convert prices to cost per solved task: cost per try divided by pass rate, including thinking tokens.
5. Apply hard constraints last: data residency (open weights or approved cloud host), language, context length, tool support.
6. Record the choice and reason in one sentence. Re-check the table monthly; model rankings and prices change fast.

## Evidence
- Together AI DeepSWE (same harness): K3 pass@1 68.5 vs Fable 5 69.9; pass@2 82.0 vs 80.2; $4.65 vs $13.41 per rollout. Secondhand, single-source. https://www.morphllm.com/kimi-k3-vs-claude
- DataCamp: Opus 5.5 leads closed-book reasoning and thin-spec rebuilds; Kimi leads long tool-heavy runs on price. https://www.datacamp.com/blog/kimi-k3-1-pro-vs-claude-opus-5-5
- Artificial Analysis: cost per task, speed and verbosity per model. Independent. https://artificialanalysis.ai/models/kimi-k3-1-pro
- The routing table dates from 2026-11-12 and will go stale.
- Full research notes: [references/evidence.md](references/evidence.md)
