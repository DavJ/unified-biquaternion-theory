# Court-Grade CMB Comb Test - Implementation Summary

**Status**: ✅ Complete  
**Version**: 1.0  
**Date**: 2026-01-11

This directory contains the court-grade implementation of the CMB comb test for detecting periodic signatures in cosmic microwave background power spectrum residuals.

## What Was Implemented

This PR completes the court-grade CMB comb test with the following features:

### 1. Repro/Status Automation ✓

**Tool**: `tools/forensic/print_run_summary.py`

Quick status reporting for CMB comb test runs:

```bash
# Show all runs in table format
python tools/forensic/print_run_summary.py

# Show last 10 runs
python tools/forensic/print_run_summary.py --last 10

# Export to CSV
python tools/forensic/print_run_summary.py --format csv --output summary.csv

# Export to JSON
python tools/forensic/print_run_summary.py --format json --output summary.json
```

**Features**:
- Automatic timestamp extraction
- Planck and WMAP p-values
- Best-fit period and phase
- Whitening mode
- ℓ-ranges
- Verdict (PASS/FAIL/CANDIDATE)
- Incomplete run detection

### 2. Whitening Implementation (Full Covariance) ✓

**Updated**: `forensic_fingerprint/run_real_data_cmb_comb.py`

Three whitening modes for error handling:

```bash
# Diagonal (candidate-grade, default)
--whiten diag

# Full covariance (court-grade)
--whiten full --planck_cov data/planck_pr3/covariance.npy

# No whitening (debugging only)
--whiten none
```

**Features**:
- Cholesky decomposition (default): `--cov_method cholesky`
- Eigenvalue decomposition (stable): `--cov_method eigh`
- Automatic symmetrization
- Ridge regularization: `--cov_jitter 1e-12`
- Condition number monitoring

### 3. Polarization TE/EE Pipeline ✓

**Updated**: Loaders and main runner

Support for all CMB spectra:

```bash
# Temperature (TT)
--spectrum TT

# Temperature-E cross (TE)
--spectrum TE

# E-mode (EE)
--spectrum EE

# B-mode (BB)
--spectrum BB
```

**Use case**: Independent cross-check of TT results. Real signal should appear in all spectra with same period and consistent phase.

### 4. Ablation ℓ-Ranges ✓

**Updated**: `forensic_fingerprint/run_real_data_cmb_comb.py`

Test signal persistence across independent multipole windows:

```bash
# Pre-defined ranges (Planck: low/mid/high)
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --ablate-ell \
    --mc_samples 10000

# Custom ranges
python run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --ablate-ell \
    --ablate-ranges "30-500,500-1000,1000-1500" \
    --mc_samples 10000
```

**Output**:
- `ablation_summary/ablation_results.json`
- `ablation_summary/ablation_summary.csv`
- `ablation_summary/ablation_report.md`

**Expected**: Real signal should appear in multiple ranges with same period.

### 5. Synthetic ΛCDM Control ✓

**Updated**: `forensic_fingerprint/run_real_data_cmb_comb.py`

False positive rate calibration with synthetic ΛCDM data:

```bash
# Basic null control (100 trials)
python run_real_data_cmb_comb.py \
    --null-data lcdm \
    --null-trials 100 \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --mc_samples 10000

# Court-grade (1000 trials, full covariance)
python run_real_data_cmb_comb.py \
    --null-data lcdm \
    --null-trials 1000 \
    --planck_cov data/planck_pr3/covariance.npy \
    --whiten full \
    --mc_samples 100000
```

**Output**:
- `null_control/null_results.json`
- `null_control/null_summary.csv`
- `null_control/null_report.md`

**Checks**:
- False positive rate at p<0.01 (expect ~1%)
- False positive rate at p<0.05 (expect ~5%)
- Period 255 bias (expect ~17%, i.e., 1/6)
- P-value uniformity (Kolmogorov-Smirnov test)

**Warning signs**:
- FPR > 3% at p<0.01 → systematic bias
- Period 255 > 25% → period selection bias
- KS p-value < 0.05 → non-uniform p-values

## Documentation

### RUNBOOK_REAL_DATA.md

Comprehensive guide with:
- Quick start examples
- Advanced features section (250+ lines)
- Whitening modes guide
- Polarization workflows
- Ablation procedures
- ΛCDM null control guide
- Court-grade checklist
- Troubleshooting

**Key sections added**:
- "Advanced Features" (comprehensive guide)
- Whitening modes (3 modes explained)
- Polarization spectra (TT/TE/EE workflows)
- ℓ-range ablation (pre-defined and custom)
- Synthetic ΛCDM null control

### SKEPTIC_CHECKLIST.md

Updated to reflect implementation status:
- ✅ Whitening: Fully implemented
- ✅ Polarization: Fully implemented
- ✅ Ablation: Fully implemented
- ✅ ΛCDM control: Fully implemented

**Summary table**: All 11 counter-arguments addressed or partially addressed.

## Test Coverage

**Total**: 100 tests passing (up from 90)

New tests added:
- `test_runner_integration.py`: 10 tests
  - Ablation range validation
  - ΛCDM spectrum generation (TT/EE/TE)
  - Mock observation generation
  - Ablation summarization

All existing tests still passing:
- Whitening modes: 21 tests
- Synthetic ΛCDM: 19 tests
- Ablation: 18 tests
- Court-grade whitening: 14 tests
- And more...

## Example Workflows

### Candidate-Grade Analysis (Quick)

```bash
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum.txt \
    --planck_model data/planck_pr3/raw/model.txt \
    --wmap_obs data/wmap/raw/wmap_spectrum.txt \
    --variant C \
    --mc_samples 5000
```

Runtime: ~30-60 seconds  
Use: Exploratory analysis

### Court-Grade Analysis (Full)

```bash
# 1. TT with full covariance
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum_tt.txt \
    --planck_model data/planck_pr3/raw/model_tt.txt \
    --planck_cov data/planck_pr3/covariance/planck_tt_cov.npy \
    --planck_manifest data/planck_pr3/manifests/planck_pr3_tt_manifest.json \
    --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_manifest data/wmap/manifests/wmap_tt_manifest.json \
    --whiten full \
    --mc_samples 100000 \
    --variant C \
    --output_dir out/court_grade_tt

# 2. TE cross-check
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum_te.txt \
    --planck_model data/planck_pr3/raw/model_te.txt \
    --planck_cov data/planck_pr3/covariance/planck_te_cov.npy \
    --spectrum TE \
    --whiten full \
    --mc_samples 100000 \
    --variant C \
    --output_dir out/court_grade_te

# 3. EE cross-check
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum_ee.txt \
    --planck_model data/planck_pr3/raw/model_ee.txt \
    --planck_cov data/planck_pr3/covariance/planck_ee_cov.npy \
    --spectrum EE \
    --whiten full \
    --mc_samples 100000 \
    --variant C \
    --output_dir out/court_grade_ee

# 4. Ablation tests
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --planck_obs data/planck_pr3/raw/spectrum_tt.txt \
    --planck_model data/planck_pr3/raw/model_tt.txt \
    --planck_cov data/planck_pr3/covariance/planck_tt_cov.npy \
    --ablate-ell \
    --whiten full \
    --mc_samples 100000 \
    --variant C \
    --output_dir out/ablation_tests

# 5. ΛCDM null control
python forensic_fingerprint/run_real_data_cmb_comb.py \
    --null-data lcdm \
    --null-trials 1000 \
    --planck_cov data/planck_pr3/covariance/planck_tt_cov.npy \
    --whiten full \
    --mc_samples 100000 \
    --variant C \
    --output_dir out/lcdm_null_control

# 6. Review results
python tools/forensic/print_run_summary.py
cat out/court_grade_tt/combined_verdict.md
cat out/lcdm_null_control/null_control/null_report.md
```

Runtime: ~1-2 hours total  
Use: Publication-ready analysis

## Court-Grade Checklist

For a run to be considered court-grade, it must include:

- ✅ Full covariance whitening (not diagonal)
- ✅ High MC samples (100k not 5k)
- ✅ SHA-256 manifest validation
- ✅ Planck + WMAP replication
- ✅ TE/EE cross-checks
- ✅ ℓ-range ablation tests
- ✅ ΛCDM null control (FPR calibration)
- ✅ All results documented

## Next Steps

For users running the court-grade analysis:

1. Run TT analysis with full covariance
2. Check `combined_verdict.md` for PASS/FAIL
3. Run TE and EE cross-checks
4. Run ablation tests to verify ℓ-range independence
5. Run ΛCDM null control to calibrate false positive rate
6. Review `SKEPTIC_CHECKLIST.md` for addressed counter-arguments
7. Compile all results for publication

## References

- **Protocol**: `forensic_fingerprint/PROTOCOL.md`
- **Runbook**: `forensic_fingerprint/RUNBOOK_REAL_DATA.md`
- **Skeptic Checklist**: `forensic_fingerprint/SKEPTIC_CHECKLIST.md`
- **Verdict Criteria**: `forensic_fingerprint/FORENSIC_VERDICT_CRITERIA.md`

---

**Questions?** See RUNBOOK_REAL_DATA.md or open a GitHub issue.

**Contributions?** Follow the court-grade testing checklist before submitting PRs.
