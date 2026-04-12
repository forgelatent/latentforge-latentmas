# Google TimesFM — Time Series Foundation Model (Mac Mini Queue)

Repo: https://github.com/google-research/timesfm
Stars: 16.5k | Apache-2.0 | v2.5 (200M params, Sept 2025)
Last updated: April 2 2026

What it does:
- Zero-shot time series forecasting (no fine-tuning required)
- 16k context length, probabilistic output with quantile head
- PyTorch or JAX backend — runs locally on Mac Mini
- Trained on 100B+ real-world time points (sales, energy, traffic, prices)

Honest fit assessment for LatentForge:
- NOT a natural fit for binary prediction market resolution
- STRONG fit for continuous time series: crypto prices, weather temps,
  volatility, Kalshi/Polymarket odds drift over time
- Best use case: pair with @polydao weather bot strategy — METAR temps
  are exactly the continuous time series TimesFM was built for
- Could model Polymarket crowd probability drift as a time series
  but this is a stretch use case, not the intended one

Best integration path (Week 4+ after Mac Mini):
1. Pull 30-day Polymarket odds history for AI regulation market
2. Run TimesFM to forecast next 7-day probability trajectory
3. Compare trajectory to text swarm daily estimates
4. If TimesFM adds signal on weather markets specifically — integrate
   as a dedicated weather market forecasting arm

Install (Mac Mini):
  pip install timesfm[torch]  # PyTorch backend recommended for Apple Silicon

Do not add to live swarm config before testing.
