# Round 3 Founder synthesis — Mode 1 specific market selection

**Date:** May 26, 2026 morning
**Maintainer:** John McGuire (Founder Engine), with Claude (Systems Engine)
**Status:** Round 3 LOCKED. 8 markets selected. Liquidity floor locked at $10K with named soft exceptions. Founder synthesis closed.
**Cross-references:**
- `founder_inputs/2026-05-25_afternoon_step7_founder_synthesis.md` (Step 7 — six locked decisions, the parent record)
- `founder_inputs/2026-05-26_round3_market_selection_briefing.md` (Round 3 briefing, committed `c87e890`)
- `founder_inputs/2026-05-26_round3_market_selection_responses.md` (Round 3 engine responses verbatim, committed `8a09444`)
- `scratch/qualifying_pool_2026-05-26.json` (the 298-market source pool)
- `founder_inputs/2026-05-26_session_handoff.md` (May 26 morning session handoff — contains the polymarket-pull structural finding)

---

## What this document is

The canonical record of the Founder's synthesis on Round 3 — the selection of 8 specific Polymarket markets that constitute the Mode 1 v1 registry. This document closes the Round 3 selection loop opened by the Round 2 surface lock on May 25.

Engine inputs (Round 3 responses) are preserved verbatim in `2026-05-26_round3_market_selection_responses.md`. This document captures *what was selected*, *what trade-offs were accepted*, and *why*. It does not re-litigate the engine arguments.

---

## The 8 locked markets (Mode 1 v1 registry)

| # | Slug | Domain | Liquidity | Days | YES | Engine support |
|---|---|---|---|---|---|---|
| 1 | `will-china-gdp-growth-in-q2-2026-be-between-4pt6-and-4pt9` | macro | $4,094 | 51 | 50% | All 3 |
| 2 | `scotus-bars-counting-mail-ballots-after-election-day` | policy | $5,349 | 67 | 72% | All 3 |
| 3 | `israel-x-iran-permanent-peace-deal-by-june-30-2026-262` | geopolitics | $102,133 | 35 | 15% | All 3 |
| 4 | `will-anthropic-have-the-best-ai-model-at-the-end-of-june-2026` | ai-tech | $27,643 | 35 | 77% | All 3 |
| 5 | `iran-agrees-to-surrender-enriched-uranium-stockpile-by-june-30-2026` | geopolitics | $63,806 | 35 | 19% | ChatGPT + Grok |
| 6 | `will-crude-oil-cl-hit-high-120-by-end-of-june` | macro/commodity | $29,068 | 35 | 20% | ChatGPT + Grok |
| 7 | `will-gpt-6-be-released` | ai-tech | $39,715 | 66 | 65% | ChatGPT solo |
| 8 | `fed-rate-cut-by-december-2026-meeting` | macro | $15,733 | 22 | 32% | Gemini solo |

**Condition IDs (for verification and registry construction):**

1. `0x800be7611c7efcdf5827c049e0baac8b6047b506af412e283dbac9ce7e202560` (China GDP)
2. `0xd73237bb27cdc455578e9a0788c358bd79609d394f43a270bde10cde4788105f` (SCOTUS mail ballots)
3. `0x5efa976ebe94080bbda7e45605333ff8f30156cc91604d66c41eb52fd3e25f3e` (Israel-Iran peace)
4. Anthropic best AI — to be retrieved from `qualifying_pool_2026-05-26.json` during registry construction
5-8. To be retrieved from `qualifying_pool_2026-05-26.json` during registry construction (full ID lookup is a tomorrow task, not a synthesis task)

**Domain mix:** 3 macro/commodity (China GDP, Crude Oil, Fed Dec) + 1 policy (SCOTUS) + 2 geopolitics (Israel-Iran, Iran uranium) + 2 ai-tech (Anthropic, GPT-6). Satisfies L-3 criterion 5 ("domain mix favoring macro/policy/geopolitics/AI-tech").

---

## The locked liquidity floor

**$10K with named soft exceptions.**

All three engines independently converged on $10K. The Founder lock accepts this convergence.

**Named soft exceptions (sub-floor markets accepted because they are unique domain anchors):**

- `will-china-gdp-growth-in-q2-2026-be-between-4pt6-and-4pt9` ($4,094 — sole numerical-band macro market with 50% uncertainty and 51-day horizon)
- `scotus-bars-counting-mail-ballots-after-election-day` ($5,349 — sole policy market with three-engine convergence and 67-day horizon)

The soft-exception structure was proposed by ChatGPT in Round 3: "a sub-$10K market may enter only if it is uniquely valuable for domain diversity and has unusually strong resolution clarity." Founder accepts this framing — the alternative was either dropping the only macro and policy three-engine-converged markets, or lowering the floor universally (which would have admitted noisier markets).

**Registry implementation note:** The benchmark_registry_v1.json file should record both the floor ($10K) and the explicit exceptions, so that future audits can see the structure was deliberate, not accidental.

---

## Why this synthesis was clean

Unlike May 25's Decision 2 (Polymarket primary, Founder override against triple-engine convergence on hybrid), Round 3 did not require a Founder override against engine consensus. The synthesis was clean because:

1. **Four markets had three-engine convergence.** No override needed; the engines agreed and the data backed them up.

2. **Two markets had two-engine convergence.** Both passed slug verification against the pool. Founder accepted as second-tier convergence.

3. **The two solo-engine picks (GPT-6 from ChatGPT, Fed Dec from Gemini) were Founder-selected after considering all single-engine options.** GPT-6 was chosen as the second AI-tech market because it has higher liquidity than Anthropic and is less narrative-mediated (event-based vs. consensus-ranked). Fed Dec was chosen over Strait of Hormuz to mitigate the June 30 geopolitics cluster — the failure mode all three engines independently named as their top concern.

4. **The liquidity floor was unanimous across engines.** Founder accepted the engines' floor recommendation rather than overriding.

---

## Trade-offs accepted

These are the structural risks the Founder selection accepts, named explicitly so future audits can see what was traded off:

1. **June 30 cluster: 5 of 8 markets resolve on June 30, 2026.** The remaining 3 resolve on June 17 (Fed Dec), July 16 (China GDP), and August 1 (SCOTUS). The cluster is the failure mode all three engines named as most likely. Mitigation: the 3 non-cluster markets preserve longitudinal-comparison capability across June-July-August.

2. **Macro thinness.** Three macro-ish picks (China GDP, Crude Oil, Fed Dec), but China GDP is sub-floor and Fed Dec is short-horizon (22 days, 1-2 cycles before resolution). If the latent edge is strongest in macro forecasting, Mode 1 v1 may underweight that signal. Accepted because the pool itself is thin in macro; v2 may revisit if surface composition shifts.

3. **AI-tech weak-language-priors exposure.** The Anthropic best-model market is universally flagged by the engines as the weakest test of the latent thesis. GPT-6 is partially exposed (release event interpretation can be contested). Two of the 8 markets carry significant weak-language-prior exposure. Accepted as deliberate stress tests — if the latent thesis is real, it should hold under these conditions; if it fails, the failure should be analyzed against the A-1 future-audit watch item, not treated as thesis failure.

4. **Sub-floor exceptions named.** Two markets sit below the $10K liquidity floor. Soft-exception structure preserves the convergence-supported domain anchors at the cost of two markets with limited paper-trading depth. Mitigation: paper-trade these markets at minimum stake; weight calibration scoring separately if depth-related noise becomes apparent.

---

## What this synthesis does NOT do

- It does not lock the condition IDs. Condition IDs 4-8 need to be retrieved from `qualifying_pool_2026-05-26.json` during the next session's registry construction. This is a mechanical lookup, not a synthesis decision.

- It does not build the `benchmark_registry_v1.json` file. That is the next work block.

- It does not write the loader logic with hard-fail visibility. That is also the next work block.

- It does not address the polymarket-pull structural finding from this morning. That is a separate work block per Pattern D (per the May 26 morning session handoff).

- It does not update `state_manifest.md`. polymarket-pull `VALID: yes` designation is now questionable and probably belongs at `VALID: limited`; this is a separate work block.

---

## What is now closed (not to be re-opened lightly)

The Founder synthesis on Round 3 selected 8 markets from a 298-market qualifying pool, after three engines reviewed cold and produced converging recommendations. The synthesis is allowed under the operating model and respects all six locked Step 7 decisions.

The legitimate triggers for re-opening Round 3:

- If `benchmark_registry_v1.json` construction reveals that any of the 8 condition IDs cannot be retrieved or have changed (Polymarket API state has drifted between this morning's pull and tomorrow's construction).
- If one of the 8 markets resolves before registry construction completes (would invalidate that market's selection).
- If the polymarket-pull structural finding from this morning produces evidence that the qualifying pool itself was biased in ways the engines could not see.
- If, after operating Mode 1 v1 for 30+ days, the four-arm benchmark surfaces evidence that the selected markets are systematically wrong for the latent thesis.

Founder cognitive doubt about the selection itself is **not** a legitimate trigger.

---

## What is now unblocked

With Round 3 closed, the next work surfaces (in dependency order) are:

1. **`benchmark_registry_v1.json` construction.** Write the registry file at `experiments/benchmark/benchmark_registry_v1.json` with the 8 slugs, their condition IDs, expected resolution dates, the $10K liquidity floor with named exceptions, and the v1 metadata.

2. **Loader logic with hard-fail visibility.** Write the script that reads the registry, queries Polymarket for current state per slug, produces explicit `NO_LIVE_MARKET` state when a market is missing (per the May 24 afternoon3 architectural lock). No silent 0.5 fallbacks.

3. **text-swarm rebuild against Mode 1.** Conditional on Mode 1 producing deterministic output per May 24 afternoon3 architectural lock. The three text-swarm restoration prerequisites become re-evaluable once Mode 1 produces stable output.

4. **polymarket-pull remediation.** Separate work block per Pattern D. The launchd job parameterized as "top 200 by volume" needs a structural decision (refactor to category-based pulling, fix the limit, document the VALID: limited designation in state_manifest.md). Not part of Round 3 scope.

5. **incident_ledger.md entry for the polymarket-pull finding.** Also separate work block per Pattern D.

---

## Reproducer summary

| Claim | Reproducer |
|---|---|
| Eight markets locked | This file's "The 8 locked markets" section |
| Slug verification against pool | `scratch/qualifying_pool_2026-05-26.json`, all 8 slugs present (1 slug `will-gpt-6-be-released-before-gta-vi` from Grok was a mangled version of `will-gpt-6-be-released`; the latter is the real slug and is what's locked here) |
| Three-engine convergence on 4 markets | `founder_inputs/2026-05-26_round3_market_selection_responses.md` Q1 sections |
| Two-engine convergence on 2 markets | Same file, Q1 sections (ChatGPT + Grok agreed on Iran uranium and Crude Oil $120) |
| Liquidity floor convergence on $10K | Same file, Q2 sections (all 3 engines) |
| Soft-exception framing | Same file, ChatGPT Q2 section |
| June 30 cluster as top failure mode | Same file, all 3 Q4 sections |
| Founder override authority | `docs/intent.md` "How this project works" section |

---

*End of synthesis. Round 3 closed. `benchmark_registry_v1.json` construction blocked on this synthesis being committed.*
