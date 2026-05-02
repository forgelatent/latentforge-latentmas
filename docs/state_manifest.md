# LatentForge — state_manifest.md

**What must be currently true for reasoning to be safe.**

Companion to `docs/intent.md`. Where `intent.md` defines what the project is *for* (permanent), this file defines what is *currently true* (volatile — operational state + session hygiene). Fresh Claude sessions read both at the start of every session.

Last meaningful update: April 29, 2026
Maintained by: John McGuire (Founder Engine), with Systems Engine (Claude) and Divergent Thinking Engine (Grok)

---

## HEAD

**HEAD:** `41e5429` — founder_inputs: end-of-day handoff note for April 22 restart
*(Use `git log -1 HEAD` for timestamp.)*

---

## Handoff integrity check

This file is one leg of the Trinity of Truth bootstrap: `docs/intent.md` + `docs/state_manifest.md` + `docs/incident_ledger.md`. A fresh session must confirm all three files are loaded before trusting any section below.

If any of the three is missing from context, declare the session UNINITIALIZED and halt. Do not reason from a partial Trinity.

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

- **Reproducer requirement** (ratified April 20, 2026). Every claim in an incident doc, state manifest, or strategic artifact must include a command or file-path check that a fresh agent could rerun. Claims without a reproducer are `[INFERRED]` by default, not `[VERIFIED]`. This applies to transformation logic as well as claim verification: any aggregation, filtering, weighting, or matching layer must have a reproducer that traces outputs back to raw inputs. (The April 20 text-swarm `_extract_price` failure — real Polymarket JSON, broken extraction logic, silent fallback to 0.5 — is the canonical example of why transformation layers need their own reproducers.)

- **Live-data primacy** (ratified April 29, 2026). Any output that can be regenerated from live polymarket-pull or kalshi-pull data must be treated as stale if older than 24 hours, unless explicitly frozen for research purposes. Regenerable outputs include: text-swarm predictions, calibration-tracker entries, shadow_match logs. Static outputs (research summaries, founder_inputs notes) are exempt.

- **Manual simulation rule** (ratified April 19, 2026). Whenever a global annotation sweep or contamination cleanup is performed, the full launchd agent sequence must be manually simulated via production wrappers before the reset is considered closed. Scheduled automation is not a substitute.

- **Failure Escalation Protocol** (ratified April 29, 2026). When any of the following are detected: session-tainting condition met, Strategic Drift identified, a required component marked `VALID: no`, or the Precedence Rule fails to resolve cleanly — Claude must halt forward reasoning, explicitly declare the failure condition, identify which rule triggered it, and request resolution or clarification. No conclusions may be drawn under unresolved failure conditions. The rule converts the manifest from "well-described" to "enforced."

- **Mixed-Source Synthesis Rule** (ratified April 29, 2026). Do not synthesize across components or files of differing validity or freshness without explicit reconciliation. A `VALID: yes` output and a `VALID: no` output may not be combined into a single conclusion. A current output and a stale output may not be combined without an explicit timestamp note. This covers cross-file staleness, mixed-validity synthesis, and the Social Proof Loop class of failure (where confident narratives compound across engines without returning to raw data).

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
  - Live pulls verified April 28-29
  - `kalshi-pull` uses public endpoints only. Kalshi's authenticated endpoints (RSA-based) are not currently configured.
  - `depends-on: (none — root)`

- compression-researcher `[LOADED: yes | VALID: limited | scope: research-only, no downstream impact]`
  - **Note on naming:** launchd job is `com.latentforge.compression-researcher`; the underlying script is `experiments/week1/scripts/latent_compression_researcher.py` (filename mismatch).
  - **Declared dependencies (as written in script source):**
    - research-sweep (via `DIGEST_DIR` at line 14, `Path("research/daily-digest")` — relative path)
    - BRAIN.md (via `BRAIN_PATH` at line 18, `Path("BRAIN.md")` — relative path)
  - **Effective dependencies under launchd execution:** none of the declared file dependencies actually resolve. Lines 14 and 18 use relative paths against an unspecified working directory. The script has no `os.chdir()` to compensate. Both read functions (`load_latest_digest()` lines 57-61, `load_brain_summary()` lines 64-75) include guard clauses returning placeholder strings (`"No digest available."`, `"BRAIN.md not found."`) when paths don't resolve. So under launchd execution the agent's prompt context receives placeholder strings, not actual digest or BRAIN.md content. Production output since April 4 has been generated without the project-specific context the script appears to provide. *(This claim is script-level inference, not run-level verification. Run-level verification — grep cron.log for placeholder strings, grep recent outputs for context-blindness signs — is queued as a future audit item.)*
  - **`depends-on:`** none (effective — this is a bug, not a design choice). Declared dependencies on research-sweep and BRAIN.md are non-functional under launchd.
  - **Structural bug (out of tonight's scope):** Per BRAIN.md April 5 entry, "every script called by launchd must use absolute paths." This script violates that rule at lines 14 and 18. SUGGESTIONS_DIR (line 15) and OUTPUT_FILE (line 17) use absolute paths correctly; DIGEST_DIR and BRAIN_PATH do not.
  - Verified by script audit, April 29 2026: `latent_compression_researcher.py` lines 11-22 (path constants and API key), 57-61 (load_latest_digest with guard), 64-75 (load_brain_summary with guard), 127 (output write).

- research-sweep `[LOADED: yes | VALID: limited | scope: research-only, no downstream impact]`
  - `depends-on:` none. Script has zero local-filesystem read sites; inputs are external API calls only (arXiv, GitHub per BRAIN.md). Writes to `~/Projects/latentforge-latentmas/research/daily-digest/YYYY-MM-DD.md` (absolute path, OUTPUT_DIR at line 8).
  - **Not** dependent on: BRAIN.md (no read), previous research-sweep output (no self-dependency), founder_inputs/, any other launchd component.
  - **Note on absolute-path rule compliance:** Script uses absolute path for OUTPUT_DIR (line 8). Has no read paths to violate. Modified April 5, 2026 — same day the absolute-path rule was added to BRAIN.md.
  - Verified by script audit, April 29 2026: `research_sweep.py` lines 5-10 (path constants and OUTPUT_FILE construction), 160 (write site). No file-read sites in the script (verified by grep returning zero matches for read patterns).

**Active, untrusted:**

- calibration-tracker `[LOADED: yes | VALID: no]`
  - Issue: scoring against contaminated or fallback baselines; pending text-swarm matching fix
  - Per Failure handling rule: do not use outputs for reasoning. VALID: no propagates downstream along the depends-on chain. No components currently depend on calibration-tracker, so propagation is a no-op tonight.
  - `depends-on: text-swarm, polymarket-pull`

**Unloaded, pending remediation:**

- text-swarm `[LOADED: no | VALID: no]`
  - Issue: matching logic broken (bimodal fallback output); pending matching contract
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
  - **Structural note:** The two self-dependencies (THESIS_FILE explicit, REVENUE_DIR active) are both mechanisms of the Social Proof Loop. Both must be addressed before this component is reloaded. Suggested fixes (out of tonight's scope): (a) split commercialization output into a separate directory; (b) modify `load_latest` to filter by filename prefix; (c) replace reverse-alphabetical sort with mtime-based selection.
  - Verified by script audit, April 29 2026: `commercialization_agent.py` lines 22-29 (path constants), 32-40 (load_latest including sort logic), 42-65 (other load functions), 79-84 (call sites), 172 (write site). Reproducer: `sed -n '32,40p' experiments/week1/scripts/commercialization_agent.py` shows the sort logic.

**Manual-only, pending remediation:**

- shadow_match `[not in launchd | VALID: no]`
  - Issue: still reads quarantined `policy_markets_seed.json`; pending rewrite to live-data source
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
