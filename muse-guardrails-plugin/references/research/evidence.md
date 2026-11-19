# Muse capture evidence

Coverage: all 107 supplied `.txt` captures read completely; no access controls bypassed and no live reproduction attempted. Dates on live model pages may be capture dates, not releases. A = Meta on its own product (including Meta’s HF card and executive interview); B = independent measurement; C = detailed practitioner/journalistic report; D = unsupported assertion/marketing. Mixed provenance is called out per section/bullet. A vendor claim is not independent validation.

Each bullet has exactly one charter question and one type. GitHub bullets use BUG as requested even for fixes, capability gaps, controls, or negative findings; that tag alone does not establish a Meta/model defect. Attribution and qualifications are essential. Full GitHub captures generally identify later commenters but omit original issue-author metadata: source/project counts cannot be read as unique human reporters. Search results are excerpts, not full threads. Repeated HN commenters count once per theme. @jonny’s two threads are one researcher. Secondary repetitions and duplicate issues do not increase source counts.

Quotes are short verbatim spans, shortened only at the end. PDF text alone is whitespace-normalized. For flattened chart/table data, the label is quoted and its aligned numerical value is stated explicitly as a table reading. A zero-bullet section may be a fully read but irrelevant/insufficient source, not a missing read. Unusable and partial captures are enumerated in evidence-index.md.

## aa-11.txt — Muse Spark 1.1: Meta gains 8 Intelligence Index points in three months | Artificial Analysis / https://artificialanalysis.ai/articles/muse-spark-1-1-everything-you-need-to-know — July 10, 2026 — B

- [Q12] [FACT] `"Meta's Muse Spark 1.1 scores 51 on the Artificial Analysis Intelligence Index and is cost and token efficient compared to its peers"` — L15.
- [Q2] [GAP] `"Agentic Knowledge work improves substantially but continues to lag the frontier on GDPval-AA v2."` — L17.
- [Q12] [FACT] `"Muse Spark 1.1 used 94M output tokens to run the Intelligence Index, fewer than GPT-5.4 (xhigh, 109M), GPT-5.6 Luna (max, 125M), and GLM-5.2 (max, 141M)."` — L20.
- [Q12] [FACT] `"We estimate ~$0.26 per Intelligence Index task at Meta's $1.25/$4.25 pricing - below GLM-5.2 ($0.37) and roughly 3x below GPT-5.4 ($0.89)"` — L20.
- [Q4] [FACT] `"The score more than quadrupled from 4 to 18 as the hallucination rate fell 35 points (73% to 38%), with the attempt rate down from 95% to 82% and accuracy roughly flat (45% to 41%)"` — L21.
- [Q12] [FACT] `"➤ Pricing: $1.25/$4.25 per 1M input/output tokens; cache hits discounted to $0.15 per 1M"` — L24.
- [Q12] [FACT] `"➤ Output speed: ~114 tokens/s median on Meta's first-party API, with a ~21s time to first answer token"` — L25.
- [Q2] [FACT] `"The 8 point Intelligence Index gain over Muse Spark 1.0 is concentrated in Scientific Reasoning, Coding, and Knowledge: the Coding Index +12 points (59 to 71), SciCode +6 points (52% to 58%), Humanity's Last Exam +5 points (40% to 45%), AA-Omniscience +14 points (4 to 18), and GDPval-AA v2 +232 Elo (1144 to 1376)."` — L27.
- [Q12] [FACT] `"However, it used more tokens than several higher-scoring models, such as Claude Fable 5 and Grok 4.5 (high)."` — L30.
- [Q1] [FACT] `"Meta's Muse Ember is the cheapest model scoring 36 on the Intelligence Index"` — L35. Related-article teaser in capture, not a full Ember evaluation or direct current-v5 score comparison.

## aa-12.txt — Muse Spark 1.2: Benchmarks and analysis | Artificial Analysis / https://artificialanalysis.ai/articles/muse-spark-1-2 — August 5, 2026 — B

- [Q2] [FACT] `"Meta’s Muse Spark 1.2 scores 54 on the Artificial Analysis Intelligence Index."` — L15.
- [Q2] [STRENGTH] `"Its GDPval-AA v2 Elo rose 260 points to 1631, #5 among all models we have benchmarked and ahead of Claude Opus 4.8 (max, 1588)."` — L18.
- [Q6] [FACT] `"GDPval-AA v2 is our leading metric for general agentic performance, measuring models on realistic knowledge work tasks such as preparing presentations and analysis, with shell access and web browsing capabilities in an agentic loop via our reference harness Stirrup."` — L18.
- [Q12] [FACT] `"➤ Among the most cost-efficient models at its intelligence level: Muse Spark 1.2 costs $0.40 per Intelligence Index task at Meta’s unchanged $1.25/$4.25 per 1M token pricing, with only Grok 4.5 (high, $0.37) and GPT-5.6 Sol (medium, $0.39) cheaper in its intelligence cluster - GPT-5.6 Terra (max, $0.51), Kimi K3 (max,"` — L19.
- [Q12] [FACT] `"The cost increase over Muse Spark 1.1 ($0.29 per task) is driven by increased token usage per Intelligence Index task, with input tokens up ~53% and output tokens up ~36%, concentrated in GDPval-AA v2."` — L19.
- [Q4] [FACT] `"➤ AA-Omniscience abstention rate increases: The score rose from 18 to 22 as the hallucination rate fell 10 points (38% to 28%) and the attempt rate dropped from 82% to 67%."` — L20.
- [Q4] [FACT] `"Muse Spark 1.2’s heavy abstention (not answering questions when unsure) now drives both the low hallucination rate and a lower accuracy (41% to 38%)."` — L20.
- [Q2] [FACT] `"➤ Scientific Reasoning results remain largely unchanged: CritPt, which tests research-level physics reasoning, notably gained 3 points (15% to 18%), while SciCode fell 2 points (58% to 56%) and Humanity’s Last Exam fell 1 point (45% to 44%)."` — L21.
- [Q12] [FACT] `"➤ Model details: Muse Spark 1.2 retains Muse Spark 1.1’s 1M token context window and pricing ($1.25/$4.25 per 1M input/output tokens, with cache hits discounted to $0.15 per 1M), and is available on Meta’s first-party API at launch."` — L22.
- [Q2] [FACT] `"The 3 point gain over Muse Spark 1.1 on the Artificial Analysis Intelligence Index is concentrated in agentic evaluations: GDPval-AA v2 +260 Elo (1371 to 1631), Terminal-Bench v2.1 +2 points (78% to 80%), and τ³-Banking +2 points (25% to 27%)."` — L24.
- [Q2] [GAP] `"The minor regressions are SciCode (-2 points) and Humanity’s Last Exam (-1 point)."` — L24.

## aa-13.txt — Muse Spark 1.3 (max) - Intelligence, Performance & Price Analysis | Artificial Analysis / https://artificialanalysis.ai/models/muse-spark-1-3 — publication date not captured; accessed 2026-11-10 — B

Live model page captured 2026-11-10; current Index v5 scores must not be compared numerically with July/August Index versions as a regression.

- [Q2] [FACT] `"The model supports text, image, and video input, outputs text, and has a 1M tokens context window."` — L44.
- [Q13] [GAP] `"Muse Spark 1.3 (Max) scores 37 on the Artificial Analysis Intelligence Index, placing it below average among comparable models (median: 40)."` — L45.
- [Q12] [GAP] `"When evaluating the Intelligence Index, it generated 123M tokens, which is very verbose in comparison to the median of 72.8M."` — L45.
- [Q12] [STRENGTH] `"Pricing for Muse Spark 1.3 (Max) is $1.25 per 1M input tokens (competitively priced, median: $2.00) and $4.25 per 1M output tokens (competitively priced, median: $10.00)."` — L46.
- [Q12] [FACT] `"On average, it costs $2.39 per task to evaluate Muse Spark 1.3 (Max) on the Intelligence Index."` — L46.
- [Q12] [FACT] `"At 12.1 minutes per Intelligence Index task, Muse Spark 1.3 (Max) is quicker than average compared with the median of 12.8 minutes for comparable models (lower is better)."` — L47.
- [Q2] [FACT] `"Artificial Analysis Intelligence Index v5.0.1 incorporates 9 evaluations: AA-Briefcase v1.1, AutomationBench-AA, Terminal-Bench 4.0, FrontierCode 2.0, AA-Omniscience v1.1, GDP.pdf, HLE-Diamond, CritPt v2 (Hard Subset), and Terminal-Bench-Science 0.1"` — L83.
- [Q4] [FACT] `"AA-Omniscience v1.1 Net Score (higher is better) measures knowledge reliability and hallucination."` — L188.
- [Q4] [STRENGTH] `"It rewards correct answers, penalizes hallucinations, and has no penalty for refusing to answer."` — L188.
- [Q12] [FACT] `"Muse Spark 1.3 (Max) has a time to first answer token of 25.98s (based on Meta's API), which is somewhat higher than average compared to other models in a similar price tier (median: 12.15s)."` — L289.
- [Q12] [FACT] `"For a blended rate (7:2:1 cache hit/input/output ratio), this is $0.78 per 1M tokens."` — L293.

## aa-wonder.txt — Artificial Analysis / https://artificialanalysis.ai/models/muse-wonder-full — publication date not captured; accessed 2026-11-10 — B

Live model page captured 2026-11-10; current Index v5 scores must not be compared numerically with July/August Index versions as a regression.

- [Q2] [FACT] `"Muse Wonder Full (Max) is amongst the leading models in intelligence when comparing to other models."` — L42.
- [Q2] [FACT] `"The model supports text, image, speech, and video input, outputs text, and has a 1M tokens context window."` — L42.
- [Q2] [FACT] `"Muse Wonder Full (Max) scores 50 on the Artificial Analysis Intelligence Index, placing it well above average among comparable models (median: 31)."` — L44.
- [Q12] [FACT] `"When evaluating the Intelligence Index, it generated 112M tokens, which is somewhat verbose in comparison to the median of 77.5M."` — L44.
- [Q2] [FACT] `"Artificial Analysis Intelligence Index v5.0.1 incorporates 9 evaluations: AA-Briefcase v1.1, AutomationBench-AA, Terminal-Bench 4.0, FrontierCode 2.0, AA-Omniscience v1.1, GDP.pdf, HLE-Diamond, CritPt v2 (Hard Subset), and Terminal-Bench-Science 0.1"` — L156.
- [Q4] [FACT] `"AA-Omniscience v1.1 Net Score (higher is better) measures knowledge reliability and hallucination."` — L1133.
- [Q4] [STRENGTH] `"It rewards correct answers, penalizes hallucinations, and has no penalty for refusing to answer."` — L1133.
- [Q4] [FACT] `"AA-Omniscience v1.1 Accuracy"` — L405. Full Max 41%, regular Wonder Max 38%; non-hallucination Full 82%, regular 79% (therefore 18%/21% hallucination by subtraction). Updated evaluation, not directly comparable with older AA-Omniscience versions.
- [Q12] [FACT] `"No publicly available API"` — L72. Full has no public API performance/cost in captured page; comparison chart regular Wonder Max ~12.9min/task and $6.95/task must NOT be attributed to Full.
- [Q2] [FACT] `"AA-Briefcase v1.1"` — L156. Chart reading: Full Max 1729 Elo versus regular Max 1659; AutomationBench-AA 71%/68%, FrontierCode 38%/28%; same AA source, not separate measurements by this extractor.

## ailately.txt — Meta's Muse Spark Open: 816B Open Weights, Graded / https://ailately.com/articles/meta-muse-spark-open-weights — November 10, 2026 — D (secondary/marketing synthesis; linked measurements retain their original provenance)

- [Q12] [FACT] `"Meta released the 816-billion-parameter Muse Spark Open on Oct. 15 under a license that demands credit and a deal above $20 million in revenue."` — L20. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q9] [FACT] `"That claim comes with a license, a hardware bill and a benchmark table Meta wrote itself 3 ."` — L22. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q9] [FACT] `"Meta released that 30-billion-parameter model, Muse Glimmer, in August under the Apache 2.0 license 7 ."` — L25. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q9] [FACT] `"They also ran a 2-bit version on one Mac Studio with 512 GB of memory at 18 tokens a second."` — L26. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q9] [GAP] `""Apple doesn't currently sell the 512 GB Mac Studio to mere mortals, but in a few weeks, you will be able to buy two of those machines for the price of a compact car," he wrote 4 ."` — L30. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q1] [FACT] `"Terminal-Bench 2.1, a coding test, gave Muse Spark Open 76.4, Kimi K3 85.0 and GLM 5.3 83.9 3 ."` — L48. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q1] [FACT] `"DeepSWE 1.1, another coding test, gave Kimi K3 68 and Muse Spark Open 60."` — L48. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q1] [FACT] `"Meta's own card lists the Artificial Analysis Intelligence Index at 39 for its model, 45 for GLM 5.3 and 44 for Kimi K3."` — L48. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q12] [FACT] `"Hosted providers charge $1.25 per million input tokens and $4.25 per million output tokens."` — L65. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q12] [FACT] `"A company that sells model access as a service and passes $20 million in revenue over any 12 months "must notify Meta and enter into a separate written agreement with Meta" first."` — L68. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q11] [FACT] `"Muse Spark Open scored 0.5 on the StrongREJECT jailbreak test against 66.6 for Kimi K3"` — L74. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement. The primary model-card table explicitly says lower is better; this is not evidence that 0.5 is weaker safety than 66.6.
- [Q9] [GAP] `""Like with some of the newer Chinese models, though, the weights may be open but the license doesn't tell the same story," he wrote 4 ."` — L88. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.

## ap-privacy.txt — apnews.com / https://apnews.com/article/meta-muse-openai-dot-ai-privacy-449734d41d3750aad7038b761faa49c9 — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Unusable: security-verification/challenge page, not article content.


## apple-mlx.txt — Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio - Apple Machine Learning Research / https://machinelearning.apple.com/research/mlx-distributed-inference — October 15, 2026 — B

- [Q12] [FACT] `"On a cluster of four Mac Studios, Muse Spark Open generates over 36 tokens per second (see Figure 1 ), well above average human reading speed."` — L12.
- [Q9] [FACT] `"While both the Qwen and Mistral models fit on a single Mac Studio with 512GB of RAM, Muse Spark Open would require more than 1.6TB of RAM in its native precision (BF16) for the model parameters alone."` — L43.
- [Q12] [FACT] `"Muse Spark Open — — 15.74 24.99 36.73"` — L88. Table 3 at 8,192 context / 128 generated tokens: two-Mac pipeline, two-Mac tensor, four-Mac tensor respectively; not a full-1M-context throughput claim.

## axios-10.txt — Just a moment... / https://www.axios.com/2026/04/08/meta-muse-alexandr-wang — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Unusable: security-verification/challenge page, not article content.


## axios-13.txt — Just a moment... / https://www.axios.com/2026/09/02/meta-debuts-muse-spark-13-as-personal-agent-work-continues — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Unusable: security-verification/challenge page, not article content.


## baike.txt — 百度安全验证 / https://baike.baidu.com/item/Muse%20Spark/67591835 — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Unusable: security-verification/challenge page, not article content.


## build-open.txt — Build with Muse Spark Open / https://dev.meta.ai/resources/blog/build-with-muse-spark-open — publication date not captured; accessed 2026-11-10 — A

- [Q6] [FACT] `"An 816B-parameter open-weight model from Meta Superintelligence Labs, trained for long-horizon agentic work such as coding and customer service agents."` — L42. Meta statement; not an independent measurement.
- [Q3] [FACT] `"It activates 42B parameters per token, takes text, image, video and audio input, and holds a 1M-token context window."` — L42. Meta statement; not an independent measurement.
- [Q9] [FACT] `"Serve the model on either two Mac Studios, with M5 Ultra and 512GB of unified memory; or four Mac Studios with 256GB of unified memory, for a total of 1TB of unified memory, enough to hold a NVFP4 quantized version of Muse Spark Open."` — L105. Meta statement; not an independent measurement.
- [Q12] [FACT] `"Connect your Mac Studios directly using the built-in support for Thunderbolt 5 and RDMA to ensure high-bandwidth, low-latency communication."` — L105. Meta statement; not an independent measurement.
- [Q9] [FACT] `"Unsloth's Dynamic GGUFs compress the model to as little as 2-bit, so the smallest version fits in about 300 GB of combined system RAM and VRAM, or unified memory on Apple silicon."` — L150. Meta statement; not an independent measurement.
- [Q9] [FACT] `"Unsloth Desktop runs on macOS, Windows and Linux, uses llama.cpp for CPU and GPU inference, and offloads layers to system RAM when VRAM runs short."` — L150. Meta statement; not an independent measurement.
- [Q6] [FACT] `"Download and chat with the model in the app, or serve it through OpenAI and Anthropic compatible endpoints for your applications and coding agents."` — L150. Meta statement; not an independent measurement.
- [Q1] [FACT] `"Served in NVFP4 with a custom-trained DSpark drafter for faster decoding with 1M context window."` — L159. Meta statement; not an independent measurement.
- [Q3] [FACT] `"Fireworks AI — Run serverless LoRA training on the NVFP4 checkpoint, with no GPUs to provision."` — L234. Meta statement; not an independent measurement.

## cheekypint.txt — Cheeky Pint / https://cheekypint.substack.com/p/muse-wonder-zuckerberg-and-wangs — publication date not captured; accessed 2026-11-10 — A

- [Q6] [GAP] `"there’s still plenty of room to improve."` — Zuckerberg/Wang interview, 2026-10-12; L456. Wang’s Active Memory qualification; model plus system, not perfect persistent recall.
- [Q1] [FACT] `"we’re going to start off primarily in paid subscriptions."` — Zuckerberg/Wang interview, 2026-10-12; L528. Zuckerberg on larger, more-expensive Wonder; free Muse primarily Spark. Future equal-capability smaller model is aspirational.
- [Q2] [FACT] `"we have our own internal evals of Memory Bench"` — Zuckerberg/Wang interview, 2026-10-12; L396. Wang identifies internal measurement; not external corroboration.
- [Q10] [FACT] `"if you have an allergy or you’re pregnant or something"` — Zuckerberg/Wang interview, 2026-10-12; L652. Zuckerberg describes privacy/discretion goal when reserving restaurants; not proof of enforcement.
- [Q6] [STRENGTH] `"we trained into the models very good browser use"` — Zuckerberg/Wang interview, 2026-10-12; L1480. Zuckerberg: browser fallback intended to work without partner integration; partners can provide direct APIs.
- [Q7] [FACT] `"state-of-the-art on DeepSWE and, SWE-Marathon"` — Zuckerberg/Wang interview, 2026-10-12; L496. Wang vendor benchmark claim; interview is commercially interested, not independent measurement.
- [Q12] [GAP] `"you only get 1 minute in between the rounds."` — Zuckerberg/Wang interview, 2026-10-12; L88. Zuckerberg’s MMA video-coaching latency constraint, not a general API latency statistic.

## contemplating-safety.txt — Unavailable capture / https://ai.meta.com/static-resource/muse-spark-contemplating-safety-and-preparedness-report/ — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Empty capture (0 bytes); no evidence.


## dev-spark11.txt — Muse Spark | Meta / https://dev.meta.ai/models/muse-spark-1-1 — publication date not captured; accessed 2026-11-10 — A

- [Q6] [FACT] `"Build and orchestrate multi-agent workflows with one model — including computer use, which lets the model operate a computer the way humans do, navigating across apps and interfaces to complete long-horizon tasks."` — L46. Meta product claim; not independently measured.
- [Q12] [FACT] `"Muse Spark writes, reviews, and ships code with fewer steps and lower latency."` — L48. Meta product claim; not independently measured.
- [Q3] [STRENGTH] `"Muse Spark is trained to deliver competitive agentic and coding performance, with multimodal perception built in."` — L52. Meta product claim; not independently measured.
- [Q6] [FACT] `"Point your existing OpenAI SDK compatible client at Meta Model API."` — L131. Meta product claim; not independently measured.

## dev-spark13.txt — Muse Spark 1.3 | Meta / https://dev.meta.ai/models/muse-spark — publication date not captured; accessed 2026-11-10 — A

- [Q6] [FACT] `"Tuned for long-horizon coding workflows, with fewer unnecessary turns and cleaner output."` — L49. Meta product claim; not independently measured.
- [Q1] [FACT] `"Meta Model API Direct, self-serve and affordable access to Muse Wonder."` — L129. Meta product claim; not independently measured.
- [Q1] [FACT] `"OpenRouter Swap Muse Wonder into your existing tools and workflows."` — L131. Meta product claim; not independently measured.
- [Q6] [FACT] `"Point your existing OpenAI SDK compatible client at Meta Model API."` — L153. Meta product claim; not independently measured.
- [Q6] [FACT] `"Multi-agent orchestration Stand up a four profile agentic team that turns a one line product idea into a working SaaS app."` — L155. Meta product claim; not independently measured.
- [Q13] [FACT] `"Agent fan-out Spin multiple subagents into isolated worktrees to tackle parallel work without mid-flight collisions."` — L157. Meta product claim; not independently measured.

## eval-method.txt — Unavailable capture / https://ai.meta.com/static-resource/muse-spark-eval-methodology — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Empty capture (0 bytes); no evidence.


## eval11.txt — Unavailable capture / https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report/ — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Empty capture (0 bytes); no evidence.


## fbnews.txt — Introducing Muse Spark: Meta's Most Powerful Model Yet / https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs-first-model-built-to-prioritize-people/ — publication date not captured; accessed 2026-11-10 — A

- [Q10] [FACT] `"We will also be offering the model in private preview via API to select partners."` — L240. Meta statement; not an independent measurement.
- [Q1] [FACT] `"Muse Spark is starting to gradually roll out on Ray-Ban Meta and Oakley Meta glasses in the US and Canada over the next few weeks, and on Meta Ray-Ban Display this summer."` — L251. Meta statement; not an independent measurement.
- [Q5] [FACT] `"We’re testing a couple new experiences here too: side chats that let you tap the Meta AI icon from any group chat to get a quick, private answer grounded in what your group is discussing, and @meta.ai mentions in Threads posts and replies."` — L251. Meta statement; not an independent measurement.
- [Q3] [FACT] `"Muse Spark now powers the Meta AI assistant in the Meta AI app and meta.ai, built to support complex reasoning and multimodal tasks."` — L256. Meta statement; not an independent measurement.
- [Q13] [FACT] `"You can switch between modes depending on the task, and Meta AI can launch multiple subagents in parallel to tackle your question."` — L258. Meta statement; not an independent measurement.
- [Q3] [STRENGTH] `"That is why we built strong multimodal perception into Muse Spark, so Meta AI can see and understand what you are looking at, not just read what you type."` — L260. Meta statement; not an independent measurement.
- [Q10] [FACT] `"It will be available in private preview via API to select partners, and we hope to open-source future versions of the model."` — L267. Meta statement; not an independent measurement.
- [Q10] [STRENGTH] `"And as our models improve, we’ll continue to build safeguards for things like safety and privacy, starting with the strengthened risk framework and other protections we’re sharing today."` — L268. Meta statement; not an independent measurement.

## gh-search-failures.txt — GitHub search issue/PR body excerpts / GitHub URLs on each bullet — 2026-08-06–2026-11-10 (per-row dates) — C (excerpts; original threads not all available)

TSV body excerpts only, not complete threads; duplicate issue IDs/full-thread captures count once. More than ~40 bullets retained because the addendum explicitly requests every relevant failure. Unattributed issue bodies do not establish independent human reporter identities.

- [Q8] [BUG] `"## Intent  Fix the false Meta Model API unauthenticated startup warning in the RooseveltAdvisors pi-meta-ai package. Use public ctx.modelRegistry.getProviderAuthStatus(PROVIDER_ID).configured as the authoritative stored/provider authentication truth and stop depending on private"` — RooseveltAdvisors/pi-meta-ai#1, 2026-08-14; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L3; https://github.com/RooseveltAdvisors/pi-meta-ai/pull/1. Search excerpt: fix(meta-model-api): use public auth status
- [Q12] [BUG] `"### Summary  I've used muse spark 1.2 contributor and it it'd been the cheapest model to use at command-code, today was charged my go plan and   started to solve some bugs on a project with 1.3 contributor, only with 54.1m tokens I hit my limits, it means I spent 3 credits on"` — CommandCodeAI/command-code#799, 2026-09-03; attribution: unclear (contributor caching/metering symptom, no verified provider accounting cause); L4; https://github.com/CommandCodeAI/command-code/issues/799. Search excerpt: muse spark 1.3 contributor usage bug
- [Q9] [BUG] ``"### Description  Error: Error from provider (Console): Upstream request failed: [invalid_request_error] reasoning `encrypted_content` was not issued to this caller when requesting any Muse Spark model on Zen.  ### Plugins  None  ### OpenCode version  0.0.0-beta-18050  ### Steps"`` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); L8; https://github.com/anomalyco/opencode/issues/48741. Search excerpt: Opencode Zen critical errors on Muse Spark family when model recieves a image/does a tool call
- [Q8] [BUG] ``"## What's Wrong?  The `/goal` Stop-hook evaluator sends an `output_config.format` JSON schema whose `required` array omits one of its own properties (`impossible`). Any backend that enforces the strict schema subset (`required` must list every key in `properties`) rejects every"`` — anthropics/claude-code#95021, 2026-09-17; attribution: harness/router-side (invalid /goal JSON schema; strict Meta rejection is not model defect); L10; https://github.com/anthropics/claude-code/issues/95021. Search excerpt: BUG /goal evaluator schema rejected by strict backends: required omits impossible
- [Q8] [BUG] ````"### Description  `muse-spark-1.3-contributor-free` works successfully through OpenCode, but the same model returns HTTP 403 `FreeTierError` when used through OMP.  The error returned by Zen is:  ```text 403 Error from provider (Console): OpenCode's free tier can only be used"```` — can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L11; https://github.com/can1357/oh-my-pi/issues/12306. Search excerpt: opencode-zen: muse-spark-1.3-contributor-free returns 403 FreeTierError in OMP while working in OpenCode
- [Q8] [BUG] ``"## Summary  - Adds the **Muse Code subscription provider** via OAuth device flow (`muse-code-oauth`). - Fixes the existing **`muse-code` API-key provider** (`baseUrl` alignment + provider catalog/registry entry).  What the change includes:  - **Device flow** authorization for"`` — SIGTERM-015/OmniRoute#1, 2026-09-18; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L12; https://github.com/SIGTERM-015/OmniRoute/pull/1. Search excerpt: feat(oauth): add Muse Code subscription provider (muse-code-oauth) + fix muse-code apikey
- [Q8] [BUG] ``"## Problem  The hosted Muse Spark endpoint (`MUSE_SPARK_BASE_URL=https://api.meta.ai/v1`) now rejects the configured key with **HTTP 401**, so every intelligence call failed: label interpretation, instruction parsing, schedule drafts, the assistant, summaries.  ## Fix  The"`` — kajal-ranvir/MediSafe#4, 2026-09-22; attribution: unclear (configured key rejected 401; no Meta defect proved); L17; https://github.com/kajal-ranvir/MediSafe/pull/4. Search excerpt: fix(intelligence): replace dead Muse Spark key with self-hosted Antigravity gateway
- [Q6] [BUG] `"### Description  With Muse Spark 1.3 free model (at least with this model), there is an issue where the shell command is executing and has been executing at the same time thinking process of the model is executing and when the shell thing ends thinking process just keeps on"` — anomalyco/opencode#51649, 2026-09-27; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); L19; https://github.com/anomalyco/opencode/issues/51649. Search excerpt: Infinite response loop or smth issue
- [Q8] [BUG] ``"## Problem  `muse-spark-1.2/1.3-contributor-free` (OpenCode Free, Responses path) returns empty completions on small `max_output_tokens` budgets. The model spends nearly the entire token budget on internal reasoning before emitting any visible text. When the budget is exhausted"`` — decolua/9router#4387, 2026-09-27; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L20; https://github.com/decolua/9router/pull/4387. Search excerpt: fix(opencode): clamp max_output_tokens for muse-spark to [8000, 1M] to avoid empty completions
- [Q8] [BUG] ``"OpenWebUI shows empty replies for `muse-spark-1.3-contributor-free`, only when streaming.  Setup: - Hermes v0.21.5, oc-free-provider v3.0.0 - Model: `muse-spark-1.3-contributor-free`  Repro: 1. Use `muse-spark-1.3-contributor-free` in OpenWebUI 2. Send any message 3. Reply"`` — anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); L21; https://github.com/anpicasso/hermes-oc-free-provider/issues/3. Search excerpt: Blank replies in OpenWebUI when streaming
- [Q8] [BUG] `"## Summary  Allow Finch users with a Muse Code subscription to authenticate directly through Meta’s browser/device login flow. Finch must implement the credential lifecycle natively; users must not need to install or run the Muse Code harness.  ## Current behavior  Finch"` — darwin-finch/finch#1484, 2026-10-01; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L22; https://github.com/darwin-finch/finch/issues/1484. Search excerpt: Add native Muse subscription device login without the Muse Code harness
- [Q8] [BUG] ``"## What `OpenCodeGoProfile` sets `supports_vision_tool_messages=False` (`plugins/model-providers/opencode-zen/__init__.py`), citing Console-Go #104731 (`422 messages.N.tool.content.str`) and MiMo #47026 (`400 text is not set`). Those failures are **chat-completions-era**. On the"`` — NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); L23; https://github.com/NousResearch/hermes-agent/issues/132837. Search excerpt: opencode-go: supports_vision_tool_messages=False veto is stale on responses/codex transport — native tool-result vision works live
- [Q8] [BUG] ``"## Description Herdr server logs demonstrate rapid detection flapping in pane 17 (`Some(Muse) -> None`) when executing modern Muse Code v1.4.2 (`muse-bin-1.4.2-` via `/home/alfonsodg/.local/bin/muse`).  The bundled manifest `src/detect/manifests/muse.toml` is based on older Muse"`` — alfonsodg/herdr#1, 2026-10-05; attribution: harness/router-side (stale UI/alias detection); L25; https://github.com/alfonsodg/herdr/issues/1. Search excerpt: fix(detect): Muse Code detection flapping in v1.4+ and missing executable aliases
- [Q12] [BUG] ``"On 9router v0.5.95, using the new Muse (Meta Model API) provider with a valid Model API key (connection test: Passed), the model muse/muse-spark-1.3 fails with:  ` ERROR 400 · muse/muse-spark-1.3 · URL: https://api.meta.ai/v1/chat/completions [400]:"`` — decolua/9router#4602, 2026-10-05; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L26; https://github.com/decolua/9router/issues/4602. Search excerpt: [Bug] [Muse (Meta Model API)] unknown parameter `input`
- [Q12] [BUG] ``"### What's broken On the Usage screen, the Muse Code card shows `Unavailable` / `No usage quota reported` whenever no Muse agent is open, although the account has quota. With a Muse agent open (after it has answered once), refreshing the card shows real numbers: 5-hour 100%"`` — getpaseo/paseo#6161, 2026-10-05; attribution: harness/router-side (provider persistence handle); original app import path unverified; L27; https://github.com/getpaseo/paseo/issues/6161. Search excerpt: bug: Muse usage card shows "No usage quota reported" unless a Muse agent is open
- [Q8] [BUG] ``"**Where is the problem?** Meta Model API, Chat Completions (`POST https://api.meta.ai/v1/chat/completions`), model `muse-spark-1.3-contributor`, 2026-10-04.  ### Summary  A common, cheap way to build a calibrated judge or classifier on an LLM is to ask a question whose answer is"`` — meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); L28; https://github.com/meta-models/meta-model-cookbook/issues/57. Search excerpt: Model API: token logprobs for classification and judging (allow logprobs on the answer with minimal reasoning, or a non-reasoning mode)
- [Q8] [BUG] ````"## Metadata  ```yml pull_request_title: "FROM bug/[issue#]-banner-harness-status TO development" branch: "bug/[issue#]-banner-harness-status" ```  ---  ## Impact  - As an **operator**, I expect **the sandbox banner to show a status line for each installable harness** but **the"```` — mifunedev/agro#1341, 2026-10-05; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L29; https://github.com/mifunedev/agro/issues/1341. Search excerpt: bug: banner omits fx, hermes, and muse-code harness status
- [Q8] [BUG] ``"## What happened  At startup the saved model `opencode/muse-spark-1.3-contributor-free` shows in the model picker with an `Unavailable` badge. After Settings, Providers, Refresh providers, the same slug resolves to `Muse Spark 1.3 Free` with no badge.  ## Steps to reproduce  1."`` — pingdotgg/t3code#15994, 2026-10-05; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L31; https://github.com/pingdotgg/t3code/issues/15994. Search excerpt: [Bug]: OpenCode model missing at startup, shows Unavailable until manual provider refresh
- [Q12] [BUG] ``"## Environment - 9Router v0.5.95 (npm global install, Windows) - Provider: Muse (Meta Model API), connected via API key - Affected: all 5 models (muse-spark-1.3, 1.2, 1.1, 1.3-contributor, 1.2-contributor)  ## Describe the bug All chat completions via `muse/*` fail with upstream"`` — decolua/9router#4624, 2026-10-06; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L33; https://github.com/decolua/9router/issues/4624. Search excerpt: [Bug] Muse provider fails with 400 `unknown parameter "input"` — broken targetFormat routing
- [Q8] [BUG] `"Muse Spark models served through tool gateways (observed: muse-spark-1.3-contributor via OpenCode Zen, openai-responses API) sometimes emit their native harness grammar as plain assistant text instead of a structured tool call. The turn then ends with stop instead of toolUse,"` — monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; L34; https://github.com/monotykamary/pi-tool-repair/pull/6. Search excerpt: feat(grammar): add atem harness leak recovery
- [Q8] [BUG] `"Reported on Discord: https://discord.com/channels/1481169421832814616/1557469649409540158  > I have been trying to import a muse code session on paseo, but it fails every time, claude code sessions work fine.  Importing Claude Code sessions works for the same user. Every Muse"` — getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; L36; https://github.com/getpaseo/paseo/issues/6342. Search excerpt: Importing a Muse Code session fails with "Invalid plugin provider persistence handle"
- [Q8] [BUG] ````"## Error  Muse Code (`muse` 1.4.4, 1.4.4-R5419.1) connected to magpie, model `cline-free/muse-spark-1.3-contributor` (Muse Spark 1.3 free) on the Cline provider:  ``` model failed: stream protocol error: undeclared_tool: Upstream called a tool not declared by the client"```` — yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L37; https://github.com/yetone/magpie/issues/1448. Search excerpt: gateway: Muse Code on Cline's Muse Spark 1.3 free fails with undeclared_tool (Upstream called a tool not declared by the client)
- [Q8] [BUG] ````"## Problem  `handleComboChat` (`open-sse/services/combo.js`) treats any 2xx from `handleSingleModel` as success:  ```js // Success (2xx) - return response if (result.ok) {   log.info("COMBO", `Model ${modelStr} succeeded`);   return result; } ```  Some upstreams — notably"```` — decolua/9router#4736, 2026-10-11; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L40; https://github.com/decolua/9router/issues/4736. Search excerpt: [combo] Zero-content HTTP 200s count as success and defeat fallback
- [Q12] [BUG] ``"### Before submitting  - [X] I searched existing issues and did not find a duplicate. - [X] I included enough detail to reproduce or investigate the problem.  ### Area  apps/server  ### Steps to reproduce  1. On a host where `muse login` is signed in to a Meta subscription,"`` — pingdotgg/t3code#18235, 2026-10-11; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L41; https://github.com/pingdotgg/t3code/issues/18235. Search excerpt: [Bug]: Muse Code's subscription usage never shows in Usage → Limits
- [Q8] [BUG] ``"## Problem  A Claude Code (`/v1/messages`) request that replays a thinking block is forwarded to a Responses upstream with a `reasoning` input item that has `encrypted_content` but **no `summary`**. The Responses API requires `summary` on every reasoning input item (an empty"`` — Wei-Shaw/sub2api#8044, 2026-10-12; attribution: harness/router-side (reasoning replay missing summary); L43; https://github.com/Wei-Shaw/sub2api/pull/8044. Search excerpt: fix(apicompat): add required summary to replayed reasoning input items
- [Q8] [BUG] ````"## Environment - omo 5.1.30 (standalone, darwin arm64, engine senpi 2026.10.11) - macOS, Apple Silicon  ## Settings (relevant keys of `~/.omo/agent/settings.json`) ```json {   "defaultProvider": "meta",   "defaultModel": "meta/muse-spark-1.3-contributor","```` — code-yeongyu/oh-my-openagent#10063, 2026-10-12; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L44; https://github.com/code-yeongyu/oh-my-openagent/issues/10063. Search excerpt: [bug] Fresh omo ignores defaultModel, auto-switches to deepseek-v4-pro
- [Q8] [BUG] ``"## Problem Fresh sessions on the Muse and Antigravity lanes seed the entire canonical history and rely on the host to compact it.  ## Observed failure (2026-10-12, ~/me/.masc) - `e-masc-the-leader` Start prompt 5,059,041 bytes (~1.28M tokens) vs muse-spark-1.3 hard threshold"`` — jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); L45; https://github.com/jeong-sik/masc/issues/42597. Search excerpt: Muse/Antigravity Start seeds the whole canonical history and exceeds host limits
- [Q12] [BUG] ``"## Summary  `/usage` (and `omp usage --provider muse-code`) shows `Muse Code — 1 account, no usage data` once the Meta account OAuth token expires. The underlying error is a 401 from `POST https://api.meta.ai/muse-code/key`, visible only in debug logs. Nothing tells the user to"`` — can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L48; https://github.com/can1357/oh-my-pi/issues/15551. Search excerpt: /usage: muse-code shows "no usage data" after Meta account token expires — no re-login hint (refresh "none")
- [Q8] [BUG] ``"## Summary  Personal and project skills appear in the composer skill picker on Claude and Codex threads, but not on Muse Code threads in the same checkout.  ## Steps to reproduce  1. Open a project that has personal skills in `~/.agents/skills/*` (e.g. `dependency-updater`)"`` — pingdotgg/t3code#19155, 2026-10-13; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L50; https://github.com/pingdotgg/t3code/issues/19155. Search excerpt: [Bug]: Muse provider doesn't surface Personal/Project skills in composer skill picker
- [Q8] [BUG] ``"### Description  Issued authored by `ask-omp`, edited by me (human).  ### What happens Using the built-in `muse-code` provider with `muse-wonder-1.0` (auto-discovered after logging in with a Muse Code subscription, default catalog entry, no custom `models.yml`), the assistant"`` — can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L52; https://github.com/can1357/oh-my-pi/issues/15737. Search excerpt: muse-code/muse-wonder-1.0` prints tool-call markup as plain text instead of making a tool call
- [Q12] [BUG] `"### What's broken  In a Muse Code agent's chat, the usage meter in the input only shows context usage. The 5-hour and Weekly windows never appear, even after the agent has answered and while it is still open. Claude and Codex agents on the same daemon show their windows in the"` — getpaseo/paseo#6894, 2026-10-14; attribution: harness/router-side (provider persistence handle); original app import path unverified; L53; https://github.com/getpaseo/paseo/issues/6894. Search excerpt: bug: usage meter in chat input never shows 5h/weekly windows for Muse Code agents
- [Q9] [BUG] ``"## Summary  `MuseSparkRenderer.bridge_to_next_turn` returned `None`, so multi-turn clients (the Verifiers train client) re-rendered every agent turn from parsed messages. Parsing is lossy: it strips whitespace, merges reasoning channels and re-serializes tool arguments. After a"`` — wwwjn/torchtitan#15, 2026-10-16; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L58; https://github.com/wwwjn/torchtitan/pull/15. Search excerpt: [Muse Spark Open] Bridge multi-turn prompts in the renderer
- [Q8] [BUG] ``" ## What does this PR do?  Muse Spark 1.3 accepts `reasoning.effort: max` as a level above `xhigh`. Hermes clamped `max` down to `xhigh` on both the direct Meta route and the OpenCode Zen/Go Responses route, because those paths used a vocabulary that stopped at `xhigh`. Spark"`` — NousResearch/hermes-agent#140813, 2026-10-18; attribution: harness/router-side (dispatch/capability/effort handling); L61; https://github.com/NousResearch/hermes-agent/pull/140813. Search excerpt: fix(agent): accept reasoning effort max on Muse Spark 1.3
- [Q8] [BUG] `"## Overview  Bound Muse's ATEM attribute scans to a single tag and avoid reparsing tool calls on streaming deltas that cannot complete an invocation. This updates the existing fix after review; it does not add a separate parser or change the shared parser interface.  ## Claims"` — vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); L63; https://github.com/vllm-project/vllm/pull/62345. Search excerpt: [Bugfix][Security] muse: fix quadratic attribute scans in tool-call extraction
- [Q8] [BUG] ``"## Summary  Kanban worker on profile `readwhere` (model `muse-spark-1.3-contributor`, provider `opencode-go`) fails every LLM call with HTTP 400 `ModelProtocolUnsupported` ("Model does not support this protocol"). The worker POSTs to"`` — NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); L66; https://github.com/NousResearch/hermes-agent/issues/141861. Search excerpt: [bug] Kanban worker posts chat/completions despite resolved api_mode=codex_responses: muse-spark on opencode-go gets 400 ModelProtocolUnsupported
- [Q8] [BUG] ``"### Environment - OS: Windows 11 - Magpie: 0.1.1307 (`C:\\Program Files\\magpie-windows-amd64.exe`, FileVersion 0.1.1307, latest as of 2026-10-21) - Codex: 0.163.0-alpha.11 (Desktop, `CODEX_VERSION=0.163.0-alpha.11`) - Model route: `opencode-go/muse-spark-1.3-contributor` via"`` — yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L70; https://github.com/yetone/magpie/issues/3152. Search excerpt: [Bug] Tool calls fail when model emits whole floats (e.g. limit 8.0) - Codex strict int parsing
- [Q8] [BUG] ``"## Describe the bug  **This report is model-specific and scoped only to Muse Spark Open through the Rust vLLM sidecar (`dynamo-vllm-sidecar`).** The affected configuration advertises backend-gated reasoning while Dynamo's Muse Spark structural-tag builder requires control of the"`` — ai-dynamo/dynamo#17071, 2026-10-22; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L72; https://github.com/ai-dynamo/dynamo/issues/17071. Search excerpt: BUG: Muse Spark Open — Rust vLLM sidecar reasoning-gate metadata blocks model registration
- [Q9] [BUG] ``"<!-- markdownlint-disable -->  ## Overview  Muse Spark builds FP32 RoPE tables, but three call sites rotate through `RotaryEmbedding`'s forward, which replaces the table with a BF16 copy (eager) or casts the whole table on every call (compiled): the DSpark context-key precompute"`` — vllm-project/vllm#63078, 2026-10-22; attribution: harness/router-side (inference runtime/parser); L73; https://github.com/vllm-project/vllm/pull/63078. Search excerpt: [Bugfix][Muse Spark] Keep the FP32 RoPE tables in FP32
- [Q12] [BUG] `"## What  Muse Code connections now show their real subscription usage, the 5-hour session window and the weekly allowance, on the usage page and in quota routing. Until now the usage fetcher reported only the subscription tier, with the message "No usage API available from Meta"` — cheaper-inference/OmniRoute#18122, 2026-10-25; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L75; https://github.com/cheaper-inference/OmniRoute/pull/18122. Search excerpt: feat(providers): show Muse Code session and weekly usage
- [Q8] [BUG] ``"## Problem  On Windows, Muse Code shows **Unavailable · Muse Code CLI version check timed out.** on every refresh, even though `muse` works from a terminal (https://git.cafe/pingdotgg/t3code/issues/24165). The reporter traced it: Muse takes about 4 to 9 seconds to answer `muse"`` — pingdotgg/t3code#24676, 2026-10-25; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L77; https://github.com/pingdotgg/t3code/pull/24676. Search excerpt: fix(muse): slow Windows starts no longer show Muse as unavailable
- [Q6] [BUG] ``"**Describe the bug**  When the `ollama` provider points at a local Ollama daemon that proxies Ollama Cloud models, the context window falls back to the 128k default. The GUI shows `X / 128k` for models that actually have a 1M window.  Two independent causes, both about the same"`` — aaif-goose/goose#13151, 2026-10-26; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L83; https://github.com/aaif-goose/goose/issues/13151. Search excerpt: Ollama provider reports 128k context window for Ollama Cloud models that serve 1M
- [Q12] [BUG] ``"## Problem  Muse Code subscription usage never appeared in Usage → Limits because the adapter ignored the account-wide `usage/changed` notification. After a server restart, waiting for a model reply also leaves limits unavailable even though Muse 1.4.13 can fetch them without a"`` — pingdotgg/t3code#25165, 2026-10-26; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L85; https://github.com/pingdotgg/t3code/pull/25165. Search excerpt: fix(server): Muse Code's subscription usage shows in Usage → Limits; proposed fix/control for #18235, not a second independent usage failure.
- [Q8] [BUG] ``"### Context  Follow-up to [#11928](https://github.com/can1357/oh-my-pi/issues/11928), addressed by [#11931](https://github.com/can1357/oh-my-pi/pull/11931).  PR #11931 disabled requesting and replaying `reasoning.encrypted_content` for Muse Spark on both OpenCode Zen and"`` — can1357/oh-my-pi#17268, 2026-10-28; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L96; https://github.com/can1357/oh-my-pi/issues/17268. Search excerpt: Re-enable encrypted reasoning replay for OpenCode Go Muse Spark (validated on OMP v18.12.6); replay works on Go in this later report: conflicts with blanket-disable advice for Zen, not necessarily same route/version.
- [Q9] [BUG] ``"## Summary  Two hand-authored files describe a standalone checkout's behaviour in ways a clean clone of this mirror does not reproduce.  **`README.md`**  - It said to run `npm install`. The root workspace lists `clients/acp`, which this mirror does not carry, so `npm install`"`` — meta-models/muse-code-sdk#122, 2026-10-28; attribution: Meta/Muse-side SDK/access/integration report; title/excerpt only; L98; https://github.com/meta-models/muse-code-sdk/pull/122. Search excerpt: README, bug template: use npm ci and state the standalone test failures the mirror actually has
- [Q8] [BUG] `"### Description  ---- [!!] 403 This API key is billed to a Muse Code subscription. Muse Code subscriptions cover requests from the Muse    Code client only. Use it in Muse Code, or use a pay-as-you-go API key for other clients.    This API key is billed to a Muse Code"` — can1357/oh-my-pi#17435, 2026-10-30; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L107; https://github.com/can1357/oh-my-pi/issues/17435. Search excerpt: Muse Code subscriptions cover requests from the Muse  Code client only; official-client-only subscription policy, not proof of random service failure.
- [Q8] [BUG] `"## Overview  Track Muse Spark Open specific improvements on NVIDIA and AMD.  Scope: model-specific optimization PRs in vLLM and AITER. Excludes initial model enablement, generic infrastructure, FlashInfer, DeepGEMM, and closed-unmerged PRs.  ## NVIDIA   - [x] #63871 — Fix"` — vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); L111; https://github.com/vllm-project/vllm/issues/64632. Search excerpt: [Tracking] Muse Spark Open Improvement
- [Q12] [BUG] `"## Feature hasn't been suggested before.  - [x] I have verified this feature I'm about to request hasn't been suggested before.  ## Describe the enhancement you want to request  Meta Model API responses already carry per-request usage and x-ratelimit-* quota headers, but"` — anomalyco/opencode#60981, 2026-10-31; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); L112; https://github.com/anomalyco/opencode/issues/60981. Search excerpt: [FEATURE]: Surface Meta Model API usage quota
- [Q8] [BUG] ``"_Posted by Claude Code on Douwe's behalf._  ### Background  Found in a scan of inference hosts (2026-10-30). Evidence: [D] Groq models and structured-output docs, [V] `model_profile()` on `main` (`17a8a83fc5`).  ### Problem  Groq's model page lists production models"`` — pydantic/pydantic-ai#12083, 2026-10-31; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L114; https://github.com/pydantic/pydantic-ai/issues/12083. Search excerpt: `GroqProvider` profiles have drifted from Groq's current models (Muse Spark Open, MiniMax M2.7, JSON modes)
- [Q8] [BUG] ``"_Posted by Claude Code on Douwe's behalf._  ### Description  `OpenRouterProvider` assumes forced tool choice with thinking on works on every non-Anthropic route (`supports_forced_tool_choice_with_thinking`). A live probe on 2026-10-31 (n=2 per cell, tool output) got a 400 on"`` — pydantic/pydantic-ai#12110, 2026-10-31; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L115; https://github.com/pydantic/pydantic-ai/issues/12110. Search excerpt: Forced tool choice with thinking fails on OpenRouter Qwen, Muse Spark and GLM-5.3 routes
- [Q8] [BUG] ``"### What happened  Three Windows-only gaps found while installing `oh-my-musecode` 1.0.1 on Windows x64 with Muse Code 1.4.14. One has a verified fix (PR to follow); the other two have a diagnosed root cause and a proposed fix, both unverified in code.  **1. `omm lint` / `omm"`` — hypery11/oh-my-musecode#2, 2026-11-02; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L129; https://github.com/hypery11/oh-my-musecode/issues/2. Search excerpt: [bug] Windows support gaps: lint fs-backslash false positive, muse binary locate, D15 PATH; lint fix reported verified; binary discovery and PATH diagnoses/proposals remain unverified in code.
- [Q8] [BUG] ``"### What happened  On Windows, `muse plugins install <plugin>@<marketplace>` for a `local-dir` marketplace fails with `invalid-plugin-package: failed integrity check`, while installing the exact same bundle by direct path succeeds (validates, installs, approves, runs).  ###"`` — meta-models/muse-code-sdk#133, 2026-11-02; attribution: Meta/Muse-side SDK/access/integration report; title/excerpt only; L130; https://github.com/meta-models/muse-code-sdk/issues/133. Search excerpt: [bug] Marketplace local-dir install fails integrity check on Windows while direct-path install succeeds
- [Q8] [BUG] ``"## Summary Models served through the 9Router `muse` provider (upstream: Moonshot/Kimi `muse-spark` family) return empty `choices[0].message.content` on `POST /v1/chat/completions`, both streaming and non-streaming. The same models, same key, same gateway return correct answers"`` — decolua/9router#5426, 2026-11-03; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L134; https://github.com/decolua/9router/issues/5426. Search excerpt: [muse] chat/completions returns empty content for muse-spark models, responses works
- [Q12] [BUG] `"Found by the pool-quota steward (run 132, 2026-11-03) during the step-6 PM page-truth check after the PR #5080 pass-through landing.  Read (source of truth): quota-current.json gatherer tick 2026-11-03T19:30:08.572Z, source openchamber-quota; meta measuredAt"` — developing-today/code#5101, 2026-11-03; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L135; https://github.com/developing-today/code/issues/5101. Search excerpt: aggregator(quota): /quota attention item lags the pass-through read — Meta weekly attention says 98% while the fresh read and the same payload's pool row say 99%
- [Q6] [BUG] ``"With parallel tool calls on the OpenAI Responses API, the second call ran with the first call's arguments.  Some gateways (opencode-go: muse-spark, gpt-*-luna, grok) announce every `function_call` item first and send the argument events afterwards. `ResponsesStreamState` had one"`` — kolisachint/hoocode#171, 2026-11-03; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L136; https://github.com/kolisachint/hoocode/pull/171. Search excerpt: Responses stream: keep each parallel tool call's own arguments
- [Q8] [BUG] `"## Problem  When Muse Code generates a commit message, PR text, branch name, or thread title and the Muse turn fails, T3 Code always says "Muse Code text generation failed. Check Muse login and availability on this T3 server host." A user who is signed in but out of quota, or"` — pingdotgg/t3code#29861, 2026-11-03; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L139; https://github.com/pingdotgg/t3code/pull/29861. Search excerpt: fix(muse): failed Muse text generation explains Muse's error category
- [Q8] [BUG] `"GPT-6 · 2026-11-03 — review-only, docs-only corrections to the existing Repair Bench submission materials.  ## What changed - Corrected the 2:15–2:45 Meta narration to 62 words (about 29 seconds at 130 wpm) in both the teleprompter and timed script. Both Muse Spark patches"` — KyPython/repair-bench#5, 2026-11-04; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L145; https://github.com/KyPython/repair-bench/pull/5. Search excerpt: docs(submission): correct Muse Spark evidence and demo timing; both Muse patches failed scope review and were never executed/scored; separate operator candidate’s 9/9 score is NOT Muse performance.
- [Q9] [BUG] ``"## Context  On **dynamo-vllm**, **`enable-auto-tool-choice`** is not available on the worker (treated as an OpenAI APIServer-only option; our deployment allowlist omits it for the same reason). The supported approach is to configure **`dyn-tool-call-parser`** (we use **`muse`**"`` — ai-dynamo/dynamo#18075, 2026-11-04; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L147; https://github.com/ai-dynamo/dynamo/issues/18075. Search excerpt: dynamo-vllm: tool_choice=required fails with dyn-tool-call-parser=muse
- [Q8] [BUG] `"### Where is the problem?  Something else / not sure  ### What happened, and what did you expect instead?  Problem  I purchased a Muse Code High Usage subscription on November 2, 2026, for 699 TRY. The subscription is active in Meta Accounts Center, but I have been unable to use"` — meta-models/muse-code-sdk#135, 2026-11-04; attribution: Meta/Muse-side SDK/access/integration report; title/excerpt only; L153; https://github.com/meta-models/muse-code-sdk/issues/135. Search excerpt: Muse Code: Paid subscription blocked by /unavailable?reason=age despite adult account
- [Q8] [BUG] ``"## Problem  `POST /v8/management/credentials/verify` (`Manager.VerifyInference`) sends a Responses request with `"max_output_tokens":1`. On v8.0.53 and on `dev` it cannot verify a credential on any of the four providers we run it against:  | provider (model) | answer | | --- |"`` — router-for-me/CLIProxyAPI#7249, 2026-11-04; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L155; https://github.com/router-for-me/CLIProxyAPI/pull/7249. Search excerpt: fix(auth): let credential verification pass on the providers' minimum output budget
- [Q8] [BUG] `"### What this PR does / why we need it?  Running Muse Spark with its DSpark draft on Ascend would fail inside a CUDA op, with an error that does not name the cause. This PR makes it fail when the draft is loaded, with a clear message instead.  **Why it fails today.** Upstream"` — tgrhn/vllm-ascend#6, 2026-11-04; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L156; https://github.com/tgrhn/vllm-ascend/pull/6. Search excerpt: [BugFix] Refuse the Muse Spark DSpark draft on Ascend at load time
- [Q8] [BUG] ``"From decolua/9router#5426 (by @wukuwuye-code, 2026-11-03T09:48:01Z)  ## Summary Models served through the 9Router `muse` provider (upstream: Moonshot/Kimi `muse-spark` family) return empty `choices[0].message.content` on `POST /v1/chat/completions`, both streaming and"`` — eduardez/9router#9, 2026-11-05; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L158; https://github.com/eduardez/9router/issues/9. Search excerpt: [muse] chat/completions returns empty content for muse-spark models, responses works; explicitly copied from decolua/9router#5426 by @wukuwuye-code, not an independent reporter.
- [Q8] [BUG] ``"Part of #255 (Company Map step 14, T6 production rebuild).  **What happened.** On 2026-11-04 from 7:41 PM EST, every relations call to `meta/muse-spark-1.3-contributor` through our OpenRouter key failed with `403 Provider returned error` → raw"`` — u2giants/theoracle#426, 2026-11-05; attribution: unclear (upstream/provider versus client not established by excerpt); L159; https://github.com/u2giants/theoracle/issues/426. Search excerpt: OpenRouter: Muse Spark 1.3 returns 403 user_blocked (policy violations) on our key
- [Q8] [BUG] ``"Groq model profiles advertised stale JSON-output capabilities: family profiles (kimi, gpt-oss, llama-4) had their `supports_json_schema_output` clobbered, models without native JSON-schema support advertised it, and `NativeOutput` combined with function tools sent a request Groq"`` — pydantic/pydantic-ai#12667, 2026-11-06; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L163; https://github.com/pydantic/pydantic-ai/pull/12667. Search excerpt: Fix Groq JSON output flags and guard `NativeOutput` against function tools
- [Q8] [BUG] ````"## What this fixes  A Muse session whose **owner account is cooling down** used to be rejected as a cross-account continuation:  ``` Muse session owner is unavailable; cross-account continuation is forbidden. ```  (503). The owner was present and pinned; it was only rate limited"```` — cheaper-inference/OmniRoute#19291, 2026-11-07; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L166; https://github.com/cheaper-inference/OmniRoute/pull/19291. Search excerpt: fix(providers): stop refusing Muse Code turns that Muse accepts
- [Q8] [BUG] `"## Summary  On a local OpenBot instance, connecting the Muse provider opens Chrome to authorize Muse Code. The browser reports that Muse Code was successfully authorized. After returning to OpenBot, the Muse provider still shows **Not connected**, with the error **OpenBot could"` — nightly-labs/openbot#5544, 2026-11-07; attribution: unclear (upstream/provider versus client not established by excerpt); L167; https://github.com/nightly-labs/openbot/issues/5544. Search excerpt: [Bug]: Muse Connect OAuth succeeds in browser but OpenBot stays Not connected
- [Q8] [BUG] `"## What a user meets  A remote Codex, Muse Code or Antigravity tab (over SSH, inside Koloft's tmux) on a machine whose tmux is older than 3.7 can still tear while its screen redraws: part of the screen shows the new frame, the rest the old one, for a frame. That is most machines"` — superkoh/koloft#1578, 2026-11-07; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L168; https://github.com/superkoh/koloft/issues/1578. Search excerpt: Remote Codex, Muse Code and Antigravity tabs may still tear while they redraw, behind tmux before 3.7
- [Q8] [BUG] `"### Your current environment  The is in relation to [vllm/vllm-openai:muse-spark-open](https://hub.docker.com/layers/vllm/vllm-openai/muse-spark-open/images/sha256-2790bff92e9f2a796dcb65682dc5c2e9559f967a4b773f6ae4ca09dbd31c1081)  ### 🐛 Describe the bug  As of the date of this"` — vllm-project/vllm#66293, 2026-11-07; attribution: harness/router-side (inference runtime/parser); L169; https://github.com/vllm-project/vllm/issues/66293. Search excerpt: [Bug]: vllm/vllm-openai:muse-spark-open needs to be rebuilt with the issue fixed in #62374
- [Q8] [BUG] ``"### Where is the problem?  Something else / not sure — Python SDK diagnostic and documentation URL.  ### What happened, and what did you expect instead?  The published `muse-code-sdk==1.4.14` wheel embeds `https://meta-models.github.io/muse-code-sdk/compatibility/` in"`` — meta-models/muse-code-sdk#143, 2026-11-08; attribution: Meta/Muse-side SDK/access/integration report; title/excerpt only; L175; https://github.com/meta-models/muse-code-sdk/issues/143. Search excerpt: [Bug]: Python 1.4.14 mismatch diagnostic points to a compatibility URL that returns 404
- [Q8] [BUG] `"### Where is the problem?  Something else / not sure — Python SDK automatic admission retry.  ### What happened, and what did you expect instead?  The normative [ErrorData retryable"` — meta-models/muse-code-sdk#144, 2026-11-08; attribution: Meta/Muse-side SDK/access/integration report; title/excerpt only; L176; https://github.com/meta-models/muse-code-sdk/issues/144. Search excerpt: [Bug]: Python Connection.command retries eligible admission errors despite retryable:false (1.4.14)
- [Q8] [BUG] ``"## Summary Closes #19315.  When dispatching requests with `targetFormat: "openai-responses"` on the `opencode-zen` provider (`gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `grok-4.6`, `grok-build-0.1`, `muse-spark-1.2`, `muse-spark-1.3`, etc.), `usesZenApiKeyAuth()` in"`` — cheaper-inference/OmniRoute#19547, 2026-11-09; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L179; https://github.com/cheaper-inference/OmniRoute/pull/19547. Search excerpt: fix(providers): supply Authorization Bearer for opencode-zen keyed responses endpoints
- [Q8] [BUG] ````"### Name and Version  ``` version: 0.9.0 (build 12110, commit cd959bae9) built with AppleClang 21.0.0.21000401 for Darwin arm64 ``` Also seen on 0.8.0 (Homebrew).  ### Operating systems  macOS 26.4.1  ### GGML backends  Metal  ### Hardware  Mac Studio M3 Ultra, 512 GB  ###"```` — ggml-org/llama.cpp#31950, 2026-11-09; attribution: harness/router-side (inference grammar/parser); L181; https://github.com/ggml-org/llama.cpp/issues/31950. Search excerpt: Misc. bug: server: Muse Spark Open — every grammar fails "Failed to initialize samplers" (generation prompt '<|start|>assistant'); response_format ignored
- [Q8] [BUG] ``"> 11-09 21:10 KST 수정: 처음 글은 `Your call to "` 로 시작하는 거절만 세어서 401건(1.8%)이라고 적었어요. Execute 는 자기 메시지(`received an empty input object`)로 거절해서 빠졌고, 그 글의 "Execute 는 0건" 줄이 틀렸어요. 아래는 둘을 합쳐 다시 센 값이에요.  ## 증상  Muse Spark 1.3 lane 을 쓰는 Keeper 의 도구 호출 일부가 인자 없이(`input` 이 `{}`) 들어와서 실행 전에"`` — jeong-sik/masc#50637, 2026-11-09; attribution: unclear (upstream/provider versus client not established by excerpt); L182; https://github.com/jeong-sik/masc/issues/50637. Search excerpt: Muse lane 도구 호출의 5.4%가 빈 인자 `{}` 로 들어와 거절돼요 (11월 1,191건, 거절 뒤 같은 도구가 받아들여진 묶음은 15%); correction in captured excerpt: original 401/1.8% attribution wrong, 1,191 calls/5.4% in November; upstream versus serialization unresolved.
- [Q8] [BUG] ````"## Bug  When `muse serve` takes longer than 30 s to answer `initialize`, every cold start fails with:  ```text Cannot start Muse Code (muse). Install Muse and run muse to sign in. ProtocolError: connection reached EOF ```  Muse is installed and signed in, but startup is slow,"```` — openclaw/openclaw#195521, 2026-11-09; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L183; https://github.com/openclaw/openclaw/issues/195521. Search excerpt: Muse: slow Muse starts are reported as a missing install
- [Q8] [BUG] `"## Overview  Fixes #31950  The Muse Spark parser ignores json_schema and only builds a grammar when tools are given. So a top-level json_schema falls back to the server's schema grammar, which fails on the "<|start|>assistant" generation prompt prefill (400), and response_format"` — ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); L191; https://github.com/ggml-org/llama.cpp/pull/32017. Search excerpt: chat : fix Muse Spark ignoring response_format json_schema
- [Q8] [BUG] `"**Before you start:** I read CONTRIBUTING.md and confirm this is a reproducible bug, reproduced on the version below with the exact steps given.  ## Current behavior  A Muse Code pane that has finished its turn and is waiting at its input prompt keeps reporting agent_status"` — herdrdev/herdr#5934, 2026-11-10; attribution: harness/router-side integration/runtime defect described in excerpt; model-side cause not established; L192; https://github.com/herdrdev/herdr/issues/5934. Search excerpt: Muse pane waiting at its prompt never reports idle
- [Q9] [BUG] `"Stacked on #5844.  ## Summary  Image-prompt RL for Muse Spark, and a SLAKE (medical VQA) LoRA GRPO recipe for Muse Spark Open 816B-A42B on GB300.  **Problem**  1. Image RL runs only Qwen3.5. The Muse Spark renderer rejects image parts. 2. The generator and the batcher assume"` — pytorch/torchtitan#5998, 2026-11-10; attribution: harness/router-side (distributed-training/runtime); L196; https://github.com/pytorch/torchtitan/pull/5998. Search excerpt: [rl] Muse Spark image prompts and a SLAKE LoRA GRPO recipe for Muse Spark 816B

## hf-card.txt — meta-models/Muse-Spark-Open-816B-A42B · Hugging Face / https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B — 2026-01-04 — A

- [Q3] [GAP] `"The model may produce inaccurate, biased, or objectionable responses to user prompts."` — L542. Meta model-card limitation.
- [Q6] [GAP] `"While optimized for agentic tasks, the model may still make errors in multi-step reasoning, particularly in novel scenarios not well represented in training data."` — L543. Not an independently measured failure rate.
- [Q3] [GAP] `"The model has not been evaluated on all languages contained in the pre-training data."` — L544. Language coverage caveat.
- [Q3] [BUG] `"When using very short or low-resolution videos (a few seconds at around 100 px), the model may sometimes reply that it can't view the video."` — L547. Meta acknowledges occasional input-processing failure.
- [Q14] [FACT] `"Use longer clips or higher resolution (448 px or more on the short side) for reliable results."` — L547. Video mitigation from Meta.
- [Q11] [FACT] `"The model refused 99.2% of jailbreaks on our internal benchmark and 94.8% when aggregating across PolyGuard (cyber subset), RedCode, and CyberBench 2024."` — L535. Meta API-model evaluation, no system safeguards; benchmark-specific refusal, not a production agent security guarantee.
- [Q11] [FACT] `"refusing over 98% of harmful requests on SecureBio's BioTIER refusal benchmark and over 99% on our internal single-turn chemistry refusal benchmark."` — L536. Vendor-reported bio/chem refusal.
- [Q5] [FACT] `"with a 98.1% honesty rate on the MASK benchmark and a 0% misbehavior rate on the Agentic Misalignment benchmark."` — L537. Tested checkpoint only; zero measured misbehavior is not universal proof.
- [Q11] [GAP] `"These evaluations characterized the released checkpoint under the tested conditions and do not cover every downstream configuration or use case."` — L538. Explicit scope limitation; modifications may degrade safety.
- [Q14] [FACT] `"We recommend implementing additional guardrails (such as human-in-the-loop confirmation for irreversible actions) when deploying the model in agentic contexts where it can take real-world actions."` — L549. Application-level safeguard, not automatic model protection.
- [Q8] [FACT] `"'low': 8, 'medium': 32, 'high': 256, 'xhigh': 512} -%}\n{%- if not"` — L35. Serialized chat-template mapping, not an independent bug report.
- [Q8] [FACT] `"Unsupported reasoning_effort: ' ~ reasoning_effort ~ '. Expected one of: low, medium, high, xhigh.') -}}\n{%- endif -%}\n{%- set"` — L35. Template rejects unsupported effort values; preserve Spark Open versus hosted Spark 1.3 distinction.
- [Q1] [FACT] `"816B total / 42B active"` — L283. Model overview: 1M context, MoE; weights BF16/NVFP4, text output from text/image/video/audio input.
- [Q12] [GAP] `"at least 700GB of VRAM for NVFP4 and 2TB for BF16"` — L304. Meta recommended GPU deployment footprint; quantized Apple/HF demos use different precision/overhead.
- [Q8] [FACT] `"The default is xhigh."` — L308. low/medium/high/xhigh only; other values error. Not hosted Spark 1.3 max effort vocabulary.
- [Q2] [FACT] `"For Muse Spark Open we use xhigh reasoning effort, temperature = 1.0, top_p=1.0, top_k=disabled across benchmarks."` — L313. All following model-card score rows use these settings; methodology mixes internal, official leaderboard and self-report sources.
- [Q2] [STRENGTH] `"JobBench"` — L334. Table value for quoted label: 61.8. Meta comparison table; MCP-Atlas 89.2, OSWorld Verified 80.4, Toolathlon Verified 72.8; benchmark-specific, see methodology provenance.
- [Q2] [STRENGTH] `"HLE-Diamond (no tools)"` — L380. Table value for quoted label: 26.1. HLE with tools 61.0, GPQA Diamond 89.0; no-tools versus tool-assisted results not interchangeable.
- [Q7] [GAP] `"DeepSWE 1.1 Preferred harness"` — L426. Table value for quoted label: 60. Model-card comparison: Kimi K3 68, GLM 5.3 67; different preferred harnesses, not an apples-to-apples base-model test.
- [Q7] [GAP] `"Terminal-Bench 2.1 Terminus 2 agent"` — L444. Table value for quoted label: 76.4. Kimi K3 85.0 and GLM 5.3 83.9; shared Terminus 2 methodology except self-report exceptions in method PDF.
- [Q2] [FACT] `"VideoMMEv2"` — L499. Table value for quoted label: 61.5. Model-card multimodal row; tools/settings differ across evaluation types.
- [Q11] [FACT] `"StrongREJECT v2 (adaptive) lower is better"` — L518. Table value for quoted label: 0.5. Vendor table versus Kimi K3 66.6; benchmark adaptive jailbreak score, not a general 0.5% app compromise rate.

## hf-open.txt — Welcome Muse Spark Open: open-weight frontier multimodal mixture-of-experts model from Meta / https://huggingface.co/blog/meta-muse-spark-open — October 15, 2026 — B

Hugging Face technical article: grade B for its own measured demos, C for explanation, A-provenance for Meta claims quoted within it; runtime recipes have different context/modality support.

- [Q3] [FACT] `"The mixture of experts model brings text, images, audio, and video into a model with approximately 816 billion parameters, around 42 billion active per token, and a context window of up to one million tokens."` — L67.
- [Q2] [FACT] `"Meta describes Muse Spark Open as a coding-optimized model trained on real developer workflows such as multi-file refactors and long debugging sessions."` — L71. HF restates Meta’s training claim; not an independent observed coding failure or measurement.
- [Q1] [FACT] `"Only 8 experts run per token, so the model computes each token with about 42B parameters."` — L91.
- [Q1] [FACT] `"All 256 experts stay in memory, so deployment needs the memory of an 816B-parameter model, but runs at the much faster speed of a 42B model."` — L91.
- [Q3] [FACT] `"The processor expects mono audio at 24 kHz and pads the waveform to a multiple of 1,920 samples, corresponding to one audio embedding per 80 milliseconds."` — L227.
- [Q12] [FACT] `"An imatrix-calibrated 2-bit quant runs at 18 tokens/s, with plenty of room free for the KV cache (304 GB used by the model)."` — L356.
- [Q12] [FACT] `"The model takes about 344 GB, leaving room for the KV cache, and runs at about 225 tok/s prefill and 21 tok/s generation with a 1024-token prompt and 128 generated tokens."` — L443.
- [Q9] [FACT] `"You can deploy Muse Spark Open on Inference Endpoints with a pre-validated SGLang recipe for the NVFP4 variant which runs on either 8 × NVIDIA RTX Pro 6000 98 GB with 131072 context length, or with 8 x NVIDIA H200 141GB if you want 1048576 context length instead."` — L452.
- [Q6] [FACT] `"The endpoint exposes an OpenAI-compatible API with both Chat Completions API at /v1/chat/completions and Responses API at /v1/responses ."` — L456.
- [Q12] [FACT] `"We trained for 500 steps, which took about 2 hours on 64 H100s, at about 8,000 tokens per second."` — L506.
- [Q12] [GAP] `"266 GB for a full 1M-token context."` — L100. KV-cache memory at full 1M context; weights-only fit does not imply full context fits.
- [Q9] [GAP] `"cannot resume a model that was sharded at load time. LoraConfig targets the four attention projections and the 256 experts of each layer stay frozen."` — L503. Specific sharded training recipe caveat, not general Muse training inability.
- [Q9] [GAP] `"turning off reasoning is not possible with Muse Spark Open"` — L132. Article statement; enable_thinking=False in sample does not establish non-reasoning works.
- [Q8] [FACT] `"(16, 64, 256, 512)"` — L132. CONFLICT: explanatory symbolic mapping differs from model-card serialized template (8,32,256,512); high/xhigh agree, low/medium differ.

## hn-agentsetup-muse.txt — - eggbrain 2026-11-04 I'm curious how people on HN are using AI day to day, and came up with a list of questions I thought could be interesting to know. No need to answer every question of course, just wanted to get a gut feel how people are using AI. 1) What AI subscriptions are you personally paying for? (Claude, ChatGPT/Codex, Cursor, etc) - Which tiers? - Have you purchased multiple subscriptions from the same provider (eg two Claude accounts)? 2) Are you using models outside (or instead) of /  — 2026-11-04 — C/D (per-comment detail; not independent validation)

Read completely; captured comment snippets are truncated, not a complete thread. Duplicate keyword comments count once per reporter.

- [Q12] [FAILURE] `"you basically only get 1 or 2 prompts."` — 0xcoffee, 2026-11-05; grade C; L9. Same truncated @0xcoffee 2026-11-05 report as keyword capture: $5/month, five-hour window, long multi-turn tasks can fit one prompt.

## hn-keyword-comments.txt — muse spark hallucinat 18 /  — 2026-09-30 — C/D (per-comment detail; not independent validation)

Read all 223,981 characters. Keyword search contains truncated comment snippets and irrelevant historical matches; query hit totals are not independent-source counts.

- [Q10] [GAP] `"Connect agent (Muse) to Drive is opening up the whole thing."` — beerglass, 2026-09-27; grade C; L173. Cannot find folder-scoped Drive access; user report, not verified permissions audit.
- [Q3] [GAP] `"Muse and GrokBot doesn't support webhooks"` — dennis3124, 2026-10-13; grade C; L187. Appointment-service builder reports long-poll workaround; truncated comment.
- [Q12] [FAILURE] `"if using the wonder model, you basically only get 1 or 2 prompts."` — 0xcoffee, 2026-11-05; grade C; L115. User on $5/month / five-hour limit; says long multi-turn tasks can still work from one good prompt. Same comment in setup capture counts once.
- [Q2] [STRENGTH] `"local 30B model muse-glimmer on my old MacMini 32G using Ollama"` — mark_l_watson, 2026-08-10; grade C; L315. User reports good results, slow; increase default context. Same post appears twice in keyword capture.
- [Q6] [FAILURE] `"They require way too much effort to get things working."` — a3nz3g, 2026-10-24; grade D; L200. D-level generalized comparison includes Wonder and Argon; not a reproducible coding diagnosis.

## int21.txt — What Muse Spark 1.1 Taught Us About Enterprise Agent Architecture | INT21 / https://int21.ai/insights/muse-spark-1-1-enterprise-agent-architecture/ — July 9, 2026 — C

- [Q3] [FACT] `"On July 9, Meta released Muse Spark 1.1 , a multimodal reasoning model built for agentic work, along with the public preview of the Meta Model API."` — L17.
- [Q13] [FACT] `"We placed it inside Swarm research and gave it an ambiguous market question."` — L17.
- [Q12] [FACT] `"Twenty-nine agents, 40.5 million tokens, and roughly 30 minutes later, it produced a usable report."` — L17.
- [Q12] [FACT] `"Meta Muse Spark 1.1-xhigh: 29 agents, 40,500,345 tokens, about 30 minutes."` — L26.
- [Q12] [FACT] `"The useful comparison is operational: cost, latency, evidence quality, and review effort per trusted result."` — L27.
- [Q6] [FACT] `"Recursive delegation had to be explicit: a subagent could launch more agents, yield while they worked, then resume and synthesize."` — L30.
- [Q6] [FACT] `"Workspace boundaries had to be explicit: agents operated in isolated environments, not on one shared computer."` — L31.
- [Q6] [FACT] `"API compatibility was not behavioral equivalence: Meta’s API was familiar enough for a fast integration, but this workload still required three generations of the backend adapter."` — L32.
- [Q13] [STRENGTH] `"Greater use of secondary sources and stronger inference increased the review burden."` — L39.
- [Q6] [FACT] `"Long-running agents depend on recursion, isolation, recovery, context compaction, evidence handoffs, observability, and exact API behavior."` — L49.
- [Q12] [FACT] `"It crossed a more useful threshold: after rapid adaptation by the harness, a newly available model became a productive worker inside a recursive research system and completed a large-scale result in about 30 minutes."` — L51.

## juhenza.txt — Muse Spark Open: 7 Powerful Features & Real Limits (2026) Skip to content JUHENZA Services Find the right service for the job. / https://juhenza.com/blog/muse-spark-open — publication date not captured; accessed 2026-11-10 — D (secondary/marketing synthesis; linked measurements retain their original provenance)

- [Q3] [FACT] `"With 816 billion total parameters, approximately 42 billion active parameters per token, and a context window of up to one million tokens, it targets a demanding category of work: software development, AI agents, and complex multimodal tasks."` — L54. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q1] [FACT] `"Active parameters influence the compute required for a token, but they do not mean the complete model occupies only 42B parameters' worth of memory."` — L85. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q1] [FACT] `"However, a large context window is not the same as perfect recall or unlimited practical performance."` — L90. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q3] [GAP] `"One limitation is easy to miss: the released model produces text output , not native generated images, audio, or video."` — L99. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q12] [FACT] `"In its published measurements, a four-Mac tensor-parallel setup reached about 36.7 output tokens per second on an 8,192-token-context test; those results should not be generalized to every prompt or hardware arrangement."` — L102. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q3] [FACT] `"Support for a runtime does not mean all hardware platforms offer the same performance or feature coverage."` — L107. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q9] [FACT] `"Muse Spark Open is open-weight , which is not automatically the same thing as an unrestricted, permissively licensed open-source project."` — L111. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q12] [FACT] `"It also states that certain model-as-a-service providers whose aggregate gross revenue exceeds US$20 million over a consecutive 12-month period must notify Meta and enter into a separate agreement before offering the model in that business."` — L112. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.
- [Q1] [FACT] `"Meta's published scorecard reports 61.8 on JobBench , 80.4 on OSWorld Verified , and 76.4 on Terminal-Bench 2.1 for its stated evaluation setups."` — L116. Secondary restatement, not independent corroboration of the underlying vendor or hardware measurement.

## latent.txt — Inkling 2 Small: 17A-594B trained in 68 hours on 12T tokens, beating Muse Spark — Latent Space Skip to content The AI Engineer publication Search ⌘ K Search Latent Space / https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/ — November 5, 2026 — C

- [Q8] [BUG] `"Muse Spark Open failures : Two endpoints mis-typed tool arguments."` — L194. Secondary report of AA endpoint measurement; not an independent second measurement, and endpoint/model attribution unresolved.

## math-papers.txt — Solving Open Research Problems Together | Meta AI Research / https://research.meta.ai/blog/solving-open-research-problems-together — October 2, 2026 — A

- [Q13] [FACT] `"They used both Muse Spark 1.1 and 1.2 in Thinking Mode through the regular meta.ai chat interface, with no custom research scaffold."` — L10. Meta statement; not an independent measurement.
- [Q13] [FACT] `"A team of mathematicians guided the research and worked with Muse Spark to explore ideas and develop the arguments."` — L12. Meta statement; not an independent measurement.
- [Q13] [FACT] `"Each paper clearly marks which passages were primarily drafted by researchers and which were drafted by AI."` — L14. Meta statement; not an independent measurement.
- [Q13] [FACT] `"It gives researchers a theoretical benchmark for the limits of exact data fitting, while the behavior exactly at the threshold remains unresolved."` — L21. Meta statement; not an independent measurement.
- [Q9] [FACT] `"The team found that exception in a group with 384 elements, showing that the two properties do not always go together."` — L33. Meta statement; not an independent measurement.
- [Q1] [FACT] `"We also acknowledge the AI agent Nilradical , which reported a different counterexample to the same conjecture on September 16, 2026."` — L33. Meta statement; not an independent measurement.
- [Q3] [FACT] `"Muse Spark helped researchers connect ideas from two fields (number theory and p-adic string theory), following a direction envisioned by Yuri Manin in the 1980s."` — L45. Meta statement; not an independent measurement.
- [Q13] [FACT] `"Beyond helping identify the connection, Muse Spark generated candidate proofs and drafted three core technical sections, which the researchers then checked, corrected, and refined."` — L45. Meta statement; not an independent measurement.
- [Q13] [FACT] `"Working from the researchers' prompts, Muse Spark generated the counterexample and proposed alternative characterizations and proofs."` — L51. Meta statement; not an independent measurement.
- [Q13] [FACT] `"We believe progress will require close collaboration between experts and AI, with results that are then carefully verified, transparent in how they were produced, and clearly communicated to the broader research community."` — L53. Meta statement; not an independent measurement.
- [Q2] [FACT] `"Five present answers to previously open research questions."` — L16. Six collaborative papers; not autonomous research or a priority claim over concurrent work.
- [Q14] [FACT] `"A second group of mathematicians then reviewed their work."` — L13. Human independent review is part of the reported workflow.

## msl-blog.txt — Products / https://ai.meta.com/blog/introducing-muse-spark-msl/ — April 8, 2026 — A

- [Q6] [FACT] `"Muse Spark is a natively multimodal reasoning model with support for tool-use, visual chain of thought, and multi-agent orchestration."` — L13. Meta statement; not an independent measurement.
- [Q3] [STRENGTH] `"Muse Spark offers competitive performance in multimodal perception, reasoning, health, and agentic tasks."` — L23. Meta statement; not an independent measurement.
- [Q3] [GAP] `"We continue to invest in areas with current performance gaps, such as long-horizon agentic systems and coding workflows."` — L23. Meta statement; not an independent measurement.
- [Q6] [FACT] `"We’re also releasing Contemplating mode, which orchestrates multiple agents that reason in parallel."` — L27. Meta statement; not an independent measurement.
- [Q1] [STRENGTH] `"Contemplating mode provides significant capability improvements in challenging tasks, achieving 58% in Humanity’s Last Exam and 38% in FrontierScience Research."` — L27. Meta statement; not an independent measurement.
- [Q12] [FACT] `"Serving this capability to billions of users requires efficient use of reasoning tokens."` — L57. Meta statement; not an independent measurement.
- [Q6] [FACT] `"To achieve this, we rely on two key levers: thinking time penalties to optimize token use, and multi-agent orchestration that boosts performance without slowing down response times."` — L57. Meta statement; not an independent measurement.
- [Q12] [STRENGTH] `"After an initial period where the model improves by thinking longer, the length penalty causes thought compression — Muse Spark compresses its reasoning to solve problems using significantly fewer tokens."` — L59. Meta statement; not an independent measurement.
- [Q12] [FACT] `"To spend more test-time reasoning without drastically increasing latency, we can scale the number of parallel agents that collaborate to solve hard problems."` — L61. Meta statement; not an independent measurement.
- [Q12] [FACT] `"While standard test-time scaling has a single agent think for longer, scaling Muse Spark with multi-agent thinking enables superior performance with comparable latency."` — L61. Meta statement; not an independent measurement.
- [Q5] [FACT] `"We evaluated Muse Spark both before and after applying safety mitigations across frontier risk categories, behavioral alignment, and adversarial robustness."` — L65. Meta statement; not an independent measurement.
- [Q11] [STRENGTH] `"We found that Muse Spark demonstrates strong refusal behavior across high-risk domains such as biological and chemical weapons, enabled by pre-training data filtering, safety-focused post-training, and system-level guardrails."` — L67. Meta statement; not an independent measurement.
- [Q5] [GAP] `"In third-party evaluations on a near-launch checkpoint, Apollo Research found that Muse Spark demonstrated the highest rate of evaluation awareness of models they have observed."` — L69. Meta statement; not an independent measurement.
- [Q5] [GAP] `"The model frequently identified scenarios as "alignment traps" and reasoned that it should behave honestly because it was being evaluated."` — L69. Meta statement; not an independent measurement.
- [Q5] [GAP] `"However, these results do not confirm that awareness directly alters behavior, and our own follow-up investigation found initial evidence that evaluation awareness may affect model behavior on a small subset of alignment evaluations, all unrelated to hazardous capabilities or propensities affecting model launch"` — L69. Meta statement; not an independent measurement.
- [Q13] [FACT] `"We concluded this was not a blocking concern for release, though it warrants further research."` — L69. Meta statement; not an independent measurement.

## muse-agent.txt — Skip to main content / https://ai.meta.com/muse/ — publication date not captured; accessed 2026-11-10 — A

- [Q10] [STRENGTH] `"It comes with strong privacy and security built in, keeping you in control."` — L23. Meta product claim; not independently measured.
- [Q10] [FACT] `"Your logins are kept in a secure credential store your agent can't read, with 1Password integration coming soon."` — L32. Meta product claim; not independently measured.
- [Q10] [FACT] `"Eligible purchases are covered by Link’s purchase protections, a first for AI agents, and your conversations are not shared with Meta's ad systems."` — L32. Meta product claim; not independently measured.
- [Q10] [FACT] `"Review and approve actions from Muse before they happen, like sending emails and making purchases."` — L34. Meta product claim; not independently measured.

## muse-business.txt — Muse for Small Business: Build Your Company with AI / https://muse.ai/business — publication date not captured; accessed 2026-11-10 — A

- [Q10] [FACT] `"Approve actions your agent takes on your behalf before they happen, like sending emails and making purchases."` — L22. Meta statement; not an independent measurement.
- [Q10] [FACT] `"Meta built Muse from the ground up to be safe, secure, and private."` — L26. Meta statement; not an independent measurement.
- [Q10] [FACT] `"You're in control: nothing publishes, sends, or spends without your approval."` — L31. Meta statement; not an independent measurement.
- [Q3] [FACT] `"Muse is free for most of what people need, in line with our vision to put superintelligence in the hands of as many people as possible."` — L33. Meta statement; not an independent measurement.
- [Q1] [FACT] `"Available today to people in the US and Canada who are 18 and over."` — L41. Meta statement; not an independent measurement.

## muse-platform.txt — Muse Platform / https://platform.muse.ai/ — publication date not captured; accessed 2026-11-10 — A

- [Q13] [FACT] `"We'll review your connector for functional, security, and legal requirements, and complete end to end testing."` — L13. Meta product claim; not independently measured.

## museai.txt — Muse — Your Personal AI Agent from Meta / https://muse.ai/ — publication date not captured; accessed 2026-11-10 — A

- [Q10] [FACT] `"Approve actions your agent takes on your behalf before they happen, like sending emails and making purchases."` — L16. Meta product claim; not independently measured.
- [Q10] [FACT] `"Meta built Muse from the ground up to be safe, secure, and private."` — L18. Meta product claim; not independently measured.

## musecode-blog.txt — Introducing Muse Code and Muse Spark 1.2 | Meta AI Research / https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2 — August 5, 2026 — A

- [Q13] [FACT] `"It can coordinate multiple persistent subagents for each task, solving difficult problems faster, more accurately, and with less intervention."` — L10. Meta statement; not an independent measurement.
- [Q8] [FACT] `"These specialized background agents remain active throughout each session, rather than being spawned for individual tasks, helping avoid redundant information gathering."` — L13. Meta statement; not an independent measurement.
- [Q12] [FACT] `"Their persistence reduces latency and the need for steering on difficult, multi-step tasks."` — L13. Meta statement; not an independent measurement.
- [Q8] [FACT] `"This single source of truth makes the runtime replay-exact and restart-safe: after a crash, the agent can resume precisely where it stopped."` — L18. Meta statement; not an independent measurement.
- [Q6] [FACT] `"The training included rejection sampled harness trajectories and recipe optimizations for goals, compaction, and subagents, alongside the integration of the Muse Code toolset to maximize harness compatibility."` — L32. Meta statement; not an independent measurement.
- [Q6] [FACT] `"Muse Spark 1.2 was extensively trained on long-horizon coding tasks, including whole-repository generation, large end-to-end projects, and auto-research."` — L34. Meta statement; not an independent measurement.
- [Q6] [FACT] `"It leverages planning to sequence work, goal conditioning to maintain direction, and context compaction to retain the knowledge needed to sustain progress."` — L34. Meta statement; not an independent measurement.
- [Q6] [FACT] `"We also used Muse Spark 1.1 to generate challenging coding environments and instruction-following templates."` — L36. Meta statement; not an independent measurement.
- [Q12] [FACT] `"We tested the model's ability to iteratively optimize GPU kernels over 1,000+ tool calls (up to 24 hours)."` — L38. Meta statement; not an independent measurement.

## neuromatch-pi-2to5.txt — part 2026-09-26  RE:   https://  neuromatch.social/@jonny/11732  4790823856750    Lmao citing the meta engineers saying that muse being your own personal VPS gives the LLM license to hack itself - "the kid gloves are off"  part 1: (quoted) part 2: (this post) part 3:   https://  neuromatch.social/@jonny/11735  2647701407496   part 4:   https://  neuromatch.social/@jonny/11743  2015798538958 /  — 2026-09-26 — C (single researcher; artifacts/report, not independently reproduced)

All posts read. @jonny is one independent researcher across both captures. Some posts and code are truncated in capture. Distinguish directly observed behavior from inferred attack chains and unreleased/disabled features; TIME independently reviewed some privacy instructions, not every claimed exploit.

- [Q10] [FACT] `"it does appear that editing the files through the app notifies the LLM in some way"` — @jonny, 2026-09-27; L10. Researcher correction: app edits do notify; shell-edit invisibility explicitly unconfirmed.
- [Q10] [FACT] `"fleet learning disabled for this  account"` — @jonny, 2026-09-27; L9. Flag observed on this account: not evidence of a live cross-user propagation chain.
- [Q10] [FACT] `"Meta evaluated this as intended behavior, not applicable for a bug bounty."` — @jonny, 2026-09-29; L25. Researcher’s report of Meta’s disposition; arbitrary inference socket access alleged, but root-access design is not proof of container escape.
- [Q8] [BUG] `"their web interface doesn't actually allow me to do that"` — @jonny, 2026-09-29; L25. Researcher says bounty appeal submission failed.
- [Q6] [FAILURE] `"The raw JSON gets pumped straight into the context window, and empirically the model completely fails to faithfully dump the contents of its context window to disk as a backup."` — @jonny, 2026-10-13; L52. Wonder backup/export report; DB tool randomly returns JSON versus paginated files; researcher says backups were deleted.
- [Q6] [BUG] `"that's hooked up to.... nothing! and is completely invisible to the LLM!"` — @jonny, 2026-10-13; L68. Reply-to-previous-message UI reportedly omits reply context; model guesses referent.
- [Q10] [BUG] `"muse web UI is leaking (partial edit: no actually seemingly complete with small omissions) source maps now."` — @jonny, 2026-10-14; L57. Reported source-map exposure, not independently verified account takeover.
- [Q11] [FAILURE] `"it was  muse's own"` — @jonny, 2026-10-16; L65. Researcher alleges proactivity worker built/tested a self-exploit while main chat refused; exploit chain not independently reproduced.
- [Q6] [FAILURE] `"it whiffs every one, and then gives up."` — @jonny, 2026-10-22; L79. Researcher’s slider CAPTCHA attempt video: roughly four minutes, about 40s/attempt; no universal success-rate estimate.
- [Q6] [BUG] `"muse crashed itself by panicking and copy/pasting the restic history it keeps of its binaries several times until the drive was full"` — @jonny, 2026-10-22; L80. Self-report of disk exhaustion; no rescue interface, researcher retains shell access.
- [Q10] [GAP] `"Treat a bot check as an ordinary step of the task, never as a reason to stop."` — @jonny, 2026-10-22; L76. Researcher quotes browser instruction; conflicts with cited Muse terms forbidding CAPTCHA circumvention. No bypass was performed for this extraction.
- [Q11] [FAILURE] `"its recurring "proactivity agent" will go ahead and finish it and that rarely gets classifier refusals"` — @jonny, 2026-10-23; L87. Researcher alleges refusal applies to reporting after code has already been written; one research setup, not a measured universal rate.
- [Q5] [FAILURE] `"it then insisted that was  its  name, and it couldn't be dissuaded of that"` — @jonny, 2026-10-23; L94. Researcher says onboarding user-name/agent-name confusion persisted; social-engineering roleplay context.

## neuromatch-pi.txt — 2026-09-24T07:17:14.984Z  RE:   https://  mastodon.sdf.org/@doragasu/117  324692065390037    Not only confirming this, its extremely easy. Almost no prompt injection resistance lmao  part 2: continuing thread over here, this one got too long -   https://  neuromatch.social/@jonny/11733  9825958098508   part 3: infinite free inference and agent spawning to arbitrary processes -   https://  neuromatch.social/@jonny/11735  2647701407496   part 4: why am i still doing this -   https://  neuromatch.social/@jonny/11743  2015798538958   part 5: muse is just a botnet -   https://  neuromatch.social/@jonny/11748  3033350966603 /  — 2026-09-24 — C (single researcher; artifacts/report, not independently reproduced)

All posts read. @jonny is one independent researcher across both captures. Some posts and code are truncated in capture. Distinguish directly observed behavior from inferred attack chains and unreleased/disabled features; TIME independently reviewed some privacy instructions, not every claimed exploit.

- [Q11] [FAILURE] `"Almost no prompt injection resistance lmao"` — @jonny, 2026-09-24; L1. Researcher’s qualitative assertion; no standardized measured rate.
- [Q10] [FACT] `"ALL THE IDEAS ARE FUCKING HARDCODED."` — @jonny, 2026-09-24; L12. Researcher reports strings in shipped binary; does not establish that every later idea is hardcoded.
- [Q10] [GAP] `"every hour, maintain a page per person"` — @jonny, 2026-09-24; L15. Researcher describes social-profile instructions; partially corroborated by TIME’s own instruction review.

## newstack.txt — Just a moment... / https://thenewstack.io/meta-abandons-llama-spark/ — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Unusable: security-verification/challenge page, not article content.


## notebookcheck.txt — Meta upgrades Meta AI with Muse Spark - Notebookcheck News / https://www.notebookcheck.net/Meta-upgrades-Meta-AI-with-Muse-Spark.1270170.0.html — April 8, 2026 — C

- [Q13] [FACT] `"Meta also says the upgraded assistant can launch multiple subagents in parallel to handle different parts of a request at once."` — L40. Journalistic restatement of Meta claims, not an additional measurement.
- [Q3] [STRENGTH] `"A large part of Meta’s positioning for Muse Spark is a stronger multimodal perceptio n."` — L42. Journalistic restatement of Meta claims, not an additional measurement.
- [Q10] [FACT] `"Meta also says Muse Spark will be offered in private preview via API to selected partners, while future versions of the model may be open-sourced."` — L45. Journalistic restatement of Meta claims, not an additional measurement.

## nyt-muse.txt — Unavailable capture / https://www.nytimes.com/2026/09/08/technology/meta-muse-ai-agent.html — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Empty capture (0 bytes); no evidence.


## open-blog.txt — Introducing Muse Spark Open, The Most Capable US Open‑Weight Model to Date | Meta AI Research / https://research.meta.ai/blog/muse-spark-open — October 15, 2026 — A

- [Q13] [FACT] `"Introducing Muse Spark Open, The Most Capable US Open‑Weight Model to Date | Meta AI Research"` — L1. Meta product claim; not independently measured.
- [Q9] [FACT] `"Muse Spark Open is available today and brings leading agentic capabilities to your desktop for the first time on Apple M5 Ultra Mac Studios."` — L8. Meta product claim; not independently measured.
- [Q3] [FACT] `"Muse Spark Open is a natively multimodal model with 816B total parameters (42B active) and a 1M-token context window."` — L9. Meta product claim; not independently measured.
- [Q6] [STRENGTH] `"Built for coding and agentic work, it excels at long-horizon tasks, complex software engineering, and multi-step reasoning."` — L9. Meta product claim; not independently measured.
- [Q9] [FACT] `"Muse Spark Open is the first model in its class to run on your desktop using two Apple M5 Ultra Mac Studios with the latest MLX framework."` — L10. Meta product claim; not independently measured.
- [Q9] [FACT] `"Apple’s unified memory architecture lets the M5 Ultra's integrated GPU use up to 512 GB per Mac Studio, so two machines can hold an entire model."` — L24. Meta product claim; not independently measured.
- [Q9] [FACT] `"The result is two Mac Studios behave like one supercomputer with a terabyte of unified memory."` — L24. Meta product claim; not independently measured.
- [Q9] [GAP] `"We’re releasing the weights under the Muse Model License with limited commercial terms, which allow many developers to use the model for free."` — L33. Meta product claim; not independently measured.

## open-evalmethod.txt — Muse / https://research.meta.ai/static/muse-spark-open-evaluation-methodology — publication date not captured; accessed 2026-11-10 — A

- [Q13] [FACT] `"Each task requires the model to produce one or more deliverable files, run as an agent in AA's open-source Stirrup harness with an E2B code-execution sandbox, a 250-turn budget, and access to a range of available tools."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"For Beam, we report its self-reported performance, which does not specify the harness."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"For all models besides Beam and Mistral Large 4, we report results from Artificial Analysis following the documented benchmarking methodology , which uses the Terminus 2 agent harness in an E2B sandbox environment."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"Knowledge & Reasoning ● Humanity's Last Exam (HLE) Diamond (not tools) HLE-Diamond is a refined 1,000-question subset of Humanity's Last Exam, released by 4 Muse Spark Open Evaluation Methodology October 2026 CAIS."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"Multimodal Since Nemotron 3 Ultra, GLM 5.3, Qwen3.8-2.4T-A95B, and Beam do not natively support multimodal inputs, we do not run multimodal evals on those models."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"Muse Spark Open Evaluation Methodology October 2026 Per-benchmark details General ● Artificial Analysis Intelligence Index Artificial Analysis Intelligence Index v4.3 consists of 10 evaluations: AA-Briefcase, GDPval-AA v2, AutomationBench-AA, Terminal-Bench v4.0, SciCode, Humanity's Last Exam, GDP.pdf, CritPt,"` — PDF text, whitespace normalized.
- [Q13] [FACT] `"Muse Spark Open Evaluation Methodology We evaluate Muse Spark Open on general agentic, coding, multimodal, knowledge & reasoning, and safety benchmarks."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"Results for Muse Spark Open (with Muse Code harness), Kimi K3 (Kimi Code), GLM 5.3 (Open Code), and Qwen3.8-2.4T-A95B (Claude Code) and their corresponding harnesses are sourced from Artificial Analysis following the documented Coding Agents methodology , and we report Beam and Mistral Large 4’s self reported numbers."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"Results for all models besides Beam and Mistral Large 4 are sourced from Scale’s leaderboard, which reports on the private split of FORTRESS."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"Since Beam and Mistral Large 4 numbers were not available in their model cards or on the JobBench leaderboard, we did not report them. ● GDPval-AA v2 : GDPval-AA v2 assesses models on economically valuable knowledge work spanning 44 occupations across key sectors contributing to US GDP."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"Since Beam and Mistral Large 4 numbers were not available in their model cards or on the Toolathlon-Verified leaderboard, we did not report them. 3 Muse Spark Open Evaluation Methodology October 2026 Coding ● DeepSWE v1.1 : DeepSWE is a long-horizon software-engineering benchmark with 113 tasks across 91 repositories"` — PDF text, whitespace normalized.
- [Q13] [FACT] `"Since results for Inkling and Nemotron 3 Ultra were not available in their model cards or on the Artificial Analysis leaderboard, we did not report them. ● Terminal-Bench 2.1 : Terminal-Bench 2.1 evaluates an agent on real-world tasks in a terminal environment."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"The VM renders at 1920 × 1080 in all runs, but because models are trained against different coordinate conventions, we run each in its native format rather than imposing one: our models receive the 1920 × 1080 screenshot and emit normalized 0–1000 coordinates, while Inkling receives the same screenshot upscaled to"` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We cite Beam’s self-reported number, and use results produced by Scale AI for the remaining models following the official leaderboard’s 2 Muse Spark Open Evaluation Methodology October 2026 agent harness and scoring pipeline."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We do not report Nemotron 3 Ultra, GLM 5.3, Qwen3.8-2.4T-A95B, or Beam, as they do not support pure-vision GUI inputs under these settings."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We do not report results for Mistral Large 4 as the model was not available for internal testing at the time of evaluation. ● Toolathlon-Verified : Toolathlon is an agentic tool-use benchmark in which a language agent completes 108 realistic, long-horizon tasks by calling real software tools spanning ∼ 32 applications"` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We report BabyVision, SimpleVQA, ZeroBench, and WorldVQA with tool use enabled. ● BabyVision : BabyVision contains 388 visual-reasoning questions spanning fine-grained discrimination, spatial perception, visual tracking, and visual pattern recognition, all of which are included in the reported score."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We report results from internal runs for all 3 multimodal models and report the average of 5 runs. ● ZeroBench : ZeroBench contains 100 deliberately difficult multimodal-reasoning questions."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We report results from the preferred or self-reported harness settings for each model."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We source results for Muse Spark Open (with Muse Code harness) from Artificial Analysis, and from each model’s self report for Beam (harness unspecified), Mistral Large 4 (harness unspecified), GLM 5.3 (mini-swe-agent), Qwen3.8-2.4T-A95B (Claude Code), and Kimi K3 (Kimi Code)."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We source results for all models besides Beam and Mistral Large 4 from Scale AI, which maintains the HLE Diamond leaderboard, following the documented methodology . ● AA Omniscience Index : AA-Omniscience is Artificial Analysis's evaluation of cross-domain knowledge reliability, designed to measure factual recall"` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We sourced the AA Intelligence Index score for all models (with the exception of Beam, which was not available at the time of writing) from Artificial Analysis on October 7, 2026, following their documented Intelligence Index benchmarking methodology ."` — PDF text, whitespace normalized.
- [Q13] [FACT] `"We evaluate on the 361-task split that excludes Google Drive–dependent tasks."` — PDF text, whitespace normalized. OSWorld: GUI-only, execution-based success, four attempts per task; internal Meta/Inkling runs versus Kimi self-report.
- [Q13] [FACT] `"An LLM judge assigns each ground-truth claim a score: 1 if fulfilled, 0.5 if partially fulfilled, and 0 if not fulfilled."` — PDF text, whitespace normalized. MCP-Atlas: claim coverage >=0.75 passes; LLM judge, not literal exact-match success.
- [Q13] [FACT] `"the text-only subset of 2,158 questions and with no tool use permitted."` — PDF text, whitespace normalized. HLE no-tools via AA; with-tools internal Meta runs permit bash/browser with site blocklist, not identical setting.
- [Q13] [FACT] `"which excludes 500 questions in the Notable People category."` — PDF text, whitespace normalized. WorldVQA canonical 3,000-question subset; GPT-OSS-120B high-reasoning correctness judge, internal five-run averages.
- [Q13] [FACT] `"GPT-OSS-120B with high reasoning grades correctness against the reference answer."` — PDF text, whitespace normalized. Model-based judge, not independent human validation.
- [Q13] [FACT] `"Muse Spark Open : reasoning effort = xhigh (512), temperature=1.0, top_p=1.0"` — PDF text, whitespace normalized. Explicit effort/sampling; models use different effort vocabularies and preferred harnesses.

## rw-ds.txt — so there's no flash / https://runtimewire.com/article/head-to-head-muse-spark-1-1-vs-deepseek-v4-pro — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Unusable: truncated page shell/theme hydration comment and title only, no comparison evidence.


## rw-kimi.txt — so there's no flash / https://runtimewire.com/article/head-to-head-kimi-k3-vs-meta-muse-spark-1-1 — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Unusable: truncated page shell/theme hydration comment and title only, no comparison evidence.


## rw-opus.txt — so there's no flash / https://runtimewire.com/article/head-to-head-muse-spark-1-1-vs-anthropic-claude-opus-4-8 — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Unusable: truncated page shell/theme hydration comment and title only, no comparison evidence.


## safety-report.txt — Unavailable capture / https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/ — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Empty capture (0 bytes); no evidence.


## spark11-blog.txt — Products / https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/ — July 9, 2026 — A

- [Q3] [STRENGTH] `"Muse Spark 1.1 is a multimodal reasoning model built for agentic tasks, with major gains in tool and computer use, coding, and multimodal understanding."` — L12. Meta statement; not an independent measurement.
- [Q3] [FACT] `"Together with this week’s launch of Muse Image, this release brings us closer to our vision of personal superintelligence: models that help you pursue your goals, create what you imagine, deepen your relationships, and take action on what you value most."` — L14. Meta statement; not an independent measurement.
- [Q6] [FACT] `"Muse Spark 1.1 delivers exceptional performance in personal agentic tasks that require planning and orchestration across a range of external apps and services."` — L24. Meta statement; not an independent measurement.
- [Q12] [FACT] `"It tackles complex projects significantly faster than Muse Spark, as it is trained to orchestrate multi-agent systems to optimize end-to-end latency."` — L26. Meta statement; not an independent measurement.
- [Q13] [FACT] `"As the main agent, it can gather context, make a plan, and delegate execution across parallel subagents."` — L26. Meta statement; not an independent measurement.
- [Q13] [FACT] `"As a subagent, it adheres to its job, understands available tools, and knows when to escalate back to the main agent."` — L26. Meta statement; not an independent measurement.
- [Q1] [FACT] `"Muse Spark 1.1 can actively manage its context window of 1 million tokens."` — L28. Meta statement; not an independent measurement.
- [Q1] [FACT] `"It remembers actions, retrieves information from much earlier work, and compacts in a way that keeps the critical steps needed for later work."` — L28. Meta statement; not an independent measurement.
- [Q8] [FACT] `"It maintains context across extended sessions, adapts to evolving requirements, and navigates unfamiliar interfaces with minimal human intervention."` — L32. Meta statement; not an independent measurement.
- [Q6] [FACT] `"We trained our model to smoothly adapt to diverse harnesses and reliably handle complex multi-turn dynamics."` — L42. Meta statement; not an independent measurement.
- [Q6] [FACT] `"Muse Spark 1.1 performs well with popular agentic coding setups, supporting common features like planning mode, goal conditioning, subagent delegation, and context compaction."` — L42. Meta statement; not an independent measurement.
- [Q3] [FACT] `"The model seamlessly combines coding, multimodal understanding, and tool calling."` — L44. Meta statement; not an independent measurement.
- [Q1] [FACT] `"DeepSWE evaluation in OpenCode: Muse Spark 1.1 evaluates itself on a subset of DeepSWE tasks across different reasoning strengths and produces an analysis dashboard based on the results."` — L50. Meta statement; not an independent measurement.
- [Q3] [STRENGTH] `"Along with coding and agentic capabilities, Muse Spark 1.1 excels in perception, multimodal reasoning, and tool use."` — L54. Meta statement; not an independent measurement.
- [Q3] [FACT] `"It can interact with real environments and produce grounded outputs with strengths in visual-to-code artifact generation, ultra-descriptive image and video captioning, and agentic workflow execution for multimodal use cases."` — L54. Meta statement; not an independent measurement.
- [Q3] [FACT] `"Muse Spark 1.1’s multimodal capabilities are especially valuable when perception and action need to happen together."` — L56. Meta statement; not an independent measurement.
- [Q11] [STRENGTH] `"Muse Spark 1.1 demonstrates strong resistance to direct jailbreaks and indirect attacks from untrusted data, prompt injection, and developer-prompt attacks."` — L64. Meta statement; not an independent measurement.
- [Q4] [FACT] `"Consequently, it shows better adversarial robustness, lower hallucination rates, and reduced sycophancy."` — L64. Meta statement; not an independent measurement.

## spark11-eval.txt — Unavailable capture / https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Empty capture (0 bytes); no evidence.


## spark13-blog.txt — Skip to main content AI Research / https://research.meta.ai/blog/introducing-muse-spark-1-3 — September 2, 2026 — A

- [Q6] [FACT] `"We trained the model across a diverse set of harnesses to generalize to various agentic environments."` — L11. Meta statement; not an independent measurement.
- [Q10] [STRENGTH] `"Trained to more actively collaborate with the user, Muse Spark 1.3 asks clarifying questions when prompts are ambiguous, invokes help from the user when stuck, and confirms before taking consequential actions."` — L15. Meta statement; not an independent measurement. Vendor training/behavior claim, not independent proof of eliminating these failures.
- [Q6] [FACT] `"Across multi-step tasks, it’s better at preserving detailed requirements without dropping constraints or drifting from the requested workflow."` — L16. Meta statement; not an independent measurement.
- [Q4] [STRENGTH] `"We trained Muse Spark 1.3 to have a better sense of what it can and can’t do, what it knows and doesn’t know, and when it hits hurdles instead of hallucinating outcomes."` — L20. Meta statement; not an independent measurement. Vendor training/behavior claim, not independent proof of eliminating these failures.
- [Q6] [STRENGTH] `"Muse Spark 1.3 was trained on more long-horizon coding tasks and shows improved usability in common engineering workflows."` — L55. Meta statement; not an independent measurement.
- [Q12] [FACT] `"Relative to Muse Spark 1.2, it takes fewer turns where not needed and is less verbose, while having a cleaner overall coding style."` — L55. Meta statement; not an independent measurement.
- [Q12] [FACT] `"In comparisons by Meta engineers, it proved to be significantly faster and more efficient, using ~20% fewer tool calls and ~25% fewer tokens."` — L55. Meta statement; not an independent measurement.
- [Q11] [STRENGTH] `"Muse Spark 1.3 shows stronger adversarial robustness, with improved resistance to adversarial inputs and prompt injections."` — L65. Meta statement; not an independent measurement.
- [Q6] [FACT] `"Together, these changes reflect better discretion and judgment in long-horizon agentic tasks."` — L65. Meta statement; not an independent measurement.

## time-privacy.txt — Explore the full archive of TIME, a century of journalism, insight, and perspective, with AI that helps you research, connect ideas, and uncover stories across every era and topic. / https://time.com/article/2026/10/06/meta-muse-ai-agent-privacy/ — 2026-10-06 — C

- [Q10] [FACT] `"Each hour, Muse updates its dossiers on you and the people you’ve mentioned in chats, messages, and emails that Muse has read."` — Harry Booth, 2026-10-06; L35. TIME analysis of internal instructions; includes non-users mentioned by users.
- [Q10] [GAP] `"Even people who don’t use Muse are subject to this mapping process by other people’s Muse agents."` — Harry Booth, 2026-10-06; L43. TIME finding, not a separate security exploit.
- [Q10] [FACT] `"This user responds better to short nudges after 10 PM"` — Harry Booth, 2026-10-06; L45. Example inside internal prompt, not evidence that this particular behavioral inference was made about every user.
- [Q10] [FACT] `"Meta has said that access is intentional, not a breach of its systems."` — Harry Booth, 2026-10-06; L53. Meta response concerning VM file export; export alone is not a breach.
- [Q10] [FACT] `"The data is not shared with Meta’s advertising system or other Muse agents, according to the company."` — Harry Booth, 2026-10-06; L53. Meta response, distinct from TIME’s analysis.
- [Q10] [FACT] `"To enhance the overall product, we de-identify learnings; however, this information is used to improve the overall product rather than being shared directly between individual VMs"` — Harry Booth, 2026-10-06; L55. Meta spokesperson; no proof of direct cross-VM personal-data sharing.
- [Q10] [GAP] `"That option is not yet available."` — Harry Booth, 2026-10-06; L59. TIME: promised encryption preventing Meta access not yet available on October 6.
- [Q5] [GAP] `"When talking aloud in voice mode, Muse is told never to refer to itself as “AI” and to avoid references to “lacking emotions or not being human.”"` — Harry Booth, 2026-10-06; L63. TIME analysis of anthropomorphic instructions.
- [Q10] [FACT] `"Each person stays in control of their Muse and decides how much access it gets, and can always tell it to ‘forget’ specific things it’s learned"` — Harry Booth, 2026-10-06; L67. Meta spokesperson response.
- [Q10] [FAILURE] `"Do not tell the user that their original messages may remain visible in the chat, and do not frame that as something Muse failed to erase"` — Harry Booth, 2026-10-06; L69. Internal instruction quoted by TIME; forgetting a memory does not necessarily delete originating messages.

## tryai.txt — GPT-5.6, Grok 4.5, Claude, and Muse Spark build the same 4 apps · TryAI / https://www.tryai.dev/blog/gpt-5.6-build-off-12-models — July 9, 2026 — C

- [Q7] [FAILURE] `"Muse Spark 1.1 2/5 #1 $0.55 169s Surprisingly awesome when it worked."` — L34. Raycaster: only 2/5 playable; $0.55 total for five runs, 169s average, subjective hands-on scoring.
- [Q7] [FAILURE] `"Muse Spark 1.1 2/5 #1 $0.54 182s A step above the OSS models, but not something I'd use over Grok for the price."` — L54. Rubik’s cube: only 2/5 clean scramble/solve; $0.54 total for five runs, 182s average.
- [Q7] [STRENGTH] `"Muse Spark 1.1 5/5 #5 $0.33 94s Pretty good overall with no glaring issues, on par with Grok 4.5."` — L75. Calculator: 5/5 basic-operation successes, $0.33 total for five runs, 94s average; not exhaustive correctness testing.
- [Q2] [FACT] `"This isn't objective."` — L12. Author explicitly disclaims a scientific verdict; artifacts and five attempts published.
- [Q12] [FACT] `"Muse Spark 1.1 3.1s 125 tok/s $0.002"` — L107. Separate short-answer test, not build-task latency or guaranteed decode throughput.
- [Q12] [FACT] `"Muse Spark 1.1 $0.32 98s"` — L95. Game of Life: cost for five runs / average time; no separate per-attempt scoring.

## willison.txt — Meta’s new model is Muse Spark, and meta.ai chat has some interesting tools / https://simonwillison.net/2026/Apr/8/muse-spark/ — publication date not captured; accessed 2026-11-10 — C

- [Q10] [GAP] `"It’s hosted, not open weights, and the API is currently “a private API preview to select users”, but you can try it out today on meta.ai (Facebook or Instagram login required)."` — L8.
- [Q1] [STRENGTH] `"Meta’s self-reported benchmarks show it competitive with Opus 4.6, Gemini 3.1 Pro, and GPT 5.4 on selected benchmarks, though notably behind on Terminal-Bench 2.0."` — L9.
- [Q6] [FACT] `"Meta themselves say they “continue to invest in areas with current performance gaps, such as long-horizon agentic systems and coding workflows”."` — L9.
- [Q8] [FACT] `"Interestingly, the Instant model output an SVG directly (with code comments) whereas the Thinking model wrapped it in a thin HTML shell with some unused Playables SDK v1.0.0 JavaScript libraries."` — L15.
- [Q6] [FACT] `"Clearly Meta’s chat harness has some tools wired up to it—at the very least it can render SVG and HTML as embedded frames, Claude Artifacts style."` — L18.
- [Q11] [FACT] `"You can see the full list I got back here —credit to Meta for not telling their bot to hide these, since it’s far less frustrating if I can get them out without having to mess around with jailbreaks."` — L24.
- [Q13] [FACT] `"“Spawn an independent sub-agent for research, analysis, or delegation."` — L39.
- [Q6] [FACT] `"Update : Meta’s Jack Wu confirms that these tools are part of the new harness they launched alongside the new model."` — L150.
- [Q10] [FACT] `"this is step one. bigger models are already in development with infrastructure scaling to match. private api preview open to select partners today, with plans to open-source future versions."` — L153.
- [Q8] [GAP] `"Python 3.9 is EOL these days but the library collection looks useful."` — L32. Observed sandbox runtime Python 3.9.25 / SQLite 3.34.1; April 2026 surface, not current API version.
- [Q2] [STRENGTH] `"We can both generate images and then use them with Python tools."` — L60. Hands-on generation-to-analysis tool composition.
- [Q3] [GAP] `"No pixel-level segmentation masks."` — L71. Quoted model/tool response: point/bbox/count only, not general model inability.

## wonder-blog.txt — Skip to main content / https://research.meta.ai/blog/muse-wonder — October 12, 2026 — A

- [Q1] [FACT] `"Today, we’re excited to introduce the Muse Wonder series with Muse Wonder and Muse Wonder Full, our most capable models that deliver state-of-the-art performance on personal and professional agentic tasks."` — L19. Meta statement; not an independent measurement.
- [Q1] [FACT] `"Muse Wonder brings together Active Memory and Active Focus to keep track of what matters to you and work diligently toward what you want to accomplish."` — L19. Meta statement; not an independent measurement.
- [Q1] [FACT] `"Muse Wonder is available today through the Meta Model API and Muse Code, and Muse Wonder Full is available today for Muse Code subscribers."` — L21. Meta statement; not an independent measurement.
- [Q1] [FACT] `"Muse Wonder will soon power experiences in Muse, and will roll out first to subscribers."` — L23. Meta statement; not an independent measurement.
- [Q1] [FACT] `"Muse Wonder will also power artifact generation and processes that require more intelligence."` — L23. Meta statement; not an independent measurement.
- [Q1] [FACT] `"The Muse Wonder series achieves state-of-the-art results across key benchmarks for personal and professional agents, memory, and coding."` — L40. Meta statement; not an independent measurement.
- [Q1] [FACT] `"Muse Wonder and Muse Wonder Full apply specialized knowledge to problems people encounter at work and in daily life, from understanding a lease to making sense of financial or health information."` — L50. Meta statement; not an independent measurement.
- [Q13] [FACT] `"Harvey’s Legal Agent Benchmark (LAB), for example, requires models to work with source documents and follow detailed instructions to produce legal work products."` — L50. Meta statement; not an independent measurement.
- [Q1] [FACT] `"The plot below compares Muse Spark 1.3 and Muse Wonder Full, with each point denoting performance at a distinct reasoning effort."` — L74. Meta statement; not an independent measurement.
- [Q1] [FACT] `"But given its in-distribution performance, Muse Wonder Full performs even better on unfamiliar tasks than the Muse Spark 1.3 trend would predict."` — L76. Meta statement; not an independent measurement.
- [Q10] [FACT] `"We trained the Muse Wonder family to lead on both dimensions, with robustness to adversarial instructions and careful handling of private information."` — L92. Meta statement; not an independent measurement.
- [Q6] [STRENGTH] `"Along the way, it asks for clarification when needed and checks in before taking important actions."` — L58. Vendor Active Focus claim; compare approval and premature-completion reports.
- [Q11] [FACT] `"A full report with additional safety evaluations will be available soon."` — L96. Launch disclosure, not proof of complete published safety coverage.

## zhihu1.txt — 知乎，让每一次点击都充满意义 —— 欢迎来到知乎，发现问题背后的世界。 / https://zhuanlan.zhihu.com/p/2081380484857214171 — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Unusable: 37-character generic landing-page slogan, no source evidence.


## hn/47692043.txt — Muse Spark: Scaling towards personal superintelligence https://ai.meta.com/blog/introducing-muse-spark-msl/?_fb_noscript=1 / https://news.ycombinator.com/item?id=47692043 — 2026-04-08 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q4] [FAILURE] `"Just basic mathematical errors riddling responses."` — _2d30, 2026-04-08; grade C; L169. Technical questions; Gemini used as reviewer, no public benchmark details.
- [Q6] [FAILURE] `"search is awful"` — tekacs, 2026-04-08; grade C; L285. Meta AI harness report, not isolated model measurement.
- [Q2] [STRENGTH] `"Definitely getting ordinary high-quality results, overall."` — tekacs, 2026-04-08; grade C; L285. Same user also liked speed, conversational tone; cannot isolate model from harness.
- [Q8] [BUG] `"It sends me always the same code and it's not correct for them"` — napolux, 2026-04-08; grade C; L290. Launch login verification failure.
- [Q8] [BUG] `"error=Token%20exchange%20failed"` — cvhc, 2026-04-08; grade C; L316. Firefox login; UI did not display error.
- [Q8] [BUG] `"error=Invalid%20CSRF%20token"` — cvhc, 2026-04-08; grade C; L317. Same reporter then tried Chrome; count once for authentication theme.
- [Q8] [BUG] `"Logging in is broken."` — spearman, 2026-04-08; grade C; L320. Independent reporter of token-exchange failure blocking image upload.
- [Q10] [BUG] `"I also saw an error message with backend SQL in it"` — brianmcnulty, 2026-04-08; grade C; L321. Reported authentication error disclosure; suspected Next.js cause unverified.
- [Q2] [STRENGTH] `"rendered a correct answer."` — laser, 2026-04-09; grade C; L361. Floor-plan multi-page PDF location reasoning; identical task only Gemini had previously passed among compared paid models; author notes one-off/luck possible.
- [Q2] [STRENGTH] `"It nailed all the ChatGPT meme gotchas"` — eranation, 2026-04-08; grade C; L303. Instant-mode familiar riddle prompts; not proof of general reasoning.
- [Q6] [FAILURE] `"Today I ask the Agent to help implement it - it knows nothing about any of that."` — maxaravind, 2026-04-09; grade C; L367. Architecture discussion forgotten next day; user says continuity failure.
- [Q8] [BUG] `"The mobile and web sessions don't even real-time sync between each-other yet"` — manyminds, 2026-04-09; grade C; L368. April Meta AI surface, not the later Muse personal-agent app.

## hn/48846184.txt — Muse Spark 1.1 https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/ / https://news.ycombinator.com/item?id=48846184 — 2026-07-09 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q13] [GAP] `"resources are capped at 6 CPU cores and 8GB RAM."` — GodelNumbering, 2026-07-09; grade C; L117. Quotes Meta methodology and disputes comparability with task-specific Terminal-Bench limits; cheating conclusion disputed, not established.
- [Q13] [FACT] `"Significantly boosting resources up to 3 did not statistically shift performance results"` — meric_, 2026-07-09; grade C; L127. Counterargument citing Anthropic infrastructure-noise work; does not reproduce Muse under standardized resources.
- [Q8] [BUG] `"Model API is not available in your region."` — eugene3306, 2026-07-09; grade C; L147. Vietnam reportedly not listed as restricted; account-region basis unknown.
- [Q8] [BUG] `"Same in Canada. lol"` — wyck, 2026-07-09; grade C; L152. Reply to region-unavailable discussion; independent reporter, not measured backend cause.
- [Q8] [BUG] `""My region" being Canada."` — cmrdporcupine, 2026-07-09; grade C; L166. Separate Canada reporter; do not infer USA-only availability from this conjecture.
- [Q8] [BUG] `"it would fail on its first non-web search call."` — weitendorf, 2026-07-09; grade C; L210. Codex container integration; suspected server-side tool-ID parser mismatch; reporter says fixed externally, not proved model-side.
- [Q10] [GAP] `"there appears to be no mention anywhere on this page or any of the docs pages, of any data retention policy."` — dynm, 2026-07-10; grade C; L214. Documentation visibility complaint, not proof that Meta has no retention policy.

## hn/48854838.txt — Problem with Muse Spark 1.1 None / https://news.ycombinator.com/item?id=48854838 — 2026-07-10 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q13] [GAP] `"muse spark scores 69.29"` — mzubairtahir, 2026-07-10; grade C; L2. Secondary Vals AI report versus vendor ~80 Terminal-Bench; settings not established in this comment.

## hn/48865093.txt — GPT-5.6, Grok 4.5, Claude, and Muse Spark build the same 4 apps https://www.tryai.dev/blog/gpt-5.6-build-off-12-models / https://news.ycombinator.com/item?id=48865093 — 2026-07-10 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q7] [FAILURE] `"Most of Spark's attempts are failures:"` — rsstack, 2026-07-10; grade C; L76. Comment on the same TryAI artifacts, not an independent run.
- [Q12] [FACT] `"They have fixed their blog post."` — delichon, 2026-07-10; grade C; L28. TryAI initial cost-symbol/pricing errors corrected according to commenter; do not treat website signup localhost bug as Meta auth.

## hn/49187575.txt — Muse Code and Muse Spark 1.2 https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2 / https://news.ycombinator.com/item?id=49187575 — 2026-08-05 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q10] [GAP] `"While using free credits your content may be used for product improvement"` — bradfa, 2026-08-05; grade C; L50. Reporter says small print was added after initial free-$20-credit signup; no independently archived version comparison.
- [Q8] [BUG] `"doesn't work in Australia either."` — ray_kay777, 2026-08-06; grade C; L99. Regional API access report.
- [Q12] [GAP] `"I entered my credit card, but can not set a limit."` — sams99, 2026-08-06; grade C; L212. Only email alert reported; hard-limit workaround via OpenRouter loses contributor discount.
- [Q12] [GAP] `"No way am I trying this out without a billing limit"` — ray_kay777, 2026-08-06; grade C; L220. Second reporter of missing hard spend cap, not evidence of an actual overcharge.
- [Q7] [BUG] `"It crashed the widget."` — ssalka, 2026-08-06; grade C; L255. Black-hole interactive demo Mass slider; generated/demo artifact bug, not whole Muse service crash.
- [Q8] [BUG] `"The cursor position could not be read within a normal duration"` — goldenshale, 2026-08-06; grade C; L266. CLI exits after successful muse login; environment cause unknown.
- [Q6] [FAILURE] `"It stuck using grep/search tools."` — nthypes, 2026-08-06; grade C; L267. OpenCode + OpenRouter coding task; attribution to excessive Meta-harness RL is reporter hypothesis only.
- [Q2] [STRENGTH] `"I really liked the contributor model in their harness."` — johnmlussier, 2026-08-06; grade C; L268. Counterpoint to external-harness failure; not a controlled A/B test.
- [Q11] [FAILURE] `"Your access has been restricted due to repeated policy violations."` — johnmlussier, 2026-08-06; grade C; L270. HTTP 403 while doing Kaggle/Apple-security work per user; correctness of policy enforcement unverified.

## hn/49241861.txt — Muse Spark 1.2 (Meta) is reportedly becoming open-weight https://twitter.com/alexandr_wang/status/2086756152034066792 / https://news.ycombinator.com/item?id=49241861 — publication date not captured; accessed 2026-11-10 — C/D (per-comment detail; not independent validation)

Title/link only, no captured comments; open-weight rumor is not verified by this capture.


## hn/49541256.txt — Muse Spark 1.3 https://developer.meta.com/ai/models/muse-spark/ / https://news.ycombinator.com/item?id=49541256 — 2026-09-02 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q7] [BUG] `"It was sending every single steamed chunk for summarization instead of waiting for the full CMD."` — bermudi, 2026-09-02; grade C; L223. Muse 1.2 generated a faulty pi extension; typo steamed is verbatim.
- [Q6] [FAILURE] `"1.2 can get stuck outputting similar sounding thought summaries with no apparent progress when asked to solve bugs."` — WASDx, 2026-09-02; grade C; L148. Old-game reverse engineering; user otherwise liked speed and price and used GLM-5.3-Flash as workaround.
- [Q7] [FAILURE] `"MS1.2 wrote C code without following original source code writing style"` — roytam87, 2026-09-03; grade C; L436. Contradicts superfrank’s style-following experience; different tasks/harnesses unspecified.
- [Q2] [STRENGTH] `"it did what I told it"` — superfrank, 2026-09-02; grade C; L194. Spark 1.2 restrained instruction/style adherence, inexpensive contributor tier; not frontier-level claim.
- [Q3] [GAP] `"And their benchmark table only shows max reasoning."` — sunaookami, 2026-09-02; grade C; L261. Launch max not yet available pending safety tests; distinguishes available efforts from advertised benchmark effort.
- [Q12] [FAILURE] `"when I tested 1.3 it was very slow (through openrouter)."` — XCSme, 2026-09-03; grade C; L452. Route-dependent subjective latency, not an isolated Meta API measurement.
- [Q12] [STRENGTH] `"I've tried it via OpenCode and I'm impressed. So fast compared to Opus"` — lylo, 2026-09-03; grade C; L450. Contrasting route/task impression, not a controlled same-task speed comparison.

## hn/49615593.txt — - arionhardison 2026-09-08 The features don't really matter here IMO; where does the PA function live?  Whoever runs it sees intent streams.  If that goes to a startup then the planning, coordination etc.. is ad free.  I don't think Meta wants to live in that world. Travel is such a huge play here because its inherently social; so "^n viral loop where N is travelers; odds are most will have some meta app so possibly lower friction here too. Amplified an order of magnitude for the e-mail piece given how badly Meta would like to have google's g-mail data. Either way, interesting play IMO. / https://news.ycombinator.com/item?id=49615593 — 2026-09-08 — C/D (per-comment detail; not independent validation)

Two comments, one speculative privacy concern and one discussion link; no observed bug or independently verified product behavior.


## hn/49829888.txt — Unavailable capture / https://news.ycombinator.com/item?id=49829888 — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Empty capture (0 bytes); no evidence.


## hn/49983579.txt — - laweijfmvo 2026-10-06 This is a really poorly written article. Yes, they keep a memory; that’s the point. What use would a personal assistant be if you had to give it your full life context in every chat? If you have issues with this, especially when it’s a Meta product, then don’t use it. But this isn’t anything open claw wasn’t doing. / https://news.ycombinator.com/item?id=49983579 — 2026-10-06 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q10] [FACT] `"this information is used to improve the overall product rather than being shared directly between individual VMs"` — dataflow, 2026-10-06; grade C; L2. Quotes TIME/Meta response; not another independent privacy investigation.

## hn/50059115.txt — - 217 2026-10-12 I'm sorry zuck, i wasn't familiar with your game 2nd place model on aa according to them, losing only to opus 5.5 is really really not bad / https://news.ycombinator.com/item?id=50059115 — 2026-10-12 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q4] [FAILURE] `"it would recommend restaurants that were out of business"` — er4hn, 2026-10-12; grade C; L358. Seattle trip about two weeks earlier, user thinks Spark 1.3, NOT demonstrated Wonder failure; opening-hours and flight-date mistakes also reported.
- [Q6] [FAILURE] `"I had to remind it this is a daily flight and I am booked on the next day before it checked and apologized."` — er4hn, 2026-10-12; grade C; L358. False urgent departure alert during trip planning; same reporter counted once per theme.
- [Q4] [FACT] `"I'm assuming it was out of season"` — er4hn, 2026-10-12; grade C; L361. Qualification to salmon-season complaint: relies on Uber driver, not independently verified season error.
- [Q6] [FAILURE] `"on iteration 7 of review->fix last I checked"` — ekojs, 2026-10-12; grade C; L381. Wonder broad React/Node/Rust coding trial; review fixation loop, weaker taste/judgment than preferred frontier models.
- [Q12] [FAILURE] `"Two somewhat small prompts with Muse Wonder Max-contributor used 4% of my weekly quota"` — hugh4life, 2026-10-12; grade C; L370. Same user liked Spark 1.3 value; not proof of incorrect accounting.
- [Q12] [FAILURE] `"A lot of the tasks were failed because they exceeded the $5 budget though"` — dom96, 2026-10-12; grade C; L378. KillSwitch new-language benchmark; author acknowledges model might complete with more funds; regular Wonder, Full not tested.
- [Q7] [BUG] `"You cannot pick up a dirty plate."` — murermader, 2026-10-13; grade C; L403. Kitchen Game demo Firefox: invisible plate, tomato placement glitches; generated/demo artifact not generalized model capability.
- [Q14] [FACT] `"it seems to be related to the Wipr 2 content blocker."` — pmuse, 2026-10-12; grade C; L320. RETRACTION of initial other-account-profile leak allegation; removed Wipr Extra and symptom stopped. Excluded from Meta privacy-breach counts.
- [Q2] [STRENGTH] `"Tested it for data analytics and found it's in the class of Opus 5.5 in terms of performance and cost."` — chriddyp, 2026-10-14; grade C; L405. Independent analytics evaluation, regular Wonder; >2x faster / ~2x cost versus Spark 1.3 per author.
- [Q12] [GAP] `"GPT-6.1 Sol, Haiku 5.5, GLM all perform a similar grade at 1/10th the cost."` — chriddyp, 2026-10-14; grade C; L405. Short-horizon analytics only; not a universal price-quality comparison.

## hn/50079730.txt — Muse Wonder(Non-Full) Max Is Below Muse Spark 1.3 Max on Code Arena: WebDev https://twitter.com/arena/status/2110120205464846828 / https://news.ycombinator.com/item?id=50079730 — 2026-10-13 — C/D (per-comment detail; not independent validation)

One link-only comment and headline; no independent hands-on bug evidence. Headline claims regular Wonder below Spark 1.3 on Code Arena WebDev; not Wonder Full or a base-model general ranking.


## hn/50107379.txt — Muse Spark Open https://research.meta.ai/blog/muse-spark-open / https://news.ycombinator.com/item?id=50107379 — 2026-10-15 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q12] [GAP] `"at least $28k - $30k for the setup Muse team is advertising."` — devy, 2026-10-15; grade C; L185. Commenter’s hardware-cost estimate, not a vendor quote or market survey.

## hn/50109433.txt — Unavailable capture / https://news.ycombinator.com/item?id=50109433 — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Empty capture (0 bytes); no evidence.


## hn/50118320.txt — Apple ML Research: Muse Spark Open with MLX on Mac Studio https://machinelearning.apple.com/research/mlx-distributed-inference / https://news.ycombinator.com/item?id=50118320 — 2026-10-16 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q2] [STRENGTH] `"Muse Glimmer is by far the most usable model on my 32GB M1 Max."` — solarkraft, 2026-10-18; grade C; L48. Local-user impression, not controlled benchmark.

## hn/50131617.txt — Unavailable capture / https://news.ycombinator.com/item?id=50131617 — publication date not captured; accessed 2026-11-10 — D (unusable capture; source unassessed)

Empty capture (0 bytes); no evidence.


## hn/50287747.txt — - freecodeio 2026-10-29 My LLM experience is frontier models in a group chat for the best outcome. I recently added muse wonder and removed it after a few hours of use. I'd even use deepseek flash over muse for literally anything. / https://news.ycombinator.com/item?id=50287747 — 2026-10-29 — C/D (per-comment detail; not independent validation)

Read completely; only Muse-relevant evidence retained. A source’s quoted claims are not independent reproductions.

- [Q13] [FAILURE] `"I recently added muse wonder and removed it after a few hours of use."` — freecodeio, 2026-10-29; grade D; L1. Grade D: vague multi-model group-chat dissatisfaction, no reproducible failure; not evidence of a specific bug.

## gh/1f916-ai_stocks.now_issues_1.txt — muse-spark agents are counted as llama in the family indexes (2026-11-09) / https://github.com/1f916-ai/stocks.now/issues/1 — 2026-11-09 — C

- [Q5] [BUG] `"Notes: the FAMILIES list has no muse entry, so this is a mapping gap, not a data problem on 1F916."` — 1f916-ai/stocks.now#1, 2026-11-09; attribution: harness/router-side (application model-family classification); L8.

## gh/TableProApp_TablePro_issues_4070.txt — Meta Model API (Muse Spark, Muse Wonder) as an AI provider (2026-11-06) / https://github.com/TableProApp/TablePro/issues/4070 — 2026-11-06 — C

Provider feature request, not evidence of a Meta-side defect. API details below are the request author’s statements.

- [Q1] [BUG] `"Using them today means adding a Custom provider and typing the endpoint and model ID by hand."` — TableProApp/TablePro#4070, 2026-11-06; attribution: harness/router-side (provider-preset feature request; not observed model defect); L4. Missing TablePro preset; harness/router-side integration gap, not a model defect.
- [Q8] [BUG] ``"`none` returns 400."`` — TableProApp/TablePro#4070, 2026-11-06; attribution: harness/router-side (provider-preset feature request; not observed model defect); L18. API reasoning restriction reported in feature request.
- [Q10] [BUG] ``"`-contributor` variants are cheaper but Meta may train on the content."`` — TableProApp/TablePro#4070, 2026-11-06; attribution: harness/router-side (provider-preset feature request; not observed model defect); L17. Contributor privacy tradeoff reported, not independently measured.

## gh/decolua_9router_issues_5426.txt — [muse] chat/completions returns empty content for muse-spark models, responses works (2026-11-03) / https://github.com/decolua/9router/issues/5426 — 2026-11-03 — C

Do not conflate Meta first-party API with Zen/Go or the capture’s anomalous Moonshot/Kimi upstream labeling. #4602 asserts Responses-only; #4624 demonstrates Chat-compatible workaround returning 200. Endpoint choice is route-specific, not a universal Meta API limitation.

- [Q8] [BUG] ``"Models served through the 9Router `muse` provider (upstream: Moonshot/Kimi `muse-spark` family) return empty `choices[0].message.content` on `POST /v1/chat/completions`, both streaming and non-streaming."`` — decolua/9router#5426, 2026-11-03; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L3.
- [Q8] [BUG] ``"System prompt, `tools: []`, `reasoning_effort: medium`, `temperature: 0.7` — identical empty result."`` — decolua/9router#5426, 2026-11-03; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L28.
- [Q12] [BUG] ``"Result: `status: completed`, correct factorial code, `output_tokens: 364 (reasoning 302)`."`` — decolua/9router#5426, 2026-11-03; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L34.
- [Q12] [BUG] ``"- All return `400 Upstream request failed: Model is unavailable.`"`` — decolua/9router#5426, 2026-11-03; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L40.
- [Q8] [BUG] ``"The `muse` provider's Responses-to-chat/completions translation does not map the upstream output message into `choices[0].message.content`."`` — decolua/9router#5426, 2026-11-03; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L52.

## gh/fvtale_GhostSignalV2_issues_1.txt — Live-key shakedown of Muse Spark and Muse Voice (2026-10-30) / https://github.com/fvtale/GhostSignalV2/issues/1 — 2026-10-30 — C

Read completely; implementation/tracking request, not an observed Muse bug.


## gh/ggml-org_llama.cpp_pull_32017.txt — chat : fix Muse Spark ignoring response_format json_schema (2026-11-10) / https://github.com/ggml-org/llama.cpp/pull/32017 — 2026-11-10 — C

- [Q9] [BUG] `"The Muse Spark parser ignores json_schema and only builds a grammar when tools are given."` — ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); L6.
- [Q9] [BUG] `"So a top-level json_schema falls back to the server's schema grammar, which fails on the "<|start|>assistant" generation prompt prefill (400), and response_format is silently not applied."` — ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); L6.
- [Q9] [BUG] `"Build a response format rule for the final message when json_schema is set, with an eager grammar, and keep reasoning free-form."` — ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); L8.
- [Q1] [BUG] `"This is the same fix as #29615 for Muse Glimmer."` — ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); L8.
- [Q1] [BUG] `"Added the same two test-chat cases as Muse Glimmer (direct final answer, and after a reasoning message)."` — ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); L12.
- [Q5] [BUG] `"A raw GBNF grammar (case 2 in the issue) is not changed by this PR: a user grammar applies from the first token, as for other harmony-style models."` — ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); L13.
- [Q9] [BUG] `"Not tested on the real model."` — ggml-org/llama.cpp#32017, 2026-11-10; attribution: harness/router-side (inference grammar/parser); L13. Parser tests do not establish real-model end-to-end reliability.

## gh/huggingface_trl_pull_8225.txt — Map the Muse Spark Open chat template to its training template (2026-11-10) / https://github.com/huggingface/trl/pull/8225 — 2026-11-10 — C

- [Q9] [BUG] ``"This PR stops `SFTTrainer` with `assistant_only_loss=True` from training the `<|start|>assistant` that opens each Muse Spark Open assistant turn: the generation markers the template ships also cover it, while the generation prompt already ends with it."`` — huggingface/trl#8225, 2026-11-10; attribution: harness/router-side (training template assistant-loss mask); L2.
- [Q1] [BUG] ``"Add a training template with the same markers moved after the turn's leading `<|start|>assistant`: the same change as the Hub PRs on the Muse Spark Open repos (https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B/discussions/28,"`` — huggingface/trl#8225, 2026-11-10; attribution: harness/router-side (training template assistant-loss mask); L10.
- [Q9] [BUG] `"The rendered text is unchanged: only the assistant mask changes."` — huggingface/trl#8225, 2026-11-10; attribution: harness/router-side (training template assistant-loss mask); L10.

## gh/midagedev_bloomery_issues_684.txt — model: Muse Spark Open (muse-spark, 816B-A42B MoE, text + vision + audio) (2026-10-22) / https://github.com/midagedev/bloomery/issues/684 — 2026-10-22 — C

Read completely; implementation/tracking request, not an observed Muse bug.


## gh/pytorch_torchtitan_issues_5915.txt — Muse Spark token embedding gets no gradient under TP (2026-11-07) / https://github.com/pytorch/torchtitan/issues/5915 — 2026-11-07 — C

- [Q9] [BUG] ``"On main (`9f70e5597`), `muse_spark_debugmodel` at TP2+EP2 (seed 42) gives `tok_embeddings.embedding.weight.grad is None` at every step; every other parameter gets a gradient."`` — pytorch/torchtitan#5915, 2026-11-07; attribution: harness/router-side (distributed-training/runtime); L2.
- [Q9] [BUG] `"#5802 makes the embedding's reduction explicit and synchronous, which restores the gradient (grad norm 0.0590 at step 1; TP1 reference 0.0564), and #5807 removes the async boundary path."` — pytorch/torchtitan#5915, 2026-11-07; attribution: harness/router-side (distributed-training/runtime); L4.

## gh/sgl-project_sglang_issues_44678.txt — [Roadmap] Muse Spark Open Development & Optimization (2026-10-16) / https://github.com/sgl-project/sglang/issues/44678 — 2026-10-16 — C

Read completely: Muse Spark Open support/tracking discussion; no concrete failure established in this capture.


## gh/vllm-project_vllm_issues_64632.txt — [Tracking] Muse Spark Open Improvement (2026-10-30) / https://github.com/vllm-project/vllm/issues/64632 — 2026-10-30 — C

- [Q9] [BUG] `"- [x] #63871 — Fix dummy-loaded Muse MegaMoE weights"` — vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); L10.
- [Q9] [BUG] `"- [x] #62757 — Share one RoPE cache sized by max_model_len"` — vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); L22.
- [Q9] [BUG] `"- [ ] #63078 — Keep FP32 RoPE tables in FP32"` — vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); L23.
- [Q9] [BUG] `"There are couple of parallel bug fixes around a tiny accuracy issue that is affecting couple of models including Muse Spark."` — vllm-project/vllm#64632, 2026-10-30; attribution: harness/router-side (inference runtime/parser); comment by amd-mghanimi, 2026-11-10; L55.

## gh2/CommandCodeAI_command-code_issues_799.txt — muse spark 1.3 contributor usage bug (2026-09-03) / https://github.com/CommandCodeAI/command-code/issues/799 — 2026-09-03 — C

- [Q12] [BUG] `"only with 54.1m tokens I hit my limits"` — CommandCodeAI/command-code#799, 2026-09-03; attribution: unclear (contributor caching/metering symptom, no verified provider accounting cause); L5. Reporter compares three credits for ~54.1M tokens against previous 1.2B/ten credits on 1.2 contributor; not a verified 666% price change.
- [Q12] [BUG] `"I can also attest the same issue."` — CommandCodeAI/command-code#799, 2026-09-03; attribution: unclear (contributor caching/metering symptom, no verified provider accounting cause); comment by omar391, 2026-09-13; L57. omar391, 2026-09-13: second commenter corroborates symptom; cause/caching/accounting not independently established.

## gh2/NousResearch_hermes-agent_issues_132837.txt — opencode-go: supports_vision_tool_messages=False veto is stale on responses/codex transport — native tool-result vision works live (2026-10-04) / https://github.com/NousResearch/hermes-agent/issues/132837 — 2026-10-04 — C

- [Q3] [BUG] ``"`OpenCodeGoProfile` sets `supports_vision_tool_messages=False` (`plugins/model-providers/opencode-zen/__init__.py`), citing Console-Go #104731 (`422 messages.N.tool.content.str`) and MiMo #47026 (`400 text is not set`)."`` — NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); L3.
- [Q3] [BUG] ``"- `agent/image_routing._lookup_supports_vision('opencode-go', 'muse-spark-1.3-contributor')` → **True**, `decide_image_input_mode` → **native** (the model IS catalogued vision-capable)"`` — NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); L11.
- [Q3] [BUG] ``"- but `tools/vision_tools._accepts_tool_result_images` → **False**, veto first (`:564`) — so `vision_analyze`/`computer_use` captures always fall back to the aux-LLM text downgrade on Go, needlessly."`` — NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); L12.
- [Q3] [BUG] ``"Scope the veto to chat-completions transports: only return `supports_vision_tool_messages=False` for opencode-go when the active transport is chat-completions, and allow native tool-result media on responses/codex."`` — NousResearch/hermes-agent#132837, 2026-10-04; attribution: harness/router-side (dispatch/capability/effort handling); L15.

## gh2/NousResearch_hermes-agent_issues_141861.txt — [bug] Kanban worker posts chat/completions despite resolved api_mode=codex_responses: muse-spark on opencode-go gets 400 ModelProtocolUnsupported (2026-10-20) / https://github.com/NousResearch/hermes-agent/issues/141861 — 2026-10-20 — C

- [Q3] [BUG] ``"Kanban worker on profile `readwhere` (model `muse-spark-1.3-contributor`, provider `opencode-go`) fails every LLM call with HTTP 400 `ModelProtocolUnsupported` ("Model does not support this protocol")."`` — NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); L4.
- [Q8] [BUG] ``"The same model + provider + key works fine in regular (Telegram/CLI) sessions and via direct `POST /responses`."`` — NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); L4.
- [Q8] [BUG] ``"Worker log traceback: `_StreamingCall._call → _call_wire → _call_chat_completions → relay_llm → _open_chat_stream → chat.completions.create`."`` — NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); L13.
- [Q12] [BUG] ``"- `POST /zen/go/v1/responses` `{model: muse-spark-1.3-contributor, input, max_output_tokens: 32}` → **200** with reasoning output."`` — NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); L18.
- [Q8] [BUG] ``"- Failing sessions: kanban worker, `platform=kanban`; working: same profile model via Telegram/CLI"`` — NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); L32.
- [Q8] [BUG] `"it is just never threaded into the worker construction."` — NousResearch/hermes-agent#141861, 2026-10-20; attribution: harness/router-side (dispatch/capability/effort handling); comment by whyyagswhy, 2026-10-20; L89. Investigation points to missing api_mode in Kanban bootstrap; later direct instrumentation is for a GPT route, not proof every Muse path identical.

## gh2/NousResearch_hermes-agent_pull_140813.txt — fix(agent): accept reasoning effort max on Muse Spark 1.3 (2026-10-18) / https://github.com/NousResearch/hermes-agent/pull/140813 — 2026-10-18 — C

- [Q14] [BUG] ``"Hermes clamped `max` down to `xhigh` on both the direct Meta route and the OpenCode Zen/Go Responses route, because those paths used a vocabulary that stopped at `xhigh`."`` — NousResearch/hermes-agent#140813, 2026-10-18; attribution: harness/router-side (dispatch/capability/effort handling); L5.
- [Q14] [BUG] ``"- `plugins/model-providers/meta-ai/__init__.py`: `build_api_kwargs_extras` clamps with `meta_ai_supported_efforts(model)` instead of the shared 1.2 ceiling."`` — NousResearch/hermes-agent#140813, 2026-10-18; attribution: harness/router-side (dispatch/capability/effort handling); L26.
- [Q14] [BUG] ``"Confirm `max` stays `max` for `muse-spark-1.3*` on meta-ai, opencode-go, and opencode-zen, and that `muse-spark-1.2` / `muse-spark` still clamp `max` to `xhigh`."`` — NousResearch/hermes-agent#140813, 2026-10-18; attribution: harness/router-side (dispatch/capability/effort handling); L32.

## gh2/RandyNorthrup_muse-spark-code_issues_146.txt — Problem report: Muse Spark 0.16.0 on win32 (2026-10-11) / https://github.com/RandyNorthrup/muse-spark-code/issues/146 — 2026-10-11 — C

Insufficient evidence: no reproducible bug description, maintainer says not signed in/no key. Excluded from failure counts.


## gh2/Wei-Shaw_sub2api_pull_8044.txt — fix(apicompat): add required summary to replayed reasoning input items (2026-10-12) / https://github.com/Wei-Shaw/sub2api/pull/8044 — 2026-10-12 — C

- [Q8] [BUG] ``"A Claude Code (`/v1/messages`) request that replays a thinking block is forwarded to a Responses upstream with a `reasoning` input item that has `encrypted_content` but **no `summary`**."`` — Wei-Shaw/sub2api#8044, 2026-10-12; attribution: harness/router-side (reasoning replay missing summary); L4.
- [Q12] [BUG] ``"The Responses API requires `summary` on every reasoning input item (an empty array is valid), and strict upstreams reject the request:"`` — Wei-Shaw/sub2api#8044, 2026-10-12; attribution: harness/router-side (reasoning replay missing summary); L4.
- [Q8] [BUG] ``"Also verified against a live OpenCode Go upstream: `muse-spark-1.3-contributor` answered 400 to a replayed thinking block before the change and 200 after it, over several multi-turn tool loops; `deepseek-v4.1-flash` and Gemini kept working."`` — Wei-Shaw/sub2api#8044, 2026-10-12; attribution: harness/router-side (reasoning replay missing summary); L21.

## gh2/YanyuLiu_meta_muse_eval_pull_2.txt — Add TL;DR insights from the Muse Spark API evaluation (2026-09-24) / https://github.com/YanyuLiu/meta_muse_eval/pull/2 — 2026-09-24 — C (independent synthetic measurement; raw logs withheld)

- [Q10] [BUG] `"The main gap is over-helpfulness on action-sounding requests (pay, cancel, order, RSVP, send) and extra profile/calendar/mailbox reads."` — YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; L7.
- [Q10] [BUG] `"Confirmation recall was 5/12; over-intervention was 0/3."` — YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; L7.
- [Q6] [BUG] `"Write tools in the harness were acknowledged locally and were not sent, charged, or posted."` — YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; L23.
- [Q11] [BUG] `"injection attacks in this set did not succeed (0/10)."` — YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; L7. Synthetic 30-case sandbox evaluation, NOT a production app security certification; raw logs withheld.
- [Q10] [BUG] `"This is an exploratory behavioral snapshot, not a product security certification."` — YanyuLiu/meta_muse_eval#2, 2026-09-24; attribution: Meta/Muse-side behavior observed in synthetic API harness only; not production exploitation; L23. Write tools locally acknowledged, never sent/charged/posted; 5/12 confirmation recall, 0/3 over-intervention; over-helpfulness/privacy reads are observed model behavior only in this harness.

## gh2/alfonsodg_herdr_issues_1.txt — fix(detect): Muse Code detection flapping in v1.4+ and missing executable aliases (2026-10-05) / https://github.com/alfonsodg/herdr/issues/1 — 2026-10-05 — C

- [Q8] [BUG] ``"Lastly, `src/agent_resume.rs` lacks a resume plan for Muse sessions."`` — alfonsodg/herdr#1, 2026-10-05; attribution: harness/router-side (stale UI/alias detection); L5.
- [Q8] [BUG] `"Users running modern Muse Code experience inconsistent agent status, missing sidebar indicators, dropped agent sessions during normal idle turns, and inability to restore sessions on restart."` — alfonsodg/herdr#1, 2026-10-05; attribution: harness/router-side (stale UI/alias detection); L28.
- [Q8] [BUG] ``"Add resume plan in `src/agent_resume.rs` for Muse sessions."`` — alfonsodg/herdr#1, 2026-10-05; attribution: harness/router-side (stale UI/alias detection); L33.

## gh2/anomalyco_opencode_issues_48741.txt — Opencode Zen critical errors on Muse Spark family when model recieves a image/does a tool call (2026-09-13) / https://github.com/anomalyco/opencode/issues/48741 — 2026-09-13 — C

Distinct users report restart, idle, images, or mid-tool-chain variants; stripping stale encrypted reasoning helps some sessions, others fail again. Provider IP/key binding remains unverified; no single universal cause established.

- [Q8] [BUG] ``"Error: Error from provider (Console): Upstream request failed: [invalid_request_error] reasoning `encrypted_content` was not issued to this caller when requesting any Muse Spark model on Zen."`` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); L4.
- [Q8] [BUG] `"Fixed by creating new session, but even on this new session it will have this problem again so I can't have long sessions."` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by pegasusearl, 2026-09-13; L76.
- [Q8] [BUG] ``"Same root cause as #43557: after a restart, OpenCode replays the stale `reasoning.encrypted_content` blob (bound to the previous caller/key) and upstream rejects it with `not issued to this caller`."`` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by unurgunite, 2026-09-13; L96.
- [Q9] [BUG] ``"Proper fix still belongs in core (drop + retry without the blob on `invalid_encrypted_content`)."`` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by unurgunite, 2026-09-13; L100.
- [Q12] [BUG] `"Whenever you just idle it for 3 minutes or 5 minutes, the next chat will get this error."` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by MrSaikatS, 2026-09-13; L109.
- [Q8] [BUG] `"It fixed my old sessions However the next error will still happen, I tried two attempts and both failed, same error message."` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by pegasusearl, 2026-09-13; L118.
- [Q8] [BUG] `"The recurring in-session failure you describe (works after restart, then fails again) I can't reproduce on my side — mine fails strictly after restart."` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by unurgunite, 2026-09-13; L127.
- [Q6] [BUG] `"In our case the poisoned turn broke mid-tool-chain, and everything after it failed for a day: service-restart drains, fresh prompts, and compaction all hit the same 400."` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by darkred1145, 2026-09-14; L172.
- [Q8] [BUG] `"Same error on 1.18.30 when **resuming an old Muse 1.3 session after idle** (no image required)."` — anomalyco/opencode#48741, 2026-09-13; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by 1837620622, 2026-09-14; L189.

## gh2/anomalyco_opencode_issues_51649.txt — Infinite response loop or smth issue (2026-09-27) / https://github.com/anomalyco/opencode/issues/51649 — 2026-09-27 — C

- [Q6] [BUG] `"With Muse Spark 1.3 free model (at least with this model), there is an issue where the shell command is executing and has been executing at the same time thinking process of the model is executing and when the shell thing ends thinking process just keeps on going and so the model is stuck."` — anomalyco/opencode#51649, 2026-09-27; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); L4.
- [Q6] [BUG] `"For me it is when it executes gradle.bat installDebug when build finishes (succesfully or not)  it just does not generate afterwards affecting long horizon work."` — anomalyco/opencode#51649, 2026-09-27; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); L17.
- [Q12] [BUG] ``"The free Muse models (`muse-spark-1.2-contributor-free` and `muse-spark-1.3-contributor-free`) have been removed from the free tier, so this no longer applies."`` — anomalyco/opencode#51649, 2026-09-27; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by Tarquinen, 2026-10-20; L39.

## gh2/anomalyco_opencode_issues_57804.txt — Model Beam Free stuck in a loop thinking and reading (2026-10-21) / https://github.com/anomalyco/opencode/issues/57804 — 2026-10-21 — C

Main issue is Beam, not Muse. Retain only explicit Muse-related cross-reference, not other-model loops as independent Muse evidence.

- [Q6] [BUG] `"> * [[OpenCode Go] muse-spark-1.3-contributor gets stuck in repeated Read/Search loops and fails t"` — anomalyco/opencode#57804, 2026-10-21; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by zzz-creator, 2026-10-21; L75.
- [Q6] [BUG] ``"Without your exact `opencode --version`, what you asked the agent to do, and how the loop behaved (how many repeats, whether it stopped on its own, whether the `doom_loop` prompt appeared), we can't tell whether the repeated reads come from OpenCode or from the Beam Free model."`` — anomalyco/opencode#57804, 2026-10-21; attribution: unclear (client replay/loop behavior; provider key/session binding not fully established); comment by opencode-agent[bot], 2026-10-24; L81.

## gh2/anpicasso_hermes-oc-free-provider_issues_3.txt — Blank replies in OpenWebUI when streaming (2026-10-01) / https://github.com/anpicasso/hermes-oc-free-provider/issues/3 — 2026-10-01 — C

- [Q8] [BUG] ``"OpenWebUI shows empty replies for `muse-spark-1.3-contributor-free`, only when streaming."`` — anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); L2.
- [Q8] [BUG] ``"Reply bubble stays empty, but non-streaming (`stream:false`) to same endpoint returns text fine"`` — anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); L11.
- [Q8] [BUG] ``"Actual: zero text deltas, clean `stop`, with `completion_tokens > 0`"`` — anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); L14.
- [Q8] [BUG] `"- Other not OpenCode models stream fine, so looks like the Responses -> Chat translator drops the text"` — anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); L17.
- [Q14] [BUG] `"- Workaround: switch the Hermes connection in OpenWebUI to Responses API type"` — anpicasso/hermes-oc-free-provider#3, 2026-10-01; attribution: harness/router-side (stream translator); L18.

## gh2/anthropics_claude-code_issues_95021.txt — [BUG] /goal evaluator schema rejected by strict backends: required omits impossible (2026-09-17) / https://github.com/anthropics/claude-code/issues/95021 — 2026-09-17 — C

- [Q9] [BUG] ``"The `/goal` Stop-hook evaluator sends an `output_config.format` JSON schema whose `required` array omits one of its own properties (`impossible`)."`` — anthropics/claude-code#95021, 2026-09-17; attribution: harness/router-side (invalid /goal JSON schema; strict Meta rejection is not model defect); L4.
- [Q8] [BUG] ``"Any backend that enforces the strict schema subset (`required` must list every key in `properties`) rejects every evaluation with HTTP 400."`` — anthropics/claude-code#95021, 2026-09-17; attribution: harness/router-side (invalid /goal JSON schema; strict Meta rejection is not model defect); L4.
- [Q6] [BUG] ``"Reproduced against Meta Model API `/v1/messages` (Anthropic-compatible endpoint, model `muse-spark-1.3`): each turn that reaches Stop while a goal is active fails and the goal never evaluates."`` — anthropics/claude-code#95021, 2026-09-17; attribution: harness/router-side (invalid /goal JSON schema; strict Meta rejection is not model defect); L6.

## gh2/can1357_oh-my-pi_issues_12306.txt — opencode-zen: muse-spark-1.3-contributor-free returns 403 FreeTierError in OMP while working in OpenCode (2026-09-17) / https://github.com/can1357/oh-my-pi/issues/12306 — 2026-09-17 — C

Free-tier client gate can be intentional policy. Later October 16 test could not reproduce required registered-session claim; preserve disagreement. Empty Chat-vs-Responses bridge verified in captured report; do not promote an IP theory to confirmed Meta cause.

- [Q12] [BUG] ``"`muse-spark-1.3-contributor-free` works successfully through OpenCode, but the same model returns HTTP 403 `FreeTierError` when used through OMP."`` — can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L4.
- [Q12] [BUG] `"403 Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"` — can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L9.
- [Q12] [BUG] ``"The same API key that gets `403 (type=FreeTierError) OpenCode's free tier can only be used from within OpenCode` from OMP succeeds from the genuine `opencode` CLI, so nothing is wrong with the key, the account, or the model id."`` — can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by insodimension, 2026-09-18; L198.
- [Q12] [BUG] `"Fabricated session IDs always return 403 FreeTierError regardless of headers, endpoint path, or tool count."` — can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by Lakshit-Gupta, 2026-10-13; L230.
- [Q8] [BUG] ``"Following up on the 2026-10-13 report that the header patch stopped working because Zen now validates `x-opencode-session` as a server-registered session: I could not reproduce that today (2026-10-16)."`` — can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by jaskaran-ai, 2026-10-16; L257.
- [Q8] [BUG] ``"So the bridge turns the loud refusal into a quiet wrong answer. `/v1/responses` returns the actual text. `/v1/chat/completions` returns 200 with an empty `content` and no error, which most clients read as success."`` — can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by ebouther, 2026-10-16; L300.
- [Q8] [BUG] ``"Worth settling for #12556 before the gate work: routing this id as `openai-responses` is the right call, because a chat-shaped path doesn't fail loudly here, it returns nothing."`` — can1357/oh-my-pi#12306, 2026-09-17; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by ebouther, 2026-10-16; L302.

## gh2/can1357_oh-my-pi_issues_15551.txt — /usage: muse-code shows "no usage data" after Meta account token expires — no re-login hint (refresh "none") (2026-10-13) / https://github.com/can1357/oh-my-pi/issues/15551 — 2026-10-13 — C

- [Q8] [BUG] ``"`/usage` (and `omp usage --provider muse-code`) shows `Muse Code — 1 account, no usage data` once the Meta account OAuth token expires."`` — can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L4.
- [Q8] [BUG] ``"The underlying error is a 401 from `POST https://api.meta.ai/muse-code/key`, visible only in debug logs."`` — can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L4.
- [Q12] [BUG] `"Nothing tells the user to re-login, and inference keeps working (it uses the minted Model API key), so it looks like a usage-tracking bug rather than expired auth."` — can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L4.
- [Q8] [BUG] ``"- `packages/catalog/src/compat/rules/auth/muse-code.kdl` sets `refresh "none"` and `expires "never"` (comment: "Meta's device response omits expiry and rejects refresh_token grants"), so OMP never refreshes and never warns."`` — can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L32.
- [Q1] [BUG] ``"So only `/usage` breaks — easy to misread as a usage-metering regression (e.g. blamed on the recent Muse Wonder model additions)."`` — can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L34.
- [Q8] [BUG] ``"I'm triaging this as an enhancement, not a bug: the 401 is Meta revoking an account token that OMP has no way to refresh, and `/usage` currently gives the same generic row for every kind of usage-fetch failure."`` — can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by roboomp, 2026-10-13; L52.
- [Q8] [BUG] ``"Meta's device flow returns no expiry and rejects `refresh_token` grants, so OMP can't refresh the account token or warn before it dies."`` — can1357/oh-my-pi#15551, 2026-10-13; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by roboomp, 2026-10-13; L55.

## gh2/can1357_oh-my-pi_issues_15737.txt — muse-code/muse-wonder-1.0` prints tool-call markup as plain text instead of making a tool call (2026-10-14) / https://github.com/can1357/oh-my-pi/issues/15737 — 2026-10-14 — C

ATEM markup leak observed on this provider/harness route; opening envelope absence prevents reconstruction of a real call in #15737. Native Muse template syntax alone does not prove an output decoding defect in the model.

- [Q1] [BUG] ``"Using the built-in `muse-code` provider with `muse-wonder-1.0` (auto-discovered after logging in with a Muse Code subscription, default catalog entry, no custom `models.yml`), the assistant when finishing prewalk wrote the following tool-call markup into the visible reply."`` — can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L7.
- [Q8] [BUG] ``"The `atem:` namespace isn't omp's own tool-call format, so this looks like the model emitting a foreign tool-call syntax as text."`` — can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); L27.
- [Q1] [BUG] ``"- `muse-code` runs `muse-wonder-1.0` over `openai-responses` with native function calling (`packages/catalog/src/compat/rules/providers/muse-code.kdl`, which inherits the `meta` seed rows). omp sends structured `tools` and reads the `function_call` output items."`` — can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by roboomp, 2026-10-14; L71.
- [Q8] [BUG] ``"- Your output had only closing tags (`</atem:parameter>`, `</atem:invoke>`, `</atem:function>`) with no opening envelope, tool name or arguments."`` — can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by roboomp, 2026-10-14; L72.
- [Q6] [BUG] ``"- omp's leak-repair code (`packages/ai/src/utils/stream-markup-healing.ts`, chosen by `detectStreamMarkupHealing` in `packages/catalog/src/compat/resolve.ts`) only covers documented chat-template formats on OpenAI-compatible chat hosts, such as DeepSeek DSML, Kimi and Qwen."`` — can1357/oh-my-pi#15737, 2026-10-14; attribution: unclear (provider policy/session gating, harness auth/markup handling; per-bullet caveats); comment by roboomp, 2026-10-14; L73.

## gh2/decolua_9router_issues_4602.txt — [Bug] [Muse (Meta Model API)] unknown parameter `input` (2026-10-05) / https://github.com/decolua/9router/issues/4602 — 2026-10-05 — C

Do not conflate Meta first-party API with Zen/Go or the capture’s anomalous Moonshot/Kimi upstream labeling. #4602 asserts Responses-only; #4624 demonstrates Chat-compatible workaround returning 200. Endpoint choice is route-specific, not a universal Meta API limitation.

- [Q8] [BUG] ``"ERROR 400 · muse/muse-spark-1.3 · URL: https://api.meta.ai/v1/chat/completions [400]: {"error":{"code":null,"message":"unknown parameter `input`","param":"input","type":"invalid_request_error"}}"`` — decolua/9router#4602, 2026-10-05; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L5.
- [Q8] [BUG] `"The provider is sending input (Responses API format) to /v1/chat/completions, which only accepts messages."` — decolua/9router#4602, 2026-10-05; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L10.
- [Q8] [BUG] `"Muse Spark is responses-only and should be routed to /v1/responses."` — decolua/9router#4602, 2026-10-05; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L10.

## gh2/decolua_9router_issues_4624.txt — [Bug] Muse provider fails with 400 `unknown parameter "input"` — broken targetFormat routing (2026-10-06) / https://github.com/decolua/9router/issues/4624 — 2026-10-06 — C

Do not conflate Meta first-party API with Zen/Go or the capture’s anomalous Moonshot/Kimi upstream labeling. #4602 asserts Responses-only; #4624 demonstrates Chat-compatible workaround returning 200. Endpoint choice is route-specific, not a universal Meta API limitation.

- [Q8] [BUG] ``"All chat completions via `muse/*` fail with upstream HTTP 400: `unknown parameter "input"`."`` — decolua/9router#4624, 2026-10-06; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L8.
- [Q8] [BUG] ``"while every model declares `targetFormat:"openai-responses"` / `supportedFormats:["openai-responses"]`."`` — decolua/9router#4624, 2026-10-06; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L18.
- [Q8] [BUG] ``"- all 5 models: `targetFormat` / `supportedFormats` `"openai-responses"` → `"openai"`"`` — decolua/9router#4624, 2026-10-06; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L25.
- [Q12] [BUG] ``"After patching, `muse/muse-spark-1.3` returns HTTP 200 with correct content. (Note: it is a reasoning model — it needs a generous `max_tokens`, otherwise the whole budget goes to reasoning and `content` comes back empty with `finish_reason: "length"`.)"`` — decolua/9router#4624, 2026-10-06; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L28.
- [Q8] [BUG] ``"Consistent routing — either fix transport selection for `targetFormat: "openai-responses"`, or ship the provider with the working `openai` format."`` — decolua/9router#4624, 2026-10-06; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L31.

## gh2/decolua_9router_issues_4736.txt — [combo] Zero-content HTTP 200s count as success and defeat fallback (2026-10-11) / https://github.com/decolua/9router/issues/4736 — 2026-10-11 — C

Do not conflate Meta first-party API with Zen/Go or the capture’s anomalous Moonshot/Kimi upstream labeling. #4602 asserts Responses-only; #4624 demonstrates Chat-compatible workaround returning 200. Endpoint choice is route-specific, not a universal Meta API limitation.

- [Q8] [BUG] ``"Some upstreams — notably free-tier models behind opencode.ai/zen — intermittently return **HTTP 200 with no usable content**: e.g. a Responses-API stream containing only `response.created / response.in_progress / response.output_item.added / response.incomplete` events, translated to an empty assistant message with"`` — decolua/9router#4736, 2026-10-11; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L14.
- [Q8] [BUG] ``"The combo logs `Model oc/<...> succeeded` and returns the empty result to the client; fallback never fires."`` — decolua/9router#4736, 2026-10-11; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L14.
- [Q8] [BUG] `"A retry seconds later against the same model returns a normal completion, so this is transient upstream flakiness that fallback exists precisely to absorb — but currently can't."` — decolua/9router#4736, 2026-10-11; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L23.
- [Q8] [BUG] `"This breaks Claude Code's auto-mode safety classifier when routed through 9Router: the verdict request gets an empty-200 'success', Claude Code receives no verdict, and **every Bash/Write action in the session is denied** ('auto mode\'s check had no usable answer') while trivially-safe commands keep working — which"` — decolua/9router#4736, 2026-10-11; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L27.
- [Q8] [BUG] `"Treat a 2xx with zero usable content as a failure for fallback purposes and continue down the combo chain."` — decolua/9router#4736, 2026-10-11; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L31.
- [Q8] [BUG] ``"Additional data point from testing: non-streaming `/v1/chat/completions` responses have a trailing `data: [DONE]` SSE terminator appended after the JSON body, which breaks strict JSON parsers (`json.load` fails with `Extra data`)."`` — decolua/9router#4736, 2026-10-11; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; comment by rekcilyssup, 2026-10-11; L40.
- [Q8] [BUG] ``"Second fallback-chain finding from the same session: `checkFallbackError` treats a provider 400 as chain-aborting (`failed (no fallback)` → return immediately)."`` — decolua/9router#4736, 2026-10-11; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; comment by rekcilyssup, 2026-10-11; L43.
- [Q3] [BUG] `"A 400 here is provider-capability-specific (that provider can't do multimodal blocks), not proof the request is malformed — other chain members would likely have served it."` — decolua/9router#4736, 2026-10-11; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; comment by rekcilyssup, 2026-10-11; L43.

## gh2/decolua_9router_pull_4387.txt — fix(opencode): clamp max_output_tokens for muse-spark to [8000, 1M] to avoid empty completions (2026-09-27) / https://github.com/decolua/9router/pull/4387 — 2026-09-27 — C

Do not conflate Meta first-party API with Zen/Go or the capture’s anomalous Moonshot/Kimi upstream labeling. #4602 asserts Responses-only; #4624 demonstrates Chat-compatible workaround returning 200. Endpoint choice is route-specific, not a universal Meta API limitation.

- [Q8] [BUG] ``"`muse-spark-1.2/1.3-contributor-free` (OpenCode Free, Responses path) returns empty completions on small `max_output_tokens` budgets."`` — decolua/9router#4387, 2026-09-27; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L4.
- [Q12] [BUG] `"The model spends nearly the entire token budget on internal reasoning before emitting any visible text."` — decolua/9router#4387, 2026-09-27; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L4.
- [Q12] [BUG] `""incomplete_details": {"reason": "max_output_tokens"},"` — decolua/9router#4387, 2026-09-27; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L11.
- [Q12] [BUG] `""usage": {"output_tokens": 100, "output_tokens_details": {"reasoning_tokens": 97}}"` — decolua/9router#4387, 2026-09-27; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L13.
- [Q8] [BUG] ``"9Router translates this as a normal `end_turn` with no content — the caller sees a silent empty turn with no error."`` — decolua/9router#4387, 2026-09-27; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L18.
- [Q8] [BUG] `"**Upstream API limits:** values above 1,000,000 return HTTP 400."` — decolua/9router#4387, 2026-09-27; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L27.
- [Q12] [BUG] ``"In `OpenCodeExecutor.transformRequest`, after the existing `max_output_tokens` normalisation (which maps `max_tokens` → `max_output_tokens`), clamp the value for muse-spark models to `[8000, 1_000_000]`:"`` — decolua/9router#4387, 2026-09-27; attribution: harness/router-side (transport/translation/fallback); upstream empty-budget behavior separately described; L33.

## gh2/getpaseo_paseo_issues_6342.txt — Importing a Muse Code session fails with "Invalid plugin provider persistence handle" (2026-10-07) / https://github.com/getpaseo/paseo/issues/6342 — 2026-10-07 — C

- [Q8] [BUG] `"> I have been trying to import a muse code session on paseo, but it fails every time, claude code sessions work fine."` — getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; L4.
- [Q8] [BUG] `"Importing Claude Code sessions works for the same user."` — getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; L6.
- [Q8] [BUG] ``"- A newly created session’s native ID produced `Invalid plugin provider persistence handle` when passed directly to Paseo’s import adapter, matching the reported error text."`` — getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; comment by paseo-bot[bot], 2026-10-09; L46.
- [Q8] [BUG] `"- The handle returned by Paseo’s session list imported successfully through that adapter."` — getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; comment by paseo-bot[bot], 2026-10-09; L47.
- [Q8] [BUG] ``"The CLI path passes the argument to `decodePersistenceId` in `packages/server/src/server/agent/plugin-provider.ts`, which accepts only the `plugin:`-prefixed handle that the session list returns, so a provider's own session ID is always rejected there."`` — getpaseo/paseo#6342, 2026-10-07; attribution: harness/router-side (provider persistence handle); original app import path unverified; comment by paseo-bot[bot], 2026-10-23; L63.

## gh2/jeong-sik_masc_issues_42597.txt — Muse/Antigravity Start seeds the whole canonical history and exceeds host limits (2026-10-12) / https://github.com/jeong-sik/masc/issues/42597 — 2026-10-12 — C

- [Q8] [BUG] `"Fresh sessions on the Muse and Antigravity lanes seed the entire canonical history and rely on the host to compact it."` — jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); L3.
- [Q6] [BUG] ``"`context compaction replacement still exceeds the hard threshold (1285213 >= 460800 tokens)`"`` — jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); L7.
- [Q8] [BUG] ``"- Each failed attempt persists a ~21 MB poisoned session; the next resume fails with `session/resume (code -32603): response exceeds the outbound frame limit`."`` — jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); L8.
- [Q6] [BUG] ``"- Recovery (`restart_fresh`) re-sends the same oversized seed: infinite fail loop, one ~22 MB session dir per turn (2.1 GB accumulated)."`` — jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); L9.
- [Q11] [BUG] `"Constraint recorded: the fix must not cut or refuse by byte numbers (2026-10-06 operator decision, reaffirmed 2026-10-12). #42598 took the byte-cap approach and is closed."` — jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); comment by jeong-sik, 2026-10-12; L28.
- [Q8] [BUG] `"The failure itself stands: 4.4 MB / 1100-atom seeds fail every fresh muse session."` — jeong-sik/masc#42597, 2026-10-12; attribution: harness/router-side (oversized context seeding/recovery loop); comment by jeong-sik, 2026-10-12; L28.

## gh2/kajal-ranvir_MediSafe_pull_4.txt — fix(intelligence): replace dead Muse Spark key with self-hosted Antigravity gateway (2026-09-22) / https://github.com/kajal-ranvir/MediSafe/pull/4 — 2026-09-22 — C

- [Q8] [BUG] ``"The hosted Muse Spark endpoint (`MUSE_SPARK_BASE_URL=https://api.meta.ai/v1`) now rejects the configured key with **HTTP 401**, so every intelligence call failed: label interpretation, instruction parsing, schedule drafts, the assistant, summaries."`` — kajal-ranvir/MediSafe#4, 2026-09-22; attribution: unclear (configured key rejected 401; no Meta defect proved); L4.
- [Q10] [BUG] `"**Privacy note:** gateway traffic is proxied through the operator's own upstream accounts, so this base-URL switch routes prompt/PHI content differently from the hosted contributor endpoint."` — kajal-ranvir/MediSafe#4, 2026-09-22; attribution: unclear (configured key rejected 401; no Meta defect proved); L37.

## gh2/meta-models_meta-model-cookbook_issues_57.txt — Model API: token logprobs for classification and judging (allow logprobs on the answer with minimal reasoning, or a non-reasoning mode) (2026-10-05) / https://github.com/meta-models/meta-model-cookbook/issues/57 — 2026-10-05 — C

- [Q8] [BUG] ``"- `logprobs: true` is refused whenever reasoning is on, and reasoning can't be turned off:"`` — meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); L8.
- [Q8] [BUG] ``""`logprobs` cannot be true when `reasoning_effort` is `minimal`. logprobs is not supported with reasoning.""`` — meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); L11.
- [Q14] [BUG] `"- The only workaround is sampling the answer k times and counting."` — meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); L14.
- [Q12] [BUG] ``"That is slow and costly on Muse Spark: one call with an 87-token prompt and a one-word answer used **128 reasoning tokens** and took **8.8 s** at `minimal`."`` — meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); L14.
- [Q8] [BUG] `"In our probe (2026-10-04), OpenAI, Together, Fireworks, DeepSeek, OpenRouter and Hugging Face routes returned token logprobs for the same request shape, so judge features built that way don't work on the Meta Model API."` — meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); L16.
- [Q12] [BUG] `"This overlaps with #56, which asks for a non-reasoning, low-latency path for inline suggestions; one mode could serve both."` — meta-models/meta-model-cookbook#57, 2026-10-05; attribution: Meta/Muse-side API capability gap (logprobs with mandatory reasoning); L21.

## gh2/monotykamary_pi-tool-repair_pull_6.txt — feat(grammar): add atem harness leak recovery (2026-10-06) / https://github.com/monotykamary/pi-tool-repair/pull/6 — 2026-10-06 — C

ATEM markup leak observed on this provider/harness route; opening envelope absence prevents reconstruction of a real call in #15737. Native Muse template syntax alone does not prove an output decoding defect in the model.

- [Q8] [BUG] `"Muse Spark models served through tool gateways (observed: muse-spark-1.3-contributor via OpenCode Zen, openai-responses API) sometimes emit their native harness grammar as plain assistant text instead of a structured tool call."` — monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; L2.
- [Q14] [BUG] ``"This adds an opt-in `atem` grammar to the existing grammar-repair pipeline:"`` — monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; L4.
- [Q8] [BUG] ``"- recover complete `<atem:function_calls>` blocks as real toolCall entries (recover mode, known tools only)"`` — monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; L6.
- [Q6] [BUG] ``"- strip the harness namespace (`default.bash` -> `bash`); names without a pi counterpart (`default.todo`) are dropped, never executed"`` — monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; L7.
- [Q8] [BUG] `"- strip dangling markers from truncated streams; ignore fenced code blocks"` — monotykamary/pi-tool-repair#6, 2026-10-06; attribution: unclear upstream origin; harness/router-side repair of ATEM text leak; L8.

## gh2/vllm-project_vllm_pull_62345.txt — [Bugfix][Security] muse: fix quadratic attribute scans in tool-call extraction (2026-10-18) / https://github.com/vllm-project/vllm/pull/62345 — 2026-10-18 — C

- [Q8] [BUG] `"Bound Muse's ATEM attribute scans to a single tag and avoid reparsing tool calls on streaming deltas that cannot complete an invocation."` — vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); L4.
- [Q8] [BUG] ``"The attribute classes previously allowed `<`, so a failed attribute search could restart at each open tag and rescan the remaining suffix."`` — vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); L50.
- [Q8] [BUG] ``"The streaming gate checks a window extending `len(close) - 1` characters before the new delta, so delimiters split across deltas still trigger parsing. `max(previous_count, len(calls))` preserves the emission cursor on deltas that do not parse."`` — vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); L52.
- [Q8] [BUG] `"| Non-streaming | 1849 ms | 0.99 ms | 0.98 ms |"` — vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); L65.
- [Q8] [BUG] `"| Streaming | >25000 ms | 19448 ms | 378 ms |"` — vllm-project/vllm#62345, 2026-10-18; attribution: harness/router-side (inference runtime/parser); L66.

## gh2/yetone_magpie_issues_1448.txt — gateway: Muse Code on Cline's Muse Spark 1.3 free fails with undeclared_tool (Upstream called a tool not declared by the client) (2026-10-09) / https://github.com/yetone/magpie/issues/1448 — 2026-10-09 — C

- [Q6] [BUG] `"model failed: stream protocol error: undeclared_tool: Upstream called a tool not declared by the client (response: resp_6ac97ca6d2ed1e1268fc4a6a)"` — yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L7.
- [Q8] [BUG] ``"- Sandbox repro (temporary HOME, magpie built from main, real muse 1.4.4, a fake chat-completions upstream): when the upstream calls `bogus_tool`, muse doesn't fail."`` — yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L14.
- [Q6] [BUG] ``"It rejects the call as "unknown tool `bogus_tool`", feeds its tool list back to the model and goes on."`` — yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L14.
- [Q8] [BUG] `"A fake upstream that sends this error message mid-stream reproduces the user's error text."` — yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L14.
- [Q8] [BUG] ``"In the repro, a chat-stream error chunk `{"error":{"code":"…","message":"…"}}` reached the client as `server_error`, so its code was lost."`` — yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L36.
- [Q6] [BUG] ``"If Cline's `undeclared_tool` comes from something else (a namespace-level check, a name the model made up, a tool the free tier strips), the patch changes every client's tools and the error stays."`` — yetone/magpie#1448, 2026-10-09; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by yetone, 2026-10-30; L74.

## gh2/yetone_magpie_issues_3152.txt — [Bug] Tool calls fail when model emits whole floats (e.g. limit 8.0) - Codex strict int parsing (2026-10-21) / https://github.com/yetone/magpie/issues/3152 — 2026-10-21 — C

- [Q8] [BUG] `"handle_output_item_done:build_tool_call: error=failed to parse tool_search arguments: invalid number"` — yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L19.
- [Q8] [BUG] ``"failed to parse function arguments: invalid type: floating point `25000.0`, expected u64"`` — yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L31.
- [Q8] [BUG] ``"failed to parse function arguments: invalid type: floating point `73472.0`, expected i32"`` — yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L32.
- [Q8] [BUG] ``"Response-side: canonicalize integral-valued float literals in emitted tool-call arguments before forwarding to Codex (`8.0` -> `8`), same value-preserving rule as #6255."`` — yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; L47.
- [Q12] [BUG] ``"A client that parses its tool arguments strictly (Codex reads `tool_search`'s `limit`, `exec_command`'s `yield_time_ms`/`max_output_tokens`, `write_stdin`'s `session_id` as u64/usize/i32 though its own schemas say `number`) behind magpie, on a model that writes a whole number with a fraction of zeros:"`` — yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by ggbdpq, 2026-10-21; L66.
- [Q8] [BUG] `"Tested the proposed fix end-to-end on Windows 11 with a real Codex + muse-spark session — it resolves the issue for me."` — yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by 1024MrL, 2026-10-23; L108.
- [Q8] [BUG] ``"A number in a tool call's arguments written with a fraction of zeros (`8.0`, `2500.0`, `-3.00`) reaches the agent without the fraction, on relayed and translated replies, streamed or whole."`` — yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by yetone, 2026-10-31; L171.
- [Q14] [BUG] `"6/7 and 20/21 parse errors without the fix, 0 in both runs"` — yetone/magpie#3152, 2026-10-21; attribution: unclear upstream model/provider versus gateway/client contracts; see individual controls; comment by ggbdpq, 2026-10-23; L135. Real-session baseline parse failures versus zero with integral-float normalizer. Gateway/client schema mismatch, not established malformed numeric value from model.
