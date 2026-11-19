---
name: read-manifest
description: "Maintain .agent/manifest.json — the on-disk record of which files this session has read or fetched (path, size, hash, line ranges, summary) — via `ad.py manifest record|check|show`, so an unchanged file is answered from its manifest summary or a line range instead of being re-opened, and the manifest is reinjected after context compaction. Use when about to open a file a second time, after a compaction/summary event, in sessions that read more than ~5 files, or when the read-cache hook reports UNCHANGED. Backed by lib/ad.py manifest + read-cache/record-read hooks. Scope boundary: deciding how much of a file to read → `narrow-read-discipline`; whether to fetch at all → `inventory-before-fetch`."
metadata:
  priority: 8
  pathPatterns:
    - '**/.agent/manifest.json'
  bashPatterns:
    - '\bad\.py manifest\b'
---
# Read manifest

Compaction deletes what you read; the manifest does not. In one measured Codex session, 95% of compactions were followed by re-reading an already-read file. Fix: write what you learned to disk, in a form small enough to reinject.

## Protocol
- **Before a read:** `ad.py manifest check PATH`. UNCHANGED + summary suffices → do not open it. UNCHANGED + need detail → read **only the range** you need. CHANGED → read the changed region (`git diff`, or the range) and update the entry.
- **After a read:** `ad.py manifest record PATH --range 120-180 --summary "<what it is, what matters, what you concluded>"`. The summary is the payload — write it for a future you who has lost everything else.
- **After compaction / new thread:** `ad.py reinject` (hooked on SessionStart/PostCompact) emits ledger + checkpoint + manifest in ≤ ~1.5K tokens. Trust it over memory.
- **Record fetches too** (URL, size) so `fetch-guard` can refuse a duplicate download.

## Summary quality bar (3 lines)
1. What the file is and who owns it. 2. The facts you extracted (numbers, names, line refs). 3. What you did not read.

## Anti-patterns
Re-reading a file to "refresh" · reading whole files to find one function (grep) · summaries like "config file" · relying on the host's summary of your context instead of your own manifest.
