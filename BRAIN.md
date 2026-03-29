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

