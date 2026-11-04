**Engine:** Google. **Model:** Gemini 2.5 Pro (as self-reported; round 5's Gemini reader self-reported 3.1 Pro). **Briefing:** 2026-11-03_cold_briefing_v6_adjudication_decision4.md. Tier 3. Filed verbatim.

### Q1 — "survives" for the primary endpoint

**The sensitivity interval must lie entirely above $m$.**

#### Addressing the strongest opposing point

The opposing argument [E4, Gemini 3.1 Pro] points out that coarsening into sensitivity blocks inflates variance without shifting the point estimate, so requiring the wider interval to clear $m$ risks failing a true-but-small effect whose primary lower bound exceeds $m$ and whose sensitivity lower bound exceeds zero (i.e., directional significance survives, but margin clearance does not).

Per E2, the framework already provides an explicit operational disposition for this case:

> "A primary PASS whose sensitivity interval does not clear $m$ is reported as 'not established under the sensitivity partition' and is a FAIL. [...] FAIL means 'did not establish the required advantage,' not 'the advantage is absent.'" [E2]

When a run lands in this region ($LB_{\text{primary}} > m$, but $0 < LB_{\text{sens}} \le m$):

* **How it must be reported:** It is reported as a **FAIL** with the specific finding: *"not established under the sensitivity partition"* [E2].
* **What it licenses the project to say:** It licenses the project to say that a positive directional advantage of latent over text is robust to macro/driver-level clustering ($LB_{\text{sens}} > 0$), and that the advantage exceeded $m$ under the assumption that outcome groups are independent ($LB_{\text{primary}} > m$); but it explicitly **does not** license claiming that an effect exceeding $m$ was proven under dependence coarsening [E1, E4].

Attempting to grant a "PASS" when the sensitivity lower bound only clears zero creates an irreconcilable contradiction with the Founder's core requirement in E1:

> "...the latent arm beats the text arm by more than the pre-registered margin, with error bars." [E1]

If the error bars that define survival allow values down to $\epsilon > 0$, the run has established with 95% confidence under the coarser partition only that the effect is non-zero, not that it clears $m$ [E4].

#### Impact of E6

E6 reinforces this determination. In round 5, the primary statistical objection against "entirely above $m$" was that "broad blocks like D01 and D03" chained via shared tags would artificially coalesce dozens of events into mega-clusters, severely and needlessly blowing up the sensitivity interval [E4, E6].

Under E6(a) and E6(b), bridge nodes are dismantled by restricting assignment to **one main driver tag per event** and splitting broad drivers like D01 [E6]. Because blocks will be smaller and more evenly distributed, the sensitivity resampling variance will not suffer the artificial inflation caused by the earlier multi-tag transitive chaining. The mitigation adopted in E6 directly softens the practical friction raised by the looser reading without sacrificing the rigor demanded by E1.

---

### Q2 — Gate 2 under sensitivity

**Yes, Gate 2 (L beats S, 95% bootstrap interval above zero) MUST also hold under the sensitivity resampling.**

#### Adjudicating the exchange

The argument that Gate 2 under sensitivity is redundant [E5, Gemini 3.1 Pro] relies on the premise that beating text by $m$ under sensitivity already implies beating silence ($S$), unless text communication actively harms the receiver ($Brier_T > Brier_S$). That reader proposes patching this with a primary-level gate or a simple point-estimate requirement ($mean(Brier_S - Brier_T) \ge 0$).

The counter-argument [E5, GPT-6 Astra Pro, Grok 4.7] is correct: **text actively harming silence is precisely the failure mode that requires structural protection under the sensitivity partition.**

1. **Point estimates do not protect against correlated noise:** A point estimate of $mean(Brier_S - Brier_T) \ge 0$ offers no error bounds. Correlated drivers can systematically degrade text drafts on certain slices of events (e.g., compounding misleading narratives across a macro-shock block) while leaving silence unaffected.
2. **The meaning of Gate 2:** Gate 2 exists to prove *usefulness*—that a two-agent communication pipeline actually adds value over an isolated agent [E2]. If Gate 2 does not clear zero under sensitivity, the project cannot assert with cluster-robust confidence that the latent communication mechanism outperforms silence. A run where $L$ beats $T$ simply because $T$ actively disorients agent B under correlated macro conditions does not demonstrate a useful communication channel; it demonstrates an anti-useful text channel.

#### What this choice licenses

Requiring Gate 2 to clear zero under sensitivity licenses the claim that **the usefulness of the latent arm over a single agent is robust to driver-level dependence**, and not an artifact of macro-shock confounding where text collapsed below silence. Permitting Gate 2 to pass only at the primary level licenses only the weaker claim that usefulness holds if outcome groups are independent, leaving open the vulnerability that the advantage over a single agent vanishes under coarser clustering.

#### Impact of E6

E6 does not change the structural logic of Gate 2, but it makes the sensitivity requirement less prone to unwarranted failure. Because E6 prevents massive chained blocks, block-level noise in single-agent baseline performance ($Brier_S$) is far less likely to spuriously widen the Gate 2 sensitivity interval across zero.

---

### Optional

Yes. In E2 (§8, "Pass"):

> "Pass: primary-endpoint interval entirely above the pre-registered margin m under primary-group resampling, AND the sensitivity interval entirely above m (proposed reading of v3's "survives"), AND Gate 1, AND Gate 2, AND L beats BR." [E2]

And earlier in E2 (§8, "Gates"):

> "Whether a gate must also survive sensitivity to count as met is open; the primary endpoint must." [E2]

If the parenthetical *(proposed reading of v3's "survives")* is replaced or interpreted as "sensitivity interval excludes zero", and the open question regarding the gates is left unamended, a run could be labelled PASS while the sensitivity interval only clears zero and Gate 2 only holds on primary groups.

To prevent this and formalize the stricter adjudication across both questions, update the **Pass** definition in E2 to:

> *"Pass: primary-endpoint interval entirely above the pre-registered margin m under primary-group resampling, AND the sensitivity interval entirely above m, AND Gate 1 surviving both primary and sensitivity resampling (intervals excluding zero), AND Gate 2 surviving both primary and sensitivity resampling (intervals excluding zero), AND L beats BR."*

---

**Filing.**
Vendor: Google
Model: Gemini 2.5 Pro
