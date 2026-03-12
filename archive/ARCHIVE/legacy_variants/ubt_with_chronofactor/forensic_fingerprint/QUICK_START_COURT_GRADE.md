# Court-Grade CMB Comb Analysis - Quick Start Guide

This guide provides exact commands for running court-grade CMB comb fingerprint analysis with full covariance whitening and falsification tests.

## Prerequisites

1. **Data files**: Download Planck PR3 and/or WMAP data
   ```bash
   bash tools/data_download/download_planck_pr3_cosmoparams.sh
   ```

2. **Python dependencies**: numpy, scipy, matplotlib
   ```bash
   pip install numpy scipy matplotlib
   ```

## Command Reference

### 1. Basic Analysis (Diagonal Whitening)

Minimal command for Planck TT with diagonal uncertainties:

```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --variant C
```

### 2. Court-Grade Analysis (Full Covariance Whitening)

With full covariance matrix (recommended for publication):

```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/covariance.txt \
    --whiten_mode covariance \
    --mc_samples 100000 \
    --variant C
```

**Key parameters:**
- `--whiten_mode covariance`: Use full Cholesky whitening
- `--mc_samples 100000`: High MC sampling for p-value resolution
- `--planck_cov`: Full covariance matrix file

### 3. Two-Dataset Replication (Planck + WMAP)

For independent verification:

```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/covariance.txt \
    --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_cov data/wmap/covariance.txt \
    --whiten_mode covariance \
    --mc_samples 100000 \
    --variant C
```

### 4. Whitening Mode Options

Available whitening modes (use with `--whiten_mode`):

- **`none`**: No whitening (raw residuals)
- **`diagonal`**: Standard diagonal uncertainties (default)
- **`cov_diag`**: Use sqrt(diag(Cov)) instead of provided sigma
- **`covariance`**: Full Cholesky whitening (court-grade)

Example comparing modes:

```bash
# Diagonal mode (fast, but ignores correlations)
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --whiten_mode diagonal \
    --output_dir out/diagonal_run

# Full covariance mode (rigorous)
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/covariance.txt \
    --whiten_mode covariance \
    --output_dir out/covariance_run
```

### 5. ΛCDM Null Control Test

Measure false positive rate under synthetic ΛCDM:

```bash
python forensic_fingerprint/run_synthetic_lcdm_control.py \
    --model_file data/planck_pr3/raw/model.txt \
    --sigma_file data/planck_pr3/raw/spectrum.txt \
    --cov_file data/planck_pr3/covariance.txt \
    --whiten_mode covariance \
    --n_realizations 100 \
    --mc_samples 5000
```

**Expected output**: False positive rate ~1% at p < 0.01 threshold

### 6. Ablation Tests (ℓ-Range Robustness)

Test multiple ℓ-windows to verify signal robustness:

```bash
# Planck: Low-ℓ window [30-500]
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/covariance.txt \
    --ell_min_planck 30 --ell_max_planck 500 \
    --whiten_mode covariance \
    --output_dir out/ablation_30_500

# Planck: Mid-ℓ window [500-1000]
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/covariance.txt \
    --ell_min_planck 500 --ell_max_planck 1000 \
    --whiten_mode covariance \
    --output_dir out/ablation_500_1000

# Planck: High-ℓ window [1000-1500]
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/covariance.txt \
    --ell_min_planck 1000 --ell_max_planck 1500 \
    --whiten_mode covariance \
    --output_dir out/ablation_1000_1500
```

**Robustness criterion**: Signal is robust if Δℓ=255 appears in ≥2 independent windows with consistent phase (within π/2).

### 7. Provenance and Reproducibility

With SHA-256 manifests for data provenance:

```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --planck_cov data/planck_pr3/covariance.txt \
    --planck_manifest data/planck_pr3/manifests/planck_pr3_tt_manifest.json \
    --whiten_mode covariance \
    --mc_samples 100000 \
    --seed 42 \
    --variant C
```

## Output Files

Each run produces:

- `combined_verdict.md` - PASS/FAIL decision report (**READ THIS FIRST**)
- `planck_results.json` - Full numerical results (Planck)
- `wmap_results.json` - Full numerical results (WMAP, if run)
- `figures/` - Diagnostic plots
  - `residuals_with_fit.png` - Residuals + best-fit sinusoid
  - `null_distribution.png` - MC null distribution histogram

## Interpretation Guide

### Skeptic Checklist

Before trusting results, verify:

1. **Units check**: χ²/dof should be ~1 (not >>1)
   - If χ²/dof >> 1: units mismatch or wrong model
   
2. **Covariance check**: 
   - Condition number reported in verdict
   - Ridge regularization applied if needed
   
3. **Look-elsewhere correction**: 
   - Automatic via MC max-statistic over locked candidate set
   
4. **ΛCDM control**: 
   - Run synthetic control to measure false positive rate
   - Expected ~1% at p < 0.01
   
5. **Ablation tests**: 
   - Signal should persist across multiple ℓ-windows
   - Phase should be consistent

### P-Value Interpretation

- **p < 2.9e-7** (5σ): **STRONG** signal
- **p < 0.01**: **CANDIDATE** signal (requires replication)
- **p > 0.05**: **NULL** (no significant signal)

### MC Sampling Guidelines

- **Candidate-grade**: 5,000-10,000 MC samples (p-floor = 2e-4 to 1e-4)
- **Strong-grade**: 100,000 MC samples (p-floor = 1e-5)
- **Court-grade**: 1,000,000 MC samples (p-floor = 1e-6)

If p-value hits the floor (p = 1/n_mc), increase `--mc_samples`.

## Common Issues

### Units Mismatch Warning

If you see:
```
WARNING: POSSIBLE UNITS MISMATCH OR WRONG MODEL
χ²/dof = 1234.56 >> 1
```

**Solution**: Verify observation and model files use same units (Cl or Dl). Check file headers.

### Covariance Not Positive Definite

If covariance fails Cholesky:
```
ERROR: Cholesky decomposition failed even after regularization
```

**Solution**: Ridge regularization is applied automatically. Check condition number in output.

### P-Value at Floor

If you see:
```
⚠ MC p-floor: p-value at floor (1/10000)
```

**Solution**: Increase `--mc_samples` for better p-value resolution.

## Advanced: Polarization (TE/EE)

TE and EE spectra can be analyzed using the same loaders (set `spectrum_type` parameter in loader code). This is currently a manual process.

## Performance Notes

- **Diagonal mode**: ~10 seconds for 1500 multipoles, 10k MC samples
- **Covariance mode**: ~2-5 minutes for same (Cholesky overhead)
- **ΛCDM control (100 realizations)**: ~30-60 minutes

## Questions?

See:
- `FORENSIC_VERDICT_CRITERIA.md` - Pre-registered pass/fail criteria
- `PROTOCOL.md` - Full statistical protocol
- `WHITENING_IMPLEMENTATION_SUMMARY.md` - Technical details
- `RUNBOOK_REAL_DATA.md` - Detailed runbook

## Citation

If using this code, cite:
- Jaroš, D. et al. (2025). "UBT Forensic Fingerprint Analysis Protocol"
- GitHub: https://github.com/DavJ/unified-biquaternion-theory
