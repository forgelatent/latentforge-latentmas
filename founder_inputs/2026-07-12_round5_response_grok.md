Recommendation: (b) Trigger v2 now.
Reasoning grounded in the briefing

Core purpose (Section 1): Mode 1 exists as a longitudinal measuring stick on a fixed, stable question set. Stability within a version is the load-bearing property. A 3-market registry is not invalid in a strict logical sense (it is still fixed and snapshot-able), but it is a severely degraded instrument for the intended purpose. With only 3 LIVE markets (Section 4), statistical power, category coverage, and robustness to individual market noise are materially reduced. This is not speculation; it follows directly from "longitudinal measuring stick" + "stable question set" + the original selection of 8 markets from a 298-pool (Section 2).
Current state evidence (Section 4): 3 LIVE / 5 RETIRED. The 5 retirements were all genuine closed resolutions around June 30. The survivors are China GDP (short runway), GPT-6, and Fed Dec (longer). The loader correctly detected RETIRED_PRESENT and exited 1.
Operational facts (Section 5): Zero meaningful longitudinal data has accumulated (first unattended run is tonight; loader installed July 11). No downstream Mode 1 consumers exist yet. Switching costs nothing in terms of lost history. The loader is already designed to handle shrinking counts and will keep signaling exit 1 daily until addressed. Continuing on 3 markets would produce a thin, noisy time-series that future consumers would inherit, violating the spirit of a robust benchmark registry.
Tier 3 hypothesis test (Section 6): The date-clustering read is well-supported by the evidence (four of five retired markets had explicit June 30 deadlines in their question text). This was predictable and should inform v2 rules. The runway read is also supported for the current survivors.

Option (a) would accept a weakened instrument for months with no upside (no consumers to protect, no sunk data). Option (c) hybrid is tempting for "data is cheap" but introduces unnecessary complexity and dual registries during transition, when the point is a single stable measuring stick. (b) is cleanest: retire v1 cleanly, regenerate a fresh qualifying pool (May 26 data is stale per Section 5), and lock v2 under disciplined rules. Nothing in the locked decisions (Section 3) prevents this.
Round 3 selection rules — what carries over vs. what should change
Carry over (with citations):

The overall process: qualifying pool from full Polymarket diagnostics → selection tooling in scratch/ → final lock into benchmark_registry_v1.json style commit. This produced a valid v1 (Section 2) and should be repeated for v2. The loader contract and two-pass fetch (Section 3, commit references) already handle provenance well.
Liquidity floor concept: $10K floor with limited soft exceptions was sensible risk management. Retain a high-liquidity bias to reduce manipulation/noise risk.
Immutable Variant A within a version (Section 1 and 3).

Should change (driven by evidence):

Market count: Increase target from 8. Evidence of rapid 5/8 die-off (Section 4) + thin remaining set shows 8 was marginal. Aim higher (e.g., 15–20) while staying within loader constraints (Section 5 notes need for explicit limit on bulk URL for larger sets). This directly strengthens the "measuring stick" (Section 1).
Deadline diversity: Critical new rule. Section 6 clustering observation + Section 4 evidence (four June 30 expirations) proves mixed hard-dated / open-dated questions caused predictable clumping. v2 selection must enforce spread (e.g., caps on near-term resolutions, minimum % open-ended or 6+ month horizons). This is the clearest lesson from v1's early retirement wave.
Category mix: Explicitly require broader coverage (politics, macro, tech/AI, geopolitics, etc.) in selection criteria. Original 8 had some mix (evident in the names), but the die-off exposed gaps. Tie this to the longitudinal goal (Section 1).
Pool refresh: Mandate regeneration of the qualifying pool close to v2 lock time (Section 5 notes May 26 pool is stale).
Soft exceptions: Tighten or document more rigorously; China GDP (~$4K) and SCOTUS (~$5K) were allowed but highlight liquidity risk.

These changes remain fully compatible with locked architecture (Section 3) and do not redesign Mode 1. They are driven by the retirement pattern (Section 4), operational timeline (Section 5), and interpretive clustering (Section 6, verified by raw dates).
No speculation on specific new markets, loader code changes beyond the noted limit, or other components. This is cold per the rules.