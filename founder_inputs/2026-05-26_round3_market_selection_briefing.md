# Mode 1 market selection — multi-engine briefing (Round 3)

**Date:** May 26, 2026 morning
**Context:** Round 3 of multi-engine review on Mode 1 architecture. Round 1 (May 25 morning) proposed selection criteria. Round 2 (May 25 afternoon) confirmed surface choice — three engines independently recommended hybrid surface; Founder Engine overrode and locked Polymarket-primary with four explicit reasons. Round 3 (this briefing) asks: which 8 specific Polymarket markets, by slug/condition ID, best fit the locked criteria from a live qualifying pool of 298 markets pulled May 26 morning?

**Maintainer:** John McGuire (Founder Engine), with Claude (Systems Engine)

**Cross-references:**
- `founder_inputs/2026-05-25_afternoon_step7_founder_synthesis.md` (the six locked decisions — canonical record)
- `founder_inputs/2026-05-25_afternoon_mode1_surface_round2_briefing.md` (Round 2 briefing, format inherited here)
- `founder_inputs/2026-05-25_afternoon_mode1_surface_round2_responses.md` (Round 2 engine responses verbatim)
- `founder_inputs/2026-05-26_session_handoff.md` (May 26 session handoff, includes structural finding about daily pull)
- `scratch/qualifying_pool_2026-05-26.json` (the 298-market source pool this briefing draws from)
- `docs/intent.md`, `docs/state_manifest.md`, `docs/build_log.md` (Trinity + architecture log)

---

## How to read this briefing

This briefing has eight sections. Read all eight before answering the questions at the end.

The questions in Section 8 ask you to select **8 specific Polymarket markets, by slug and condition ID, from a qualifying pool of 298 markets that already passed the locked criteria.** This is a selection question within a locked surface, not a surface-relitigation question.

The Round 2 surface decision (Polymarket-primary, Variant A holds) is locked. The Founder Engine overrode triple-engine convergence on hybrid surface and articulated four explicit reasons for the override. The legitimate triggers for re-opening Decision 2 are documented in the Step 7 synthesis doc; today's task is not one of them. Do not relitigate the surface in Round 3.

You DO have permission to push back on:
- Pool quality (if the pool is too domain-skewed for clean 8-market selection)
- Liquidity floor (which was explicitly deferred from Step 7 to "decide when looking at actual candidate markets")
- Individual market selection within the pool (which 8 best fit the criteria)
- "Weak language priors" exposure of individual markets in the pool (A-1 from Round 2, preserved as future-audit watch item)

You DO NOT have permission to recommend:
- Adding non-Polymarket markets to the registry (Decision 2 locked)
- Changing the count from 8 (Decision 5 locked at 8, not 9 or 10)
- Changing the 14-90 day cadence (Decision 4a locked)
- Adding the synthetic/OpenSpiel/dataset hybrid surface (Decision 2 locked)

The data in Section 5 is live as of May 26, 2026 morning (full-surface API probe, not the daily 200-by-volume pull which was found to be a 1% biased sample — see Section 4).

The April 15 result in Section 6 is the project's strongest verified internal evidence about what the system can do, preserved verbatim from Round 2 for context.

---

## Section 1: The thesis (T-tags, verbatim from Round 2)

Verbatim from `docs/intent.md`, with T-tag annotations for response citation.

**T-1.** "AI agents currently coordinate by converting rich internal mathematical states ('hidden states') into human language, transmitting words, then reconstructing meaning on the other side. This translation is lossy, expensive, and forces agents to reason inside the boundaries of human concepts."

**T-2.** "LatentForge removes the translation. Agents communicate in their own latent space — compressed vector deltas against a shared seed — while a **Shadow Self** governance layer (specified, not yet operational) is designed to translate every exchange into human-readable audit logs in real time."

**T-3.** This is meant to produce two things text-agents structurally cannot:
- **Cheaper coordination** — 30-100x less compute per exchange.
- **Useful divergent thinking** — insights that exist in the geometry of the data but have no clean linguistic description. Text-based agents are structurally blind to these signals.

**T-4.** "The motor-car question is whether [useful divergent thinking] is real. Everything in this project serves that question."

**T-5.** From the same file under "Primary Strategic Bet": "Latent-space coordination produces useful divergence that text-based systems cannot, and this must be rigorously measured on live adversarial markets before any claim goes outside. The scientific arm establishes whether the physics works. The revenue-exploration arm finds where it applies. Neither is allowed to lead on narrative until the other confirms on measurement."

---

## Section 2: The proof architecture and locked decisions (P-tags + L-tags)

Verbatim from `docs/intent.md` (P-tags) and from the Step 7 synthesis doc (L-tags for locked Step 7 decisions).

**P-1. Two arms, both running. Neither is optional.**

**P-2. Scientific arm.** "Does the thesis work? Mac Mini M4 Pro runs activation steering experiments, bidirectional fix attempts, and four-arm benchmark runs against Phi-3 Mini. Output: reproducible latent-communication physics."

**P-3. Revenue-exploration arm.** "Where does the thesis apply? Three components working in parallel:
1. **Polymarket as the starting validation surface.** Small real-money bets once the benchmark is honest. Chosen as a hard, adversarial, ground-truth-resolved environment — if latent agents can produce alpha here, the thesis is unassailable.
2. **Revenue-exploration agents** (revenue-strategist, commercialization-agent) scan daily for opportunities beyond Polymarket — weather arbitrage, enterprise governance, synthetic alpha, dataset licensing.
3. **Founder inputs pipeline** — human-layer feed of discoveries automated agents cannot see."

**P-4. The $10M threshold.** "$10M of verifiable real-world performance before going outside. Combined across whatever channels work. Not a revenue target to optimize — a pre-commitment against self-promotion without proof."

**P-5. Measurable proof targets:**
- *Divergence target:* Latent agents must be >1.5× more divergent than the text baseline on **OpenSpiel**.
- *V0.1 proof target:* Two agents communicating via latent deltas with Shadow Self translation must show compute savings ≥30% per turn plus a novel-solutions count distinguishable from text-only communication.

**P-6. Mode 1 architecture (locked May 24).** Variant A: Mode 1's registry holds explicit Polymarket slugs/condition IDs. 8-12 markets. Immutable within a version. When a market retires, the registry hard-fails on that slug. Founder makes an explicit logged decision to iterate to v2 with new slugs. Silent 0.5 fallback dies in the rebuild. Replaced with explicit `NO_LIVE_MARKET` state.

**P-7. Founder Decision 1 (locked May 25).** Mode 1 plays role **(c) — both jobs**: must support divergence measurement AND outcome-based calibration.

---

**The six locked Step 7 decisions from May 25 (L-tags):**

**L-1. Mode 1 role.** (c) Both jobs — divergence AND calibration.

**L-2. Surface.** (d) Polymarket primary. Variant A holds. Founder Engine override against three-engine convergence on hybrid; four explicit reasons preserved in synthesis doc Decision 2 section. **Locked.**

**L-3. Convergent criteria (all five locked):**
1. Resolution clarity must dominate liquidity — binary outcomes with verifiable external resolution sources
2. Exclude sports and tennis-microcontracts
3. Crowd uncertainty band 15-80% at selection time
4. Resolution source must be a trusted external official source
5. Domain mix favoring macro/policy/geopolitics/AI-tech over noise categories

**L-4. Divergent criteria items:**
- **Cadence:** Strict 14-90 days (Gemini's rule, locked)
- **Liquidity floor:** Deferred to Round 3 (this briefing). To be decided when looking at actual candidate markets.
- **"Weak language priors" criterion:** ChatGPT's argument (A-1) preserved as future-audit watch item. If after 30 days of operating Mode 1 the latent arm fails to demonstrate edge against the text arm, this argument is the first thing to re-examine before concluding the thesis is wrong.

**L-5. Number of markets.** 8 (not 9, not 10, not 12).

**L-6. Round 2 structure (meta).** All six decisions synthesized in same session (May 25 afternoon). N/A for Round 3.

---

## Section 3: Anti-anchoring framing — read this carefully

This section's purpose is the same as Round 2's anti-anchoring section: give engines explicit permission to push back where pushback is legitimate, and explicit restraint where it isn't. The framing is flipped from Round 2 because Round 3 is a different kind of task.

**Round 2 was a surface-selection task.** Engines had permission to retire Variant A entirely if their honest assessment was that Polymarket was the wrong surface. They used that permission — all three recommended hybrid. Founder overrode.

**Round 3 is a within-surface selection task.** The Founder override is now part of the audit trail. Round 3's job is to pick 8 specific markets within the Polymarket-primary architecture, applying the locked criteria to the live qualifying pool.

**Permission, stated explicitly:**

You have permission to push back on:

1. **Pool quality.** If the qualifying pool is too domain-skewed (e.g., 60+ governor primaries crowd out other domains), too short-horizon-clustered (e.g., many markets resolve on the same day, creating longitudinal-comparison fragility), or has any other structural property that makes clean 8-market selection difficult, name it. The Founder needs to hear this.

2. **Liquidity floor recommendation.** Decision 4 explicitly deferred this to "when looking at actual candidate markets, not in the abstract." Now you are looking at the actual markets. Recommend a floor (in dollars) based on what you see. The floor will affect which markets in the pool are realistically tradable for the four-arm benchmark.

3. **Individual market weaknesses.** Per the "weak language priors" watch item (A-1 from Round 2): some markets in the pool are heavily narrative-mediated ("Will X have the best AI model"). Some are numerical-band ("Will China GDP growth in Q2 2026 be between 4.6% and 4.9%"). If you think specific markets in the pool are weak tests of the latent thesis, name them. The Founder needs to weigh this in selection.

4. **The structural finding about the daily pull.** The May 26 morning session discovered that the polymarket-pull launchd job has been returning 93 markets per day because parameterized as "top 200 by volume." Actual Polymarket active surface is 10,000+ markets. This briefing's pool comes from a full-surface API probe, not the daily pull. If you have concerns about this — e.g., reproducibility of the pool, what the launchd job's `VALID: yes` designation in `state_manifest.md` should become, whether the launchd job should be fixed before Round 3 selection is finalized — name them. This finding is documented for separate work-block remediation, but flagging concerns here is legitimate.

**You do NOT have permission to recommend:**

1. **Retiring or modifying Variant A.** The Founder Engine override on Decision 2 is locked. The legitimate re-open triggers are documented in the synthesis doc; today's task is not one of them. Do not propose hybrid surfaces, non-Polymarket markets, OpenSpiel-as-supplement, or any architectural change to the registry's composition.

2. **Changing the 8-market count.** Decision 5 is locked at 8. Do not propose 6, 9, 10, 12, or any other number.

3. **Changing the 14-90 day cadence.** Decision 4a is locked. Do not propose widening to 14-180 days even if specific compelling markets fall outside the window.

4. **Retiring the "exclude sports" criterion.** Decision 3 is locked.

**Why these restraints matter:**

The May 25 anti-anchoring framing in Round 2 was deliberately permissive because the question was "is the surface right?" Engines used that permission and reached convergence on hybrid. The Founder weighed that convergence and overrode. The override is now Tier 2 locked discipline (Founder Engine has final authority per `docs/intent.md` "How this project works" section).

If Round 3 were to relitigate the surface — even implicitly, by recommending markets that conveniently happen not to exist in Polymarket and therefore require a hybrid — that would be the override's first legitimate-trigger event, but the trigger is "30+ days of operating Mode 1, latent arm fails to demonstrate edge," not "next-day reconsideration."

Within-surface pushback is welcome and important. Surface-relitigation is not. The distinction matters.

---
## Section 4: Pool quality observations

The qualifying pool for Round 3 was generated by a full-surface API probe on May 26 morning (paging the Polymarket Gamma API to exhaustion), then filtering against the five locked criteria from L-3 and the 14-90 day cadence from L-4. The probe and filter scripts are committed at `scratch/probe_polymarket_api.py` and `scratch/full_pull_and_filter.py`. The resulting pool is saved at `scratch/qualifying_pool_2026-05-26.json`.

**M-1. Pool size.** 298 markets passed all five locked criteria. This is the source pool Round 3 selects from.

**M-2. Structural finding about the daily pull (relevant context).** During Round 3 prep, the daily `polymarket-pull` launchd job was found to return 93 markets per day, not because of a bug but because of a deliberate-but-mismatched parameter: `limit=200, order=volume, ascending=false`. The intent was "pull the top 200 highest-volume markets." The mismatch is that high volume on Polymarket today means novelty (GTA VI, Jesus Christ return), short-horizon sports, and microcontracts — not the macro/policy/geopolitics/AI-tech markets Mode 1 was designed for. The actual Polymarket active surface is 10,000+ markets. The 93 returned by the daily pull is a 1% sample biased toward the wrong domains. **This is documented in `founder_inputs/2026-05-26_session_handoff.md` as a finding for separate remediation. It does not block Round 3 because Round 3 uses the full-surface probe.** Engines should be aware that `state_manifest.md` currently designates polymarket-pull as `VALID: yes` but this designation is now questionable; probably belongs at `VALID: limited` with a scope note. Out of Round 3 scope; preserved here for transparency.

**M-3. Domain breakdown of the 298-market pool (before "other" trimming):**

| Domain | Count |
|---|---|
| macro | 5 |
| policy | 18 |
| geopolitics | 62 |
| ai-tech | 21 |
| crypto | 5 |
| other | 187 |

**M-4. The "other" bucket was trimmed.** The 187 "other" markets are mostly leaked sports/esports (Vitality, Team Spirit, LCK, IEM Cologne) and novelty (Jesus Christ return, Rihanna album, Playboi Carti album) that the keyword filter missed. Hand-inspection of the top 30 by liquidity in the "other" bucket revealed approximately 18 real macro/policy/geopolitics candidates whose slugs did not match the domain keyword lists. 13 were retained for this briefing (the slug matching had a 5-slug gap due to slug-truncation issues during inspection; transparent disclosure). **These were retained and surfaced explicitly in Section 5 below under a new "Other (curated)" domain group.** The remaining 174 junk markets in "other" were dropped from the briefing. Engines should know: the trimming step was Systems Engine hand-curation, not Founder-locked logic; if you think a specific "other" candidate is mis-trimmed in either direction, name it.

**M-5. Honest pool shape after trimming:**

| Effective domain (post-trim) | Count |
|---|---|
| macro (named) | 5 |
| macro/commodities (from "other") | 7 (Crude Oil 4, Gold 2, Silver 1) |
| policy (named) | 18 |
| policy (from "other") | 5 (Trump AG, Switzerland 2, Kash Patel, Lee Zeldin) |
| geopolitics (named) | 62 |
| geopolitics (from "other") | 1 (Hormuz only — Starmer/Cuba/Hezbollah/Machado/US-Cuba may not have matched curated keep-list; verify in Section 5) |
| ai-tech | 21 |
| crypto | 5 |
| Total available for selection | ~124 |

**M-6. Pool quality observations worth surfacing:**

- **Macro is genuinely thin and short-horizon-clustered.** The two highest-liquidity macro markets are Fed rate cut markets resolving in 22 days. A 22-day resolution gives 1-2 four-arm benchmark cycles before the market is gone; the longitudinal-comparison value is limited. The third macro market (China GDP) sits at $4K liquidity.

- **Geopolitics is heavy on US state primaries and the Colombian presidential election.** 62 named geopolitics markets, but a substantial fraction are state governor primaries (one per state, many states) and Colombian first-round candidates. Real, resolvable, but domain-skewed toward electoral predictions specifically.

- **AI-tech has the strongest pool quality of any domain.** "GPT-6 before GTA VI" at $40K liquidity, "Anthropic best model end of June" at $28K, "Google best model end of June" at $24K. Real liquidity, real adversarial uncertainty. The trade-off: 19 of 21 AI-tech markets resolve on the same day (June 30, 2026), creating longitudinal-comparison fragility if multiple AI-tech markets are picked.

- **The "Israel x Iran permanent peace deal by June 30" market** is the highest-liquidity market in the entire qualifying pool ($102K), 35-day resolution, 15% YES, real binary outcome with clear external resolution source. Worth special attention.

**M-7. The "weak language priors" tension in the pool (A-1 from Round 2, made concrete).**

The locked criterion A-1 (preserved as future-audit watch item) was ChatGPT's Round 2 argument that prediction markets are heavily linguistically-mediated by construction — possibly the worst surface for proving the latent thesis. Looking at the actual pool, this tension is concrete:

- **Markets LEAST exposed to weak language priors (best test of latent thesis):**
  - Numerical-band markets: "Will China GDP growth in Q2 2026 be between 4.6% and 4.9%?", "Will Crude Oil hit $120 by end of June?", "Will Gold (GC) hit low $4,300 by end of June?", "Will Silver settle at $60-$70 in June?"
  - Date-threshold markets with external official resolution: "Strait of Hormuz traffic returns to normal by end of June?" (binary, externally resolved)

- **Markets MOST exposed to weak language priors (heavily narrative-mediated):**
  - "Will Anthropic have the best AI model at the end of June 2026?" (subjective, requires consensus judgment)
  - "Will GPT-6 be released before GTA VI?" (event-defined, somewhat narrative)
  - "Will [politician] be out by June 30?" (definition of "out" can be contested)

This tension is NOT a reason to bias selection toward only numerical markets — domain mix is locked (L-3) and macro/policy/geopolitics/AI-tech all matter. But engines should weigh this tension in selection. The Founder may prioritize numerical-band markets where they exist in the right domains, accepting narrative markets where they don't.

**M-8. Liquidity floor question.** The pool liquidity ranges from $1 to $194K. Approximate distribution:
- Above $50K liquidity: ~5 markets
- $20K-$50K: ~15 markets
- $10K-$20K: ~30 markets
- $5K-$10K: ~35 markets
- Below $5K: ~40 markets

A liquidity floor at $10K eliminates ~80 markets but keeps ~50. A floor at $5K keeps ~85. A floor at $20K keeps ~20. The trade-off is between "tradable for real-money paper-trading" (higher floor) and "domain mix achievable" (lower floor — needed because macro is so thin).

---

## Section 5: The qualifying pool (sorted by liquidity within domain)

The 298-market pool, after trimming the "other" bucket from 187 to 13 real candidates per Section 4 M-4. Total markets shown below: 124.

### MACRO (5)

**Q:** Fed rate cut by October 2026 meeting?
- slug: `fed-rate-cut-by-october-2026-meeting-199-747`
- conditionId: `0x4092815fea8f91e60586882d45fa2f61bfca8a36d595f47fdea9eec5d2893025`
- YES: 19% | resolves: 2026-06-17 (22 days) | volume: $46,363 | liquidity: $19,403
- tags: macro

**Q:** Fed rate cut by December 2026 meeting?
- slug: `fed-rate-cut-by-december-2026-meeting`
- conditionId: `0xc60022fe066abd6f96c375adb09f38d92c4931f09c10b805354581b4e5465e93`
- YES: 32% | resolves: 2026-06-17 (22 days) | volume: $120,718 | liquidity: $15,733
- tags: macro

**Q:** Will China GDP growth in Q2 2026 be between 4.6% and 4.9%?
- slug: `will-china-gdp-growth-in-q2-2026-be-between-4pt6-and-4pt9`
- conditionId: `0x800be7611c7efcdf5827c049e0baac8b6047b506af412e283dbac9ce7e202560`
- YES: 50% | resolves: 2026-07-16 (51 days) | volume: $8,581 | liquidity: $4,094
- tags: macro, geopolitics

**Q:** Will China GDP growth in Q2 2026 be between 4.9% and 5.2%?
- slug: `will-china-gdp-growth-in-q2-2026-be-between-4pt9-and-5pt2`
- conditionId: `0x4af115cc5eadfbaa831523a17f297842011e6ba4175fc194b6d1e5e862193077`
- YES: 37% | resolves: 2026-07-16 (51 days) | volume: $4,334 | liquidity: $3,845
- tags: macro, geopolitics

**Q:** Will S&P 500 (SPX) hit $7,700 (HIGH) in June?
- slug: `spx-hit-7700-high-jun-2026-675`
- conditionId: `0x0357f760e337c64f62a83f89f0bc99faf22778453188878330cc39a535eaf68a`
- YES: 44% | resolves: 2026-06-30 (35 days) | volume: $15,791 | liquidity: $3,585
- tags: macro


### POLICY (18)

**Q:** Will Kim Farington be the Republican nominee for Senate in Virginia?
- slug: `will-kim-farington-be-the-republican-nominee-for-senate-in-virginia`
- conditionId: `0x151f00b091b2e346656190b49c06644920fdba4f1280f7976e7f5f6bdfec7bb3`
- YES: 30% | resolves: 2026-06-16 (21 days) | volume: $458,188 | liquidity: $22,599
- tags: policy

**Q:** Will Marquita Bradshaw be the Democratic nominee for Senate in Tennessee?
- slug: `will-marquita-bradshaw-be-the-democratic-nominee-for-senate-in-tennessee`
- conditionId: `0x253a4a01dd09a35fd73e6671ddaacada7af886af4d5c196dfc9a6d50b1e735ba`
- YES: 76% | resolves: 2026-08-06 (72 days) | volume: $4,012 | liquidity: $10,606
- tags: policy

**Q:** Will Bert Mizusawa be the Republican nominee for Senate in Virginia?
- slug: `will-bert-mizusawa-be-the-republican-nominee-for-senate-in-virginia`
- conditionId: `0x114ba3133f9949f6a34f75caf515b6eb43eecf19a71958fdb0950f4bd94cf10e`
- YES: 49% | resolves: 2026-06-16 (21 days) | volume: $11,284 | liquidity: $6,367
- tags: policy

**Q:** SCOTUS bars counting mail ballots after election day?
- slug: `scotus-bars-counting-mail-ballots-after-election-day`
- conditionId: `0xd73237bb27cdc455578e9a0788c358bd79609d394f43a270bde10cde4788105f`
- YES: 72% | resolves: 2026-08-01 (67 days) | volume: $40,189 | liquidity: $5,349
- tags: policy, geopolitics

**Q:** No change in Bank of Japan’s interest rates after the June 2026 meeting?
- slug: `no-change-in-bank-of-japans-interest-rates-after-the-june-2026-meeting`
- conditionId: `0xe2fc1b6f5e644f939e090c42c309a498db86fb3bc20c02f05021ab42f1567de7`
- YES: 20% | resolves: 2026-06-16 (21 days) | volume: $46,261 | liquidity: $4,944
- tags: policy

**Q:** Bank of Japan increases interest rates by 25 bps after the June 2026 meeting?
- slug: `bank-of-japan-increases-interest-rates-by-25-bps-after-the-june-2026-meeting`
- conditionId: `0xb3237c597bd198f2e5af2d9c2597c71cdda3ab88649a410a917798b3eec8cff4`
- YES: 76% | resolves: 2026-06-16 (21 days) | volume: $47,119 | liquidity: $4,406
- tags: policy

**Q:** Law banning sports prediction markets enacted in 2026?
- slug: `law-banning-sports-prediction-markets-enacted-in-2026`
- conditionId: `0x3ef18432c0e44e0a28b75d0950aa2d187a8f6e9aff6d5b56147693b6ddc235b4`
- YES: 21% | resolves: 2026-06-30 (35 days) | volume: $14,446 | liquidity: $3,229
- tags: policy

**Q:** Will Jim Priest be the Democratic nominee for Senate in Oklahoma?
- slug: `will-jim-priest-be-the-democratic-nominee-for-senate-in-oklahoma`
- conditionId: `0xac50f53a650c8de904c6944b02758d2c156409b8578a7d6838cdede8fc6cc7ba`
- YES: 26% | resolves: 2026-06-16 (21 days) | volume: $4,464 | liquidity: $2,925
- tags: policy

**Q:** Will the Bank of Korea make no change to the base rate after the July Meeting?
- slug: `will-the-bank-of-korea-make-no-change-to-the-base-rate-after-the-july-meeting`
- conditionId: `0x532bc7c57ab441649590c6d3477c7ec1cf145914d5aebc5f0580c6d2a81e0526`
- YES: 44% | resolves: 2026-07-16 (51 days) | volume: $2,871 | liquidity: $2,634
- tags: policy

**Q:** Will the Bank of Israel make no change to the Bank of Israel Interest Rate after the July decision?
- slug: `will-the-bank-of-israel-make-no-change-to-the-bank-of-israel-interest-rate-after-the-july-decision`
- conditionId: `0x17c51c52caf554ca5337fb1391dae64e2b9dda236ff5725e27191faae96e1b83`
- YES: 42% | resolves: 2026-07-06 (41 days) | volume: $853 | liquidity: $2,153
- tags: policy, geopolitics

**Q:** Will the Bank of Korea increase the base rate after the July Meeting?
- slug: `will-the-bank-of-korea-increase-the-base-rate-after-the-july-meeting`
- conditionId: `0x4961d77539d2ae985a957254aa479a1cf95394be11d03b4a39be8278695f6e5a`
- YES: 56% | resolves: 2026-07-16 (51 days) | volume: $4,021 | liquidity: $1,847
- tags: policy

**Q:** Will the Bank of Israel decrease the Bank of Israel Interest Rate after the July decision?
- slug: `will-the-bank-of-israel-decrease-the-bank-of-israel-interest-rate-after-the-july-decision`
- conditionId: `0xac8094e49053b7b8db7e434a0703db67b12d85e40335950afec12ed995f0fc8b`
- YES: 56% | resolves: 2026-07-06 (41 days) | volume: $723 | liquidity: $1,614
- tags: policy, geopolitics

**Q:** Will N’Kiyla “Jasmine” Thomas be the Democratic nominee for Senate in Oklahoma?
- slug: `will-nkiyla-jasmine-thomas-be-the-democratic-nominee-for-senate-in-oklahoma`
- conditionId: `0x1f1c63908f6c1e3b49559fa80ddef36baa9c5482d52e6a7852c90303807ee22e`
- YES: 53% | resolves: 2026-06-16 (21 days) | volume: $2,214 | liquidity: $1,514
- tags: policy

**Q:** Will Billy Webster win the 2026 South Carolina Governor Democratic primary election?
- slug: `will-billy-webster-win-the-2026-south-carolina-governor-democratic-primary-election`
- conditionId: `0x5c8dc748cfec530d07f450add0f80996a742d36d532058b39bd561cd6e67d841`
- YES: 16% | resolves: 2026-06-09 (14 days) | volume: $300 | liquidity: $799
- tags: policy, geopolitics

**Q:** Will the Central Bank of Colombia announce an increase at the June meeting?
- slug: `will-the-central-bank-of-colombia-announce-an-increase-at-the-june-meeting`
- conditionId: `0xde7971d294b406b3184545a9295b01ba25d45e0358108710986c0b5b1393c478`
- YES: 49% | resolves: 2026-06-30 (35 days) | volume: $1,078 | liquidity: $688
- tags: policy

**Q:** Will another AI-generated song reach number 1 on any Billboard chart by June 30?
- slug: `will-another-ai-generated-song-reach-number-1-on-any-billboard-chart-by-june-30`
- conditionId: `0x5074bb49c52a2d552bc45f044419f2168ade7cc5072762a47b257d076ca820bf`
- YES: 35% | resolves: 2026-06-30 (35 days) | volume: $6,219 | liquidity: $646
- tags: policy

**Q:** Will the Central Bank of Colombia announce no change at the June meeting?
- slug: `will-the-central-bank-of-colombia-announce-no-change-at-the-june-meeting`
- conditionId: `0xdb57f9b9232a158cb5837b0d33ff54d61cdb8cce1ab4c9cd2a2bf57b284d5d22`
- YES: 61% | resolves: 2026-06-30 (35 days) | volume: $1,581 | liquidity: $431
- tags: policy

**Q:** Will Elon Musk Testify to Congress about Epstein?
- slug: `will-elon-musk-testify-to-congress-about-epstein`
- conditionId: `0x919accaaa0401567e47dc9e7e2acaab929d9750a6af2f9264cc5c4d389e957fa`
- YES: 17% | resolves: 2026-06-30 (35 days) | volume: $1,104 | liquidity: $302
- tags: policy


### GEOPOLITICS (62)

**Q:** Israel x Iran permanent peace deal by June 30, 2026?
- slug: `israel-x-iran-permanent-peace-deal-by-june-30-2026-262`
- conditionId: `0x5efa976ebe94080bbda7e45605333ff8f30156cc91604d66c41eb52fd3e25f3e`
- YES: 15% | resolves: 2026-06-30 (35 days) | volume: $557,852 | liquidity: $102,133
- tags: geopolitics

**Q:** Will Ivan Cepeda Castro win the 2026 Colombian presidential election?
- slug: `will-ivan-cepeda-castro-win-the-2026-colombian-presidential-election`
- conditionId: `0x0fb006e0c06caa4db12f7e30ec8c2483d658f83eb57b2ee8eb478e39beca3dfd`
- YES: 27% | resolves: 2026-06-21 (26 days) | volume: $1,419,209 | liquidity: $84,484
- tags: geopolitics

**Q:** Will Abelardo de la Espriella  win the 2026 Colombian presidential election?
- slug: `will-abelardo-de-la-espriella-win-the-2026-colombian-presidential-election`
- conditionId: `0xfbe85201ab2b4acff01cd5a3639039fc813d3448c64db081f70926bd9b9e74e9`
- YES: 70% | resolves: 2026-06-21 (26 days) | volume: $1,577,283 | liquidity: $80,993
- tags: geopolitics

**Q:** Iran agrees to surrender enriched uranium stockpile by June 30, 2026?
- slug: `iran-agrees-to-surrender-enriched-uranium-stockpile-by-june-30-2026`
- conditionId: `0x6cb3ec9e0fb1c258898f648f8b33422f59ba3e8a71aee551449d7cb147bb8ead`
- YES: 19% | resolves: 2026-06-30 (35 days) | volume: $2,659,088 | liquidity: $63,806
- tags: geopolitics

**Q:** Will China invades Taiwan before GTA VI?
- slug: `will-china-invades-taiwan-before-gta-vi-716-644`
- conditionId: `0x7b49b9bacb5f435bc10f3b100ff59e2fdd346f7f92a9001881bc9825a0af0f11`
- YES: 50% | resolves: 2026-07-31 (66 days) | volume: $1,843,497 | liquidity: $52,465
- tags: geopolitics

**Q:** Will no qualifying diplomatic US-Iran meeting occur by June 30, 2026?
- slug: `will-no-qualifying-diplomatic-us-iran-meeting-occur-by-june-30-2026-673`
- conditionId: `0x189c38e8bf3733572f401f8d578099f7233baef3d5fcb438b4eeb0b73bacc787`
- YES: 25% | resolves: 2026-06-30 (35 days) | volume: $1,011,081 | liquidity: $46,874
- tags: geopolitics

**Q:** US-Iran nuclear deal by June 30?
- slug: `us-iran-nuclear-deal-by-june-30`
- conditionId: `0xa70fc3695a65833b91b45df6db6015096f3e1471b70352ca411b4209010e7633`
- YES: 38% | resolves: 2026-06-30 (35 days) | volume: $2,972,334 | liquidity: $45,260
- tags: geopolitics

**Q:** Will the next diplomatic US-Iran meeting be in Pakistan?
- slug: `will-the-next-diplomatic-us-iran-meeting-be-in-pakistan-295`
- conditionId: `0x0f3062f421a43ab9af2f3dc9c3eef48e2aab38a4c9858aca7651947642c4c964`
- YES: 46% | resolves: 2026-06-30 (35 days) | volume: $1,005,911 | liquidity: $43,340
- tags: geopolitics

**Q:** Tamas Sulyok out as President of Hungary by June 30?
- slug: `tamas-sulyok-out-as-president-of-hungary-by-june-30`
- conditionId: `0x2af78d63305bbeeab287701eba943a587357b9c63086603cb85b15d8405e12a7`
- YES: 38% | resolves: 2026-06-30 (35 days) | volume: $247,628 | liquidity: $42,963
- tags: geopolitics

**Q:** Will a team from LPL (China) win MSI 2026?
- slug: `will-a-team-from-lpl-china-win-msi-2026`
- conditionId: `0x9f61a4c01f2c8414b54fae93f7bad383593edea835ccd5c1990fa43422be1634`
- YES: 31% | resolves: 2026-07-12 (47 days) | volume: $21,485 | liquidity: $35,738
- tags: geopolitics

**Q:**  Iran agrees to end enrichment of uranium by June 30?
- slug: `iran-agrees-to-end-enrichment-of-uranium-by-june-30`
- conditionId: `0x9d3f02264a94bafc676afd7add8b11442e6ec72dabaa69cefef835f0672275c7`
- YES: 26% | resolves: 2026-06-30 (35 days) | volume: $1,559,364 | liquidity: $35,675
- tags: geopolitics

**Q:** Trump out as President before GTA VI?
- slug: `trump-out-as-president-before-gta-vi-846`
- conditionId: `0x84f8b70331323c2fba97d7ceaa9a35fb645a0770d0dbff169d07f24f376766e9`
- YES: 50% | resolves: 2026-07-31 (66 days) | volume: $658,232 | liquidity: $32,951
- tags: geopolitics

**Q:** Israeli parliament dissolved by June 30?
- slug: `israeli-parliament-dissolved-by-june-30-228`
- conditionId: `0x3f0bc2757babb8bb9971c9f782fe81f9db734c12d84822f1120a90681c991ff8`
- YES: 55% | resolves: 2026-06-30 (35 days) | volume: $237,072 | liquidity: $28,224
- tags: geopolitics

**Q:** Will Marie Gluesenkamp Perez advance to the general election for WA-03?
- slug: `will-marie-gluesenkamp-perez-advance-to-the-general-election-for-wa-03`
- conditionId: `0xef720745be0a15b63c392854dacae4227a9deafe11fdf6afe79bdf45754dd10a`
- YES: 64% | resolves: 2026-08-04 (70 days) | volume: $7,358 | liquidity: $23,945
- tags: geopolitics

**Q:** Will J.D. Vance attend the next US x Iran diplomatic meeting?
- slug: `will-jd-vance-attend-the-next-us-x-iran-diplomatic-meeting`
- conditionId: `0x7e5228c4aa228752fb75ec1ffcb315a5f2fef812d746ceb6601cee285366d1a8`
- YES: 37% | resolves: 2026-06-30 (35 days) | volume: $672,482 | liquidity: $17,449
- tags: geopolitics

**Q:** Will Haley Stevens win the 2026 Michigan Democratic Primary?
- slug: `will-haley-stevens-win-the-2026-michigan-democratic-primary`
- conditionId: `0x0bde18e0a0220d1f97173850504a1ed4fa90ef2c6a7bc0932952790053ca0c0e`
- YES: 15% | resolves: 2026-08-04 (70 days) | volume: $35,884 | liquidity: $16,619
- tags: geopolitics

**Q:** Will Francesca Hong win the 2026 Wisconsin Governor Democratic primary election?
- slug: `will-francesca-hong-win-the-2026-wisconsin-governor-democratic-primary-election`
- conditionId: `0x00925aafdbb3fbec14b49f343eb430ddb9cc1f827e5934b5513703d13f2851de`
- YES: 27% | resolves: 2026-08-11 (77 days) | volume: $9,940 | liquidity: $15,798
- tags: geopolitics

**Q:** Miguel Díaz-Canel out as President of Cuba by June 30?
- slug: `miguel-daz-canel-out-as-president-of-cuba-by-june-30`
- conditionId: `0x48874462b88af831a4d90479286c6c1d4cd683a6b119d926f85ac66549385b21`
- YES: 17% | resolves: 2026-06-30 (35 days) | volume: $263,180 | liquidity: $15,641
- tags: geopolitics

**Q:** Will Mike Lindell win the 2026 Minnesota Governor Republican primary election?
- slug: `will-mike-lindell-win-the-2026-minnesota-governor-republican-primary-election`
- conditionId: `0xbbd623c4191ca76dec466507375d6df85b403b7e14f9cbd3d09f2c450ae0cd96`
- YES: 26% | resolves: 2026-08-11 (77 days) | volume: $92,145 | liquidity: $15,483
- tags: geopolitics

**Q:** Will Eric Barlow win the 2026 Wyoming Governor Republican primary election?
- slug: `will-eric-barlow-win-the-2026-wyoming-governor-republican-primary-election`
- conditionId: `0xfb481845055afdf15febad269fcb534be4c5e79d5789b72659a036660b46e11b`
- YES: 15% | resolves: 2026-08-18 (84 days) | volume: $18,101 | liquidity: $14,402
- tags: geopolitics

**Q:** Will Jonathan Bush win the 2026 Maine Governor Republican primary election?
- slug: `will-jonathan-bush-win-the-2026-maine-governor-republican-primary-election`
- conditionId: `0xfc500f154bcf7019dbddc34b05266048b5e7a7445f574a89b9d6e16a83ef264d`
- YES: 18% | resolves: 2026-06-09 (14 days) | volume: $16,063 | liquidity: $14,001
- tags: geopolitics

**Q:** Will Phil Weiser win the 2026 Colorado Governor Democratic primary election?
- slug: `will-phil-weiser-win-the-2026-colorado-governor-democratic-primary-election`
- conditionId: `0x6b59b736ef8ec2c0f88139eb426dfcdbe7a0549e3415884f28b07a9b66602544`
- YES: 17% | resolves: 2026-06-30 (35 days) | volume: $14,501 | liquidity: $13,017
- tags: geopolitics

**Q:** Will Steve Witkoff attend the next US x Iran diplomatic meeting?
- slug: `will-steve-witkoff-attend-the-next-us-x-iran-diplomatic-meeting`
- conditionId: `0x7e591fb31786d46761d906abbffbcec8eba519b649909bfb2d7833609a960782`
- YES: 71% | resolves: 2026-06-30 (35 days) | volume: $108,539 | liquidity: $11,687
- tags: geopolitics

**Q:** Will Russia capture Kostyantynivka by June 30?
- slug: `will-russia-capture-kostyantynivka-by-june-30-382-954-769`
- conditionId: `0xb23587fc1e319cdf9aaa12c503f6b2149c820c3d64ded3c98b4ff6719cac78fe`
- YES: 22% | resolves: 2026-06-30 (35 days) | volume: $335,655 | liquidity: $11,486
- tags: geopolitics

**Q:** Will Pamela Evette win the 2026 South Carolina Governor Republican primary election?
- slug: `will-pamela-evette-win-the-2026-south-carolina-governor-republican-primary-election-972`
- conditionId: `0x2ff32cec61a2e9924b5e1207974fdb171efe4568bff1aff58b3d15b26237b36b`
- YES: 36% | resolves: 2026-06-09 (14 days) | volume: $10,037 | liquidity: $10,590
- tags: geopolitics

**Q:** Will Jared Kushner attend the next US x Iran diplomatic meeting?
- slug: `will-jared-kushner-attend-the-next-us-x-iran-diplomatic-meeting`
- conditionId: `0xf0abc9c2b0726ec594aa6547d121e46d5264d778f20acd00689d5c21b5e38d18`
- YES: 53% | resolves: 2026-06-30 (35 days) | volume: $134,241 | liquidity: $10,093
- tags: geopolitics

**Q:** Will Trump attend NATO Summit?
- slug: `will-trump-attend-nato-summit-279`
- conditionId: `0x71ee9c148f0e2b386ba959aca5954c5e6c428695bf1a5fca0af9194f40487758`
- YES: 66% | resolves: 2026-07-08 (43 days) | volume: $13,356 | liquidity: $9,687
- tags: geopolitics

**Q:** Will Nancy Dahlstrom advance from the 2026 Alaska Governor primary election?
- slug: `will-nancy-dahlstrom-advance-from-the-2026-alaska-governor-primary-election`
- conditionId: `0xc42165d729164b01fe0f147307731c8d1cfb0c3e7db1920a83dbf04f751c1127`
- YES: 17% | resolves: 2026-08-18 (84 days) | volume: $12,118 | liquidity: $9,421
- tags: geopolitics

**Q:** Will Alan Wilson win the 2026 South Carolina Governor Republican primary election?
- slug: `will-alan-wilson-win-the-2026-south-carolina-governor-republican-primary-election-725`
- conditionId: `0xfec5e4fb10dd82bc4fb945dfed9c126a244f1bc3311a6a28c7a1515580ebc190`
- YES: 38% | resolves: 2026-06-09 (14 days) | volume: $4,934 | liquidity: $6,976
- tags: geopolitics

**Q:** Will Abdul El-Sayed win the 2026 Michigan Democratic Primary?
- slug: `will-abdul-el-sayed-win-the-2026-michigan-democratic-primary`
- conditionId: `0xca0329cd4392d91e39df0702949229573d2415ae4a37b0103d0c6e9d03b8dd44`
- YES: 54% | resolves: 2026-08-04 (70 days) | volume: $127,375 | liquidity: $6,945
- tags: geopolitics

**Q:** Will Mallory McMorrow win the 2026 Michigan Democratic Primary?
- slug: `will-mallory-mcmorrow-win-the-2026-michigan-democratic-primary`
- conditionId: `0xeb44a06c677ce7a47e5fd2007182e020a577395dc3613ad55d3d576e33964c3d`
- YES: 23% | resolves: 2026-08-04 (70 days) | volume: $43,268 | liquidity: $6,843
- tags: geopolitics

**Q:** Will Brent Hennrich advance to the general election for WA-03?
- slug: `will-brent-hennrich-advance-to-the-general-election-for-wa-03`
- conditionId: `0xe97fd68138299f654dfe7d46c56e86c30b03bd558d121e6380d204dfc016b6a7`
- YES: 21% | resolves: 2026-08-04 (70 days) | volume: $18,607 | liquidity: $6,663
- tags: geopolitics

**Q:** Will Troy Jackson win the 2026 Maine Governor Democratic primary election?
- slug: `will-troy-jackson-win-the-2026-maine-governor-democratic-primary-election`
- conditionId: `0x9e7946bfbc35a400efea548fe34b649fc96893f80c899ae87cb6b5a650907032`
- YES: 42% | resolves: 2026-06-09 (14 days) | volume: $11,625 | liquidity: $6,437
- tags: geopolitics

**Q:** Will Genter Drummond win the 2026 Oklahoma Governor Republican primary election?
- slug: `will-genter-drummond-win-the-2026-oklahoma-governor-republican-primary-election`
- conditionId: `0x6f78fd69fd6dafb695a8f4074dac11971b1da612bd150aa0c837efbd86417292`
- YES: 48% | resolves: 2026-06-16 (21 days) | volume: $116,328 | liquidity: $6,150
- tags: geopolitics

**Q:** Will Matt Claman advance from the 2026 Alaska Governor primary election?
- slug: `will-matt-claman-advance-from-the-2026-alaska-governor-primary-election`
- conditionId: `0x4427ce55f5fc0cc00f2708f914c585442bce7eede689d5daec4671449dc25f8d`
- YES: 39% | resolves: 2026-08-18 (84 days) | volume: $26,787 | liquidity: $5,728
- tags: geopolitics

**Q:** Will Mandela Barnes win the 2026 Wisconsin Governor Democratic primary election?
- slug: `will-mandela-barnes-win-the-2026-wisconsin-governor-democratic-primary-election`
- conditionId: `0x0f1843cae1fa85c263c1f8118554fcff73f8af53d58d0f9fa5283490e69a7d94`
- YES: 54% | resolves: 2026-08-11 (77 days) | volume: $10,548 | liquidity: $5,726
- tags: geopolitics

**Q:** Will Nirav Shah win the 2026 Maine Governor Democratic primary election?
- slug: `will-nirav-shah-win-the-2026-maine-governor-democratic-primary-election`
- conditionId: `0x906842f0acae58e8633c17e933010e1662ca6616fbb3de89f61ff7a3718f5cc7`
- YES: 37% | resolves: 2026-06-09 (14 days) | volume: $10,445 | liquidity: $5,332
- tags: geopolitics

**Q:** Will Robert Charles win the 2026 Maine Governor Republican primary election?
- slug: `will-robert-charles-win-the-2026-maine-governor-republican-primary-election`
- conditionId: `0xfbe834154a7b7d8ec4ccd0f5468b58a113bdbf0e7c0a41876ae8b014ab94631b`
- YES: 70% | resolves: 2026-06-09 (14 days) | volume: $9,152 | liquidity: $5,255
- tags: geopolitics

**Q:** Will Dan Cox win the 2026 Maryland Governor Republican primary election?
- slug: `will-dan-cox-win-the-2026-maryland-governor-republican-primary-election`
- conditionId: `0x3d6221450862c69f69e9b278a9119fc3e11f1c794650f7cddf283d4adefeee20`
- YES: 67% | resolves: 2026-06-23 (28 days) | volume: $96,150 | liquidity: $5,068
- tags: geopolitics

**Q:** Will Chip Keating win the 2026 Oklahoma Governor Republican primary election?
- slug: `will-chip-keating-win-the-2026-oklahoma-governor-republican-primary-election`
- conditionId: `0x6c0b425903eab2fd17e3171fedb3fe557497de75a2da23dd2db21f2624e9b20a`
- YES: 30% | resolves: 2026-06-16 (21 days) | volume: $3,483 | liquidity: $5,028
- tags: geopolitics

**Q:** Will John James win the 2026 Michigan Governor Republican primary election?
- slug: `will-john-james-win-the-2026-michigan-governor-republican-primary-election`
- conditionId: `0xbc63ab257269b6d88696a7c395c22a032dd8bcaec0f20b22083ac17dd8a9221c`
- YES: 35% | resolves: 2026-08-04 (70 days) | volume: $11,923 | liquidity: $4,817
- tags: geopolitics

**Q:** Will Ed Hale win the 2026 Maryland Governor Republican primary election?
- slug: `will-ed-hale-win-the-2026-maryland-governor-republican-primary-election`
- conditionId: `0x16711932e48692c37b0be92837cc09c015063d8cbf124e916f393f143d741af0`
- YES: 28% | resolves: 2026-06-23 (28 days) | volume: $14,682 | liquidity: $4,529
- tags: geopolitics

**Q:** Will Cindy Holscher win the 2026 Kansas Governor Democratic primary election?
- slug: `will-cindy-holscher-win-the-2026-kansas-governor-democratic-primary-election`
- conditionId: `0x8bb083247bc0525ae99c364b72394f3cd8e8d15bd4ed7ce08bd71079bba2bda6`
- YES: 32% | resolves: 2026-08-04 (70 days) | volume: $3,149 | liquidity: $4,385
- tags: geopolitics

**Q:** Will Jerri Green win the 2026 Tennessee Governor Democratic primary election?
- slug: `will-jerri-green-win-the-2026-tennessee-governor-democratic-primary-election`
- conditionId: `0x22776ecdacca07302e6cc578cdcf26df93b4233d5a8166cbf131cb32fec425b9`
- YES: 78% | resolves: 2026-08-06 (72 days) | volume: $34,242 | liquidity: $4,317
- tags: geopolitics

**Q:** Will Victor Marx win the 2026 Colorado Governor Republican primary election?
- slug: `will-victor-marx-win-the-2026-colorado-governor-republican-primary-election`
- conditionId: `0x0b94b4e361a4797c94c4802dec1080f7d60005c04885a8930e931e62b12ea879`
- YES: 75% | resolves: 2026-06-30 (35 days) | volume: $6,693 | liquidity: $3,391
- tags: geopolitics

**Q:** Will Perry Johnson win the 2026 Michigan Governor Republican primary election?
- slug: `will-perry-johnson-win-the-2026-michigan-governor-republican-primary-election`
- conditionId: `0xd4607b688346dfbe7b5fa5e805d16e5b7878d60bf2e1d4c7c0192665ffeafdf9`
- YES: 43% | resolves: 2026-08-04 (70 days) | volume: $12,006 | liquidity: $3,256
- tags: geopolitics

**Q:** Will Therese Terlaje win the 2026 Guam Governor Democratic primary election?
- slug: `will-therese-terlaje-win-the-2026-guam-governor-democratic-primary-election`
- conditionId: `0xa34f2fb5664f2cc079ba616597ab300bbbe6dd91e3d597f5bc45693c6ea20082`
- YES: 76% | resolves: 2026-08-01 (67 days) | volume: $5,577 | liquidity: $3,236
- tags: geopolitics

**Q:** Will Lisa Demuth win the 2026 Minnesota Governor Republican primary election?
- slug: `will-lisa-demuth-win-the-2026-minnesota-governor-republican-primary-election`
- conditionId: `0xd25c820d3aee1c735c0fa62c36f4905632ab8c6988653b5b4134593b3209eb7f`
- YES: 61% | resolves: 2026-08-11 (77 days) | volume: $58,130 | liquidity: $3,027
- tags: geopolitics

**Q:** Will Josh Tenorio win the 2026 Guam Governor Democratic primary election?
- slug: `will-josh-tenorio-win-the-2026-guam-governor-democratic-primary-election`
- conditionId: `0x8d240de0d0ab5a55bc688eb09ca7066a023fc0942a08d6cb2607971eb87d936f`
- YES: 16% | resolves: 2026-08-01 (67 days) | volume: $9,202 | liquidity: $3,017
- tags: geopolitics

**Q:** Will Jonathan Kreiss-Tomkins advance from the 2026 Alaska Governor primary election?
- slug: `will-jonathan-kreiss-tomkins-advance-from-the-2026-alaska-governor-primary-election`
- conditionId: `0xdfa9c276f883ae7539684ceaf7289ff3db4b83003afb1b8f561f0a569368ff24`
- YES: 53% | resolves: 2026-08-18 (84 days) | volume: $2,961 | liquidity: $2,905
- tags: geopolitics

**Q:** Will Ethan Corson win the 2026 Kansas Governor Democratic primary election?
- slug: `will-ethan-corson-win-the-2026-kansas-governor-democratic-primary-election`
- conditionId: `0xb83df8ea773e1f6693320c4ee94f28ab3fbe10d270d695b6e0f76d03cabeed4d`
- YES: 65% | resolves: 2026-08-04 (70 days) | volume: $2,883 | liquidity: $2,782
- tags: geopolitics, crypto

**Q:** Will Click Bishop advance from the 2026 Alaska Governor primary election?
- slug: `will-click-bishop-advance-from-the-2026-alaska-governor-primary-election`
- conditionId: `0x3342ecddb31d790a0aa690a12b3ef674d0c5014fcd5c3a50afb828b30f982170`
- YES: 55% | resolves: 2026-08-18 (84 days) | volume: $40,596 | liquidity: $2,720
- tags: geopolitics

**Q:** Will Antony Barran advance to the general election for WA-03?
- slug: `will-antony-barran-advance-to-the-general-election-for-wa-03`
- conditionId: `0x5fae5ba9043197e890c32aef1acf277e3ebbc31b643022bef86006b35b3dec5e`
- YES: 15% | resolves: 2026-08-04 (70 days) | volume: $116 | liquidity: $1,869
- tags: geopolitics

**Q:** Will Dave Bronson advance from the 2026 Alaska Governor primary election?
- slug: `will-dave-bronson-advance-from-the-2026-alaska-governor-primary-election`
- conditionId: `0x7fdfdf3089f2926e189998489f530a1a4b3f90ee8d2d52f81d8774757f8ca762`
- YES: 34% | resolves: 2026-08-18 (84 days) | volume: $2,203 | liquidity: $1,724
- tags: geopolitics

**Q:** Labour leadership election scheduled by June 30?
- slug: `labour-leadership-election-scheduled-by-june-30`
- conditionId: `0x6bc2c22c0200475f44030c497e48617311d87c299d8c65d039897a912ebc05b2`
- YES: 63% | resolves: 2026-06-30 (35 days) | volume: $21,921 | liquidity: $1,637
- tags: geopolitics

**Q:** Will Jermaine Johnson win the 2026 South Carolina Governor Democratic primary election?
- slug: `will-jermaine-johnson-win-the-2026-south-carolina-governor-democratic-primary-election`
- conditionId: `0xf688606e6f30e1c55c595ccb992d095e8c9ffe2153154aeec6609eb002f201ee`
- YES: 68% | resolves: 2026-06-09 (14 days) | volume: $11,013 | liquidity: $1,500
- tags: geopolitics

**Q:** Will Rakhi Israni Singh win the CA-14 special election?
- slug: `will-rakhi-israni-singh-win-the-ca-14-special-election`
- conditionId: `0x67bf91daba125a739f48ef9bc0a6d3420cb2258ba44cb1e93ae18cce6e0b3175`
- YES: 16% | resolves: 2026-08-18 (84 days) | volume: $696 | liquidity: $1,477
- tags: geopolitics

**Q:** Will Bernadette Wilson advance from the 2026 Alaska Governor primary election?
- slug: `will-bernadette-wilson-advance-from-the-2026-alaska-governor-primary-election`
- conditionId: `0x39dc2c86efd159ae5b0fddc70b0b15af308993353eff43b5725bf6a0e473ca83`
- YES: 67% | resolves: 2026-08-18 (84 days) | volume: $14,146 | liquidity: $1,400
- tags: geopolitics

**Q:** Will Treg Taylor advance from the 2026 Alaska Governor primary election?
- slug: `will-treg-taylor-advance-from-the-2026-alaska-governor-primary-election`
- conditionId: `0x77396e9b7a44481197718658079006c7b1eff3e9e763007d6b4755fcbaf7c4df`
- YES: 28% | resolves: 2026-08-18 (84 days) | volume: $56,386 | liquidity: $1,345
- tags: geopolitics

**Q:** Claudio Tapia out as AFA President by July 19, 2026?
- slug: `claudio-tapia-out-as-afa-president-by-july-19-2026`
- conditionId: `0x76151c30f23ef5ee963e2f73fa49d5433b4db34839c39383bee4989cb270b639`
- YES: 34% | resolves: 2026-07-19 (54 days) | volume: $194,824 | liquidity: $616
- tags: geopolitics

**Q:** Will Aly Richards win the 2026 Vermont Governor Democratic primary election?
- slug: `will-aly-richards-win-the-2026-vermont-governor-democratic-primary-election`
- conditionId: `0xf77bd5682beec44a135a9ab814a28e4b69481e84365243bc6a86f1cea39dfd76`
- YES: 72% | resolves: 2026-08-11 (77 days) | volume: $52 | liquidity: $379
- tags: geopolitics

**Q:** Will Aisha Wahab win the CA-14 special election?
- slug: `will-aisha-wahab-win-the-ca-14-special-election`
- conditionId: `0x54c2b2d889a1f1d86e2ebe557a6b3da3e35c77c476c96d1a90498632f00db20e`
- YES: 72% | resolves: 2026-08-18 (84 days) | volume: $495 | liquidity: $44
- tags: geopolitics


### AI-TECH (21)

**Q:** Will GPT-6 be released before GTA VI?
- slug: `will-gpt-6-be-released`
- conditionId: `0x0ea8005efbc460378340a2f28a6d97b0d1d9d9d7fba4d16f529b8a415dca77a2`
- YES: 65% | resolves: 2026-07-31 (66 days) | volume: $628,779 | liquidity: $39,715
- tags: ai-tech

**Q:** Will Anthropic have the best AI model at the end of June 2026?
- slug: `will-anthropic-have-the-best-ai-model-at-the-end-of-june-2026`
- conditionId: `0xa4d72632ac0ddadcac5247ffc586a193f1bc3bc839cf9ce993c2471e0d599cca`
- YES: 77% | resolves: 2026-06-30 (35 days) | volume: $1,074,451 | liquidity: $27,643
- tags: ai-tech

**Q:** Will Google have the best AI model at the end of June 2026?
- slug: `will-google-have-the-best-ai-model-at-the-end-of-june-2026`
- conditionId: `0x0bd1b836a2494f80aaee62927cf01e5f6fceb19114e96fc517c6440aea4576e4`
- YES: 17% | resolves: 2026-06-30 (35 days) | volume: $688,273 | liquidity: $23,743
- tags: ai-tech

**Q:** Will OpenAI’s market cap be $1.5T or greater at market close on IPO day?
- slug: `will-openais-market-cap-be-greater-than-1pt5t-at-market-close-on-ipo-day`
- conditionId: `0x4a8005d19b41af72c1cd5c619640d9d51da548dd7c3544b12ae0c520d9e6805b`
- YES: 26% | resolves: 2026-06-30 (35 days) | volume: $108,713 | liquidity: $8,539
- tags: ai-tech

**Q:** Will OpenAI not IPO by December 31, 2026?
- slug: `will-openai-not-ipo-by-december-31-2026`
- conditionId: `0x3849e1d62e0807801913d3e2427e8caf3cc6dd1c8ef42d8d5c08c6f9c449dc5e`
- YES: 25% | resolves: 2026-06-30 (35 days) | volume: $321,680 | liquidity: $8,437
- tags: ai-tech

**Q:** Will Google have the top AI model at the end of June 2026?
- slug: `will-google-have-the-top-ai-model-at-the-end-of-june-2026`
- conditionId: `0xa3681c6be3faf6b4f05918ed0bc9786e41e600d9882c335907b5a3402bf93494`
- YES: 18% | resolves: 2026-06-30 (35 days) | volume: $22,416 | liquidity: $3,737
- tags: ai-tech

**Q:** Will Anthropic have the top AI model at the end of June 2026?
- slug: `will-anthropic-have-the-top-ai-model-at-the-end-of-june-2026-475`
- conditionId: `0x0811ed7f71c2466d04f9ba801c0e21c9cfb016385cdff97b5c9984df0fa5801e`
- YES: 75% | resolves: 2026-06-30 (35 days) | volume: $35,358 | liquidity: $3,606
- tags: ai-tech

**Q:** Will Anthropic have the third best AI model at the end of June 2026?
- slug: `will-anthropic-have-the-third-best-ai-model-at-the-end-of-june-2026`
- conditionId: `0x3c6ece0cadb3d3d87bd47ac065722bf75521e904274870da03e164d719ea2c14`
- YES: 66% | resolves: 2026-06-30 (35 days) | volume: $3,076 | liquidity: $3,092
- tags: ai-tech

**Q:** Will an Anthropic Claude model score at least 45% on Humanity’s Last Exam?
- slug: `will-an-anthropic-claude-model-score-at-least-45-on-humanitys-last-exam`
- conditionId: `0x4a3ae5bc03b849fa2aae19b687428cc9cbf27ce27a966bacdc879fa067a62a2d`
- YES: 19% | resolves: 2026-06-30 (35 days) | volume: $135,381 | liquidity: $2,882
- tags: ai-tech

**Q:** Will Tesla deliver between 375000 and 400000 vehicles in Q2 2026
- slug: `will-tesla-deliver-between-375000-and-400000-vehicles-in-q2-2026`
- conditionId: `0x13150beedcc4b60c60580eec5f87bbb3092995cd893aadb709425e097af82df4`
- YES: 19% | resolves: 2026-06-30 (35 days) | volume: $5,125 | liquidity: $2,842
- tags: ai-tech

**Q:** Will Google have the third best AI model at the end of June 2026?
- slug: `will-google-have-the-third-best-ai-model-at-the-end-of-june-2026`
- conditionId: `0x9a410fefe79447cf2bc106107a7c1d95e09ce3951fb004d0c95fecfea8899203`
- YES: 28% | resolves: 2026-06-30 (35 days) | volume: $1,064 | liquidity: $2,591
- tags: ai-tech

**Q:** Will Anthropic have the #3 AI model at the end of June 2026 (Style Control On)?
- slug: `will-anthropic-have-the-3-ai-model-at-the-end-of-june-2026-style-control-on`
- conditionId: `0xd3b572f14a93e1d3eb1fb9424c684bbf602539fb02111c971c2936aaf69812ea`
- YES: 72% | resolves: 2026-06-30 (35 days) | volume: $570 | liquidity: $2,256
- tags: ai-tech

**Q:** Will Tesla deliver between 400000 and 425000 vehicles in Q2 2026
- slug: `will-tesla-deliver-between-400000-and-425000-vehicles-in-q2-2026`
- conditionId: `0xb98ca5f27a851fd490082e9d3f3058e9a8cf0266ec207854395693015acbd293`
- YES: 25% | resolves: 2026-06-30 (35 days) | volume: $8,801 | liquidity: $1,822
- tags: ai-tech

**Q:** Will Tesla deliver between 425000 and 450000 vehicles in Q2 2026
- slug: `will-tesla-deliver-between-425000-and-450000-vehicles-in-q2-2026`
- conditionId: `0x3be2b05f91f41cea6c5bd803b4c456ca5339a38a8c2bb19f71d38ef44636b0da`
- YES: 19% | resolves: 2026-06-30 (35 days) | volume: $4,813 | liquidity: $1,566
- tags: ai-tech

**Q:** Will GPT-6 be released by September 30, 2026?
- slug: `will-gpt-6-be-released-by-september-30-2026`
- conditionId: `0xf82f84686ee2a25f5690430461413c4dc5a39dcea922a7c5f47d9d29418fbdb6`
- YES: 54% | resolves: 2026-06-30 (35 days) | volume: $6,132 | liquidity: $1,241
- tags: ai-tech

**Q:** Will Google have the #2 AI model at the end of June 2026 (Style Control On)?
- slug: `will-google-have-the-2-ai-model-at-the-end-of-june-2026-style-control-on`
- conditionId: `0x47f87fd6632b1066497c7e63137b8b1222fa75b8cdbc3f352fd48e8b611a7b1e`
- YES: 19% | resolves: 2026-06-30 (35 days) | volume: $165 | liquidity: $1,194
- tags: ai-tech

**Q:** Will OpenAI GPT score at least 50% on Humanity’s Last Exam?
- slug: `will-openai-gpt-score-at-least-50-on-humanitys-last-exam`
- conditionId: `0xc3bb9eb2c758cd71f7a59199c27bf3f20c9e1d929687c72b20c8d06076c45c78`
- YES: 57% | resolves: 2026-06-30 (35 days) | volume: $23,655 | liquidity: $1,039
- tags: ai-tech

**Q:** Will Anthropic have the #2 AI model at the end of June 2026 (Style Control On)?
- slug: `will-anthropic-have-the-2-ai-model-at-the-end-of-june-2026-style-control-on`
- conditionId: `0x2fa398b0da1dddf91587ca5b78410460c1d418126226bcd45a02d35d0958f6e4`
- YES: 75% | resolves: 2026-06-30 (35 days) | volume: $309 | liquidity: $1,027
- tags: ai-tech

**Q:** Will Apple release Homepod Mini Successor by June 30?
- slug: `will-apple-release-homepod-mini-successor-by-june-30`
- conditionId: `0xe6e841c41ed65247c83f0806e53a9872529ff19976c3dacb9420a660b686ac15`
- YES: 22% | resolves: 2026-06-30 (35 days) | volume: $2,078 | liquidity: $1,012
- tags: ai-tech

**Q:** Meta "Mango" model released by June 30?
- slug: `meta-mango-model-released-by-june-30`
- conditionId: `0xe2b3aca20d136af79f908b7c9cba9832b338e2c02083aa114444f273621b17b4`
- YES: 50% | resolves: 2026-06-30 (35 days) | volume: $6,432 | liquidity: $874
- tags: ai-tech

**Q:** Will Sam Altman get OpenAI equity by June 30?
- slug: `will-sam-altman-get-openai-equity-by-june-30`
- conditionId: `0xbb3097da94d7eaf185196f9b384c8e37499248ada1fcd0465b30531cca30d269`
- YES: 38% | resolves: 2026-06-30 (35 days) | volume: $4,916 | liquidity: $352
- tags: ai-tech


### CRYPTO (5)

**Q:** Will bitcoin hit $1m before GTA VI?
- slug: `will-bitcoin-hit-1m-before-gta-vi-872-424`
- conditionId: `0xbb57ccf5853a85487bc3d83d04d669310d28c6c810758953b9d9b91d1aee89d2`
- YES: 49% | resolves: 2026-07-31 (66 days) | volume: $4,420,580 | liquidity: $144,167
- tags: crypto

**Q:** MicroStrategy sells any Bitcoin by June 30, 2026?
- slug: `microstrategy-sells-any-bitcoin-by-june-30-2026`
- conditionId: `0x8e7a03cb1970e2ad6533b01892403516b6b3f5b5fa90ed7d104c28b27e40ba00`
- YES: 32% | resolves: 2026-07-01 (36 days) | volume: $4,006,034 | liquidity: $64,185
- tags: crypto

**Q:** Will MegaETH perform an airdrop by June 30? 
- slug: `will-megaeth-perform-an-airdrop-by-june-30-143-229-513-574-212-254`
- conditionId: `0xe459d1b598da754c9fd5fc155b6efe3a144aa80abbc7d041fce7d35d903d3c8e`
- YES: 17% | resolves: 2026-07-01 (36 days) | volume: $1,546,689 | liquidity: $4,147
- tags: crypto

**Q:** Will Beth Davidson be the Democratic nominee for NY-17?
- slug: `will-beth-davidson-be-the-democratic-nominee-for-ny-17`
- conditionId: `0xd81e304a53cfdac107189a8ab1fe862416c4f6de3a009b3243d057eb89fa8491`
- YES: 38% | resolves: 2026-06-23 (28 days) | volume: $23,799 | liquidity: $2,473
- tags: crypto

**Q:** Will a new country buy Bitcoin by June 30, 2026?
- slug: `will-a-new-country-buy-bitcoin-by-june-30-2026-493`
- conditionId: `0xabbcf4b109800ea512cbe08aa5efe734131855da2847fcb497d763778de4f654`
- YES: 25% | resolves: 2026-06-30 (35 days) | volume: $371 | liquidity: $65
- tags: crypto


### OTHER (CURATED) (13)

**Q:** Strait of Hormuz traffic returns to normal by end of June?
- slug: `strait-of-hormuz-traffic-returns-to-normal-by-end-of-june`
- conditionId: `0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187`
- YES: 38% | resolves: 2026-06-30 (35 days) | volume: $9,980,858 | liquidity: $194,129
- tags: other

**Q:** Starmer out by June 30, 2026?
- slug: `starmer-out-by-june-30-2026-862-594-548-219`
- conditionId: `0xbee2cd40473495f713c69b9dfbce9fc2837fa4011568222c83c83bb773e35053`
- YES: 23% | resolves: 2026-06-30 (35 days) | volume: $4,740,867 | liquidity: $97,972
- tags: other

**Q:** Will Crude Oil (CL) hit (HIGH) $120 by end of June?
- slug: `will-crude-oil-cl-hit-high-120-by-end-of-june`
- conditionId: `0xba8af64c1b08f322ca7f66f3cfdbdfd50c0eae6fc88d2fcf29c30ceb62682421`
- YES: 20% | resolves: 2026-06-30 (35 days) | volume: $718,229 | liquidity: $29,068
- tags: other

**Q:** Miguel Díaz-Canel out as leader of Cuba by June 30?
- slug: `miguel-daz-canel-out-as-leader-of-cuba-by-june-30-935-772`
- conditionId: `0x119db6dda44f109bcdc2ec5e1d9cb8c21fa1a7e66489f59b1190fdfb25c0d515`
- YES: 18% | resolves: 2026-06-30 (35 days) | volume: $837,696 | liquidity: $28,572
- tags: other

**Q:** Will Crude Oil (CL) hit (LOW) $70 by end of June?
- slug: `will-crude-oil-cl-hit-low-70-by-end-of-june-776-556-989-392-677-842-888-775-665`
- conditionId: `0xe3f8272f4957b7dcc492d988e5c7cd6dbb2f4111cd309571514a280938d617f1`
- YES: 15% | resolves: 2026-06-30 (35 days) | volume: $478,408 | liquidity: $27,927
- tags: other

**Q:** Kash Patel out by June 30?
- slug: `kash-patel-out-by-june-30-165-798`
- conditionId: `0x79859c9e6645873e1568344b0b8ee54cc9eb02b90701cc5ba19c9a547ff313ce`
- YES: 18% | resolves: 2026-06-30 (35 days) | volume: $394,495 | liquidity: $23,531
- tags: other

**Q:** Will Crude Oil (CL) hit (LOW) $80 by end of June?
- slug: `will-crude-oil-cl-hit-low-80-by-end-of-june-412`
- conditionId: `0xbaf252e7ac957d6636a6916da51892c9f42e59bfbf808bd4d8e16f194694d2b5`
- YES: 46% | resolves: 2026-06-30 (35 days) | volume: $382,942 | liquidity: $22,366
- tags: other

**Q:** Will Crude Oil (CL) hit (HIGH) $115 by end of June?
- slug: `will-crude-oil-cl-hit-high-115-by-end-of-june-217-913-468-473`
- conditionId: `0x46f19d5bedd6d601d597d308d86814245974014d8a108395a7690d7a099cacdd`
- YES: 29% | resolves: 2026-06-30 (35 days) | volume: $752,451 | liquidity: $20,441
- tags: other

**Q:** Naim Qassem out as Hezbollah’s secretary-general by June 30, 2026?
- slug: `naim-qassem-out-as-hezbollahs-secretary-general-by-june-30-2026`
- conditionId: `0xb14c073b5ff01c3f9a42b15c867475ae38612ecbe3a8945375ba56969c270247`
- YES: 21% | resolves: 2026-06-30 (35 days) | volume: $147,862 | liquidity: $18,869
- tags: other

**Q:** Will Silver (SI) hit (LOW) $65 by end of June?
- slug: `will-silver-si-hit-low-65-by-end-of-june-998-897`
- conditionId: `0xa43ad4037543d8376fe6bc828997820cc197ceb86d8c8f51b33b95c6676078cf`
- YES: 18% | resolves: 2026-06-30 (35 days) | volume: $206,156 | liquidity: $12,707
- tags: other

**Q:** Will Gold (GC) hit (LOW) $4,200 by end of June?
- slug: `gc-hit-4200-low-jun-2026-737-562-112-239-328-831-356-185-544-513-223-988`
- conditionId: `0x8cf61b7b84b6ac2e0c619867dd6966e688b43e4fd4c866423da2f757c58f0a9f`
- YES: 18% | resolves: 2026-06-30 (35 days) | volume: $315,295 | liquidity: $12,059
- tags: other

**Q:** US x Cuba economic deal by June 30, 2026?
- slug: `us-x-cuba-economic-deal-by-june-30-2026`
- conditionId: `0xe34380896d3df2ac2fcd753a01b3a8887acc335778c11e93af952fd273fca7fb`
- YES: 21% | resolves: 2026-06-30 (35 days) | volume: $141,568 | liquidity: $11,053
- tags: other

**Q:** Will María Corina Machado enter Venezuela by June 30?
- slug: `will-mara-corina-machado-enter-venezuela-by-june-30`
- conditionId: `0x8d6e53e9c96faed715f6fe20d7d1944f31bf203f980d8f3d94304c0a302381fc`
- YES: 23% | resolves: 2026-06-30 (35 days) | volume: $228,269 | liquidity: $9,115
- tags: other



---
## Section 6: The April 15 first-flight — what the system has actually done (F-tags, verbatim from Round 2)

Preserved verbatim from Round 2 for context. This is the project's strongest verified internal evidence about what the latent communication system can do.

**Context.** This experiment ran on Mac Mini M4 Pro on April 15, 2026. It was the third successive self-correction in the activation-steering work — the prior contrastive-injection result was retracted within hours of being claimed (the team identified it as complement arithmetic, not belief update). The semantic invariance test below was specifically designed to remove that confound.

**F-1.** Verbatim from `BRAIN.md` lines 2280-2326:

> Results: experiments/week4/activation_steering/semantic_test_2026-04-15_2009.json
>
> Test design (semantic invariance — no crowd anchor, forced reasoning):
> Agent B prompt: Will Bitcoin hit 80k or 60k first? Begin with exactly:
> "After considering all factors, my probability that Bitcoin reaches 80k
> first is X%." Then 2-3 sentences of actual reasoning. No complement math.
>
> RESULTS at layers [16,20,24]:
> Control (no injection): 35%
> Reasoning: hedged, balanced, moderate
>
> Bullish vector (h_bull - h_bear) injected at scale 0.4:
> Result: 75% — 40 point upward shift
> Reasoning: institutional investments, positive sentiment, strong upward
> trajectory — genuine bullish arguments, no hedging
>
> THIS IS TRUE LATENT STEERING:
> 1. 40 point probability shift (35% to 75%)
> 2. Reasoning changed to match injected stance
> 3. Stance-specific bullish arguments in output
> 4. No complement arithmetic — both report P(80k first)

**F-2.** In plain terms: the system can take a mathematical vector representing "bullish" and inject it into another agent's hidden state mid-generation. The result: the other agent's probability estimate moves substantially AND its reasoning changes to match. Both directions report the same target probability, so it is not arithmetic flipping. The agent is producing stance-specific reasoning that was not in its prompt.

**F-3.** Bearish injection at the same configuration breaks coherence. The bullish pole works; the bearish pole does not. Symmetric bidirectional control is not yet proven.

**F-4.** Contamination status: this result is Tier 2 valid (reproducible internally). It survived the April 18 contamination audit because the test was on Mac Mini physics and did not depend on Polymarket baselines.

**F-5.** Relevance to Round 3 market selection: the experiment used a Bitcoin price question as a *vehicle* for testing whether activation steering works. The question's specific subject was incidental. For the four-arm benchmark on the Mode 1 registry, the selected markets will play a similar role — they are *vehicles* for measuring latent vs text agent behavior under adversarial real-money conditions. The markets themselves do not need to be "AI-relevant" to test the latent thesis; they need to be resolvable, well-calibrated against crowd uncertainty, and exposed to enough adversarial pressure that any latent edge is real and not artifact.

---

## Section 7: Questions to answer

Answer all four questions. Length guidance: 2-4 paragraphs per question, plus the per-market rationales in Q1. Cite line tags where relevant (T-N, P-N, L-N, M-N, F-N).

---

**Q1. Which 8 markets do you pick?**

Select 8 specific markets from the qualifying pool in Section 5. For each market, give:

- The slug (so the Founder can verify the exact market)
- A one-sentence rationale for the pick

Your 8 markets must satisfy L-3 criterion 5 ("domain mix favoring macro/policy/geopolitics/AI-tech over noise categories"). Practical interpretation: at least one market from each of macro, policy, geopolitics, and AI-tech, with the remaining four distributed however you judge best. If the pool's structural shape (per Section 4 M-5) makes balanced distribution impossible, explicitly name the trade-off you accepted and why.

Format your answer as a numbered list of 8 picks, each with slug + one-sentence rationale. Then a brief paragraph (2-3 sentences) explaining the overall shape of your selection — what you optimized for, what you de-prioritized.

---

**Q2. What liquidity floor do you recommend?**

The Step 7 synthesis (L-4) explicitly deferred the liquidity floor decision to Round 3, "to be decided when looking at actual candidate markets." Round 3 is now looking at actual candidate markets.

Recommend a specific dollar amount for the liquidity floor. Show your reasoning by referencing the pool's liquidity distribution from M-8 in Section 4. A floor at $20K keeps ~20 markets. A floor at $10K keeps ~50. A floor at $5K keeps ~85. Lower floors enable broader domain coverage; higher floors enable real-money paper-trading without slippage.

State your recommendation in this form: "Liquidity floor: $X. Reasoning: ..."

---

**Q3. Which of your 8 markets are weakest tests of the latent thesis (A-1 weak language priors)?**

The Round 2 A-1 argument (ChatGPT, preserved as L-4 future-audit watch item) was that prediction markets are heavily linguistically-mediated by construction — possibly the worst surface for proving the latent thesis. Section 4 M-7 made this concrete with examples.

Of your 8 selected markets, identify the 1-3 markets most exposed to weak language priors. For each, briefly explain why (e.g., "subjective consensus required for resolution," "narrative-dominated price discovery," "event definition contestable"). Then briefly describe how you would mitigate this exposure during the four-arm benchmark — e.g., flag these markets for separate-track reporting, weight them less in aggregate scoring, or accept the exposure as the cost of domain mix.

---

**Q4. Honest assessment of your 8-market selection's failure mode.**

Every selection has a structural risk. Name yours. Examples:

- "My selection over-indexes on the June 30 AI-tech cluster, creating longitudinal-comparison fragility when all those markets resolve the same day."
- "My selection accepts thin liquidity in 2 of 8 picks (sub-$5K), which may produce noisy four-arm benchmark signal."
- "My selection's macro bucket is dominated by short-horizon Fed markets (22-day resolution), giving Mode 1 v1 only 1-2 cycles on macro before requiring re-registration."
- "My selection's geopolitics picks are all electoral predictions, which may not generalize if the latent edge is domain-specific."

Be specific. The Founder needs to see the failure mode you accepted in order to evaluate the trade-off you made.

---

## Anti-bias self-check (answer in your response)

Same format as Round 2.

1. **What in the briefing's framing biases toward your answer?** Be specific. Section 4's "weak language priors" examples lean toward numerical markets; Section 4 M-6's flagging of the Israel-Iran market for special attention might bias selection. Name what biased you.

2. **What did the briefing not include that would have made your answer more rigorous?** Examples: pool history (which markets in the pool were also active 30 days ago, suggesting longevity), API resolution-source reliability metrics, the actual condition-ID-level price update frequency. Name what was missing.

3. **Is there a 5th question that should have been asked but was not?** The four questions cover selection, liquidity floor, weakness identification, and failure mode. Is there a structural question about Mode 1 that Round 3 should have asked but did not?

---

## Section 8: Response format guidance

- Lead with a one-line position summary: "Picked 8 markets across [domains]. Liquidity floor: $X. Failure mode: [one phrase]."
- Then the four numbered answers, in order, with Q1 as the longest (8 picks + overall rationale).
- Then the three anti-bias self-check items.
- Cite line tags (T-N, P-N, L-N, M-N, F-N) where relevant. The Founder will read three responses cold and synthesize; tags make cross-comparison clean.
- Brevity preferred over comprehensiveness. The Founder is reading three responses and producing a synthesis decision; long responses get diminishing returns past about 1500 words.
- Do not consult other engines' answers. This is a cold review.

---

*End of briefing. Engines: please answer cold. The Founder synthesis follows after all three responses are captured verbatim.*
