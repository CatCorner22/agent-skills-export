---
name: retrieval-verification-gate
description: "Before saying 'according to your file / I reviewed the document / the report shows', require a quoted excerpt with source name and location, and label which of four states applies: visible in UI, indexed, retrieved, read. Use whenever a claim rests on a user document, project file, attachment, URL, or memory. Prevents 'I reviewed your genome report' when nothing was retrieved. Scope boundary: finding the file → `inventory-before-fetch`; evidence for non-file claims → `claim-evidence-pairing`."
metadata:
  priority: 8
---
# Retrieval verification gate

Four distinct states, often confused:
| State | Meaning | May you say "I read it"? |
|---|---|---|
| **Visible** | User sees it in a folder/project list | No |
| **Indexed** | Host has embedded/chunked it for search | No |
| **Retrieved** | A search call returned chunks from it | Only for those chunks |
| **Read** | You loaded the content (whole or range) into context | Yes, for that range |

## Gate
A claim about a document is allowed only with: **source name · location (page/section/line/chunk) · verbatim excerpt (≤ 40 words)**.
```
Per `Nebula_Report.pdf` §4.2 (retrieved, chunk 3): "APOE: ε3/ε3 … no increased risk". 
```
If retrieval returned nothing: say "Search for X returned no passages from `file`; I have **not** read it." Then → `inventory-before-fetch`.

## Rules
- Never upgrade a state: retrieved chunks ≠ the whole document. Say "the retrieved passages do not mention…", not "the document does not mention…".
- Quote, don't paraphrase, when the quote *is* the evidence. Paraphrase only after the quote.
- If the host summarizes files for you (Projects, Gems, NotebookLM), that summary is **indexed/retrieved**, not read — label it.
- After compaction, your memory of a file is a *summary*; re-verify before quoting numbers.
