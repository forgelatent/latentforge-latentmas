# Gate 4 cold re-read — findings and resolution

**Date:** September 14, 2026
**Session:** fresh context; bootstrap bundle + three handoffs; did not perform the selection
**Subject:** `benchmark_registry_v2_CANDIDATE.json` (sha256 `b5e9f9cd…`, commit `03ffbff`)
**Verdict:** NOT CONFIRMED as submitted. **Confirmed after two Founder-approved replacements.**

---

## 1. Integrity (step 1) — PASS

All five hashes matched the Sept 14 handoff exactly: CANDIDATE `b5e9f9cd…`, pool-of-record
`160b2628…`, pull tool v3_1 `e1b6e97c…`, mode1 loader `8ce0ca39…` (Gate 3 version),
registry v1 `db050ed5…`. No uncommitted changes to any canonical file.

*Reproducer:* `git ls-files | grep -E "CANDIDATE|qualifying_pool|v3_1|market_state_loader" | xargs shasum -a 256`

## 2. Rules as submitted (step 2)

| Rule | Requirement | As submitted |
|---|---|---|
| 3a | 15 markets | PASS |
| 3b | max 3 settling per calendar month | **FAIL** — F1 |
| 3c | at least 5 open-ended or 180d+ | PASS, zero margin — exactly 5 |
| 3e | $10K floor, max 2 exceptions | PASS — lowest $26,503; 0 exceptions |
| 3f | category mix documented | **FAIL on accuracy** — F3 |

## 3. Findings

### F1 — 3b violated: four markets settle on one day, masked by the year boundary

Picks 7, 8, 9, 10 all settle at the end of December 31, 2026. `end_date` split them 2/2 across
"December 2026" and "January 2027" because two are phrased as deadlines (`before 2027`, `in 2026`)
and carry a 2027-01-01 stamp. Month-bucketing on `end_date` reported 2 and 2, passing 3b; real
exposure was 4 of 15 — 27% of the registry — expiring simultaneously.

This is v1's failure mode. 3b exists because 5 of v1's 8 markets shared ~June 30 deadlines and
resolved together five weeks after selection.

**Resolved** by D4 (drop pick 7).

### F2 — pick 13 had posted depth but no crowd

Russia x Ukraine ceasefire: liquidity $114,465.50, lifetime volume $3,880.90 — posted depth ~30x
total lifetime trading. Every other pick traded $137K-$66M lifetime.

3e filters on liquidity, which measures quoted depth, not revealed interest. The benchmark scores
agents against a crowd price; $3.8K of lifetime trading is a market-maker quote, not a consensus.

Confirmed as a family trait during replacement search: the sibling ceasefire markets (by Mar 31 2027,
by Jun 30 2027) scored v/l 1.1x and 0.8x. The whole question family is quoted-but-untraded.

**Resolved** by D2 (replace pick 13).

### F3 — 3f block inaccurate; correlation disclosure incomplete

- Declared category counts summed to **14**, not 15. The note accounted for one dual-tagged pick
  (Senate) but two exist (Senate, California wealth tax).
- Corrected as submitted: geopolitics **8**, not 7 — 53% of the registry.
- The declared US-Iran correlation was a **trio**, not a pair: pick 7 (Strait of Hormuz) loaded on
  the same US-Iran conflict variable as picks 9 and 12.
- Undeclared: picks 4 and 5 both settle on 2026 US election day, correlated through the same
  partisan wave.

**Resolved** by D3. The Iran trio reverted to the accepted pair as a side effect of D4.

### F4 — `end_date` mislabels settlement month on a third pick

Found while re-checking all 15 under D1. Pick 3 (Bitcoin $82,500 "in September") carries `end_date`
2026-10-01 but settles September 30; the selection session counted it as October. Corrected in the
settlement map (section 5). No rule breach resulted.

### F5 — `end_date` unusable on an entire market family

Found during replacement search. About 19 of 53 candidates were crypto "FDV one day after launch"
markets across nine different products (Predict.fun, Variational, Base, Abstract, Unit, Cambria,
Tread, Arc, Dreamcash). **All carried an identical `end_date` of 2028-01-01 and 473d** — a
placeholder, not a settlement date.

These have an unknowable settlement date and cannot be bucketed under 3b at all. All rejected.
Two further candidates were rejected on the same ground: Anthropic IPO (`end_date` 2027-07-01 while
the question says October 31 2026 — about 47 days, not 289) and OpenAI market cap at IPO close
(settlement conditional on an IPO occurring).

### F6 — long-runway supply in this pool is genuinely thin

Of 12,640 pool records, only 28 cleared 180d+ with $10K liquidity and $100K volume. After removing
the FDV family, the ceasefire family, and direct conflicts with existing picks, the usable slate was
roughly six markets. Outside crypto token launches and 2028 US election markets, Polymarket's
180-day-plus horizon is sparse.

Not a selection error. **Implication:** 3c will be the binding constraint on every future version,
and the pool tool may need a lower volume floor at long horizons to surface enough candidates.

## 4. Founder decisions (September 14, 2026)

### D1 — 3b is read semantically. **Standing; applies to all future selections.**

The rule exists to prevent mass same-day expiry. **Settlement date governs; the `end_date` field does
not.** Future selections must bucket by when a market actually resolves, derived from the question
text wherever the field disagrees. Markets with unknowable settlement dates (F5) are not selectable.

### D2 — pick 13 replaced; volume recorded alongside liquidity. **Standing.**

A liquidity number without trading volume is not a crowd. Replacements require real lifetime volume,
not posted depth. Volume is recorded beside liquidity for every pick going forward.

### D3 — F3 accepted as stated

3f corrected; the Iran cluster and the election-day pair named explicitly in the registry file.

### D4 — pick 7 (Strait of Hormuz) is the Dec-31 settler dropped

Chosen because it resolves F1 and the F3 Iran trio in one move. **Cost accepted on record:** pick 7
had $11.7M lifetime volume against $397K liquidity — one of the healthiest crowds in the set — and
was the registry's only other-commodities pick.

### D5 — replacements: skin cancer vaccine FDA, and Milei Argentina

Both sourced from `scratch/qualifying_pool_2026-09-14.json` (verified hash), never from engine
general knowledge.

- **Skin cancer vaccine FDA approved by December 31, 2027** — 473d, settles Dec 31 2027,
  liq $21,482, vol $84,228, v/l 3.9x. New domain (biotech regulatory), uncorrelated with all
  other picks, fills the month pick 13 vacated.
- **Will Javier Milei win the 2027 Argentina presidential election** — 404d, settles Oct 24 2027,
  liq $23,701, vol $174,357, v/l 7.4x. Chosen over the Alito SCOTUS alternative;
  **cost accepted on record:** returns geopolitics to 8/15 (53%), undoing F3's incidental fix.

## 5. Final registry — settlement map under D1

| Settlement | Count | Picks |
|---|---|---|
| Sep 2026 | 1 | Bitcoin $82.5k |
| Oct 2026 | 2 | Bolsonaro, Fed October |
| Nov 2026 | 3 | GOP Senate, CA wealth tax, Iotova |
| Dec 2026 | 3 | Apple, US-Iran invasion, Clarity Act |
| Mar 2027 | 1 | US x Iran meeting |
| Apr 2027 | 1 | Le Pen |
| Oct 2027 | 1 | Milei |
| Dec 2027 | 1 | Skin cancer vaccine |
| Nov 2028 | 2 | Vance nomination, GOP 2028 |

**Rules on the final set:** 3a PASS (15), 3b PASS (max 3), 3c PASS with margin (6: picks 10-15,
each verified against question text), 3e PASS (lowest $21,427, zero exceptions), 3f geopolitics 8,
policy 3, macro 1, crypto 1, ai-tech 1, other 1.

**Declared correlations:** US-Iran pair (invasion and diplomatic meeting, opposite valence);
Vance nomination feeding GOP 2028 general; Senate control and CA wealth tax (same 2026 election
day); Bolsonaro and Milei (thin South American right-populist linkage).

## 6. Live verification (step 3) — PASS, 15/15

Checked against the live Gamma API, two-pass (bare returned 15 rows; `closed=true` returned 0 rows;
no overlap). Liveness per the Round 4 contract (`closed==False AND acceptingOrders==True`).

- **15/15 LIVE.** All open and accepting orders.
- **15/15 above the $10K floor.** Lowest: Milei $21,427.
- **15/15 v/l above 1.0.** Lowest: Fed October at 2.1x. Highest: US-Iran at 100.3x.
- Liquidity drift from selection: -13% to +14%. Ordinary intraday movement, no collapse.

*Reproducer:* fetch the 15 conditionIds from `gamma-api.polymarket.com/markets` with the loader's
User-Agent; read `liquidityNum` and `volumeNum`.

## 7. Judgment pass (step 4) — endorsed

Prices span 0.165 to 0.695, so no market is a gimme. Eight distinct resolution months. Domains cover
elections on three continents, monetary policy, crypto, equities, legislation, biotech regulation.
Every price is backed by real trading.

**Three characteristics recorded, none disqualifying:**

1. Geopolitics at 8/15 (53%) — the largest concentration; accepted under D5.
2. Three markets settle simultaneously on Dec 31 2026 (20% of the registry). At the 3b cap exactly.
3. Two resolve within three weeks — Bitcoin (16d), Bolsonaro (19d). The registry drops to 13 live by
   early October; the 3d version trigger sits at 10.

**Forward implication:** a v3 conversation is likely due around January 2027 once the December
cluster clears. Flagged now rather than discovered later.

## 8. Root pattern (three instances this session)

Every rule in 3a-3f is enforced against a Gamma API field, and two of those fields do not mean what
the rules assume:

- **`end_date` is not settlement date** — F1, F4, F5. Three distinct surfaces in one registry.
- **`liquidity` is not crowd participation** — F2. Quoted depth, not revealed interest.

The selection session applied the rules correctly as written. The rules leaned on the API. This joins
the standing Gamma cautions: `endDate` unreliable (June 27, 2026), the silent closed-filter
(July 11), and the eight traversal pathologies (July 12).

**Generalization for future rule-writing:** a rule that names an API field is only as good as that
field's semantics. Where a rule encodes intent (do not cluster expiries, require a real crowd), the
check must be written against the intent, with the field as evidence rather than as definition.

## 9. Session texture

- **The repo's own working code is the reference implementation.** Two live-check failures this
  session came from writing fresh fetch logic instead of borrowing the loader's: (a) HTTP 403,
  because Gamma requires a real User-Agent — documented at loader line 64; (b) all money fields
  reading zero, because `liquidity` and `volume` are **strings** while `liquidityNum` and
  `volumeNum` are floats — the loader already reads the Num variants via `require_num_field`.
  Both traps were solved in the file being repointed. Borrow mechanics; do not rewrite them.
- **The zero readings were caught only by cross-checking against pool figures.** Without an
  independent number to compare against, fifteen zero results could have read as total collapse.
  Reproducer discipline working as intended.
- **A null `days_to_resolution` crashed the first filter pass.** 49 pool records carry null day
  counts (the open-ended bucket). Excluded from candidate search deliberately and visibly,
  consistent with the Sept 14 finding that the null-endDate bucket is contaminated with
  short-runway markets.
- **New paste hazard: a document pasted into the shell runs as commands.** A draft of this file was
  pasted at a zsh prompt; the shell parsed the markdown as instructions, errored on table pipes, and
  left the terminal inside an unclosed quote that swallowed the next command. No file was created or
  modified (verified by hash and `git status`). This differs from the known heredoc echo blind-spot:
  the hazard is a document entering the shell, not a large paste being truncated. Canonical
  documents should be handed over inside a quoted heredoc so the shell treats them as text.
- **Oversized heredoc aborted safely.** A 95-line part-1 paste was truncated mid-transfer and left
  zsh at a `heredoc>` prompt. Because zsh collects the heredoc before running the command, no file
  was created. Recovery was Ctrl-C, not typing the terminator — typing it would have written a
  truncated file that looked plausible. The document was then rewritten as seven parts of about 40
  lines each, every part guarded and content-checked. Reaffirms the July 60-line ceiling.
- **Incidental infrastructure observations** (section 10) were surfaced by `git status` during
  step 1, not sought out.

## 10. Infrastructure observed incidentally

- **No Strategic Drift.** `launchctl` shows exactly the six jobs the manifest declares loaded.
  text-swarm is not loaded; its `swarm_cron.log` (Apr 20 05:27) and final output
  `text_swarm_2026-04-20.md` are stale uncommitted artifacts, not evidence of execution.
- **mode1 loader healthy.** Daily output through Sept 14, clean RETIRED_PRESENT exit 1. Six ERROR
  sidecars dated July 15-27 represent a closed transient window.
- **v1 is at live=1 retired=7** as of the Sept 14 04:58 run — past the 3d urgent threshold
  (below 6). The v2 handover is the remedy already in flight.
- **research-sweep and compression-researcher produced no output August 11 to September 8**
  (about 4 weeks), both restarting Sept 8-9. Absent files rather than false "all quiet" digests —
  the July 12 fix behaving as designed. Both are research-only with no downstream impact; registry
  selection unaffected. Cause not investigated.

## 11. Outstanding after this file

1. Promote CANDIDATE to locked v2 (apply D4/D5 edits, rename, commit).
2. Repoint the mode1 loader job to v2.
3. Archive v1 with the July note template (registry companion note, manifest entry, ledger).
4. Manifest updates, including the stale mode1-loader hash `f487be95` to `8ce0ca39`.
5. Queued ledger entries from the Sept 14 selection session: open-ended/null-endDate contamination;
   recurring-market churn and auto-split traversal.
6. Pattern-minting queue, twice deferred: inconsistent-view API pattern; research-sweep
   silent-success second instance. F5 and section 8 may be relevant input.
