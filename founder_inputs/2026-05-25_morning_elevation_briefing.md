# Multi-engine briefing — May 25, 2026

**Subject:** Where, if anywhere, the afternoon2 finding and three adjacent observations should be elevated in `docs/incident_ledger.md`.

**Format:** v2 hallucination-resistant briefing. Embedded verbatim source from the live ledger and from the May 24 afternoon2 handoff. Line tags for citation: L-N for ledger excerpts, H-N for afternoon2 handoff excerpts, F-N for afternoon2 finding facts.

**Important framing notes (please read before responding):**

1. **This briefing IS the prompt to respond to**, not a preview being shown to you. Yesterday's calibration_tracker review surfaced that ChatGPT's first response treated a similar briefing as meta-commentary rather than the prompt itself. Please respond substantively as Engine N of 3, not with commentary about the briefing format.

2. **You do not have terminal access.** All reproducers cited in this briefing are operator-runnable, not engine-runnable. If you would like to reason about a claim I have not embedded, name what you would want to see and I will surface it from source — do not invent contents.

3. **Cite the line tags in your reasoning.** If you anchor on a piece of evidence, name which tag (L-N, H-N, F-N) you are anchoring on. This catches hallucination early.

4. **The Founder's preferences and the Systems Engine's recommendations are deliberately withheld.** Reason from the embedded evidence to your own conclusions. Yesterday's afternoon3 multi-engine review followed the same discipline and produced sharper results than the lunch session that did not.

5. **Pattern D applies to your response.** If you find yourself drafting ready-to-paste ledger text, stop. The question is whether the entries should exist and roughly what shape they should take. The canonical writing happens in a future session against fresh-eyes review of the live ledger.

6. **The briefing carries four questions, not one.** They are related but answerable in different directions. Please answer each separately rather than collapsing them.

---

# Part 1: The afternoon2 finding (Tier 1)

## What was discovered (afternoon2 session, May 24, ~1:30pm–2:30pm Pacific)

**F-1.** The project's 11 fixed benchmark questions (Fed rates, Bitcoin, AI regulation, Tesla, CPI, S&P, Ethereum, unemployment, midterms × 3) are hardcoded in `experiments/benchmark/03_text_swarm.py` lines 31-41. These have been the canonical longitudinal-comparison set since March 30, 2026 founding.

**F-2.** Fuzzy-matching diagnostic against `~/Projects/data/polymarket/2026-05-24.json` (91 markets pulled May 24). Result: zero real semantic matches across all 11 questions. Best score was 0.40 — "Will Monero hit $1000 in 2026?" matching "Will the Fed cut rates by at least 50bps in 2026?" on shared tokens "2026" and "$" punctuation, not on meaning. All other matches were similar token-overlap artifacts.

**F-3.** Sample of first 5 Polymarket markets May 24: tennis, soccer match draw, Monero crypto, Colombia soccer, soccer over/under. Pattern: general Polymarket data, no category filtering at pull layer (by design per April 6 architectural rule — filtering lives downstream).

**F-4.** Keyword search against `~/Projects/data/kalshi/markets_2026-05-24.json` (1,000 markets). Event ticker prefix breakdown: 814 `KXMVESPORTSMULTIGAMEEXTENDED`, 178 `KXMVECROSSCATEGORY`, 8 `KXMVENBASINGLEGAME`. Sample of first 10 markets: NBA, MLB pitching, tennis, NBA, MLB, MLB, MLB pitching, MLB, Premier League soccer, NBA. All sports.

**F-5.** Topic keyword search returned 0 real hits for Bitcoin, AI regulation, Tesla, CPI, S&P 500, Ethereum, unemployment, midterms, voter turnout. The 2 "Fed" hits were random substring matches on the letters "FED" inside sports event tickers.

**F-6. Bottom-line:** None of the 11 fixed benchmark questions appear in either the Polymarket daily pull (91 markets, mixed crypto/sports/soccer) or the Kalshi daily pull (1,000 markets, 100% sports) on May 24, 2026.

## The failure mechanism

**F-7.** `experiments/benchmark/03_text_swarm.py` line 45 contains a silent fallback: when the matching layer fails to find a market for a benchmark question, the script returns `0.5` (coin-flip crowd value) and continues. No error, no log entry, no exception.

**F-8.** Text-swarm was loaded into launchd from approximately April 18 (post-contamination rebuild via commit `6457e02`) through April 20 (when it went dormant — see incident_ledger.md Section 4 May 23 entry). During those two days, the script ran daily and produced output files `text_swarm_2026-04-19.md` and `text_swarm_2026-04-20.md` containing silent-0.5 fallback values for every market it could not match.

**F-9.** Fake output was undetected at the time on both days. The April 19 output was committed via `6488a0a` ("quarantine: commercialization_thesis.md...") with no quarantine markers on the text-swarm output file — the modification was an incidental script re-run picked up by `git add`, not a deliberate edit recognizing the output as compromised.

**F-10.** Text-swarm has not been executed since April 20, 2026. The component is `[LOADED: no | VALID: no]` per current state_manifest.md.

## What the afternoon2 handoff says about elevation

**H-1.** From `founder_inputs/2026-05-24_afternoon2_end_of_session_handoff.md` "What this session got done" section:

> "This is a Pattern A shape (silent fallback producing structurally legitimate output against semantically invalid input) at a much larger scope than the May 24 morning shadow_match finding or this session's earlier diagnostic-script Finding 1. Whether it warrants pattern elevation in `incident_ledger.md` Section 8 is a fresh-session decision (Pattern D guard: do not elevate during the discovery session)."

**H-2.** From the same handoff, "What the fresh session should do" Step 7:

> "Decide ledger-elevation for this session's findings. The afternoon2-finding (11 questions not in either pull + Pattern A silent fallback in production) is structurally substantive. Possible homes: (a) Standalone Section 4 entry under May 24 (third May 24 entry — would join shadow_match audit and calibration_tracker audit); (b) Section 8 pattern entry if elevated as a new Pattern A instance at production-component scope; (c) Both; (d) Neither (just fold into the architectural-change commit that addresses it). Pattern D applies here. The fresh session can decide whether to elevate; the actual ledger writing should be a separate work block."

**Note on H-1 and H-2 framing:** The afternoon2 handoff describes the finding as "a Pattern A shape" and frames the Section 8 question as "elevated as a new Pattern A instance." This framing should be evaluated against the live ledger's actual Pattern A text (embedded in Part 2 below) and against the live ledger's closing paragraph on silent fallbacks (also embedded in Part 2). The framing may or may not match the live taxonomy. Engines should reason against the live taxonomy, not the handoff's framing.

---

# Part 2: The live ledger as it stands (embedded verbatim)

## Pattern A through Pattern E (Section 8 "Cross-cutting patterns")

**L-1.** Pattern A:

> "Pattern A — Compounding mechanisms hide in sort logic. Apr 19 documented the commercialization-agent Social Proof Loop as one compounding channel: the THESIS_FILE write-back, where each run reads the prior day's thesis as input. The Apr 29 script audit revealed a second compounding channel that had operated invisibly the entire time: load_latest(REVENUE_DIR) at line 81 picks the lexicographically-greatest filename via sorted(..., reverse=True). Because commercialization_* filenames always sort after YYYY-MM-DD.md in reverse-alphabetical order, this call returns commercialization-agent's own previous output whenever any commercialization output exists in the directory. The variable is named prev_revenue but the data is its own past output. Generalization for future audits: structural compounding mechanisms can hide inside utility functions whose names misleadingly describe a different role. Sort-logic, filename-prefix collisions, and mtime-vs-lexical ordering are the specific surfaces this case exposes; other agents may have analogous hiding surfaces not yet audited."

**L-2.** Pattern B:

> "Pattern B — Scope narrowness in remediation passes. Remediation scope tracks the discovery surface, not the contamination surface. The Apr 18 sweep rewrote the agent in the active launchd pipeline (text_swarm) but missed shadow_match.py because shadow_match.py was not scheduled in launchd and did not surface during the production-pipeline review. Apr 20 caught it. Apr 20's own grep was scoped narrowly to policy_markets_seed; the broader audit named in Apr 20 Question 1 never executed. The April 18 sweep also missed 01_kalshi_selector.py, found by Apr 20's grep — Apr 20 caught two seed-file loaders that Apr 18 had missed. Pattern: when a remediation pass is scoped to 'the active pipeline' or 'this specific search term,' contamination outside that scope persists."

**L-3.** Pattern C: Filename is not behavior. (Identification by content, not by name. Examples: 01_kalshi_selector.py read seed file not Kalshi; launchd job com.latentforge.compression-researcher invokes latent_compression_researcher.py.)

**L-4.** Pattern D: Finding-real, prescription-wrong. (Prescriptions drafted while still inside contaminated state can be built on the same Tier 3 inferences the contamination came from. Discipline: finding identification and prescription writing should be temporally separated.)

**L-5.** Pattern E: Runtime-input contamination as a propagation surface. (Apr 20's "artifact calcification" stage covered static artifacts; runtime inputs to production agents are a separate propagation type. revenue-strategist parses BRAIN.md sections into agent prompt context daily.)

## The closing paragraph on what Section 8 does NOT establish

**L-6.** From immediately after Pattern E:

> "What Section 8 does not establish. The named-mode taxonomy for the April 18–20 contamination remains at two: Social Proof Loop and intra-engine confabulation, both named by the Apr 20 supplement. Patterns A through E are extensions, not new named modes. Two close-cousin concepts are canonically named elsewhere and not imported here: the Context-Filling Machine framing in intent.md's Decision Rule for Design Changes and state_manifest.md's session-tainting rule; and **the 'silent fallback' instance from Section 7 Finding 1, which is an instance of the four-stage sequence's 'ambiguous output' stage rather than a separately-named pattern.** Future readers asking which framing applies should consult the home document."

**Bold added for emphasis.** This is the live ledger's canonical position on silent fallback as a category: it is an instance of an existing four-stage sequence, not a pattern in its own right.

## The four-stage sequence referenced in L-6

**L-7.** From earlier in Section 8 ("The common pattern"):

> "Apr 20's analysis of the four events identified a four-stage sequence: engine reads ambiguous output → generates confident narrative → forward-propagates without returning to raw data → narrative calcifies into artifact layer. This sequence is preserved as the canonical pattern for the April 18–20 contamination episode."

## Section 4 May 24 entries (for structural reference)

**L-8.** The shadow_match May 24 audit entry begins:

> "May 24, 2026 — shadow_match.py audited; structural invalidity across data, metric, narrative, and cost layers (Pro-Thesis Optimization Loop, candidate pattern). Audit of experiments/benchmark/shadow_match.py (259 lines, HEAD aad034e) surfaced seven findings that together form a closed loop in which the script is structurally incapable of falsifying the project's core hypothesis."

— and runs approximately 60 paragraphs covering audit findings, multi-engine review, convergence as evidence, architectural findings 1-5, hygiene findings 6-7, deferred-pattern marker discipline, status, and cross-references.

**L-9.** The calibration_tracker May 24 audit entry begins:

> "May 24, 2026 — calibration_tracker.py audited; VALID restored. Audit of experiments/benchmark/calibration_tracker.py (304 lines, HEAD c01f7ba) surfaced seven findings establishing structural validity, followed by five operational verification checks confirming the script's runtime health."

— and runs approximately 50 paragraphs covering audit findings, operational verification checks, multi-engine review, the v1-hallucination-and-v2-defenses episode, corrections to prior framing, pattern observation (recorded, not elevated), and status.

Both entries follow the same structural shape: substantive finding, embedded reproducers, multi-engine review, corrections to prior framing if any, status, cross-references.

---

# Part 3: The three other adjacent observations

In addition to the afternoon2 finding above, three other observations from the May 23-25 arc are candidates for elevation.

## Observation 1: The afternoon3 protocol pattern

**H-3.** From `founder_inputs/2026-05-24_afternoon3_engine_responses.md` Part 8:

> "The first round of multi-engine review (afternoon2) produced converging direction (all three said D). The second round (this file) produced converging critique of a synthesis. The pattern is that multi-engine review is most powerful not at the recommendation layer but at the critique-of-recommendation layer. Implication: in future architectural decisions, 'draft synthesis → multi-engine critique → Founder commits' may be a more reliable structure than 'multi-engine recommend → Founder commits.'"

**H-4.** From the afternoon3 handoff "Open structural questions parked":

> "The 'draft synthesis → multi-engine critique → Founder commits' pattern. Three-engine convergence on a critique of a single synthesis element is structurally stronger evidence than three-engine convergence on a recommendation. This may deserve formalization as a protocol refinement. Parked for fresh-context review."

The observation is from one session (afternoon3, May 24). One data point.

## Observation 2: The "evening vs afternoon" CFM slip

**H-5.** From the afternoon2 handoff "Correction note":

> "An earlier draft of this file labelled this session 'evening' and used '6pm–9pm Pacific' plus phrasing like 'tonight,' 'tomorrow-you,' and 'sleep second' throughout. That framing was a Systems Engine inference error — Claude built a mental picture of a late-night session and let it leak into the document. Founder caught it. The real session window is afternoon (~1:30–2:30pm Pacific). The next fresh-context session is later today, not tomorrow."

**H-6.** Same handoff, Step 8:

> "The CFM-slip class here is a small one: Claude inferred a scene (tired Founder, late at night, ready for sleep) without evidence, and let the inference shape language. Worth a future-session decision on whether to log it formally in incident_ledger.md as a Section 4 entry; the catch worked, and the discipline implication is just Systems Engine should not infer time-of-day or Founder-state without evidence."

This is the second CFM event in the May 24 arc — the first was the calibration_tracker v1 briefing hallucination, already documented in incident_ledger.md Section 4 May 24 second entry. That earlier event was caught and contained but is preserved in the existing entry rather than its own standalone Section 4 entry.

## Observation 3: The deferred-pattern marker count

**H-7.** From the afternoon3 handoff "Open structural questions parked":

> "Three deferred-pattern markers in the ledger. Pattern F candidate (engine-prescribed-during-emergency-response, May 23); Pro-Thesis Optimization Loop candidate (May 24 shadow_match); v1-hallucination event (May 24 calibration_tracker). The afternoon2 handoff anticipated a fourth (production-scope Pattern A from the afternoon2 finding); the afternoon3 work may add a fifth. At four or five deferred markers, the deferral discipline may need a meta-review mechanism — but that meta-review is also Pattern D territory."

The count of deferred-pattern markers is four to five depending on how Observations 1 and 2 above are resolved. This is not itself a candidate for elevation, but it is context.

---

# Part 4: The four questions

For each, please give: Position; Reasoning (2-4 sentences with line-tag citations); Shape if "yes" (what rough form does the entry take — Section 4 audit-trail entry like L-8/L-9? Sub-bullet to existing Pattern A in L-1? Extension to L-6's closing paragraph? Something else?). DO NOT draft canonical text — describe shape only. Structural concerns if any.

## Question 1: The afternoon2 finding as a Section 4 audit-trail entry

Should the afternoon2 finding (11 questions not in either pull + silent 0.5 fallback in text-swarm) be recorded as a standalone Section 4 entry under May 24, joining the shadow_match audit (L-8) and the calibration_tracker audit (L-9) as the third May 24 entry?

## Question 2: The afternoon2 finding in Section 8

Where in the Section 8 taxonomy, if anywhere, does the afternoon2 finding belong?

Options to consider (not exhaustive):

(a) New Pattern F. Distinct from Patterns A-E. The afternoon2 framing in H-1 calls it "Pattern A shape" but the live Pattern A (L-1) is about sort-logic compounding, not silent fallback. May warrant its own pattern letter if it surfaces something the existing taxonomy does not capture.

(b) Sub-bullet to Pattern B. Pattern B (L-2) is "scope narrowness in remediation passes." Could be argued to extend B: the April 18 remediation closed the data-source contamination but did not verify that the live data contained the markets the scripts measure — a different kind of scope narrowness.

(c) Extension to L-6's closing paragraph. The live ledger says silent fallback is an instance of the four-stage sequence (L-7), not a separately-named pattern. Could be added as a second instance, extending the closing paragraph rather than minting a new pattern.

(d) Section 4 only. The finding is substantive at audit-trail level but does not surface a new structural pattern beyond what L-6 already establishes.

(e) Something else.

Note: The framing in H-1 may or may not match the live taxonomy in L-1 and L-6. Please reason against the live taxonomy.

## Question 3: The afternoon3 protocol observation

Should the "draft synthesis → multi-engine critique → Founder commits" observation (H-3, H-4) be recorded anywhere, and if so, where?

Considerations: discipline observation not failure record; one data point; handoff has already parked it.

## Question 4: The "evening vs afternoon" CFM slip

Should the "evening vs afternoon" time-inference CFM slip (H-5, H-6) be recorded anywhere, and if so, where?

Considerations: same CFM family as calibration_tracker v1 hallucination (already in L-9); catch worked; discipline implication is small.

---

# Part 5: Anti-bias check

Please flag: framing that rules out an option you would have preferred to surface; phrases or assumptions that anchor toward a particular answer; whether embedded source is sufficient; whether the four questions are correctly decomposed.

---

*End of briefing. Three engines responding cold. Founder synthesizes after all three are captured.*
