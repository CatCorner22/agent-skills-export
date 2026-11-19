---
name: style-guide-lock
description: "Load a house style once as a rules file and check every draft against it rule by rule: sentence length, banned words, required terms, passive voice, forbidden patterns. Use when writing for a publication, client, brand or court with a known style, when drafts drift in tone, or before handing prose to a reviewer. Ships a style checker and a rules template."
---

# Style-guide lock

> **Muse.** On Muse Code, Muse Spark, Muse Wonder, or the Meta Model API, also read `adapters/muse.md`.

## When it fires
Prose must meet a defined style, or you are producing many pieces that should sound alike.

## Steps
1. Turn the style guide into `style-rules.json` (start from `templates/style-rules.json`): max sentence words, max sentences per paragraph, banned words with preferred replacements, banned patterns (regex), required terms, passive-voice ceiling.
2. Put the three most important rules at the top of the writing prompt. Do not paste the whole guide; models follow a short list better.
3. Draft, then run `python3 scripts/style_check.py draft.md --rules style-rules.json`. Fix every violation or record why it stands.
4. Add new rules when a reviewer flags something twice. Keep the file under 40 rules.
5. Version the rules file with the project so every session uses the same one.

## Evidence
- Blind essay judging found the largest model differences in style-guide discipline rather than ideas; the same checks lift any model. Single-source test (Wagner, Kimi K3.1 Pro vs Claude Fable 5).
- The passive-voice detector is a heuristic; expect some false flags.
- Full research notes: [references/evidence.md](references/evidence.md)
