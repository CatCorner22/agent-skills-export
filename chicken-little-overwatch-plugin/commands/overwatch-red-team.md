---
description: Run the Chicken Little Overwatch red-team swarm (present defects and future design problems) on a file, folder, or plan
argument-hint: "[file-or-folder] [tier T1|T2|T3]"
---

Use the `chicken-little-overwatch` skill in Red team mode on this target: $ARGUMENTS

If the target above is empty, use the file, folder, or text that the user named in this conversation. If the user named nothing, ask for the artifact and its requirements, and stop.

1. Build a short Plan (Step 1): the artifact, the requirements matrix, and the tier. Choose the tier from the stakes, unless the target names one. State the tier and the reason.
2. Launch the attack roles for that tier as separate agents with the launch template in `references/roles.md`: `clo-proofreader`, `clo-style-prosecutor`, `clo-fact-auditor`, `clo-break-it-tester`, `clo-future-analyst`, and `clo-gap-analyst`. Give each role only the artifact, the requirements, and its charter.
3. Send all findings to `clo-arbiter`. At T3, run cross-examination, send each Critical, High, and contested finding to `clo-defender`, collect one finder rebuttal, and ask `clo-arbiter` to rule.
4. Deliver the report in `references/red-team-swarm.md`.

Do not edit the artifact. Do not declare it ready. If your host cannot launch agents, run each role as a separate pass, in order, and state in Flags that one model simulated the swarm.
