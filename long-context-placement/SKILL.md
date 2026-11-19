---
name: long-context-placement
description: "Lay out long prompts so any model can use them: instructions in the system prompt with critical rules repeated at the end, the question restated after large documents, labeled sections and an index for middle content, chunks under a per-model threshold, dynamic fields out of the cached prefix, newest user turn last. Use when a prompt exceeds roughly 20K tokens, when answers ignore content in the middle of a long document, or when building RAG or multi-document prompts. Ships context_layout.py. Scope boundary: session-level context budgeting and checkpoints are skill:context-budget-governor; what to read is skill:narrow-read-discipline."
---

# Long context placement

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
A prompt carries documents, transcripts or code larger than a few thousand tokens.

## Steps
1. Save the request body and run `python3 scripts/context_layout.py request.json --chunk-tokens 100000 --window 200000` with your model's safe chunk size and window. Tokens are estimated at 4 chars each.
2. Fix findings in this order: oversize single documents (chunk and label, or retrieve the relevant parts); question stated only before the document (restate question and output format after it); rules only in the middle (move to system, repeat critical ones at the end); newest user turn not last; timestamps or ids in the first message (move to the end so the prefix caches).
3. Give every document a leading label line (`[Source 3: contract.pdf, pages 1-12]`) and, for more than three documents, a short index at the top so the model can cite by label.
4. For whole-document questions, require quote-plus-location answers (page, section, timestamp); a quote the harness can find in the source is the cheapest hallucination check.
5. Stay well under the window. Claimed windows are not tested windows; independent long-context retrieval scores fall with length and with middle placement on every model that has been measured.

## Evidence
- "Lost in the middle" (Liu et al., 2023) and later long-context evaluations show accuracy drops for information placed mid-prompt across model families. Academic.
- Moonshot compacts at 200K in its own evaluations despite a 1M claimed window; Kimi's hosted Deep Research caps context at 128K and recommends under 100K of reference material. Vendor.
- Prompt caching on all major providers requires an unchanged prefix. Vendor docs.
- Full notes: [references/evidence.md](references/evidence.md)
