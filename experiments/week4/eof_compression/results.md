# EOF vs Top-k Compression Proxy Test
Date: 2026-04-12T12:29:39.974965
Seed: 42 | Top-k k: 128 | EOF variance: 0.95

## Vector Collection
Model: claude-sonnet-4-20250514
Proxy: character n-gram frequency vectors (dim=1024)
NOTE: Coarse proxy — Mac Mini will use real Phi-3 hidden states

Vectors collected: 70
Vector shape: (70, 1024)


## Results

### Top-k Sparsity Baseline (k=128)
- Avg MSE: 0.000242
- Avg cosine distance: 0.132777
- Coefficients used: 128.0

### EOF Adaptive Compression (95% variance)
- Avg MSE: 0.000710
- Avg cosine distance: 0.474239
- Avg components: 18.0
- Min/Max components: 18/18

### Content-Adaptive Behavior by Group
- ai_regulation: avg 63.0 components (n=10)
- crypto_markets: avg 63.0 components (n=10)
- geopolitics: avg 63.0 components (n=10)
- economics: avg 63.0 components (n=10)
- technology: avg 63.0 components (n=10)
- elections: avg 63.0 components (n=10)
- mixed_control: avg 63.0 components (n=10)

### Verdict
- H1 (lower reconstruction error): FAIL
- H2 (content-adaptive): FAIL
- Top-k MSE: 0.000242
- EOF MSE: 0.000710
- Similar groups avg components: 63.0
- Diverse groups avg components: 63.0
- EOF efficiency ratio vs top-k: 7.11x

Note: Proxy test using Claude API character n-gram vectors (dim=1024).
Retest with real Phi-3 hidden states on Mac Mini for citable result.

