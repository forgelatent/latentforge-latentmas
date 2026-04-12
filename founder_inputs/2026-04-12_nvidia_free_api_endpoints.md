# NVIDIA Free API Endpoints — Test on Mac Mini

Source: build.nvidia.com (legitimate NVIDIA platform)
Thread: @theRayW / @AdolfoUsier on X, April 2026

What it is:
- Free serverless API endpoints for frontier models
- OpenAI-compatible (/v1/chat/completions)
- Free credits on signup (~1000-5000, 40 RPM free tier)
- Models: MiniMax M2.7 (230B MoE), GLM-5 (744B MoE), Kimi K2.5
- API key format: nvapi-...
- Generate key at: build.nvidia.com

Why relevant:
- Zero-cost alternative/fallback to Anthropic API for text swarm
- Model diversity for swarm agents (different reasoning styles)
- MiniMax M2.7 strong for agentic tasks — potential swarm agent
- GLM-5 for deep reasoning — potential Shadow replacement

Decision: Park until Mac Mini.
Do NOT add to live swarm config before migration — risk of overnight
failure during final stretch of 30-day paper trading clock.

Mac Mini Day 1: Sign up, get nvapi- key, run one test call,
compare output quality vs claude-sonnet-4-6 on same market prompt.
If competitive: add as configured fallback in text swarm.

Potential integration: Replace one swarm agent with MiniMax M2.7
to add genuine model diversity (not just role diversity).
