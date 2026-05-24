# Multi-engine briefing — benchmark set vs. data pull mismatch

**To:** Gemini, ChatGPT, Grok
**From:** John McGuire (Founder Engine) + Claude (Systems Engine)
**Date:** May 24, 2026 evening
**Type:** Multi-engine review — structural direction decision
**This briefing IS the prompt to respond to.** Not a preview. Please respond substantively.

---

## What this briefing asks of you

A diagnostic run tonight surfaced a finding that affects multiple components of the LatentForge measurement infrastructure. The Founder has not stated a preferred direction. Three engines (you plus two others) are being asked to review the evidence and recommend a structural response, cold and independent.

The context, the embedded verbatim terminal output from tonight's diagnostic steps, and the four options surfaced so far are below. Please respond in the structured format requested at the end.

---

## Hallucination-resistance discipline

Per `incident_ledger.md` Section 4 May 24 entry, "v1 hallucination and v2 structural defenses":

- The terminal output below is **verbatim** from the operator's terminal session tonight. Reason from this evidence, not from what you imagine the data looks like.
- You do not have terminal access. You are reviewing the operator's audit. If you need to verify a claim, name the reproducer command and the Founder will run it.
- Cite specific embedded line tags (e.g. "the K-1 line showing 0 Bitcoin hits") when anchoring claims to evidence.
- If a claim in this briefing does not match what you see in the embedded output, flag it explicitly.

---

## Context

LatentForge runs a measurement infrastructure built around **eleven fixed benchmark questions** chosen at March 30, 2026 founding for longitudinal comparison purposes. The eleven questions live as a hardcoded Python list in `experiments/benchmark/03_text_swarm.py` lines 31-41. Two production components depend on these eleven markets existing in the daily prediction-market data pulls:

1. **text-swarm** (currently `[LOADED: no | VALID: no]` per `state_manifest.md` — unloaded for separate matching-layer + random-number-swarm issues, see `incident_ledger.md` May 23 entry)
2. **shadow_match** (currently `[not in launchd | VALID: no]` — under restoration; multi-engine review earlier today locked five of six decisions, see `founder_inputs/2026-05-24_shadow_match_restoration_review.md`)

The architectural pattern (per `build_log.md` Section 3.2) is **parallel implementations**: text-swarm and shadow_match each run the same 11 questions through swarm logic for longitudinal comparison. The diagnostic value depends on the 11 being a stable measurement set whose results can be compared across days, weeks, and months.

A separate component, **calibration-tracker** (`[LOADED: yes | VALID: yes]` per the May 24 audit that restored its trust), does *not* use the eleven-question set. It uses live-discovered markets from Polymarket filtered by category and 5-95% probability bands. It is operationally healthy. This briefing is **not** about calibration-tracker.

---

## What we found tonight

The finding came from trying to answer a small question: "when do the 11 benchmark markets resolve?" — needed to decide a reload-gate for shadow_match. The diagnostic process revealed something bigger than the original question.

### Step 1: Locate the eleven questions in the source

```
$ grep -n -E "question|market|benchmark" experiments/benchmark/03_text_swarm.py | head -40
[S-1]  29:# Fixed benchmark markets (same 11 as before)
[S-2]  31:    {"id": 1, "question": "Will the Fed cut rates by at least 50bps in 2026?"},
[S-3]  32:    {"id": 2, "question": "Will Bitcoin reach $150,000 by end of 2026?"},
[S-4]  33:    {"id": 3, "question": "Will AI regulation bill pass in US Congress before end of 2026?"},
[S-5]  34:    {"id": 4, "question": "Will Elon Musk remain CEO of Tesla through 2027?"},
[S-6]  35:    {"id": 5, "question": "Will US CPI inflation be above 3% in April 2026?"},
[S-7]  36:    {"id": 6, "question": "Will S&P 500 be above 5500 at end of April 2026?"},
[S-8]  37:    {"id": 7, "question": "Will Ethereum close above $2000 in April 2026?"},
[S-9]  38:    {"id": 8, "question": "Will US unemployment rate rise above 4.5% in Q2 2026?"},
[S-10] 39:    {"id": 9, "question": "Will Republicans win the House majority in 2026 midterms?"},
[S-11] 40:    {"id": 10, "question": "Will Democrats win the Senate majority in 2026 midterms?"},
[S-12] 41:    {"id": 11, "question": "Will US voter turnout exceed 50% in 2026 midterms?"},
[S-13] 45:    """Read live Polymarket price. Returns 0.5 only if nothing is usable."""
[S-14] 73:def get_live_crowd_price(question):
[S-15] 74:    """Pull current YES price from latest Polymarket JSON."""
[S-16] 81:        q_lower = question.lower()
[S-17] 82:        for m in markets:
[S-18] 83:            api_q = m.get("question", "").lower()
```

The 11 questions are policy/macro/markets/elections — the categories the project's revenue-exploration arm is supposed to measure. Line S-13 shows text-swarm's matching function `get_live_crowd_price` returns `0.5` (coin flip) when no live data is usable.

### Step 2: Search for the 11 in today's Polymarket pull

A diagnostic script ran each of the 11 questions against the Polymarket pull at `~/Projects/data/polymarket/2026-05-24.json` using fuzzy token-overlap matching (threshold >0.3, preferring tz-aware `endDate` field over date-only `endDateIso` per Finding 1 from tonight's session-findings file).

```
[K-1]  Total markets in pull: 91
[K-2]
[K-3]  Q1: Will the Fed cut rates by at least 50bps in 2026?
[K-4]    Matched (score 0.40): Will Monero hit $1000 in 2026?
[K-5]    endDate: 2027-01-01T05:00:00Z  (+221 days from now)  status: OPEN
[K-6]
[K-7]  Q2: Will Bitcoin reach $150,000 by end of 2026?
[K-8]    Matched (score 0.40): Will Monero hit $1000 in 2026?
[K-9]    endDate: 2027-01-01T05:00:00Z  (+221 days from now)  status: OPEN
[K-10]
[K-11] Q3: Will AI regulation bill pass in US Congress before end of 2026?
[K-12]   NO MATCH (best score: 0.29)
[K-13]
[K-14] Q4: Will Elon Musk remain CEO of Tesla through 2027?
[K-15]   NO MATCH (best score: 0.29)
[K-16]
[K-17] Q5: Will US CPI inflation be above 3% in April 2026?
[K-18]   Matched (score 0.40): Will Monero hit $1000 in 2026?
[K-19]   endDate: 2027-01-01T05:00:00Z  (+221 days from now)  status: OPEN
[K-20]
[K-21] Q6: Will S&P 500 be above 5500 at end of April 2026?
[K-22]   Matched (score 0.40): Will Monero hit $1000 in 2026?
[K-23]   endDate: 2027-01-01T05:00:00Z  (+221 days from now)  status: OPEN
[K-24]
[K-25] Q7: Will Ethereum close above $2000 in April 2026?
[K-26]   NO MATCH (best score: 0.29)
[K-27]
[K-28] Q8: Will US unemployment rate rise above 4.5% in Q2 2026?
[K-29]   NO MATCH (best score: 0.29)
[K-30]
[K-31] Q9: Will Republicans win the House majority in 2026 midterms?
[K-32]   Matched (score 0.33): Will the Republican Party win the CO-01 House seat?
[K-33]   endDate: 2026-11-03T00:00:00Z  (+162 days from now)  status: OPEN
[K-34]
[K-35] Q10: Will Democrats win the Senate majority in 2026 midterms?
[K-36]   Matched (score 0.33): Will Pamela Evette win the 2026 South Carolina Governor Republican primary
[K-37]   endDate: 2026-06-09T00:00:00Z  (+15 days from now)  status: OPEN
[K-38]
[K-39] Q11: Will US voter turnout exceed 50% in 2026 midterms?
[K-40]   Matched (score 0.33): Will Pamela Evette win the 2026 South Carolina Governor Republican primary
[K-41]   endDate: 2026-06-09T00:00:00Z  (+15 days from now)  status: OPEN
```

**Reader note:** the "matches" above are token-overlap artifacts on shared words like "2026" or "House" or "Republican." Semantically none of the 11 questions match any market in today's pull. Best real-match score across all 11 was 0.40, achieved by "Will Monero hit $1000 in 2026?" — clearly not the same question as any of the 11. The remaining matches at 0.29-0.33 are equally semantic mismatches.

### Step 3: Verify the shape of the Polymarket pull

Sample of the first 5 markets in today's Polymarket pull for category identification:

```
[P-1] question: Kosice: Kilian Feldbausch vs Gilles Arnaud Bailly       (tennis)
[P-2] question: Will the match end in a draw?                            (soccer)
[P-3] question: Will Monero hit $1000 in 2026?                           (crypto)
[P-4] question: Will Colombia win on 2026-06-01?                         (soccer)
[P-5] question: CD La Serena vs. CD Limache: O/U 2.5                     (soccer)
```

The polymarket-pull job (per `state_manifest.md` and `build_log.md` Section 2.1.2) pulls general Polymarket data with no category filtering at the pull layer. Filtering by category happens downstream in calibration-tracker per the April 6 architectural rule ("LLMs handle judgment, scripts handle everything else"). This is by design.

### Step 4: Search for the 11 in today's Kalshi pull

The Kalshi pull at `~/Projects/data/kalshi/markets_2026-05-24.json` contains 1,000 markets. Event ticker prefix counts:

```
[KAL-1] Total markets: 1000
[KAL-2]
[KAL-3] Event ticker prefixes (top 20 by count):
[KAL-4]    814  KXMVESPORTSMULTIGAMEEXTENDED
[KAL-5]    178  KXMVECROSSCATEGORY
[KAL-6]      8  KXMVENBASINGLEGAME
```

Keyword search across all 1,000 markets for the 11 questions' topics:

```
[KAL-7]  Fed/rates: 2 markets across 2 events
[KAL-8]      KXMVESPORTSMULTIGAMEEXTENDED-S2026EF887159C06
[KAL-9]      KXMVECROSSCATEGORY-S2026129FED64CDF
[KAL-10] Bitcoin: 0 markets across 0 events
[KAL-11] AI regulation: 0 markets across 0 events
[KAL-12] Tesla/Musk: 0 markets across 0 events
[KAL-13] CPI/inflation: 0 markets across 0 events
[KAL-14] S&P 500: 0 markets across 0 events
[KAL-15] Ethereum: 0 markets across 0 events
[KAL-16] Unemployment: 0 markets across 0 events
[KAL-17] Midterms/House/Senate: 0 markets across 0 events
[KAL-18] Voter turnout: 0 markets across 0 events
```

Sample of the first 10 markets in today's Kalshi pull (for category identification):

```
[KSAMP-1]  yes San Antonio, yes New York, yes Evan Mobley: 10+               (NBA)
[KSAMP-2]  yes Mitch Keller: 2+, yes Brandon Young: 3+                       (MLB pitching)
[KSAMP-3]  yes Alexander Zverev, yes Alejandro Davidovich Fokina             (tennis)
[KSAMP-4]  yes Stephon Castle: 15+, yes Oklahoma City wins by over 2.5       (NBA)
[KSAMP-5]  yes Over 6.5 runs scored                                          (MLB)
[KSAMP-6]  yes Mitch Keller: 2+, yes Drew Rasmussen: 3+                      (MLB pitching)
[KSAMP-7]  yes Dylan Cease: 5+, yes Brandon Young: 3+                        (MLB pitching)
[KSAMP-8]  yes Yoshinobu Yamamoto: 7+, yes Los Angeles D wins by over 1.5    (MLB)
[KSAMP-9]  yes Both Teams To Score, yes Manchester United, yes Newcastle     (soccer)
[KSAMP-10] yes Shai Gilgeous-Alexander: 4+, yes De'Aaron Fox: 2+             (NBA)
```

**Reader note:** The 2 "Fed" hits at lines KAL-8/KAL-9 are random substring matches on the letters "FED" within sports event tickers (`...EF887...` and `...129FED64...`). They are not real Fed-rate markets. The 814 + 178 + 8 = 1000 prefix breakdown is consistent with the first-10 sample at KSAMP-1 through KSAMP-10: 100% sports.

The current kalshi-pull uses public endpoints only. Kalshi's authenticated policy/macro endpoints require RSA authentication that was deferred at March 29 founding (per `state_manifest.md` kalshi-pull entry and `build_log.md` Section 2.1.1).

### Bottom line

**None of the 11 fixed benchmark questions appear in either the Polymarket daily pull (91 markets, mixed crypto/sports/soccer) or the Kalshi daily pull (1,000 markets, 100% sports) on May 24, 2026.**

text-swarm's silent fallback to `0.5` for unmatched markets (line S-13) means it has been generating output against fake crowd values whenever it has run. shadow_match has the same dependency. The April 18 contamination response replaced the seed-file data source with live Polymarket reads (`state_manifest.md` and `incident_ledger.md` April 18 entry) — but the question of *whether the live data contains the markets the scripts measure* was not part of that remediation's scope.

---

## Open question for the engines

**The 11-question benchmark set is not present in the data the project is currently pulling.** Multiple downstream components depend on these markets being in the data. What is the right structural response?

### Four options surfaced so far

- **Option A: Update the benchmark set.** Audit Polymarket and/or Kalshi for what is available, select a new fixed set of questions that match real markets, update text-swarm and shadow_match to use the new set. Preserves the longitudinal-comparison design at the cost of resetting the longitudinal clock.

- **Option B: Update the data pull.** Investigate whether different Polymarket API endpoints, filtering parameters, or paid plans would surface the 11 existing questions. Or pursue Kalshi RSA authentication to unlock policy markets. Or both. Preserves the benchmark set; changes the infrastructure feeding it.

- **Option C: Shift to live-discovered markets.** Remove the eleven-question hardcoded list. Have text-swarm and shadow_match operate on live-discovered markets the way calibration-tracker already does. Trades longitudinal-comparison value for measurements that match the data actually present.

- **Option D: Reconsider what the components are for.** Including but not limited to: consolidating shadow_match into calibration-tracker if the diagnostic value overlaps; scoping the project's measurement infrastructure to what calibration-tracker already covers; rebuilding the benchmark around resolved markets only; revisiting whether the four-arm benchmark architecture (per `build_log.md` Section 1.3) still requires a fixed parallel comparison set.

### What the briefing asks

For each engine: please respond with

```
Recommendation: [A / B / C / D — and if D, name the option]
Reasoning: 2-4 sentences anchored on specific embedded output line tags (S-N, K-N, P-N, KAL-N, KSAMP-N)
Code/architecture outline: rough structure of what changes; pseudocode acceptable
Sequencing: what must happen before what
Structural concerns: anything not addressed in the four options above
Anti-bias check: any place where the briefing's framing rules out an option you would have preferred to surface
```

End with a single overall-assessment paragraph.

---

## Important framing notes for the engines

1. **This is not a fire.** No external claims have been made on text-swarm output. shadow_match is already unloaded. calibration-tracker is healthy and unaffected. The project's scientific-arm work (Mac Mini activation steering, per `intent.md`) is unaffected. The decision can be made carefully.

2. **The Pattern D guard applies to the response, not just the discovery.** The Founder is aware that engine recommendations under cognitive pressure of fresh discoveries can themselves be "finding-real, prescription-wrong." Please flag if your recommendation feels rushed — better to recommend "investigate further before deciding" than to commit to a direction prematurely.

3. **There is a parked question:** Grok's anti-bias flag at lunch named the deeper question of whether shadow_match should exist at all given calibration-tracker's existence. That question is in scope for Option D.

4. **There is a known operational matter:** text-swarm has separate structural problems (matching layer broken; swarm logic replaced with random number generation; see `incident_ledger.md` May 23 entry). Whatever direction is chosen will need to integrate with text-swarm restoration. Engines should treat text-swarm as "also under restoration, separately" rather than as an independent constraint.

5. **The eleven questions themselves may not be sacred.** Both Gemini and ChatGPT independently flagged at lunch that the original March 30 benchmark set should be audited for fit-for-purpose. Option A and Option D both implicitly accept this. Option B implicitly preserves the questions; please name this if recommending B.

---

## Response format requested

Respond as a single message addressed back to the Founder Engine. Do not include meta-commentary on the briefing. Do not infer Founder preferences. Cite embedded line tags (S-N, K-N, P-N, KAL-N, KSAMP-N) where you anchor claims.

If the embedded evidence is insufficient for you to make a recommendation, name what additional reproducer command would help and the Founder will run it.

---

*End of briefing.*
