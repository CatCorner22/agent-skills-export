---
name: inventory-before-fetch
description: "Check what you already have before fetching, downloading, re-reading, or asking the user to upload. Fires on any plan containing download, re-download, fetch, pull, clone, 'please provide/upload', 'I don't have access to', or a file the user says is in a project/folder/attachment. Produces a one-line inventory result before any fetch and distinguishes 'not available to me in this thread' from 'does not exist'. Enforced by the fetch-guard hook (lib/ad.py hook fetch-guard). Scope boundary: recording what was read → `read-manifest`; proving a claim came from a file → `retrieval-verification-gate`."
metadata:
  priority: 9
  bashPatterns:
    - '\b(curl|wget|aria2c|gdown|scp|rsync|gsutil cp|aws s3 cp)\b'
    - '\bad\.py (fetch-check|manifest)\b'
---
# Inventory before fetch

A file visible in the user's project folder is **not** in your context. Project knowledge, attachments, memory, and earlier tool results are separate stores; most hosts make you *call* a search tool to load them. The failure this skill prevents: the user says "check your background files" and you propose to re-download a 400 MB genome file you already hold.

## Procedure (run in order; stop at the first hit)

1. **Local state.** `ad.py manifest check <name>` — was it read or fetched this session? If UNCHANGED, use the summary or a line range.
2. **Product stores.** Call the host's retrieval tool with the filename **and two synonyms** (e.g. `nebula.cram`, `genome`, `Nebula Genomics`): Claude Projects `project_knowledge_search`, ChatGPT file search, Gemini/NotebookLM sources, Devin attachments/knowledge, Cursor `@file`.
3. **Conversation.** Attachments and tool outputs earlier in this thread (and the reinjected manifest after compaction).
4. **Filesystem.** `ls`/`find`/`glob` by name and by extension in the workspace, downloads, and data dirs.

## Output: the inventory line (always, before any fetch)

```
Inventory: FOUND `nebula_genome.cram` in project knowledge (412 MB, indexed 2026-09-01) — using it.
Inventory: NOT AVAILABLE TO ME in this thread (checked: manifest, project search ×3 terms, attachments, ./data). Options: (a) you re-attach, (b) I download 412 MB — say which.
```

Rules: "not available to me" ≠ "does not exist". Never propose a download over 100 MB without an inventory line. Never ask the user to re-upload what step 2 can find. If the inventory finds the file, **cite it** when you use it (→ `retrieval-verification-gate`).

## When a fetch is right

Only after NOT AVAILABLE, and then: record it — `ad.py ledger add GRANT "download <name>: not in project knowledge (checked <stores>)"` — so the hook allows it and the decision is on record. After the fetch: `ad.py manifest record <path> --summary "…"`.

## Anti-patterns
"Let me download the latest copy" · "Please upload the file again" · "I don't have access to your files" (without having searched) · fetching to "be safe" · re-fetching after compaction because you forgot (the manifest remembers).
