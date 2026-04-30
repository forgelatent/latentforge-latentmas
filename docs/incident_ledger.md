# LatentForge — incident_ledger.md

**Accumulated remediation history. Read at session start as third leg of Trinity of Truth.**

This file consolidates the canonical incident record. Full historical incident documents (preserved unchanged) live in:

- `docs/INCIDENT_2026-04-18.md`
- `docs/INCIDENT_SUPPLEMENT_2026-04-19.md`
- `docs/INCIDENT_SUPPLEMENT_2026-04-20.md`

**This file is a stub.** Full mechanical consolidation pending sub-task 3 of Path A (April 29 documentation governance track). Until then, fresh Claude sessions should read this file PLUS the three incident documents linked above.

---

## Corrections to prior incident documents

- **April 29, 2026 — INCIDENT_SUPPLEMENT_2026-04-19 framing incomplete (commercialization-agent Social Proof Loop).** Audit of `commercialization_agent.py` during `state_manifest.md` drafting revealed the Social Proof Loop has two compounding channels, not one as documented in INCIDENT_SUPPLEMENT_2026-04-19. The REVENUE_DIR channel (`load_latest` sort logic) is described in `state_manifest.md`'s commercialization-agent entry. The supplement's framing of the failure mechanism is incomplete; the unload remains correct, but a future reload requires structural fixes named in the manifest.

---

## Findings from script audit, April 29, 2026

These are findings that emerged during the script audit conducted as part of state_manifest.md sub-task 1 (Path A, documentation governance track). They are structural observations about the codebase that prior incident documents do not address; they are recorded here for traceability rather than as corrections to prior framing.

- **compression-researcher launchd-rule violation and context-blind production state.** Audit of `latent_compression_researcher.py` revealed two of three declared file dependencies (DIGEST_DIR at line 14, BRAIN_PATH at line 18) use relative paths in violation of the absolute-path rule established in BRAIN.md April 5. Under launchd execution, both reads return placeholder strings via guard clauses, so the agent has been generating daily research suggestions since April 4 without project-specific context. Details and reproducer in `state_manifest.md`'s compression-researcher entry.

- **BRAIN.md is a runtime input to multiple production agents.** Of five audited agent scripts, two (revenue-strategist, compression-researcher) declare a runtime dependency on `BRAIN.md` and parse specific sections (`## 1. THE THESIS`, `## 3. 90-DAY GOALS`, `## 4. WHAT WE ARE BUILDING`, `## 11. ARCHITECTURE DECISIONS`) into agent prompt context. revenue-strategist's read works under launchd; compression-researcher's is broken (see entry above). Where the read works, BRAIN.md's `[INVALIDATED 2026-04-18]` banner and the surrounding pre-reset content propagate into the agent's prompt context as runtime input. This means BRAIN.md is not solely a strategic reference document — it is a load-bearing input to the production pipeline. Implications: edits to BRAIN.md are edits to agent behavior; the `[INVALIDATED 2026-04-18]` banner surrounding pre-reset content is being read into agent prompts where the dependency works; rewriting BRAIN.md (mentioned in `state_manifest.md`'s sub-task 5 immediate tasks list) requires considering the runtime-input role, not just the human-reference role. Specific dependency citations in `state_manifest.md`'s revenue-strategist and compression-researcher entries.

---

## Forward action items

- **Apr 29 2026 — Audit stored credentials.** Audit all stored credentials (env files, dotfiles, Keychain) against active script dependencies. Remove orphaned secrets. Recurrence: at incident-ledger entry boundary or quarterly.
  - *Trigger: Apr 29 2026 Kalshi key near-miss revealed a plaintext key (`KALSHI_API_KEY` in `~/.zshrc` line 4) that had been doing nothing for weeks. Script accesses public endpoints only; no authentication required.*
  - *Mitigation completed Apr 29 2026:* Old key revoked on Kalshi, plaintext line removed from `~/.zshrc`, backup saved as `~/.zshrc.backup-2026-04-29`, `kalshi_pull.py` confirmed working without authentication (1,000 markets pulled successfully).

---

*Stub maintained pending sub-task 3 consolidation.*
