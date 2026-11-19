# The 4 quadrants

Rumsfeld named 3 kinds of knowledge in a 2002 briefing: known knowns, known unknowns, and unknown unknowns. Analysts added a 4th: unknown knowns, the things a team knows but does not use, admit, or say. Work the quadrants in this order. Each quadrant feeds the next.

## Q1 Known knowns: facts the team relies on

Goal: a list of facts with evidence grades, and a sample that you checked.

1. List every fact, number, and assumption that the decision rests on. Include the ones that seem too obvious to write down; those hide the worst errors.
2. Grade each one: **verified** (you opened the source or ran the check this session), **sourced** (a named source that you did not open), **recalled** (memory or habit), or **asserted** (someone said so).
3. Verify a sample. Pick the 5 facts whose failure would hurt most, and check each one against its source or by recalculation. Record what you found. If 1 of the 5 fails, verify 5 more.
4. Date every fact. Ask what event would make it false, and when someone last checked it.
5. Move each fact that fails verification to Q2 as a question, and each one that the team cannot source to Q4.

Questions that expose weak known knowns:

- Who measured this, with what instrument, and when?
- Does this number describe our case, or a different population, period, product, or jurisdiction?
- Would the same source still say this today?
- What do we treat as settled that a competitor, regulator, or auditor would dispute?

## Q2 Known unknowns: questions the team can name

Goal: a question register with a triage by how much each answer changes the decision and what it costs to learn.

For each question, record: ID; the question; the decision it affects; the answer that would change the decision; who or what can answer it; the cost and time to learn; the value of learning it; the deadline after which the answer no longer helps; and the owner.

Triage by value of information (Howard 1966). Ask: if we knew the answer for certain, would we act differently? If no answer would change the action, the question carries no decision value, however interesting it is. When the stakes carry numbers, compute the expected value of perfect information: the expected outcome with the answer minus the expected outcome without it. When they do not, rank by 2 axes: how much the answer could move the decision, and how cheap and fast the answer is.

Act on the result:

- High value, cheap to learn: learn it now, before the decision.
- High value, expensive to learn: design the cheapest experiment that narrows it, or stage the decision so the first step stays reversible until the answer arrives.
- Low value: record it and move on.

Common questions that teams leave off the register: the base rate for projects like this one; what happened the last 3 times someone tried this; who else has a veto; what the exit costs; and who is accountable when it fails.

## Q3 Unknown unknowns: surprises that nobody has named

Goal: convert some unknown unknowns into known unknowns, and make the plan survive the ones that stay hidden.

Nobody can list unknown unknowns; the label would make them known. You can do 3 things:

1. **Widen the search** with techniques that produce candidates from outside the team's frame.
2. **Measure exposure without a cause.** Ask how much a shock of a given size hurts, whatever causes it. Fragility shows in the shape of the loss (Taleb 2012): if a change of 2 units hurts more than twice as much as a change of 1 unit, the system is fragile to that variable, and the cause does not matter.
3. **Build detection and response.** Tripwires that fire on symptoms rather than causes, reserves and slack, reversible first steps, and a rehearsed response plan all pay off against surprises that no one named.

Techniques that widen the search (use at least 4; state which ones you used):

| Technique | How | Source |
|---|---|---|
| Pre-mortem | Assume the plan failed at 3, 12, and 36 months. Each person writes the most plausible story of the failure before any discussion. | Klein 2007 |
| Outside view and reference class | Find 10 or more past cases that resemble this one. Record their base rate of failure, cost overrun, or delay before you look at the specifics of this case. | Kahneman and Lovallo 1993; Flyvbjerg 2006 |
| Inversion | Ask what would guarantee failure, then check whether the plan does any of it. | Jacobi, via Munger |
| Perspective rotation | Describe the plan from the seat of each stakeholder: user, insider, competitor, regulator, supplier, the person on call at 3 a.m., and the person who inherits it in 5 years. | Heuer 1999 |
| Second-order effects | For each intended effect, ask "and then what?" 3 times. Who adapts, who games it, what grows or shrinks because of it? | Systems thinking (Meadows 2008) |
| Boundary check | List what the analysis treats as outside its scope, fixed, or someone else's problem. Each item is a candidate surprise. | Leveson 2011 (STPA) |
| Near-miss and weak-signal scan | Collect incidents that almost went wrong, complaints that nobody escalated, workarounds that staff use, and metrics that drifted without an alarm. | Reason 1997 |
| Analogy from other fields | Ask how a hospital, an airline, a bank, a farm, and a military unit would see this risk. Each field has named failures that others have not. | Cross-domain transfer |
| Expert elicitation | Ask 3 or more experts for the worst case they have seen in a situation like this, and for the surprise that embarrassed them. Ask for the story, not the probability. | Tetlock and Gardner 2015 |
| Adversarial play | Run the adversary models in `adversarial.md`. | |

Record each candidate as a Q2 question, with its trigger, early signal, and the cheapest test.

## Q4 Unknown knowns: what the team knows but does not use

Goal: surface tacit knowledge, denied knowledge, and assumptions that masquerade as facts.

- Ask the people closest to the work, not the people who own the plan: "What do you know about this that the plan ignores?" and "What do you work around every week?"
- Look for knowledge that the team holds but has agreed not to say: a key person who is leaving, a customer who is unhappy, a control that no one follows.
- Look for the assumptions behind the Q1 list that nobody wrote down: the supplier stays solvent, the law stays the same, the model keeps behaving as it does today, the owner stays healthy.
- Check the record. Did an earlier review, audit, incident report, or customer complaint already name this risk? A risk that someone named and the team dropped is a Q4 item, and it needs an owner and a decision now.

## Register format

Carry 1 register through the whole review:

ID | Quadrant | Item | Evidence grade or status | Decision it affects | Trigger or early signal | Consequence if wrong | Reversibility | Cheapest test or control | Owner | Due date
