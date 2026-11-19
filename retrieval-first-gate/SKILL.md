---
name: retrieval-first-gate
description: "Before stating any fact a tool could check, retrieve it: decide retrieve-or-recall, force the first tool call, and audit transcripts for facts stated from memory. Works with any model and agent framework. Use when an agent has search, file, database or API tools and the task involves numbers, dates, names, prices, versions, quotes or law."
---

# Retrieval-first gate

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
A tool exists that can confirm the fact. The answer will be relied on.

## Steps
1. Classify the question: recall is fine for definitions and stable concepts; retrieval is required for anything that changes (prices, versions, dates, people, law, code in this repo) or anything quoted.
2. For retrieval tasks, make the first assistant turn a tool call. In APIs that support it, set `tool_choice` to the retrieval tool or `required` on that turn.
3. In the system prompt: "Do not state a number, date, name, version or quote that did not come from a tool result in this conversation. If no tool can answer, say 'not verified'."
4. Keep retrieval tools few and clearly named; load others on demand.
5. Audit: `python3 scripts/retrieval_gate_check.py transcript.json`. It flags fact-like text before the first tool result and final answers with facts but no tool call. Use `--allow-memory` to downgrade to warnings for recall-only tasks.
6. Mark anything unverified in the deliverable. Never present recall as retrieval.

## Evidence
- Vendor guidance that models may answer from memory instead of calling a tool and that `tool_choice` forces retrieval: Moonshot K3 guide. Same pattern exists in OpenAI and Anthropic tool-use docs. https://platform.kimi.ai/docs/guide/kimi-k3-tool-calling-best-practice
- Artificial Analysis Omniscience hallucination rates show every frontier model guesses on some share of unknowns; Kimi K3.1 Pro 44%. Independent. https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks
- Full research notes: [references/evidence.md](references/evidence.md)
