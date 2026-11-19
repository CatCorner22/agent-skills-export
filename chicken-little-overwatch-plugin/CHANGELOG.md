# Changelog

## 2.0.0 (13 November 2026)

Rebuilt from the drafts `llm-quality-control` (skill) and `llm-qc-suite` (plugin) as Chicken Little Overwatch.

- Renamed the skill `chicken-little-overwatch` and the plugin `chicken-little-overwatch-plugin`.
- Made the package model-agnostic: added an Agent Plugins root manifest, Cursor, Devin, and Gemini CLI manifests, Gemini TOML commands, and `references/hosts.md`, which covers hosts with and without agents, a shell, or files.
- Rewrote `SKILL.md`: numbered core rules C1-C8, 4 modes, a tier choice in the Plan, load-on-demand file table, and one owner for each rule.
- Moved each role charter into `references/roles.md`, added shared rules S1-S9 and a launch template with artifact delimiters, and generated the agent files from it, so the skill and the agents cannot drift apart.
- Renamed the agents from `rt-*` to `clo-*` to avoid clashes with other red-team packs.
- Hardened the scanners: no traceback on a missing, folder, or non-UTF-8 input (exit 2); standard input; byte-order marks; matches across wrapped lines; front matter that never closes no longer hides the file; an unclosed code fence or marker zone now warns, and an unclosed marker blocks; mention zones in the watchlist; `--no-spacing`.
- Fixed a scanner defect that the new tests exposed: the watchlist missed the dotted forms "Q.D." and "Q.O.D.".
- Made each launch delimiter carry a random token, so text inside an artifact cannot close the artifact block early.
- Added 23 regression tests, a seeded-defect fixture with an answer key (`tests/fixtures/`) for testing any model, and a package validator.
- Removed `references/original-plugin.json`, which no step used.
- Kept the writing standard's text unchanged, removed its front matter, and added a package note.
