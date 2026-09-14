# Registry input contract — what 04_market_state_loader.py requires

Verified September 14, 2026 against loader source and `benchmark_registry_v2.json`.
Exists so the schema-conformance gate is checkable without re-deriving the contract
from source each time. Supersedes "read the loader's source" as the gate's method —
but re-verify against the loader when the loader changes.

**The registry is two documents in one file.** The loader reads a small part of it.
The rest is the selection audit trail, enforced by the gates and the Founder, never
by code. A registry that satisfies only the loader half will load cleanly and have
shed its entire provenance record. Both halves are listed below for that reason.

## Loader-required — hard fail (RegistryError), loader refuses to run

- `version` — exact string match against EXPECTED_REGISTRY_VERSION (line 44). [loader:128]
- `markets` — must be a list. [loader:137]
- `markets` length — exactly 15. [loader:139]
- `condition_id` per market — non-empty string. [loader:145-152]
- `condition_id` uniqueness — no duplicates across the 15. [loader:154-159]

Caution: the count and duplicate error *messages* still say "8 markets" and the
version error says "built for the v1 registry only". The enforced logic is 15/v2;
the strings are stale from v1. Trust the code, not the message.

## Loader pass-through — read with .get(), default None, never validated

`slug`, `registry_index`, `question`, `selection_snapshot`. [loader:487-513, 589-595, 606-614]
Copied into output. A registry missing them loads fine and emits nulls.

- `selection_snapshot` is a flat dict: `date`, `liquidity_usd`, `volume_usd`, `yes_price`.
  Passed through whole; the loader never inspects inside it. `volume_usd` is where
  decision D2 (volume recorded alongside liquidity) lives.
- `registry_index` doubles as the output sort key, None-last guarded. [loader:653-654]
- Unverified: three output record shapes are built (487, 589, 606). Two carry
  `condition_id`; the 487 block does not. Read those functions before relying on
  identity being present in every output record.

## Governance-only — present in v2, never read by the loader

Inventory only. Field meanings NOT verified in this session — see the v2 selection
record (`founder_inputs/2026-07-12_v2_selection_session_handoff.md`,
`founder_inputs/2026-09-14_gate4_findings.md`) before relying on any of them.

Per market: `days_to_resolution_at_selection`, `end_date`, `engine_support`,
`liquidity_exception`, `pool_tags`, `settlement_month`, `synthesis_domain`.

Top level: `accepted_tradeoffs`, `created`, `declared_correlations`,
`domain_mix_target`, `exceptions_summary`, `liquidity_floor_usd`,
`live_verification_2026-09-14`, `reopen_triggers`, `rule_3b_note`,
`selection_rules`, `source_pool`, `status`, `synthesis_doc`, `synthesis_doc_sha256`.

Two notes that are verified:
- `settlement_month` is where decision D1 (3b read semantically) is recorded. The
  loader never cross-checks it against `end_date`, so a market with a misleading
  `end_date` stays invisible to the loader by design.
- `live_verification_2026-09-14` carries a date in its key name. v3 will name it
  differently; nothing should read that key by literal name.

## Reproducers

- Enforced checks: `sed -n '117,160p' experiments/benchmark/04_market_state_loader.py`
- Every registry field the loader reads: `grep -n "registry_record.get" experiments/benchmark/04_market_state_loader.py`
- Actual v2 field inventory: `python3 -c "import json; r=json.load(open('benchmark_registry_v2.json')); print(sorted(r.keys())); print(sorted(r['markets'][0].keys()))"`
