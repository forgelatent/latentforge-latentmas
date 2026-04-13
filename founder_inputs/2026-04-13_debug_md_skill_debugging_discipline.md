# DEBUG.md Skill — Persistent Debugging Rules for Claude Code

Source: https://x.com/ShenHuang_/status/2043469166418735204
Type: Claude Code skill / debugging discipline

The 4 rules:
1. List all assumptions before changing any code
2. Each experiment: change at most 5 lines of code
3. Write all evidence (hypotheses, counter-evidence, results) to
   a persistent DEBUG.md file — prevents context loss across long sessions
4. If the same direction fails twice, force a completely new hypothesis

Why relevant to LatentForge Mac Mini work:
- echo_test.py debugging sessions may run long — context compression risk
- Silicon delta verification (Phase 7) may surface unexpected issues
- Latent bridge handoffs are subtle — assumptions must be explicit
- Rule 2 reinforces Karpathy Surgical Changes principle
- Rule 3 directly addresses context loss during multi-hour debug sessions

Relationship to andrej-karpathy-skills:
- Karpathy = coding discipline (Simplicity First, Surgical Changes,
  Think Before Coding, Goal-Driven Execution)
- DEBUG.md skill = debugging discipline (assumptions explicit, evidence
  persistent, max 5 lines per change, new hypothesis on repeated failure)
- These are complementary layers, not redundant

Mac Mini Day 1 / Week 1: Install alongside Karpathy skills.
Consider merging into a single CLAUDE.md + DEBUG.md combined guidelines file.
Do not add persistent DEBUG.md files to the experiments/ directory —
keep them in a separate debug/ folder to avoid polluting benchmark logs.

Thesis impact: neutral — tooling improvement, no thesis impact
Motor-car linkage: Governance (debugging discipline = experiment integrity)
