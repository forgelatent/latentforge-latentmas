# LatentForge — state_manifest.md

**What must be currently true for reasoning to be safe.**

Companion to `docs/intent.md`. Where `intent.md` defines what the project is *for* (permanent), this file defines what is *currently true* (volatile — operational state + session hygiene). Fresh Claude sessions read both at the start of every session.

Last meaningful update: September 19, 2026
Maintained by: John McGuire (Founder Engine), with Systems Engine (Claude) and Divergent Thinking Engine (Grok)

---

## HEAD

**HEAD:** `d7c8d09` — fix(kalshi-pull): fail loud on empty or wrong-shaped answer; check before write. This is the last code commit; before it, `36a6fc5` (research-sweep) and `2832d02` (compression-researcher). Every other commit after `36a6fc5` is records, evidence or pattern text. The commit that carries this line is itself past the anchor; expected, not drift.
*(Use `git log -1 HEAD` for timestamp.)*

---

## Bootstrap integrity check

A fresh session is initialized via the **bootstrap bundle**: five canonical documents loaded together by the `brainload_handoff` alias.

| Role | Files |
|---|---|
| **Trinity** (3) | `docs/intent.md` (purpose) + `docs/state_manifest.md` (current state) + `docs/incident_ledger.md` (incident history) |
| **Referenced** (1) | `docs/INCIDENT_2026-04-18.md` (root incident record, preserved at original path because 20+ inline disclaimer headers across the codebase cite it) |
| **Complementary** (1) | `docs/build_log.md` (architectural and per-component design rationale) |

All five files are required. If any of the five is missing from context, declare the session UNINITIALIZED and halt. Do not reason from a partial bundle.

The "Trinity of Truth" remains the integrity-critical core — the three files that together define what the project is for, what is currently true, and what has gone wrong — but the bundle is the full session-initialization context. A session missing any single file from the bundle is incomplete and unsafe to reason from.

If only `BRAIN.md` is present, the legacy `brainload` alias was used — close the session and restart with `brainload_handoff`.

---

## Hosts

- **MacBook Air** (`Johns-MacBook-Air`) — production pipeline host. All launchd jobs, data pulls, agent outputs, git operations run here.
- **Mac Mini M4 Pro** — experimental compute (not part of production pipeline). Activation steering, latent transport, Phi-3 MPS runs.
  - **Status:** Powered on, idle. No active experiments since April 17, 2026.
  - **Autonomy rule:** Mac Mini work is Founder-initiated only. Fresh Claude sessions must NOT propose using the Mac Mini autonomously — even if the MacBook Air hits a capacity bottleneck. Claude requests Mac Mini work; Claude does not propose it.

### Paths

- **Repo root:** `~/Projects/latentforge-latentmas/`
- **Data root:** `~/Projects/data/` — Polymarket and Kalshi pulls
- **Founder inputs:** `~/Projects/latentforge-latentmas/founder_inputs/`
- **Research outputs:** `~/Projects/latentforge-latentmas/research/`
- **Logs:** co-located with each job's output directory. Repo-side jobs log to the repo (e.g., `experiments/benchmark/calibration/cron.log`). Data-pull jobs log to the data root (e.g., `~/Projects/data/polymarket/cron.log`).

---

## Session-tainting rule

This rule defends against the Context-Filling Machine (CFM) failure mode: sessions that lack required reasoning protocols and, under pressure, generate plausible-sounding but unsafe outputs by inferring missing context rather than requesting it.

**A session is tainted if it was started before the installation of the most recent required reasoning protocol.** A tainted session must be closed and restarted — factual knowledge of prior incidents is not sufficient, because informed speculation is still speculation.

**Required protocols (current):**

- Context Declaration
- Ground Truth Hierarchy
- Decision Rule for Design Changes
- Verification Output Safety

**Reference installation point:** `docs/intent.md` at the most recent CFM-defense protocol commit. When new protocols are added, the boundary moves to the most recent installation commit.

> Boundary moved on April 29 commit `ba1e814` when Verification Output Safety was added. Sessions started before that commit are tainted under the current four-protocol list.

**Discipline note:** This list governs high-governance reasoning protocols only — the constitutional protocols that prevent CFM failure. Operational practices and verification rules (see Operational protocols section) are tracked separately and do not affect session-tainting. Growing this list without a corresponding new CFM-class failure would dilute the rule. Operational protocols should likewise be consolidated when possible: any proposal to add a new operational protocol must justify why it cannot be merged into an existing one.

---

## Trust boundary for outputs

See Ground Truth Hierarchy in `docs/intent.md`. Session hygiene (the tainting rule above) is necessary but not sufficient for trust — a clean session can still produce unsafe outputs if the hierarchy isn't applied. Tier 3 agent syntheses do not override Tier 1 or Tier 2 evidence, regardless of how confident or well-written they sound.

---

## Failure handling rule

If a component is marked `VALID: no` in the System Validity section below, do not use its outputs for reasoning, and treat dependent components as invalid until the upstream component is revalidated. A "no" propagates downstream along the `depends-on:` chain.

---

## Precedence Rule

Derived from the Ground Truth Hierarchy in `docs/intent.md`, applied to canonical documents and live system state. Named as a first-class rule: future changes to it require their own review, not just appeal to the hierarchy.

**The rule:**

1. If this file contradicts `intent.md`, `intent.md` wins — it defines the rules this file operates under.
2. If this file is stale relative to live system state (git, launchd, data), live system state wins. The commit hash at the top of this file is the anchor: if HEAD has moved past it, treat this file as a snapshot, not ground truth.
3. **Strategic Drift case.** If `intent.md` directly contradicts live system state — e.g., `intent.md` says a component should be disabled but launchd shows it running — flag as **Strategic Drift** and seek Founder intervention. Do not resolve by preferring one over the other without review. This is a bug report, not a precedence decision.
4. **Conflict escalation meta-rule.** When multiple rules in the Trinity of Truth resolve in different directions for the same question, prefer drift detection over automatic resolution. Flag and escalate rather than auto-resolve.

   *One illustrative shape this takes — not the only one:* the silent-drift edge case, where the session is clean (passes the tainting rule), the System Validity section says `VALID: yes` for the relevant component, but live HEAD has moved past this file's anchor commit AND `intent.md` is stale relative to recent operational changes. Each individual rule appears to license proceeding, but the combination is a drift signal. Flag it, don't reconcile it.

---

## Operational protocols in force

These govern how work gets done and how remediation is verified. They are load-bearing but do not affect session-tainting.

- **Reproducer requirement** (ratified April 20, 2026). Every claim in an incident doc, state manifest, or strategic artifact must include a command or file-path check that a fresh agent could rerun. Claims without a reproducer are `[INFERRED]` by default, not `[VERIFIED]`. This applies to transformation logic as well as claim verification: any aggregation, filtering, weighting, or matching layer must have a reproducer that traces outputs back to raw inputs. (The April 20 text-swarm `_extract_price` failure — real Polymarket JSON, broken extraction logic, silent fallback to 0.5 — is the canonical example of why transformation layers need their own reproducers.) **Enumeration clause** (added September 19, 2026). When the claim is a complete list or a count ("these are all of them", "N files"), the reproducer must be a search over the whole file, folder or log, not a reading of the part in view. The search must be written against the thing being described, not the wording last seen. The claim must also say what the search could not have found. *Evidence: the September 14-15 loader stale strings — seven found in one window where ten existed, then five more missed by a whole-repo search for a single phrasing.*

- **Live-data primacy** (ratified April 29, 2026). Any output that can be regenerated from live polymarket-pull or kalshi-pull data must be treated as stale if older than 24 hours, unless explicitly frozen for research purposes. Regenerable outputs include: text-swarm predictions, calibration-tracker entries, shadow_match logs. Static outputs (research summaries, founder_inputs notes) are exempt.

- **Manual simulation rule** (ratified April 19, 2026). Whenever a global annotation sweep or contamination cleanup is performed, the full launchd agent sequence must be manually simulated via production wrappers before the reset is considered closed. Scheduled automation is not a substitute.

- **Failure Escalation Protocol** (ratified April 29, 2026). When any of the following are detected: session-tainting condition met, Strategic Drift identified, a required component marked `VALID: no`, or the Precedence Rule fails to resolve cleanly — Claude must halt forward reasoning, explicitly declare the failure condition, identify which rule triggered it, and request resolution or clarification. No conclusions may be drawn under unresolved failure conditions. The rule converts the manifest from "well-described" to "enforced."

- **End-of-session handoff** (practice since May 2026; codified July 11, 2026). Before session close, write `founder_inputs/YYYY-MM-DD_end_of_session_handoff.md` carrying what the Trinity does not: session patterns, CFM observations, founder context, next-session do/do-not lists. Rationale: practices not written into the bundle die at the session boundary — this practice itself silently dropped on July 11 until the Founder asked.

- **Mixed-Source Synthesis Rule** (ratified April 29, 2026). Do not synthesize across components or files of differing validity or freshness without explicit reconciliation. A `VALID: yes` output and a `VALID: no` output may not be combined into a single conclusion. A current output and a stale output may not be combined without an explicit timestamp note. This covers cross-file staleness, mixed-validity synthesis, and the Social Proof Loop class of failure (where confident narratives compound across engines without returning to raw data).

- **Registry version selection procedure** (ratified September 14, 2026). Selection rules 3a-3f (ledger, July 12, 2026) define what a valid registry *contains*; this procedure defines how a candidate is *verified* before it becomes canonical. Gates run in order, none skippable. Generalized from the v2 selection gates, which were written as a one-off for that version.
  - **Fresh pool.** Regenerate the qualifying pool before selecting; a prior pool is stale by default. Identify existing tooling by content, not filename (Pattern C). Selection runs only against the fresh pull's output.
  - **Known loader defects ship before lock.** Any outstanding defect in the consuming loader is fixed and verified (ast.parse clean, `--selfcheck` passing on the current registry, new hash recorded) before a candidate is locked — not after.
  - **Schema conformance.** Verify the candidate against the loader's input contract by reading the loader's source, not by assuming its interface. Field names and required keys are part of the contract. *Added after the v2 promotion, where the candidate was built in pool-record shape and would have hard-failed the loader on version mismatch; caught only by reading the source.*
  - **Candidate, then confirm.** Commit the selection as a CANDIDATE file. Promotion to locked requires a cold re-read in a fresh context. Only after promotion: repoint the loader, archive the predecessor with the ratified archive note.
  - **Standing prohibitions.** No market may be proposed from an engine's general knowledge — that is the seed-file shape; cite a pool line for every pick. Never promote a CANDIDATE inside the selection session. Never combine two registry versions as one series.
  - **Evidence base:** promoted on one completed run (v2, September 14, 2026), which caught six findings including a 3b violation masked by the year boundary, and missed the schema shape now covered above. One run, not a battle-tested procedure.

---

## System validity by component

*Unresolved entries are intentionally left with explicit blocking tags per Failure Escalation Protocol. These are not gaps to fill — they are signals to halt.*

Purpose: to show a fresh session the *Operational Delta* — the gap between whether a component is running and whether its output is trustworthy — so reasoning doesn't silently depend on a loaded-but-contaminated job.

**Validity legend:**
- `VALID: yes` — outputs trustworthy, use freely
- `VALID: limited` — outputs trustworthy only within stated constraints
- `VALID: no` — do not use outputs for reasoning; propagates downstream

**Active and trusted:**

- polymarket-pull `[LOADED: yes | VALID: yes]`
  - Live pulls verified April 28-29 (consistent across two consecutive days post-travel-recovery)
  - `depends-on: (none — root)`

- kalshi-pull `[LOADED: yes | VALID: yes]`
  - Live pulls verified April 28-29; silent-success bug fixed May 11 (see resolution note below)
  - `kalshi-pull` uses public endpoints only. Kalshi's authenticated endpoints (RSA-based) are not currently configured.
  - **VALID restored May 11, 2026** per incident_ledger.md "May 9, 2026 audit findings" resolution. Script-level fix shipped in `kalshi_pull.py` (added `sys.exit(1)` to the `except` handler). After fix, kalshi-pull now exits non-zero on exceptions, triggering the wrapper's 3-attempt retry, structurally parallel to polymarket-pull. Verified May 11 via happy-path (exit 0, 1000 markets saved) and failure-path (WiFi off, exit 1, NameResolutionError logged) tests. A separate follow-on observation (kalshi_pull treats empty-data API response as success) is documented in the same May 9 audit findings subsection as a deferred Tier 3 ticket; this does not affect VALID: yes designation under normal API behavior.
  - **September 19, 2026 (fourth session): empty-answer ticket closed, commit `d7c8d09`.** File hash of record `2549a452...` (69 lines; the first hash recorded for this script in this manifest; supersedes `8fc24ac8`). **Failure contract:** exit 1 = could not reach Kalshi (exception); exit 2 = Kalshi answered but the answer was unusable (unrecognised shape, or markets empty or not a list). On either, nothing is written to the output path; both checks precede the write. The wrapper retries on any non-zero exit. Verified on host by offline harness (3 of 9 before, 9 of 9 after) and one live run; a run through the launchd wrapper is not yet verified. Fourth same-session fix; cold re-read owed.
  - **The daily file is the first page only, and always has been.** The script requests `limit=1000` and does not follow the `cursor`. 124 of 124 saved files hold exactly 1,000 markets; a live probe on September 19 returned 1,000 markets with a non-empty cursor. Each file is truthful and incomplete. Since `d7c8d09` every run logs a NOTE saying so. Pagination is deliberately unchanged. **Founder decision pending, opened September 19, 2026:** what this feed is for (all pages, a relevant subset, or nothing), and whether `VALID: yes` should carry a scope. The label above has not been re-assessed against this finding. Nothing loaded reads this output (revenue-strategist is `LOADED: no`).
  - *Observation, untouched:* lines 28-29 (read in masked view only) reference an API key from the environment and a Bearer header; the key was deleted April 29 and the endpoints are public. *Reproducers:* `shasum -a 256 experiments/week1/scripts/kalshi_pull.py` returns `2549a452...`; `grep -c "sys.exit" experiments/week1/scripts/kalshi_pull.py` returns 3; `python3 experiments/week1/scripts/test_kalshi_pull.py` (from the repo root, offline) reports 9 of 9; `grep -c "first page only" ~/Projects/data/kalshi/cron.log` grows by one per run once the wrapper path is confirmed.
  - `depends-on: (none — root)`

- compression-researcher `[LOADED: yes | VALID: limited | scope: research-only, no downstream impact]`
  - **[BLOCKING: VALID label under review. Founder decision pending, opened September 19, 2026]** The `VALID: limited` label above predates the September 19 findings and has not been re-assessed. Do not read it as an assessment. Until the Founder sets a new label: (1) treat any file in `research/suggestions/` dated 2026-04-20 through 2026-09-18 as untrusted unless `grep -c "SUGGESTION"` on it returns 3; (2) treat nightly operation under the `2832d02` fix as unverified, since no scheduled run had completed under it when this tag was written; (3) all real output, past and future, is context-blind. `scope: research-only, no downstream impact` still holds: the only other reader of the folder is commercialization-agent (`LOADED: no`). The label is to be decided on several nights of evidence, not one. A session that wants to reason from this component's output checks the file first and says that this tag applies.
  - **Note on naming:** launchd job is `com.latentforge.compression-researcher`; the underlying script is `experiments/week1/scripts/latent_compression_researcher.py` (filename mismatch).
  - **File hash of record: `8d19bcc2...`** (157 lines), after the September 19, 2026 fix `2832d02`; supersedes `4a633e94`. Cold re-read the same day in a separate session: 3 of 3 PASS, no defects, six observations (see `incident_ledger.md` September 19 third-session entry).
  - **Failure contract (since `2832d02`):** any failed call exits non-zero and writes nothing to the output path. Exit 1 = call failed (no key, non-200 response, request exception). Exit 2 = the response has no `SUGGESTION` or is under 1,000 characters. The wrapper retries on any non-zero exit. A `caffeinate -i -w` wake assertion starts at the top of `main` (line 121); whether it holds through a night-time wake is unproven.
  - **Output history (Tier 1; `incident_ledger.md` September 19 entries):** real output nightly April 1-19. From 2026-04-20 the script wrote error text to its output path and reported SUCCESS: 105 error files were produced (read timeouts, DNS failures, one API 529 on 2026-05-14). **104 remain on disk**, dated 2026-04-20 through 2026-09-18; the 105th, 2026-09-19, was replaced with real output by that day's live test. 29 real files exist; the last before September 19 is 2026-06-08. Root cause is host sleep mid-request, not the API. The junk files are kept as evidence (committed `0eee1f8`) and are a reload precondition for commercialization-agent, which reads this folder. Test for a real file: `grep -c "SUGGESTION"` returns 3; a junk file returns 0.
  - **Declared dependencies (as written in script source):**
    - research-sweep (via `DIGEST_DIR` at line 21, `Path("research/daily-digest")` — relative path)
    - BRAIN.md (via `BRAIN_PATH` at line 25, `Path("BRAIN.md")` — relative path)
  - **Effective dependencies under launchd execution:** none of the declared file dependencies resolve. Lines 21 and 25 use relative paths against an unspecified working directory, and the file contains no `os.chdir()`. Both read functions (`load_latest_digest()` lines 70-74, `load_brain_summary()` lines 77-88) return placeholder strings when paths don't resolve, so under launchd the prompt receives placeholders, not the digest or BRAIN.md. **Not addressed by the September 19 fix: real output is still generated without project context.** *(Still script-level inference: no run-level check of placeholder strings in a prompt is recorded. The 77-88 end line is calculated from the patch offset, not re-read.)*
  - **`depends-on:`** none (effective — this is a bug, not a design choice). Declared dependencies on research-sweep and BRAIN.md are non-functional under launchd.
  - **Structural bug (open):** the absolute-path rule (BRAIN.md April 5) is violated at lines 21 and 25. `SUGGESTIONS_DIR` (line 22) and `OUTPUT_FILE` (line 24) use absolute paths correctly.
  - **Other stale content (open):** the system prompt still says "Mac Mini (arriving April 9-16)" (line 59). The component has no memory of its own output; on September 19 it re-suggested its April 1 first idea.
  - **Host-sleep exposure:** `WakeForJob` is not a launchd key and nothing schedules a wake (`incident_ledger.md` September 19 second-session entry). Recorded, not fixed.
  - Verified against hash `8d19bcc2...`, September 19, 2026: path constants lines 20-25, key read from environment line 27, `fail()` 64-67, `call_claude` from 92 (model line 104, `timeout=300` line 109), `main` from 119, output write line 150. *Reproducers:* `shasum -a 256 experiments/week1/scripts/latent_compression_researcher.py`; `grep -n -E '^(DIGEST_DIR|SUGGESTIONS_DIR|OUTPUT_FILE|BRAIN_PATH) *=|^def |chdir|caffeinate|open\(' experiments/week1/scripts/latent_compression_researcher.py`; `grep -L "SUGGESTION" research/suggestions/*.md | wc -l` returns 104 (as of September 19); `grep -l "SUGGESTION" research/suggestions/*.md | wc -l` returns 29 (grows nightly if the fix holds).

- research-sweep `[LOADED: yes | VALID: limited | scope: research-only, no downstream impact]`
  - `depends-on:` none. Script has zero local-filesystem read sites; inputs are external API calls only (arXiv, GitHub per BRAIN.md). Writes to `~/Projects/latentforge-latentmas/research/daily-digest/YYYY-MM-DD.md` (absolute path, OUTPUT_DIR at line 8).
  - **Not** dependent on: BRAIN.md (no read), previous research-sweep output (no self-dependency), founder_inputs/, any other launchd component.
  - **Note on absolute-path rule compliance:** Script uses absolute path for OUTPUT_DIR (line 8). Has no read paths to violate. Modified April 5, 2026 — same day the absolute-path rule was added to BRAIN.md.
  - Verified by script audit, April 29 2026: `research_sweep.py` lines 5-10 (path constants and OUTPUT_FILE construction), 160 (write site). No file-read sites in the script (verified by grep returning zero matches for read patterns).
  - **Silent-success bug found and fixed July 12, 2026** (see incident_ledger.md July 12 entry). Fetchers previously swallowed all failures and wrote template "all quiet" digests with exit 0; now total-failure exits 1 (wrapper retry engages) and partial-failure is flagged in-digest and in-log. File hash of record `dcba5e13...` (supersedes `ae81b844` from the July 12 fix). **September 19, 2026:** every failed fetch is now named in log and digest; a fully-dark arXiv or GitHub source writes the digest with a FETCH FAILED section and then exits 1 (reverses the July 12 partial-failure-exits-0 decision, Founder-approved); Andrew Ng feed removed (404); see incident_ledger.md September 19 second-session entry. Digests dated 2026-06-17, -18, -19, -23, -26 and the 2026-07-11 manual output are template output, not real sweeps — do not cite as "no activity" evidence. `VALID: limited` framing unchanged (the May 2 matching-quality audit items remain open and are the binding constraint).
  - **Correction, September 19, 2026 (fourth session): the template-digest list above is incomplete.** 17 template digests are on disk, not 6, every one exactly 1,711 bytes: 2026-04-25, -26, -27; 05-05, -06, -28, -31; 06-05, -09, -11, -16, -17, -18, -19, -23, -26; 07-11. Do not cite any of them as "no activity" evidence. Separately, the arXiv section of these digests prints the quiet-day sentence although arXiv returned nothing usable: 2026-04-13, 05-14, 05-17, 05-26, 06-03 (before the July 12 fix; cause unrecoverable) and 07-31, 09-13, 09-14, 09-15 (after it; arXiv dark, banner present). Across 130 logged runs, zero arXiv hits has never coincided with a healthy arXiv on this host. **Open gap:** a 200 answer with no entries is not counted as a failure for arXiv or GitHub (RSS only, since `36a6fc5`); confirmed at source lines 94-104, not observed in practice. The arXiv id pattern at line 97 matches `http://` ids only. **The digest's "Competitive Watch" section is static text** (identical in 2026-04-04 and 2026-09-19); `COMPETITIVE_WATCH` (line 59) is defined and never fetched. Flagged to the Founder against `intent.md`, not resolved. July 12 fix `755a79c` cold re-read the same day: 3 of 3 PASS. Detail in `incident_ledger.md` September 19 fourth-session entry. *Reproducers:* `stat -f "%z %N" research/daily-digest/2026-*.md | awk '$1==1711' | wc -l` returns 17; `grep -c "COMPETITIVE_WATCH" experiments/week1/scripts/research_sweep.py` returns 1; `diff <(sed -n '24,28p' research/daily-digest/2026-04-04.md) <(sed -n '24,28p' research/daily-digest/2026-09-19.md)` prints nothing.
- calibration-tracker `[LOADED: yes | VALID: yes]`
  - **VALID restored May 24, 2026** per Tier 1 source audit + three-engine review + five verification checks (see `incident_ledger.md` Section 4 May 24 second entry). Previous "VALID: no" framing rested on two assumptions, both disproved against source: (a) "scoring against contaminated or fallback baselines" — script pulls `crowd_prob` directly from live Polymarket Gamma API (lines 50 and 89), no `policy_markets_seed` reads; April 5 log entries from inside the contamination window show realistic near-zero crowd probabilities on NBA rookie markets, confirming live-data sourcing from script inception; fallback-to-0.5 density in the resolved Brier log is 1 of 27 entries (3.7%), not flattening aggregate scoring. (b) "Pending text-swarm matching fix" — script does not read text-swarm output or any text-swarm-derived file; the `swarm_estimate` function (lines 110-141) makes three independent Anthropic API calls per market with three distinct persona system prompts and averages results.
  - Scoring layer is structurally honest: lines 193-198 compute Brier scores against `outcome` (the actual market resolution fetched via `check_resolution()` at line 87, which calls the live Polymarket API at line 89). The script is structurally capable of failing — recent log entries (May 20 Cornyn loss, May 24 Paxton win) show the swarm defaulting to 0.5 against directionally-correct crowd on Texas Republican Primary markets, producing swarm Brier 0.25 = naive Brier 0.25 > crowd Brier 0.18 — exactly the "honest measurement showing swarm losing to crowd" shape that a non-rigged system produces. Brier Skill Score output explicitly names negative-skill-means-worse semantics (line 284).
  - Three independent engine reviews (Gemini, ChatGPT, Grok) on the v2 briefing converged: no evidence of seed-file contamination, divergence-from-anchor scoring, random-number substitution, or hardcoded narrative output. Audit is structurally sound; operational quality confirmed by five verification checks.
  - **Operational health observations (not structural concerns):** swarm-default-to-0.5 behavior on some market types is a forecasting-quality finding the script surfaces correctly via Brier scoring — separate question from structural validity. Agent API errors (12 in 2,610 log lines across 36 days) are rare and known-transient causes (401 auth, timeout, DNS); the script's structural design (`return None` on full-failure, `continue` on `None` swarm_prob) makes silent-failure-as-0.5 impossible.
  - **Reproducers (verified May 24):**
    - Live-data sourcing: `grep -n "polymarket\|policy_markets_seed" experiments/benchmark/calibration_tracker.py` returns only `gamma-api.polymarket.com` URLs at lines 50 and 89; zero matches for `policy_markets_seed`.
    - Outcome-based scoring: `grep -n -E "outcome|resolved|resolution|brier" experiments/benchmark/calibration_tracker.py` returns 47 matches including Brier formulas at lines 193-195.
    - Real AI calls: `sed -n '110,145p' experiments/benchmark/calibration_tracker.py` shows three persona prompts + three API calls to `api.anthropic.com/v1/messages`; `grep -n "random"` returns zero matches.
    - No internal dependencies: `grep -n "text_swarm\|shadow_match\|data/polymarket" experiments/benchmark/calibration_tracker.py` returns zero matches.
    - Fallback density: `grep -c '"crowd_prob": 0.5' experiments/benchmark/calibration/brier_running.json` returns 1 (of 27 entries).
    - Import surface: `head -n 35 experiments/benchmark/calibration_tracker.py` shows 5 stdlib imports, no internal modules.
    - Git history since reset: `git log --oneline --since="2026-04-18" experiments/benchmark/calibration_tracker.py` returns only `f548904` (April 19 syntax fix) and `d86f0ff` (April 18 reset snapshot) — no logic changes in 36 days.
    - Agent error frequency: `grep -c "Agent error:" experiments/benchmark/calibration/cron.log` returns 12 in a 2,610-line log.
    - Live operation: `tail -25 experiments/benchmark/calibration/brier_running.json` shows entries from May 24, 2026 (today).
  - **Open observation (not gating, separate cleanup):** the file carries an `[INVALIDATED 2026-04-18]` banner at lines 1-4 from the post-contamination blanket annotation. The audit demonstrates the banner is incorrect against source for this specific file — the script has read live Polymarket data since inception. Banner removal is a separate cleanup task, not part of this VALID: yes promotion.
  - `depends-on:` Anthropic API, Polymarket Gamma API (both via direct HTTPS calls). Does **not** depend on: text-swarm, shadow_match, polymarket-pull (the launchd job — calibration-tracker calls Polymarket directly, not via stored files), commercialization-agent, BRAIN.md.
  - Cross-reference: `incident_ledger.md` Section 4 May 24, 2026 second entry ("calibration_tracker.py audited; VALID restored").

- mode1-loader `[LOADED: yes | VALID: yes]`
  - Mode 1 market-state loader: `experiments/benchmark/04_market_state_loader.py` (launchd job `com.latentforge.mode1-loader`, 4:50 AM, wrapper `scripts/run_mode1_loader.sh` — keyless, public Gamma endpoint, deliberately not `run_with_key.sh`). **File hash of record: `32197ee0...`** (supersedes `aa8e59cd` from the September 14 input-contract session, `9cc65738` from the v2 repoint, `8ce0ca39` Gate 3 hardening, and `f487be95` from the July 11 install).
  - **Reads `benchmark_registry_v2.json` (repo root), 15 markets, locked September 14, 2026** after the Gate 4 cold re-read. Registry hash of record `c4717c68...`. Registry v1 archived the same day — see `experiments/benchmark/benchmark_registry_v1_ARCHIVE_NOTE.md` and `incident_ledger.md` September 14, 2026 entry.
  - Two-pass bulk fetch (bare -> live; `closed=true` -> closed), merged with duplicate-cid hard-fail, explicit `limit` param. Q5.1 identity check on the merged set; per-market LIVE/RETIRED classification with `cause_of_death`; tiered exits 0/1/2 (ALL_LIVE / RETIRED_PRESENT / ERROR). **Exit 1 is a success tier, not a failure** — the wrapper translates 0 and 1 both to clean exit for launchd and retries only on 2.
  - Output: `experiments/benchmark/mode1/market_state_YYYY-MM-DD.json` + atomic `market_state_current.json` symlink; ERROR runs write a sidecar and preserve the last good file. Daily output gitignored; ERROR sidecars deliberately not ignored.
  - Current data state: **15 LIVE, 0 RETIRED** (verified September 14, 2026 — first exit 0 since the June 30 v1 retirements). **Downstream consumers must still handle a shrinking live count:** two markets resolve within three weeks (Bitcoin 16d, Bolsonaro 19d), and rule 3d triggers next-version selection below 10 live, urgent below 6.
  - **Reproducers — registry state** (what the loader is wired to, independent of scheduling): `shasum -a 256 experiments/benchmark/04_market_state_loader.py` returns `32197ee0...`; `shasum -a 256 benchmark_registry_v2.json` returns `c4717c68...`; `python3 experiments/benchmark/04_market_state_loader.py --selfcheck` reports registry version v2, market count 15, 15 unique condition_ids.
  - **Reproducers — job health** (whether the scheduled wrapper is running): `launchctl list | grep mode1` shows the job; `tail -5 experiments/benchmark/mode1/cron.log` shows the most recent run line. **Note:** after a registry repoint, cron.log lags until the next 4:50 AM run — it reports the last *scheduled* run, not the current registry. A mismatch between this log and the data-state line above is expected during a handover window and is not drift.
  - **Series gaps and host-sleep exposure** (recorded September 19, 2026; Tier 1 from the loader's own `cron.log`; detail in `incident_ledger.md` September 19 third-session entry). The daily series is not continuous: no run is logged between Jul 27 08:02 and Jul 31 19:55 PDT, and none between Aug 11 04:56 and Sep 8 14:33 PDT (the same four-week window as the research components). The wrapper's 300-second retry wait does not advance while the host sleeps: observed waits of about 13.5 hours (Jul 17), 12.5 hours (Jul 22) and more than four days (Jul 27 to Jul 31); awake, the same wait took 5 minutes (Jul 15). Nothing schedules a wake. Recorded, not fixed. A host that never wakes writes no log line and no sidecar, so absence of errors is not evidence of health.
  - **Outputs are named by UTC date.** A run late in the Pacific evening is filed under the next day's date, and that day's scheduled run overwrites it. `market_state_2026-08-01.json` was written twice (Jul 31 19:55 PDT, live=2 retired=6; then the Aug 1 scheduled run, live=1 retired=7). Daily outputs are gitignored, so only the log line survives for the first. **Downstream consumers must not assume one file per local day, or a gap-free series.**
  - *Reproducers:* `grep -n -E "Retrying in|Attempt [23] of 3" experiments/benchmark/mode1/cron.log` shows each retry gap; `grep -c "market_state_2026-08-01" experiments/benchmark/mode1/cron.log` returns 2; `grep -n -E "Aug 11|Sep +8" experiments/benchmark/mode1/cron.log` shows both edges of the four-week gap on adjacent lines.
  - `depends-on:` Polymarket Gamma API (direct HTTPS), `benchmark_registry_v2.json`. Not dependent on: any other launchd component, BRAIN.md, Anthropic API.

**Active, untrusted:**

*Currently empty. Calibration-tracker promoted to "Active and trusted" on May 24, 2026 per incident_ledger.md Section 4 May 24 second entry; no other components currently in this category.*


**Unloaded, pending remediation:**

- text-swarm `[LOADED: no | VALID: no]`
  - **Issue 1 (matching layer):** Matching logic broken (bimodal fallback output); pending matching contract. Per Apr 20 Pending Item 1.
  - **Issue 2 (swarm layer, surfaced May 23, 2026):** Swarm logic replaced with random number generation (`random.uniform(35, 75)` with per-persona multipliers) in commit `6457e02` (Apr 18, 6:32 PM Pacific). The three personas (Macro Analyst, Quant Researcher, Contrarian Forecaster) are name-only — no Anthropic API calls, no model, no reasoning. The script produced 2 days of undetected fake output (April 19, 20) before going dormant; has not been executed since April 20. Real swarm logic survives in `experiments/benchmark/calibration_tracker.py` lines 110-141 (function `swarm_estimate`), but uses model `claude-sonnet-4-20250514` vs. the deleted text-swarm's `claude-sonnet-4-6` — never identical implementations.
  - **Provenance of the change (per May 23 audit):** This commit was made during the April 18 contamination response. The Founder authored the commit (per git) but does not specifically recall the swarm-replacement decision; founder recollection on May 23 indicates the work was engine-influenced ("whatever I did, I did because one of the engines told me to do that"). However, no contemporaneous record corroborates this. The swarm replacement is not mentioned in the commit message, in BRAIN.md's April 19 end-of-day manifest, in `INCIDENT_2026-04-18.md` Section 5 Remediation, nor in either April 19 or April 20 incident supplement (which describe text-swarm's matching layer failure but do not describe the swarm-logic replacement). The Tier 1 evidence is the diff itself (`6457e02`). All claims about *why* the swarm was replaced — including which engine prescribed it, what was specifically said, and whether the engine prescribed swarm removal vs. proposed a fix that the Founder executed as removal — are Tier 3 inference from Founder memory, not corroborated by any contemporaneous documentation. See `incident_ledger.md` May 23, 2026 entry for full pattern analysis and provenance audit.
  - **Reproducers:**
    - Swarm stub: `grep -n "random.uniform" experiments/benchmark/03_text_swarm.py` returns line 99
    - Commit history: `git log -p -S "random.uniform" -- experiments/benchmark/03_text_swarm.py` shows commit `6457e02` as the introduction point
    - Output file dates: `ls -la experiments/benchmark/text_swarm_*.md | awk '{print $9}'` shows March 30 through April 20 only; no executions since April 20
    - Surviving swarm: `grep -n "anthropic\|claude\|swarm_estimate" experiments/benchmark/calibration_tracker.py` returns hits at lines 110, 122, 128, 133, 232
  - **Cross-reference:** `incident_ledger.md` May 23, 2026 entry for full Tier 1 chain and pattern analysis.
  - **Restoration prerequisites (expanded from Apr 20 Pending Item 1):**
    1. Matching contract design (original Apr 20 scope)
    2. Swarm restoration architecture (new, May 23 scope) — decision between parallel implementation vs. shared module with calibration_tracker
    3. Audit-trail design — what gets logged per swarm run (model identifier, individual agent responses, system prompts version)
  - `depends-on: polymarket-pull`

- benchmark-updater `[LOADED: no | VALID: no]`
  - **Issue:** Script is in scaffolding-only state. Validation gates were installed on April 19 (`validate_polymarket_data()` lines 7-37, `validate_claims()` lines 40-65), but the generation logic that previously produced v0.1 of the benchmark report has been removed. The `__main__` block (lines 67-78) prints `"(Full original logic restored from git commit ac430e9)"` as a literal string but does not perform the restoration. A placeholder `sample_report = "# Benchmark Report v0.2\nSome analysis here."` runs through the validation layer for end-to-end testing of the gates. The script cannot currently produce a benchmark report.
  - `depends-on:` polymarket-pull (via `Path.home() / "Projects/data/polymarket"` at line 9, read for validation gate only). No other reads. No writes.
  - **Not** dependent on: calibration-tracker (despite prior assumption — script does not read calibration data; the report-generation code that would have read it has been removed), shadow_match (does not read), BRAIN.md, founder_inputs/.
  - **Reframe:** The unload from launchd is correct. The path forward is not a "v0.2 rewrite" of an existing component — it is a first-time write of post-validation report-generation logic. The April 18 cleanup put validation in front of the door; the April 19 cleanup left the room behind the door empty. INCIDENT_2026-04-18.md's "Restore full generation logic from git commit ac430e9, merged with validation gate" describes work that was *planned* but never executed; the script itself acknowledges this in the line 76 print statement.
  - **Launchd-rule compliance:** Single read path uses `Path.home() / ...` (absolute). Compliant. No violation.
  - Verified by script audit, April 29 2026: full file (88 lines), specifically lines 7-37 (validate_polymarket_data with single read at line 9), 40-65 (validate_claims, no reads), 67-78 (__main__ block showing scaffolding-only state).

- revenue-strategist `[LOADED: no | VALID: no]`
  - Issue: pre-reset template contamination, plus runtime BRAIN.md dependency that loads pre-reset content into prompt context (see depends-on).
  - `depends-on:`
    - kalshi-pull (via KALSHI_DIR — `load_latest_file(KALSHI_DIR)` at line 75, default `.json` extension, mtime-based selection)
    - research-sweep (via DIGEST_DIR — `load_latest_file(DIGEST_DIR, ".md")` at line 76, mtime-based selection)
    - BRAIN.md (via BRAIN_PATH — `load_brain_summary()` at line 77 reads sections marked `## 1. THE THESIS`, `## 3. 90-DAY GOALS`, `## 4. WHAT WE ARE BUILDING`. **Note:** BRAIN.md currently bears an `[INVALIDATED 2026-04-18]` banner; agent prompt context inherits this contamination.)
    - founder_inputs/ (manual, not a launchd component — propagation rules differ; line 80 defines `FOUNDER_INPUTS_DIR`, line 84 reads files within)
  - **Not** dependent on: compression-researcher (despite prior assumption — script does not read SUGGESTIONS_DIR), previous revenue-strategist output (no self-dependency).
  - **Sort logic note:** `load_latest_file` (lines 23-31) uses mtime-based sort (`key=lambda x: x.stat().st_mtime, reverse=True`). Unlike commercialization-agent's filename-based sort, this produces no latent self-dependency even when called against a directory with mixed writers.
  - Verified by script audit, April 29 2026: `revenue_strategist.py` lines 12-18 (path constants), 23-31 (load_latest_file with sort logic), 33-40 (load_brain_summary), 75-77 (call sites), 80-84 (founder_inputs read).

- commercialization-agent `[LOADED: no | VALID: no]`
  - Issue: Social Proof Loop compounding from cherry-picked metrics
  - `depends-on:`
    - research-sweep (via DIGEST_DIR)
    - compression-researcher (via SUGGESTIONS_DIR)
    - calibration-tracker (via CALIBRATION_DIR)
    - commercialization-agent itself (via THESIS_FILE — explicit self-dependency, append-on-write at line 172, read-at-startup at line 44)
    - commercialization-agent itself (via REVENUE_DIR — **active** self-dependency: `load_latest(REVENUE_DIR)` at line 81 picks the lexicographically-greatest filename via `sorted(..., reverse=True)`. Because `commercialization_*` filenames always sort after `YYYY-MM-DD.md` in reverse-alphabetical order, this call returns commercialization-agent's own previous output whenever any commercialization file exists in the directory. The variable is named `prev_revenue` but the data is its own past output.)
    - founder_inputs/ (manual, not a launchd component — propagation rules differ)
    - revenue-strategist (via REVENUE_DIR — **dormant**: revenue-strategist outputs are present in the same directory but are not surfaced by `load_latest` while any commercialization output exists. revenue-strategist becomes the actual upstream only if commercialization-agent has not yet written to REVENUE_DIR.)
  - **Structural note:** The two self-dependencies (THESIS_FILE explicit, REVENUE_DIR active) are both mechanisms of the Social Proof Loop. Both must be addressed before this component is reloaded. Suggested fixes (out of tonight's scope): (a) split commercialization output into a separate directory; (b) modify `load_latest` to filter by filename prefix; (c) replace reverse-alphabetical sort with mtime-based selection. All three fixes (a, b, c) target the REVENUE_DIR channel; none addresses the THESIS_FILE channel, where `commercialization_thesis.md` is appended to nightly at line 172 and read at startup at line 43. The THESIS_FILE channel requires a separate structural decision (stop reading the thesis, truncate it nightly, version it per run, or rebuild it from clean inputs each night) not yet specified. Source: build_log.md Section 2.4.2.
  - Verified by script audit, April 29 2026: `commercialization_agent.py` lines 22-29 (path constants), 32-40 (load_latest including sort logic), 42-65 (other load functions), 79-84 (call sites), 172 (write site). Reproducer: `sed -n '32,40p' experiments/week1/scripts/commercialization_agent.py` shows the sort logic.

**Manual-only, pending remediation:**

- shadow_match `[not in launchd | VALID: no]`
  - Issue: structural invalidity across four layers (data, scoring, cost, narrative) per May 24 audit — see `incident_ledger.md` Section 4 May 24, 2026 entry ("shadow_match.py audited; Pro-Thesis Optimization Loop candidate pattern"). Reload requires four prerequisites: (1) live-data rewrite (replace seed-file load with polymarket-pull read); (2) scoring layer rewritten against resolved-outcome data rather than `abs()` distance from anchor; (3) cost-comparison layer rewritten to use measured tokens rather than hardcoded `0.003` constants; (4) hardcoded `grant_line` output (lines 226, 229, 232 + docstring lines 4, 9 self-documenting "Strengthens the Rain grant narrative") removed entirely. Addressing only prerequisite (1) would leave the Pro-Thesis Optimization Loop intact.
  - `depends-on: (currently) policy_markets_seed.json (quarantined); (post-rewrite) polymarket-pull`

**Experimental hosts (not in production pipeline):**

- Mac Mini M4 Pro `[LOADED: n/a | VALID: n/a | role: experimental compute only]`
  - Used for activation steering, latent transport, Phi-3 MPS runs
  - **Status:** Powered on, idle. No active experiments since April 17, 2026.
  - **Autonomy rule:** Mac Mini work is Founder-initiated only. Fresh Claude sessions must NOT propose using the Mac Mini autonomously — even if the MacBook Air hits a capacity bottleneck. Claude requests Mac Mini work; Claude does not propose it.

---

## Measurable proof target status

Per `intent.md` "Measurable proof targets" section. This section tracks current measurement status — what is measured, what is not measured, what blocks measurement. Update cadence: when measurement infrastructure is built, when measurements are taken, or when target operativeness is reviewed. Not a daily-updated section.

**Status legend:**
- `MEASURED: yes` — measurement taken against operative infrastructure, result recorded
- `MEASURED: in-progress` — infrastructure built, measurement underway, result not yet final
- `MEASURED: no` — infrastructure not yet built or measurement not yet attempted

### OpenSpiel divergence target

- **Threshold:** latent agents >1.5× more divergent than text baseline on OpenSpiel.
- **Status: `MEASURED: no`.**
- **Required infrastructure:** OpenSpiel benchmark setup; latent-vs-text agent comparison harness; reproducible divergence-score measurement methodology.
- **Blocked by:** infrastructure not built. Mac Mini experimental work paused since April 17, 2026. Mac Mini work is Founder-initiated only per Hosts section above.
- **Not blocked by:** the post-April-19 contamination remediation (this target is independent of the Polymarket benchmark layer).

### V0.1 proof target

- **Threshold:** compute savings ≥30% per turn AND a novel-solutions count distinguishable from text-only communication, on the V0.1 demo (two agents communicating via latent deltas with Shadow Self translation, drift detection, and logging).
- **Status: `MEASURED: no`.**
- **Required infrastructure:** V0.1 demo not yet built. The April 17 work on Mac Mini M4 Pro produced verified components (latent transport, activation steering, unidirectional semantic steering on a single market) but did not constitute the V0.1 demo.
- **Blocked by:** V0.1 demo not yet built. Mac Mini work required. Mac Mini Autonomy Rule applies.
- **Sub-target progress:**
  - Compute-savings half: not yet measured. Compression fidelity work (24x compression with fidelity 1.0000 on Phi-3 Mini 3.8B) is foundational but not the same measurement.
  - Novel-solutions half: not yet measured. The four-arm benchmark architecture on prediction markets is the parallel measurement instrument for "useful divergence" but is currently blocked by text-swarm matching contract (per text-swarm component entry above).

---

## How to use this file

This file is not a source of truth — it is a consistency checker between `intent.md` and live system state.

Read sections top to bottom. When rules appear to disagree, consult the Precedence Rule. When the Precedence Rule does not produce a clean answer, the conflict escalation meta-rule applies: flag and escalate, don't auto-resolve.
