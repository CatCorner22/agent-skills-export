---
name: task-contract
description: "Write the task to any model as a contract: job, finish line with runnable checks, an effective-instructions block that replaces earlier instructions, boundaries, harness-owned state, inputs present, output shape and a numbered stop rule. Use before delegating non-trivial work to a model or sub-agent, when a run drifted or stopped early, when corrections keep getting appended, and when output must be cacheable. Ships a template and contract_check.py. Scope boundary: expanding a thin spec into requirements and defining done for a human deliverable are skill:deliverable-first."
---

# Task contract

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
A model or sub-agent is about to do work longer than one reply, or a previous run drifted, stopped early, guessed at a missing input or kept old instructions alive.

## Steps
1. Copy `templates/task-contract.md` and fill every section. Finish line needs at least one runnable check in backticks or a named deliverable file. Stop rule needs a number.
2. Put the whole current instruction set in "Effective instructions" and say it replaces earlier ones. Models weigh instructions by recency and salience, not by validity; appended corrections leave the old rule live.
3. Keep counts, dates, versions, done/pending lists and deadlines in "State", written by the harness each turn. Do not let the model infer them from history.
4. List every input by name under "Inputs present". Anything referred to but not listed is a stop condition, not a guess.
5. Run `python3 scripts/contract_check.py contract.md --files <attached files>`. It fails on missing or empty sections, leftover placeholders, a stop rule without a number, and inputs that are not attached; it warns about timestamps or run ids above the State section, which would break prefix caching.
6. Send the contract with stable sections first and State last. Re-send the full contract (with a bumped generation number) after any change instead of a one-line correction.

## Evidence
- Practitioner migration guidance across providers: pass effective instructions explicitly, pass state in structured form, keep counts and recency on the harness side, treat large context as headroom not a warehouse.
- Missing-input test: a frontier model attempted answers about an absent chart 93% of the time; listing inputs and a stop condition is the counter. https://neoresearch.ai/research/kimi-k3-misalignment-evaluation/
- Prompt caching on all major providers depends on an unchanged prefix; dynamic fields belong at the end.
- Full notes: [references/evidence.md](references/evidence.md)
