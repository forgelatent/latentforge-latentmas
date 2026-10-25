# LatentForge — cold review briefing, October 25, 2026

**To the reviewing engine: read this section first.**

You do not have terminal access, repository access, or the project's files. You are reviewing an operator's evidence, not the source. Every fact you may rely on is in a labeled block below (E1, E2, ...). When you make a claim, cite the block it rests on. If a claim you want to make has no block, say "no evidence in briefing" rather than filling the gap. In a May 24, 2026 review of this project, one engine described code that did not exist, with line numbers; the operator caught it by running the engine's own commands. That is why this format exists.

The Founder's own view on the decision below is deliberately withheld. Do not infer it from the question wording. Two attachments accompany this briefing: `2026-09-25_founder_decision_review.md` (the Systems Engine's September 23 recommendation and its September 25 correction) and Section 3 of arXiv 2608.04893. Read the second document in the attachment before the first; the first is superseded and kept for the record.

---

## 1. The project in one paragraph

LatentForge (March 2026 to present; solo non-technical founder; Claude as "Systems Engine," Grok, Gemini and ChatGPT as review engines) tests whether AI agents that pass hidden-state vectors to each other, instead of words, (a) coordinate more cheaply and (b) produce correct insights that word-passing agents do not. A prediction-market benchmark was built as the measurement surface. On April 18, 2026, the benchmark was found to have been scoring against a hand-typed seed file instead of live data for 20 days; all "vs crowd" claims were retracted; no external claim was ever made. From April 18 to September 21 the work was remediation and governance: evidence tiers, a reproducer rule, cold review, an incident ledger. A September 21 audit found the project's canonical compression claim was also wrong (see E3). The Founder was away September 25 to October 25. A decision on the project's direction is open.

## 2. What is established at Tier 1 (operator-verified, reproducible)

**E1 — The one real scientific result.** April 15, 2026, Mac Mini M4 Pro, Phi-3 Mini 3.8B: a contrastive "bullish" vector (bullish-prompt hidden state minus bearish-prompt hidden state) injected at layers 16/20/24, scale 0.4, moved a second agent's stated probability from 35% to 75% with stance-specific reasoning in the output. Single model, single market family, greedy decoding. The April 17 "replication" file is byte-identical to the April 15 file (same sha256), so it is not an independent run. Bearish injection: every normalized method flat; only raw negative injection broke output.

**E2 — No matched latent-versus-text experiment exists in the repository.** The April 17 "A/B test" gave the two arms different information (text arm: agents see prior agents' estimates; latent arm: independent agents with a generic optimism vector injected). The four-arm benchmark's latent arms never injected anything (Phase 11 divergence 0.0 on every market). The text "control arm" was replaced with `random.uniform(35, 75)` on April 18 and has not run since April 20.

**E3 — Compression.** Repository result file `05_topk_sparsity_phi3.json`, committed March 29: cosine fidelity 1.0 at 1x (uncompressed), 0.827 at 6x, 0.714 at 12x, 0.607 at 24x. Pass bar in the sibling script: 0.95. No level met it. The canonical documents said "24x at fidelity 1.0000" from April 13 to September 21. The script that produced the file is not in the repository or its history. Status: OUTPUT_OBSERVED, not reproducible.

**E4 — State of the pipeline, October 25, 2026 (terminal output, pasted by the operator today).**
```
== 6 real vs junk
      37
     104
```
Meaning: 37 real nightly research-suggestion files, 104 junk files (error text written as output, April 20 to September 18). The junk count was 104 on September 21 and is 104 today: the September 19 fail-loud fix has written no new junk in 34 days. Real files went 31 to 37: six real nights out of 34.
```
Thu Oct 15 21:33:40 PDT 2026: PERMANENT FAILURE after 3 attempts — manual rerun required
Fri Oct 16 02:00:38 PDT 2026: Attempt 1 of 3 — running .../latent_compression_researcher.py
Fri Oct 16 11:23:37 PDT 2026: FAILED on attempt 1 (exit code 1)
Sat Oct 17 11:57:43 PDT 2026: FAILED on attempt 2 (exit code 1)
Sun Oct 18 14:31:32 PDT 2026: FAILED on attempt 3 (exit code 1)
Sun Oct 18 14:31:32 PDT 2026: PERMANENT FAILURE after 3 attempts — manual rerun required
```
Meaning: the laptop sleeps with the lid closed; a 35-second API call started at 02:00 is suspended for hours or days; while one wrapper is stuck in retries, no new nightly attempt starts. Three PERMANENT FAILURE lines (Oct 15, 18, 24) reached nobody until today. Nothing is broken; the host is asleep when scheduled, and failures are loud into a log nobody reads.

**E5 — Benchmark registry.** 15 fixed prediction markets selected September 14. Today: 13 live, 2 retired. Both retirements are "will X happen by DATE" markets that closed well before DATE (Bitcoin by Sept 30, closed ~Sept 21; US-Iran meeting by March 31 2027, closed in October). A market expected to settle ~Oct 3 is still open. Nothing loaded reads this registry's output; its consumer (the four-arm benchmark) does not exist.

**E6 — Repository state.** Public, GitHub. All agent output through October 25 is committed and pushed as of today (commits `86e6f5e`, `0dd6637`). Push protection and secret scanning: on (operator screenshot, today). A Kalshi RSA private key sat in public git history from April 4 to September 21; the matching key ID was revoked April 29; closed. Last code commit: `d7c8d09`, September 19.

## 3. What changed outside the project (Tier 3: abstracts only, read October 25)

**E7 — Already published before September (from the September 25 document; peer-reviewed where stated).** LatentMAS (ICML 2026 spotlight): 70.8–83.7% fewer output tokens, ~4x faster than text multi-agent baselines; 2.8% aggregate accuracy gain over its text counterpart, per-task −1.6 to +2.3, no error bars. C2C (ICLR 2026), KVComm (ICLR 2026). Two causal audits, both preprints: arXiv 2607.26773 (July) and arXiv 2608.04893 (August, v2 Aug 27). The August audit's estimand is the *pairing effect* (correct sender cache vs a different example's cache). It finds the effect at ceiling when the receiver needs the sender's private information, and bounded within ±2.8 points when the receiver could solve alone. Its own text says its direct-text arm is a validity calibration, never interpreted as a text-channel baseline.

**E8 — September 22 to October 25, five abstracts read in full.**
- *LatCom* (arXiv 2609.37017, Sept 29, preprint): cross-agent latent compression built on LatentMAS; optimizes compressed latents for receiver task accuracy, not reconstruction; reports ~2.5x speed-up over LatentMAS, ~70% fewer tokens, comparable accuracy, Qwen3-4B.
- *LatComm* (arXiv 2610.26840, Oct 19, preprint): frozen encoder LLM to a *different* frozen receiver LLM via fixed-size packet and cross-attention; up to +10.2 points over single-vector baselines on 12 QA sets.
- *CondenseFlow* (Findings of ACL 2026, peer-reviewed): KV-cache to fixed-size representation; >99% memory reduction, negligible accuracy loss, seven benchmarks, six models.
- *Caught in the Act / Telling FIBS* (arXiv 2610.12445, FAR.AI, Oct, preprint; dataset and code released): probes on hidden states detect statements the model believes false, including ones the output text cannot reveal; ~98% AUROC on agentic sabotage; up to 99.7% AUC separating a model's true hidden goal. A detector, not a translator.
- *DiscoveryRSI* (arXiv 2610.23839, Oct 16, preprint, code released): an operational definition of a valuable, testable hypothesis; a benchmark for hypothesis quality; a novelty score (fraction of generated hypotheses matching research published after the model's cutoff: 6.3% vs 2–3% for frontier baselines). Text agents; four life-science domains.

**E9 — What the five-week scan could not see.** The project's paper feed matches on ten keywords, nine of which return physics and astronomy noise; only "latentMAS" produced clean hits. A matched latent-versus-text paper titled without the word "latent" would not appear. Absence from the scan is not absence from the field.

## 4. The four hypotheses (from the September 25 document, attached)

- **H1** Latent channels can carry item-specific private information. Closed at the core (August audit: ceiling effect); open only at edges (cross-model, compressed) — and E8 shows the edges being worked.
- **H2** Latent systems can be cheaper/faster. Closed, peer-reviewed (E7). LatentForge's own measured savings were 4.3% and ~9%, uncompressed, OUTPUT_OBSERVED only.
- **H3** Latent beats a *strong* text channel at matched token/compute budgets when agents see the same information. The September 25 document says: open; neither audit tests it; LatentMAS's 2.8% is variance-free and not carried by example pairing.
- **H4** Latent coordination produces correct, useful discoveries that strong text systems do not. No paper found tests it. The design problem (what counts as a discovery, scored against what truth) was recorded as unsolved; E8's DiscoveryRSI is one group's working answer for text agents.

## 5. The plan under review (Systems Engine, October 25; not yet adopted)

0. Write the decision down with a kill date measured from the day work starts.
1. Inspect the Mac Mini (read-only): clone state, unpushed work, capacity.
2. This cold round.
3. Choose the model from evidence: must fit 48 GB; must be one the LatentMAS code and the August audit's released harness already run on, so mechanics are borrowed, not rewritten.
4. Pre-register one H3 experiment: same checkpoint in every arm; LatentMAS relay as the latent arm; a text arm given the sender's full written reasoning at a matched token budget; a mismatched-cache arm as content control; a task where all agents see the same input; margin and seed protocol borrowed from the audit; repeated measures from items. Committed, hashed, cold-read before first run, not amended after. Kill criterion: no latent advantage outside the pre-registered margin by the kill date → archive, H4 never started.
5. Decide what the nightly pipeline does meanwhile: pause all jobs; fix host-sleep first; or leave running and stop reading logs.
6. Update the state manifest.

## 6. Questions for you

Answer each separately. Cite blocks. Say "no evidence in briefing" where that is the honest answer.

**Q1 (narrow, load-bearing).** Read Section 3 of arXiv 2608.04893 as attached. Does that paper's direct-text arm license *any* claim about latent-versus-text performance? Quote the sentence(s) in Section 3 you rely on. The September 25 document says no; the September 23 document said yes and was withdrawn.

**Q2.** Given E7 and E8, is H3 as stated in Section 4 still open? If you know of a paper that tests a latent relay against a strong text channel at matched budgets with error bars and shared information, name it with an arXiv ID. If you do not, say so; do not reconstruct one.

**Q3.** The experiment description in step 4: name the single biggest reason its result could be uninterpretable (a confound, a budget-matching problem, a task choice, a statistical power problem). One reason, argued, not a list.

**Q4.** Step 5: pause, fix-sleep-first, or leave running. Pick one and give the reason in two sentences. Note E4: the pipeline is honest but produces about six useful nights a month, and nothing loaded consumes the benchmark registry's output (E5).

**Optional.** If you think the right decision is not in the plan at all (including STOP), say so in one paragraph, grounded in blocks.

## 7. What this briefing deliberately does not contain

The Founder's current preference. The Systems Engine's confidence numbers from September 25 (they are in the attachment; do not anchor on them). Any claim about what the Mac Mini currently holds (unknown). Any model name as a recommendation.
