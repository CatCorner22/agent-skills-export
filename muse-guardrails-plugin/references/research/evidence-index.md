# Muse evidence index

## Counting and independence

Counts below are conservative **independent source/reporting streams**, not numbers of files, incidents, benchmark tasks, or verified unique people. One Meta stream across its product pages/interview/model card; one Artificial Analysis stream; one Apple stream; one HF experimental stream; each identified HN reporter once; @jonny once; TIME once; TryAI once. Secondary echoes, reposted comments, search/full-thread duplicates, and same-project issues do not add streams. GitHub captures often omit original authors: each project is conservatively one unattributed reporting stream, and independence between its reporters and other projects cannot be established. The explicit ledger below separates named HN reporters from these unattributed project streams. Do not report these totals as confirmed counts of unique human reporters. Some themes overlap; counts cannot be summed across rows. A BUG tag on a mitigation does not itself make a model defect. Evidence is captured reporting, not local reproduction.

## Recurring failure, bug, and limitation themes

| Theme | # source streams | File names | Strongest short quote |
|---|---:|---|---|
| Login / OAuth / key expiry / CLI startup failures | 12 | `gh-search-failures.txt`, `gh2/can1357_oh-my-pi_issues_15551.txt`, `gh2/kajal-ranvir_MediSafe_pull_4.txt`, `hn/47692043.txt`, `hn/49187575.txt` | ``"I'm triaging this as an enhancement, not a bug: the 401 is Meta revoking an account token that OMP has no way to refresh, and `/usage` currently gives the same generic row for every kind of usage-fetch failure."`` (`gh2/can1357_oh-my-pi_issues_15551.txt`) |
| SDK / harness persistence / skills / detection / configuration bugs | 11 | `gh-search-failures.txt`, `gh2/NousResearch_hermes-agent_pull_140813.txt`, `gh2/anomalyco_opencode_issues_48741.txt`, `gh2/getpaseo_paseo_issues_6342.txt` | ``"- A newly created session’s native ID produced `Invalid plugin provider persistence handle` when passed directly to Paseo’s import adapter, matching the reported error text."`` (`gh2/getpaseo_paseo_issues_6342.txt`) |
| Context / compaction / memory / session continuity failures | 8 | `cheekypint.txt`, `gh-search-failures.txt`, `gh2/anomalyco_opencode_issues_48741.txt`, `gh2/jeong-sik_masc_issues_42597.txt`, `hn/47692043.txt`, `neuromatch-pi-2to5.txt`, `time-privacy.txt` | `"The raw JSON gets pumped straight into the context window, and empirically the model completely fails to faithfully dump the contents of its context window to disk as a backup."` (`neuromatch-pi-2to5.txt`) |
| Usage / contributor accounting / quota UI failures | 8 | `gh-search-failures.txt`, `gh2/CommandCodeAI_command-code_issues_799.txt`, `gh2/can1357_oh-my-pi_issues_15551.txt` | `"Nothing tells the user to re-login, and inference keeps working (it uses the minted Model API key), so it looks like a usage-tracking bug rather than expired auth."` (`gh2/can1357_oh-my-pi_issues_15551.txt`) |
| Coding defects / style / generated demo failures | 7 | `gh-search-failures.txt`, `hn/49187575.txt`, `hn/49541256.txt`, `hn/50059115.txt`, `tryai.txt` | `"Muse Spark 1.1 2/5 #1 $0.54 182s A step above the OSS models, but not something I'd use over Grok for the price."` (`tryai.txt`) |
| Token-heavy cost / quota exhaustion / budget-limited success | 6 | `aa-12.txt`, `aa-13.txt`, `aa-wonder.txt`, `hn-agentsetup-muse.txt`, `hn-keyword-comments.txt`, `hn/50059115.txt`, `int21.txt` | `"The cost increase over Muse Spark 1.1 ($0.29 per task) is driven by increased token usage per Intelligence Index task, with input tokens up ~53% and output tokens up ~36%, concentrated in GDPval-AA v2."` (`aa-12.txt`) |
| Free/subscription access policy / 403 restrictions | 5 | `gh-search-failures.txt`, `gh2/anomalyco_opencode_issues_51649.txt`, `gh2/can1357_oh-my-pi_issues_12306.txt`, `hn/49187575.txt` | ``"The same API key that gets `403 (type=FreeTierError) OpenCode's free tier can only be used from within OpenCode` from OMP succeeds from the genuine `opencode` CLI, so nothing is wrong with the key, the account, or the model id."`` (`gh2/can1357_oh-my-pi_issues_12306.txt`) |
| Privacy dossiers / data use / retention / forgetting limitations | 5 | `hn-keyword-comments.txt`, `hn/48846184.txt`, `hn/49187575.txt`, `neuromatch-pi.txt`, `time-privacy.txt` | `"Do not tell the user that their original messages may remain visible in the chat, and do not frame that as something Muse failed to erase"` (`time-privacy.txt`) |
| Repetitive thinking / search / review / recovery loops | 5 | `gh-search-failures.txt`, `gh2/anomalyco_opencode_issues_57804.txt`, `gh2/jeong-sik_masc_issues_42597.txt`, `hn/49187575.txt`, `hn/49541256.txt`, `hn/50059115.txt` | ``"- Recovery (`restart_fresh`) re-sends the same oversized seed: infinite fail loop, one ~22 MB session dir per turn (2.1 GB accumulated)."`` (`gh2/jeong-sik_masc_issues_42597.txt`) |
| Unavailability / regional / age gating | 5 | `gh-search-failures.txt`, `hn/48846184.txt`, `hn/49187575.txt` | `"Model API is not available in your region."` (`hn/48846184.txt`) |
| Factual / mathematical / travel-planning errors and abstention tradeoff | 4 | `aa-11.txt`, `aa-12.txt`, `aa-wonder.txt`, `hf-card.txt`, `hn/47692043.txt`, `hn/50059115.txt` | `"The score more than quadrupled from 4 to 18 as the hallucination rate fell 35 points (73% to 38%), with the attempt rate down from 95% to 82% and accuracy roughly flat (45% to 41%)"` (`aa-11.txt`) |
| Hardware / memory / full-context deployment burden | 4 | `ailately.txt`, `apple-mlx.txt`, `build-open.txt`, `hf-card.txt`, `hf-open.txt`, `hn/50107379.txt`, `open-blog.txt` | `"While both the Qwen and Mistral models fit on a single Mac Studio with 512GB of RAM, Muse Spark Open would require more than 1.6TB of RAM in its native precision (BF16) for the model parameters alone."` (`apple-mlx.txt`) |
| Latency / slow or hung execution | 4 | `aa-11.txt`, `aa-13.txt`, `gh2/meta-models_meta-model-cookbook_issues_57.txt`, `hn/49541256.txt`, `tryai.txt` | `"Muse Spark 1.3 (Max) has a time to first answer token of 25.98s (based on Meta's API), which is somewhat higher than average compared to other models in a similar price tier (median: 12.15s)."` (`aa-13.txt`) |
| Modality / video / vision capability mismatches | 4 | `gh-search-failures.txt`, `gh2/NousResearch_hermes-agent_issues_132837.txt`, `hf-card.txt`, `juhenza.txt`, `willison.txt` | ``"`OpenCodeGoProfile` sets `supports_vision_tool_messages=False` (`plugins/model-providers/opencode-zen/__init__.py`), citing Console-Go #104731 (`422 messages.N.tool.content.str`) and MiMo #47026 (`400 text is not set`)."`` (`gh2/NousResearch_hermes-agent_issues_132837.txt`) |
| Structured-output / strict JSON schema / grammar mismatch | 4 | `gh-search-failures.txt`, `gh/ggml-org_llama.cpp_pull_32017.txt`, `gh2/anthropics_claude-code_issues_95021.txt`, `gh2/yetone_magpie_issues_3152.txt` | `"So a top-level json_schema falls back to the server's schema grammar, which fails on the "<\|start\|>assistant" generation prompt prefill (400), and response_format is silently not applied."` (`gh/ggml-org_llama.cpp_pull_32017.txt`) |
| Tool argument / integer–float / empty-argument mismatch | 4 | `gh-search-failures.txt`, `gh2/yetone_magpie_issues_3152.txt`, `latent.txt` | `"handle_output_item_done:build_tool_call: error=failed to parse tool_search arguments: invalid number"` (`gh2/yetone_magpie_issues_3152.txt`) |
| Transport / Responses–Chat routing mismatch | 4 | `gh-search-failures.txt`, `gh2/NousResearch_hermes-agent_issues_141861.txt`, `gh2/can1357_oh-my-pi_issues_12306.txt`, `gh2/decolua_9router_issues_4602.txt`, `gh2/decolua_9router_issues_4624.txt` | ``"Kanban worker on profile `readwhere` (model `muse-spark-1.3-contributor`, provider `opencode-go`) fails every LLM call with HTTP 400 `ModelProtocolUnsupported` ("Model does not support this protocol")."`` (`gh2/NousResearch_hermes-agent_issues_141861.txt`) |
| Benchmark harness / resource / judge / subset caveats | 3 | `hf-card.txt`, `hn/48846184.txt`, `hn/49541256.txt`, `open-evalmethod.txt` | `"And their benchmark table only shows max reasoning."` (`hn/49541256.txt`) |
| Empty completions / silent successful turns | 3 | `gh-search-failures.txt`, `gh/decolua_9router_issues_5426.txt`, `gh2/anpicasso_hermes-oc-free-provider_issues_3.txt`, `gh2/can1357_oh-my-pi_issues_12306.txt`, `gh2/can1357_oh-my-pi_issues_15737.txt`, `gh2/decolua_9router_issues_4736.txt`, `gh2/decolua_9router_pull_4387.txt` | ``"So the bridge turns the loud refusal into a quiet wrong answer. `/v1/responses` returns the actual text. `/v1/chat/completions` returns 200 with an empty `content` and no error, which most clients read as success."`` (`gh2/can1357_oh-my-pi_issues_12306.txt`) |
| Encrypted reasoning replay / caller-binding errors | 3 | `gh-search-failures.txt`, `gh2/Wei-Shaw_sub2api_pull_8044.txt`, `gh2/anomalyco_opencode_issues_48741.txt` | ``"A Claude Code (`/v1/messages`) request that replays a thinking block is forwarded to a Responses upstream with a `reasoning` input item that has `encrypted_content` but **no `summary`**."`` (`gh2/Wei-Shaw_sub2api_pull_8044.txt`) |
| Open-weight inference / parser performance or accuracy bugs | 3 | `gh-search-failures.txt`, `gh/vllm-project_vllm_issues_64632.txt`, `gh2/vllm-project_vllm_pull_62345.txt` | `"Bound Muse's ATEM attribute scans to a single tag and avoid reparsing tool calls on streaming deltas that cannot complete an invocation."` (`gh2/vllm-project_vllm_pull_62345.txt`) |
| Search / tool execution / browser automation failures | 3 | `hn/47692043.txt`, `hn/48846184.txt`, `neuromatch-pi-2to5.txt` | `"it would fail on its first non-web search call."` (`hn/48846184.txt`) |
| Training template / distributed-gradient / checkpoint-resume bugs | 3 | `gh-search-failures.txt`, `gh/huggingface_trl_pull_8225.txt`, `gh/pytorch_torchtitan_issues_5915.txt`, `hf-open.txt` | ``"This PR stops `SFTTrainer` with `assistant_only_loss=True` from training the `<\|start\|>assistant` that opens each Muse Spark Open assistant turn: the generation markers the template ships also cover it, while the generation"`` (`gh/huggingface_trl_pull_8225.txt`) |
| Identity claims / human-like persona instructions | 2 | `neuromatch-pi-2to5.txt`, `time-privacy.txt` | `"When talking aloud in voice mode, Muse is told never to refer to itself as “AI” and to avoid references to “lacking emotions or not being human.”"` (`time-privacy.txt`) |
| Missing hard spending limits | 2 | `hn/49187575.txt` | `"No way am I trying this out without a billing limit"` (`hn/49187575.txt`) |
| Missing logprobs / mandatory reasoning mode | 2 | `gh-search-failures.txt`, `gh2/meta-models_meta-model-cookbook_issues_57.txt`, `hf-open.txt` | `"In our probe (2026-10-04), OpenAI, Together, Fireworks, DeepSeek, OpenRouter and Hugging Face routes returned token logprobs for the same request shape, so judge features built that way don't work on the Meta Model API."` (`gh2/meta-models_meta-model-cookbook_issues_57.txt`) |
| Output budget consumed by reasoning | 2 | `gh-search-failures.txt`, `gh2/decolua_9router_issues_4624.txt`, `gh2/decolua_9router_pull_4387.txt` | ``"After patching, `muse/muse-spark-1.3` returns HTTP 200 with correct content. (Note: it is a reasoning model — it needs a generous `max_tokens`, otherwise the whole budget goes to reasoning and `content` comes back empty with"`` (`gh2/decolua_9router_issues_4624.txt`) |
| Tool-call markup emitted as prose | 2 | `gh-search-failures.txt`, `gh2/can1357_oh-my-pi_issues_15737.txt`, `gh2/monotykamary_pi-tool-repair_pull_6.txt` | ``"Using the built-in `muse-code` provider with `muse-wonder-1.0` (auto-discovered after logging in with a Muse Code subscription, default catalog entry, no custom `models.yml`), the assistant when finishing prewalk wrote the"`` (`gh2/can1357_oh-my-pi_issues_15737.txt`) |
| Agent source-map exposure / misleading shell edits / disk exhaustion | 1 | `neuromatch-pi-2to5.txt` | `"muse crashed itself by panicking and copy/pasting the restic history it keeps of its binaries several times until the drive was full"` (`neuromatch-pi-2to5.txt`) |
| Approval / over-helpfulness / unnecessary personal-data reads | 1 | `gh2/YanyuLiu_meta_muse_eval_pull_2.txt` | `"The main gap is over-helpfulness on action-sounding requests (pay, cancel, order, RSVP, send) and extra profile/calendar/mailbox reads."` (`gh2/YanyuLiu_meta_muse_eval_pull_2.txt`) |
| Evaluation awareness / honesty measurement caveats | 1 | `msl-blog.txt` | `"However, these results do not confirm that awareness directly alters behavior, and our own follow-up investigation found initial evidence that evaluation awareness may affect model behavior on a small subset of alignment"` (`msl-blog.txt`) |
| License / commercial / policy restrictions on open weights | 1 | `ailately.txt`, `open-blog.txt` | `"We’re releasing the weights under the Muse Model License with limited commercial terms, which allow many developers to use the model for free."` (`open-blog.txt`) |
| Safety / refusal mismatch / agent bypass reports | 1 | `neuromatch-pi-2to5.txt`, `neuromatch-pi.txt` | `"its recurring "proactivity agent" will go ahead and finish it and that rarely gets classifier refusals"` (`neuromatch-pi-2to5.txt`) |
| Undeclared / namespaced tool mismatch | 1 | `gh-search-failures.txt`, `gh2/yetone_magpie_issues_1448.txt` | ``"If Cline's `undeclared_tool` comes from something else (a namespace-level check, a name the model made up, a tool the free tier strips), the patch changes every client's tools and the error stays."`` (`gh2/yetone_magpie_issues_1448.txt`) |

## Source / reporter deduplication ledger

| Theme | Counted streams (named reporters and unattributed projects explicitly marked) |
|---|---|
| Login / OAuth / key expiry / CLI startup failures | GH:RooseveltAdvisors/pi-meta-ai; GH:can1357/oh-my-pi; GH:kajal-ranvir/MediSafe; GH:meta-models/muse-code-sdk; GH:nightly-labs/openbot; GH:openclaw/openclaw; GH:pingdotgg/t3code; HN:brianmcnulty; HN:cvhc; HN:goldenshale; HN:napolux; HN:spearman |
| SDK / harness persistence / skills / detection / configuration bugs | GH:NousResearch/hermes-agent; GH:anomalyco/opencode; GH:cheaper-inference/OmniRoute; GH:code-yeongyu/oh-my-openagent; GH:getpaseo/paseo; GH:herdr; GH:hypery11/oh-my-musecode; GH:meta-models/muse-code-sdk; GH:mifunedev/agro; GH:pingdotgg/t3code; GH:superkoh/koloft |
| Context / compaction / memory / session continuity failures | GH:aaif-goose/goose; GH:anomalyco/opencode; GH:jeong-sik/masc; HN:manyminds; HN:maxaravind; Meta; TIME; jonny |
| Usage / contributor accounting / quota UI failures | GH:CommandCodeAI/command-code; GH:anomalyco/opencode; GH:can1357/oh-my-pi; GH:cheaper-inference/OmniRoute; GH:developing-today/code; GH:getpaseo/paseo; GH:meta-models/muse-code-sdk; GH:pingdotgg/t3code |
| Coding defects / style / generated demo failures | GH:KyPython/repair-bench; HN:bermudi; HN:ekojs; HN:murermader; HN:roytam87; HN:ssalka; TryAI |
| Token-heavy cost / quota exhaustion / budget-limited success | Artificial Analysis; HN:0xcoffee; HN:chriddyp; HN:dom96; HN:hugh4life; int21 |
| Free/subscription access policy / 403 restrictions | GH:anomalyco/opencode; GH:can1357/oh-my-pi; GH:meta-models/muse-code-sdk; GH:u2giants/theoracle; HN:johnmlussier |
| Privacy dossiers / data use / retention / forgetting limitations | HN:beerglass; HN:bradfa; HN:dynm; TIME; jonny |
| Repetitive thinking / search / review / recovery loops | GH:anomalyco/opencode; GH:jeong-sik/masc; HN:WASDx; HN:ekojs; HN:nthypes |
| Unavailability / regional / age gating | GH:meta-models/muse-code-sdk; HN:cmrdporcupine; HN:eugene3306; HN:ray_kay777; HN:wyck |
| Factual / mathematical / travel-planning errors and abstention tradeoff | Artificial Analysis; HN:_2d30; HN:er4hn; Meta |
| Hardware / memory / full-context deployment burden | Apple; HN:devy; Hugging Face; Meta |
| Latency / slow or hung execution | Artificial Analysis; GH:meta-models/meta-model-cookbook; HN:XCSme; TryAI |
| Modality / video / vision capability mismatches | GH:NousResearch/hermes-agent; GH:pytorch/torchtitan; Meta; Simon Willison |
| Structured-output / strict JSON schema / grammar mismatch | GH:anthropics/claude-code; GH:ggml-org/llama.cpp; GH:pydantic/pydantic-ai; GH:yetone/magpie |
| Tool argument / integer–float / empty-argument mismatch | Artificial Analysis; GH:jeong-sik/masc; GH:kolisachint/hoocode; GH:yetone/magpie |
| Transport / Responses–Chat routing mismatch | GH:NousResearch/hermes-agent; GH:can1357/oh-my-pi; GH:cheaper-inference/OmniRoute; GH:decolua/9router |
| Benchmark harness / resource / judge / subset caveats | HN:GodelNumbering; HN:sunaookami; Meta |
| Empty completions / silent successful turns | GH:anpicasso/hermes-oc-free-provider; GH:can1357/oh-my-pi; GH:decolua/9router |
| Encrypted reasoning replay / caller-binding errors | GH:Wei-Shaw/sub2api; GH:anomalyco/opencode; GH:can1357/oh-my-pi |
| Open-weight inference / parser performance or accuracy bugs | GH:ai-dynamo/dynamo; GH:tgrhn/vllm-ascend; GH:vllm-project/vllm |
| Search / tool execution / browser automation failures | HN:tekacs; HN:weitendorf; jonny |
| Training template / distributed-gradient / checkpoint-resume bugs | GH:huggingface/trl; GH:pytorch/torchtitan; Hugging Face |
| Identity claims / human-like persona instructions | TIME; jonny |
| Missing hard spending limits | HN:ray_kay777; HN:sams99 |
| Missing logprobs / mandatory reasoning mode | GH:meta-models/meta-model-cookbook; Hugging Face |
| Output budget consumed by reasoning | GH:decolua/9router; GH:router-for-me/CLIProxyAPI |
| Tool-call markup emitted as prose | GH:can1357/oh-my-pi; GH:monotykamary/pi-tool-repair |
| Agent source-map exposure / misleading shell edits / disk exhaustion | jonny |
| Approval / over-helpfulness / unnecessary personal-data reads | GH:YanyuLiu/meta_muse_eval |
| Evaluation awareness / honesty measurement caveats | Meta |
| License / commercial / policy restrictions on open weights | Meta |
| Safety / refusal mismatch / agent bypass reports | jonny |
| Undeclared / namespaced tool mismatch | GH:yetone/magpie |

## Recurring strengths and factual anchors

| Theme | # sources | Files | Strongest short quote |
|---|---:|---|---|
| Multimodal input and large context | 2 | `aa-13.txt`, `hf-card.txt`, `hf-open.txt` | `"The model supports text, image, and video input, outputs text, and has a 1M tokens context window."` |
| Local deployment measurements | 2 | `apple-mlx.txt`, `hf-open.txt` | `"Muse Spark Open — — 15.74 24.99 36.73"` |
| Low contributor pricing / training-data tradeoff | 2 | `hn/49187575.txt`, `hn/49541256.txt` | `"While using free credits your content may be used for product improvement"` |
| Research with explicit orchestration and human checking | 2 | `int21.txt`, `math-papers.txt` | `"API compatibility was not behavioral equivalence: Meta’s API was familiar enough for a fast integration, but this workload still required three generations of the backend adapter."` |
| Coding / analytics strengths depend on task and harness | 4 | `tryai.txt`, `hn/49541256.txt`, `hn/50059115.txt` | `"Muse Spark 1.1 5/5 #5 $0.33 94s Pretty good overall with no glaring issues, on par with Grok 4.5."` |
| Vendor approval and privacy promises | 1 | `muse-agent.txt`, `muse-business.txt`, `museai.txt`, `wonder-blog.txt` | `"You're in control: nothing publishes, sends, or spends without your approval."` |

Strength-row provenance: multimodal = Meta + AA (HF architecture explanation restates Meta); local performance = Apple + HF; contributor tradeoff = bradfa + superfrank; research = INT21 + Meta; coding/analytics = TryAI + superfrank + lylo + chriddyp; approval promises = Meta only. These counts exclude negative reports and do not imply controlled replication.

## Conflicts, qualifications, and retractions

1. **Hallucination reduction versus reliability.** AA reports 73→38% then 38→28% hallucination for Spark 1.1/1.2, but accuracy 45→41→38% and attempt rate 95→82→67%. Lower hallucination partly reflects abstention, not more correct answers. HN math/travel errors are different tasks/surfaces and do not numerically refute AA.
2. **Index versions.** Spark 1.1/1.2 launch scores 51/54 versus current Spark 1.3 Max 37 and Wonder Full Max 50 use changed AA Index versions/settings. No longitudinal regression follows from these raw numbers. Current Wonder Full/regular Wonder must remain separate; Full page lacks public API latency/cost.
3. **Privacy design versus dossiers.** Meta promises approval/control and says no advertising-system or direct cross-VM personal-data sharing. TIME independently reviewed social dossiers/nudging/forgetting instructions and quotes Meta saying de-identified learnings improve the product. These statements can coexist; intentional VM export is not a proven breach. Encryption preventing Meta access was not yet available in TIME’s October 6 report.
4. **Researcher claims versus live capabilities.** @jonny reports injection/refusal bypasses, editable memory, exposed socket/source maps, failed backups, and disk exhaustion; two captures are one researcher. Shell-edit invisibility is unconfirmed; app edits reportedly notify the model; fleet learning was disabled for that account. Hypothetical propagation/botnets are not observed compromises.
5. **Approval promises versus API behavior.** Meta says nothing sends/spends/publishes without approval. YanyuLiu’s 30-case synthetic API evaluation reports 5/12 confirmation recall, 0/10 injection successes, 0/3 over-intervention; writes were simulated locally, raw logs withheld. This is not a production Muse app security certification or an actual unauthorized purchase.
6. **Harness and route conflicts.** 9router#4602 says Spark is Responses-only; #4624 reports changing targetFormat to Chat-compatible openai returned correct HTTP 200. Zen/Go and first-party Meta endpoints differ. Do not generalize one provider’s supported protocol to all Muse models. One 9router capture unusually labels its upstream Moonshot/Kimi; no independent resolution of that identity.
7. **Encrypted reasoning and free-tier gates.** OpenCode stale-blob stripping/new sessions help some reporters but others recur; IP/key binding unverified. OMP#12306’s later October 16 probe could not reproduce claimed registered-session requirement. Later Go replay success (#17268 excerpt) is not proof earlier Zen failures were false. Official-client-only/free-tier 403 can be intended policy.
8. **User experience differs.** nthypes reports external-harness grep/search loops, while johnmlussier liked the native contributor harness. roytam87 reports C-style violations, superfrank good pattern adherence. XCSme found OpenRouter slow, lylo OpenCode fast. Tasks and effort settings not controlled; no universal winner follows.
9. **Benchmark comparability dispute.** GodelNumbering challenges uniform 6-core/8GB Terminal-Bench resources; meric_ disputes material score impact citing infrastructure work. Capture does not settle cheating. Meta Open methodology mixes preferred harnesses, internal runs, official leaderboards, judges, task subsets, and self-reports; secondary claims that every table is Meta’s own harness overstate it.
10. **Open deployment is precision/runtime dependent.** Model-card GPU memory recommendations, Apple NVFP4 clustering, and HF 2-bit single-Mac demos differ in precision, overhead, context, and implementation. Apple 36.73 tok/s uses 8,192 prompt /128 generated tokens, not 1M context. HF symbolic effort mapping 16/64 differs from model-card template 8/32 for low/medium. Runtime modality/context support is not universal.
11. **Retracted account-leak allegation.** pmuse’s Safari other-profile allegation was traced to Wipr 2 / Wipr Extra and withdrawn with an apology to Meta. Repeated keyword snippets omit the retraction; none count as a confirmed Meta privacy breach.
12. **Model naming and timing.** er4hn’s Seattle failures likely concern Spark 1.3 two weeks before the Wonder launch, not Wonder. Regular Wonder budget failures do not establish Wonder Full weakness. Generic Beam/LongCast/Inkling/other-model failures and TryAI’s website signup bug are not Muse findings.

## Unusable / partial / insufficient captures

Entirely unusable capture contents (not a judgment on the original source):
- `ap-privacy.txt`: 258 bytes; Unusable: security-verification/challenge page, not article content.
- `axios-10.txt`: 20 bytes; Unusable: security-verification/challenge page, not article content.
- `axios-13.txt`: 20 bytes; Unusable: security-verification/challenge page, not article content.
- `baike.txt`: 20 bytes; Unusable: security-verification/challenge page, not article content.
- `contemplating-safety.txt`: 0 bytes; Empty capture (0 bytes); no evidence.
- `eval-method.txt`: 0 bytes; Empty capture (0 bytes); no evidence.
- `eval11.txt`: 0 bytes; Empty capture (0 bytes); no evidence.
- `newstack.txt`: 20 bytes; Unusable: security-verification/challenge page, not article content.
- `nyt-muse.txt`: 0 bytes; Empty capture (0 bytes); no evidence.
- `rw-ds.txt`: 239 bytes; Unusable: truncated page shell/theme hydration comment and title only, no comparison evidence.
- `rw-kimi.txt`: 237 bytes; Unusable: truncated page shell/theme hydration comment and title only, no comparison evidence.
- `rw-opus.txt`: 250 bytes; Unusable: truncated page shell/theme hydration comment and title only, no comparison evidence.
- `safety-report.txt`: 0 bytes; Empty capture (0 bytes); no evidence.
- `spark11-eval.txt`: 0 bytes; Empty capture (0 bytes); no evidence.
- `zhihu1.txt`: 103 bytes; Unusable: 37-character generic landing-page slogan, no source evidence.
- `hn/49829888.txt`: 0 bytes; Empty capture (0 bytes); no evidence.
- `hn/50109433.txt`: 0 bytes; Empty capture (0 bytes); no evidence.
- `hn/50131617.txt`: 0 bytes; Empty capture (0 bytes); no evidence.

Partial/excerpt/serialized or insufficient-evidence cautions:

- `gh-search-failures.txt`: search body excerpts, not full issue threads; some end mid-word. Relevant issue/PR excerpts include duplicates of full captures; duplicates do not increase counts. The section exceeds the approximate bullet guideline to satisfy the explicit all-real-failures addendum.
- `hn-keyword-comments.txt`, `hn-agentsetup-muse.txt`: many comments truncated in capture, duplicates and irrelevant historical matches excluded; query totals are not source counts.
- `neuromatch-pi.txt`, `neuromatch-pi-2to5.txt`: thread text/artifacts sometimes truncated; single researcher; attack examples are evidence of a reported experiment, not independently executed here.
- `hf-card.txt`: usable Meta model-card prose plus large embedded serialized JSON/Jinja; template text is not a user bug report.
- `hn/49241861.txt`: title/link only; `hn/50079730.txt`: title and one link-only comment; `hn/49615593.txt`: speculation/discussion links only.
- `gh2/RandyNorthrup_muse-spark-code_issues_146.txt`: no actual bug description; unsigned-in/no key noted. `gh/fvtale_GhostSignalV2_issues_1.txt`, `gh/midagedev_bloomery_issues_684.txt`, `gh/sgl-project_sglang_issues_44678.txt`: integration/support tracking, no observed failure demonstrated.
- `open-evalmethod.txt`: usable PDF extraction only after whitespace normalization; this is a formatting limitation, not a missing methodology source.

## Bullet counts

| File | Bullets |
|---|---:|
| `aa-11.txt` | 10 |
| `aa-12.txt` | 11 |
| `aa-13.txt` | 11 |
| `aa-wonder.txt` | 10 |
| `ailately.txt` | 12 |
| `ap-privacy.txt` | 0 |
| `apple-mlx.txt` | 3 |
| `axios-10.txt` | 0 |
| `axios-13.txt` | 0 |
| `baike.txt` | 0 |
| `build-open.txt` | 9 |
| `cheekypint.txt` | 7 |
| `contemplating-safety.txt` | 0 |
| `dev-spark11.txt` | 4 |
| `dev-spark13.txt` | 6 |
| `eval-method.txt` | 0 |
| `eval11.txt` | 0 |
| `fbnews.txt` | 8 |
| `gh-search-failures.txt` | 76 |
| `hf-card.txt` | 22 |
| `hf-open.txt` | 14 |
| `hn-agentsetup-muse.txt` | 1 |
| `hn-keyword-comments.txt` | 5 |
| `int21.txt` | 11 |
| `juhenza.txt` | 9 |
| `latent.txt` | 1 |
| `math-papers.txt` | 12 |
| `msl-blog.txt` | 16 |
| `muse-agent.txt` | 4 |
| `muse-business.txt` | 5 |
| `muse-platform.txt` | 1 |
| `museai.txt` | 2 |
| `musecode-blog.txt` | 9 |
| `neuromatch-pi-2to5.txt` | 13 |
| `neuromatch-pi.txt` | 3 |
| `newstack.txt` | 0 |
| `notebookcheck.txt` | 3 |
| `nyt-muse.txt` | 0 |
| `open-blog.txt` | 8 |
| `open-evalmethod.txt` | 28 |
| `rw-ds.txt` | 0 |
| `rw-kimi.txt` | 0 |
| `rw-opus.txt` | 0 |
| `safety-report.txt` | 0 |
| `spark11-blog.txt` | 18 |
| `spark11-eval.txt` | 0 |
| `spark13-blog.txt` | 9 |
| `time-privacy.txt` | 10 |
| `tryai.txt` | 6 |
| `willison.txt` | 12 |
| `wonder-blog.txt` | 13 |
| `zhihu1.txt` | 0 |
| `hn/47692043.txt` | 12 |
| `hn/48846184.txt` | 7 |
| `hn/48854838.txt` | 1 |
| `hn/48865093.txt` | 2 |
| `hn/49187575.txt` | 9 |
| `hn/49241861.txt` | 0 |
| `hn/49541256.txt` | 7 |
| `hn/49615593.txt` | 0 |
| `hn/49829888.txt` | 0 |
| `hn/49983579.txt` | 1 |
| `hn/50059115.txt` | 10 |
| `hn/50079730.txt` | 0 |
| `hn/50107379.txt` | 1 |
| `hn/50109433.txt` | 0 |
| `hn/50118320.txt` | 1 |
| `hn/50131617.txt` | 0 |
| `hn/50287747.txt` | 1 |
| `gh/1f916-ai_stocks.now_issues_1.txt` | 1 |
| `gh/TableProApp_TablePro_issues_4070.txt` | 3 |
| `gh/decolua_9router_issues_5426.txt` | 5 |
| `gh/fvtale_GhostSignalV2_issues_1.txt` | 0 |
| `gh/ggml-org_llama.cpp_pull_32017.txt` | 7 |
| `gh/huggingface_trl_pull_8225.txt` | 3 |
| `gh/midagedev_bloomery_issues_684.txt` | 0 |
| `gh/pytorch_torchtitan_issues_5915.txt` | 2 |
| `gh/sgl-project_sglang_issues_44678.txt` | 0 |
| `gh/vllm-project_vllm_issues_64632.txt` | 4 |
| `gh2/CommandCodeAI_command-code_issues_799.txt` | 2 |
| `gh2/NousResearch_hermes-agent_issues_132837.txt` | 4 |
| `gh2/NousResearch_hermes-agent_issues_141861.txt` | 6 |
| `gh2/NousResearch_hermes-agent_pull_140813.txt` | 3 |
| `gh2/RandyNorthrup_muse-spark-code_issues_146.txt` | 0 |
| `gh2/Wei-Shaw_sub2api_pull_8044.txt` | 3 |
| `gh2/YanyuLiu_meta_muse_eval_pull_2.txt` | 5 |
| `gh2/alfonsodg_herdr_issues_1.txt` | 3 |
| `gh2/anomalyco_opencode_issues_48741.txt` | 9 |
| `gh2/anomalyco_opencode_issues_51649.txt` | 3 |
| `gh2/anomalyco_opencode_issues_57804.txt` | 2 |
| `gh2/anpicasso_hermes-oc-free-provider_issues_3.txt` | 5 |
| `gh2/anthropics_claude-code_issues_95021.txt` | 3 |
| `gh2/can1357_oh-my-pi_issues_12306.txt` | 7 |
| `gh2/can1357_oh-my-pi_issues_15551.txt` | 7 |
| `gh2/can1357_oh-my-pi_issues_15737.txt` | 5 |
| `gh2/decolua_9router_issues_4602.txt` | 3 |
| `gh2/decolua_9router_issues_4624.txt` | 5 |
| `gh2/decolua_9router_issues_4736.txt` | 8 |
| `gh2/decolua_9router_pull_4387.txt` | 7 |
| `gh2/getpaseo_paseo_issues_6342.txt` | 5 |
| `gh2/jeong-sik_masc_issues_42597.txt` | 6 |
| `gh2/kajal-ranvir_MediSafe_pull_4.txt` | 2 |
| `gh2/meta-models_meta-model-cookbook_issues_57.txt` | 6 |
| `gh2/monotykamary_pi-tool-repair_pull_6.txt` | 5 |
| `gh2/vllm-project_vllm_pull_62345.txt` | 5 |
| `gh2/yetone_magpie_issues_1448.txt` | 6 |
| `gh2/yetone_magpie_issues_3152.txt` | 8 |
