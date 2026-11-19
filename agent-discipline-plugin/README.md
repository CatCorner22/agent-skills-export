# agent-discipline

Sixteen skills and nine deterministic guards against the recurring LLM/agent failures documented in
*LLM Failure Modes and Skill/Plugin Solutions*: resource blindness (re-downloading a file you already have),
compaction → re-read loops, whole-file/whole-suite habits, context rot, passivity and re-asking, over-agency,
false "done", sycophancy, rule neglect, tool misuse, silent assumptions, model drift.

Three layers, by design: **Guidance** (SKILL.md, portable to any host) · **State** (`.agent/` files that survive
compaction) · **Enforcement** (hooks that deny what must never happen). Rule of thumb: if a failure cost more than
ten minutes or any data, it lives in State or Enforcement, not Guidance.

## Layout
```
plugin.json                    plugin manifest (Agent Plugins format; `muse plugins validate .`)
hooks/hooks.json               hooks for Muse Code's .muse/hooks.json: SessionStart/PostCompact reinject, PreToolUse guards, PostToolUse log+trim, Stop gate
lib/ad.py                      one CLI + hook entrypoint (stdlib only, Python ≥3.8); lib/ad_*.py modules
skills/<name>/SKILL.md         16 skills (see table)
tests/test_ad.py               31 tests incl. hook stdin/stdout contract and fail-open behaviour
```
State dir: `./.agent` (override `AGENT_STATE_DIR`): `manifest.json`, `ledger.md`, `CHECKPOINT.md`, `scope.json`,
`toollog.jsonl`, `provenance.jsonl`, `outputs/`, `regress/`.

## Skills ↔ guards
| Failure | Skill (guidance) | Guard (state / enforcement) |
|---|---|---|
| Resource blindness | `inventory-before-fetch` | `hook fetch-guard` (P1): denies downloads of files already in the manifest, large-type files with no inventory, or > `AD_MAX_FETCH_MB` |
| Re-read loops | `read-manifest` | `manifest`, `hook read-cache` / `record-read` (P2) |
| Whole-file habits | `narrow-read-discipline`, `test-impact-selector` | `test-impact` |
| Context rot | `context-budget-governor` | `checkpoint`, `hook reinject` (P5) |
| Passivity / re-asking | `autonomy-ledger`, `ask-or-assume` | `ledger add|check` |
| Over-agency | `scope-and-blast-radius-check` | `hook scope-fence` (P3): destructive patterns + path containment, unlocked only by a matching ledger GRANT |
| False success | `completion-evidence-gate`, `retrieval-verification-gate` | `hook completion-gate` (P4, Stop hook; cross-checks `toollog.jsonl`) |
| Sycophancy | `premise-check`, `claim-evidence-pairing` | `provenance add|show|audit` (P8) |
| Rule neglect | `negative-constraint-compiler`, `rules-hygiene` | `rules lint|compile|rewrite`, `deny-regex` (P7) |
| Tool misuse | `tool-call-validator` | `hook validate-call`, `hook log-trim` (P6 trimmer) |
| Model drift | `model-sanity-regression` | `regress init|show|record|report` (P9) |

## Quick start
```
python3 lib/ad.py scope set .                       # declare write scope
python3 lib/ad.py ledger add ACCEPT "done = tests green + PR draft"
python3 lib/ad.py manifest record data/genome.cram --summary "Nebula WGS, 412 MB, hg38"
python3 lib/ad.py fetch-check "curl -O https://…/genome.cram"   # → denied, points at the manifest entry
python3 -m unittest discover tests
```
Install on Muse Code:
1. Install the plugin with `muse plugins install ./agent-discipline-plugin --scope user` (or `--scope project`), or copy each folder under `skills/` to `<repo>/.agents/skills/<name>/`.
2. Copy `hooks/hooks.json` to `<repo>/.muse/hooks.json` and replace every `__AD_ROOT__` with the absolute path of this folder. Muse Code runs hook commands with a cleared environment, so a path variable won't reach them. Project hooks run only after you trust the workspace.
3. Start a new session; Muse Code loads hooks at startup. It warns about any event, matcher, or handler it doesn't support and skips that entry, so read the startup warnings and fix the tool names in each `matcher` to match Muse Code's tools.

UNVERIFIED: nobody has run these hooks on Muse Code. Meta documents the hook events (SessionStart, PreToolUse, PostToolUse, PostCompact, Stop and others) and the file location, not the input JSON (https://dev.meta.ai/docs/muse-code/extending, read 2026-11-18). Every hook reads JSON on stdin and writes a decision JSON on stdout, plus exit 2 on deny; check that contract with one PreToolUse hook before you rely on the rest. Without hooks, call the same CLI (`python3 lib/ad.py …`) yourself.

## Design guarantees
- Fail-open on internal error (a broken hook never bricks the agent) — except destructive patterns, which fail closed.
- Every denial returns the alternative (the manifest entry, the ledger line, the procedure), never just "no".
- No dependencies; each hook runs in tens of milliseconds; all state is plain text you can read and edit.
