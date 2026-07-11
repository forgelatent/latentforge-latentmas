# Round 4 loader contract — Founder synthesis

**Date:** June 27, 2026
**Maintainer:** John McGuire (Founder Engine), with Claude (Systems Engine)
**Status:** Loader contract LOCKED. Five decisions (Q1–Q5) synthesized from three cold engine responses (June 7) plus a targeted Q4(b) re-ask (June 27). Implementation is the NEXT work block — NOT started here (Pattern D firewall).

**AMENDED July 11, 2026:** Q4(b) "one bulk call" and Q5.3 "api_response_sha256" (singular) were amended during the loader install — see the Amendment section at the end of this document. The original text below is preserved unedited as the June 27 record.
**Briefing:** `founder_inputs/2026-05-26_loader_contract_briefing_to_engines.md` (committed `a03fdf5`)
**Round 4 responses:** `founder_inputs/2026-06-07_loader_contract_responses.md` (committed `2fc7b2e`)
**June 7 handoff:** `founder_inputs/2026-06-07_end_of_session_handoff.md`
**Registry under contract:** `experiments/benchmark/benchmark_registry_v1.json` (committed `be7aa94`)

---

## What this document is

This is the founder synthesis that closes Round 4 of the May-architectural-arc. It decides the **Mode 1 v1 loader contract** — the rules the loader script must follow. It does NOT decide implementation; the loader is not written here.

The contract was synthesized from three cold engine responses captured June 7, read in a fresh session on June 27 (20-day Pattern D separation), one question at a time with explicit per-decision founder approval. Q4 additionally went through a narrow, single-question re-ask on June 27 after the founder's own reproducer overturned the factual premise the engines' Q4 answers had rested on.

Everything inherited from prior rounds is treated as locked and was not re-opened: afternoon3 architecture, Step 7 six decisions, Round 3 8-market selection + $10K floor, registry v1 schema, Variant A immutability, and the [L-1] no-silent-fallback constitutional principle.

---

## Pre-synthesis state checks (June 27)

- **Liveness re-check.** All 8 registry markets re-verified live this morning: `closed: False`, actively trading. No Round 3 single-market re-open trigger fired. Registry intact.
- **Fed Dec re-open flag (from June 7 handoff) — resolved, did NOT fire.** The June 7 handoff flagged that Fed Dec was scheduled to resolve June 17 and that if it had resolved before synthesis, that was a legitimate Round 3 re-open trigger. Checked at synthesis time: Fed Dec is `closed: False`, `acceptingOrders: True`, ~$1855 volume in the last 24h, normal price split (`["0.185", "0.815"]`) — actively trading despite a stale `endDate` of June 17. The trigger did not fire because the market is genuinely still live. The *reason* it didn't fire became a new finding (see below).
- **New finding — `endDate` is unreliable as a liveness/resolution signal.** Fed Dec's `endDate` (June 17) is in the past while the market is actively trading. `endDate` must NOT be used as a liveness or resolution signal. This joins the known traps: `active: True` on closed markets ([E-3]) and `outcomePrices`-is-a-JSON-string ([E-4]). Three fields now established as "store-but-don't-trust" for liveness: `active`, `outcomePrices` (without parsing), and `endDate`. Folded into Q1 and Q2 below.

---

## The locked contract — summary table

| Q | Decision |
|---|---|
| **Q1 — State granularity** | Schema **β** (Grok): three states — LIVE / RETIRED / ERROR. Liveness test = `closed == False` AND `acceptingOrders == True`. `endDate` excluded from liveness; recorded but not trusted. Cause-of-death (closed vs missing) recorded as a sub-field under RETIRED. |
| **Q2 — Output schema** | Full transform, loader is the single normalization gatekeeper. Parsed prices with hard-fail, `*Num` floats only, two timestamps, selection snapshot retained. No computed mid-price (no robot interpretation). |
| **Q3 — Scheduling** | Hybrid launchd, once/day, **4:50 AM**, one shared output file. Manual trigger retained. Loud failure: don't update production file, exit non-zero, digest alert. |
| **Q4 — HTTP pattern** | urllib + UA. **Bulk `/markets?condition_ids=...`, one call for all 8, no fallback (Schema B).** All-or-nothing is intended; clean labeled gap on failure. 2-attempt retry on the single bulk call. |
| **Q5 — Missing question** | Loader must be self-auditing: identity hard-fail + tiered exit codes (0/1/2) + provenance stamp. |

---

## How the inputs were weighted

The synthesis did not treat the three responses as three equal votes. Per the June 7 capture integrity notes, the weighting was:

- **Gemini** — full cold-format response, honestly self-disclosed that the briefing's E-tags anchored it toward finer granularity (γ) and aggressive parsing. Evidence-handling weighted heavily; granularity *conclusion* discounted for disclosed anchoring.
- **ChatGPT** — did not follow the response format; opened "my answer remains essentially unchanged," suggesting carry-over rather than a cold read. Did not answer Q1, Q3, or Q4. Treated as a **one-idea contributor** (provenance), not a three-question voter. Its silence on a question was NOT counted as agreement.
- **Grok** — full cold-format response, also disclosed E-tag anchoring, but reasoned to a *different* Q1 answer than Gemini (β vs γ). That independent divergence-under-shared-anchor was treated as real signal.

**Convergence asymmetry applied throughout:** convergence was weighted heavily only where it was genuinely independent (Q5), and discounted where the briefing's framing could have manufactured it (Q1 granularity, Q4 slug-preference). This is the "founder catches convergence-as-pattern" discipline from the briefing's Section 3.

---

## Q1 — State granularity

**Decision: Schema β (Grok) — three states: LIVE / RETIRED / ERROR — with cause-of-death recorded as data, and `endDate` excluded from the liveness test.**

**The choice.** Gemini argued γ (four states: LIVE / CLOSED / MISSING / ERROR), on the grounds that closed and missing are different kinds of failure. Grok argued β (three states), collapsing closed+missing into RETIRED because both trigger the *same founder response* — stop and decide whether to iterate to v2. ChatGPT did not pick a letter.

The deciding test was **response-equivalence, not difference-existence.** The question is not "are closed and missing different?" (they are) but "do I respond to them differently?" (I do not — both are Variant A hard-fail triggers demanding a v2 decision). ERROR is genuinely separate because its response is different: retry, don't touch the registry. So the number of *action states* is three, and that is what the exit codes (Q5) key off.

**Why this isn't simply discounting Gemini.** Gemini's instinct that closed-vs-missing is worth knowing is correct — it is just that the distinction belongs in the *audit trail*, not in the action-state label. The contract therefore records the specific cause of a RETIRED verdict (closed vs missing) as a sub-field, preserving Gemini's information without inflating the action-state count. This sided with Grok on the label while keeping Gemini's data.

**`endDate` exclusion (June 27 finding).** Both engines, when defining liveness, leaned partly on `endDate` being in the future. The June 27 Fed Dec finding overturns that: `endDate` can be in the past on an actively trading market. The locked liveness test is therefore **`closed == False` AND `acceptingOrders == True`** only. `endDate` is recorded in the output but never used to judge liveness or resolution — same treatment as `active` ([E-3]).

**Honors [L-1].** Any state that is not cleanly LIVE is surfaced explicitly and loudly. No silent fallback.

---

## Q2 — Output schema for live markets

**Decision: Full transform — the loader is the single normalization gatekeeper. No raw pass-through. No computed interpretation.**

**The principle all three named (and it is correct):** the loader is the single place where Polymarket's ambiguity is converted into deterministic Mode 1 semantics. Cleaning once, centrally, prevents the April 20 class of failure (a trap passed downstream where a consumer silently falls into it). This is [L-1] applied to data shape.

**Per LIVE market the loader writes:**

- **Durable identity:** `slug` + `condition_id`.
- **Parsed prices:** `outcomePrices` decoded from its JSON-string form into real floats, with **hard-fail** if the parse fails, yields `["0","0"]` on an open market, or does not yield **exactly 2** outcomes. (The "exactly 2" check absorbs Gemini's binary-dimension-mutation concern — a binary market mutated to multi-outcome fails here rather than silently miscalculating downstream.)
- **Normalized numerics:** liquidity, volume (24h + total) taken from the `*Num` typed fields only; string twins discarded. ([E-6])
- **Recorded-but-not-trusted:** `endDate` (per Q1), and the RETIRED cause-of-death sub-field (per Q1).
- **Two timestamps:** `loader_run_at` (loader's check time) + API `updatedAt` (Polymarket's last-change time). Keeping both exposes Polymarket-side staleness — old data cannot masquerade as fresh. ([E-7])
- **Selection snapshot:** carried through from the registry so selection-time-vs-live drift is visible downstream.

**No computed mid-price / no "benchmark-ready probability."** Grok proposed a computed mid-price; the contract rejects it. A mid-price is interpretation, and the locked architecture keeps fetch and interpret separate — the loader reports what *is*, never what it *means*. Grok itself flagged this as borderline and "wisely scoped out." Every historical contamination involved a layer doing interpretation it should not; keeping the loader interpretation-free is a structural defense. If a downstream consumer wants a midpoint, that consumer computes it and owns the interpretation.

---

## Q3 — Scheduling and operational shape

**Decision: Hybrid launchd, once per day, 4:50 AM, one shared output file. Manual trigger retained. Loud failure on any non-clean run.**

**Once per day, one file, all consumers read the same snapshot.** Both engines that addressed scheduling converged here, and the convergence is real (it follows from the measurement model, not from briefing framing). Per-consumer querying would let text-swarm and the scoring layer read the market at different moments, breaking the temporal integrity of the benchmark — the scoring layer would evaluate text-swarm against market state text-swarm never saw (Gemini's example). One daily snapshot to one file eliminates that drift.

**Time slot: 4:50 AM.** After polymarket-pull (4:43) and kalshi-pull (4:45), comfortably before text-swarm (~5:15, when restored). Gemini said 4:55, Grok said ~4:50; the difference is immaterial. 4:50 chosen for slightly more headroom before downstream consumers.

**Manual trigger retained** for ad-hoc founder runs (the "hybrid" half).

**Loud failure — directly defends the May 9 kalshi-pull silent-success scar.** On any RETIRED or ERROR state, the loader: writes the error, does NOT update the production state file (so downstream consumers cannot run on corrupted/partial data), and exits non-zero so the morning digest flags it as a blocking alert. Visibility over silent gaps.

---

## Q4 — HTTP pattern choice

**Decision: stdlib urllib + explicit User-Agent. Bulk `/markets?condition_ids=...`, one call for all 8, no per-slug fallback (Schema B). All-or-nothing is intended behavior. 2-attempt retry on the single bulk call.**

This is the only decision that required a re-ask, and the arc is worth preserving as provenance.

**The Round 4 answer and why it was overturned.** On June 7, both engines that addressed Q4 chose the per-slug endpoint, explicitly *because* the bulk `condition_ids` endpoint had returned a 403 and was treated as broken/untested ([E-9]). That premise was false. The 403 was a missing-User-Agent problem, not auth or deprecation. The endpoint works under the proper UA — confirmed June 7 (manual probe) and re-confirmed June 27 with a thorough reproducer: one bulk call returned all 8 markets, every returned `conditionId` matched the registry exactly, and every field the locked Q2 schema needs was present.

**(a) Tool: urllib + UA.** Both engines; dependency hygiene; matches working repo code (`full_pull_and_filter.py`, `shadow_match`); aligns with the April 6 "scripts handle deterministic operations" rule. Unaffected by the endpoint finding.

**(b) Endpoint: bulk condition_ids, no fallback.** After the premise flipped, a narrow single-question re-ask (June 27) put the reproduced evidence cold to all three engines, with the Systems Engine's reversal-toward-bulk explicitly disclosed so anchoring could be consciously checked. Result: **Gemini → B, Grok → B, ChatGPT → C** (bulk-primary + labeled per-slug fallback). All three agreed bulk should be the measurement endpoint; the only split was what happens on a failed call.

The contract takes **B over C** on the strength of [L-1], not vote-count. A per-slug fallback — even a labeled one — reintroduces fallback-shaped behavior and a second, differently-shaped ingestion path into a system whose constitutional rule is *no silent fallback, hard-fail visibility*. The project was nearly destroyed by a fallback (the silent 0.5); the disciplined posture is to not build another. Both cold-read engines (Gemini, Grok) independently reached B and independently rejected C as unnecessary complexity that dilutes the consistency guarantee that justified bulk in the first place.

**All-or-nothing is intended, not a bug.** For a once-daily longitudinal snapshot, a partial day is a broken measurement *either way* — whether 7-of-8 arrive, or all 8 arrive at 8 slightly different moments. The contract treats each run as atomic: a complete time-aligned record, or a clean labeled gap. ChatGPT's legitimate concern (don't go blind on a failed day) is satisfied by the Q3 loud-failure rule (ERROR state, no file update, non-zero exit, digest alert) — the founder *knows* it failed — without a second data path. A clean labeled gap is honest missing-data the benchmark can handle; a fallback is contaminated-shaped data it cannot.

Per-slug is recorded as the known **v2 option** if unattended runs later reveal a bulk-specific failure mode that per-slug does not exhibit.

**(c) Retry: 2 attempts (10s, 30s) on the single bulk call, then ERROR.** Lighter than polymarket-pull's 3×5min because this is one targeted call, not a full-surface pull.

---

## Q5 — The missing question

**Decision: the loader must be self-auditing. Three required mechanisms.**

This is the strongest-grounded decision in the contract: all three engines independently named the same gap in Round 4, before any anchoring, reversal, or re-ask. Identity-verification + exit-code discipline was named by Gemini and Grok explicitly; ChatGPT named provenance. The three combine into one principle — **the loader must verify it is looking at the right market, report what kind of day it had in a machine-readable way, and stamp its output so any number is traceable forever.**

**1. Identity verification** (Gemini + Grok, independent). The returned `conditionId` set must exactly match the registry's 8. Any mismatch or wrong count is a hard-fail (RETIRED / CORRUPTED), not a shrug. Defends the Pattern A silent-reassignment vector, where an active slug silently begins tracking a different market structure. Already promoted to central in Q4 (the loader now fetches *by* condition_id); the June 27 reproducer already runs this exact check and passed.

**2. Tiered exit codes** (Gemini + Grok, independent). The exit code distinguishes the three Q1 states so the morning digest can act without reading logs:
- `0` = all 8 LIVE, validated, fresh.
- `1` = one or more RETIRED → founder v2 decision required.
- `2` = ERROR (network/transient) → safe to retry, registry not invalidated.

Grok's 0/1/2 chosen over Gemini's 0/10/20 — the load-bearing thing is three tiers, not the numbers. Directly defends the May 9 kalshi-pull silent-success scar.

**3. Provenance stamp** (ChatGPT, distinct contribution). Every output file carries `loader_run_id`, `api_response_sha256` (fingerprint of the raw bulk response), `registry_version`, `loader_schema_version`. Makes every downstream number traceable to the exact API payload that produced it — the Reproducer Requirement applied to the loader's own output. This rests on a single engine rather than three, but is included on principle-fit: it is a direct instance of an existing project discipline, and every historical contamination involved a number that could not be traced back to its source.

**Deliberately not separate requirements:**
- **Binary-dimension validation** (Gemini's "len == 2"): folded into the Q2 price hard-fail rather than duplicated here.
- **Idempotency** (Grok): handled by Q3's once-daily-snapshot design. Bit-identical same-day reruns are not what a live-market loader should want — two runs minutes apart will legitimately differ because the market moved. Not a separate requirement.

---

## Discipline notes (for the record)

- **Pattern D firewall held end-to-end.** Responses collected June 7; synthesis decided June 27 (20-day separation). Implementation is explicitly NOT started in this session — it is the next, separately-handed-off work block.
- **The Q4 reversal arc is a clean provenance example.** Round 4 said slug. The founder's own reproducer overturned the factual premise (`condition_ids` works under proper UA). A narrow, single-question re-ask confirmed bulk. The founder caught what the engines could not (because the engines were working from a stale fact), and the decision updated on reproduced evidence rather than on assertion. This is the three-engine system operating as designed: the founder supplies the fact the engines lack, and the disciplined path is chosen on principle ([L-1]), not on convergence.
- **Convergence was stress-tested, not assumed.** Where three engines agreed (Q5, and the re-asked Q4), the synthesis checked whether the agreement was independent (different reasoning roads to the same place) before trusting it. It was. Where agreement could have been framing-manufactured (Q1 granularity), it was discounted and the decision rested on first-principles response-equivalence instead.
- **Single-engine contributions were kept where they fit existing discipline** (ChatGPT's provenance) and discounted where they did not carry independent weight (ChatGPT's silence on Q1/Q3/Q4 was not counted as a vote).

---

## What happens next (NOT this session)

1. **Move this file into the repo and commit.** Suggested:
   ```
   git -C ~/Projects/latentforge-latentmas add founder_inputs/2026-06-27_loader_contract_founder_synthesis.md
   git -C ~/Projects/latentforge-latentmas commit -m "docs(founder_inputs): Round 4 loader contract LOCKED — Q1-Q5 synthesis; bulk condition_ids, three-state, self-auditing"
   git -C ~/Projects/latentforge-latentmas push
   ```
2. **Loader implementation** — separate work block, its own handoff. Blocked until this contract is committed. Does NOT start in the same session as this synthesis (Pattern D).
3. **Parked, unchanged from June 7 handoff:** housekeeping pile (untracked files cleanup); polymarket-pull `VALID: limited` downgrade in `state_manifest.md`; polymarket-pull structural-finding writeup in `incident_ledger.md`. All still firewalled.

---

*End of synthesis. The Mode 1 v1 loader contract is locked. Implementation is the next, separate work block.*


---

## Amendment — July 11, 2026 (loader install session)

**What changed and why.** During the install (per `LOADER_HANDOVER_2026-06-28`), the first repo-location run hard-failed the Q5.1 identity check: only 3 of 8 markets returned. Tier 1 live-API probes established that the Gamma `/markets` endpoint silently applies `closed=false` by default even on explicit `condition_ids` queries, and `closed=true` is an exclusive filter. There is no single-call way to retrieve a registry containing any resolved market. The June 27 reproducer that validated "one bulk call returns all 8" was correct *at the time* — all 8 markets were then live, so the silent filter had nothing to hide.

**Q4(b) amended:** "one call for all 8" becomes a **two-pass bulk fetch** — bare query (live markets) + `closed=true` query (closed markets), merged by conditionId with a duplicate-cid hard-fail guard. This is API-forced, not a design preference. Everything else in Q4 stands: bulk `condition_ids` endpoint, no per-slug fallback, all-or-nothing atomicity (now across the merged pair), 3 attempts per call (1 + 2 retries per `RETRY_BACKOFF_SECONDS = [10, 30]`, verified at line 75), [L-1] no-silent-fallback posture unchanged.

**Retry-count wording note (pre-existing, not amended behavior):** the June 27 contract's Q4(c) reads "2 attempts (10s, 30s)"; the code implements 1 initial attempt + 2 retries = 3 attempts total. The (10s, 30s) backoffs match — the contract's "2" counts retries, worded as attempts. Recorded here as a wording imprecision that predates the July 11 fix; behavior was never in conflict.

**Q5.3 amended:** the single `api_response_sha256` becomes **dual hashes** — `api_response_sha256_live` and `api_response_sha256_closed` — one fingerprint per pass, computed from the raw as-received bytes of each response.

**Provenance:** fix designed as a Founder-approved 5-item plan, implemented in-session under explicit Pattern D override, verified through all gates (ast.parse -> selfcheck -> live run, exit 1 RETIRED_PRESENT). Commit `6476c03`; ledger entry July 11, 2026; cold re-read verification July 11 afternoon (commit `9f560a4`, existence verified at amendment time). File hash of record: `f487be95...`.
