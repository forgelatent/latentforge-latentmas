> not-a-directive: this file preserves scoping work from the May 1, 2026 session for sub-task 2 (CFM-defense patterns consolidation into intent.md). It is reference material for tomorrow's drafting session, not an instruction to execute. Architecture decisions and per-pattern scoping below were locked through the May 1 session under strict per-item discipline.

# Sub-task 2 scoping — CFM-defense patterns consolidation into intent.md

**Author:** John McGuire (Founder Engine), with Claude (Systems Engine)
**Session date:** May 1, 2026
**Status:** Architecture locked. Per-pattern scoping complete for all 8 patterns. Drafting deferred (or partially completed — see end of file for drafting status at session close).
**Predecessor work:** Section 8 of incident_ledger.md, committed earlier in same session as `40acffa`.

---

## What sub-task 2 is

Consolidate the CFM-defense patterns currently distributed across three locations into a permanent canonical home in intent.md. Per the existing framing in incident_ledger.md Section 10's live-answer subsection: *"Consolidation into intent.md will happen when the pattern set stabilizes; until then, the live record lives across [these three places]."* Sub-task 2 is the consolidation step.

The patterns currently live in:
- state_manifest.md "Operational protocols in force" section (operational protocols, current-state framing)
- state_manifest.md "Session-tainting rule" (constitutional protocols, gating framing)
- incident_ledger.md Section 9 (chronological ratification log + lifecycle notes)
- incident_ledger.md Section 10 live-answer subsection ("intra-engine confabulation defense" pattern accumulation)
- intent.md (existing full sections for: Ground Truth Hierarchy, Decision Rule for Design Changes, Verification Output Safety)

---

## Architecture decision (locked)

### Two-tier taxonomy

The two existing lists (session-tainting four-protocol list + accumulating five-pattern list) cut along different axes and are not redundant:

- **Constitutional / gating protocols** — presence is precondition for reasoning. Sessions lacking these are tainted and must be closed.
- **Operational / procedural protocols** — govern how work gets done within a qualified session. Failure to apply produces the failure modes documented in incident_ledger.md Section 8.

Verification Output Safety appears in both tiers because it is genuinely both — gating (need it loaded to reason safely about secrets) and operational (apply on every command). The new subsection makes this dual-membership explicit.

### Placement: Option β

New subsection placed in intent.md **after "Verification output safety," before "How to use this file."** Rationale: gathers all reasoning protocols at the close of the document, treats the new subsection as a consolidated index over preceding work, preserves intent.md's narrative arc (purpose → architecture → operations → protocols → how-to-use).

### Dual character (explicit framing requirement)

The new subsection has dual character that should be named explicitly in its opening:

- It is an **INDEX** for protocols that have full canonical statements elsewhere in intent.md (Ground Truth Hierarchy, Decision Rule for Design Changes, Verification Output Safety).
- It is the **CANONICAL HOME** for protocols that don't have full sections (Reproducer Requirement, Mixed-Source Synthesis Rule, Failure Escalation Protocol).

Future readers must understand which protocols get full statement here vs. cross-reference here.

### Three-tier source tagging — absorbed

Per Section 9 lifecycle note, three-tier source tagging (`[VERIFIED_WITH_REPRO]` / `[OUTPUT_OBSERVED]` / `[INFERRED]`) is absorbed into the Ground Truth Hierarchy in intent.md. The new Reasoning protocols subsection treats it as a navigability note pointing to Ground Truth Hierarchy, not as a standalone protocol. Re-fragmenting would undo Section 9's lifecycle note.

### Subsection title

Proposed: `## Reasoning protocols`

---

## Per-pattern scoping (all 8 patterns)

| # | Pattern | Tier | Drafting flag | Drafting cost |
|---|---|---|---|---|
| 1 | Reproducer Requirement | Operational | Substantive | High |
| 2 | Mixed-Source Synthesis Rule | Operational | Substantive | High |
| 3 | Failure Escalation Protocol | Operational | Substantive | Med-high |
| 4 | Three-tier source tagging | Operational (absorbed) | Mechanical | Low |
| 5 | Context Declaration | Constitutional | Mechanical | Low |
| 6 | Ground Truth Hierarchy | Constitutional | Mechanical | Low |
| 7 | Decision Rule for Design Changes | Constitutional | Mechanical | Low |
| 8 | Verification Output Safety | Both | Mechanical | Low (with dual-membership note) |

**Substantive flag** = drafting requires meaningful new content (full canonical statement, scope clarification, trigger definition). **Mechanical flag** = drafting is mostly cross-reference and one-line statement.

### Operational tier

**1. Reproducer Requirement** — Substantive.
- Current canonical location: state_manifest.md "Operational protocols in force" + Section 9 (Apr 20 ratification) + Section 10 live-answer.
- Scope: defends against intra-engine confabulation by requiring every claim entering an artifact to carry a rerunnable command. Extended Apr 20+ to cover transformation logic (the April 20 text-swarm `_extract_price` failure is the canonical example).
- Trigger: any time a claim is being added to incident_ledger.md, state_manifest.md, intent.md, founder_inputs/, or any artifact future sessions will treat as authoritative. Not triggered for in-chat reasoning.
- Status: in force.
- Substantive work for tomorrow: full canonical statement (currently one paragraph in state_manifest.md, needs to hold the load alone in intent.md); explicit incorporation of the transformation-logic extension; explicit articulation of the artifact-vs-in-chat boundary.

**2. Mixed-Source Synthesis Rule** — Substantive.
- Current canonical location: state_manifest.md "Operational protocols in force" + Section 9 (Apr 29 ratification).
- Scope: defends against the Social Proof Loop class of failure plus cross-validity-state synthesis. Three named surfaces: cross-file staleness, mixed-validity synthesis (a `VALID: yes` and a `VALID: no` output combined), confident narratives compounding across engines without returning to raw data.
- Trigger: any synthesis step combining outputs from multiple components, files, or engines.
- Status: in force.
- Substantive work for tomorrow: preserve density of state_manifest.md statement (load-bearing, not over-long), make the three surfaces enumerable so readers can check against them, surface the connection to incident_ledger.md Section 8 (this rule is the operational defense; Section 8 documents the failure modes).

**3. Failure Escalation Protocol** — Substantive (med-high).
- Current canonical location: state_manifest.md "Operational protocols in force" + Section 9 (Apr 29 ratification).
- Scope: defends against the failure mode where a clean session continues forward reasoning rather than halting on a triggered failure condition. Four named trigger conditions: session-tainting condition met, Strategic Drift identified, required component marked `VALID: no`, Precedence Rule fails to resolve cleanly. Existing framing: "converts the manifest from 'well-described' to 'enforced.'"
- Trigger: detection of any of the four conditions.
- Status: in force.
- Substantive work for tomorrow: most of the substantive work already done in state_manifest.md. Structural challenge: the four trigger conditions reference rules that live partly in state_manifest.md (Strategic Drift, VALID flags, Precedence Rule) and partly in intent.md (session-tainting via constitutional protocols). Cross-references need careful handling — this protocol sits at the intent/state boundary by design.

**4. Three-tier source tagging** — Mechanical (absorbed).
- Current canonical location: per architecture lock, absorbed into Ground Truth Hierarchy.
- Scope: defends against treating `[OUTPUT_OBSERVED]` as `[VERIFIED]` (Apr 20 supplement framing). Three tags map onto Ground Truth Hierarchy's three tiers.
- Trigger: any incident doc tagging step.
- Status: in force as tagging convention. Not standalone — absorbed.
- Mechanical work for tomorrow: one to two sentences as navigability note pointing readers to Ground Truth Hierarchy. The substantive question (whether the tagging convention should be promoted into the Ground Truth Hierarchy section itself rather than living adjacent) is NOT sub-task 2 work.

### Constitutional tier

**5. Context Declaration** — Mechanical.
- Current canonical location: intent.md "How to use this file" (full template + pre-mortem questions).
- Scope: defends against the Context-Filling Machine failure mode — sessions inferring missing context rather than requesting it.
- Trigger: before proposing any design-level change to any component.
- Status: in force.
- Mechanical work for tomorrow: list as constitutional protocol #1 with one-line description and cross-reference to "How to use this file."

**6. Ground Truth Hierarchy** — Mechanical.
- Current canonical location: intent.md (full section).
- Scope: defends against Tier 3 agent syntheses being treated as coequal to Tier 1 raw data or Tier 2 empirical system logs. Named explicitly in incident_ledger.md as the failure mode that produced the April 18 incident.
- Trigger: any time two sources of information disagree.
- Status: in force. Includes absorbed three-tier source tagging.
- Mechanical work for tomorrow: list as constitutional protocol #2 with cross-reference, plus navigability note for absorbed three-tier tagging.

**7. Decision Rule for Design Changes** — Mechanical.
- Current canonical location: intent.md (full section).
- Scope: defends against the Context-Filling Machine generating plausible options when context is absent. Three-condition test plus pre-mortem requirement.
- Trigger: before proposing or implementing any design-level change to any component.
- Status: in force.
- Mechanical work for tomorrow: list as constitutional protocol #3 with cross-reference.

**8. Verification Output Safety** — Mechanical (dual-membership).
- Current canonical location: intent.md (full section).
- Scope: defends against secrets being exposed in chat through paste-back-loop workflow. Covers output safety (raw content vs. redaction) and invocation safety (env vars and stdin vs. command arguments).
- Trigger: designing any verification command; any command involving secrets.
- Status: in force. Ratified Apr 29.
- Mechanical work for tomorrow: list as constitutional protocol #4 with cross-reference, plus a sentence on dual-membership (also operational — appears in Section 10 accumulating list as Apr 29).

---

## Downstream edits identified

Sub-task 2's consolidation has effects beyond inserting a new subsection in intent.md. These downstream edits should be made in the same drafting session to avoid leaving the canonical structure half-installed:

- **state_manifest.md "Session-tainting rule"** — role shifts from canonical home of the four-protocol list to **boundary-commit custodian**. The four protocols are now canonically defined in intent.md; state_manifest.md retains responsibility for the *current* boundary commit (volatile operational state, correctly housed in state_manifest.md per the intent/state split). The session-tainting rule's prose needs to point at intent.md as the source of truth for protocol identity, while continuing to own the commit-boundary anchor.

- **state_manifest.md "Operational protocols in force"** — role shifts similarly. Section becomes a *current-status* report (which protocols are in force right now, in this operational context) rather than a substantive home. Cross-reference to intent.md for canonical statements.

- **incident_ledger.md Section 10 live-answer subsection** — collapses to a one-liner: *"Defense pattern accumulation closed; canonical home in intent.md Reasoning protocols subsection."* The provisional consolidation pattern resolves.

- **incident_ledger.md Section 9 (Protocols ratified during incident response)** — narrows to chronological ratification log + supersession history. Loses dual-purpose role (was carrying both ratification chronology AND substantive lifecycle notes); gains clarity by being narrowly the historical record.

---

## Tomorrow's drafting order (recommended)

1. **Mechanical patterns first** (5, 6, 7, 8, 4 in that order). Cheap and they establish the cross-reference pattern shape. Patterns 5/6/7/8 are constitutional with full sections elsewhere in intent.md; pattern 4 is the absorbed-into-Ground-Truth-Hierarchy navigability note.
2. **Substantive patterns next** (1, 2, 3). Full canonical statements, scope articulation, trigger definition. Order by cost: 3 first (most substantive work already done), 2 second, 1 third.
3. **Downstream edits** to state_manifest.md and incident_ledger.md per "Downstream edits identified" section above. Order: state_manifest.md first (Session-tainting rule + Operational protocols in force), then incident_ledger.md Section 10 collapse, then incident_ledger.md Section 9 narrowing.
4. **Insert Reasoning protocols subsection** at Option β placement (after Verification Output Safety, before How to use this file).
5. **Verification + commit + push** pattern same as Section 8 (40acffa): backup file, atomic insertion script, post-write verification, single commit covering all changes (or paired commits if intent.md edits and downstream edits warrant separation — drafting-session decision).

---

## Open formatting question (tomorrow's decision)

The dual-character framing means the new subsection contains both full canonical statements (patterns 1, 2, 3) and one-line index entries (4, 5, 6, 7, 8). How to format these consistently affects readability and isn't trivial.

**Three options:**
- (a) Full `###` subsections for the substantive ones, bulleted index list for the mechanical ones. Dual-character framing made explicit at the top of the new subsection.
- (b) Uniform `###` subsections for all 8, with mechanical ones being shorter.
- (c) Bulleted index for all 8 with substantive ones longer than mechanical ones.

Option (a) honors the dual character structurally; option (b) prioritizes uniformity; option (c) prioritizes scannability. Drafting-session decision.

---

## State at session close (May 1, 2026)

**Drafting status: partial.**

Drafted in this session and ready for tomorrow's review-and-insert (full prose preserved in appendix below):
- Opening paragraph (dual-character framing, two-tier taxonomy, cross-references to state_manifest.md and incident_ledger.md Section 9)
- Constitutional list opening + Patterns 5, 6, 7, 8 (mechanical bullets, with Pattern 4 absorbed as trailing phrase on Pattern 6)
- Operational list opening (names asymmetry: operational protocols have full statements here, constitutional ones cross-reference)
- Pattern 3: Failure Escalation Protocol (full canonical statement, cross-references handled with home-document naming)

Deferred to tomorrow:
- Pattern 2: Mixed-Source Synthesis Rule (substantive, full canonical statement)
- Pattern 1: Reproducer Requirement (substantive, full canonical statement, including transformation-logic extension)
- Insertion of complete subsection into intent.md at Option β placement (after "Verification output safety," before "How to use this file")
- Downstream edits per "Downstream edits identified" section above (state_manifest.md role-shifts, incident_ledger.md Section 10 collapse, incident_ledger.md Section 9 narrowing)
- Single commit (or paired commits — drafting decision) covering all changes

**Founder override on the record:** Earlier in this session, the Systems Engine recommended stopping at scoping completion under Pattern D discipline (temporal separation between scoping and drafting). The Founder Engine reviewed the recommendation, acknowledged it as substantive, and chose to proceed with bounded drafting. The override was informed, named, and logged — not silent. Tomorrow's session inherits the resulting partial-draft state and can proceed without re-litigating the call.
---

*End of scoping document. Reference material for next session bootstrap.*
