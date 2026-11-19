# Adversarial analysis

Nature does not aim at you; adversaries do. Adversarial analysis asks who gains when the plan fails, and how they would make it fail. Run it after the 4 quadrants, because the quadrants give the adversary its map.

## Rules

- **AD1 Model, do not caricature.** Give each adversary real capabilities, limits, costs, and incentives. An adversary with unlimited power produces no useful finding.
- **AD2 Free play.** Let the adversary pick the target, the timing, and the method. Do not restrict it to the paths that the defenders already watch.
- **AD3 Evidence.** Each attack path needs a location in the plan, the precondition it exploits, and the step at which a defender could notice it.
- **AD4 Independence.** If your host can run separate agents, give each adversary model to a separate agent that sees only the plan and its own charter. Otherwise, run each model as a separate pass and say so.
- **AD5 Honest limits.** State which adversaries you did not model and why.

## Adversary models

Run every model that fits the artifact. State the ones you skip and why.

| Model | Goal | First questions |
|---|---|---|
| Competitor | Take the customers, the staff, the suppliers, or the price | What does our plan make cheap for a rival to copy or undercut? Which dependence can a rival buy or block? |
| Insider | Gain money, cover an error, or settle a score, with legitimate access | Which control can 1 person bypass alone? Who approves their own work? What log would show it, and who reads that log? |
| Outside attacker | Steal data, extort, or disrupt, with no access at first | What is the first thing an attacker sees? Which credential, form, or API accepts input from a stranger? What happens after 1 account falls? |
| Regulator or litigant | Find a breach after the fact | Which rule did the plan assume away? What would a plaintiff's lawyer quote from our own documents? |
| Nature and infrastructure | Fire, flood, outage, pandemic, supply failure | Which single site, person, vendor, or system stops everything? How long until the owner notices, and how long until recovery? |
| Model and automation | An AI component drifts, hallucinates, or follows an injected instruction | What does the system do with a confident wrong answer? Where does untrusted text reach a model that can act? |
| Gamer | Meets the metric and defeats the purpose | Which number does the plan reward? How does someone hit that number while making the outcome worse? |
| Future self | The owner, under pressure, in 2 years | Which decision will the owner reverse when money or time runs short, and what does that reversal break? |

## Methods

- **Attack trees.** Put the adversary's goal at the root. Branch into the ways to reach it, down to concrete steps. Mark each leaf with cost, skill, detectability, and the control that blocks it. A leaf with no control is a finding. (Schneier 1999)
- **Kill chain.** For each attack path, list the stages: reconnaissance, access, foothold, action, and cover. Ask at which stage a defender has the cheapest chance to notice or stop it.
- **Analysis of competing hypotheses.** When evidence about an adversary is ambiguous, list the hypotheses in columns and the evidence in rows. Score each cell as consistent or inconsistent. Keep the hypothesis with the least inconsistent evidence, not the one with the most support. (Heuer 1999)
- **Control bypass walk.** Take each control in the plan and ask: who can turn it off, who can approve around it, what happens when it fails open, and who reconciles its output against reality.
- **Incentive audit.** For each party, write what it gains if the plan fails and what it loses if the plan succeeds. A party that gains from failure and holds a lever is an adversary, whatever its title.
- **Wargame.** Play 3 moves: the adversary acts, the defender responds, the adversary adapts. Most plans survive move 1 and fail move 3.

## Output

For each surviving attack path: ID | Adversary | Goal | Path (steps) | Precondition it exploits | Where a defender could notice | Present control | Gap | Cost to the adversary (low, medium, high) | Consequence | Reversibility | Cheapest credible control | Owner

Then list the adversaries you did not model and the paths you could not test.
