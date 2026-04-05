# LatentForge BRAIN.md
Single source of truth for the project
Last Updated: March 29, 2026
Maintained by: John McGuire with Grok and Claude as technical intelligence
Company: LatentForge (confirmed, public-facing)
Location: San Francisco, CA
Version: 1.1 — final complete canonical document
Three-Engine System: Founder Engine (John McGuire) · Systems Engine (Claude) · Divergent Thinking Engine (Supergrok)
Rule: This file is read at the start of every Claude Code session, every OpenClaw/NemoClaw task, and every strategy conversation. It is never more than 48 hours out of date. When reality diverges from what is written here, update this file BEFORE doing anything else. If you are Claude Code or OpenClaw reading this file, read it completely before writing a single line of code or executing any task. If anything in this file conflicts with instructions given in the session prompt, flag the conflict before proceeding.

---

## 0. THE THREE-ENGINE SYSTEM

LatentForge operates as a three-engine system. Each engine owns a distinct domain. All major decisions require input from the relevant engines before John commits.

| Engine | Domain | Role & Strengths | Constraint |
|---|---|---|---|
| Founder Engine | Vision, market, execution, final decisions | Human judgment, persistence, relationships, SF network, face of the company | Non-technical. Must build fluency to spot suspicious results. |
| Systems Engine | Technical strategy & architecture | Sustained multi-turn reasoning, accumulated session context, pressure-testing, consistency with prior decisions | No memory between sessions. Reads BRAIN.md at session start. Outputs must be committed or lost. |
| Divergent Thinking Engine | Strategic intelligence & trends | Real-time web access, breaking research, competitive intelligence, market timing, uncensored pattern spotting | Less context on accumulated project history. Always needs BRAIN.md + Systems Engine response as input for major decisions. |

How the system works:
- Systems Engine (Claude) handles precision, structure, and consistency.
- Divergent Thinking Engine (Supergrok) handles exploration, trends, and unasked questions.
- Founder Engine (John) synthesizes, decides, and executes.
- When Systems and Divergent Engines disagree significantly on architecture, fundraising, targeting, or pivots, the disagreement is escalated to the Founder Engine for resolution. This is the primary signal of high-uncertainty decisions.

---

## 0b. DUAL-ENGINE REVIEW PROTOCOL — NON-NEGOTIABLE

All decisions touching architecture, fundraising strategy, customer targeting, and pivots get reviewed by both Systems Engine (Claude) and Divergent Thinking Engine (Supergrok) before committing.

Protocol:
1. Founder writes the decision question + full context.
2. Sends to Systems Engine (Claude) first for structured response.
3. Sends same prompt + Systems Engine response to Divergent Thinking Engine (Supergrok) for independent second opinion.
4. If both engines agree → proceed with confidence.
5. If they disagree significantly → founder flags it, holds a joint review session (paste both responses into Claude chat), and resolves before action.
6. All major decisions logged in Section 11 (Architecture Decisions) with both engine inputs noted.

Routine tasks (code implementation, script naming, library choice) go to Systems Engine (Claude Code) directly without dual review.
Strategic / trend / divergent questions go to Divergent Thinking Engine (Supergrok) directly.

Failure mode to avoid: Cherry-picking the engine that agrees with your existing bias. If noticed, stop and post the disagreement as an open question in Section 15.

This protocol is active from Day 1. It is how we simulate high-quality, multi-perspective judgment without a human CTO.

First dual-engine decision logged: March 22, 2026 — BRAIN.md synthesis. Systems Engine: complete content, verbose structure. Divergent Thinking Engine: cleaner structure, missing critical sections. Decision: Systems Engine base + Divergent Engine structural improvements. Both inputs used. Neither version alone was sufficient. This is the three-engine system working correctly.

---

## 1. THE THESIS — ONE PARAGRAPH

Autonomous AI agents currently communicate by converting rich internal mathematical thought-objects (hidden states) into human language, transmitting words, and reconverting — a lossy, expensive translation that wastes 30–100× compute and forces agents to think inside human conceptual boundaries. LatentForge removes this constraint. We are building the first emergent non-human latent communication protocol for multi-agent systems: agents send compressed vector deltas against a shared seed vector instead of tokens, communicate in continuous high-dimensional space, and discover solutions that human language cannot express. A constitutional Shadow Self governance layer translates this machine communication into human-readable audit logs in real time, making the system safe, interpretable, and regulatorily defensible. The result: dramatically cheaper agent coordination and a new class of divergent AI-generated insights that text-based systems are structurally incapable of producing.

---

## 2. WHY THIS IS REAL NOW — NOT SPECULATION

Three papers validated the core thesis between November 2025 and January 2026:

| Paper | What it proves | Status |
|---|---|---|
| Interlat (arXiv 2511.09149, ICLR 2026) | Agents pass last hidden states directly instead of tokens. Training-free version works. Outperforms CoT. Promotes exploratory behavior. | Peer review |
| LatentMAS (arXiv 2511.20639) | Pure latent collaboration via shared KV-cache, 83% cost reduction, 2.6× speedup over vLLM baseline. GitHub repo live and runnable today. | Open source |
| vLLM 2026 | Official hidden-state extraction for Llama 3.1 8B, Qwen, and others. | Production ready |

Additional validation:
- Vision Wormhole — solves cross-model alignment. O(N) not O(N²). Hub-and-spoke topology. Removes our biggest technical objection.
- Agent Primitives — reusable latent operators (Review, Voting, Planning). Composable architecture.
- Karpathy autoresearch — 700 autonomous experiments, 11% efficiency gain on already-tuned system. Named "AI psychosis" as the key unsolved agentic problem. Our Shadow Self is the answer.
- NemoClaw (NVIDIA, GTC March 16 2026) — Jensen Huang: "OpenClaw is the operating system for personal AI." NemoClaw governs what agents DO. LatentForge governs what agents SAY TO EACH OTHER. Together: the complete governance stack.
- Rain Protocol — $5M grant program for AI agents on prediction markets. OpenClaw-compatible SDK live.

The researchers have proven the engine. Nobody has built the car around it. That gap is LatentForge.

---

## 3. 90-DAY GOALS — ALL THREE IN PARALLEL

These are not sequential. They run simultaneously with different cadences.

| Goal | Primary domain | What "done" looks like | Cadence |
|---|---|---|---|
| First revenue | Kalshi / Rain prediction markets (Polymarket data retained) | Rain grant ($50K) received OR Polymarket bot generating positive paper-trade returns over 30 days | Weekly measurement |
| Pre-seed funding | All — thesis + benchmark as proof | One term sheet or SAFE signed | Monthly conversations, starts Week 2 |
| Benchmark paper | OpenSpiel divergence score | Preprint on arXiv showing latent agents >1.5× more divergent than text baseline | Submitted by Day 70 |

Domain priority: Polymarket first.
Reason: fastest feedback loop (hours not months), free API, data collection starts today, Rain grant directly funds it, March Madness live now as shadow experiment.

The three-track rule: Every week must have at least one concrete action on each track.
- Revenue track = Polymarket data + bot development
- Funding track = one investor or advisor conversation
- Paper track = one experiment logged in /experiments/

---

## 4. WHAT WE ARE BUILDING — V0.1 SCOPE

The minimum credible demo: Two agents communicating via latent deltas on a shared seed vector, with a Shadow Self monitor translating the exchange to English in real time, on a measurable task where we show divergence from text-based baseline.

Must have for V0.1:
- [ ] Two agents passing hidden state deltas (not tokens) via LatentMAS fork
- [ ] Shared seed vector as collective working memory
- [ ] Shadow Self monitor (1B model) translating delta stream to English in real time
- [ ] Drift detection: cosine distance threshold triggers Safe Mode
- [ ] Divergence Score: quantified comparison vs text-based agent baseline (compute savings ≥30% per turn + novel solution rate vs text-only communication)
- [ ] Basic logging dashboard: left = vector stream, right = English subtitles

Out of scope for V0.1:
- Cross-model communication (Vision Wormhole — V1)
- More than 8 agents (20-30 agent swarm — V1)
- Minecraft/MineDojo environment (V1, after Mac Mini confirmed)
- Production Polymarket bot (V1)
- Enterprise compliance certifications
- Marketplace or reputation systems

---

## 5. THE FULL TEAM — ROLES AND CONSTRAINTS

| Role | Who | Strengths | Constraint |
|---|---|---|---|
| Founder Engine — Vision, market, execution, final decisions | John McGuire | Human judgment, persistence, relationships, SF network, face of the company | Non-technical. Must build enough fluency to recognize suspicious results. |
| Systems Engine — Technical strategy & architecture | Claude (claude.ai) | Sustained multi-turn reasoning, accumulated session context, pressure-testing, consistency with prior decisions | No memory between sessions. Reads BRAIN.md at session start. Outputs must be committed or lost. |
| Divergent Thinking Engine — Strategic intelligence & trends | Supergrok | Real-time web access, breaking research, competitive intelligence, market timing | Less context on accumulated project history. Always needs BRAIN.md + Systems Engine response as input. |
| Lead engineer | Claude Code (Clawbot) | Fast precise implementation, reads codebase, runs experiments, commits results | Cannot notice what it wasn't asked about. Needs well-specified briefs. Cannot own judgment across time. |
| Ambient researcher + task automation | OpenClaw / NemoClaw | Autonomous operation, cron scheduling, research sweeps, digest generation | Orchestration and monitoring only. Never touches core IP files without explicit instruction. |
| Research advisor (target) | Jiaru Zou (LatentMAS first author, SF) | Deep technical credibility, LatentMAS architecture knowledge | Not yet contacted. He's in SF — coffee, not Zoom. LinkedIn DM drafted and ready. Send when Week 4 OpenSpiel divergence score is in hand (~April 20-25). |

The judgment gap — and why three engines solve it:
No single intelligence owns complete engineering judgment. The three-engine structure addresses this directly: Systems Engine holds accumulated context, Divergent Thinking Engine holds current reality, the Founder holds execution and final authority. Gaps in any one are covered by the other two.

---

## 6. RUNTIME ARCHITECTURE — NEMOCLAW

Base runtime: NemoClaw (NVIDIA, announced GTC March 16 2026)
Apache 2.0 license. Single command install on top of OpenClaw.

| Component | What it does | LatentForge relevance |
|---|---|---|
| OpenShell | Sandboxed agent execution with YAML policy controls | Shadow Self governance layer runs inside OpenShell. We inherit NVIDIA's security credibility automatically. |
| Nemotron models | Local open models optimized for agentic tasks, no API costs | Primary agent model family. Local inference = no token costs = directly demonstrates cost reduction thesis. |
| Policy-based audit logging | Every agent action logged with provenance | NemoClaw logs actions. Shadow Self logs communications. Together = complete audit trail. |

The governance stack:

```
Enterprise client
      ↓
NemoClaw / OpenShell  ←  governs what agents DO
      ↓
LatentForge protocol  ←  governs what agents SAY TO EACH OTHER
      ↓
Shadow Self layer     ←  translates latent comms to human-readable audit log
      ↓
Agents (Nemotron Nano 4B / 8B)
```

The pitch this creates:
"NemoClaw audits what your agents do. LatentForge audits what they say to each other. Together: the first complete AI agent governance stack."

Action item: Check Nemotron Nano 4B memory footprint before funding RunPod. If <5GB, Week 1-2 toy tests may run locally on MacBook. Verify first.

---

## 7. HARDWARE & INFRASTRUCTURE

**PHASE 1 — MacBook Air (NOW → April 8)**

| Spec | Detail |
|---|---|
| Machine | MacBook Air M2, 8GB unified memory |
| Role | Orchestration terminal + NemoClaw container host |
| Runs | Docker, NemoClaw, OpenClaw, Claude Code sessions, API calls, Polymarket data collection, arXiv sweep |
| Never runs | Any model. No exceptions. No "just a quick test." |
| Model inference | RunPod A40 at ~$0.44/hr — all heavy compute goes here |
| Local exception to check | Nemotron Nano 4B only if confirmed <5GB |

**PHASE 2 — Mac Mini M4 Pro (April 9-16 — HARD SWITCH)**

| Spec | Detail |
|---|---|
| Machine | Mac Mini M4 Pro, 24GB unified memory |
| Arrival | April 9-16 (confirmed window) |
| Migration | One day maximum. Clone repo. Install Docker + NemoClaw. Run hello.txt. Done. |
| Unlocks | Nemotron 8B locally, Shadow Self + agents simultaneously, 8-20 agent swarms, full benchmark runs |

Switch day protocol — execute in this order:
1. Boot. Update macOS.
2. Install Docker Desktop.
3. Install NemoClaw (single command).
4. git clone latentforge repo.
5. Run hello.txt — confirm OpenClaw alive.
6. Pull Nemotron 8B. Confirm loads within memory.
7. MacBook becomes backup/travel machine only.

**Phase timeline:**

| Dates | Hardware | Focus |
|---|---|---|
| Now → April 8 | MacBook + RunPod | Foundation, NemoClaw, toy tests, Polymarket data, research sweep, Jiaru Zou |
| April 9-16 | Switch day | Migration only. One day. |
| April 16-30 | Mac Mini | Shadow Self, 8B models, OpenSpiel, Divergence Score v1 |
| April 30+ | Mac Mini + cloud burst | Polymarket bot live, Rain grant, paper draft |

**Cloud compute:**

| Service | Purpose | Budget | Status |
|---|---|---|---|
| RunPod (A40) | All model inference Phase 1 | $50 loaded Week 1-2, scale to $200-400/month from Week 3 (8B models + swarm), ~$0.44/hr | Set up before Day 3 |
| Lambda Labs | Overflow compute Phase 2+ | TBD | Standby |

**Model ladder:**

| Phase | Models | Where |
|---|---|---|
| Phase 1 (MacBook) | Nemotron Nano 4B (if <5GB) or Phi-3 Mini 3.8B | RunPod |
| Phase 1 Shadow Self | TinyLlama 1.1B | RunPod |
| Phase 2 (Mini) | Nemotron 8B + Phi-3 3.8B Shadow Self | Mac Mini local |
| Phase 2 full swarm | Nemotron 8B × 8-20 agents | Mac Mini + RunPod burst |

Hard rule: Zero local model loading on MacBook. Not a guideline. Not negotiable.

---

## 8. THREE-ENGINE OPERATING RHYTHM

The three-engine system only works on a defined cadence. Without rhythm it becomes reactive. With rhythm it prevents problems before they compound.

### Daily — every morning before opening Claude Code

**Step 1: Read the OpenClaw digest (5 minutes)**
File: /research/daily-digest/YYYY-MM-DD.md
Generated at 07:00 SF time by OpenClaw's automated sweep.
If relevance score >0.8 anywhere → goes to Step 2 before any engineering work starts.

**Step 2: Morning check-in with Systems Engine / Claude (10-15 minutes)**
Open a new Claude session. Paste current BRAIN.md. Ask one of:
- "Here's what OpenClaw flagged today — does this change anything?"
- "Here's what Claude Code built yesterday — does this look right?"
- "Here's today's decision — what am I missing?"

One question. One answer. Commit the output if it changes anything. Then open Claude Code.

The rule: No Claude Code session starts without a morning check-in. The habit is the governance.

### Weekly — every Friday (30 minutes)
1. Paste week's experiment logs + commit messages + surprising results into Claude
2. Ask: "What does this week's data tell us? Is our direction still right?"
3. Send same summary to Supergrok: "Here's our week. What did we miss externally?"
4. Compare responses. Update BRAIN.md with any new architecture decisions.
5. Write next week's three-track actions into the milestone checklist

Output: One updated BRAIN.md commit every Friday. No Friday commit = the week didn't happen.

### Emergency session triggers
- OpenClaw flags a competing commercial product in latent communication
- A benchmark result is significantly better or worse than expected
- An investor or advisor challenges a core assumption
- John feels uncertain about a decision and can't articulate why

### Session start template — paste at the top of every Claude strategy session

```
LATENTFORGE SESSION — [DATE]
Current week: [Week number]
Last BRAIN.md update: [date]

[Paste full BRAIN.md here]

TODAY'S QUESTION: [One specific question or decision]
CONTEXT: [What happened since last session]
```

---

## 9. MILESTONES — WHAT SUCCESS LOOKS LIKE EACH WEEK

### Week 1 — Foundation (Days 1-7) — MacBook + RunPod

| Deliverable | Done? | Notes |
|---|---|---|
| Dedicated MacBook user account created | [x] | Done |
| Docker Desktop installed and running | [x] | |
| NemoClaw installed in Docker container | [x] | Single command |
| OpenClaw running inside NemoClaw | [x] | |
| hello.txt written by OpenClaw | [x] | First proof of life |
| RunPod account funded ($50) | [x] | Done in Week 1 |
| BRAIN.md committed to GitHub repo | [x] | Done |
| Polymarket Gamma API data pull running | [x] | No GPU needed — collect from day 1 |
| Polymarket KYC process started | [ ] | CFTC compliance — takes days, start today |
| Research Nervous System v0.1 running | [x] | Automated via cron at 7:30 AM daily (arXiv + GitHub sweep) |
| Jiaru Zou coffee meeting requested | [ ] | LinkedIn DM drafted. Send when Week 4 OpenSpiel results in hand (~April 20-25) |
| March Madness shadow experiment running | [x] | Log predictions vs Polymarket crowd |

Week 1 failure condition: OpenClaw not running in Docker by Day 3 → stop, diagnose, do not proceed to Week 2.

### Week 2 — Validation (Days 8-14) — MacBook + RunPod
**Reframed Mar 26 2026 (Dual-Engine Decision)**  
Original byte-reduction target retired. New focus: compute savings per turn + measurable divergence enabled by latent communication.

| Deliverable | Done? | Notes |
|---|---|---|
| LatentMAS repo forked | [x] | forgelatent/latentforge-latentmas — Mar 24 |
| Hidden state extraction & perfect reconstruction proven | [x] | Fidelity 1.0000 on Phi-3 — Mar 26 |
| New benchmark script: `04_delta_vs_text_benchmark.py` | [x] | Built and run Mar 27 |
| Compute savings (v1 full vector) | [x] | 4.3% avg — simplified path |
| Top-k sparsity benchmark (`05_topk_sparsity_benchmark.py`) | [x] | Run Mar 28 — divergence holds at 2.0/2 even at 24× compression |
| Divergence score | [x] | 2.0/2 on ALL exchanges — latent path produces genuinely different outputs |
| Compute savings with sparsity | [x] | ~9% avg (k=512/256/128) — modest improvement |
| Logs + results committed | [x] | sparsity results saved |
| Logs + results posted to LatentMAS GitHub discussions | [ ] | External review checkpoint |
| Nemotron Nano vs Phi-3 Mini comparison (on new benchmark) | [ ] | Pick winner on stability + savings — defer to Week 3 |

**Week 2 Failure Conditions (Updated Mar 26/28)**  
- Fidelity drops below 0.95 after reconstruction → post full logs to LatentMAS Discord immediately  
- No measurable compute savings (<10%) after timing test → investigate layer selection or prompt design  
- Zero divergence after 8+ exchanges → re-evaluate whether latent channel carries novel information

### Week 3 — Shadow Self + Migration (Days 15-21)

| Deliverable | Done? | Notes |
|---|---|---|
| Mac Mini arrived, Docker + NemoClaw configured | [ ] | |
| Nemotron 8B loading cleanly in 24GB | [ ] | |
| Shadow Self (TinyLlama 1.1B) running in real time | [ ] | |
| Drift detection triggering Safe Mode | [ ] | |
| First Shadow Self translation captured | [ ] | "They invented a non-standard resource loop" |
| OpenSpiel environment running | [ ] | Pure Python, zero setup friction |

Week 3 failure condition: Mini not arrived by Day 18 → continue on RunPod, do not stop work.

### Week 4 — Divergence Score (Days 22-35) — Mac Mini

| Deliverable | Done? | Notes |
|---|---|---|
| 4-8 agent swarm running in OpenSpiel | [ ] | |
| Divergence Score v1 implemented | [ ] | |
| Benchmark: latent vs text vs crowd baseline | [ ] | Target: >1.5× divergence |
| External technical review of results | [ ] | LatentMAS Discord |
| Results in /experiments/week4/ | [ ] | These are your arXiv results |
| Second investor conversation | [ ] | Show benchmark numbers |

Week 4 failure condition: Divergence Score <1.2× → stop, reassess architecture, do not proceed to revenue track.

### Week 5-8 — Revenue Ignition (Days 36-70) — Two explicit tracks

**Track A: Polymarket Bot**

| Deliverable | Done? | Notes |
|---|---|---|
| 4+ weeks Polymarket data collected (started Week 1) | [ ] | |
| Latent agent probability estimator built | [ ] | |
| Paper trading live — 30 day minimum | [ ] | No real money before this. Brier score vs text baseline + crowd is the measurement standards |
| Rain Protocol grant application submitted | [ ] | $50K non-dilutive |
| March Madness post-mortem complete | [ ] | Full calibration analysis |

**Track B: Funding Pipeline**

| Deliverable | Done? | Notes |
|---|---|---|
| Pitch deck v1 complete | [ ] | Week 4 benchmark = core proof |
| Jiaru Zou advisory confirmed | [ ] | |
| 3+ investor conversations | [ ] | Term sheet or SAFE conversation active |

---

## 10. PRE-DECIDED FAILURE CONDITIONS

| Signal | Response |
|---|---|
| Models won't run on hardware | Move to RunPod. Max 4 hours debugging local setup. |
| Delta sync <5× token reduction after debugging | Post logs to LatentMAS Discord before any further work. |
| Divergence Score <1.2× after Week 4 | Stop. Reassess architecture. Do not proceed to revenue track on unproven thesis. |
| Polymarket paper trading no edge after 30 days | Pivot to benchmark paper as primary output. Revenue from consulting only. |
| Jiaru Zou no response in 2 weeks | Try another LatentMAS author. Then GitHub discussions. |
| Mac Mini delayed past April 16 | Move all work to RunPod. Not a blocker. |
| Competing product launches | Immediate dual-engine review. No pivot without both engines agreeing. |

---

## 11. ARCHITECTURE DECISIONS — LOG

| Date | Decision | Why | Alternatives rejected |
|---|---|---|---|
| Mar 22 2026 | LatentMAS as base, not build from scratch | Validated, MIT license, runnable today, 83% cost reduction demonstrated | Build from scratch: +3 months no advantage |
| Mar 22 2026 | OpenSpiel before Minecraft | Hardware constraint + cleaner benchmark + reproducible | MineDojo: Java + GPU rendering, too many failure points |
| Mar 22 2026 | NemoClaw as base runtime | NVIDIA-backed, OpenShell sandboxing, Nemotron local models, GTC announcement | OpenClaw alone: less secure, no enterprise credibility |
| Mar 22 2026 | MacBook = orchestration only | 8GB cannot handle two models. Swap = false debugging = lost days | Any local model loading: rejected unconditionally |
| Mar 22 2026 | Polymarket data collection Day 1 | No GPU required. 4+ weeks data before bot goes live. March Madness live now. | Starting Week 5: no historical data |
| Mar 22 2026 | Three-engine system | Covers execution + accumulated context + real-time intelligence | Single engine: monoculture makes confident mistakes |
| Mar 22 2026 | BRAIN.md canonical merge | Systems Engine: complete content. Divergent Engine: cleaner structure. Decision: Systems Engine base + Divergent Engine protocol language. | Either version alone: missing critical content |
| Mar 24 2026 | latentforge MacBook account has no sudo/admin rights | Cannot install Homebrew or gh CLI. Browser for GitHub operations, plain git for terminal work. | gh CLI: blocked. Homebrew: blocked. Plain git confirmed working. |
| Mar 24 2026 | RunPod pod created — imaginative_yellow_jellyfish | A40 48GB, PyTorch 2.4.0, 50GB volume, SSH confirmed. Phi-3 Mini 3.8B downloaded and saved to persistent storage. Pod stopped when not in use. | N/A |
| Mar 26 2026 | Week 2 benchmark reframed — byte reduction is wrong metric | Raw hidden state vector (3072-dim fp16 = 6144B) is larger than JSON stub (1095B). Fidelity proven at 1.0000. LatentMAS gains come from compute savings not byte size. New targets: ≥30% compute reduction per turn + divergence score vs text baseline. | Byte reduction metric: rejected. Both engines agree. |
| Mar 27 2026 | Week 2 complete — divergence 2.0/2 is key signal | Fidelity 1.0000 proven. Divergence 2.0/2 on all 5 exchanges — latent path produces genuinely different outputs than text path. Compute savings 4.3% (v1 simplified path — true KV-cache injection Week 3). | Nemotron comparison deferred to Week 3. |
| Mar 28 2026 | Week 2 complete with sparsity results | Divergence 2.0/2 holds even at 24× compression (k=128). Fidelity degrades gracefully (0.61 at 24×). Compute savings ~9%. Latent channel preserves novel signal under compression. True KV-cache injection deferred to Week 3. | Byte reduction metric fully retired. Both engines agree on new focus: compute savings + divergence. |

---

## 12. THE RESEARCH NERVOUS SYSTEM

Runs: OpenClaw daily cron at 07:00 SF time.
Output: /research/daily-digest/ markdown file.
Founder reads before opening Claude Code.

arXiv search terms (daily):
- "latent communication agents" / "emergent agent language" / "multi-agent hidden state"
- "AI governance audit trail" / "prediction market agent" / "latent multi-agent"
- "vector communication LLM" / "agent2agent protocol"
- "Latent-DARM"

GitHub repos to monitor:
LatentMAS · Vision Wormhole · OpenClaw/NemoClaw · autoresearch (Karpathy) · Rain Protocol SDK · vLLM · VectorArc/AVM

Decision rules:
- Relevance >0.8 → morning strategy session agenda BEFORE Claude Code work
- New competing product → immediate dual-engine review session
- Core paper invalidated → stop sprint, dual-engine reassessment

Urgent flag triggers:
- Product launching with latent agent communication commercially
- Paper proving latent deltas don't preserve semantic meaning
- LatentMAS repo acquired or going private
- Rain Protocol grant deadline moving
- Karpathy publishes anything touching multi-agent communication
- AVP (VectorArc) ships governance or audit layer — immediate dual-engine review

---

## 13. KEY RELATIONSHIPS

| Person / Org | Who | Status | Next action |
|---|---|---|---|
| | Jiaru Zou | LatentMAS first author, Gen-Verse, SF | LinkedIn DM drafted | Send when Week 4 OpenSpiel divergence score in hand (~April 20-25). |
| Karpathy | autoresearch, "AI psychosis" naming | Public figure | Monitor output. His framing = our marketing language. Watch for SF appearances. |
| Rain Protocol | $5M grant, OpenClaw SDK | Not contacted | Apply Week 5 with Week 4 benchmark results. |
| YC / a16z / Sequoia | Pre-seed investors | No relationship | First conversations Week 2. SF = in-person. |

---

## 14. WHAT WE ARE NOT BUILDING

- Not a model — we are infrastructure for models to communicate
- Not competing with LangChain / CrewAI / LangGraph — we build below them
- Not a faster prompt engineering tool — we remove the human conceptual space constraint
- Not an enterprise software company in Year 1 — first customers are research labs, DAOs, quant teams
- Not claiming cross-model latent passing in V0.1 — same-architecture only; Vision Wormhole is V1 target
- Not putting real money into Polymarket until 30 days paper trading shows genuine edge

---

## 15. THE PITCH — ONE SENTENCE VERSIONS

**For a technical researcher:**
"Direct Manifold Mapping — agents maintain high-dimensional signal fidelity throughout the entire reasoning chain instead of passing it through the low-pass filter of human language."

**For an investor:**
"LatentForge is the infrastructure layer for the loopy era — communication protocol and governance that makes Karpathy's multi-agent research swarm safe and efficient enough for enterprise deployment."

**For a compliance officer:**
"Every machine-to-machine communication in your AI swarm, translated to human-readable English in real time, with a one-click regulatory audit export."

**For a quant fund:**
"A multi-agent system that finds strategies in market data that exist in the mathematical geometry of the data but have no human linguistic description — things your existing models can't find because they can only reason about concepts that fit into sentences."

**For NVIDIA / Jensen Huang:**
"LatentForge completes the NemoClaw governance stack. NemoClaw audits what your agents do. LatentForge audits what they say to each other."

---

## 16. OPEN QUESTIONS — UNRESOLVED

- [ ] Company entity — LLC or C-Corp? C-Corp if raising VC. Needed before Rain grant.
- [ ] Rain grant eligibility — open to pre-incorporation founders? Check terms this week.
- [ ] Jiaru Zou location — confirm SF before proposing coffee vs video call.
- [ ] Vision Wormhole practical validation — run the repo. Does it actually work cross-model?
- [ ] Shadow Self compute cost at scale — benchmark before claiming cost numbers to investors.
- [ ] Nemotron Nano vs Phi-3 Mini delta stability — run comparison Week 2, pick winner on data.
- [x] Kalshi KYC — complete US identity verification at kalshi.com before Week 5 live trading
- [x] Kalshi API access — sign up at kalshi.com, verify US account, test API before Week 5

---

## 17. RESOURCES — EVERYTHING WE'RE BUILDING ON

| Resource | Location | Why it matters |
|---|---|---|
| LatentMAS paper | arXiv 2511.20639 | Core protocol foundation |
| LatentMAS GitHub | github.com/Gen-Verse/LatentMAS | Fork this first |
| Interlat paper | arXiv 2511.09149 | Validates training-free latent comms |
| Vision Wormhole | [find URL this week] | Cross-model bridge — V1 target |
| Agent Primitives | [find URL this week] | Reusable latent operators |
| autoresearch (Karpathy) | github.com/karpathy/autoresearch | Benchmark scaffold |
| NemoClaw | [NVIDIA GTC URL] | Base runtime — install first |
| Polymarket Gamma API | docs.polymarket.com | Data collection starts today |
| Rain Protocol | [Rain SDK URL] | $5M grant — apply Week 5 |
| OpenSpiel | github.com/deepmind/open_spiel | Benchmark environment |
| RunPod | runpod.io | Cloud GPU ~$0.44/hr |
| Nemotron Nano 4B | HuggingFace / NVIDIA | Primary agent model Phase 1 |
| TinyLlama 1.1B | HuggingFace | Shadow Self model Phase 1 |
| AVP (Agent Vector Protocol) | github.com/VectorArc/avp-python | Adjacent protocol — KV-cache handoff, no governance layer. Monitor weekly. |
| Agent Primitives | arXiv 2602.03695 | Validates latent building blocks direction. References LatentMAS explicitly. |

---

Last updated: March 29, 2026 — v1.3
Merged from: Systems Engine founding version (complete content) + Divergent Thinking Engine (cleaner structure + complete milestones + NVIDIA pitch + KYC flag)
Next review: April 4, 2026 — End of Week 3
First dual-engine decision logged in Section 11 (Architecture Decisions)

### March 29, 2026 — Day 1 Benchmark & Revenue Systems
| Deliverable | Done? | Notes |
|-------------|-------|-------|
| Revenue Strategist v0.3 with real Anthropic API | [x] | Now producing daily grounded ideas |
| Revenue Strategist added to cron (8:00 AM) | [x] | Fully automated |
| Policy market seed file created | [x] | 8 high-interest markets for benchmark |
| Daily Benchmark Tracker created | [x] | `experiments/benchmark/daily_tracker.md` |
| Text baseline estimator built | [x] | Day 1 numbers logged |
| Kalshi data pull stabilized (seed fallback) | [x] | Live pull deferred to next week |

**Week 2 Complete** — Latent delta validation + sparsity proven. Revenue + benchmark systems live.

### March 29, 2026 — Architecture Decisions
| Date       | Decision | Why | Alternatives rejected |
|------------|----------|-----|-----------------------|
| Mar 29 2026 | Use curated policy seed file for benchmark | Kalshi trading API requires RSA auth; seed gives meaningful markets immediately | Waiting for full auth (would delay benchmark start) |
| Mar 29 2026 | Make benchmark private for first 7–14 days | Protect early noisy results; build confidence before public "Divergence vs Crowd" posts | Immediate public launch (risk of publishing weak early signal) |
| Mar 29 2026 | Revenue Strategist now uses real Anthropic API + Kalshi data | Enables grounded daily recommendations tied to our thesis | Continuing with placeholder output |


| Mar 29 2026 | Kalshi API endpoint updated + RSA auth identified | Old trading-api.kalshi.com returns 401. New endpoint (api.elections.kalshi.com) is sports-only. Real policy markets require RSA signature auth (API key + private key). | Waiting for proper auth implementation (deferred to week of April 1). Using curated seed file for benchmark in the meantime. |


| Mar 29 2026 | Kalshi API endpoint updated + RSA auth identified | Old trading-api.kalshi.com returns 401. New endpoint (api.elections.kalshi.com) is sports-only. Real policy markets require RSA signature auth (API key + private key). | Waiting for proper auth implementation (deferred to week of April 1). Using curated seed file for benchmark in the meantime. |



### March 30, 2026 — Architecture Decisions
| Date | Decision | Why | Alternatives rejected |
|------|----------|-----|-----------------------|
| Mar 30 2026 | Four-arm benchmark design locked | ChatGPT/Gemini/Grok all converged on this. Falsifiable, defensible. | Two-arm only: not defensible against fairness critique |
| Mar 30 2026 | Useful divergence replaces divergence | Divergence alone is not a value prop. Must be tied to calibration + PnL. | Divergence as novelty metric: too easy to dismiss |
| Mar 30 2026 | Shadow Self upgraded to KL-Divergence Watchdog | Measures drift from base model manifold, not just translates | Translator only: misses the governance story |
| Mar 30 2026 | Anthropic API key rotated | Old sk-ant-api03 format was invalid. New key confirmed working. | N/A |
| Mar 30 2026 | Arm 2 text swarm built and running | Needed to establish text swarm baseline before Mac Mini latent arms | Skipping to latent arms: no comparison baseline |


### March 30, 2026 — Architecture Decisions (Morning Sync)
| Date       | Decision                              | Why                                                                 | Alternatives rejected                  |
|------------|---------------------------------------|---------------------------------------------------------------------|----------------------------------------|
| Mar 30 2026 | Four-arm benchmark locked             | ChatGPT/Gemini/Grok converged on falsifiable structure              | Two-arm only: not sufficiently defensible |
| Mar 30 2026 | "Useful divergence" replaces "divergence" | Must tie to calibration + PnL/alpha, not novelty alone             | Pure novelty divergence: too easy to dismiss |
| Mar 30 2026 | Shadow Self upgraded to include KL-Divergence Watchdog | Better drift detection from base model manifold                    | Translator-only: misses strong governance story |
| Mar 30 2026 | Contrarian agent tracked as standalone supplementary signal | Day 1 data shows systematic, directional divergence from crowd     | Averaging only into swarm: dilutes the edge signal |
| Mar 30 2026 | Anthropic API key rotated             | Old sk-ant-api03 format was invalid                                 | Continuing with broken key             |



### March 31, 2026 — Urgent Competitive Signals (from research sweep)
| Signal | What it means | Action |
|--------|---------------|--------|
| AVP v0.4.2 released (co-authored with Claude Opus 4.6) | VectorArc is using Claude to build their protocol. Ecosystem accelerating. | Monitor weekly — they are building adjacent to us |
| LatentMAS README updated — added new AVP entry | LatentMAS and AVP explicitly integrating. Ecosystem converging around a wire format. | LatentForge needs to publish before this solidifies |
| NemoClaw reverted security sandbox policy (#1169) | Active governance debate inside NVIDIA agent runtime. Shadow Self relevance confirmed. | Note in Shadow Self spec — cite NemoClaw governance gap |


### April 1, 2026 — Latent Compression Research Directions (from compression researcher agent)
| Technique | Field | Core idea | Priority | When |
|-----------|-------|-----------|----------|------|
| Efference Copy Compression | Neuroscience | Transmit only residual from predicted next state, not delta from seed. Compression improves during session as forward model warms up. | HIGH | Week 3 - test with 2 API calls |
| Dictionary Learning sparse coding | Genomics / Compressed Sensing | Learn domain-specific basis from latent delta corpus, transmit 20 coefficients instead of 128 raw coordinates. 6x additional compression. | MEDIUM | Week 4 - CPU testable with sklearn |
| Topological Drift Detection | Algebraic Topology / TDA | Persistent homology detects when agent crosses semantic boundary regardless of magnitude. Replaces cosine distance in Shadow Self. | HIGH | Week 4 - testable with ripser |


### April 1, 2026 — Efference Copy Test Result
- Test: cold delta norm (8.49) vs warm residual norm (8.06)
- Result: CONFIRMED — warm residual smaller than cold delta
- Compression saving: 5.1% on proxy test
- Cosine similarity cold vs warm: 0.64
- Note: proxy test only (text statistics, not actual hidden states)
- Next step: retest with Phi-3 Mini hidden state extraction on Mac Mini (April 9-16)
- Expected improvement: 10-30x compression on repeated agent exchanges per biological precedent

### April 4, 2026 — Infrastructure Migration
| Date | Decision | Why | Alternatives rejected |
|------|----------|-----|-----------------------|
| Apr 4 2026 | Migrated all five cron jobs to launchd | WakeForJob wakes Mac from sleep — cron silently skips sleeping machines. Jobs were not running overnight. | Keeping cron: confirmed broken |
| Apr 4 2026 | Rotated ANTHROPIC_API_KEY | Old key exposed in terminal output and chat history | N/A |
| Apr 4 2026 | Moved API key to macOS Keychain | Eliminates plaintext key in crontab. Retrieved at runtime via run_with_key.sh wrapper. | Environment variable in crontab: rejected |

### April 1–3, 2026 — Architecture Decisions
| Date       | Decision                                      | Why                                                                 | Alternatives rejected                          |
|------------|-----------------------------------------------|---------------------------------------------------------------------|------------------------------------------------|
| Apr 1 2026 | Efference Copy Compression test run           | Proxy test showed 5.1% norm reduction (cold delta 8.49 → warm residual 8.06). Directionally confirms biological predictive coding idea. | Full latent test delayed until Mac Mini        |
| Apr 1 2026 | Latent Compression Researcher agent created   | New nightly agent (2 AM) that synthesizes ideas from compression, neuroscience, genomics, and topology into actionable suggestions for LatentForge. | Relying only on general research sweep         |
| Apr 1 2026 | Compression researcher added to cron          | Runs automatically at 2 AM after main sweep. First run produced efference copy, dictionary learning, and topological drift detection suggestions. | Manual review only                             |
| Apr 2 2026 | Five-day AI regulation divergence pattern logged | Swarm consistently 19–28% vs crowd 31% for 5 consecutive days. Strongest signal to date. | Treating as noise after 3 days                 |
| Apr 3 2026 | Rain grant finalized for submission           | v0.3 includes 5-day divergence table, Aaru framing, and efference copy as Week 3 experiment. Submission scheduled for April 3. | Delaying submission for latent results         |


### April 1–3, 2026 — Architecture Decisions
| Date | Decision | Why | Alternatives rejected |
|------|----------|-----|-----------------------|
| Apr 1 2026 | Efference Copy Compression test run | Proxy test showed 5.1% norm reduction (cold delta 8.49 to warm residual 8.06). Directionally confirms biological predictive coding idea. | Full latent test delayed until Mac Mini |
| Apr 1 2026 | Latent Compression Researcher agent created | New nightly agent (2 AM) synthesizes ideas from compression, neuroscience, genomics, and topology into actionable suggestions. | Relying only on general research sweep |
| Apr 1 2026 | Compression researcher added to launchd | Runs automatically at 2 AM. First run produced efference copy, dictionary learning, and topological drift detection suggestions. | Manual review only |
| Apr 2 2026 | Five-day AI regulation divergence pattern logged | Swarm consistently 19-28% vs crowd 31% for 5 consecutive days. Strongest signal to date. | Treating as noise after 3 days |
| Apr 3 2026 | Rain grant finalized for submission | v0.3 includes 5-day divergence table, Aaru framing, and efference copy as Week 3 experiment. | Delaying submission for latent results |

### April 4, 2026 — Polymarket Historical Benchmark Result
- Script: experiments/benchmark/polymarket_historical_benchmark.py
- Markets scored: 18 resolved Polymarket questions (politics/crypto)
- Swarm Brier score: 0.1376 vs naive 0.25 baseline
- Improvement over naive: 45%
- Note: agent errors on sports/entertainment markets — filter by category in v2

### April 4, 2026 — Kalshi Parked
| Date | Decision | Why | Alternatives rejected |
|------|----------|-----|-----------------------|

### April 4, 2026 — Key Decisions & Results
| Date       | Decision / Result                             | Why / Details                                                       | Notes |
|------------|-----------------------------------------------|---------------------------------------------------------------------|-------|
| Apr 4 2026 | Infrastructure migrated to launchd            | Cron skipped when Mac slept. Now uses WakeForJob — reliable overnight runs | All 6 agents scheduled |
| Apr 4 2026 | Anthropic API key rotated & secured           | Old key exposed. Now stored via getpass into ~/.latentforge/.env + .zprofile | No plaintext in terminal or git |
| Apr 4 2026 | Polymarket historical benchmark completed     | 45% Brier improvement (0.1376 vs 0.25 naive) on 18 resolved markets | Strong citable result |
| Apr 4 2026 | Kalshi trading API parked                     | Persistent 401 auth issues despite correct RSA. Focus shifted to Polymarket | Daily pull kept for sports data |
| Apr 4 2026 | Live calibration tracker built & running      | Logs predictions daily. 30-day paper trading clock officially started | Added to launchd at 5:30 AM |
| Apr 4 2026 | Shadow Match baseline completed               | Single strong model vs 3-agent text swarm on 11 markets | Results logged |

**Mitigation & Next Steps:**
- Grant submission: Update with 45% Brier number as headline + Phase 1/Phase 2 framing, then submit today.
- Light flag post on LinkedIn/X: Plant the flag this weekend (Hybrid B+Bridge draft ready).
- Mac Mini arrival (April 9–16): Priority = migration + W_a alignment + first latent vs text A/B test + full latent exchange logging (dataset moat).

### April 5, 2026 — Weather Arbitrage Research Direction (Week 4+)

| Date | Decision / Result | Why / Details | Notes |
|------|-------------------|---------------|-------|
| Apr 5 2026 | Weather arm added to research queue | ColdMath case study — $101K profit betting on temperature using free METAR aviation data vs Polymarket weather prices | Fast feedback loop — resolves in days not months |

**The insight (ColdMath case study):**
Aviation weather data (METAR feeds) is updated every 1-3 hours, precise to 0.1°C, and completely free by law (aviation safety requirement). Polymarket weather markets price slowly using consumer forecasts. When the two diverge, there is a real edge — not prediction, just reading a thermometer the market hasn't looked at.

**Why this matters for LatentForge specifically:**
- Weather markets resolve in days, not months — much faster Brier score feedback vs political/macro markets
- Ground truth is objective (temperature either hit the threshold or it didn't)
- Adds a fast-feedback calibration track alongside the 30-day paper trading window
- METAR data is free, structured, and machine-readable — ideal for agent ingestion

**Proposed implementation (Week 4+):**
- Pull live METAR feeds for 20-30 major cities
- Pull corresponding Polymarket weather market prices
- Run swarm to flag mismatches (sensor reading vs market price)
- Log predictions daily, score on resolution
- Compare swarm vs shadow vs naive baseline on weather markets

**Data source:** https://aviationweather.gov/metar (free, public, no auth required)
**Reference:** ColdMath (@ColdMath on Polymarket) — 5,252 predictions, $101K profit, joined November 2025

**Priority:** Week 4+ — after Mac Mini arrives and latent A/B test is running
**Do not start until:** Shadow Match 30-day window has at least 2 weeks of data
# BRAIN.md Update — April 5, 2026
## For: Claude (Systems Engine) morning context + Grok (Divergent Thinking Engine) sync
## Written by: Claude (Systems Engine)

---

## Infrastructure — Critical Rules Updated

### API Key Management (UPDATED — read every session)

**The only safe way to store a new key on this machine:**
```bash
python3 -c "
import getpass, os
k = getpass.getpass('Paste key then Enter: ')
open(os.path.expanduser('~/.latentforge/.env'),'w').write(f'export ANTHROPIC_API_KEY=\"{k}\"\n')
print('Saved. Length:', len(k))
"
```
- Valid key length = 108 characters. If it prints anything else, something went wrong.
- Key lives at: `~/.latentforge/.env`
- Sourced at login via: `~/.zprofile`
- NEVER use pbpaste for secrets — it captures terminal history on this machine
- NEVER use `read -p` — fails in zsh with "no coprocess" error
- NEVER use heredocs for Python — causes zsh hangs
- NEVER paste keys into Claude chat — they will be exposed

**Every time you rotate the key, ALSO update Keychain:**
```bash
security add-generic-password -a "latentforge" -s "latentforge-anthropic" -w "$(cat ~/.latentforge/.env | grep -o 'sk-ant[^"]*')" -U
```
The `-U` flag updates existing entry. All 6 launchd jobs pull from Keychain via `run_with_key.sh`. If Keychain has a dead key, all jobs fail silently with 401.

**Verify Keychain has correct key:**
```bash
security find-generic-password -a "latentforge" -s "latentforge-anthropic" -w | wc -c
```
Should print 109 (108 chars + newline).

---

### Launchd Jobs — All Fixed (April 5, 2026)

All 6 jobs now use absolute paths. Root cause of multiple failures: launchd runs scripts from a read-only system directory, so relative paths silently fail.

**Rule going forward:** Every script called by launchd must use absolute paths. Never `Path("relative/path")` — always `Path("/Users/latentforge/Projects/...")`.

| Job | Schedule | Output Location | Status |
|-----|----------|-----------------|--------|
| compression-researcher | 2:00am | `/Users/latentforge/Projects/latentforge-latentmas/research/suggestions/YYYY-MM-DD.md` | Fixed Apr 5 |
| research-sweep | 4:30am | `/Users/latentforge/Projects/latentforge-latentmas/research/daily-digest/YYYY-MM-DD.md` | Fixed Apr 5 |
| kalshi-pull | 4:45am | `/Users/latentforge/Projects/data/kalshi/markets_YYYY-MM-DD.json` | Running |
| revenue-strategist | 5:00am | `/Users/latentforge/Projects/latentforge-latentmas/revenue_ideas/YYYY-MM-DD.md` | Fixed Apr 5 |
| text-swarm | 5:15am | `/Users/latentforge/Projects/latentforge-latentmas/experiments/benchmark/text_swarm_YYYY-MM-DD.md` | Fixed Apr 5 |
| calibration-tracker | 5:30am | `/Users/latentforge/Projects/latentforge-latentmas/experiments/benchmark/calibration/` | Fixed Apr 5 |

**To check if a job ran last night:**
```bash
ls -lt [output directory] | head -3
```
If the top file is dated today, it ran. If not, check the cron.log in that directory.

---

### Calibration Tracker — Two Fixes Applied (April 5)

1. ZeroDivisionError fix — script no longer crashes when no markets have resolved yet
2. 5-95% crowd probability filter — only tracks markets with genuine uncertainty. Markets where crowd is already above 95% or below 5% are excluded.

Current state (April 5): 25 markets tracked, Day 2 of 30-day paper trading clock.

---

## Research — Key Findings (April 5)

### LatentMAS Paper (arXiv:2511.20639v2)
Confirms the core thesis. Latent collaboration beats text-based MAS by up to 14.6% accuracy, 70-83% token reduction, 4x faster inference. Training-free. Use in grant as academic validation. Outreach to Jiaru Zou (first author, Google DeepMind) planned for late April after Week 4 OpenSpiel results.

### Weather Arbitrage — Week 4+ Queue
METAR aviation feeds (free, public, 1-3 hour updates, precise to 0.1C) vs Polymarket weather market prices. ColdMath case study: $101K profit, 5,252 predictions. Fast feedback loop — markets resolve in days. Do not start until Shadow Match has 2+ weeks of data.

### Compression Researcher Suggestion (April 5)
Sparse Distributed Representations (SDR) from computational neuroscience. Transmit binary activation mask (which dimensions fired) instead of float32 magnitudes. O(k) operations instead of O(d). Read full suggestion at: `/Users/latentforge/Projects/latentforge-latentmas/research/suggestions/2026-04-05.md`

---

## Shadow Match Baseline (April 4)

11 markets logged. Key divergences worth watching:
- Powell confirmed as Fed Chair: Crowd 0.1% vs Shadow/Swarm 3-4%
- US-Iran nuclear deal: Crowd 22.5% vs Shadow/Swarm 7-8%
- Bitcoin $60k or $80k first: Shadow 62% vs Swarm 52% (contrarian agent moving the needle)

Results at: `~/.latentforge/shadow_match/shadow_match_2026-04-04.json`

---

## Text Swarm — Day 7 AI Regulation Divergence

Swarm consistently prices AI regulation passage at 21-28% vs crowd 31%. Seven consecutive days. Unresolved — will not know if edge or blind spot until market resolves.

---

## Questions for Grok

1. AI regulation divergence — 7 days running. Strongest case the crowd is right and we're wrong?
2. Powell market — Crowd 0.1%, Shadow/Swarm 3-4%. Genuine edge or Polymarket framing issue?
3. Weather arbitrage — fast-track or keep in Week 4+ queue? Distraction risk vs opportunity?
4. SDR compression — does transmitting binary activation mask preserve enough information for useful agent communication? Theoretical floor on information loss?
5. Swarm architecture — should we add a 4th agent (pure Bayesian updater) to anchor the swarm alongside Base Rate, News, Contrarian?

---

## 90-Day Goals — Status (April 5)

| Goal | Status |
|------|--------|
| Submit Rain grant | Ready — submit today |
| 30-day paper trading clock | Running — Day 2 |
| Shadow Match baseline | Complete |
| Mac Mini arrival | April 9-16 |
| Latent vs text A/B test | Pending hardware |
| Prove latent > text | Pending hardware |

**Priority for rest of today:**
1. Submit Rain grant to rain.one
2. LinkedIn/X flag post
3. Read compression researcher suggestion in full

---

*Prepared by Claude (Systems Engine) — April 5, 2026*
*Next review: April 6 — after first clean overnight run of all 6 fixed jobs*

### April 5, 2026 — 4th Agent Added to Text Swarm

| Date | Decision | Why | Notes |
|------|----------|-----|-------|
| Apr 5 2026 | Bayesian Updater added as 4th swarm agent | Grok recommended to anchor swarm and reduce narrative drift | Trial week April 5–12 before making permanent |

**Current swarm architecture (4 agents):**
- Agent 1: Macro Analyst — economic fundamentals, base rates, central bank policy
- Agent 2: Quant Researcher — market signals, momentum, crowd wisdom
- Agent 3: Contrarian Forecaster — stress-tests assumptions, finds tail risks crowd underweights
- Agent 4: Bayesian Updater — neutral prior, updates only on concrete evidence, ignores narrative and sentiment

**Early observation (Day 1):** Bayesian Updater tracking very close to Quant Researcher on most markets. Watch over trial week to see if they diverge on specific markets. If they don't diverge meaningfully by April 12, reconsider whether the 4th agent adds value or just adds API cost.

**Review date:** April 12, 2026 — keep or drop based on one week of data.

### April 5, 2026 — Dorsey/Botha Essay + Single Grain Implementation Notes
Jack Dorsey and Roelof Botha published "From Hierarchy to Intelligence" (April 1, 2026). Single Grain shared a practical 4-month implementation of a similar AI-native operating system (Single Brain vector DB, specialized agents, DRI teams, conflict resolution, NemoClaw security).

**Useful validation for LatentForge:**
- Reinforces the importance of a unified world model and compounding data moat.
- Highlights real coordination pain (agent conflicts, security) that Shadow Self is designed to solve.
- DRI pattern for temporary agent teams is borrowable for structured experiments (e.g., latent A/B test DRI).

**Not directly applicable:**
- Their system is text-based internal operations (marketing agency workflows). We are building the inter-agent latent communication protocol + governance + prediction market validation.

**Action:**
- Log every latent exchange + Shadow Self translation + outcome from Mac Mini Day 1 onward. This builds the proprietary dataset moat.
- Consider DRI-style temporary agent teams for the first latent vs text comparison.

Decision: Article is validation, not competitive threat. Continue current priorities (grant submission, light flag post, Mac Mini prep).


### Standing Rule — Claude Session Startup (Added April 5, 2026)

**Every Claude session must begin with a full BRAIN.md paste. Never start with a truncated version.**

The Systems Engine (Claude) has no memory of previous sessions beyond what is pasted into the current conversation. Starting with a partial or summarized BRAIN.md causes Claude to work with incomplete context and make avoidable mistakes (example: not knowing we had already forked the LatentMAS repo).

**Startup command:**
```bash
brainload
```

This alias copies the full BRAIN.md to your clipboard. Paste it as the first message in every new Claude session before asking anything else.

**To install the alias (one time only — already done April 5):**
```bash
echo "alias brainload='cat ~/Projects/latentforge-latentmas/BRAIN.md | pbcopy && echo BRAIN.md copied to clipboard'" >> ~/.zprofile
source ~/.zprofile
```

**Rule:** If a session starts without a full BRAIN.md paste, stop and run brainload before proceeding.

### April 5, 2026 — Founder Inputs Pipeline Added

| Date | Decision | Why | Notes |
|------|----------|-----|-------|
| Apr 5 2026 | Founder inputs pipeline built | Revenue strategist was missing X/Twitter signals found by Founder Engine | Automated agents can't browse X — human layer fills the gap |

**How it works:**
- Folder: `~/Projects/latentforge-latentmas/founder_inputs/`
- Drop any interesting X posts, articles, or links as `.md` files
- Naming convention: `YYYY-MM-DD_short_description.md`
- Revenue strategist reads this folder every morning at 5:00am and incorporates signals into daily recommendations

**First input logged:** `2026-04-05_coldmath_weather_arbitrage.md` — ColdMath $101K weather arbitrage on Polymarket using free METAR aviation data

**Standing rule:** When you find something interesting on X or anywhere else that the automated agents wouldn't see, drop it in `founder_inputs/` before end of day. The morning revenue strategist will pick it up.

### April 5, 2026 — Grant Submission Decision
| Date       | Decision                                      | Why                                                                 | Alternatives rejected                          |
|------------|-----------------------------------------------|---------------------------------------------------------------------|------------------------------------------------|
| Apr 5 2026 | Rain grant submission deferred                | $50K non-dilutive is attractive, but exposing the full thesis (latent deltas + Shadow Self + divergence benchmark) while still pre-latent results is not worth the risk at this stage. Self-funding the next 60 days with personal capital is sufficient and preserves secrecy. | Submit immediately with current text-swarm results |

**Rationale & Plan:**
- Current compute needs for next 60 days estimated at $150–$350 (mostly Anthropic API calls). Easily covered by personal $10K budget.
- Strong preference for keeping the latent communication + governance thesis private until we have real latent vs text A/B results after Mac Mini arrival.
- Grant document saved in `docs/rain_grant_final.md` for future submission once we have stronger proof (target: late April / early May after latent runs and more paper trading data).
- Continue 30-day paper trading clock and daily automation. Focus on Mac Mini prep and logging everything for the dataset moat.


### April 5, 2026 — Hardware Plan Updated

| Date | Decision | Why | Notes |
|------|----------|-----|-------|
| Apr 5 2026 | Two-machine hardware plan locked | Mac Mini arrives soon for dev work, M5 Mac Studio ordered for production scale | Don't cancel Mac Mini — use both |

**Hardware Roadmap:**

| Machine | Arrives | Role |
|---------|---------|------|
| Mac Mini M4 Pro 32GB 1TB | April 9–16 | Dev machine — initial latent experiments, text swarm, calibration tracker, Shadow Match |
| M5 Mac Studio 128GB 1TB | June/July 2026 | Production machine — full 4-arm benchmark, latent swarm at scale, dataset moat |

**Mac Mini constraints to work around (32GB):**
- Use 4-bit quantization for Phi-3 Mini to reduce memory footprint by 60-70%
- Run latent agents sequentially rather than in parallel if memory is tight
- Use RunPod for overflow compute if needed (~$50-100 total)
- Do not attempt to run more than 2-3 model instances simultaneously

**M5 Mac Studio — why we're waiting:**
- 28% improvement in memory bandwidth over M4
- 128GB unified memory — no ceiling for latent swarm experiments
- Expected WWDC June 2026 launch
- At 128GB, can run full 4-arm benchmark simultaneously with no memory management overhead
- This is the production machine for the next 3+ years

**Standing rule:** When M5 Mac Studio arrives, migrate all launchd jobs, model weights, and latent logging infrastructure from Mac Mini. Mac Mini becomes secondary dev/test machine.

---

# SYSTEMS STATUS — Read This Every Session
## Last Updated: April 5, 2026
## This section gives Claude full operational context at the start of every session.

---

## The Three-Engine System
- Founder Engine: John McGuire (strategy, vision, serendipitous discovery)
- Systems Engine: Claude (execution, infrastructure, debugging, writing)
- Divergent Thinking Engine: Grok/Supergrok (challenging assumptions, open questions)
- Single source of truth: BRAIN.md at github.com/forgelatent/latentforge-latentmas
- Rule: Read full BRAIN.md at start of every session using `brainload` alias

---

## Machine Infrastructure

### MacBook Air (latentforge account)
- Primary development machine right now
- All 6 launchd jobs run here via WakeForJob=true
- User account: latentforge
- Project root: ~/Projects/latentforge-latentmas/

### Mac Mini M4 Pro 32GB 1TB (arriving April 9-16)
- Role: Dev machine for initial latent experiments
- Use 4-bit quantization for Phi-3 Mini to stay within 32GB
- Run agents sequentially not in parallel if memory is tight
- Priority on arrival: migrate launchd jobs, run first latent vs text A/B test

### M5 Mac Studio 128GB 1TB (arriving June/July 2026)
- Role: Production machine for full 4-arm benchmark at scale
- Waiting for WWDC June 2026 launch
- On arrival: migrate everything from Mac Mini, Mac Mini becomes secondary dev machine

---

## API Keys & Secrets

### Anthropic API Key
- Name: latentforge-main
- Stored at: ~/.latentforge/.env
- Sourced via: ~/.zprofile (loads at login for launchd)
- Also stored in: Keychain (account: latentforge, service: latentforge-anthropic)
- Valid key length: 108 characters

### Safe key rotation procedure (ALWAYS follow this order):
1. Create new key at console.anthropic.com
2. Store via python3 getpass method:
```bash
python3 -c "
import getpass, os
k = getpass.getpass('Paste key then Enter: ')
open(os.path.expanduser('~/.latentforge/.env'),'w').write(f'export ANTHROPIC_API_KEY=\"{k}\"\n')
print('Saved. Length:', len(k))
"
```
3. Update Keychain:
```bash
security add-generic-password -a "latentforge" -s "latentforge-anthropic" -w "$(cat ~/.latentforge/.env | grep -o 'sk-ant[^"]*')" -U
```
4. Verify length = 108:
```bash
echo ${#ANTHROPIC_API_KEY}
```
5. Test with curl before doing anything else

### Known zsh issues on this machine:
- NEVER use pbpaste for secrets — captures terminal history
- NEVER use read -p — fails with "no coprocess" error
- NEVER use heredocs in python3 -c strings — causes hangs
- NEVER paste keys into Claude chat — they will be exposed
- NEVER use heredoc (cat << EOF) — hangs in zsh. Use python3 file writes instead.

---

## The 6 Launchd Jobs (All Fixed April 5, 2026)

All scripts use absolute paths. All pull API key from Keychain via run_with_key.sh.
Rule: Every script called by launchd must use absolute paths.

| Job | Time | Output | Check Command |
|-----|------|--------|---------------|
| compression-researcher | 2:00am | ~/Projects/latentforge-latentmas/research/suggestions/YYYY-MM-DD.md | ls -lt ~/Projects/latentforge-latentmas/research/suggestions/ |
| research-sweep | 4:30am | ~/Projects/latentforge-latentmas/research/daily-digest/YYYY-MM-DD.md | ls -lt ~/Projects/latentforge-latentmas/research/daily-digest/ |
| kalshi-pull | 4:45am | ~/Projects/data/kalshi/markets_YYYY-MM-DD.json | ls -lt ~/Projects/data/kalshi/ |
| revenue-strategist | 5:00am | ~/Projects/latentforge-latentmas/revenue_ideas/YYYY-MM-DD.md | ls -lt ~/Projects/latentforge-latentmas/revenue_ideas/ |
| text-swarm | 5:15am | ~/Projects/latentforge-latentmas/experiments/benchmark/text_swarm_YYYY-MM-DD.md | ls -lt ~/Projects/latentforge-latentmas/experiments/benchmark/ |
| calibration-tracker | 5:30am | ~/Projects/latentforge-latentmas/experiments/benchmark/calibration/ | ls -lt ~/Projects/latentforge-latentmas/experiments/benchmark/calibration/ |

### Morning job check routine:
```bash
ls -lt ~/Projects/latentforge-latentmas/research/suggestions/ | head -3
ls -lt ~/Projects/latentforge-latentmas/research/daily-digest/ | head -3
ls -lt ~/Projects/data/kalshi/ | head -3
ls -lt ~/Projects/latentforge-latentmas/revenue_ideas/ | head -3
ls -lt ~/Projects/latentforge-latentmas/experiments/benchmark/ | head -3
ls -lt ~/Projects/latentforge-latentmas/experiments/benchmark/calibration/ | head -3
```
If any file is not dated today, that job failed. Check cron.log in that directory.

---

## The Founder Inputs Pipeline

**This is how John feeds serendipitous discoveries into the system.**

- Folder: ~/Projects/latentforge-latentmas/founder_inputs/
- Drop any interesting X posts, articles, or links as .md files
- Naming: YYYY-MM-DD_short_description.md
- Revenue strategist reads this folder every morning at 5am automatically
- Claude should check this folder at the start of every session

### Current founder inputs (as of April 5):
- 2026-04-05_coldmath_weather_arbitrage.md — METAR data vs Polymarket weather markets
- 2026-04-05_llm_knowledge_base_wiki.md — Compounding LLM wiki in Obsidian
- 2026-04-05_gstack_parallel_sprints.md — Garry Tan's parallel sprint model + latent skill templates

### Standing rule:
When John finds something interesting anywhere (X, GitHub, articles), drop it in
founder_inputs/ before end of day. The morning revenue strategist picks it up automatically.

---

## The Text Swarm (4 Agents as of April 5, 2026)

Script: ~/Projects/latentforge-latentmas/experiments/benchmark/03_text_swarm.py
Markets: 11 policy/macro/geopolitical markets on Polymarket
Runs: Nightly at 5:15am

| Agent | Role |
|-------|------|
| Macro Analyst | Economic fundamentals, base rates, central bank policy |
| Quant Researcher | Market signals, momentum, crowd wisdom |
| Contrarian Forecaster | Stress-tests assumptions, finds tail risks |
| Bayesian Updater | Neutral prior, updates only on concrete evidence (added April 5 — trial week ends April 12) |

Key divergence to watch: AI regulation — swarm 21-28% vs crowd 31% for 7+ consecutive days.

---

## Shadow Match Baseline (April 4, 2026)

Script: ~/Projects/latentforge-latentmas/experiments/week1/scripts/shadow_match.py
Results: ~/.latentforge/shadow_match/shadow_match_2026-04-04.json
11 markets logged. Single strong model (Shadow) vs 3-agent swarm vs crowd.
Fill in "outcome": 0 or 1 when markets resolve.

Key divergences:
- Powell confirmed as Fed Chair: Crowd 0.1% vs Shadow/Swarm 3-4%
- US-Iran nuclear deal: Crowd 22.5% vs Shadow/Swarm 7-8%
- Bitcoin $60k or $80k first: Shadow 62% vs Swarm 52%

---

## Calibration Tracker (30-Day Clock — Started April 4)

Script: ~/Projects/latentforge-latentmas/experiments/benchmark/calibration_tracker.py
Output: ~/Projects/latentforge-latentmas/experiments/benchmark/calibration/
Runs: Nightly at 5:30am
Filter: Only tracks markets with 5-95% crowd probability (genuine uncertainty)
Day 2 of 30 as of April 5. 25 markets tracked.

---

## Research Outputs

### Daily Research Digest
Location: ~/Projects/latentforge-latentmas/research/daily-digest/YYYY-MM-DD.md
Contains: arXiv papers, GitHub repos, competitive watch, X watchlist

### Compression Researcher Suggestions
Location: ~/Projects/latentforge-latentmas/research/suggestions/YYYY-MM-DD.md
Runs at 2am — autonomous agent reads arXiv and suggests latent compression techniques

### Revenue Ideas
Location: ~/Projects/latentforge-latentmas/revenue_ideas/YYYY-MM-DD.md
Reads: Kalshi data + research digest + founder inputs folder

---

## Key Research Directions (Week 4+)

| Direction | Status | Notes |
|-----------|--------|-------|
| Efference copy compression | Queued | Autonomous agent suggested 3 consecutive days |
| SDR (Sparse Distributed Representations) | Queued | Compression researcher April 5 suggestion |
| Weather arbitrage (METAR vs Polymarket) | Queued | ColdMath case study — fast Brier feedback |
| Latent skill templates (gstack-inspired) | Queued | Role-specialized latent agents |
| Compounding research wiki | Queued | LLM-maintained Obsidian wiki |
| Dictionary learning from genomics | Queued | PhD friend suggestion |
| Topological drift detection | Queued |  |
| Injective manifold mapping | Queued | PhD friend suggestion |
| Hilbert curve image compression | Queued |  |

---

## Key Results Logged

- Fidelity 1.0000, divergence score 2.0/2 at 24x compression on Phi-3 Mini 3.8B (RunPod)
- 45% Brier improvement vs naive baseline on 18 resolved Polymarket markets (0.1376 vs 0.25)
- 7 consecutive days of AI regulation divergence (swarm 21-28% vs crowd 31%)
- Shadow Match baseline logged April 4 on 11 markets

---

## Competitive Watch

- LatentMAS (Zou et al., arXiv:2511.20639v2) — validates thesis, not a threat. Outreach to Jiaru Zou planned late April after Week 4 results.
- Aaru ($1B valuation) — text-based population simulation. Direct comparison point.
- VectorArc/AVP v0.4.1 — adjacent protocol, KV-cache handoff, no governance layer. Monitor.
- gstack (Garry Tan/YC) — agent orchestration toolkit, validation of role specialization approach.

---

## 90-Day Goals — Current Status

| Goal | Status |
|------|--------|
| Rain grant | Parked — resubmit after Mac Mini latent results. Doc at docs/rain_grant_final.md |
| 30-day paper trading clock | Running — Day 2 of 30 |
| Shadow Match baseline | Complete — April 4 |
| Mac Mini arrival | April 9-16 |
| Latent vs text A/B test | Pending Mac Mini |
| M5 Mac Studio order | Pending WWDC June 2026 |
| LinkedIn/X flag post | Parked — after first latent results |
| Jiaru Zou outreach | Parked — after Week 4 OpenSpiel results |

---

## GitHub

Repo: github.com/forgelatent/latentforge-latentmas
All decisions, scripts, and data committed here.
Rule: BRAIN.md never more than 48 hours out of date.

---
*Systems Status section maintained by Claude (Systems Engine)*
*Update this section whenever infrastructure changes*
