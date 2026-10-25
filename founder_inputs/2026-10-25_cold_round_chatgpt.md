# Cold round answer — ChatGPT, October 25, 2026

**Engine:** ChatGPT. **Model:** not recorded by the Founder. **Attachments received:** none; it retrieved arXiv 2608.04893v2 itself and quotes Section 3; it states it did not review the September 25 document. **Briefing:** `founder_inputs/2026-10-25_cold_briefing_v1.md` (hash `568b369b6154`). Tier 3. Filed verbatim.

**Flag at filing:** names a paper not in the briefing or the project's feed — *Draft-KV: Learning Useful Latent Communication Between Language Models*, arXiv 2609.34754 — as a near-miss for H3. Not yet read by anyone on the project; its figures below are ChatGPT's reading.

---

# LatentForge — cold review

**My conclusions: Q1—no; Q2—H3 remains unresolved under the stated standard; Q3—the budget comparison is not sufficiently defined; Q4—pause the nightly jobs.**

I received the briefing, but neither of its two referenced attachments. I retrieved **arXiv:2608.04893v2** directly to answer Q1; I have not reviewed the missing September decision document. Project-specific findings below rely on the briefing's labeled evidence blocks.

## Q1. Does Section 3's direct-text arm license a latent-versus-text performance claim?

**No. It does not establish that latent communication performs better, worse, or equivalently to text under controlled conditions. The September 25 correction, as described in E7, is supported.**

Section 3, under **"Intervention arms,"** states:

> "This last arm is a validity calibration, not a medium comparison: … we never interpret it as a text-channel baseline."

The omitted portion explains that the intervention changes both information availability and the receiver's final prompt. The direct-text arm checks whether the receiver can solve the task when the private information is supplied visibly; it does not isolate the effect of the communication medium.

Consequently, the paper's **±2.8-point bound concerns correctly paired versus mismatched caches**. It is not a bound on the performance difference between latent and text communication. **[E7]**

You can report the observed scores of the paper's individual configurations, with their conditions attached. You cannot turn that descriptive comparison into a conclusion about which channel is superior.

## Q2. Is H3 still open, given E7 and E8?

**Yes—H3 remains unresolved by the evidence supplied. I have not verified a paper meeting all the requested conditions simultaneously: shared information, a strong text comparator, matched resource budgets, and uncertainty estimates for the latent-minus-text difference.**

That is a bounded conclusion about the evidence reviewed. **E9 explicitly prevents treating the scan as proof that no qualifying paper exists.**

| Evidence | What it establishes or reports | Why it does not settle H3 |
|---|---|---|
| **E7: LatentMAS** | Efficiency improvements and reported accuracy gains over text systems. | The briefing reports no uncertainty estimates for the gains and does not establish the required strong-text, matched-budget comparison. |
| **E7: causal audits** | Evidence about the contribution of correctly paired latent content. | Their pairing comparison answers a different question from H3. |
| **E8: LatCom, LatComm, CondenseFlow** | Compression, speed, memory, or task-performance results. | **No evidence in briefing** that these results meet every H3 comparison requirement. |
| **E8: FIBS and DiscoveryRSI** | Hidden-state detection and evaluation of generated hypotheses, respectively. | Neither described result is the required latent-versus-text experiment. |

There are two relevant qualifications from checking the primary literature.

**First, LatentMAS does contain a communication-medium ablation.** However, its hybrid text arm transmits only the **last 128 decoded tokens**. That comparison does not establish performance against the full written-reasoning comparator proposed in your plan. It would therefore be inaccurate to say nobody has compared the media; the issue is whether the comparison meets H3's standard.

**Second, I found a close candidate outside the briefing: _Draft-KV: Learning Useful Latent Communication Between Language Models_, arXiv:2609.34754.** Its public protocol gives both models the same question and compares latent transmission with the same generated draft supplied as text. However, its reported MMLU-Redux cost comparison uses **13.745 TFLOPs for Draft-KV versus 7.187 TFLOPs for Text-to-Text**. That is a relevant comparison, but it does not establish H3 at matched compute.

**My assessment is that H3 remains a legitimate empirical question, while the claim that it represents untouched territory would be unsupported.** **[E7–E9; external checks above]**

## Q3. What is the single biggest reason step 4 could produce an uninterpretable result?

**The experiment could confuse a communication advantage with an unequal amount of computation.**

Step 4 promises a **"matched token budget"** while comparing a latent cache relay with the sender's **"full written reasoning."** It does not define the accounting that makes those allowances comparable. There is **no evidence in briefing** that the proposed arms have matched end-to-end computation, and no existing matched experiment supplies that missing foundation. **[§5, step 4; E2]**

The problem is straightforward: using the same checkpoint and providing the same original question controls the model and the starting information. It does not, by itself, control the work performed by the sender and receiver. Counting emitted text tokens alone leaves unspecified how to charge latent processing, cache construction or reuse, and the receiver's processing of the message.

That creates an ambiguity in either direction. A latent win could reflect a larger computational allowance. Alternatively, forcing the text arm's "full written reasoning" into a superficial token match could truncate the very comparator the experiment promises to test. These are possible outcomes of the unspecified budget rule, not claims about an implementation I have inspected.

The mismatched-cache arm does not resolve this issue: it tests whether the correct cache pairing matters. **[E7]**

**The repair is to define one primary end-to-end resource budget before preregistration.** For example, use a specified inference-compute allowance, account for all sender and receiver operations, and let each system use that allowance through a documented procedure. Report elapsed time, memory, and token counts separately, and fix the rule for traces that would exceed the allowance.

There is no need to require that the two messages contain the same number of bits. Conveying more useful information within the same resource allowance could be precisely the advantage being tested. The requirement is that **"latent wins at budget B" has a clear, auditable meaning.**

## Q4. Pause, fix sleep first, or leave running?

**Pause all nightly jobs while the direction is decided.** The fail-loud fix has prevented new junk, but six real outputs in 34 days and a registry with no loaded consumer do not justify making host-sleep repair the next priority. **[E4–E5]**

## Optional — the decision I would add

**Add a feasibility gate at the beginning of the same timebox, without extending the kill date:** demonstrate the resource accounting and a functioning paired comparison on separate development items before committing to the production experiment. E1 establishes steering in one configuration; E2 supplies no valid channel comparison; E3 removes the claimed compression foundation; and E7–E8 show substantial work elsewhere on the underlying capabilities. Those blocks justify ending open-ended development and making further work conditional on one executable, bounded study. If the gate cannot be passed using the existing machinery, archive without launching the production study. If the study finishes without a convincing advantage, stopping can still be the correct project decision—but an interval that includes both zero and a worthwhile benefit would mean **inconclusive evidence**, not scientific disproof of H3. **[E1–E3, E7–E8; §5, steps 0–4]**
