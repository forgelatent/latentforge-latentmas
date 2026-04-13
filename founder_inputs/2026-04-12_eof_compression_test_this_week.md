# Compression Researcher — April 12 Suggestion Worth Testing This Week

## Eigenmode Decomposition / EOF (Suggestion 3 from 2026-04-12.md)

Source: compression-researcher agent, April 12 2026
Priority: Test this week — CPU-only, no Mac Mini required

Core idea: Top-k sparsity is coordinate-aligned but transformer latent space is
deeply correlated. EOF decomposition finds the actual axes of variance in your
specific agent communication history, not the axes the model was trained with.

Adaptive truncation: bandwidth proportional to semantic content.
- Agents agreeing = fewer coefficients transmitted
- Agents genuinely diverging = more coefficients automatically
- This makes compression content-adaptive in a way fixed-k sparsity is not

Test protocol (numpy only, no GPU):
1. Collect 100+ latent-proxy vectors from Claude API
2. Compute rolling-window PCA on delta sequence (window=20, step=1)
3. For each new delta: encode as EOF coefficients, truncate at 95% variance
4. Decode, measure reconstruction error vs top-128 sparsity at matched ratio
5. Verify: fewer modes required when prompts are semantically similar

If EOF beats top-k at matched compression ratio: add to benchmark report
before Mac Mini arrives. That is a result we can cite independently of latent runs.

Related: Suggestion 1 (Sparse Predictive Coding) queues behind efference copy
on Mac Mini. Suggestion 2 (Topological Homology) is Shadow Self upgrade Week 4+.
