# Forensic Stress Tests - Complete Guide

**Version**: 1.1  
**Date**: 2026-01-11  
**Objective**: Publication-grade falsification testing of the Δℓ = 255 CMB periodicity

---

## Executive Summary

This directory contains **five independent stress tests** designed to actively attempt to destroy the candidate Δℓ = 255 signal in CMB power spectrum residuals. These tests implement a **Popperian falsification paradigm**: the signal must survive ALL tests to be upgraded from "initial observation" to "replicated anomaly."

### Critical Philosophy

**This is NOT a confirmation exercise.** Each test is explicitly designed to eliminate the signal if it arises from:
- Correlated noise or covariance artifacts
- Instrumental systematics
- Localized ℓ-range contamination
- Generic ΛCDM features
- Random noise with unstable phase

Only if the signal survives ALL five independent falsification attempts does it warrant further investigation.

---

## Test Suite Overview

| Test | Target | Null Hypothesis | Skeptic One-Liner |
|------|--------|----------------|-------------------|
| **#1** | Covariance | Signal is correlated noise | "If correlated noise, whitening eliminates it. It does or does not." |
| **#2** | Polarization | Signal is TT-only artifact | "If instrumental/scalar, no EE/TE signal. It does or does not." |
| **#3** | ℓ-Range | Signal is localized artifact | "If narrow-range artifact, ablation destroys it. It does or does not." |
| **#4** | ΛCDM Null | Signal is generic ΛCDM feature | "If generic ΛCDM, appears frequently in sims. It does or does not." |
| **#5** | Phase | Signal is random noise | "If random noise, phase is incoherent. It does or does not." |

---

## Test #1: Whitening / Full Covariance

### Purpose
Validate that the signal is not an artifact of ignoring correlations in the error covariance matrix.

### Methodology
1. Load Planck TT data with full covariance (if available)
2. Run comb test with four whitening modes:
   - `none` - No whitening (control)
   - `diagonal` - Diagonal σ only (standard baseline)
   - `block-diagonal` - Approximate local correlations
   - `covariance` - Full covariance whitening via Cholesky
3. Compare Δℓ, amplitude, phase, p-value across modes

### PASS Criteria
- Δℓ ≈ 255 persists (±1-2 bins) with p < 10⁻³ in ALL modes
- Phase remains stable across modes

### FAIL Criteria
- Signal disappears after covariance whitening
- Best-fit period shifts arbitrarily between modes
- p-value degrades to > 0.1

### Output Files
- `whitening_comparison.md` - Detailed comparison report
- `planck_whitened_results.json` - Numerical results
- Plots: `whitening_delta_chi2_comparison.png`

### Computational Cost
~10-30 minutes (4 modes × 10k MC trials)

---

## Test #2: Polarization Channels (EE, TE)

### Purpose
Test whether the signal propagates to polarization channels or is TT-only.

### Methodology
1. Load Planck EE and TE spectra
2. Apply identical comb test to each channel independently
3. Compare with TT results:
   - Same candidate periods [8, 16, 32, 64, 128, 255]
   - Same MC null size
   - No parameter retuning

### PASS Criteria
- **STRONG**: Δℓ ≈ 255 in EE/TE with p ≤ 10⁻³
- **WEAK**: Δℓ ≈ 255 with reduced amplitude but aligned phase

### FAIL Criteria
- No structure near 255 in polarization
- Completely random best-fit periods in EE/TE

### Interpretation
- **Structural feature**: Should appear in all channels (TT, EE, TE)
- **Instrumental artifact**: TT only
- **Scalar contamination**: TT only

### Output Files
- `polarization_comparison.md` - Joint TT/EE/TE analysis
- Individual channel results in subdirectories

### Computational Cost
~20-60 minutes (2-3 channels × 10k MC trials)

---

## Test #3: ℓ-Range Ablation

### Purpose
Exclude the possibility that the signal arises from a narrow ℓ-range artifact (foreground, beam, systematic).

### Methodology
1. Define disjoint ℓ ranges:
   - [30, 800] - Low-ℓ
   - [800, 1500] - High-ℓ
   - [30, 500] - Very low-ℓ
   - [500, 1000] - Mid-ℓ
   - [1000, 1500] - Very high-ℓ
2. Run full comb test on each range independently
3. Regenerate null distribution for each range (critical!)
4. Compare best-fit Δℓ, p-value

### PASS Criteria
- Δℓ ≈ 255 appears in ≥2 disjoint ranges with p < 0.01
- Phase alignment across ranges

### FAIL Criteria
- Signal exists only in one narrow window
- Best-fit period changes dramatically across ranges

### Output Files
- `ell_range_ablation.md` - Detailed range comparison
- `ablation_heatmap.png` - p-value vs range heatmap
- `ablation_results.json` - Numerical results

### Computational Cost
~30-90 minutes (5 ranges × 5k MC trials)

---

## Test #4: Synthetic ΛCDM Null Controls

### Purpose
Determine whether Δℓ = 255 is a generic feature of ΛCDM with cosmic variance.

### Methodology
1. Generate ≥100 synthetic ΛCDM TT spectra:
   - Use Planck best-fit ΛCDM as theory
   - Match ℓ range exactly
   - Use real observational σ for noise model
   - Add Gaussian realizations: C_obs = C_theory + N(0, σ²)
2. Apply identical comb test to each realization
3. Count frequency of Δℓ ≈ 255 as best-fit
4. Generate histogram of best-fit periods

### PASS Criteria
- Δℓ ≈ 255 appears in ≤1% of ΛCDM realizations
- Real data p-value is rare in null distribution

### FAIL Criteria
- Δℓ ≈ 255 appears frequently (>5% of realizations)
- Real data is typical of ΛCDM noise

### Output Files
- `lcdm_null_statistics.json` - Distribution of periods and p-values
- `lcdm_null_comparison.md` - Statistical analysis
- `lcdm_null_histogram.png` - Period distribution

### Computational Cost
~30-120 minutes (200 realizations × 1k MC trials)

---

## Test #5: Phase Coherence

### Purpose
Test whether the signal phase is stable or random across datasets and preprocessing.

### Methodology
1. Extract phase φ at Δℓ = 255 from:
   - Planck TT (raw, diagonal whitening)
   - Planck TT (covariance whitening, if available)
   - WMAP TT (raw, diagonal whitening)
   - WMAP TT (covariance whitening, if available)
2. Compute circular statistics:
   - Circular mean and standard deviation
   - Mean resultant length (coherence score)
   - Pairwise phase differences
3. Assess coherence using objective criteria

### PASS Criteria
- Circular std dev ≤ 15°
- Coherence score ≥ 0.9
- Pairwise differences < 30°

### FAIL Criteria
- Random phase distribution
- Large variance (std > 30°)
- Incoherent phases across datasets

### Interpretation
- **Coherent phase**: Suggests structural or systematic origin
- **Random phase**: Indicates noise or uncorrelated artifacts

### Output Files
- `phase_stability_report.md` - Complete coherence analysis
- `phase_coherence_results.json` - Numerical statistics
- Circular statistics plots

### Computational Cost
~10-30 minutes (2-4 datasets/modes × 1k MC trials)

---

## Complete Workflow

### Prerequisites

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download Data**:
   ```bash
   # Planck PR3
   bash tools/data_download/download_planck_pr3_cosmoparams.sh
   
   # WMAP (optional, for cross-dataset comparison)
   # Follow WMAP data download instructions
   ```

3. **Verify Data Files**:
   - `data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt`
   - `data/planck_pr3/raw/COM_PowerSpect_CMB-TT-model_R3.01.txt`
   - (Optional) Covariance matrix file
   - (Optional) EE, TE spectrum files
   - (Optional) WMAP data files

### Sequential Execution

```bash
# Navigate to repository root
cd /path/to/unified-biquaternion-theory

# Test #1: Whitening
python forensic_fingerprint/stress_tests/test_1_whitening.py \
    --obs data/planck_pr3/raw/TT_spectrum.txt \
    --model data/planck_pr3/raw/TT_model.txt \
    --cov data/planck_pr3/raw/TT_covariance.txt \
    --ell_min 30 --ell_max 1500 \
    --mc_trials 10000

# Test #2: Polarization (requires EE/TE data)
python forensic_fingerprint/stress_tests/test_2_polarization.py \
    --tt_obs data/planck_pr3/raw/TT_spectrum.txt \
    --tt_model data/planck_pr3/raw/TT_model.txt \
    --ee_obs data/planck_pr3/raw/EE_spectrum.txt \
    --ee_model data/planck_pr3/raw/EE_model.txt \
    --te_obs data/planck_pr3/raw/TE_spectrum.txt \
    --te_model data/planck_pr3/raw/TE_model.txt \
    --mc_trials 10000

# Test #3: Ablation
python forensic_fingerprint/stress_tests/test_3_ablation.py \
    --obs data/planck_pr3/raw/TT_spectrum.txt \
    --model data/planck_pr3/raw/TT_model.txt \
    --mc_trials 5000

# Test #4: ΛCDM Null
python forensic_fingerprint/stress_tests/test_4_lcdm_null.py \
    --model data/planck_pr3/raw/TT_model.txt \
    --obs data/planck_pr3/raw/TT_spectrum.txt \
    --n_realizations 200 \
    --mc_trials 1000

# Test #5: Phase Coherence
python forensic_fingerprint/stress_tests/test_5_phase_coherence.py \
    --planck_obs data/planck_pr3/raw/TT_spectrum.txt \
    --planck_model data/planck_pr3/raw/TT_model.txt \
    --planck_cov data/planck_pr3/raw/TT_covariance.txt \
    --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_model data/wmap/raw/wmap_tt_model_9yr_v5.txt \
    --ell_min 30 --ell_max 800 \
    --mc_trials 1000
```

### Parallel Execution (Faster)

Tests are independent and can run in parallel:

```bash
# Run all tests simultaneously (requires sufficient RAM/CPU)
python forensic_fingerprint/stress_tests/test_1_whitening.py [...] &
python forensic_fingerprint/stress_tests/test_3_ablation.py [...] &
python forensic_fingerprint/stress_tests/test_4_lcdm_null.py [...] &
python forensic_fingerprint/stress_tests/test_5_phase_coherence.py [...] &
wait

# Note: Test #2 (polarization) may take longer and can run separately
python forensic_fingerprint/stress_tests/test_2_polarization.py [...]
```

---

## Output Structure

All test results are saved to:
```
forensic_fingerprint/out/stress_tests/
├── whitening_YYYYMMDD_HHMMSS/
│   ├── whitening_comparison.md
│   ├── planck_whitened_results.json
│   └── whitening_delta_chi2_comparison.png
├── polarization_YYYYMMDD_HHMMSS/
│   ├── polarization_comparison.md
│   ├── TT/, EE/, TE/ subdirectories
│   └── phase_alignment_plot.png
├── ablation_YYYYMMDD_HHMMSS/
│   ├── ell_range_ablation.md
│   ├── ablation_results.json
│   └── ablation_heatmap.png
├── lcdm_null_YYYYMMDD_HHMMSS/
│   ├── lcdm_null_statistics.json
│   ├── lcdm_null_comparison.md
│   └── lcdm_null_histogram.png
└── phase_coherence_YYYYMMDD_HHMMSS/
    ├── phase_stability_report.md
    ├── phase_coherence_results.json
    └── phase_circular_plot.png
```

---

## Interpreting Results

### Overall Verdict

The **overall verdict** depends on ALL tests:

| Scenario | Verdict | Interpretation |
|----------|---------|----------------|
| All 5 PASS | **Signal Survives** | Upgrades to "replicated anomaly" - independent verification required |
| Any FAIL | **Signal Eliminated** | Hypothesis falsified - signal is artifact/noise |

### Individual Test Verdicts

Each test produces a clear **PASS** or **FAIL** verdict in its report file.

**Example - Test #1 PASS**:
```
VERDICT: PASS
- Δℓ = 255 in all whitening modes
- p < 10⁻³ across modes
- Phase stable within 5°
→ Signal is NOT correlated noise artifact
```

**Example - Test #4 FAIL**:
```
VERDICT: FAIL
- Δℓ = 255 appears in 12% of ΛCDM realizations
- Threshold: ≤1%
→ Signal is a generic ΛCDM feature with cosmic variance
```

---

## Important Notes

### Language and Terminology

Throughout all documentation and code, we use:

| ✓ USE | ✗ AVOID |
|-------|---------|
| "Candidate structural anomaly" | "Detected digital structure" |
| "Survives falsification" | "Proven" or "Confirmed" |
| "Replication required" | "Independently verified" |
| "Consistent with hypothesis" | "Validates theory" |
| "Signal eliminates itself" | "Test failed" (when referring to signal failure) |

This reflects the **Popperian falsification paradigm**.

### Reproducibility

All tests use:
- Fixed random seeds (default: 42, +i for realizations)
- Version-controlled analysis code
- Locked pre-registered parameters
- Transparent methodology in code comments

### Data Provenance

- All input data files should be checksummed (SHA-256)
- Manifests are provided in `data/*/manifests/`
- Official Planck/WMAP data sources documented

### Computational Resources

- **Minimum**: 8 GB RAM, 4 CPU cores
- **Recommended**: 16 GB RAM, 8 CPU cores
- **Total runtime**: 2-6 hours (sequential), 1-2 hours (parallel)

---

## Troubleshooting

### "File not found" errors

Ensure data files are downloaded:
```bash
bash tools/data_download/download_planck_pr3_cosmoparams.sh
```

### Covariance matrix errors

If covariance file is unavailable:
- Use `--whiten diagonal` for Test #1
- Skip `--planck_cov` for Test #5

### Out of memory

Reduce MC trials:
```bash
--mc_trials 1000  # Instead of 10000
--n_realizations 50  # Instead of 200 (Test #4)
```

### Python import errors

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## License

**Code**: MIT License  
**Documentation**: CC BY-NC-ND 4.0

---

## Citation

If you use these stress tests in your work, please cite:

```
UBT Forensic Fingerprint Stress Tests (2026)
Repository: https://github.com/DavJ/unified-biquaternion-theory
License: MIT (code) / CC BY-NC-ND 4.0 (docs)
```

---

## Contact

For issues, questions, or collaboration:
- Open an issue on GitHub
- See CONTRIBUTING.md for guidelines

---

**Last Updated**: 2026-01-11  
**Version**: 1.1  
**Status**: Complete implementation, awaiting execution on real data
