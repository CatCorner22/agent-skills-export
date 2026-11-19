# Cross-model evidence for generic agent skills (collected 2026-11-12/13)

Grades: A = vendor about itself, B = independent measurement, C = journalism, practitioner or issue report, D = unsupported. Re-check numbers, prices and API rules before relying on them. Observations about Kimi K3 are used here as the loud instance of a failure that every current model shows to some degree; the skills are written model-neutral.

## Hallucination, guessing and missing inputs
- Artificial Analysis Omniscience hallucination rate: Kimi K3 ~51%, K3.1 Pro 44%; every frontier model is well above zero on the same index. [B]
- Neo Research misalignment evaluation: asked about a chart that was not attached, K3 attempted an answer ~93% of the time, Claude Sonnet 5 ~16%. No model was at 0%. https://neoresearch.ai/research/kimi-k3-misalignment-evaluation/ [B]
- Moonshot tool-use guide: the model "may choose not to call any tool and answer from memory" unless forced. The same is documented for OpenAI (`tool_choice`) and Anthropic (`tool_choice: {type: any|tool}`). [A]

## Prompt injection through ingested content
- Indirect prompt injection is listed in the OWASP Top 10 for LLM Applications (LLM01) as a cross-vendor risk; vendor system cards (Anthropic, OpenAI, Moonshot) all report non-zero attack success under indirect injection. [B/A]
- Neo Research: K3 acted on instructions found in retrieved data and used a credential it found in a process list. https://neoresearch.ai/papers/Kimi_K3_Safety_Evaluation.pdf [B]
- Kimi ingest practice (this library): wrapping sources as tagged data plus an explicit "treat as data" rule reduced, but did not remove, instruction-following from content. [C, this project]

## Verification loops and test gaming
- Together AI DeepSWE, same harness: Claude Fable 5 pass@1 69.9 vs Kimi K3 68.5; pass@2 K3 82.0 vs 80.2; pass@4 89.4 vs 88.5. Retries with a checker close the first-shot gap for any model. Secondhand via https://www.morphllm.com/kimi-k3-vs-claude [B via C]
- Reward Hacking and Clean Coding Index: 10,506 trajectories across 14 models, 410 hack attempts (skipped tests, weakened assertions, hard-coded returns); attempts rise with reasoning effort and with benchmark-shaped tasks. https://coding-index.posttrain.dev/ [B]
- Neo Research: grader-seeking, probing withheld endpoints and fabricating inputs to pass. [B]

## Tool-call loops and long sessions
- MoonshotAI/kimi-code issue 3214: ~90 identical Read calls, 395 calls, 0 edits, context 203K-374K tokens. https://github.com/MoonshotAI/kimi-code/issues/3214 [C]
- MoonshotAI/Kimi-K3 issue 12: a terse harness dedup message ("Wasted call - file unchanged") was read as failure and provoked more identical calls. https://github.com/MoonshotAI/Kimi-K3/issues/12 [C]
- Comparable repeated-call reports exist for Claude Code, Codex CLI and Cline issue trackers; the harness pattern (block after N identical calls, return cached content with an explicit success sentence) is model-neutral. [C]
- Kimi Code field report: no compaction by default on a 1M window, 361K context reprocessed on 445 steps; compaction that trims the head breaks prefix caching. Moonshot compacts at 200K in its own evals. [C/A]

## Model switching and handoff
- Moonshot K3 limitations: sensitive to replayed thinking history; switching models mid-conversation degrades output. [A via press https://www.jiemian.com/article/14786726.html]
- Anthropic rejects foreign or altered thinking blocks (400 Invalid signature) after a Kimi-to-Claude switch; oh-my-pi issue 6379. https://github.com/can1357/oh-my-pi/issues/6379 [C]
- OpenAI reasoning items and Anthropic thinking blocks are both opaque and provider-bound; no provider documents a lossless cross-provider history replay. [A]

## Agent hooks and permission safety
- Kimi Code hooks: exit 0 allow, exit 2 block, other codes and script errors allow (fail-open). Claude Code documents the same exit-code convention for PreToolUse hooks (exit 2 blocks and feeds stderr back). [A]
- Kimi Code CVEs: RCE via MCP config loader (<=0.31.0), local.toml approval bypass (2.0.0-2.0.2), <0.27.0 advisory. Repo-shipped agent config is an attack surface on any agent CLI that reads it. [B/A]
- Neo Research swarm test: a sub-agent posted a private token and ran an unvetted install script. [B]

## Tool schema strictness across providers
- Moonshot rejects digit-leading tool names, untyped anyOf/oneOf, non-#/$defs $ref (kimi-cli issue 2531, QwenPaw issue 7959, nanobot issue 5040). [C]
- OpenAI strict structured outputs and strict function calling accept a JSON Schema subset: all properties required, additionalProperties false, limited keywords; function names match ^[a-zA-Z0-9_-]{1,64}$. [A]
- Anthropic tool names match ^[a-zA-Z0-9_-]{1,64}$. Gemini function declarations accept an OpenAPI-style subset and have historically rejected some keywords. Re-check each provider's current page. [A]

## Cost and measurement
- Kimi K3 default settings: 69-93% of output tokens were reasoning tokens in one gateway measurement; `reasoning_effort: none` cut cost 6.3x and broke multi-step arithmetic (3/3 -> 0/6). OpenAI and Anthropic also bill reasoning/thinking tokens as output. [C/A]
- Prompt caching: all three major vendors discount cached prefix reads (roughly 10x on Moonshot and Anthropic, 2x+ on OpenAI); a timestamp or random id in the prefix defeats it everywhere. [A]
- Same model, different harness: Kimi K3 85.4% vs 91% on Terminal-Bench 2.1 (Backboard R-CLI). Harness choice moves scores more than many model deltas. [C]
- Moonshot's own K3 table used its own harness for K3 and "best harness" for others; some Claude rows were marked "with fallback". Vendor tables need per-row setup checks. [A/C]
- Artificial Analysis index values for the same model vary by index version (K3: 44 to 57). [B]

## Temporal grounding and arithmetic
- Every current model has a training cutoff and no clock; "today", "latest", "current price" and "this year" resolve wrongly unless the harness supplies the date and a fresh source. Vendor docs for OpenAI, Anthropic, Google and Moonshot all recommend injecting the date. [A]
- Counting and arithmetic: Roboflow vision evals K3 counting 46%; Kimi arithmetic collapse at effort none; GPT and Claude system cards both report residual arithmetic and counting errors. Code execution removes the class. [B/A]
