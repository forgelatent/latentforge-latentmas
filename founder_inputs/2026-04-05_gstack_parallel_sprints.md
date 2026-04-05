# gstack — Garry Tan's Claude Code Setup — April 5, 2026

Source: GitHub — https://github.com/garrytan/gstack
Author: Garry Tan, President & CEO of Y Combinator
Stars: 54,000+ (as of April 5, 2026)

## What it is
A collection of Claude Code slash commands that turn Claude into a virtual
engineering team — CEO agent, designer, eng manager, QA lead, security
officer, release engineer. 23 specialized skills invoked via slash commands.
Enforces a structured sprint: Think → Plan → Build → Review → Test → Ship → Reflect.
Garry Tan claims 600,000+ lines of production code in 60 days running this
setup part-time while running YC full-time. Integrates with OpenClaw (which
LatentForge already uses).

## Key insight 1 — Latent skill templates (Grok's flag — highest value)
Gstack defines roles via SKILL.md markdown templates. Each skill's output
feeds into the next. The key LatentForge adaptation: define latent versions
of these roles where the prompt encodes the specialization but the actual
inter-agent communication happens in latent space instead of text.

Example: a latent CEO agent and latent QA agent that communicate via deltas
instead of text prompts. This could be a fast way to test latent coordination
before building a heavy swarm — lightweight role specialization without full
multi-agent overhead.

## Key insight 2 — Parallel sprints
Garry runs 10-15 Claude Code sessions simultaneously using Conductor
(conductor.build). Each session runs in an isolated workspace. Maps directly
to the 4-arm benchmark:
- Arm 1 (text swarm) in one session
- Arm 2 (shadow model) in another
- Arm 3 (latent swarm) in another
- Arm 4 (latent shadow) in another
- Calibration tracker scoring all four in a fifth session

## Key insight 3 — Safety and governance validation
Gstack has /guard, /freeze, /careful commands that prevent destructive
actions. Also uses NemoClaw for sandboxing. Directly validates the Shadow
Self / KL-Divergence Watchdog direction. Adopt similar policy enforcement
patterns when Mac Studio arrives.

## Key insight 4 — Sprint discipline for experiments
The Think-Plan-Build-Review-Test-Ship-Reflect cycle maps to Mac Mini
experiment discipline. Define clear stages for every latent experiment
so nothing is skipped. Borrow for the 30-day paper trading calibration run.

## What is NOT relevant right now
Most of gstack is for shipping product code. LatentForge is a research
project. The overhead would slow things down at this stage.

## Bottom line
Validation and inspiration, not a competitor. Role specialization +
structured workflows + safety guardrails work in practice. The latent
skill template idea is the most novel angle — worth prototyping on Mac Mini.

## Priority: Week 4+ — after Mac Mini arrives
## Action items:
- Design latent skill templates inspired by SKILL.md
- Evaluate Conductor for parallel latent experiment orchestration
- Adopt lightweight sprint structure for 30-day paper trading discipline
