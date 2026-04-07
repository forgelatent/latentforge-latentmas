# VC Chief of Staff on OpenClaw — April 6, 2026

Source: LinkedIn article (VC author, anonymous)
Topic: How a VC built an AI chief of staff on OpenClaw that compounds over time

## Key insights for LatentForge

### 1. Memory architecture we should build toward
The author uses two layers:
- Daily notes: memory/YYYY-MM-DD.md — raw log of everything that happened
- Long-term memory: MEMORY.md — curated synthesis updated periodically

We have: commercialization_thesis.md (running thesis) + daily agent outputs.
Gap: our agents don't synthesize across days into a unified picture yet.
The commercialization agent is the closest — it reads its own previous output.
Future upgrade: add a weekly synthesis pass that reads all daily outputs and updates a running LATENTFORGE_MEMORY.md.

### 2. The Kaizen loop — what our commercialization agent should do weekly
Every Friday his system scans what other builders are doing, surfaces improvement suggestions, and they review together on Sunday.
Our commercialization agent runs nightly but doesn't do competitive scanning.
Potential upgrade: add a weekly "what changed in the ecosystem this week and how does it affect our thesis" pass to the commercialization agent prompt.
Low effort — just update the system prompt to include this on Fridays.

### 3. LLM vs script separation rule — formalize in BRAIN.md
His rule: LLMs handle judgment, scripts handle everything else.
Anything deterministic (reading files, calling APIs, comparing timestamps) lives in Python.
LLM layer handles synthesis, prioritization, drafting, reasoning.
We are already doing this — but worth making explicit as a standing architecture rule.

### 4. System gets better on a cadence, not when you remember to tinker
The Kaizen loop makes improvement disciplined rather than ad hoc.
This is what the commercialization agent's running thesis is meant to do — but we should be more intentional about a weekly review of agent outputs and system performance.

### 5. "A smaller system you trust will always beat a bigger one you route around"
Good check for us: are we building things we actually use every morning? 
The 8-agent overnight system is working. Don't add more until existing agents prove their value.
Review date for Bayesian Updater: April 12. Cut it if it's not diverging from Quant Researcher.

## Priority
Week 4+ — after Mac Mini latent experiments are running.
Near-term action: update commercialization agent prompt to include weekly Kaizen scan on Fridays.
