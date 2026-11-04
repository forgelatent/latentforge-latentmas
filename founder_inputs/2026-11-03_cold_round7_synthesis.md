# Cold round 7 synthesis — the divergence secondary endpoint (decision 5); 2 of 3 drop, with one finding unanimous (November 3, 2026)

**Status:** Systems Engine synthesis of three cold readers; Tier 3. Readers (vendor, model, as self-reported): xAI Grok 4.7; Google Gemini 3.1 Pro; OpenAI GPT-6 Astra Pro. Briefing: `founder_inputs/2026-11-03_cold_briefing_v7_adjudication_decision5.md` (52 lines, hash `26b9e607…`). Answers filed verbatim as `founder_inputs/2026-11-03_cold_round7_*.md`. Under review: scoring rule CANDIDATE v0.3 §7's "divergence" and "useful divergence" paragraphs and the threshold delta = 0.10. The briefing pre-committed that this round is final for the point. Nothing is implemented; no model chosen; no count of markets, groups or blocks appears here. Written the same evening as the round; the question is a reading of text, and the Pattern D guard is not engaged.

## 1. Hallucination check

**No fabricated finding or citation.** Two notes, neither an evidence error:
- Gemini 3.1 Pro cites "[E2 in v6 / E1]" once: a block from the previous briefing, not this one. The fact cited (all arms share a checkpoint) is in this briefing's E5 lineage and v0.3 §4; citation defect only.
- Gemini 3.1 Pro's identity d_m = (p_T − y)² − (p_L − y)² = (p_T − p_L)(p_T + p_L − 2y) is correct, and so is its consequence that d_m = 0 whenever p_L = p_T. Its further step — that a positive covariance between |p_L − p_T| and d is a "near-tautological" consequence of a primary PASS — is an argument from the identity, not a theorem (a positive mean of d does not strictly force a positive covariance). Recorded as an argument, which is how it is used below.
- GPT-6 Astra Pro corrects two of its own round 5 objections (outcome-scaling does not reach Gemini's midpoint formula; "whose forecast" is answered by the midpoint). Both corrections are right. Its Q4 paragraph is under the 200-word limit by inspection.

## 2. Unanimous (3 of 3) — adopt

1. **delta = 0.10 has no evidential basis.** Grok and Gemini: therefore not a pre-registrable gate. GPT-6: pre-registrable as a convention, with the limitation kept visible in every report. All three: no evidence on whether it would select enough markets.
2. **No version of the secondary — thresholded, slope, or dropped — establishes E1's clause "the gain is concentrated where the two disagree," and none establishes the motor-car mechanism ("insights that have no clean linguistic description").** Grok: the primary and gates already decide E1; any concentration statement is descriptive. Gemini: by the identity above, all of any Brier gain is generated where the arms disagree, so the clause is arithmetic, not a finding; the filter inspects the same two numbers the primary already scored. GPT-6: a passing conditional result licenses only "latent beat text within the pre-specified subset" and "the concentration clause remains unestablished; it must remain a research question." **Consequence for v0.4 §1:** the claim sentence loses its second half; see section 5.
3. **None of the three thresholds (fixed 0.10; logit distance; |p_L − p_T| ÷ √(p̄(1−p̄)) with p̄ the forecast midpoint) uses a realized outcome.** Only scaling by a realized YES rate would; nobody proposes that. The √(p̄(1−p̄)) form still needs a 0/0 convention and the logit form a rule for forecasts at 0 or 1 (GPT-6).
4. **Whatever is reported can never rescue a primary FAIL**, and if anything inferential is kept it must be recomputed under the sensitivity resampling with the E5 labels (GPT-6 explicitly; Gemini: show both intervals if any are shown; Grok: no claim, so nothing to recompute).

## 3. The split, and the resolution proposed

**Drop (Grok, Gemini 3.1 Pro) vs keep a fixed 0.10 with a full conditional protocol (GPT-6 Astra Pro): 2 to 1.** Option (c), the slope test, was chosen by nobody; its author withdrew it (Gemini: the slope follows from the Brier identity; GPT-6: it needs a group-level disagreement measure that does not yet exist and asks a different question).

- *The case for (b), fairly stated:* a pre-fixed cutoff and aggregation define a falsifiable conditional comparison; output-dependent selection limits the claim without invalidating it; a passing result adds one narrow fact the primary does not give — the sign of the improvement inside the high-disagreement subset. GPT-6 concedes the support floor has no justified number and offers "at least two groups and two blocks" as a computability screen only.
- *The case for (a):* the purpose the endpoint was written for (E1's concentration clause) is one all three agree it cannot serve; what remains is a conditional mean on a subset chosen by the arms' outputs, requiring a support rule nobody can justify and handling for an empty set; by the identity, the subset's sign will track the overall sign except in a constructed case, so the "narrow fact" is small; and the project's rule is that a quantity which cannot change the verdict should be reported, not gated (§10's spirit).

**Resolution proposed, standing on 2 of 3 unless the Founder overrules:** (a). Replace v0.3's two divergence paragraphs with Gemini's descriptive paragraph (section 5), which reports everything GPT-6's protocol would compute — the distribution of |p_L − p_T|, the share of markets at or above a 0.10 reference line where L is closer to the outcome, and how the group-weighted Brier gain partitions across disagreement levels — as description, with no gate, no support rule, no claim. GPT-6's "narrow fact" can be read from that table; it is not asserted. If the Founder instead keeps (b), GPT-6's Q4 paragraph is adopted verbatim as the protocol, with its permitted and forbidden sentences, and the E1 clause is still rewritten per item 2 (GPT-6 agrees).

## 4. Caught by one reader only

- Gemini: the Brier identity, and its reading that "concentrated where they disagree" is arithmetic. Adopted as the record of why the clause cannot be a finding.
- Gemini: a fixed probability difference is the only scale-consistent reference line in Brier space (a 0.09 gap costs the same whether near 0.02 or near 0.45). Adopted for the descriptive reference line; it does not make 0.10 evidence-based.
- GPT-6: option (c) is not executable as written (no group-level disagreement statistic). Recorded; moot under (a).
- GPT-6: the permitted/forbidden sentence pair for a conditional result. Adopted as reporting guidance if (b) is chosen.

## 5. Consequences for v0.3 → v0.4 (edit list; nothing applied)

- **§1, the claim:** "…forecast real resolved events better than the same agents communicating in text, and is the gain concentrated where the two disagree?" becomes "…better than the same agents communicating in text? How the gain is distributed across levels of disagreement between the two arms is reported, not claimed." (Unanimous item 2; whichever option the Founder picks.)
- **§7, divergence paragraphs:** under (a), replaced by: *"Disagreement reporting (descriptive only). For every market, record |p_L − p_T|, the paired Brier difference Brier_T − Brier_L, and whether L is closer to the realized outcome than T. Report the unconditional distribution of |p_L − p_T| across markets and groups; the decomposition of the primary group-weighted Brier gain across disagreement deciles and above a descriptive reference line of |p_L − p_T| ≥ 0.10, with the count of markets and groups above the line; both resampling intervals where any interval is shown. No secondary pass/fail gate; nothing here alters the PASS/FAIL outcome of the primary endpoint or the gates."* Under (b), GPT-6's Q4 paragraph verbatim.
- **§8 Pass/Fail/Void:** unchanged by this round; "A secondary result never rescues a primary FAIL" stays in §7's reporting line and is restated once in §8.
- **§11:** open question 1 (delta) closed by decision 5; "useful divergence" as a name survives only in §10's list of things not rewarded.

## 6. Decision 5 — for the Founder

Drop (2 of 3) stands unless overruled; keep-with-protocol (1 of 3) is fully specified and can be adopted instead without a further round. Either way, the sentence in §1 changes, because the readers were unanimous that the question it asked cannot be answered by this test. The briefing's own rule holds: no third asking.

## 7. Process notes

Three readers, everything inline; every reader cited blocks and stated vendor and model. Two self-reversals on record (Gemini 3.1 Pro withdrew its own round-5 proposal; GPT-6 corrected two of its own round-5 objections), both on the evidence in the briefing rather than on the other readers' positions, since neither saw this round's other answers. Seventh consecutive round with zero fabricated findings under the v2-defense format. Systems Engine errors this round: none caught; the briefing's E5 wording "A secondary result can never rescue a primary FAIL" was a paraphrase of v0.3 §7's reporting rule presented inside a block of decided text, which is a looser standard than verbatim and is recorded here.
