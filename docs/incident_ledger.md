# LatentForge — incident_ledger.md

**Accumulated remediation history. Read at session start as part of the Trinity of Truth.**

This file is the canonical entry point for the April 18–20 benchmark contamination incident and subsequent remediation work. The April 18 root incident record is preserved at `docs/INCIDENT_2026-04-18.md` and remains the citation target for inline disclaimer headers across the codebase. The April 19 and April 20 supplements have been consolidated into this file and archived verbatim at `docs/INCIDENT_ARCHIVE/`.

Last meaningful update: May 1, 2026 (consolidation of April 19 and April 20 supplements into existing taxonomy)
Maintained by: John McGuire (Founder Engine), with Systems Engine (Claude) and Divergent Thinking Engine (Grok)

---

## Archived sources

This ledger is the canonical record. Source documents are preserved in archive for audit-trail purposes only.

| Document | Location | Original date |
|---|---|---|
| April 18 root incident record | `docs/INCIDENT_2026-04-18.md` (in place — referenced by inline disclaimer headers across the codebase) | 2026-04-18 |
| April 19 manual pipeline simulation + remediation supplement | `docs/INCIDENT_ARCHIVE/INCIDENT_SUPPLEMENT_2026-04-19_ARCHIVED.md` | 2026-04-19 |
| April 20 audit + Apr 19 corrections supplement | `docs/INCIDENT_ARCHIVE/INCIDENT_SUPPLEMENT_2026-04-20_ARCHIVED.md` | 2026-04-20 |
| Quarantined seed file (root cause artifact) | `docs/INCIDENT_ARCHIVE/policy_markets_seed_DEPRECATED_DO_NOT_LOAD.json` | 2026-03-29 (authored), 2026-04-20 (quarantined) |

The April 18 document is in-place because 20+ inline disclaimer headers across the codebase cite it directly; moving it would invalidate those references. The supplements were moved because their only references were from the April 18 document and the prior version of this ledger.

---

## Incident summary

The April 18 contamination incident produced three rounds of remediation across three days. This table is a navigation index; details are in the sections that follow.

| Date | Event | Mechanism | Status | Source archive |
|---|---|---|---|---|
| 2026-04-18 | Benchmark contamination detected | Synthetic seed file (`policy_markets_seed.json`) had been read as live Polymarket data since March 29; "vs crowd" claims compounded across BRAIN.md, benchmark report, grant draft, outreach drafts | Closed (April 18 scope; April 19/20 supplements found additional contamination) | `docs/INCIDENT_2026-04-18.md` |
| 2026-04-19 | Manual pipeline simulation + remediation | Production-wrapper simulation of the launchd agent sequence caught one broken Python file, one poisoned shell env, two content failures (text_swarm matching, commercialization-agent Social Proof Loop); two narrative agents unloaded | Partially closed (infrastructure fixes complete; matching contract + agent rewrites open) | `docs/INCIDENT_ARCHIVE/INCIDENT_SUPPLEMENT_2026-04-19_ARCHIVED.md` |
| 2026-04-20 | Confabulation discovery + shadow_match unremediation | text_swarm price-extraction bug + matching logic broken; shadow_match.py never remediated in April 18 pass (still loading the seed file); intra-engine confabulation pattern named as separate failure mode from cross-engine Social Proof Loop | Partially closed (extraction fix + seed quarantine complete; matching contract + shadow_match rewrite + kalshi_selector decision open) | `docs/INCIDENT_ARCHIVE/INCIDENT_SUPPLEMENT_2026-04-20_ARCHIVED.md` |

The April 18 incident is the root record; April 19 and April 20 are remediation rounds that revealed additional layers of the same underlying contamination. No external claims were made during any phase of the incident — impact was internal only.

---

## Corrections to prior incident documents

- **April 20, 2026 — INCIDENT_SUPPLEMENT_2026-04-19 retraction (shadow_match.py status).** The April 19 supplement asserted: *"Shadow Match script verified pulling real prices (DeSantis 2.6%, Vance 39.1%, Bitcoin 28.5%, etc.)"* This claim was retracted on April 20 after `grep SEED_FILE experiments/benchmark/shadow_match.py` revealed the script still loads `policy_markets_seed.json` — the fictional seed file named as root cause in INCIDENT_2026-04-18. The cited prices came from the seed file, not the live API. The April 19 supplement also implied shadow_match was part of the active pipeline; it is not — shadow_match has never been scheduled in launchd. The `brainload_handoff` summary drafted April 20 PM repeated this misapprehension and is retracted along with the supplement claim. Both retractions accepted by all four engines on April 20 after reproducer evidence.

- **April 29, 2026 — INCIDENT_SUPPLEMENT_2026-04-19 framing incomplete (commercialization-agent Social Proof Loop).** Audit of `commercialization_agent.py` during `state_manifest.md` drafting revealed the Social Proof Loop has two compounding channels, not one as documented in INCIDENT_SUPPLEMENT_2026-04-19. The REVENUE_DIR channel (`load_latest` sort logic) is described in `state_manifest.md`'s commercialization-agent entry. The supplement's framing of the failure mechanism is incomplete; the unload remains correct, but a future reload requires structural fixes named in the manifest.

---

## Findings from script audit, April 29, 2026

These are findings that emerged during the script audit conducted as part of state_manifest.md sub-task 1 (Path A, documentation governance track). They are structural observations about the codebase that prior incident documents do not address; they are recorded here for traceability rather than as corrections to prior framing.

- **compression-researcher launchd-rule violation and context-blind production state.** Audit of `latent_compression_researcher.py` revealed two of three declared file dependencies (DIGEST_DIR at line 14, BRAIN_PATH at line 18) use relative paths in violation of the absolute-path rule established in BRAIN.md April 5. Under launchd execution, both reads return placeholder strings via guard clauses, so the agent has been generating daily research suggestions since April 4 without project-specific context. Details and reproducer in `state_manifest.md`'s compression-researcher entry.

- **BRAIN.md is a runtime input to multiple production agents.** Of five audited agent scripts, two (revenue-strategist, compression-researcher) declare a runtime dependency on `BRAIN.md` and parse specific sections (`## 1. THE THESIS`, `## 3. 90-DAY GOALS`, `## 4. WHAT WE ARE BUILDING`, `## 11. ARCHITECTURE DECISIONS`) into agent prompt context. revenue-strategist's read works under launchd; compression-researcher's is broken (see entry above). Where the read works, BRAIN.md's `[INVALIDATED 2026-04-18]` banner and the surrounding pre-reset content propagate into the agent's prompt context as runtime input. This means BRAIN.md is not solely a strategic reference document — it is a load-bearing input to the production pipeline. Implications: edits to BRAIN.md are edits to agent behavior; the `[INVALIDATED 2026-04-18]` banner surrounding pre-reset content is being read into agent prompts where the dependency works; rewriting BRAIN.md (mentioned in `state_manifest.md`'s sub-task 5 immediate tasks list) requires considering the runtime-input role, not just the human-reference role. Specific dependency citations in `state_manifest.md`'s revenue-strategist and compression-researcher entries.

---

## Findings from manual pipeline simulation, April 19, 2026

The April 19 manual pipeline simulation ran each of the 8 launchd-scheduled agents in production-wrapper sequence, catching failures that would otherwise have surfaced as staggered alerts the next morning. *The simulation was a Founder Engine override: all four engines (Systems, Divergent, Analysis × 2) had converged on Path 3 — stop, verify at 4:40 AM April 20 automated run. The override produced seven findings (three infrastructure repairs and four content failures). It is evidence-base for Founder Engine prerogative on operational tempo.*

### Infrastructure issues found and repaired April 19 night

1. **`calibration_tracker.py` had broken Python syntax.** April 18 contamination sweep prepended a markdown disclaimer to the top of the file as raw text, causing `SyntaxError: invalid character` on import. Would have silently failed at 5:30 AM April 20. — `[RESOLVED, Apr 19 night]`. Repaired via Python-comment-block replacement; verified `ast.parse` clean. Repo-wide AST scan confirmed zero other broken `.py` files.

2. **`~/.zshrc` had a poisoned `ANTHROPIC_API_KEY` export.** Line 8 read `export ANTHROPIC_API_KEY=source ~/.zprofile` — a malformed assignment that set the env var to the literal string `"source"` (6 chars). Launchd pipeline unaffected (uses Keychain via `run_with_key.sh`), but manual testing impossible until repair. — `[RESOLVED, Apr 19 night]`. Repaired to load directly from Keychain.

3. **Plaintext Kalshi API key in `~/.zshrc` line 4.** Flagged April 19, not repaired that night. — `[RESOLVED, Apr 29]`. Original Apr 19 framing was "filed for future Keychain migration." That framing was wrong: the script accesses public endpoints only and does not need authentication. Resolved Apr 29 by deletion rather than migration. Cross-reference: Section 10, Apr 19 Item 9 + Apr 29 Audit stored credentials entry.

### Content issues found and deferred April 19

These four findings represent failures in agent behavior — narrative agents producing misleading or unusable output even after the April 18 reset. Apr 19 mitigations addressed the immediate operational risk (unloading affected agents from launchd); the structural and matching-logic fixes remain open. Several entries below also illustrate a broader pattern: Apr 19's prescribed repair direction was, in three of four cases, later revised — finding-real, prescription-wrong.

- **A. Text swarm market_mapping failure.** `03_text_swarm.py`'s `load_live_markets()` queries Polymarket for 11 hardcoded benchmark questions; none matched any real Polymarket market via the search-term logic; all 11 fell back to 50.0%. All post-reset swarm predictions were logged against 50% fallback crowd baselines, making calibration tracker's skill scores meaningless. — `[OPEN, framing superseded]`. Apr 19 prescribed merging shadow_match's "battle-tested search-term map" into text_swarm. That repair direction was wrong: April 20 supplement retracted the assumption that shadow_match's search-term map worked at all (shadow_match was loading the seed file, not the live API). Current open work is contract-design-first per Apr 20's reframing. Cross-reference: Section 10, Apr 19 Item 2 + Apr 20 Item 1.

- **B. Revenue strategist template contamination.** Daily output continued to reference Rain Grant, prediction-market-research framing, "latent agents hold probability distributions" as the commercial story. Prompt template was unchanged post-reset. Mitigation: unloaded from launchd Apr 19 night (two-engine consensus — Gemini + Claude). — `[OPEN, framing superseded]`. Apr 19 prescribed prompt rewrite. That prescription was rejected on Apr 19 itself by the Structural-vs-prompt distinction (ChatGPT/Gemini): narrative agents synthesizing misleading claims is a structural protocol violation, not a prompt bug. Current open work is structural (BRAIN.md runtime-input dependency, template contamination at the structural layer). Cross-reference: Section 10, Apr 19 Item 5.

- **C. Commercialization agent actively regenerating Social Proof Loop.** The most significant finding of Apr 19 night. The agent was reading `calibration_tracker` output showing Brier 0.0173 for Full Track and BSS −2.93 vs crowd, cherry-picking the absolute Brier while ignoring the negative skill score, generating prose like "performance in adversarial liquid markets where professional forecasters...", and writing to `commercialization_thesis.md` — a file that compounded daily, with each run reading the prior day's thesis as input. This was the exact failure mode the April 18 reset was designed to prevent, regenerating itself from the prompt template. Mitigation: unloaded from launchd Apr 19 night (unanimous four-engine consensus). — `[OPEN, framing extended]`. Apr 19 framed the Social Proof Loop as a single compounding mechanism (the THESIS_FILE write-back). Apr 29 audit revealed a second compounding channel (the REVENUE_DIR `load_latest` sort logic) — the Social Proof Loop has two compounding mechanisms, not one. Both must be addressed before the agent is reloaded. Current open work is structural fix per `state_manifest.md` commercialization-agent entry. Cross-reference: Section 10, Apr 19 Item 5 + Section 4, Apr 29 correction.

- **D. Calibration metrics uninterpretable.** Pre-April 19 swarm predictions scored against fictional seed baselines. Post-April 19 predictions scored against 50% fallbacks (per Item A). Neither reading is meaningful until Item A's matching contract is defined and implemented. — `[OPEN]`. Same dependency state. Cross-reference: Section 10, Apr 19 Item 3.

---

## Findings from April 20 audit

The April 20 audit examined the code paths behind the agent behaviors flagged April 19. Where Apr 19's findings were behavior-level (agents producing wrong output despite the reset), Apr 20's findings were code-level (the specific lines and type-check failures that caused the wrong outputs). The progression is itself a finding about how contamination unfolds — behavioral symptoms surface first, then closer inspection reveals code-level mechanisms — and it sets up the cross-cutting failure mode analysis in Section 8.

A note on coverage: Finding 5 from the source supplement (the retraction of Apr 19's "Shadow Match script verified pulling real prices" claim) is captured in Section 4, "Corrections to prior incident documents," and is not repeated here.

1. **`text_swarm` price extraction bug.** `get_live_crowd_price()` read `m.get("current_price")` — a field that does not exist in the Polymarket gamma JSON. The fallback chain attempted to read `outcomePrices`, but `outcomePrices` is a JSON-encoded *string* (e.g. `'["0.749", "0.251"]'`), not a list. The `isinstance(..., list)` check failed silently. Execution fell through to a hardcoded `0.5`. Every market. Every run. The "live data" claim was true (the script loaded the live JSON); the "used live prices" claim was false. — `[RESOLVED, Apr 20 night]`. Commit `987a171`. New `_extract_price()` helper with fallback chain: `outcomePrices` (JSON-parsed if string) → `bestBid`/`bestAsk` midpoint → `lastTradePrice` → `0.5`. *Reproducer:* `python3 -c 'import json; d=json.load(open("/Users/latentforge/Projects/data/polymarket/2026-04-20.json")); m=d[0]; print(type(m.get("outcomePrices")).__name__, m.get("current_price"))'` prints `str None` — confirming the field type mismatch and the missing field that produced the silent fallback.

2. **`text_swarm` matching logic broken.** The matching loop took the first market whose question contained any word longer than 3 characters from the benchmark query. High-frequency tokens like `"2026"` and `"April"` caused every benchmark question to map to one of the first few markets in the JSON (Ethereum intraday contract, Fiorentina UEFA qualification), regardless of actual topic. The output looked structured rather than random precisely because every benchmark question collapsed onto one of two specific markets — producing a bimodal 9.5%/99.5% distribution where 9.5% = Fiorentina (market #2, contains "2026-27") and 99.5% = Ethereum intraday (market #1, contains "April 20"). — `[OPEN, deferred Apr 20 night]`. Apr 20's four-engine consensus was to defer matching-logic redesign rather than do design work while exhausted; the work is now scoped as contract-design-first per Apr 20's reframing. This finding is the source of Apr 19 Item 2's supersession: Apr 19 had prescribed merging shadow_match's "battle-tested" search-term map, but if matching can fail this badly with high-frequency token collisions, no matching code without an upfront contract would have been safe. Cross-reference: Section 10, Apr 20 Item 1 + Apr 19 Item 2.

3. **`shadow_match.py` never remediated in April 18 pass.** Line 23: `SEED_FILE = BENCHMARK_DIR / "policy_markets_seed.json"`. The Apr 18 remediation rewrote `03_text_swarm.py` to pull live Polymarket prices but left `shadow_match.py` untouched, still loading the fictional seed file. The seed file's `current_price` field had been authored by hand on March 29, which made the resulting "shadow match" output look authoritative. The mechanism behind the miss: the Apr 18 sweep's scope was narrower than the scope of the contamination — it found and rewrote the agent in the active launchd pipeline (text_swarm) but missed shadow_match because shadow_match wasn't scheduled in launchd and didn't surface during the production-pipeline review. — `[OPEN]`. Seed file quarantined to `docs/INCIDENT_ARCHIVE/policy_markets_seed_DEPRECATED_DO_NOT_LOAD.json` Apr 20 (commit `466ec98`); script attempting to load the old path now fails with `FileNotFoundError`. shadow_match rewrite to live-data source still pending. *Reproducer:* `grep SEED_FILE experiments/benchmark/shadow_match.py` returns the seed-file reference. Cross-reference: Section 10, Apr 20 Item 3 + Section 2 Archived sources entry for the quarantined seed file.

4. **`01_kalshi_selector.py` orphaned and misnamed.** Script at `experiments/benchmark/01_kalshi_selector.py` was named "kalshi selector" but actually read `policy_markets_seed.json` and wrote to `experiments/benchmark/markets_YYYY-MM-DD.md`. Had nothing to do with Kalshi. The real `kalshi-pull` launchd job ran a different script at `experiments/week1/scripts/kalshi_pull.py` which hit the Kalshi API correctly. Pedagogical takeaway: a script's name is not evidence of what it does; future audits should verify behavior, not infer from filename. This was the *second* unremediated seed-file loader caught April 20 (after shadow_match) — Apr 20 caught two seed-file loaders that the Apr 18 sweep had missed, which is the concrete form of Apr 20's "broader audit warranted" observation. — `[RESOLVED]`. Deleted (commit `452633d`); file absence verified Apr 30 morning. Cross-reference: Section 10, Apr 20 Item 5.

---

## Failure mode analysis

This section is the cross-cutting analytical record of how the April 18–20 contamination unfolded. Section 6 documented behavioral findings (agents producing wrong output despite the reset), Section 7 documented code-level mechanisms (the specific lines and type-check failures behind the wrong output). Section 8 names the patterns that span both. Its source spine is the Apr 20 supplement's "Failure mode recap" — preserved verbatim below as the keystone analytical artifact — extended with patterns that emerged from Apr 29 audit work and from reconciliation across Sections 4, 6, 7, 9, and 10. Section 8 deliberately does not introduce new named failure modes beyond Apr 20's two-mode taxonomy; new named modes belong in their canonical home documents.

### The 4-event progression

This is the fourth compounding-narrative event in 72 hours, as recorded April 20:

| # | Event | Agent | Mechanism |
|---|---|---|---|
| 1 | Apr 18 | benchmark pipeline | "45% Brier improvement" synthesized from seed data |
| 2 | Apr 19 PM | commercialization agent | Cherry-picked Brier into compounding thesis file |
| 3 | Apr 19 PM | INCIDENT_SUPPLEMENT authors | Asserted shadow_match pulling real prices without grep |
| 4 | Apr 20 AM | Grok | Generated "low-liquidity 50%" thesis without inspecting JSON |

### The common pattern

Apr 20's analysis of the four events identified a four-stage sequence: engine reads ambiguous output → generates confident narrative → forward-propagates without returning to raw data → narrative calcifies into artifact layer (report file, thesis file, incident doc). This sequence is preserved as the canonical pattern for the April 18–20 contamination episode.

### The two named failure modes

Apr 20 named two failure modes that the four events evidenced:

- **Social Proof Loop** — cross-engine amplification, where one engine's synthesis of another engine's interpretation compounds confidence without new evidence being introduced. The three-engine system (Founder / Systems / Divergent) was designed to prevent this. Events 1 and 2 are Social Proof Loop instances.
- **Intra-engine confabulation** — within-engine narrative generation that bypasses raw data, where a single engine reads ambiguous output and forward-propagates a confident interpretation without grep, file inspection, or independent recomputation. Events 3 and 4 are intra-engine confabulation instances. Apr 20's closing line: *"The three-engine system prevents cross-engine amplification (Social Proof Loop) but does not prevent intra-engine confabulation. Different defense needed."*

The defense pattern accumulation responding to intra-engine confabulation lives in Section 10's live-answer subsection ("intra-engine confabulation defense"). Patterns logged so far include the Reproducer Requirement (Apr 20), three-tier source tagging (Apr 20), Verification Output Safety (Apr 29), the Mixed-Source Synthesis Rule (Apr 29), and the Failure Escalation Protocol (Apr 29).

### Cross-cutting patterns extending the Apr 20 framing

Five patterns are named below as extensions of Apr 20's analysis. They are not new named failure modes; they are observations about how the two named modes manifest structurally and how remediation work behaves under contamination conditions.

**Pattern A — Compounding mechanisms hide in sort logic.** Apr 19 documented the commercialization-agent Social Proof Loop as one compounding channel: the THESIS_FILE write-back, where each run reads the prior day's thesis as input. The Apr 29 script audit (Section 4 correction; reproducer in `state_manifest.md`'s commercialization-agent entry: `sed -n '32,40p' experiments/week1/scripts/commercialization_agent.py`) revealed a second compounding channel that had operated invisibly the entire time: `load_latest(REVENUE_DIR)` at line 81 picks the lexicographically-greatest filename via `sorted(..., reverse=True)`. Because `commercialization_*` filenames always sort after `YYYY-MM-DD.md` in reverse-alphabetical order, this call returns commercialization-agent's own previous output whenever any commercialization output exists in the directory. The variable is named `prev_revenue` but the data is its own past output. Generalization for future audits: structural compounding mechanisms can hide inside utility functions whose names misleadingly describe a different role. Sort-logic, filename-prefix collisions, and mtime-vs-lexical ordering are the specific surfaces this case exposes; other agents may have analogous hiding surfaces not yet audited.

**Pattern B — Scope narrowness in remediation passes.** Remediation scope tracks the discovery surface, not the contamination surface. The Apr 18 sweep rewrote the agent in the active launchd pipeline (text_swarm) but missed `shadow_match.py` because `shadow_match.py` was not scheduled in launchd and did not surface during the production-pipeline review (Section 7 Finding 3). Apr 20 caught it. Apr 20's own grep was scoped narrowly to `policy_markets_seed`; the broader audit named in Apr 20 Question 1 ("Are there other agents referencing local seed files we haven't found?") never executed (Section 10 Apr 20 Item 4: "No evidence in any session log that the broader audit happened"). The April 18 sweep also missed `01_kalshi_selector.py`, found by Apr 20's grep — Apr 20 caught two seed-file loaders that Apr 18 had missed. Pattern: when a remediation pass is scoped to "the active pipeline" or "this specific search term," contamination outside that scope persists.

**Pattern C — Filename is not behavior.** Section 7 Finding 4 names this directly: *"a script's name is not evidence of what it does; future audits should verify behavior, not infer from filename."* `01_kalshi_selector.py` was named "kalshi selector" but read `policy_markets_seed.json` and had nothing to do with Kalshi; the real Kalshi puller was a different script in a different directory. The same pattern shows up at the launchd boundary: the launchd job `com.latentforge.compression-researcher` invokes a script named `latent_compression_researcher.py` (filename mismatch documented in `state_manifest.md`'s compression-researcher entry). Two independent surfaces — script name vs. behavior, and launchd job name vs. invoked script — both demonstrate that names carry no enforcement of correspondence to code or behavior. Implication for future audits: identification of components must be by content inspection (`grep`, `cat`, behavioral test), not by name.

**Pattern D — Finding-real, prescription-wrong.** Section 6's introduction names this phrase directly: *"Apr 19's prescribed repair direction was, in three of four cases, later revised — finding-real, prescription-wrong."* Three Apr 19 prescriptions were superseded within 24 hours: (i) merging shadow_match's "battle-tested" search-term map into text_swarm was prescribed Apr 19 night; Apr 20's retraction of the "shadow_match pulling real prices" claim invalidated the assumption that the map was working ground truth (Section 10 Apr 19 Item 2 supersession). (ii) Prompt rewrites for revenue_strategist and commercialization_agent were prescribed Apr 19; the Structural-vs-prompt distinction (ChatGPT/Gemini, ratified Apr 19 itself) reframed the failure as structural protocol violation, not prompt bug (Section 10 Apr 19 Item 5 supersession). (iii) The benchmark report v0.2 was framed as a rewrite salvaging from `git checkout ac430e9`; `state_manifest.md`'s benchmark-updater entry reframed it as a first-time write of post-validation report-generation logic, because the April 19 cleanup had removed the generation logic entirely (Section 10 Apr 19 Item 7 supersession).

The Apr 19 manual pipeline simulation that produced these findings was a Founder Engine override — all four engines (Systems, Divergent, Analysis × 2) had converged on Path 3 (stop, verify at 4:40 AM April 20 automated run). The override produced seven concrete findings: three infrastructure repairs (broken Python syntax in `calibration_tracker.py`, poisoned `ANTHROPIC_API_KEY` in `~/.zshrc`, plaintext Kalshi key flagged) and four content failures (text_swarm matching, revenue_strategist contamination, commercialization-agent Social Proof Loop, calibration metrics). Catching these before the 4:40 AM automated run was the operational point. The pattern is therefore not that the override was wrong or any author's judgment was poor — the findings were real and the override was sound. The pattern is the structural difficulty of prescribing fixes under contamination conditions: prescriptions drafted while still inside the contaminated state can be built on the same Tier 3 inferences the contamination came from. The discipline implication: in a contamination response, finding identification and prescription writing should be temporally separated, with prescriptions held for next-session review against fresh ground truth.

**Pattern E — Runtime-input contamination as a propagation surface.** Apr 20's "artifact calcification" stage covered static artifacts: report files, thesis files, incident docs. The Apr 29 script audit (Section 5; specific dependency citations in `state_manifest.md`'s revenue-strategist and compression-researcher entries) revealed a second propagation surface that Apr 20's framing did not address: runtime inputs to the production pipeline. revenue-strategist's `load_brain_summary()` parses BRAIN.md sections (`## 1. THE THESIS`, `## 3. 90-DAY GOALS`, `## 4. WHAT WE ARE BUILDING`) into the agent's prompt context at every scheduled run. Where the read works (revenue-strategist), BRAIN.md's `[INVALIDATED 2026-04-18]` banner and surrounding pre-reset content enter agent prompt context daily. The compression-researcher case is a related but distinct finding: the script declares the same dependency but its relative-path bug means the read returns placeholder strings, so contamination does not propagate through that channel — the agent is context-blind instead, which is its own production-state problem (Section 5 audit finding) but not a Pattern E instance. Implication: the contamination surfaces an incident response must address include not only static artifact files but also files parsed at runtime by production agents. Apr 20's "artifact layer" framing should be read as a non-exhaustive enumeration of one propagation type, with runtime inputs as a separate type that requires separate audit.

### What Section 8 does not establish

The named-mode taxonomy for the April 18–20 contamination remains at two: Social Proof Loop and intra-engine confabulation, both named by the Apr 20 supplement. Patterns A through E are extensions, not new named modes. Two close-cousin concepts are canonically named elsewhere and not imported here: the Context-Filling Machine framing in `intent.md`'s Decision Rule for Design Changes and `state_manifest.md`'s session-tainting rule; and the "silent fallback" instance from Section 7 Finding 1, which is an instance of the four-stage sequence's "ambiguous output" stage rather than a separately-named pattern. Future readers asking which framing applies should consult the home document: intra-engine confabulation in Sections 8 and 10 of this ledger; Context-Filling Machine in `intent.md` and `state_manifest.md`. Defense pattern accumulation across both framings lives in Section 10's live-answer subsection.

---

## Protocols ratified during incident response

Chronological log of protocols ratified during the April 18–20 response. Some have since been consolidated, renamed, or absorbed into broader rules in `intent.md` or `state_manifest.md`. The current set of in-force protocols lives in `state_manifest.md` ("Operational protocols in force" section) and the four-protocol reasoning list in the Session-tainting rule.

### April 18, 2026 (in INCIDENT_2026-04-18.md, Section 6)

- **Evidence tiers.** Tier 0 (intuition) / Tier 1 (observed once) / Tier 2 (reproducible internally) / Tier 3 (externally defensible). Required tag on every claim entering BRAIN.md, outreach, or strategic documents.
  - *Lifecycle:* Superseded April 20 by the three-tier source tagging (`[VERIFIED_WITH_REPRO]` / `[OUTPUT_OBSERVED]` / `[INFERRED]`) and folded into the Ground Truth Hierarchy (Tier 1 / Tier 2 / Tier 3) in `intent.md`. The April 18 four-tier framing is no longer in force; the current three-tier hierarchy is.

- **Source-type tagging.** `[LOCAL_LOG]` / `[API_VERIFIED]` / `[DERIVED]`. Required on every metric.
  - *Lifecycle:* Superseded April 20 by the reproducer requirement (every claim carries a rerunnable command, not a tag). Source-type tagging is no longer in force.

- **Three-engine anti-Social-Proof-Loop protocol.** No engine synthesizes another engine's conclusions into BRAIN.md without Founder promotion. Disputed claims trigger git history check → raw data inspection → timestamp sanity → source freshness → independent recomputation, before new synthesis. Silent Operator mode for independent feedback.
  - *Lifecycle:* Partially in force. The "no engine synthesizes another engine's conclusions" rule is preserved in the Mixed-Source Synthesis Rule in `state_manifest.md`. The Silent Operator mode is informally in force but not codified.

### April 19, 2026 (in INCIDENT_SUPPLEMENT_2026-04-19_ARCHIVED.md)

- **Manual simulation as standard practice.** After any global annotation sweep or contamination cleanup, the full launchd agent sequence must be manually simulated via production wrappers before the reset is considered closed.
  - *Lifecycle:* In force as the Manual simulation rule in `state_manifest.md` ("Operational protocols in force" section).

- **Attested summaries rule (Gemini, pending tomorrow).** Data files passed between agents must carry validity headers (e.g. `[DATA_VALIDITY: INVALIDATED_PRE_RESET]`). Downstream agents must parse these headers and may not make high-confidence narrative claims when upstream data is tagged invalid.
  - *Lifecycle:* Marked "pending tomorrow" April 19; never operationalized as a header-and-parser system. The intent — preventing high-confidence narrative claims on invalid upstream data — is preserved in the Mixed-Source Synthesis Rule and the Failure handling rule in `state_manifest.md`. The specific header format is not in force.

- **Structural vs prompt distinction (ChatGPT, ratified by Gemini).** Narrative agents synthesizing misleading claims from real data is a structural protocol violation, not a prompt bug. Fix is evidence-tier enforcement and claim validation, not prompt tweaks.
  - *Lifecycle:* In force as a framing principle, not a codified rule. Reflected in the structural-fix requirements named in `state_manifest.md`'s commercialization-agent entry (split output directory, filter by prefix, mtime-based selection — none of which are prompt fixes).

### April 20, 2026 (in INCIDENT_SUPPLEMENT_2026-04-20_ARCHIVED.md)

- **Reproducer requirement.** Every claim in an incident doc, state manifest, or strategic artifact must include a command or file-path check that a fresh agent could rerun. Claims without a reproducer are `[INFERRED]` by default, not `[VERIFIED]`.
  - *Lifecycle:* In force as the Reproducer requirement in `state_manifest.md` ("Operational protocols in force" section). Extended April 20+ to cover transformation logic, not just claim verification (per the April 20 text-swarm `_extract_price` failure).

- **Three-tier source tagging.** `[VERIFIED_WITH_REPRO]` / `[OUTPUT_OBSERVED]` / `[INFERRED]`. Treats `[OUTPUT_OBSERVED]` as distinct from `[VERIFIED]`.
  - *Lifecycle:* In force as a tagging convention in incident docs. Folded into the Ground Truth Hierarchy in `intent.md` (Tier 1 raw API data ≈ `[VERIFIED_WITH_REPRO]`, Tier 2 empirical system logs ≈ `[OUTPUT_OBSERVED]` for reproducible measurements, Tier 3 agent syntheses ≈ `[INFERRED]`).

- **Hardcoded narrative lines in output files prohibited.** Scripts may not write claims about system state into their own output files without those claims being dynamically computed and verifiable.
  - *Lifecycle:* In force as a code-review principle. Not codified as a separate rule but enforced through script audits (per April 29 audit findings in this ledger).

- **"Clean-looking wrong output" principle.** When a system is known-broken, quarantine the scheduled job rather than let it produce polished failure.
  - *Lifecycle:* In force as standard practice. Applied April 20 (text-swarm unloaded), April 19 (commercialization-agent unloaded), and ongoing — current launchd state per `state_manifest.md` reflects this principle (failed components unloaded, not allowed to produce contaminated output).

---

## Forward action items

The list below reconciles the Apr 19 and Apr 20 supplement pending-work lists against current state, marks each item resolved/open/absorbed, and preserves the existing Apr 29 Kalshi credential audit. Entries use *Reproducer:* for rerunnable commands and *Tracking:* for pointers to where ongoing work is recorded in `state_manifest.md` or `intent.md`. *Meta-observation: the Apr 19 supplement was caught between Apr 18's contamination discovery and Apr 20's deeper findings — most of its forward plans got revised within 24 hours, so multiple Apr 19 items below are marked superseded by Apr 20 reframings rather than carried forward as written.*

### Apr 29 2026 — Audit stored credentials

- **Apr 29 2026 — Audit stored credentials.** Audit all stored credentials (env files, dotfiles, Keychain) against active script dependencies. Remove orphaned secrets. Recurrence: at incident-ledger entry boundary or quarterly.
  - *Trigger: Apr 29 2026 Kalshi key near-miss revealed a plaintext key (`KALSHI_API_KEY` in `~/.zshrc` line 4) that had been doing nothing for weeks. Script accesses public endpoints only; no authentication required.*
  - *Mitigation completed Apr 29 2026:* Old key revoked on Kalshi, plaintext line removed from `~/.zshrc`, backup saved as `~/.zshrc.backup-2026-04-29`, `kalshi_pull.py` confirmed working without authentication (1,000 markets pulled successfully).

### Apr 19 2026 — Pending work reconciled

Original list from `INCIDENT_SUPPLEMENT_2026-04-19_ARCHIVED.md`, "Pending work (handoff to April 20 session)" section. Priority order preserved.

1. **Four-point check on 4:40 AM automated run** — `[ABSORBED]`. One-time verification gate for the morning of April 20. Window passed. The bugs this check was meant to catch (text_swarm extraction failure) were discovered on April 20 through other means; the protocol concern (live-data ingestion correctness) is now an ongoing operational matter, not a discrete pending action.

2. **Merge `shadow_match` search-term map into `text_swarm.load_live_markets()`** — `[OPEN, but superseded]`. Original plan assumed shadow_match's search-term map was working ground truth. April 20 supplement retracted that view (shadow_match was loading the seed file all along; its "real prices" claim was wrong). The underlying open work — text_swarm needs working matching logic — is now tracked as Apr 20 Pending Item 1 (define matching contract first), not as the merge-from-shadow_match plan written here. *Tracking:* `state_manifest.md` text-swarm component entry, `Issue: matching logic broken (bimodal fallback output); pending matching contract`.

3. **Re-evaluate calibration validity once text_swarm is producing real crowd baselines** — `[OPEN]`. Dependency on Item 2 still holds. *Tracking:* `state_manifest.md` calibration-tracker component entry, `VALID: no, Issue: scoring against contaminated or fallback baselines; pending text-swarm matching fix`.

4. **Design attested-summaries protocol (header format, validator logic, agent-prompt enforcement)** — `[ABSORBED, soft]`. Specific protocol design (validity headers + parser logic + prompt enforcement) was never built. The intent — preventing high-confidence narrative claims when upstream data is invalid — is preserved differently in the Mixed-Source Synthesis Rule and Failure handling rule in `state_manifest.md`. If a future decision determines the header-and-parser approach is needed, this re-opens as a discrete item.

5. **Rewrite revenue_strategist + commercialization_agent prompt templates under new protocol** — `[OPEN, framing shifted]`. Original Apr 19 framing called for prompt rewrites. That framing was explicitly rejected on Apr 19 itself by the Structural-vs-prompt distinction (ChatGPT/Gemini): "narrative agents synthesizing misleading claims from real data is a structural protocol violation, not a prompt bug." The actual remaining work, per `state_manifest.md` commercialization-agent entry, is structural — split commercialization output into a separate directory, modify `load_latest` to filter by filename prefix, replace reverse-alphabetical sort with mtime-based selection. revenue-strategist's open work is also structural (BRAIN.md runtime-input dependency, template contamination). A future reader looking at this entry should treat "rewrite the prompts" as the *wrong* path — structural fix is the actual path. *Tracking:* `state_manifest.md` revenue-strategist + commercialization-agent component entries.

6. **BRAIN.md narrative rewrite grounded in April 20 live data** — `[OPEN, with runtime-input nuance]`. Apr 19 framed this as a narrative/prose update. The Apr 29 incident-ledger audit findings reframed it: BRAIN.md is a runtime input to two production agents (revenue-strategist, compression-researcher) that parse specific sections (`## 1. THE THESIS`, `## 3. 90-DAY GOALS`, `## 4. WHAT WE ARE BUILDING`) into agent prompt context. So a "rewrite" is not just human-reference documentation; it edits agent behavior. *Tracking:* `state_manifest.md` (revenue-strategist + compression-researcher component entries documenting BRAIN.md runtime dependency) and `incident_ledger.md` (April 29 audit finding on BRAIN.md as runtime input).

7. **v0.2 clean rewrite salvaging technical content from PRE_RESET_DRAFT** — `[OPEN, framing shifted]`. Original framing: "rewrite" salvaging from a prior draft. State_manifest.md benchmark-updater entry reframes: the April 19 cleanup removed the report-generation logic; the script is now scaffolding-only with validation gates in front of empty implementation. The actual work is a *first-time write* of post-validation report-generation logic, not a rewrite. A future reader should not `git checkout ac430e9` looking for code to salvage as the Apr 18 doc's Section 5 plan suggested — that approach has been superseded. *Tracking:* `state_manifest.md` benchmark-updater component entry.

8. **Bearish asymmetry re-validation (Gemini's flag: may be proxy contamination)** — `[OPEN]`. *Tracking:* `intent.md`, "What is under re-audit" section: "The bearish asymmetry finding from April 17 may be proxy contamination from the synthetic seed file invalidated on April 18, not real directional physics. Flagged by Divergent Engine (Grok). Requires re-test against live data."

9. **Move Kalshi key to Keychain** — `[RESOLVED, in different shape]`. Solved by deletion rather than migration on Apr 29 2026 — the script accesses public endpoints only, no authentication required. *Reproducer:* `grep -c 'KALSHI_API_KEY' ~/.zshrc` returns 0; `~/.zshrc.backup-2026-04-29` preserves the pre-Apr-29 file with the line; `kalshi_pull.py` runs without authentication.

10. **Mac Mini bidirectional steering work — only after 1-8 stable** — `[ABSORBED → intent.md Mac Mini Autonomy Rule]`. Per `intent.md`: "Mac Mini work is Founder-initiated only. Fresh Claude sessions must NOT propose using the Mac Mini autonomously — even if the MacBook Air hits a capacity bottleneck. Claude requests Mac Mini work; Claude does not propose it." This item is no longer Claude's to track in a remediation ledger. Current state of the work itself is not evaluated here.

### Apr 20 2026 — Pending work reconciled

Original list from `INCIDENT_SUPPLEMENT_2026-04-20_ARCHIVED.md`, "Tomorrow's first tasks" section plus Question 3 from "Questions for the team." Priority order preserved.

1. **Define matching contract before writing any matching code** — `[OPEN]`. This is the supersession target for Apr 19 Item 2. Substantive nuance: the work is contract design first (what counts as a match? required keyword set? scoring with threshold? test cases that prove or disprove correctness?) and code second. The previous matching code mapped every benchmark question to "Ethereum intraday" or "Fiorentina" because it had no formal notion of correctness. *Tracking:* `state_manifest.md` text-swarm component entry: `Issue: matching logic broken (bimodal fallback output); pending matching contract`.

2. **Implement matching per contract; verify against current live JSON** — `[OPEN, dependent on Item 1]`. Original Apr 20 phrasing referenced "verify against live 2026-04-21.json" — that date anchor is stale; verification will happen against whatever live JSON exists when implementation lands. *Tracking:* same `state_manifest.md` text-swarm entry.

3. **Rewrite shadow_match.py — point at live JSON, reuse `_extract_price()`** — `[OPEN]`. *Tracking:* `state_manifest.md` shadow_match component entry: `[not in launchd | VALID: no]`, `Issue: still reads quarantined policy_markets_seed.json; pending rewrite to live-data source`.

4. **Grep repo for seed references; delete quarantined seed file if clean** — `[OPEN, two-part]`. Apr 20's narrowly-scoped grep caught only `policy_markets_seed` references. Apr 20 Question 1 explicitly flagged that a broader audit was needed: "Are there other agents referencing local seed files we haven't found?" No evidence in any session log that the broader audit happened. Part 2 (delete the quarantined seed) depends on Part 1. *Reproducer:* `ls docs/INCIDENT_ARCHIVE/policy_markets_seed_DEPRECATED_DO_NOT_LOAD.json` shows the seed JSON still present.

5. **Decide fate of `01_kalshi_selector.py`** — `[RESOLVED]`. Deleted. *Reproducer:* `git log -- experiments/benchmark/01_kalshi_selector.py` returns commit `452633d chore(benchmark): delete 01_kalshi_selector.py`; `ls experiments/benchmark/01_kalshi_selector.py` returns `No such file or directory`.

6. **Reload text-swarm into launchd only after Items 1-3 verified** — `[OPEN, blocked on Items 1, 2, 3 above]`. *Tracking:* `state_manifest.md` text-swarm component entry: `[LOADED: no | VALID: no]`.

### Live answer to Apr 20 supplement's Question 3 — intra-engine confabulation defense

Apr 20 supplement closed with three open questions for the team. Question 3 — *"The three-engine system needs an intra-engine-confabulation defense. The reproducer requirement is step one. What else?"* — has a live answer in progress: defense patterns being accumulated across April 20+ sessions. Patterns logged so far include the Reproducer Requirement (Apr 20), three-tier source tagging (Apr 20), Verification Output Safety (Apr 29), the Mixed-Source Synthesis Rule (Apr 29), and the Failure Escalation Protocol (Apr 29). These collectively address the failure mode Apr 20 named (engine reads ambiguous output → generates confident narrative → forward-propagates without returning to raw data). Consolidation into `intent.md` will happen when the pattern set stabilizes; until then, the live record lives across `intent.md`, `state_manifest.md` ("Operational protocols in force" section), and the Apr 29 audit findings in this ledger.

