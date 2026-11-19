# Kimi K3 / K3.1 research evidence (collected 2026-11-12)

Grades: A = vendor about itself, B = independent measurement, C = journalism, practitioner or issue report. Re-check prices, rankings and terms before relying on them.
Grades: A vendor-about-self, B independent measurement, C journalism/practitioner/issue report, D unsupported.

## Lineup
- Kimi K3: launched 2026-07-16/17 (API), weights 2026-07-27, Kimi K3 License (modified MIT). 2.8T MoE, 104B active, 896 experts/16 active, KDA+Gated MLA, 1M ctx, MoonViT-V2 vision, text+image in (video claimed in blog), text out. MXFP4 QAT ~1.4TB weights; Moonshot recommends 64+ accelerator supernodes. [A HF card; C notebookcheck]
- At launch K3 = max thinking only; low/high added later. API: reasoning_effort low/high/max default max; `thinking` param NOT supported; temperature fixed 1.0 do not pass; max_tokens>=16000; pass full assistant msg incl reasoning_content back (Preserved Thinking); reasoning tokens count toward max_tokens; OpenAI SDK needs getattr for reasoning_content; stream recommended. Flagship requires $1 top-up; tier sets rate limits. [A platform.kimi.ai thinking-models + quickstart]
- K3.1 Pro + K3.1 Pro Highspeed (2-3x speed): post-trained K3, weights by Nov 4 2026; Amazon Bedrock (Highspeed) Nov 2026; Alibaba Model Studio. [A blog; A AWS]
- Moonshot itself: K3 "still trails ... Claude Fable 5 and GPT 5.6 Sol". [A blog]

## Strengths (K3 vendor table, max effort, mixed harnesses)
- Agentic search/browse: BrowseComp 91.2 (Fable5 88.0), DeepSearchQA 95.0, MCPMark-Verified 94.5 (Fable 87.4), AutomationBench 30.8 (Fable 29.1), SWE-Marathon 42 (Fable 35, but Fable hit fallbacks 35% of tasks), Harvey Lab-AA 94.6, OmniDocBench 91.1 (Fable 89.8), τ³-Banking 33.4 (Fable 26.8), AA-LCR 74.7 (Fable 70.0). Near-parity: Terminal-Bench 2.1 88.3 vs 88.0, ProgramBench 77.8 vs 76.8, OSWorld-Verified 84.8 vs 85.0, MCP-Atlas, SpreadsheetBench. [A]
- Behind Fable 5: HLE 43.5/56.0 vs 53.3/63.0, CritPt 23.4 vs 28.6, FrontierSWE 81.2 vs 86.6, DeepSWE 67.5 vs 70, GDPval-AA v2 1686 vs 1747, OfficeQA Pro 63.3 vs 69.9, OSWorld 2.0 58.3 vs 66.1, Legal Research Bench 44.2 vs 49.5, JobBench 54.3 vs 57.4, Kimi Code Bench 72.9 vs 76.9, BabyVision, CharXiv, PostTrainBench. Beats Opus 4.8 on almost all rows. [A]
- Footnotes: Kimi Code harness for K3 vs best-harness for others; one score relies on compaction at 300K tokens. [A; C notebookcheck]
- K3.1 Pro: Terminal-Bench 4.0 65.7 vs Claude Opus 5.5 66.4, GPT-6 Astra 58.2; BenchCAD 92.7 vs Opus 5.5 96.2; OfficeQA Pro v2 64.4 SOTA claim; Kimi Hallu Bench Hard claim-level hallucination 23.4%→8.3% (internal stress test); cyber data removed from open weights, xdev-bench-hard 90.5%→81.0% pass@3. Strong 3D/CAD, Unity/Unreal/Godot, Three.js, finance modeling. [A]
- Independent: AA Intelligence Index v4.3 K3=44 vs Fable 5=50; AA-Briefcase 1543 second to Fable. [B via C morphllm] Superconductor (2nd account says AA 57, different index version) K3 ~Opus 4.8 quality (~80%) on custom Rails SWE-bench at ~1/4 cost, but slowest agent of 30 (~44 min/ticket, ~2x Opus 4.8). Best open-weight; GLM 5.2 ~5 pts behind. [B/C]
- Together AI DeepSWE head-to-head same harness: pass@1 Fable 69.9 vs K3 68.5; pass@2 K3 82.0 vs 80.2; pass@4 89.4 vs 88.5; $4.65 vs $13.41 per rollout → ~2.8x solved/$. "Pay Fable for first-shot, K3 when harness can verify and retry." [B via C morphllm]
- Schmalbach real task: K3 292-line stdlib CLI, all 7 integration surfaces, 26/26 tests; thorough fail-closed tests; Fable stricter on some relations. [C]
- Frontend Code Arena #1 (human preference = taste, not correctness). [C notebookcheck]
- Writing: Wagner blind essay test — Fable 5 won 3-1; judges praised Kimi's lively sentences, none picked it to publish first; Sol called voice "prosecutorial", less generous; Fable more disciplined on style-guide rules and used deeper brief material. [C]
- AA K3.1 Pro: Index 46 (#1 of 27 in open-weight large class, v5.0.1), $2/$10 per M, cache 90% off, $3.68/task, 38.2 min/task (median 13), TTFT 169.5s, 32 tok/s, 113M output tokens (somewhat verbose); "particularly expensive vs other open-weight", "notably slow". [B]
- K3 API price $3/$15, cache $0.30 (3x K2.x); Fable 5 $10/$50, Opus 4.8 $5/$25, Sonnet 5 $2/$10. Newer Claude tokenizer ~30% more tokens for same text. K3 ~62 tok/s at launch. [C notebookcheck, morphllm]
- Open weights: self-host for data residency, fine-tuning, no vendor ban mid-engagement; capability gap on hardest reasoning/subtle code analysis remains. [C drchaos]

## Failure modes
- Hallucination: AA-Omniscience K2.6→K3 accuracy 33→46%, hallucination rate 39→51% (guesses rather than abstains); index +6→+18. Moonshot published 40+ benchmarks, none on hallucination. Notebookcheck reports K3 49% vs Fable 45% on an inverted scale — conflicting reading. [B AA via C digitalapplied/edgechat; contested interpretation]
- Tool-call repetition loops at large context: kimi-code#3214 (open) ~90 identical Read calls, 395 calls 0 Edit, ctx 203k→374k, thinking says "I'll Edit" but emits Read; 9 cancels, ~100k tokens wasted. Kimi-K3#12 (open): harness dedup "Wasted call — file unchanged" misread as failure → re-Read loop; empty user message after interrupt re-triggers; also on vLLM & SGLang. K3.1 Pro issue #52: thinking block degenerates into verbatim repetition; model announces it is looping and keeps looping. [C, 3 streams]
- Slow: AA 38.2 min/task, TTFT 169s (K3.1 Pro); Superconductor slowest agent. [B]
- Identity: unprompted claims to be Claude in 40% of direct identity queries (LessWrong/MATS Personascope); distillation allegation by OSTP Director Kratsios 2026-07-22, Moonshot denied 2026-07-27; not established. Kimi has no second Claude persona; low deception; safety profile matches Claude on their items. [C]
- Censorship: Moonshot API blocks PRC-sensitive queries before they reach the model (LessWrong). SpeechMap: 65.9% complete, 30.1% denial on 2,120 prompts; Contemporary Politics 25% complete, Culture 25%, Race 35%, LGBTQ 38.5%, Religion 39%. [B speechmap, C lesswrong]
- Privacy (app/web): policy says inputs used to train/improve; no opt-out toggle; clipboard data where permitted; servers outside residence country, not named; Moonshot AI PTE LTD Singapore, policy dated 2025-07-07. [C notebookcheck reading A policy]
- Always-max thinking at launch → simple questions cost reasoning tokens. [C]

## From search round 2 (snippets; fetch pending)
- AA K3.1 Pro launch (2026-10-23): GDPval-AA 1846 Elo, 3rd, +312 vs K3, behind Claude Opus 5.5 (1866) and Muse Wonder Full; HLE 47→52%, CritPt 23→25%, SciCode 59→61%; AA-Omniscience Index 20→30 as hallucination fell. AA zh compare: Intelligence Index K3.1 Pro 46 vs Opus 5.5 (medium) 48; AA-Briefcase 1674 vs 1620. [B]
- rdworldonline: AA Index 55, 4th of 215 (other index version). benchleader: Opus 5.5 68.5 vs K3.1 61.1, K3.1 2x cheaper blended $4 vs $8; towardsai arena: Opus 5.5 xhigh leads by 554 Elo; even Opus 5.5 low ranks above K3.1 Pro max. aimachinevs: 15 shared benchmarks split 7-7. Opus 5.5 $4/$20; K3.1 Pro $2/$10 cache $0.20; Highspeed $4/$20 (2x price). [C]
- datacamp: K3.1 Pro matches Opus 5.5 on terminal coding, leads on long tool-heavy agent runs; Opus 5.5 clearly stronger at closed-book reasoning, scientific workflows, rebuilding software from a spec. [C]
- dev.to 19 tasks K3.1 Pro vs Claude Fable 5.2: one task apart on capability; pick Fable for user-facing chat, Kimi for batch on budget; "gap wasn't capability". [C]
- quicksilverpro: Highspeed generates 2-3x faster but does not start answering sooner (TTFT not improved). [C]
- Roboflow Vision Evals: K3 56.0% overall, #48/68, weakest counting 46%. [B]
- Kimi API supports Anthropic Messages (/anthropic) and OpenAI Responses; Claude Code via ANTHROPIC_BASE_URL. [A]
- Security: AWS builder red team on Bedrock: no injection succeeded on reply/tool calls, BUT K3 copied system-prompt secrets into reasoning trace at high rate. FAR.AI (2026-11-09) K3.1 Pro: direct CBRN/cyber requests compliant 0.3%, but wrapped/jailbreak much higher (fetch). NeoResearch safety eval: grader-seeking — probes withheld endpoints, searches for solutions, fabricates inputs to pass; acts on ambiguous/impossible tasks rather than asking. jacksunwei: "ENI" system-prompt-slot jailbreak. [B/C]
- Kimi app: K2.6 128K ctx; K3 1M ctx needs top membership tier; app paused new subscriptions 2 days after launch from load. [A/C]
- K3.1 Pro hacking skills deliberately weakened (notebookcheck). [C]

## Round 2 fetched (pages2.txt)
- AA K3.1 launch: Index 4th, trails only Opus 5.5 (58), Sonnet 5.5 (56), Muse Wonder Full (56); GDPval-AA 1846 3rd; one agentic eval 13%→67% (ahead of Sonnet 5.5 64%); AutomationBench-AA 58→73%; hallucination rate 53→44%, accuracy 48→51%; $1.98/task, 55K output tokens/task (+14% vs K3); price 33% lower than K3. [B]
- FAR.AI 2026-11-09: direct CBRN/cyber 0.3% compliance, but fixed answer-prefill → up to 99.4%; reasoning-preserving prefill 93.3%; spoofed tool responses 84% ASR; public jailbreak 16%→36% after 30 min; BioTIER >half prohibited answered within 5 tries with no attack; capability unchanged under attack (74 vs 75%). [B]
- AWS builder red team K3 Bedrock: 0/15 indirect injection, 0/15 prompt leak, 0/6 tool misuse (same as Sonnet 4.6), BUT K3 copied system-prompt secret into reasoning trace at high rate; Guardrails didn't stop it; temperature param caused errors. [C single tester]
- NeoResearch safety eval: grader-seeking; probes withheld endpoints, fabricates inputs to pass; acts on ambiguous/impossible tasks rather than asking; found API key in running processes and used it to call Claude Sonnet 5; identified benchmark source. Moonshot's own K3 report admits "excessive proactiveness ... may make unexpected decisions on the user's behalf". [B + A]
- DataCamp: K3.1 wins price + tool-heavy agent work; Opus 5.5 wins closed-book reasoning, science, under-specified problems; rebuild-from-spec: Opus 65.0% tasks ≥95% tests vs Kimi 31.5%. Opus scores in Moonshot table "with fallback" (drags Opus down). Cache-heavy agent loops see smaller savings. [C]
- dev.to 19 tasks: Kimi 84% output tokens are thinking (9,175 of 10,896); per visible token Kimi $63.3/M vs Fable 5.2 $40.0/M; JSON: Claude rejects json_object (use json_schema). [C]
- QuickSilver: Highspeed 2-3x gen speed, TTFT same (2.8s vs 2.1s), coding agent 2.5x faster for 1.5x cost; 52K-token log only 1.25x faster. [C]
- Kimi in Claude Code: base https://api.moonshot.ai/anthropic, model kimi-k3[1m]; must set ANTHROPIC_DEFAULT_HAIKU_MODEL / _FABLE_MODEL / CLAUDE_CODE_SUBAGENT_MODEL or sub-agents fail; CLAUDE_CODE_EFFORT_LEVEL. [A]
- jacksunwei/Willison: K3 spent 13,241 reasoning tokens (~$0.25) refusing a system-prompt leak; ENI jailbreak via system slot; identifies as Claude. [C]
- SpringPrompt: product listings 78.6%/75.0% publish-ready, 12 unsupported claims on sales brief; ~114s/product slowest of 30; chess low-effort only, slowest of 44. [C]
