---
name: claim-evidence-pairing
description: "Every load-bearing factual or diagnostic claim in a deliverable carries [source | quote | confidence: established/probable/contested/single-source/unknown], and raw tool output is quoted, not paraphrased, when it is the evidence. Use when writing reports, diagnoses ('the bug is in X'), summaries of documents, or numbers. Recorded with `ad.py provenance add` so 'where did that number come from?' is answerable. Scope boundary: claims about user files → `retrieval-verification-gate`; completion claims → `completion-evidence-gate`."
metadata:
  priority: 7
---
# Claim–evidence pairing

Confident prose is rewarded in training; correctness is not always. Pair each claim with what would let a reader check it, and name how sure you are.

## Format
`<claim> [src: <file/URL/tool call> | "verbatim ≤ 30 words" | confidence: probable]`

Confidence scale: **established** (official doc + independent confirmation) · **probable** (one strong source, no contradiction) · **contested** (sources disagree — say how) · **single-source** (one report, unverified) · **unknown** (not found; say what you searched).

## Rules
- Numbers, dates, versions, error causes, and "the code does X" are load-bearing. Style remarks are not.
- When tool output is the evidence, **quote it** (exit code, test count, the line). Paraphrase after the quote, never instead of it.
- A diagnosis is a claim: `Root cause: null `user` at auth.ts:42 [src: stack trace | "TypeError: cannot read 'id' of null" | probable]`.
- Record it: `ad.py provenance add "<section>" "<source>" --quote "…" --confidence probable`; `ad.py provenance audit deliverable.md` lists sections with none.
- "Unknown" is a valid answer and beats a guess. Write what you searched.
- Tone follows confidence: *is* for established, *appears/likely* for probable, *reports say* for single-source.
