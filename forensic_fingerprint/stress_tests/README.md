# UBT Forensic Fingerprint - Stress Tests

This directory contains four independent, falsification-oriented stress tests for the candidate structural anomaly at Δℓ ≈ 255 in CMB power spectrum residuals.

## Overview

**Objective**: Actively attempt to destroy the signal, not strengthen it. Only survival across ALL tests upgrades the candidate status.

**Philosophy**: These tests follow the Popperian falsification paradigm. A scientific hypothesis must be testable and potentially falsifiable.

## Test Scripts

### Test #1: Whitening / Full Covariance
**File**: `test_1_whitening.py`  
**Purpose**: Validate signal against covariance-aware whitening  
**PASS Criteria**: Peak remains at Δℓ ≈ 255 (±1–2 bins) with p < 10⁻³ across all whitening modes

```bash
python test_1_whitening.py \
    --obs path/to/planck_spectrum.txt \
    --model path/to/planck_model.txt \
    --mc_trials 10000
```

**Options**:
- `--obs`: Planck observation file (required)
- `--model`: Planck model file (required)
- `--cov`: Covariance matrix file (optional)
- `--ell_min`: Minimum multipole (default: 30)
- `--ell_max`: Maximum multipole (default: 1500)
- `--mc_trials`: Monte Carlo trials (default: 5000)
- `--output_dir`: Output directory (default: auto-generated)

**Output**:
- `planck_whitened_results.json` - Combined results for all whitening modes
- `whitening_comparison.md` - Detailed comparison report
- `whitening_delta_chi2_comparison.png` - Comparison plot
- Individual results in subdirectories: `none/`, `diagonal/`, `block-diagonal/`, `covariance/`

---

### Test #2: Polarization Channels (EE, TE)
**File**: `test_2_polarization.py`  
**Purpose**: Check if signal propagates to polarization  
**PASS Criteria**: 
- STRONG: Δℓ ≈ 255 in EE/TE with p ≤ 10⁻³
- WEAK: Δℓ ≈ 255 with reduced amplitude but aligned phase

```bash
python test_2_polarization.py \
    --ee_obs path/to/EE_spectrum.txt \
    --ee_model path/to/EE_model.txt \
    --te_obs path/to/TE_spectrum.txt \
    --te_model path/to/TE_model.txt
```

**Options**:
- `--tt_obs`, `--tt_model`: TT files (for comparison, optional)
- `--ee_obs`, `--ee_model`: EE files (required for EE test)
- `--te_obs`, `--te_model`: TE files (required for TE test)
- `--ell_min`, `--ell_max`: Multipole range
- `--mc_trials`: Monte Carlo trials (default: 5000)
- `--output_dir`: Output directory

**Output**:
- `planck_EE_results.json` - EE channel results
- `planck_TE_results.json` - TE channel results
- `polarization_comparison.md` - Joint TT/EE/TE summary
- Individual results in subdirectories: `TT/`, `EE/`, `TE/`

---

### Test #3: ℓ-Range Ablation
**File**: `test_3_ablation.py`  
**Purpose**: Verify signal appears in multiple disjoint ℓ ranges  
**PASS Criteria**: Δℓ ≈ 255 in ≥2 disjoint ranges with p < 0.01

```bash
python test_3_ablation.py \
    --obs path/to/planck_spectrum.txt \
    --model path/to/planck_model.txt
```

**Default Ranges**:
- [30, 800] - Low-ℓ only
- [800, 1500] - High-ℓ only
- [30, 500] - Very low-ℓ
- [500, 1000] - Mid-ℓ
- [1000, 1500] - Very high-ℓ

**Options**:
- `--obs`, `--model`: Planck files (required)
- `--cov`: Covariance file (optional)
- `--mc_trials`: Monte Carlo trials (default: 5000)
- `--custom_ranges`: Custom ranges as JSON, e.g., `"[[30,500],[500,1000]]"`
- `--output_dir`: Output directory

**Output**:
- `ablation_results.json` - Results for all ℓ ranges
- `ablation_comparison.md` - Detailed comparison
- `ablation_heatmap.png` - Heatmap of p-value vs ℓ-range
- Individual results in subdirectories: `ell_30_800/`, etc.

---

### Test #4: Synthetic ΛCDM Null Controls
**File**: `test_4_lcdm_null.py`  
**Purpose**: Show Δℓ = 255 is rare in ΛCDM realizations  
**PASS Criteria**: Δℓ ≈ 255 in ≤1% of ΛCDM simulations

```bash
python test_4_lcdm_null.py \
    --model path/to/planck_model.txt \
    --obs path/to/planck_spectrum.txt \
    --n_realizations 100
```

**Options**:
- `--model`: ΛCDM model file (required, used as theory)
- `--obs`: Observation file (optional, for sigma extraction)
- `--ell_min`, `--ell_max`: Multipole range
- `--n_realizations`: Number of synthetic spectra (default: 100)
- `--mc_trials`: MC trials per realization (default: 1000, reduced for speed)
- `--output_dir`: Output directory

**Output**:
- `lcdm_null_distribution.json` - Distribution of best-fit periods
- `lcdm_null_comparison.md` - Detailed analysis
- `lcdm_null_histogram.png` - Histogram of best-fit Δℓ

---

## Workflow

### 1. Prepare Data
Download Planck PR3 data files:
```bash
bash tools/data_download/download_planck_pr3_cosmoparams.sh
```

Expected files:
- `data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt`
- `data/planck_pr3/raw/COM_PowerSpect_CMB-TT-model_R3.01.txt`
- (Optional) EE, TE spectrum files

### 2. Run Tests
Execute all four tests:
```bash
# Test 1: Whitening
python forensic_fingerprint/stress_tests/test_1_whitening.py \
    --obs data/planck_pr3/raw/TT_spectrum.txt \
    --model data/planck_pr3/raw/TT_model.txt \
    --mc_trials 10000

# Test 2: Polarization (if EE/TE data available)
python forensic_fingerprint/stress_tests/test_2_polarization.py \
    --ee_obs data/planck_pr3/raw/EE_spectrum.txt \
    --ee_model data/planck_pr3/raw/EE_model.txt \
    --te_obs data/planck_pr3/raw/TE_spectrum.txt \
    --te_model data/planck_pr3/raw/TE_model.txt \
    --mc_trials 10000

# Test 3: Ablation
python forensic_fingerprint/stress_tests/test_3_ablation.py \
    --obs data/planck_pr3/raw/TT_spectrum.txt \
    --model data/planck_pr3/raw/TT_model.txt \
    --mc_trials 5000

# Test 4: ΛCDM Null
python forensic_fingerprint/stress_tests/test_4_lcdm_null.py \
    --model data/planck_pr3/raw/TT_model.txt \
    --obs data/planck_pr3/raw/TT_spectrum.txt \
    --n_realizations 200 \
    --mc_trials 1000
```

### 3. Review Results
Each test generates:
- JSON file with numerical results
- Markdown report with detailed analysis
- Plots/heatmaps for visualization

Check the comparison reports:
- `forensic_fingerprint/out/stress_tests/whitening_*/whitening_comparison.md`
- `forensic_fingerprint/out/stress_tests/polarization_*/polarization_comparison.md`
- `forensic_fingerprint/out/stress_tests/ablation_*/ablation_comparison.md`
- `forensic_fingerprint/out/stress_tests/lcdm_null_*/lcdm_null_comparison.md`

### 4. Update Master Report
Fill in results in `../UBT_STRESS_TESTS.md`:
- Copy test verdicts (PASS/FAIL)
- Update overall assessment
- State explicit falsification conclusion

---

## Important Notes

### Terminology
- Use "candidate structural anomaly" NOT "detected structure"
- Use "survives falsification" NOT "proven"
- Use "replication required" NOT "confirmed"

### Computational Requirements
- **Test #1**: ~10-30 minutes (4 whitening modes × 10k MC trials)
- **Test #2**: ~20-60 minutes (2-3 channels × 10k MC trials)
- **Test #3**: ~30-90 minutes (5 ℓ ranges × 5k MC trials)
- **Test #4**: ~30-120 minutes (200 realizations × 1k MC trials)

**Total runtime**: ~1.5-5 hours depending on system

### Reproducibility
- Fixed random seeds (42, 42+i for realizations)
- Version-controlled analysis code
- SHA-256 validated input data (recommended)

### Parallel Execution
Tests are independent and can run in parallel:
```bash
python test_1_whitening.py ... &
python test_3_ablation.py ... &
wait
```

---

## License

**Code**: MIT License  
**Documentation**: CC BY-NC-ND 4.0

---

## See Also

- `../PROTOCOL.md` - Pre-registered test protocol
- `../UBT_STRESS_TESTS.md` - Consolidated results report
- `../RUNBOOK_REAL_DATA.md` - Data download and preparation guide

---

**Last Updated**: 2026-01-11  
**Author**: UBT Research Team
