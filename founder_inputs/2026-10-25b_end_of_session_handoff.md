# End-of-session handoff (second), October 25, 2026

**Session:** continuation of the Oct 25 session after `71bd10d`. Read-only; records only. Written by Systems Engine (Claude) with the Founder. Tier 3 except where marked Tier 1.

## 1. Cold-round synthesis (delivered in chat; not filed as its own document)
- Draft-KV (arXiv 2609.34754, Sept 28; code github.com/Svardfox/Draft-KV, Apache 2.0) read in full: main text, appendices A-G. Shared-input protocol with a text-to-text control on the identical draft: latent beats text in 33 of 35 settings, mean +5.85 pp; on the only strong-receiver row (Qwen3-8B -> Qwen3-4B) the gap runs -0.1 to +3.8 pp, mean about +2.1. Latent arm is a trained 1.05M-parameter bridge at 13.745 TFLOPs vs 7.187 for text (Table 8). No error bars on the medium gap. Its swap test gives LatentMAS 0.60 pp pairing gain of a 4.86 pp system gain on ARC-C: the plan's step-4 latent arm is content-blind under shared input. ChatGPT's Draft-KV figures verified exact.
- Readers: Q1 no (4/4; Grok and ChatGPT quote the paper, both Gemini answered from the briefing). Q2 open (4/4). Q3 budget undefined (3/4); effect inside the margin under shared input (Argon; now Draft-KV's number). Q4 pause (3/4), fix-sleep-first (Gemini run 1). STOP 3/4; ChatGPT a feasibility gate.
- Systems Engine recommendation: STOP, about 65% (was 55/45 for the experiment on Sept 25; one paper moved it). If not STOP: ChatGPT's gate with four preconditions (budget definition; latent arm chosen by pairing gain; Mac Mini check; margin set knowing the expected effect is about +2 pp).

## 2. Founder direction (Tier 3, stated in session; NOT a decision note)
- Founder wants to continue toward proving useful divergence on the Polymarket data collected since April. "$10M" means proof, not money. Open on domain. Resources: Mac Mini plus time; rented GPUs if needed.
- Working reframe, accepted in session: the differentiated test is latent vs strong text on a decision task with resolved outcomes; no paper found tests that. The main test needs question + resolution only; a saved crowd price is a third baseline, not a requirement.
- Decision note still unwritten. The "$10M" wording should be retired or redefined in it.

## 3. Polymarket data inventory (Tier 1; commands run on host Oct 25; `scratch/polymarket_pool_count_2026-10-25.py` reproduces the pool numbers)
- 138 daily files, 2026-03-23 to 2026-10-25 (217-day span); 62-200 markets per file, 76-90 in the newest ten; 503 KB to 1.59 MB.
- 6 files predate the April 19 launchd job (Mar 23, 28, 29; Apr 4, 18, 19). Provenance unknown; untrusted until the writing script is found. 2026-03-23 holds 100 closed markets with API-shaped prices (likely the historical-benchmark pull: inferred, not established).
- Snapshots hold zero closed markets (Apr 20: 0; Oct 25: 0). Resolutions are not on disk and must be fetched (Gamma closed=true trap, Pattern G; borrow the loader's two-pass fetch).
- 8,463 distinct conditionIds; 7,266 with endDate past; 107 with none. Lifespan: <1d 411, 1-7d 2,459, 7-30d 2,435, 30-180d 1,277, >180d 1,038, unknown 843. First-seen to endDate: same-day-or-past 1,831, 1-7d 3,630, 8-30d 1,147, >30d 1,748.
- Sports by API flags (sportsMarketType or events[0].gameId): 3,209. Crypto by keyword: 705. Policy/geo/macro by keyword: 842 (rough).
- **Candidate pool:** policy keyword, not crypto, not sports, ended, seen 7+ days ahead: 433; minus 21 "will X say Y" markets: **412 markets on 292 independent events**; 223 seen 30+ days ahead; 112 with volumeNum over $10K. Ten sampled questions were a mix of real questions, word games, and multi-outcome slices of one event.
- Fields present: question, conditionId, endDate, closed, outcomePrices, umaResolutionStatuses, sportsMarketType, volumeNum, events (no category field).

## 4. Not established
Why daily counts fell from 191 (Apr 20) to 84 (Oct 25): pull script not read. How any pool market actually resolved. Model-cutoff leakage (a rule is needed in pre-registration). endDate is unreliable (Sept 14). Keyword buckets are rough. Draft-KV Appendix H not fully read; its code not run. polymarket-pull's October runs not checked.

## 5. Next session do / do-not
**Do:** Founder writes the decision note first. Then, in order: verify polymarket-pull's October runs; resolution-lookup script (first internet touch, read-only, two-pass, own reproducer); step-1 definition of "useful divergence" as a scoreable rule (a document, then a cold round); Mac Mini check; pause the other jobs only after the Founder says so.
**Do not:** design the experiment before the budget definition exists; name a model without a filed search; pause or unload anything on your own; cite 412 as "resolved" (it is "ended by endDate"; resolution unverified).

## 6. Added later the same day (after `94abd78`)
- Founder decision note committed `2db498f`; manifest updated `f6a354a` (HEAD anchor, kalshi-pull LOADED: no, registry 13/2, suggestions 37/104). kalshi-pull unloaded Oct 25 (`launchctl list | grep -c kalshi` returns 0). Lid stays open overnight by Founder decision.
- **Resolution lookup done (Tier 1):** `scratch/pool_resolution_lookup_2026-10-25.py` (64 lines; borrows the loader's Gamma mechanics) wrote `scratch/pool_resolutions_2026-10-25.json`: 410 of 412 resolved (81 YES, 329 NO) across 291 events; 2 STILL_OPEN (both "next Prime Minister of Sweden", endDate 2026-09-14, API says open); 0 NOT_FOUND, 0 ambiguous. Clears the decision note's 250/150 floors. Resolution read from settlement prices (one side >= 0.99, the other <= 0.01).
- `umaResolutionStatuses` is NOT a usable second source: 220 of 410 settled markets show only `["proposed"]`; "resolved" appears in 115. Pattern G Form 2 shape. Recorded, not counted.
- YES rate is 19.8% (81 of 410): many pool markets are slices of one event. The scoring rule must count by event and compare both arms against a base-rate baseline, not only against each other.
- Not verified: any label against the real world. Founder eyeballed ten sampled questions. Settlement prices paid real money and are the best truth available.
- Systems Engine errors: three wrong counts (44 for 29, 27 for 25, "files" label on first-seen days); the lookup script's first half did not land on the first paste (file had 30 lines; caught by `wc -l` before running).
- Next session: the scoring-rule document for "useful divergence" (step 1 of the work order), then a cold round on it. Not to be started at the end of a long day.
