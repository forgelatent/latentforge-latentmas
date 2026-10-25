# Competitive scan — October 25, 2026

**Tier 3 (Systems Engine synthesis). Not canon.** Companion to `founder_inputs/2026-09-19_competitive_scan.md`.
Covers September 22 to October 25, 2026. Source: the 25 research-sweep digests written in that window, filtered by keyword, then five abstracts read in full. No paper was read past its abstract. Nothing in this file moves a label, a job, or a canonical claim.

Written in session with the Founder on October 25, 2026. The Founder's framing (continue) was stated before this scan was run; the scan was not designed to support or oppose it.

---

## 1. The instrument, before the findings

Of research-sweep's ten search terms, one produced clean hits: `latentMAS`, because it is a word only this field uses. The other nine (`latent delta`, `hidden state delta`, `latent governance`, `latent collaboration`, `AVP latent`, `multi-agent latent`, ...) returned dark-matter physics, brain MRI, quantum channels, astrophysics. About 385 distinct arXiv papers over five weeks; roughly a dozen are in the field. This is the May 2 matching finding (`incident_ledger.md`, May 2 audit) measured at five weeks of scale. The `## Competitive Watch` section of every digest is still the same three static lines (September 19 fourth-session finding, unchanged).

**What the feed could not have found:** anything that does not contain one of the ten terms. A matched latent-versus-text paper (the H3 gap) titled without the word "latent" would not appear. Absence from this list is not absence from the field.

*Reproducer (names and counts only):*
`grep -h -i -B1 'arxiv.org' research/daily-digest/2026-09-2[2-9].md research/daily-digest/2026-10-*.md | grep -i -E 'latent|kv.?cache|hidden.state|activation|communicat|steer' | sort -u | wc -l`

## 2. Five abstracts, read in full

**LatCom: Cross-Agent Latent Compression for Efficient Multi-Agent Collaboration** — arXiv 2609.37017v1, September 29, 2026, preprint, ten authors.
Builds on LatentMAS. Problem stated: forwarding every sender's latents makes the receiver's context grow with agent count and reasoning length. Approach: do not reconstruct the sender's hidden states; compress multiple senders into a fixed number of slots trained for the receiver's task accuracy. Reported on Qwen3-4B: about 2.5x speed-up over LatentMAS, about 70% fewer output tokens, comparable accuracy.
*Bearing on LatentForge:* the Week 2 compression test (`05_topk_sparsity_phi3.json`, 0.607 cosine at 24x, F-1 in the September 21 ledger entry) measured reconstruction fidelity. This group abandons that yardstick and measures receiver usefulness instead. The question "can the thought be squeezed and still reconstructed" is being replaced in the field by "can the thought be squeezed and still used."

**LatComm: Reusable Context Compression for Latent Communication between Large Language Models** — arXiv 2610.26840v1, October 19, 2026, preprint, four authors. (Different paper from LatCom; one letter apart.)
A frozen encoder LLM compresses context once into a fixed-size packet; a different frozen receiver LLM reads it through cross-attention. Reported: up to +10.2 points average over single-vector baselines on 12 multiple-choice QA sets; 57x smaller receiver input on QuALITY.
*Bearing on LatentForge:* this is cross-model transfer with no training of either model — the edge the September 25 reassessment listed as "open at the edges" under H1. It is being worked.

**CondenseFlow** — found incidentally in the same search; Findings of ACL 2026 (peer-reviewed). Compresses KV caches into fixed-size representations; reports over 99% KV memory reduction with negligible accuracy loss across seven benchmarks and six models. Not read beyond a listing abstract; recorded as a third compression group, the only peer-reviewed one of the three.

**Feedback Coding Enables Inference-Time Covert Agentic Communication** — arXiv 2609.24994v1, September 21, 2026, preprint.
**Title-only guess was wrong.** This is steganography in ordinary generated text (hiding a message inside a normal-looking conversation), not a latent channel. Not relevant to LatentForge. Recorded because the error is the lesson: a title containing "covert" and "agentic communication" read as latent-channel safety work; the abstract says otherwise.

**Caught in the Act (also titled Telling FIBS): Probes Effectively Detect Sabotage and Catch Unverbalized Deception** — arXiv 2610.12445v1, October 2026, preprint, FAR.AI, five authors. Dataset and code released (github.com/AlignmentResearch/fibs-probes).
Trains classifiers on a model's hidden states to detect statements the model believes are false, including cases the output text cannot reveal ("introspective deception"). Reported: about 98% AUROC on agentic sabotage benchmarks, beating text-only monitors; up to 99.7% AUC distinguishing a model's true hidden goal; improves with model scale.
*Bearing on LatentForge:* this is the nearest published thing to Shadow Self. Difference that matters: it is a detector (is this a lie: yes/no), not a translator (what is this latent saying). It does not by itself meet the September 23 reversal trigger ("a lab open-sources a latent-to-text auditor"), but it is the closest approach yet, it is released, and it is from a funded safety lab. The audit-the-hidden-state idea is now being built, by others, as a threat detector rather than a product feature.

**DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses** — arXiv 2610.23839, v1 October 16, v2 October 20, 2026, preprint, 24 authors, code released.
Gives an operational definition of a valuable, testable hypothesis (evidence-grounded, consequential, feasible to investigate, with explicit decision criteria and named alternatives), a benchmark (DFM-Bench) for scoring hypothesis quality, and a novelty check: fraction of generated hypotheses that correspond to research published after the model's training cutoff (reported 6.3% for their 27B model against 2–3% for frontier baselines). Four life-science domains; text research agents, not latent.
*Bearing on LatentForge:* H4 ("does latent coordination produce correct, useful discoveries text does not") was recorded on September 25 as having an unsolved design problem: what counts as a discovery, scored against what truth. This paper is one group's working answer to that design problem, for text agents. It does not test H3 or H4. It is a candidate rubric to borrow if H4 is ever designed.

## 3. What this scan says and does not say

Says (Tier 3, abstracts only):
- Latent compression for multi-agent LLMs is crowded: three groups, one peer-reviewed, in the five weeks since September 19.
- Cross-model latent transfer (frozen, different LLMs) is being worked.
- Hidden-state auditing is being built as deception probes with a public dataset; not as a translator.
- A scoring method for "novel and correct hypotheses" now exists in the open, for text agents.

Does not say:
- Whether anyone has run the matched latent-versus-text test (H3). This feed cannot see a paper that avoids its keywords.
- Anything about H4 being tested by anyone.
- Anything about peer-review status beyond what is stated per paper above. Four of the five read are preprints.

## 4. Corrections and method notes

- The Feedback Coding paper was pre-classified from its title as latent-channel safety work. Wrong on reading the abstract. One of five title guesses failed; the other four held at abstract level.
- Two of the five links in the digest output were truncated by the 150-character display cut, so those two papers (LatComm, Caught in the Act) were located by web search on title; the arXiv IDs above come from the search results, not from the digest.
- No paper body was read. Every "reported" figure above is the authors' own abstract claim, unverified.

## 5. Standing

Filed as input to the open Founder decision (`founder_inputs/2026-09-25_founder_decision_review.md`, status DECISION NOT MADE). Not a recommendation. A cold engine round on the September 25 document has still not happened as of this filing.
