# Sportka UBT Experiment Report

**Author**: Ing. David Jaroš  
**Status**: Implementation complete — awaiting real lottery data for full evaluation  
**Date**: 2025

---

## Overview

This report documents the design, implementation, and testing of the Sportka
lottery prediction experiment with corrected probability scaling, leakage
prevention, and UBT theta-transform integration.

Sportka is the Czech/Slovak lottery: **7 numbers drawn from 1–49** per draw
(6 main numbers + 1 bonus).  The experiment tests whether any predictor
can outperform a uniform random baseline.

---

## Critical Fixes Applied

### Fix 1: Probability Scaling

**Problem**: Earlier implementations normalised probability vectors to sum to 1
(single-class convention), which is incorrect for multi-label prediction.

**Correct rule**: Each number's probability should be interpreted as the
probability that it appears in the next draw.  For a pool of 49 numbers with
7 drawn per round:

```
p(number k appears) = count_k / n_draws
Expected sum over 49 numbers ≈ 7
```

| Predictor | Correct denominator | Sum |
|-----------|-------------------|-----|
| RandomPredictor | — | 7/49 × 49 = 7.000 exactly |
| GlobalFreqPredictor | `count_k / n_draws` | ≈ 7 |
| RollingFreqPredictor | `count_k_in_window / n_draws_in_window` | ≈ 7 |
| ExpDecayFreqPredictor | `weighted_count_k / total_weight` | ≈ 7 |

**Previously wrong** (produces sum ≈ 1):
- `freq / total_hits` (GlobalFreq)
- `count / (window × 7)` (Rolling)
- `weighted_count / (total_weight × 7)` (ExpDecay)

### Fix 2: Rolling Predictor Offset

**Problem**: Hardcoded offset of `49+13` in `RollingFreqPredictor` did not
account for different feature group combinations.

**Fix**: Removed hardcoded offset.  Introduced `get_feature_slice(groups, name)`
to compute the correct column slice for any combination of feature groups.

```python
# Correct usage:
sl = get_feature_slice(["base", "winding"], "winding")
rolling_features = X[:, sl]
```

### Fix 3: Data Leakage Prevention

**Problem**: `winding_history_features` computed `global_freq` from the entire
provided DataFrame.  When applied to validation/test split, future rows
contaminated the frequency estimates.

**Fix**: All feature builders now accept `train_max_index` parameter:

```python
global_freq = global_freq_features(df, train_max_index=train_end)
```

The `build_walk_forward_features` function builds features for each split
using only chronologically available information:

- Training features: use training data only
- Validation row i features: use training data + val rows 0..i-1
- Test row i features: use training + val data + test rows 0..i-1

### Fix 4: Time Normalisation

**Problem**: `complex_time_features` normalised `draw_index` by `max(split)`,
making train/val/test time scales inconsistent.

**Fix**: Caller passes `t_max_train` (training maximum draw index) to all
feature builders.  Validation and test draws correctly appear at t > 1.0 
on the normalised scale.

```python
t_max_train = float(train_df["draw_index"].max())
feat_val = complex_time_features(val_df, t_max_train=t_max_train)
# val t_norm values are > 1.0 — correctly after training period
```

---

## Implementation Structure

```
sportka/
├── __init__.py
├── features.py           # Feature engineering (corrected)
│   ├── global_freq_features()
│   ├── rolling_freq_features()
│   ├── exp_decay_freq_features()
│   ├── complex_time_features()
│   ├── winding_history_features()
│   ├── build_features()
│   ├── get_feature_slice()
│   └── build_walk_forward_features()   # leakage-safe splits
├── models.py             # Predictors (corrected scaling)
│   ├── RandomPredictor
│   ├── GlobalFreqPredictor
│   ├── RollingFreqPredictor
│   ├── ExpDecayFreqPredictor
│   ├── LogisticPredictor
│   ├── MLPPredictor
│   └── UBTMLPPredictor
├── model.py              # Compatibility shim → models.py
├── evaluation.py         # Metrics + controls
│   ├── brier_score()
│   ├── log_loss_multilabel()
│   ├── top_k_recall()
│   ├── mean_reciprocal_rank()
│   ├── bootstrap_metric()
│   ├── shuffled_label_control()
│   ├── reversed_time_control()
│   └── compare_predictors()
├── ubt_theta_transform.py  # Heat-kernel theta transform (experimental)
├── torus_embedding.py      # Torus embedding of numbers 1–49
├── multiscale_features.py  # Multi-scale feature combinations
├── ubt_bridge.py           # Clean UBT adapter interface
└── experiments/
    ├── run_experiment.py   # Baseline experiment
    └── run_experiment_v2.py  # Full UBT experiment + controls
```

---

## UBT Integration

The UBT theta transform is kept **experimental**.  It is accessed through a
clean adapter interface (`sportka/ubt_bridge.py`) that:

1. Exposes only numpy → numpy functions
2. Contains no speculative text about lottery prediction
3. Can be updated to import from `unified-biquaternion-theory` without changing
   the calling code

```python
from sportka.ubt_bridge import apply_theta_transform, apply_complex_phase

# Smooth a probability matrix with heat-kernel
smoothed = apply_theta_transform(prob_matrix, sigma=3.0)

# Apply imaginary-time phase diffusion
phase_mod = apply_complex_phase(prob_vector, tau_imag=0.5)
```

The `UBTMLPPredictor` uses theta-augmented features in the MLP training pipeline.

---

## Test Results

All 33 unit tests pass:

| Test class | Tests | Status |
|------------|-------|--------|
| TestRandomPredictor | 4 | ✓ pass |
| TestGlobalFreqPredictor | 4 | ✓ pass |
| TestRollingFreqPredictor | 4 | ✓ pass |
| TestExpDecayFreqPredictor | 4 | ✓ pass |
| TestProbabilitySumConsistency | 4 | ✓ pass |
| TestGlobalFreqLeakage | 2 | ✓ pass |
| TestRollingLeakage | 2 | ✓ pass |
| TestTimeNormalisationLeakage | 2 | ✓ pass |
| TestWalkForwardSplits | 3 | ✓ pass |
| TestFeatureSlice | 4 | ✓ pass |

---

## Evaluation Framework

Run the baseline experiment on synthetic data:

```bash
python -m sportka.experiments.run_experiment --draws 1000
```

Run the full UBT experiment with controls:

```bash
python -m sportka.experiments.run_experiment_v2 --draws 1000 \
    --report reports/sportka_ubt_experiment_results.md
```

---

## Signal Assessment (Synthetic Data)

**On synthetic uniform-random data, no predictor should outperform random.**

The correct null-hypothesis baseline is `RandomPredictor` with `prob_sum = 7.000`.

To assess whether a real signal exists:

1. Run the experiment on real Sportka historical data (replace
   `generate_synthetic_draws` with a real data loader)
2. Check whether any model's Brier score CI upper bound is below the
   random baseline CI lower bound
3. Run the shuffled-label and reversed-time controls — if the model
   also performs well in these controls, the result is likely spurious

**Current status**: Real Sportka data not yet loaded.  All evaluation results
are based on synthetic uniform data.  **No signal claim is made.**

---

## Metrics Explanation

| Metric | Lower is better | Notes |
|--------|----------------|-------|
| Brier score | ✓ | MSE of scaled probability vs binary label |
| Log-loss | ✓ | Binary cross-entropy |
| Top-7 recall | ✗ | Fraction of drawn numbers in top-7 predictions |
| MRR | ✗ | Mean reciprocal rank of first drawn number |

All metrics are computed with 95% bootstrap confidence intervals (500 re-samples).

---

## Acceptance Criteria Status

| Criterion | Status |
|-----------|--------|
| RandomPredictor prob sum = 7 | ✓ Implemented and tested |
| GlobalFreq prob sum ≈ 7 | ✓ Implemented and tested |
| RollingFreq prob sum ≈ 7 | ✓ Implemented and tested |
| No validation/test feature uses future rows | ✓ Walk-forward builder |
| Walk-forward split is chronological | ✓ Tested |
| UBT model evaluated against corrected baselines | ✓ UBTMLPPredictor in v2 |
| Report states clearly whether signal exists | ✓ Awaiting real data |
