# Whitening Modes Guide

## Overview

The CMB comb fingerprint test now supports multiple whitening modes to properly account for measurement uncertainties and correlations in the data. This guide explains each mode and when to use it.

## Available Whitening Modes

### 1. `none` - No Whitening
**Usage**: `--whiten none`

- **Description**: No normalization applied to residuals. Raw difference between observed and model spectra.
- **Formula**: `r = C_obs - C_model`
- **When to use**: Diagnostic purposes only. Not recommended for statistical analysis.
- **Limitations**: Does not account for varying uncertainties across multipoles.

### 2. `diagonal` - Diagonal Whitening (Default)
**Usage**: `--whiten diagonal`

- **Description**: Normalize residuals by diagonal uncertainties (σ_ℓ).
- **Formula**: `r = (C_obs - C_model) / σ`
- **When to use**: When only diagonal uncertainties are available or for quick analysis.
- **Limitations**: Ignores correlations between multipoles.
- **Default**: This is the default mode if no covariance matrix is provided.

### 3. `cov_diag` - Diagonal from Covariance
**Usage**: `--whiten cov_diag --input_cov <covariance_file>`

- **Description**: Extract diagonal uncertainties from full covariance matrix.
- **Formula**: `r = (C_obs - C_model) / sqrt(diag(Σ))`
- **When to use**: Control test to verify if correlations matter. Compare with full covariance mode.
- **Purpose**: Detect whether periodic signals are artifacts of ignoring off-diagonal correlations.

### 4. `covariance` - Full Covariance Whitening
**Usage**: `--whiten covariance --input_cov <covariance_file>`

- **Description**: Whiten using full covariance matrix via Cholesky decomposition.
- **Formula**: `r = L^{-1} (C_obs - C_model)` where `Σ = L L^T`
- **When to use**: When full covariance matrix is available. **Recommended for publication-grade analysis.**
- **Features**:
  - Automatic validation of covariance matrix (symmetry, positive definiteness)
  - Eigenvalue analysis for condition number
  - Automatic ridge regularization for ill-conditioned matrices
  - Comprehensive metadata logging

### 5. `block-diagonal` - Block-Diagonal Approximation
**Usage**: `--whiten block-diagonal`

- **Description**: Approximate covariance with block-diagonal structure (local correlations only).
- **When to use**: When full covariance unavailable but local correlations expected.
- **Limitations**: Approximation only. Does not capture long-range correlations.

## Covariance Matrix Validation

When using `--whiten covariance`, the following checks are performed automatically:

### Validation Checks
1. **Symmetry**: Covariance must be symmetric (Σ = Σ^T)
2. **Positive Definiteness**: All eigenvalues must be positive
3. **Condition Number**: Ratio of largest to smallest eigenvalue
4. **ℓ-range Compatibility**: Covariance size must match data

### Automatic Regularization

If the covariance matrix is ill-conditioned (condition number > 10^10), **ridge regularization** is applied automatically:

```
Σ_reg = Σ + λI
```

where λ is chosen to bring the condition number to ~10^8.

**Logged Metadata**:
- Ridge parameter λ
- Condition number before and after regularization
- Min/max eigenvalues

## Usage Examples

### Basic Analysis (Diagonal)
```bash
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --whiten diagonal
```

### Full Covariance (Recommended)
```bash
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/raw/covariance.txt \
    --whiten covariance
```

### Control Test (Diagonal from Covariance)
```bash
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/raw/covariance.txt \
    --whiten cov_diag
```

## Stress Testing

To compare all whitening modes systematically, use the whitening stress test:

```bash
python forensic_fingerprint/stress_tests/test_1_whitening.py \
    --obs data/planck_pr3/raw/spectrum.txt \
    --model data/planck_pr3/raw/model.txt \
    --cov data/planck_pr3/raw/covariance.txt \
    --output_dir out/whitening_stress_test
```

This will:
1. Run the CMB comb test with all whitening modes
2. Generate comparison plots
3. Produce a pass/fail assessment
4. Output `whitening_comparison.md` report

## Interpretation

### Pass/Fail Criteria

A signal **passes** the whitening stress test if:
1. Peak period remains at Δℓ ≈ 255 (±1-2 bins) across **all** whitening modes
2. p-value < 10^-3 for **all** modes
3. Signal does not disappear when correlations are accounted for

If the signal only appears in `diagonal` mode but vanishes in `covariance` mode, this suggests the signal is an **artifact of ignoring correlations**.

### Metadata Output

Results include comprehensive whitening metadata:

```json
{
  "whiten_mode": "covariance",
  "regularization_used": false,
  "lambda_ridge": null,
  "cov_metadata": {
    "is_symmetric": true,
    "is_positive_definite": true,
    "min_eigenvalue": 1.2e-04,
    "max_eigenvalue": 4.9e-04,
    "condition_number": 4.87,
    "ell_range": [30, 1500],
    "needs_regularization": false
  }
}
```

## Best Practices

1. **Always use full covariance when available** (`--whiten covariance`)
2. **Run comparison tests** to verify robustness
3. **Check metadata** for regularization warnings
4. **Report all modes** in publications for transparency
5. **Use block-diagonal** only when full covariance unavailable

## References

- See `forensic_fingerprint/PROTOCOL.md` for full statistical protocol
- See `forensic_fingerprint/stress_tests/README.md` for stress test documentation
- See implementation in `forensic_fingerprint/cmb_comb/cmb_comb.py`

## Version History

- **v1.1** (2026-01-11): Added `cov_diag` mode, automatic ridge regularization, metadata logging
- **v1.0**: Initial implementation with `none`, `diagonal`, `covariance`, `block-diagonal` modes
