---
name: output-language-lock
description: "Keep any model's answer in the requested language and script when prompts, sources or tools are in another language: lock the language in the system prompt, keep code and identifiers out of the rule, and measure the script share of the output, ignoring code blocks and URLs. Use for multilingual users, translation pipelines, non-English product copy, and when answers drift to English or mix scripts. Ships language_check.py. Scope boundary: regional formats and idioms are skill:localization-qa-filter; translation quality with glossaries is skill:kimi-context-translation."
---

# Output language lock

> **Every run:** read `adapters/muse.md` first. It maps this skill's tools to Muse and adds run rules for Muse's known failure modes.

## When it fires
The user's language differs from the language of the sources, tools or system prompt, or an answer came back partly in the wrong language.

## Steps
1. In the system prompt, one rule, stated in the target language and in English: "Answer in <language>. Code, file names, identifiers and quoted source text stay as they are. Do not switch languages mid-answer."
2. Keep instructions and few-shot examples in the target language; English examples pull answers toward English on every model.
3. `python3 scripts/language_check.py answer.md --target zh --min-share 0.9` (targets: zh ja ko en ru ar he th hi). It counts letters by Unicode script outside code blocks and URLs and fails under the threshold.
4. On failure, regenerate with the language rule repeated at the end of the user turn; do not translate the wrong-language answer, since translation hides the drift and compounds errors.
5. Reasoning text may stay in English on some models even when the answer is locked; judge the visible answer only.

## Evidence
- Reasoning drift to English with correct Chinese output is reported for Kimi; mixed-script answers are reported across model families when sources are English. Issue and practitioner reports.
- Full notes: [references/evidence.md](references/evidence.md)
