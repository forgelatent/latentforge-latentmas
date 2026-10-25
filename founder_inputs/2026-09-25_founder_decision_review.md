# Founder decision review — September 23–25, 2026 (filed October 25)

**Status: DECISION NOT MADE.** This file carries two Systems Engine documents that
otherwise existed only in a chat transcript. Filed on return from a gap of several weeks.

**Read the second document first.** The first (Sept 23) recommended STOP on the basis of
a misreading of arXiv 2608.04893 — it treated a true-cache-vs-deranged-cache audit as a
latent-vs-text comparison. The Founder caught the error. The second (Sept 25) lists the
overstated sentences, separates four hypotheses, re-scores, and recommends one bounded
H3 experiment (latent vs matched-budget text, equal information) with a kill date.

**Dates inside are stale.** The Nov 15, 2026 kill date assumed work starting late
September. Nothing started. Reset or drop it; do not keep it silently.

**Not done as of filing (Founder to confirm):** Mac Mini check; cold engine round on
these documents; Kalshi email / demo-login checks.

**Standing:** both documents are Tier 3 (Systems Engine synthesis). External claims in
them cite papers; peer-reviewed vs preprint status is stated in the Sept 25 document.
No project file, label or job was changed by either review.

---

## Document 1 — September 23, 2026: STOP recommendation (superseded, kept for the record)

Research done. Below is the decision document. Everything marked with a citation came from a primary or secondary source I read today; everything else is my synthesis (Tier 3) and should be treated that way. Nothing was changed in the repo, and nothing should be until you've done your own check on the two papers in Part 1, because my recommendation rests on them.

---

## Part 1 — What changed outside the project (verified)

**The efficiency half of the thesis is now published, peer-reviewed, and crowded.** LatentMAS, the paper the repo forked, went to ICML 2026 as a spotlight; across sequential and hierarchical settings and three backbone scales (4B, 8B, 14B), it reports up to 14.6% higher accuracy, 70.8–83.7% fewer output tokens, and about 4× faster inference than text-based multi-agent baselines (arXiv 2511.20639). Cache-to-Cache (Tsinghua) was accepted at ICLR 2026 and outperforms text communication by roughly 3–5% with an average 2.5× latency speedup (arXiv 2510.03215). KVComm is also at ICLR 2026. There is now a living survey repo tracking the subfield, listing LatentMAS, KVComm, C2C, LatentK-V, Agent Primitives, and DiffMAS among others (github.com/edzq/LatentAgentComm). A June 2026 unified framework paper catalogs a dozen-plus systems that use either the KV-cache or hidden states as the communicated quantity, and describes the standard fusion methods (prepend, add, learned projection) (arXiv 2606.05711). In plain words: "agents can talk in vectors and it's cheaper" is no longer a thesis. It is a textbook chapter.

**The experiment you were about to design has been run by someone else, with better controls.** Two causal audits appeared in July and August 2026. The August one replaces the relayed cache with deranged (mismatched-example), zeroed, and moment-matched random counterparts, under two regimes defined by whether the receiver needs the sender's private information (arXiv 2608.04893). The result splits cleanly. Where the receiver needs the sender's private information, latent relay hits ceiling (100% vs 23–25% for answer-irrelevant relays), replicated across three model families and five checkpoints. Where it does not, a pre-registered five-seed protocol shows equivalence within 2.8 points on GSM8K and ARC-Challenge across three Qwen3 scales. And on the systems themselves: zeroing the relay in one cell costs 14.7 points while a mismatched cache costs 0.4; LatentMAS's native relay transfers example-specific content, KVComm's layer subset transfers it partially, and C2C's released projector shows no detected example-specific transfer. That is the split-information task with shuffled-item and random-vector controls from handoff item 11, done at scale, pre-registered, released as an instrument.

**What that means for the "ineffable alpha" half.** Nothing in the literature I found supports the claim that latent channels produce insights text cannot. The audits say the opposite of what "useful divergence" hoped for: when both agents already have the same information (which is exactly the prediction-market setup, where every agent sees the same market), the latent channel and the text channel are statistically equivalent. The gains show up only when one agent knows something the other doesn't. That is bandwidth, not new thought.

**The safety field has turned the Shadow Self problem into a mainstream research area — and treats latent communication as the threat.** The cross-lab monitorability paper (OpenAI, Anthropic, DeepMind, and others) warns that latent reasoning models might not need to verbalize any of their thoughts and would thus lose the safety advantages that CoT confers (arXiv 2507.11473). The Frontier Model Forum's January 2026 brief recommends preferring architectures that require chains of thought for serial reasoning until interpretability methods can provide similar insight. Papers in mid-2026 already study split-evidence reasoning with malicious specialists over transported KV state (arXiv 2606.28958) and latent attacks in latent-based multi-agent systems (arXiv 2605.28214). The auditors also note the channel locks sender and receiver to compatible checkpoints and leaves no directly human-readable transcript. Shadow Self's idea (translate the latent channel into an audit log) is the right question, and it is now being worked on by people with interpretability teams. The repo holds a 120-line spec, unchanged since March 28, and no code.

**Models and hardware.** Closed models still expose no hidden states; that is unchanged and structural. Open weights are abundant and strong: secondary sources place Qwen3.6-27B at 77.2% SWE-bench Verified in a 27B dense package, with Gemma 4 and gpt-oss-120b under Apache-2.0, and Qwen3.8-27B as the pick for a single 24 GB GPU or 32 GB Mac. (Those are aggregator blogs, not model cards; treat the exact numbers as unverified.) A Mac Mini M4 Pro at 48 GB runs 14B models at roughly 25–40 tokens/second and 30B models at 12–18, and MLX now supports hidden-state work. The audits ran on Qwen3 at 4B/8B/14B — the same class the Mini handles. Phi-3 Mini 3.8B, the repo's canonical model, is two generations old. Rented GPUs are needed only for large-scale runs, not for the experiment itself.

**Speculative implications (mine, not sourced):** falling token prices (DeepSeek-class models at cents per million tokens) shrink the commercial pull of "cheaper coordination" for anyone who isn't running inference at scale. The C2C team's next release is agent-managed KV-cache with a serving system, which is the productized form of the thesis, from a lab.

---

## Part 2 — The three options, precisely

**Continue.** Reusable code: polymarket-pull, the mode1 loader, calibration-tracker's scoring layer, and the small hidden-state capture/steering scripts. That is plumbing for a benchmark whose latent arms do not exist and whose control arm is a random stub. Architecture: nine launchd agents, Phi-3, eleven fixed markets, a $10M threshold — none of it reflects how the field now measures this (mismatched-cache audits on Qwen3, asymmetric-information tasks). Hidden debt: the Sept 21 audit found two shadow_match programs, a missing sparsity script, a dead `WakeForJob` key, and canonical claims that were wrong for five months. Time to repair before useful experimentation: the last five months *were* the repair, and the scientific arm has no commit since April 17. Continuing preserves sunk cost. It does not create leverage.

**Stop.** Probability the core thesis is true: the efficiency half is true and proven by others; the "different thought" half has no support and the best available test says the channel is equivalent to text under shared information. Is the problem being eliminated? Partly — cheap tokens and better small models shrink it; the remaining real value (private-information handoff, on-device relay) is being built by labs. Novelty: none left for a solo non-technical founder in this subfield. Time elsewhere: almost certainly more valuable. Assets worth keeping: the governance methodology, the incident ledger as a case study, the market-data pull. Reconsideration triggers: listed at the end.

**Start from scratch.** Modern models do change the architecture (Qwen3-class, KV relay, not seed deltas). Starting clean would be faster than repairing. But the smallest clean implementation is a replication of the August audit on your own hardware — a good learning exercise, not new science — and the danger the founder named ("starting over is psychologically attractive but technically unnecessary") applies with full force: it would be a new repo built to re-answer a question that was answered in August.

---

## Part 3 — Scorecard

| Criterion (weight) | Continue | Stop | Start from scratch |
|---|---|---|---|
| Answering the core scientific question (25%) | 2 | 8 | 5 |
| Speed to credible evidence (20%) | 2 | 9 | 5 |
| Technical fit with current models (15%) | 3 | 5 | 8 |
| Founder-time efficiency / opportunity cost (15%) | 2 | 9 | 5 |
| Reuse of valuable existing assets (10%) | 7 | 5 | 5 |
| Differentiated scientific/commercial value (10%) | 2 | 2 | 3 |
| Clear stop/continue decision (5%) | 3 | 10 | 8 |
| **Weighted total** | **2.70** | **7.10** | **5.40** |

Arithmetic: Continue 0.50+0.40+0.45+0.30+0.70+0.20+0.15; Stop 2.00+1.80+0.75+1.35+0.50+0.20+0.50; Scratch 1.25+1.00+1.20+0.75+0.50+0.30+0.40.

**The scores that decide it.** Stop gets 8 and 9 on the first two criteria for one reason: the credible evidence already exists, in two papers, at zero cost to you. "Answering the question" does not require you to run the experiment; it requires you to accept a well-run answer. If you reject that — if you believe the audits do not test *your* question — Stop drops to about 2 and 3 on those rows and Scratch wins (roughly 5.4 vs 4.4). So the whole decision turns on one thing you can check yourself: read the August abstract and the "two regimes" result and decide whether it is your question. Continue loses on every row except asset reuse, and asset reuse is 10%.

**Scores I want to defend.** Scratch's "technical fit" 8 is real — a clean build would use the right models and the right instrument. Its "differentiated value" 3 is honest: replication has some value as learning and as a local-hardware datapoint, not as a contribution. Stop's "reuse" 5 not 3: the methodology is portable and is the thing you actually built.

---

## Part 4 — The twelve questions

1. **Still important?** The efficiency question, yes, and it is answered. The "new thought" question is important in principle and now looks empirically empty.
2. **Credible reason to expect latent > text under equal conditions?** Under equal *information*, no — the audit shows equivalence. Under asymmetric information, yes, and it is a bandwidth story, not a divergence story.
3. **More or less attractive?** Less. Better small models made the experiment easy, and better-resourced groups then ran it.
4. **Asset, liability, or record?** Historical record with two small assets inside it (market-data pull; loader) and one large one alongside it (the methodology).
5. **Reusable share of technical work?** Roughly 10–15% of the code by function (pulls, loader, scoring layer), and 0% of the latent-channel code as a foundation for anything modern.
6. **Shadow Self still differentiated?** The problem is now mainstream safety research; the differentiated part was never built. The insight is worth writing down; it is not a moat.
7. **Strongest case for continuing:** the data plumbing is honest now, the registry is live, and 30 days of cheap running costs nothing. (But it measures forecasting, which your own motor-car tests call horse territory.)
8. **Strongest case for stopping:** the question has been answered by better instruments; your remaining edge is the methodology, which does not need this project to exist.
9. **Strongest case for starting over:** a two-week Qwen3 replication of the mismatched-cache audit on the Mini would give you a first-hand, clean latent result — something the project never produced.
10. **A sophisticated founder with no history:** would not enter this subfield solo in September 2026. They would read the two audits and move on, or join a group already doing it.
11. **My own time and money:** stop the research thesis, keep the method.
12. **What would make me wrong:** if the audits' "no advantage under shared information" result fails to replicate, or if someone shows a latent-only effect on a *decision* task with resolved outcomes (not a QA benchmark). I found neither.

---

## Part 5 — Required output

**1. Recommendation.** **STOP** — archive LatentForge as a read-only evidence record, complete the security closeout, and carry the methodology forward as its own artifact.

**2. Confidence: 70%.** The 30% is almost entirely the possibility that you read the August audit and judge it does not test your question, or that the Mac Mini check turns up unpushed work that changes the evidence base. It is not uncertainty about the repo's state; that is well documented.

**3. Scorecard.** Above: Stop 7.10, Scratch 5.40, Continue 2.70.

**4. Strongest argument for each.** Continue: honest plumbing exists and costs little to leave running. Stop: the field answered the question and the safety consensus is against the commercial pitch. Scratch: a clean replication would be the first real latent result you personally own.

**5. Why Stop wins.** Your own criteria put 45% of the weight on answering the question and getting to credible evidence fast. Both are already done — externally, pre-registered, with the exact controls your Sept 21 review proposed. Paying again for an answer that exists is the one thing the criteria penalize most.

**6. Why the others lose.** Continue loses because the repo cannot answer the question with any of its instruments and five months of work confirmed that. Scratch loses because its best-case output is a replication, and the psychological pull toward a fresh repo is exactly the trap you told me to watch for.

**7. Worth preserving regardless.** The incident ledger; the evidence tiers; the reproducer requirement with the enumeration clause; the cold-review and v2-briefing method (the calibration-tracker hallucination catch is a publishable case); Pattern D, G, H; the paste-safety rule; polymarket-pull and the mode1 loader as working Gamma clients (Pattern G is a genuinely useful catalogue of that API's traps); the Shadow Self spec as a one-page idea note.

**8. Never again represented as proven.** "24× compression at 1.0000 fidelity" (it is 0.607). "30–100× compute savings" (measured 4.3–9%, uncompressed). "Bidirectional steering." "Latent swarm beats text swarm" (no matched experiment exists). Any "vs crowd" number before April 19. "Shadow Self" as a working system. "Agent-to-agent latent communication" as something this repo demonstrated — it demonstrated one-directional generic stance steering on one model.

**9. Opportunity cost.** 30 days at the September pace: another month of auditing cron logs for a benchmark with no latent arm. 90 days: the registry's own rule 3d will likely force a v3 selection session, consuming the time that a replication or a write-up would take. 180 days: a full year since the last scientific commit, spent on governance for a measurement that was never the thesis.

**10. Immediate next step.** One reading, one check, no code. Read the abstract and Section 1 of arXiv 2608.04893 yourself and write one sentence: "This is / is not my question." Then run the Mac Mini check from the handoff (unchanged, read-only). Those two things settle the 30%.

**11. Hard kill criterion and date.** If, by **October 7, 2026**, (a) you judge the audit is your question, and (b) the Mac Mini holds no unpushed latent work, the project is archived that week: security closeout finished (Kalshi email and demo-login checks, push protection confirmed — these happen regardless), repo marked read-only in its README, launchd jobs unloaded, final ledger entry written. No new experiment starts before that date.

**12. What would reverse it.** Any one of: the Mac Mini clone holds a matched latent-vs-text result with resolved outcomes; a replication fails to reproduce the audit's "equivalent under shared information" finding; a published result shows latent relay improving a *decision* task where all agents see the same information; or a lab open-sources a latent-to-text auditor that could be applied without an interpretability team — that last one would re-open Shadow Self specifically, and only that.

---

**What I would tell the founder privately.** You did not lose. You built, as a non-technical solo founder, a working method for keeping AI engines honest — evidence tiers, reproducers, cold review, incident discipline — and you proved it works by catching your own project's false claims before anyone outside heard them. That is rarer than the latent-channel result would have been. The latent question got answered by people with GPUs and grad students; that was always the likely outcome once the subfield woke up, and it woke up in October 2025. The thing nobody else has is your ledger.

**What I would do personally.** Stop LatentForge. Spend the next block writing the methodology up as a standalone thing — the four-protocol session model, the failure patterns, the v2-briefing defense, the paste-safety rule — because that is the asset, and it is portable to whatever you do next. Keep polymarket-pull if you want a market feed for something else. Do not build a new repo to re-answer an answered question.

**The decision.** STOP. Verify the one paper, run the Mac Mini check, close out security, archive by October 7.

---

One process note, not a hedge: your own protocol says a decision this size goes through a cold engine round. I'd send this document to the other engines with your framing withheld, exactly as you did for the calibration-tracker review, and let them attack the load-bearing claim — that the August audit answers your question. If it survives, act on it.

---

## Document 2 — September 25, 2026: reassessment after Founder correction (current)

Correction accepted, and it's load-bearing. I re-read the August paper in full rather than from the abstract, and it is more explicit than your summary: it says its direct-text arm is a validity calibration, not a medium comparison, and is never interpreted as a text-channel baseline; and that LatentMAS's hybrid ablation compares communication media while the audit intervenes on cache content within the latent interface, so both results can hold simultaneously. My earlier reading collapsed "pairing term bounded" into "latent equals text." That was a Context-Filling Machine error on my side: I had the shape of the experiment I expected to find and read the paper as that experiment.

## 1. Corrected interpretation of the two audits

**August (arXiv 2608.04893, v2 Aug 27, preprint, three authors: an independent researcher and two at Ohio State).** The estimand is the *pairing effect*: accuracy with the correctly paired sender cache minus accuracy with a different example's cache from the same batch. Every arm delivers a well-formed cache to the same receiver under the same prompt, so any difference is attributable to cache content. Two regimes. Where the receiver needs the sender's private information, the pairing effect is at ceiling (about +75 points on Qwen3, replicated across three families). Where the receiver could solve alone (GSM8K, ARC-C, MedQA), the pairing effect is bounded within ±2.8 points on Qwen3, with one cell showing a small detected advantage of +1.52 inside the margin. What the paper draws from this is a standard of evidence: headline gains on standard benchmarks cannot by themselves be read as evidence of latent-channel transmission. It does not measure latent against a text channel. The ±2.8 margin is borrowed from LatentMAS's own reported aggregate gain over text, used as a yardstick, not re-measured. And the paper is careful that a large total cache effect can exist without a pairing effect: on MedQA, zeroing the relay costs 14.7 points while the mismatched cache costs 0.4, meaning the relay helps but not through *which* example was sent.

**July (arXiv 2607.26773, preprint, two authors).** Applies controlled message replacements at the sender-receiver boundary on Qwen3-4B/8B over GSM8K, ARC-C, MATH-500, separating five things: encoded sender information, sensitivity to message presence and identity, task value of example-specific content, and value added by a separate agent. Its conclusion is that similar overall effects can arise from opposing components, and example-specific content and other-agent value can differ substantially across models and tasks. That is the nuanced picture you described, not blanket equivalence. The August paper itself notes the July audit leaves practical equivalence unestablished at its ±1-point margin.

**Together they establish:** pairing-specific transfer is real when the receiver needs private information, small or undetectable when it doesn't, and varies by model and task. **They do not establish:** anything about latent versus a strong text channel at matched budgets, or anything about novel discovery.

## 2. Sentences in my prior recommendation that were overstated

- "The experiment you were about to design has been run by someone else, with better controls." — Wrong. They ran a pairing audit within the latent interface; the matched latent-versus-text test is not in either paper.
- "the latent channel and the text channel are statistically equivalent." — Wrong. Equivalence is true-cache versus deranged-cache.
- "Under equal information, no — the audit shows equivalence." — Wrong, same error.
- "the best available test says the channel is equivalent to text under shared information." — Wrong.
- "The audits say the opposite of what 'useful divergence' hoped for" and "That is bandwidth, not new thought." — Overstated. Neither audit tests discovery; the second sentence was inference dressed as finding.
- "the question has been answered by better instruments" and the two scorecard rows that gave STOP 8 and 9 on that basis. — Overstated; only hypotheses 1 and 2 were answered.
- In the plain version: "when both agents already know the same things, sharing thoughts is no better than talking in words. Same score." — Wrong.

What stands: the efficiency numbers, the crowding of the field, the safety consensus, closed-model inaccessibility, the state of the repo, and the C2C finding as the paper scopes it (no detected example-specific transfer through the released projector, explicitly not a claim that C2C's benchmark gains are artifactual).

## 3. Publication status, corrected

Peer-reviewed: LatentMAS (ICML 2026 spotlight, poster June 19); C2C (ICLR 2026); KVComm (ICLR 2026); Thought Communication (NeurIPS 2025) and Communicating Activations (ICML 2025), cited in the audit's references. Preprints, not peer-reviewed: both causal audits; the June unified-framework survey; "When Latent Agents Lie"; the latent-attack paper; the monitorability paper (a multi-lab position piece, influential but a preprint). Interlat was withdrawn from ICLR 2026 and continued as an arXiv preprint; a survey listing shows it with a 2026 venue tag, which I can't reconcile from my sources, so treat its status as unclear. The model rankings I cited are blogs. I presented all of this as one block of "the field" without those distinctions; that was sloppy.

## 4. The four hypotheses

**H1 — Latent channels can transfer item-specific private information.**
*Establishes:* Yes, decisively, for same-checkpoint KV prepend (LatentMAS's native relay reaches 500/500 on Qwen3-8B against about 23–25% for answer-irrelevant relays), and the receiver measurably reads the content: under deranged relays 64–65% of outputs follow the donor example. *Doesn't establish:* transfer through learned cross-model projectors (C2C's released one showed none) or with heavy layer selection (KVComm recovers roughly a tenth). *LatentForge tested it?* No. The April A/B test transmitted no item-specific content; Phase 11 never injected. *Open?* Closed at the core; open at the edges (cross-model, compressed). *Differentiated value in answering it?* None for the core. Small at the edges, and those edges are being worked (Interlat compression, mixture-of-translators).

**H2 — Latent systems can be faster or cheaper than text systems.**
*Establishes:* Peer-reviewed efficiency numbers: 70.8–83.7% fewer output tokens and 4×–4.3× faster end-to-end inference (LatentMAS); about 2.5× latency speedup (C2C). *Doesn't establish:* that this matters commercially against falling token prices, or that it survives outside same-checkpoint deployments; the audit notes the channel locks sender and receiver to compatible checkpoints. *LatentForge tested it?* Only the Week 2 compute-savings numbers (4.3%, ~9%, uncompressed, OUTPUT_OBSERVED only). *Open?* Closed. *Differentiated value?* None.

**H3 — Latent beats a strong text channel when agents see the same information.**
*Establishes:* LatentMAS reports a 2.8% aggregate sequential gain over its text counterpart (peer-reviewed, but the audit notes the per-task figures are variance-free point estimates ranging from −1.6 to +2.3, several negative). The audits show this aggregate is not carried by example pairing in natural cells; what remains could be a generic interface effect. *Doesn't establish:* anything against a *strong* text baseline at matched token and compute budgets with error bars. The August authors explicitly refuse to read their text arm that way; "When Latent Agents Lie" names matched text-channel comparisons as a gap it targets. *LatentForge tested it?* No. The April 17 test gave the two arms different information; text-swarm is a random stub. *Open?* Yes, and it is the honest form of your equal-conditions question. *Differentiated value?* Moderate and shrinking. A pre-registered, matched-budget H3 test with a mismatched-cache control and error bars is a real contribution today; two small teams got audit preprints noticed this summer, so scale isn't the barrier. But the gap is visible to everyone in the survey and will likely be filled by year-end.

**H4 — Latent communication generates correct, useful discoveries that strong text systems don't.**
*Establishes:* Nothing. No paper I found tests discovery under equal information with ground truth. *Doesn't establish:* it, or its negation. *LatentForge tested it?* No. The project never had an instrument for it; the OpenSpiel target as written rewards being different, and the prediction-market benchmark has no latent arm. *Open?* Fully. *Differentiated value?* High if it showed anything; probability low; and the design problem (what counts as a "discovery," scored against what truth) is unsolved by anyone. This is the thesis you actually care about, and it has not been disproven. I said otherwise. I withdraw that.

## 5. Revised scorecard

| Criterion (weight) | Continue | Stop | Start from scratch |
|---|---|---|---|
| Answering the core scientific question (25%) | 2 | 2 | 5 |
| Speed to credible evidence (20%) | 2 | 3 | 5 |
| Technical fit with current models (15%) | 3 | 5 | 8 |
| Founder-time efficiency / opportunity cost (15%) | 2 | 9 | 4 |
| Reuse of valuable existing assets (10%) | 7 | 5 | 5 |
| Differentiated scientific/commercial value (10%) | 2 | 1 | 4 |
| Clear stop/continue decision (5%) | 3 | 10 | 8 |
| **Weighted total** | **2.70** | **4.30** | **5.35** |

What moved and why: Stop dropped from 8 to 2 on the first row and 9 to 3 on the second, because the external evidence answers H1 and H2 only; H3 and H4 stay open and Stop does nothing about them. Scratch stays at 5/5 (an H3 pilot is weeks on your hardware with LatentMAS's open code and the audit's released harness; H4 is months and hard). Scratch's founder-time score fell from 5 to 4 because H4 is now on the table and it is expensive. Stop's differentiated-value score went to 1: stopping forecloses the only open questions. Continue is unchanged; nothing in the correction helps the existing repo.

## 6. Revised recommendation and confidence

**START FROM SCRATCH, narrowly: one pre-registered H3 experiment, nothing else, with a kill date.** Confidence 55% that this beats STOP; 45% STOP; Continue is not a live option.

Why the flip is honest and not a scorecard artifact: the single fact that changed is that H3 is open and testable on your machine. Your criteria put 45% of the weight on answering the question and reaching evidence fast. When I believed the question was answered, those rows favored Stop; now that it isn't, they favor the option that answers it. Holding STOP after the correction would have required arguing that opportunity cost outweighs the 45%, which is a different weighting than the one you gave me.

Why 55 and not 75: the five STOP grounds still stand. Differentiation is real but closing; opportunity cost is high; the groups working this have GPUs and coauthors; the old architecture is dead (which is why this is Scratch, not Continue); and there is no commercial path, only a narrow scientific one. If you personally weight founder time higher than 15%, STOP is correct and I would not argue.

What "one H3 experiment" means, at the level of a description and not a design (design waits on a cold engine round): same checkpoint in every arm (Qwen3-8B class, fits the Mini); LatentMAS's released relay as the latent arm; a text arm that gets the sender's full written reasoning at a matched token budget, not a one-line summary; a deranged-cache arm as the content control; a task where agents see the same input; pre-registered margin and seed protocol borrowed from the audit; repeated measures from items, not seeds. Kill criterion: if by **November 15, 2026** the pre-registered test does not show a latent advantage outside the margin, the project archives and H4 is never started. If it does, H4 becomes the next decision, not an automatic continuation.

## 7. Does "extract the methodology and stop the latent research" remain the best decision?

Half of it does. Extracting the methodology is right under every option and should happen regardless. Stopping the latent research outright is no longer the best decision on your weights, because I was wrong that the science was settled. The revised answer is: extract the methodology, give the latent question exactly one clean, bounded, pre-registered shot at H3, and let that result make the stop decision for you.

One process note. This is the second time in a week I built a confident recommendation on a misread paper, and the first time you caught it rather than a reproducer. That is the "flag-and-proceed" shape from the May 23 ledger entry, mine this time. Before you act on either version, this document should go to the other engines cold, with the August paper's Section 3 attached, and the question they should be asked is the narrow one: does the paper's text arm license any latent-versus-text claim? I now say no.