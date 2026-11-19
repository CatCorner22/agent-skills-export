# Statistical analysis of rare, severe events

Use this file in Step 5. Its job is to say which world the data comes from, what the data can and cannot show about the tail, and how to decide when the probability is unknowable.

## Two worlds

- **Thin tails (Mediocristan).** Many small, independent causes add up. Heights, measurement noise, daily attendance. The average means something, the largest observation is close to the second largest, and the next record exceeds the old one by a little.
- **Heavy tails (Extremistan).** One observation can dominate the total. Wealth, city sizes, pandemic deaths, cyber-loss sizes, market crashes, war deaths, project overruns, viral spread. The average converges slowly or not at all, and the next record can exceed the old one by a large multiple. (Taleb 2007, 2020)

Decide which world you are in before you use any average, standard deviation, or "1 in N years" figure. In a heavy-tailed world, those figures mislead by construction.

## Signs of a heavy tail

Run `scripts/tail_check.py` on any series with 30 or more observations. Read the signs together; no single sign decides.

| Sign | What to look for | Why it matters |
|---|---|---|
| Concentration | The top 5% of observations carry more than half of the total | A few events set the outcome |
| Max-to-sum ratio | max(x^p) / sum(x^p) stays large as n grows, for p = 1, 2, 4 | When the ratio for p = 2 does not fall toward 0, the variance does not exist (Taleb 2020) |
| Hill tail index | alpha below 2 means no finite variance; below 1 means no finite mean (Hill 1975) | The standard error is about alpha over the square root of k; read the band, not the point |
| Mean excess | The average overshoot above a threshold grows as the threshold rises | A Pareto-type tail; in a thin tail it falls or stays flat |
| Peaks over threshold | A generalized Pareto fit to the exceedances with a positive shape xi | xi above 0 means a Pareto-type tail with no upper limit; xi above 0.5 means infinite variance (Coles 2001) |
| Kurtosis instability | Sample kurtosis jumps when 1 observation enters or leaves | A fourth moment that does not settle does not exist |

## What a sample cannot show

- **The largest event is not the worst case.** A record is a sample statistic. The next event can exceed it.
- **Absence of evidence.** With 0 events in n independent trials, the 95% upper bound on the per-trial probability is about 3/n (Hanley and Lippman-Hand 1983). Report the bound, never "it has not happened, so it does not happen". Run `scripts/tail_check.py --zero-events N`.
- **Silent evidence.** The record shows the survivors. Projects that died, firms that failed, and patients who left the study do not report (Taleb 2007). Ask who is missing from the data before you read the base rate.
- **Non-stationarity.** Every tail estimate assumes that the process stays the same. New technology, new law, new scale, and new adversaries change the process. Date the data and say what has changed since.
- **Tail dependence.** Correlations that hold in calm periods rise in a crisis; diversification that counted on independence fails together (Embrechts, McNeil, and Straumann 2002). Ask what the scenarios share: a vendor, a site, a person, a model, a market.
- **Small samples.** Below about 30 observations, the tail estimate is noise. Below 10 exceedances, do not fit a tail at all. Use the outside view instead.

## Return levels

A "1 in 100 observations" level from a peaks-over-threshold fit comes with a band. `tail_check.py` prints a 90% bootstrap band. Report the band, and say that the band itself assumes the fitted family and a stable process. Extrapolate no further than about 3 to 5 times the length of the record, and label anything further as a model assumption, not an estimate.

## Base rates and the outside view

Before any inside estimate, find the base rate for the reference class: the share of projects like this one that overran, the share of firms in this sector that failed within 5 years, the share of systems like this one that leaked data (Kahneman and Lovallo 1993; Flyvbjerg 2006). Write the reference class, the count of cases, the rate, and the source into the register. Adjust from the base rate only for evidence that is specific, documented, and large.

## When probability is unknowable

Some risks have no usable probability: nobody has the data, the process is new, or the adversary adapts. Do not invent a number. Use these decision rules instead:

1. **Severity first for ruin.** If an outcome ends the organization, kills or injures people, breaks the law, or that no one can reverse, rank it by severity and require a control that stops the path or caps the loss. Probability weighting does not apply, because there is no second draw after ruin (Taleb, Read, Douady, Norman, and Bar-Yam 2014).
2. **Time average, not ensemble average.** An expected value computed across many imagined parallel runs does not describe 1 organization that lives through 1 sequence. A gamble that is favorable on average and carries a chance of ruin destroys the player who repeats it (Peters 2019). Ask: if we take this bet every year, what happens to us over 20 years?
3. **Fragility test.** For each key variable, estimate the loss from a 1-unit, 2-unit, and 4-unit adverse move. If the loss accelerates, the exposure is fragile, and reducing it beats forecasting the trigger (Taleb 2012).
4. **Bounded downside.** Prefer a design whose worst case you know and can survive over one with a better average and an open-ended worst case.
5. **Option value.** Prefer the reversible step, the pilot, and the staged commitment. Each one buys information at a known price.
6. **Tripwires.** Set a measurable signal and a pre-committed response for each high-consequence scenario, so that the response does not depend on recognizing the surprise in the moment.

## Scenario tables

Run `scripts/exposure_table.py` on a scenario CSV (scenario, probability, impact, and optional reversible, detectable, evidence columns). It reports the expected loss by scenario, the expected shortfall of the worst 10% of probability mass, the ruin scenarios, and whether the ranking survives a 3-times error on every small probability. A ranking that flips under that error is a ranking that the evidence does not support.

## Pitfalls to name in the report

Gaussian assumption; extrapolation past the record; survivorship bias; a probability with more decimals than its evidence; "unprecedented" used as "impossible"; averaging over ruin; independence assumed among correlated failures; a model that nobody tested on data it did not fit; and a confidence interval reported without the family and sample size behind it.

## Sources that this file names

Coles 2001, *An Introduction to Statistical Modeling of Extreme Values*. Embrechts, McNeil, and Straumann 2002, "Correlation and dependence in risk management". Flyvbjerg 2006, "From Nobel Prize to project management: getting risks right". Hanley and Lippman-Hand 1983, "If nothing goes wrong, is everything all right?" *JAMA*. Hill 1975, "A simple general approach to inference about the tail of a distribution". Hosking and Wallis 1987, "Parameter and quantile estimation for the generalized Pareto distribution". Kahneman and Lovallo 1993, "Timid choices and bold forecasts". Peters 2019, "The ergodicity problem in economics", *Nature Physics*. Taleb 2007, *The Black Swan*; 2012, *Antifragile*; 2020, *Statistical Consequences of Fat Tails*. Taleb, Read, Douady, Norman, and Bar-Yam 2014, "The Precautionary Principle (with Application to the Genetic Modification of Organisms)". Verify a citation before you quote it outside this skill; this file names sources, it does not reproduce them.
