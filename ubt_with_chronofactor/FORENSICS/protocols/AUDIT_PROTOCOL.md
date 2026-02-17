# CMB Forensic Fingerprint - Audit Protocol

**Version**: 2.0 (Court-Grade)  
**Date**: January 2026  
**Status**: Production

## Overview

This document defines the court-grade audit protocol for the CMB forensic fingerprint test. The audit protocol extends the baseline candidate-grade analysis with additional robustness checks designed to eliminate systematic errors and false positives.

## Audit Modes

The audit suite consists of five complementary test modes:

### 1. Baseline Analysis

**Purpose**: Standard TT analysis with best available uncertainties

**Methods**:
- Diagonal whitening: `r_w = (C_obs - C_model) / σ`
- Covariance whitening: `r_w = L^{-1}(C_obs - C_model)` where `C = LL^T`

**Interpretation**:
- Establishes the primary candidate signal
- p < 0.01 → candidate signal
- p < 2.9×10^-7 → strong signal (~5σ)

**Criteria**:
- Best period among locked candidates: Δℓ ∈ {8, 16, 32, 64, 128, 255}
- P-value from Monte Carlo max-statistic null distribution
- Deterministic seed (42) for reproducibility

### 2. Covariance Whitening

**Purpose**: Eliminate correlated noise artifacts

**Why it matters**:
> If the candidate signal arises from correlated noise structure in the covariance matrix (e.g., mode coupling, off-diagonal correlations), whitening with the full covariance will eliminate it.

**Methods**:
- Cholesky decomposition: `C = LL^T`
- Whitening: `r_w = L^{-1} r`
- Ridge regularization if `cond(C) > 10^8`

**Interpretation**:
- **Signal persists**: Whitening reduces Δχ² by <50% → robust signal
- **Signal weakens**: Δχ² reduction 50-90% → borderline, investigate
- **Signal disappears**: Δχ² reduction >90% or p > 0.05 → likely covariance artifact

**Diagnostics**:
- Condition number: `κ(C) = λ_max / λ_min`
- Regularization λ (if applied)
- χ²/dof for units consistency check

### 3. Polarization Channels (EE, TE)

**Purpose**: Verify signal is field-level, not TT-specific artifact

**Why it matters**:
> Instrumental or foreground artifacts typically affect temperature (TT) only. A real structural feature should propagate to polarization channels (EE, TE) with consistent phase.

**Methods**:
- Independent comb test on EE and TE spectra
- Same locked candidate periods
- Same MC null distribution procedure

**Interpretation**:
- **Strong confirmation**: Δℓ = 255 appears in EE or TE with p < 0.01, phase within π/2 of TT
- **Weak confirmation**: Δℓ = 255 appears with p < 0.05, aligned phase
- **No confirmation**: No structure at 255 in polarization
- **Contradiction**: Different best period or opposite phase → TT artifact

**Expected amplitudes**:
- EE amplitude typically 10-30% of TT (polarization suppression)
- TE amplitude variable (can be positive or negative)

### 4. ℓ-Range Ablations

**Purpose**: Detect localized systematics or artifacts

**Why it matters**:
> If the signal arises from a narrow-range artifact (e.g., beam window error, foreground at specific scales), it will disappear when that range is excluded.

**Methods**:
- Pre-defined splits (NOT data-driven):
  - Planck: low (30-250), mid (251-800), high (801-1500), full_low (30-800), full_high (200-1500)
  - WMAP: low (30-200), mid (201-500), high (501-800)
- Run comb test independently on each range
- Recompute null distribution for each range (different ℓ count)

**Interpretation**:
- **Robust**: Δℓ = 255 appears in ≥2 disjoint ranges with p < 0.05
- **Phase consistent**: Max pairwise phase difference < π/2
- **Borderline**: Appears in 1 range only → possible localized artifact
- **Artifact**: Different periods in different ranges → systematic error

**Validation**:
- Each range must have ≥50 multipoles
- Ranges with <50 points are SKIPPED (not forced)

### 5. Synthetic ΛCDM Null

**Purpose**: Measure false positive rate under null hypothesis

**Why it matters**:
> If Δℓ = 255 appears frequently in pure ΛCDM realizations (no signal), the real data detection may be a statistical fluctuation rather than a real feature.

**Methods**:
1. Load ΛCDM model spectrum as "truth"
2. Generate N synthetic observations: `C_obs^(i) = C_model + N(0, Cov)`
3. Run identical comb test on each realization
4. Count frequency of Δℓ = 255 as best period
5. Measure false positive rate at p < 0.01 threshold

**Interpretation**:
- **Low FPR** (<1%): Signal unlikely to be ΛCDM artifact
- **Borderline** (1-5%): Marginal, requires additional data
- **High FPR** (>5%): Signal is likely generic ΛCDM feature → null result

**Recommended trials**:
- Candidate-grade: 100-200 trials (sufficient for FPR ~ 1%)
- Publication-grade: 1000+ trials (for tighter confidence intervals)

## Combined Verdict Criteria

A signal is considered **ROBUST** if ALL of the following hold:

1. ✓ Baseline TT: p < 0.01, Δℓ = 255
2. ✓ Whitening: Signal persists (Δχ² reduction <50%)
3. ✓ Polarization: Appears in ≥1 pol channel with aligned phase OR no pol data available
4. ✓ Ablation: Appears in ≥2 independent ℓ-ranges with phase consistency
5. ✓ Synthetic null: FPR < 5%

A signal **FAILS** audit if ANY of:

- ✗ Signal disappears after whitening (>90% Δχ² reduction)
- ✗ Opposite phase in polarization channels (|Δφ| > π/2)
- ✗ Appears only in 1 ℓ-range
- ✗ FPR > 10% in synthetic null tests

## Whitening Definitions

### None (No Whitening)
```
r = C_obs - C_model
```
Raw residuals, no normalization. Not recommended for statistical tests.

### Diagonal
```
r_w = (C_obs - C_model) / σ
```
Standard normalization by diagonal uncertainties. Assumes uncorrelated errors.

### Covariance Diagonal (cov_diag)
```
r_w = (C_obs - C_model) / sqrt(diag(Cov))
```
Uses diagonal extracted from full covariance. Intermediate option.

### Covariance (Full Whitening)
```
C = L L^T  (Cholesky)
r_w = L^{-1} (C_obs - C_model)
```
Full whitening via Cholesky solve. Decorrelates errors. **Recommended for court-grade.**

**Chi-squared invariance**:
```
χ² = r^T C^{-1} r = ||r_w||²
```

## Regularization Protocol

When `cond(C) > 10^8` or matrix is not positive definite:

1. **Symmetrization**: If `max|C - C^T| < 10^-6 * max|C|`, auto-symmetrize
2. **Ridge regularization**: Add `λI` where:
   ```
   λ = (λ_max - κ_target * λ_min) / (κ_target - 1)
   ```
   with κ_target = 10^8 (default)

3. **Logging**: Record `λ` in JSON metadata
4. **Warning**: Emit warning to user about regularization

**Never**:
- Use explicit matrix inversion (`C^{-1}`)
- Silently modify covariance without logging
- Drop to diagonal without user knowledge

## Output Schema

All audit results must include:

### JSON Metadata
```json
{
  "whiten_mode": "covariance",
  "whitening_metadata": {
    "cov_metadata": {
      "condition_number": 1.23e6,
      "is_positive_definite": true,
      "is_symmetric": true
    },
    "regularization_used": false,
    "lambda_ridge": null,
    "chi2_per_dof": 1.05
  },
  "best_period": 255,
  "p_value": 0.0023,
  "phase": 1.57,
  "amplitude": 0.045,
  "random_seed": 42,
  "n_mc_trials": 10000
}
```

### AUDIT_REPORT.md
Human-readable markdown with:
- Summary of all test modes
- Verdict tables (PASS/FAIL per criterion)
- Phase consistency across channels/ranges
- False positive rate from synthetic null
- Interpretation guidelines

## Deterministic Reproducibility

All random processes use deterministic seeds:

- **Baseline**: seed = 42 (pre-registered)
- **Ablation**: seed = 42 (same for comparability)
- **Synthetic null**: seed = 42 + trial_index (unique per trial)
- **Polarization**: seed = 42 (independent from TT via different data)

**Requirement**: Given identical input files and seeds, results must be bit-for-bit identical.

## Manifest Validation

All input files must be validated via SHA-256 manifests:

1. Compute SHA-256 hash of each input file
2. Compare against pre-recorded manifest
3. Fail if ANY file hash mismatch
4. Log all file paths in JSON output

**Exemption**: Manifest validation may be skipped for candidate-grade runs, but is **REQUIRED** for court-grade publication.

## Pre-Registered Candidate Periods

**LOCKED**: Δℓ ∈ {8, 16, 32, 64, 128, 255}

These periods were pre-registered based on theoretical predictions (Reed-Solomon overhead). They **MUST NOT** be modified based on data.

**Look-elsewhere correction**: P-values account for testing all 6 candidates via max-statistic Monte Carlo.

## Usage Examples

### Minimal Audit (TT + Whitening + Ablation)
```bash
python run_audit_suite.py \
    --planck_obs data/planck_pr3/raw/spectrum_tt.txt \
    --planck_model data/planck_pr3/raw/model_tt.txt \
    --planck_cov data/planck_pr3/raw/cov_tt.npy \
    --run_ablation \
    --mc_samples 10000
```

### Full Audit (All Modes)
```bash
python run_audit_suite.py \
    --planck_obs data/planck_pr3/raw/spectrum_tt.txt \
    --planck_model data/planck_pr3/raw/model_tt.txt \
    --planck_cov data/planck_pr3/raw/cov_tt.npy \
    --planck_obs_ee data/planck_pr3/raw/spectrum_ee.txt \
    --planck_model_ee data/planck_pr3/raw/model_ee.txt \
    --planck_obs_te data/planck_pr3/raw/spectrum_te.txt \
    --planck_model_te data/planck_pr3/raw/model_te.txt \
    --wmap_obs data/wmap/raw/wmap_tt.txt \
    --run_ablation --run_synth_null --synth_trials 200 \
    --mc_samples 10000 --seed 42
```

## Interpretation Flowchart

```
START: Candidate signal detected in baseline TT (p < 0.01)
  ↓
WHITENING: Does signal persist with full covariance?
  ├─ YES (Δχ² reduction <50%) → CONTINUE
  └─ NO (Δχ² reduction >90%) → LIKELY ARTIFACT, REPORT NULL
  ↓
POLARIZATION: Does signal appear in EE or TE?
  ├─ YES (p < 0.05, aligned phase) → STRONG CONFIRMATION
  ├─ WEAK (higher p, but aligned phase) → CONTINUE
  └─ NO or OPPOSITE PHASE → TT-SPECIFIC, CAUTION
  ↓
ABLATION: Does signal appear in multiple ℓ-ranges?
  ├─ ≥2 ranges with phase consistency → ROBUST
  ├─ 1 range only → POSSIBLE LOCALIZED ARTIFACT
  └─ Different periods in different ranges → SYSTEMATIC ERROR
  ↓
SYNTHETIC NULL: What is the false positive rate?
  ├─ FPR < 1% → STRONG SIGNAL
  ├─ FPR 1-5% → MARGINAL
  └─ FPR > 5% → LIKELY ΛCDM FLUCTUATION
  ↓
VERDICT: Combine all evidence
  ├─ ALL PASS → ROBUST CANDIDATE SIGNAL
  ├─ SOME FAIL → BORDERLINE, MORE DATA NEEDED
  └─ MULTIPLE FAIL → NULL RESULT
```

## Confidence Levels

Based on combined audit results:

- **High confidence**: All 5 criteria pass, FPR < 1%
- **Moderate confidence**: 4/5 criteria pass, FPR < 5%
- **Low confidence**: 3/5 criteria pass, FPR < 10%
- **Null result**: <3 criteria pass or FPR > 10%

## References

1. FORENSIC_VERDICT_CRITERIA.md - Baseline pass/fail criteria
2. PROTOCOL.md - Pre-registered protocol
3. WHITENING_MODES_GUIDE.md - Technical whitening details
4. RUNBOOK_REAL_DATA.md - Step-by-step usage guide

---

**End of Audit Protocol**
