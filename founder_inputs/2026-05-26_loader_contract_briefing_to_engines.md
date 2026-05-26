# Loader contract briefing — Mode 1 v1 loader logic

**Date:** May 26, 2026 afternoon
**Maintainer:** John McGuire (Founder Engine), with Claude (Systems Engine)
**Status:** Briefing for triple-engine cold review. Round 4 in the May-architectural-arc sequence.
**Cross-references:**
- `founder_inputs/2026-05-24_afternoon3_end_of_session_handoff.md` (architectural lock — load-bearing)
- `founder_inputs/2026-05-25_afternoon_step7_founder_synthesis.md` (six locked Step 7 decisions)
- `founder_inputs/2026-05-26_round3_founder_synthesis.md` (8 markets locked, registry built)
- `founder_inputs/2026-05-26_round3_market_selection_briefing.md` (Round 3 briefing — format template)
- `experiments/benchmark/benchmark_registry_v1.json` (the registry the loader reads, HEAD `be7aa94`)
- `scratch/full_pull_and_filter.py` (one of two existing Polymarket-query code patterns in the repo)
- `experiments/week1/scripts/polymarket_pull.py` (the other Polymarket-query pattern)

---

## Section 1: Context and inheritance

Read all of Section 1 before answering. The questions in Section 7 are downstream of what is locked vs. open here.

### 1.1 The architectural arc so far

This is the fourth multi-engine review in the May-architectural-arc:

- **May 24 afternoon3:** Architecture locked. Two-mode structure (Mode 1 + Mode 2). shadow_match becomes thin overlay. Silent 0.5 fallback dies — replaced with explicit `NO_LIVE_MARKET` state. text-swarm rebuilt against Mode 1. Variant A registry (explicit Polymarket slugs/condition IDs, immutable within version, hard-fail-then-iterate on retirement).
- **May 25 Step 7:** Six selection criteria locked. Decision 2 (Polymarket as primary surface) was a Founder override against triple-engine convergence on a hybrid surface. Liquidity floor deferred to Round 3.
- **May 26 Round 3:** 8 markets selected from a 298-market qualifying pool. Liquidity floor locked at $10K with two named soft exceptions (China GDP $4K, SCOTUS $5K). `benchmark_registry_v1.json` built and pushed (HEAD `be7aa94`).
- **May 26 Round 4 (this briefing):** Loader contract — the script that reads the registry, queries Polymarket for current state per market, and produces output downstream agents (rebuilt text-swarm, four-arm benchmark scoring) consume.

The architectural lock and the registry are inputs to this review. **Do not re-open them.** The legitimate triggers for re-opening the architecture are documented in the afternoon3 handoff; nothing in the loader work surfaces those triggers.

### 1.2 What is locked (inherited from prior rounds)

**[L-1] Hard-fail visibility, no silent fallback.** From afternoon3: *"Silent 0.5 fallback dies in the rebuild. Replaced with explicit `NO_LIVE_MARKET` state. Hard-fail visibility. Triply confirmed."* This is the principle the loader must honor. The afternoon3 lock did not specify operational granularity — that is what this briefing exists to settle.

**[L-2] The 8 markets and the registry.** Per `benchmark_registry_v1.json` v1 schema. The registry records durable identifiers (slug, condition_id, end_date), a selection-time snapshot (price, liquidity, volume, days), engine support, and the $10K liquidity floor with named exceptions. The loader's input is this file. The 8 slugs are not under review.

**[L-3] Variant A immutability semantics.** From afternoon3: *"When a market retires or resolves, the registry hard-fails on that slug. Founder makes an explicit logged decision to iterate to v2 with new slugs."* The loader must surface retirement/resolution as a hard-fail condition, not paper over it.

**[L-4] Mode 1 = controlled longitudinal benchmark, Mode 2 = operational calibration (calibration-tracker, unchanged).** The loader serves Mode 1 specifically. It is not a general-purpose Polymarket query layer.

### 1.3 What is open (this briefing's scope)

**[O-1] Granularity of the not-live state.** The afternoon3 lock named one bucket: `NO_LIVE_MARKET`. The Polymarket Gamma API (per evidence in Section 4) returns at least four distinguishable states: alive, closed, missing, network-error. Question: does the loader emit a single `NO_LIVE_MARKET` bucket, or distinct states per failure mode?

**[O-2] Output schema for live markets.** What fields does the loader write per live market? The registry has durable IDs + snapshot. The Polymarket response has ~50 fields. Downstream consumers (rebuilt text-swarm, scoring layer) need *some* subset. Which?

**[O-3] Scheduling.** Manual-only (like shadow_match)? launchd between polymarket-pull (4:43 AM) and downstream agents? Founder-triggered during morning routine? The afternoon3 lock is silent on this.

**[O-4] HTTP pattern choice.** The repo currently has two coexisting patterns: `urllib.request` with explicit User-Agent (in `scratch/full_pull_and_filter.py`), and `requests` library (in `experiments/week1/scripts/polymarket_pull.py`). The loader is the first component that's a candidate to set precedent for future condition_id-keyed work. Which pattern, and why?

**[O-5 — meta-question]** Is there a structural design question about the loader that this briefing did not ask? See Section 7 Q5.

### 1.4 What this briefing is NOT for

- Not for re-opening any of [L-1] through [L-4].
- Not for revising the 8 selected markets.
- Not for proposing alternative liquidity floors.
- Not for re-litigating Decision 2 (Polymarket primary).
- Not for designing the rebuilt text-swarm itself — that's downstream of this loader and gets its own review.
- Not for designing the four-arm benchmark scoring layer — also downstream.
- Not for the polymarket-pull remediation (separate work block per Pattern D, per the May 26 morning handoff).

---

## Section 2: The afternoon3 architectural lock (verbatim)

Source: `founder_inputs/2026-05-24_afternoon3_end_of_session_handoff.md`, "The architectural direction (now locked)" section.

> After the cold-critique pass, four elements survive triple-engine review and are *locked*:
>
> 1. **Two-mode structure.** Mode 1 = controlled longitudinal benchmark. Mode 2 = operational calibration (calibration-tracker, unchanged). Triply confirmed.
> 2. **shadow_match becomes thin diagnostic overlay.** Not benchmark-defining. Runs against whichever mode is active. Triply confirmed.
> 3. **Silent 0.5 fallback dies in the rebuild.** Replaced with explicit `NO_LIVE_MARKET` state. Hard-fail visibility. Triply confirmed.
> 4. **text-swarm gets rebuilt against Mode 1.** Conditional on Mode 1 being deterministic/stable enough. Triply confirmed (all three with conditions named).

Source: same document, "Variant A (Founder decision, locked)" section.

> Mode 1's registry holds **explicit Polymarket slugs/condition IDs**. 8-12 markets. Immutable within a version (v1.0, v2.0, etc.). When a market retires or resolves, the registry hard-fails on that slug. Founder makes an explicit logged decision to iterate to v2 with new slugs. Longitudinal comparison resumes on the new version with a clean version-boundary.

The "Silent 0.5 fallback dies. Replaced with explicit NO_LIVE_MARKET state. Hard-fail visibility" sentence is the *constitutional language* for this briefing. Engines should treat that sentence as the principle, and the operational schema as the question.

---

## Section 3: Anti-anchoring framing — read before answering

This briefing is a fourth multi-engine review in 48 hours. Briefing fatigue is a real risk. The Systems Engine has noticed pattern-matching shapes in prior responses (especially when subsequent rounds re-use prior framing). Three explicit anti-bias asks before you answer:

1. **The NO_LIVE_MARKET single-bucket framing in [L-1] may be wrong.** It came from a fast-paced afternoon3 session where the architectural decision was the primary concern and the operational granularity was not in scope. If you think the operational reality (Section 4) demands more than one bucket, *propose the granularity you would design instead*. The lock was on the *principle* (no silent fallback). The single-bucket *expression* of that principle is not load-bearing — only the principle is.

2. **The four questions in Section 7 may be the wrong four questions.** Q5 explicitly invites you to propose a fifth (or replace one of the four). If the Systems Engine's framing is missing a load-bearing question, flag it. The afternoon3 retrospective explicitly named "Systems Engine produced a synthesis that solved the visible problem but introduced a deeper problem that the synthesis author did not see" as a Context-Filling Machine pattern. This briefing is at risk for the same pattern.

3. **Defer to your own judgment, not to convergence with prior engine responses.** Three engines have triply-confirmed the architecture and triply-converged on the $10K floor and produced multi-engine convergence on 4 of the 8 markets. If you find yourself wanting to converge here because converging has been the recent pattern, that is anchoring. The Founder catches convergence-as-pattern; produce your honest answer even if it diverges.

The Founder will read three responses cold and synthesize. Disagreement among engines is informative; agreement-by-anchoring is not.


---

## Section 4: Loader-context observations (E-tags)

This section names what the Systems Engine learned while preparing the briefing. Three Polymarket Gamma API probes were run today (May 26, 2026 afternoon) to ground the briefing in real API behavior. Probe outputs are embedded verbatim in Section 5.

**[E-1] No prior project code queries Polymarket by condition_id.**

`grep -rn "conditionId\|condition_id" experiments/ scripts/` returns only the 8 entries from the registry built tonight. The launchd-scheduled `polymarket_pull.py` queries `?active=true&closed=false&order=volume&limit=200` (top-200-by-volume — the basis of the May 26 morning structural finding). `scratch/full_pull_and_filter.py` pages the full surface via `?limit=500&offset=N`. Neither uses condition_id. The loader is the first component in the project's history to query Polymarket by a per-market key. The contract this briefing settles will likely set precedent for future condition_id-keyed work.

**[E-2] Per-slug query returns a list, not an object.**

A query like `?slug=will-china-gdp-growth-in-q2-2026-be-between-4pt6-and-4pt9` returns a JSON list. For a real slug, the list has exactly one element. For a fake slug, the list is empty (`[]`). The API does not return 404 on missing markets. It returns 200 with an empty list. Downstream code that does `data[0]` without checking length will crash. Downstream code that does `data.get(...)` against the list assuming it's a dict will get `None` and silent-fallback.

**[E-3] `active: True` does NOT mean "currently tradable."**

Three closed historical markets (one from 2020) all return `active: True, closed: True, archived: False`. The `active` field appears to mean "not an admin-deleted scaffolding row," not "this market is accepting trades right now." The real "is this market alive for our purposes" signal is `closed == False` AND probably `endDate` in the future. Code that uses `active` as the liveness signal will treat every closed market as live — a Pattern A-shaped silent contamination.

**[E-4] `outcomePrices` is a JSON-encoded string, not a list.**

Real market response: `"outcomePrices": "[\"0.505\", \"0.495\"]"`. The value is the string `[\"0.505\", \"0.495\"]`, not the Python list `["0.505", "0.495"]`. This is the *exact bug pattern* that bit text-swarm on April 20, 2026 (per `incident_ledger.md` Section 7 Finding 1: *"`outcomePrices` is a JSON-encoded string (e.g. `'[\"0.749\", \"0.251\"]'`), not a list. The `isinstance(..., list)` check failed silently. Execution fell through to a hardcoded 0.5. Every market. Every run."*). The text-swarm fix (commit `987a171`) added a `_extract_price()` helper that explicitly `json.loads()` the field. The loader inherits the same trap. Any output of the loader that exposes prices to downstream code must either (a) decode the string explicitly with hard-fail on parse error, or (b) emit the parsed list rather than the raw string. If the loader passes the raw API response through unmodified, every downstream consumer must remember this trap. That distributes the risk; the afternoon3 lock's "no silent fallback" principle argues for centralizing the parse in the loader.

**[E-5] `outcomePrices: ["0", "0"]` on closed markets is real, not resolution data.**

All three closed historical markets returned `outcomePrices: "[\"0\", \"0\"]"`. A resolved binary market should have `["1", "0"]` or `["0", "1"]` depending on which outcome won. `[\"0\", \"0\"]` is what closed markets emit *regardless* of how they resolved. **Resolution outcomes are not surfaced on the `/markets` endpoint.** They likely live on a different endpoint (UMA oracle, `/resolutions`, or `/markets/{slug}/resolution`). The loader's scope question becomes: does the loader need resolution data, or only live-state data? `calibration_tracker.py` already queries Polymarket directly for resolution (per its May 24 audit, lines 87-89) — so resolution may not be the loader's job.

**[E-6] Field-type heterogeneity in the API response.**

Several fields appear in both string and numeric form: `liquidity` is `"3837.1978"` (string) while `liquidityNum` is `3837.1978` (float); `volume` is `"8580.893536999998"` (string) while `volumeNum` is `8580.893536999998` (float). The string variants are the canonical/historical field names; the `*Num` variants are typed. Loader code that does arithmetic on the string forms will produce string concatenation errors or wrong comparisons. The loader contract should specify whether it normalizes types (output always-numeric) or pass-through (preserve API shape).

**[E-7] Snapshot vs live drift is already happening in the registry.**

China GDP's `selection_snapshot.liquidity_usd` is `4094.30` (recorded this morning, May 26). The live query 8 hours later returns `liquidity: "3837.1978"` — a 6.3% drop in one day. This is expected behavior for an active market and is exactly why the registry uses a `selection_snapshot` sub-object rather than primary fields. But it is load-bearing for the loader: the loader's output must be tagged as "live state" with a fresh timestamp. Downstream code that confuses snapshot with live state will produce stale measurements that look fresh.

**[E-8] Two coexisting HTTP patterns in the existing codebase.**

`scratch/full_pull_and_filter.py` uses `urllib.request.Request(url, headers={"User-Agent": "latentforge-fullpull/1.0"})` followed by `urllib.request.urlopen(req, timeout=30)`. `experiments/week1/scripts/polymarket_pull.py` uses `requests.get(url, params=params, timeout=30)`. Both patterns work today; both are real prior art. The User-Agent header matters — a bare `urllib.request.urlopen` without explicit UA returns HTTP 403 from Polymarket Gamma (this was confirmed during briefing prep). The loader picking one pattern sets precedent for the launchd-scheduled implementations that follow. Stdlib-only (urllib) has zero dependency cost but more boilerplate. `requests` is more ergonomic but introduces a dependency that the existing project mostly avoids (compression-researcher and revenue-strategist use `requests`; polymarket-pull uses `requests`; full_pull_and_filter and shadow_match use urllib). The pattern is genuinely mixed, not converged.

**[E-9] Multiple endpoints the loader could choose between.**

The probes used `https://gamma-api.polymarket.com/markets?slug=...`. Alternatives that exist:

- `gamma-api.polymarket.com/markets?condition_ids=...` (returned 403 in our probe; may be deprecated, may require auth, untested with proper UA)
- `gamma-api.polymarket.com/markets/{id}` (untested; uses numeric Polymarket internal ID, not slug or condition_id)
- `clob.polymarket.com/...` (the CLOB API — likely needed for live order-book data, possibly auth-required)

The choice of endpoint affects the loader contract because different endpoints expose different fields, different freshness, and different auth requirements. The `/markets?slug=...` pattern works without auth, returns ~50 fields per market, and is what the existing launchd-scheduled `polymarket_pull.py` uses. The Systems Engine's instinct is that `/markets?slug=...` is the right endpoint for Mode 1 loader purposes — but this is the kind of inference the briefing is at risk for being wrong about.

---

## Section 5: Embedded verbatim API responses

These are the three probes that produced Section 4's findings. Embedded so engines can reason from real evidence rather than imagined API behavior. The Founder ran these from the production MacBook with the same User-Agent the existing scratch code uses.

### 5.1 Probe A — live market (China GDP, registry market #1)

```
$ python3 -c "
import urllib.request, json
url = 'https://gamma-api.polymarket.com/markets?slug=will-china-gdp-growth-in-q2-2026-be-between-4pt6-and-4pt9'
req = urllib.request.Request(url, headers={'User-Agent': 'latentforge-loader-probe/1.0'})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read())
print('Type:', type(data).__name__)
print('Count:', len(data) if isinstance(data, list) else 'N/A')
print(json.dumps(data, indent=2)[:4000])
"
```

Returns:

```
Type: list
Count: 1

[
  {
    "id": "2009765",
    "question": "Will China GDP growth in Q2 2026 be between 4.6% and 4.9%?",
    "conditionId": "0x800be7611c7efcdf5827c049e0baac8b6047b506af412e283dbac9ce7e202560",
    "slug": "will-china-gdp-growth-in-q2-2026-be-between-4pt6-and-4pt9",
    "endDate": "2026-07-16T00:00:00Z",
    "liquidity": "3837.1978",
    "startDate": "2026-04-20T21:32:21.497855Z",
    "description": "[truncated for brevity — full resolution-source description]",
    "outcomes": "[\"Yes\", \"No\"]",
    "outcomePrices": "[\"0.505\", \"0.495\"]",
    "volume": "8580.893536999998",
    "active": true,
    "closed": false,
    "createdAt": "2026-04-17T23:07:36.085601Z",
    "updatedAt": "2026-05-26T19:14:07.070469Z",
    "new": false,
    "featured": false,
    "submitted_by": "0x91430CaD2d3975766499717fA0D66A78D814E5c5",
    "archived": false,
    "resolvedBy": "0x69c47De9D4D3Dad79590d61b9e05918E03775f24",
    "restricted": true,
    "groupItemTitle": "4.6-4.9%",
    "groupItemThreshold": "3",
    "questionID": "0xd17eeec91f17d91ba673078a833bb5449f38951f6027d829bce97a1d783f6403",
    "enableOrderBook": true,
    "orderPriceMinTickSize": 0.01,
    "orderMinSize": 5,
    "volumeNum": 8580.893536999998,
    "liquidityNum": 3837.1978,
    "endDateIso": "2026-07-16",
    "startDateIso": "2026-04-20",
    "hasReviewedDates": true,
    "volume24hr": 123.73332800000001,
    "volume1wk": 3983.7737330000004,
    "volume1mo": 7970.421558999999,
    "volume1yr": 8580.893537,
    "clobTokenIds": "[\"60196551632130876128019932489360671799975840052559223687292898215759557804287\", \"70668339471785900528475091629901275408520291138233281745786857671141494802357\"]",
    "umaBond": "500",
    "umaReward": "5",
    "acceptingOrders": true,
    "negRisk": true,
    "events": [
      {
        "id": "390159",
        "ticker": "china-gdp-growth-yy-in-q2-2026",
        "slug": "china-gdp-growth-yy-in-q2-2026",
        "title": "China GDP growth (Y/Y) in Q2 2026?"
      }
    ]
  }
]
```

### 5.2 Probe B — missing market (fake slug)

```
$ python3 -c "
import urllib.request, json
url = 'https://gamma-api.polymarket.com/markets?slug=this-market-does-not-exist-fake-slug-test-2026'
req = urllib.request.Request(url, headers={'User-Agent': 'latentforge-loader-probe/1.0'})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read())
print('Type:', type(data).__name__)
print('Count:', len(data) if isinstance(data, list) else 'N/A')
print('Response:', json.dumps(data, indent=2))
"
```

Returns:

```
Type: list
Count: 0
Response: []
```

### 5.3 Probe C — closed markets (3 historical examples)

```
$ python3 -c "
import urllib.request, json
url = 'https://gamma-api.polymarket.com/markets?closed=true&limit=3'
req = urllib.request.Request(url, headers={'User-Agent': 'latentforge-loader-probe/1.0'})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read())
print('Count:', len(data))
for m in data:
    print('---')
    print('slug:', m.get('slug'))
    print('closed:', m.get('closed'))
    print('active:', m.get('active'))
    print('archived:', m.get('archived'))
    print('endDate:', m.get('endDate'))
    print('outcomePrices:', m.get('outcomePrices'))
    print('umaResolutionStatus:', m.get('umaResolutionStatus', 'NOT PRESENT'))
"
```

Returns:

```
Count: 3

---
slug: will-joe-biden-get-coronavirus-before-the-election
closed: True
active: True
archived: False
endDate: 2020-11-04T00:00:00Z
outcomePrices: ["0", "0"]
umaResolutionStatus: NOT PRESENT
---
slug: will-airbnb-begin-publicly-trading-before-jan-1-2021
closed: True
active: True
archived: False
endDate: 2021-01-02T00:00:00Z
outcomePrices: ["0", "0"]
umaResolutionStatus: NOT PRESENT
---
slug: will-a-new-supreme-court-justice-be-confirmed-before-nov-3rd-2020
closed: True
active: True
archived: False
endDate: 2020-11-04T00:00:00Z
outcomePrices: ["0", "0"]
umaResolutionStatus: NOT PRESENT
```

Note: `active: True` on every closed market is what produced finding [E-3]. `outcomePrices: ["0", "0"]` on every closed market is what produced finding [E-5].


---

## Section 6: The April 15 first-flight context (F-tags, brief)

Preserved minimally for context. Full version in Round 3 briefing Section 6.

**[F-1]** On April 15, 2026, on Mac Mini M4 Pro, a bullish contrastive vector (h_bull - h_bear) was injected into a Phi-3 Mini agent's hidden state at layers 16/20/24 at scale 0.4. Agent B's probability estimate moved from 35% to 75% (40-point shift) with stance-specific bullish reasoning generated alongside. The test was specifically designed to remove the complement-arithmetic confound that had retracted the prior contrastive result hours earlier.

**[F-2]** Result is Tier 2 valid (reproducible internally, Mac Mini physics, no Polymarket dependency).

**[F-3]** Relevance to this briefing: the loader produces the live-market state that feeds the rebuilt text-swarm and (eventually) the four-arm benchmark. The Mode 1 markets are *vehicles* for testing whether the April 15 latent steering effect produces measurable divergence under real-money adversarial conditions. The loader must not introduce noise that would obscure or fake that signal.

---

## Section 7: Questions to answer

Answer all five questions. Length guidance: 2-4 paragraphs per question, plus the explicit recommendations called out. Cite line tags where relevant (L-N, O-N, E-N, F-N).

---

**Q1. Granularity of the not-live state — operational design.**

The afternoon3 lock named one bucket: `NO_LIVE_MARKET`. The API evidence in Section 4 ([E-2], [E-3], [E-5]) shows at least four distinguishable conditions:

- (a) Slug exists, `closed: false`, `endDate` in future → live
- (b) Slug exists, `closed: true` → closed (might be resolved, might be cancelled; resolution data lives elsewhere)
- (c) Slug returns empty list → market not found on Polymarket
- (d) API returns network error / 4xx / 5xx → cannot determine state

Propose the operational schema. Should the loader emit:

- **Option α:** Single `NO_LIVE_MARKET` bucket covering (b), (c), (d). Honors lock language literally. Loses information needed for v2 iteration decision.
- **Option β:** Three distinct states — `LIVE`, `RETIRED` (covers b + c, i.e., the registry's Variant A trigger for v2 iteration), `ERROR` (covers d, transient and retryable).
- **Option γ:** Four distinct states matching (a)-(d) exactly.
- **Option δ:** Your own proposal.

State your recommendation explicitly: "Schema: [α/β/γ/δ]. Reasoning: ..."

The principle (no silent fallback) is locked. The granularity (one bucket vs. several) is open. The lock's language was set when the operational reality wasn't yet probed. If your honest read of the API behavior calls for finer granularity, propose it; if you think the single bucket is right despite the multi-state reality, defend that.

---

**Q2. Output schema for live markets.**

For markets in state `LIVE`, what does the loader's output entry look like? The Polymarket response has ~50 fields. The registry already has the durable identifiers (slug, condition_id, end_date) plus a selection-time snapshot. Downstream consumers (the rebuilt text-swarm, the four-arm benchmark scoring layer) need *some* subset of live state.

Propose the per-market output schema. At minimum, specify:

1. **Which API fields are surfaced.** Just price (`outcomePrices`)? Price + volume + liquidity? All of the `*Num` typed fields? The full response unmodified?
2. **What transformations the loader performs.** Does it `json.loads()` the `outcomePrices` string (per [E-4])? Normalize types (str→float for the `Num` pairs)? Compute mid-prices? Compute days-to-resolution from `endDate`?
3. **What freshness metadata the output carries.** A `loader_run_at` timestamp per [E-7]? The API's `updatedAt` field passed through? Both?
4. **Whether the loader retains the registry's `selection_snapshot` in its output**, or whether snapshot-vs-live comparison is a downstream concern.

The afternoon3 lock implies the loader's output is *primarily for downstream agents*, not for direct founder reading. But downstream agents will read it during debugging, and the founder will inspect it during audits. Format should be machine-readable JSON; the question is how much transformation the loader does vs. how much it passes through.

---

**Q3. Scheduling and operational shape.**

The afternoon3 lock and Round 3 synthesis are silent on whether the loader runs:

- **Manual-only**, like shadow_match — founder triggers during morning routine; gaps are explicit. Pro: founder engagement on every run. Con: missed days produce gaps.
- **launchd-scheduled**, like polymarket-pull — runs every morning. Pro: continuous time series. Con: failures must be loud (one of the May 9 kalshi-pull silent-success findings — `incident_ledger.md` May 9 audit findings — is the exact failure mode to avoid).
- **Hybrid** — launchd-scheduled with founder-facing summary in the morning digest.

If launchd-scheduled, what time slot? Existing launchd morning sequence: compression-researcher 2:00 AM, research-sweep 4:30 AM, polymarket-pull 4:43 AM, kalshi-pull 4:45 AM. Downstream agents (rebuilt text-swarm, when restored) presumably want fresh loader output before they run — text-swarm was historically at 5:15 AM. The loader has to land between polymarket-pull (which it doesn't currently depend on but might in v2) and text-swarm.

Also: should the loader run *exactly once per day*, or *per-invocation-by-downstream-consumer*? The former produces a stable daily snapshot. The latter produces fresher data per request but invites duplicate API calls and inconsistency between consumers reading at different moments.

Propose: scheduling pattern + invocation pattern + time slot if applicable. Justify against existing operational patterns and the April 18 contamination lessons.

---

**Q4. HTTP pattern choice and implementation precedent.**

The repo has two coexisting Polymarket-query patterns per [E-8]. The loader is greenfield work and the chosen pattern becomes precedent for the next condition_id-keyed component(s) (the rebuilt text-swarm, possibly an audit/verification component).

Three sub-questions:

- **(a)** Which pattern — stdlib `urllib.request` with User-Agent, or `requests` library? Defend the choice on principle (dependency hygiene, ergonomics, robustness, alignment with the project's "scripts handle deterministic operations" April 6 architectural rule).
- **(b)** Which endpoint — `/markets?slug=...`, `/markets?condition_ids=...` (if it can be made to work with proper auth), `/markets/{id}` by Polymarket internal ID, or something else? Note that the registry has slug + condition_id but no internal ID; using internal ID would require an additional lookup. Note also that `condition_ids` query returned 403 in our probe under a generic UA; we did not test it under the working UA before pivoting to slug.
- **(c)** Should the loader retry on transient errors (rate limits, network blips), and if so what's the policy? The polymarket-pull wrapper does 3-attempt retry with 5-minute delays. Should the loader follow the same pattern, or is loader retry different because the loader is per-slug rather than full-pull?

---

**Q5. Is there a structural question this briefing did not ask?**

The four questions above cover state granularity, output schema, scheduling, and HTTP pattern. The Systems Engine flagged in [O-5] that this list might be incomplete. The afternoon3 retrospective explicitly named "Systems Engine produced a synthesis that solved the visible problem but introduced a deeper problem that the synthesis author did not see" as a CFM pattern.

Is there a structural question about the Mode 1 loader that Q1-Q4 did not address? Candidates the Systems Engine considered and chose not to spin out as separate questions (you may disagree about any of these):

- **Idempotency.** Should the loader be re-runnable on the same day producing the same output for downstream consumers? Affects whether downstream scoring is stable.
- **Validation.** Should the loader validate that the registry's `conditionId` matches the API's returned `conditionId` per slug? (i.e., catch the case where Polymarket reassigns a slug to a different market — unlikely but Pattern A-shaped if it happens silently)
- **Versioning of loader output.** Should the loader's output file carry a schema version, so downstream consumers can detect breaking changes?
- **Logging.** What gets logged per run, where does the log go, and how does the founder discover the log?
- **Failure-modal exit codes.** Per the May 9 kalshi-pull silent-success finding: should the loader's exit code distinguish (LIVE for all markets) from (some markets in non-live state) from (all markets in error)?
- **Inverse question:** is the loader actually the right abstraction at all? Or should each downstream consumer (rebuilt text-swarm, scoring layer) query Polymarket directly and the "loader" be a shared library function rather than a standalone script?

Pick the one (or two) you think are most load-bearing for the architectural correctness of Mode 1. Or propose something the Systems Engine didn't consider. Or argue the four questions are sufficient. If you do that last one, be explicit — the meta-question is asking you to either find the gap or close the door on it.

---

## Anti-bias self-check (answer in your response)

Same format as Round 2 and Round 3.

1. **What in the briefing's framing biases toward your answer?** Be specific. Section 4 reads as a Systems Engine narrative of the API discovery process; that narrative may bias toward Systems-Engine-preferred conclusions. Section 7 Q1's four explicit options (α/β/γ/δ) may anchor on the three Systems-Engine-named options. The Systems Engine's stated instinct in [E-9] that `/markets?slug=...` is the right endpoint may anchor your answer to Q4(b). Name what biased you.

2. **What did the briefing not include that would have made your answer more rigorous?** Examples: a probe of the `condition_ids` query under the working UA (not done in briefing prep — the slug pivot was made after the first 403); a probe of the resolution endpoint to confirm where resolution data lives; the polymarket_pull.py 200-market wrapper's full retry/backoff configuration; performance characteristics of the API under sustained per-slug querying. Name what was missing.

3. **Is there a 6th question that should have been asked but was not?** Q5 already invites a fifth question; this is the *meta-meta* check. If after answering Q1-Q5 you realize the Systems Engine's framing has a deeper gap that Q5 didn't catch, name it.

---

## Section 8: Response format guidance

- Lead with a one-line position summary: "Schema: [α/β/γ/δ]. Output: [shape]. Scheduling: [pattern]. HTTP: [pattern]. Most-load-bearing missing question: [Q5 answer]."
- Then the five numbered answers, in order. Q1-Q4 each get 2-4 paragraphs. Q5 gets 1-3 paragraphs.
- Then the three anti-bias self-check items.
- Cite line tags (L-N, O-N, E-N, F-N) where relevant. The Founder will read three responses cold and synthesize; tags make cross-comparison clean.
- Brevity preferred over comprehensiveness. The Founder is reading three responses and producing a synthesis decision; long responses get diminishing returns past about 1500 words.
- Do not consult other engines' answers. This is a cold review.
- If you want to propose code snippets (Python function signatures, output JSON shapes), do so inline. Pseudocode is fine; the Founder is not implementing tonight — the synthesis decides the contract, the implementation comes after.

---

*End of briefing. Engines: please answer cold. The Founder synthesis follows after all three responses are captured verbatim.*
