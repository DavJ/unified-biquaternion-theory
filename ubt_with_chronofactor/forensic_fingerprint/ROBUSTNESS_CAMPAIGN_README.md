# CMB Comb Signal - Robustness & Falsification Campaign

## Overview

This directory contains the **Final Robustness & Falsification Campaign** for the candidate Δℓ = 255 periodic comb signal in CMB power spectrum residuals.

**Critical Philosophy**: This campaign is designed to **DESTROY** the signal, not strengthen it. The goal is to attempt invalidation using the strongest standard counter-arguments in CMB data analysis. If the signal survives, it becomes a robust, publishable anomaly. If it fails, that is a successful scientific outcome.

## Quick Start

### Minimum Required Command

Run the core falsification tests (whitening, ΛCDM null, ablation) with minimal Planck data:

```bash
python forensic_fingerprint/run_robustness_campaign.py \
    --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model data/planck_pr3/raw/COM_PowerSpect_CMB-TT-model_R3.01.txt
```

### Full Campaign Command

Run all tests including optional polarization and phase coherence:

```bash
python forensic_fingerprint/run_robustness_campaign.py \
    --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model data/planck_pr3/raw/COM_PowerSpect_CMB-TT-model_R3.01.txt \
    --planck_cov data/planck_pr3/raw/COM_PowerSpect_CMB-TT-covariance_R3.01.txt \
    --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_model data/wmap/raw/wmap_tt_model_9yr_v5.txt \
    --include_phase_coherence \
    --include_polarization \
    --ee_obs data/planck_pr3/raw/COM_PowerSpect_CMB-EE-full_R3.01.txt \
    --ee_model data/planck_pr3/raw/COM_PowerSpect_CMB-EE-model_R3.01.txt \
    --te_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TE-full_R3.01.txt \
    --te_model data/planck_pr3/raw/COM_PowerSpect_CMB-TE-model_R3.01.txt
```

### High-Confidence Run (Increased Monte Carlo Samples)

```bash
python forensic_fingerprint/run_robustness_campaign.py \
    --planck_obs data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model data/planck_pr3/raw/COM_PowerSpect_CMB-TT-model_R3.01.txt \
    --planck_cov data/planck_pr3/raw/COM_PowerSpect_CMB-TT-covariance_R3.01.txt \
    --mc_trials_whitening 50000 \
    --mc_trials_ablation 25000 \
    --n_lcdm_realizations 500 \
    --mc_trials_lcdm 2000
```

## Tests Included

The campaign runs the following independent falsification tests:

### Test #1: Whitening / Full Covariance (CRITICAL)
- **Purpose**: Test whether Δℓ = 255 survives proper covariance-aware whitening
- **Modes tested**: none, diagonal, block-diagonal, covariance (full)
- **Pass criteria**: Signal persists at Δℓ ≈ 255 (±1-2 bins) with p < 10⁻³ across all modes
- **Failure condition**: Signal disappears or shifts after whitening

### Test #2: Synthetic ΛCDM Null Controls (Anti-Overfitting)
- **Purpose**: Demonstrate that Δℓ = 255 does NOT appear generically in ΛCDM
- **Method**: Generate ≥100 synthetic ΛCDM realizations, run identical comb test
- **Pass criteria**: Δℓ ≈ 255 appears in ≤1% of ΛCDM realizations
- **Failure condition**: Δℓ ≈ 255 appears frequently in pure ΛCDM

### Test #3: ℓ-Range Ablation (Local Artifact Check)
- **Purpose**: Test whether signal is global or confined to specific multipole band
- **Ranges tested**: [30-800], [800-1500], [30-500], [500-1000], [1000-1500]
- **Pass criteria**: Δℓ ≈ 255 appears in ≥2 disjoint ranges with p < 0.01
- **Failure condition**: Signal exists only in one narrow window

### Test #4: Polarization Channels (OPTIONAL, High-Impact)
- **Purpose**: Test cross-channel coherence (TT vs EE vs TE)
- **Pass criteria**: Δℓ ≈ 255 appears coherently across channels
- **Note**: Requires EE and TE data files

### Test #5: Phase Coherence (OPTIONAL)
- **Purpose**: Test phase stability across datasets and preprocessing
- **Pass criteria**: Phase stable within ~15° across Planck/WMAP, raw/whitened
- **Note**: Requires WMAP data

## Command-Line Options

### Required Arguments
- `--planck_obs` - Planck TT observation file
- `--planck_model` - Planck TT model file

### Optional Data Files
- `--planck_cov` - Planck TT covariance matrix (enables full whitening test)
- `--wmap_obs` - WMAP TT observation file (for phase coherence)
- `--wmap_model` - WMAP TT model file
- `--wmap_cov` - WMAP covariance matrix
- `--ee_obs` - Planck EE observation file (for polarization)
- `--ee_model` - Planck EE model file
- `--te_obs` - Planck TE observation file
- `--te_model` - Planck TE model file

### Test Selection
- `--skip_whitening` - Skip whitening test (NOT RECOMMENDED)
- `--skip_lcdm_null` - Skip ΛCDM null test (NOT RECOMMENDED)
- `--skip_ablation` - Skip ablation test (NOT RECOMMENDED)
- `--include_polarization` - Run polarization test (requires EE/TE data)
- `--include_phase_coherence` - Run phase coherence test (requires WMAP)

### Test Parameters
- `--mc_trials_whitening` - MC trials for whitening (default: 10000)
- `--mc_trials_ablation` - MC trials for ablation (default: 5000)
- `--mc_trials_polarization` - MC trials for polarization (default: 10000)
- `--n_lcdm_realizations` - Number of ΛCDM realizations (default: 100)
- `--mc_trials_lcdm` - MC trials per ΛCDM realization (default: 1000)
- `--ell_min` - Minimum multipole (default: 30)
- `--ell_max` - Maximum multipole (default: 1500)

### Output
- `--output_dir` - Custom output directory (default: auto-generated timestamped)

## Output

The campaign generates:

### Primary Deliverable
- **`ROBUSTNESS_AND_FALSIFICATION.md`** - Consolidated report with:
  - Executive summary
  - Pass/fail summary table
  - Overall campaign verdict (PASS/FAIL/INCOMPLETE)
  - Detailed results for each test
  - Explicit failure documentation
  - Machine-readable format suitable for publication

### Supporting Files
- `campaign_metadata.json` - Campaign execution metadata
- Individual test result directories with timestamped subdirectories
- JSON files with numerical results
- Diagnostic plots and visualizations

### Directory Structure
```
forensic_fingerprint/out/robustness_campaign/YYYYMMDD_HHMMSS/
├── ROBUSTNESS_AND_FALSIFICATION.md  (PRIMARY DELIVERABLE)
├── campaign_metadata.json
└── (links to individual test results)

forensic_fingerprint/out/stress_tests/
├── whitening_YYYYMMDD_HHMMSS/
│   ├── whitening_comparison.md
│   ├── planck_whitened_results.json
│   └── plots/
├── lcdm_null_YYYYMMDD_HHMMSS/
│   ├── lcdm_null_distribution.json
│   ├── lcdm_null_comparison.md
│   └── plots/
├── ablation_YYYYMMDD_HHMMSS/
│   ├── ablation_results.json
│   ├── ablation_comparison.md
│   └── plots/
└── ...
```

## Execution Time

Estimated runtime (sequential execution):

- **Minimum campaign** (3 core tests): 1-3 hours
- **Full campaign** (all 5 tests): 3-6 hours
- **High-confidence run** (increased MC): 6-12 hours

*Actual time depends on system performance and MC sample sizes.*

## Interpretation Guidelines

### Overall Verdict Rules

| All Tests | Any Test Fails | Result |
|-----------|----------------|--------|
| ✓ PASS | No | **SIGNAL SURVIVED** - Upgrades to "candidate anomaly" |
| Mixed | Yes | **SIGNAL FAILED** - Hypothesis falsified |
| Incomplete | N/A | **INCOMPLETE** - Insufficient evidence |

### Tone and Language

Throughout all documentation and code, we use:

| ✓ USE | ✗ AVOID |
|-------|---------|
| "Candidate structural anomaly" | "Detected digital structure" |
| "Survives falsification" | "Proven" or "Confirmed" |
| "Replication required" | "Independently verified" |
| "Signal eliminates itself" | "Test failed" |

**This reflects the Popperian falsification paradigm.**

## Important Notes

### Scientific Integrity > Confirmation

- **DO NOT** tune parameters to enhance the signal
- **DO NOT** introduce new degrees of freedom
- **DO NOT** condition on outcomes
- **DO NOT** suppress or soften failures

All tests use the **SAME** comb-search algorithm and statistics as the baseline run.

### Successful Failure

**This task is successful even if the signal FAILS.**

A signal that fails falsification tests is:
- A scientific success (hypothesis was testable and falsifiable)
- Better than a false positive that wastes community resources
- Publishable as a null result

### Data Requirements

**Minimum** (core tests only):
- Planck TT observation file
- Planck TT model file

**Recommended** (for full campaign):
- Planck TT covariance matrix
- WMAP TT observation and model files
- Planck EE and TE files

**Data Download**:
```bash
# Planck PR3 data
bash tools/data_download/download_planck_pr3_cosmoparams.sh

# WMAP data (if needed)
# Follow WMAP download instructions
```

## Troubleshooting

### "File not found" errors
Ensure data files are downloaded and paths are correct.

### Memory errors
Reduce Monte Carlo samples:
```bash
--mc_trials_whitening 5000
--n_lcdm_realizations 50
```

### Missing dependencies
```bash
pip install numpy scipy matplotlib
```

### Test timeout
Individual tests have 2-hour timeout. If exceeded, try reducing MC samples or running tests individually.

## Citation

If you use this campaign in your work, please cite:

```
UBT Robustness & Falsification Campaign (2026)
Repository: https://github.com/DavJ/unified-biquaternion-theory
License: MIT (code) / CC BY-NC-ND 4.0 (docs)
```

## See Also

- `stress_tests/README.md` - Individual test documentation
- `stress_tests/COMPLETE_GUIDE.md` - Detailed test methodology
- `UBT_STRESS_TESTS.md` - Results consolidation template
- `PROTOCOL.md` - Pre-registered test protocol

---

**Last Updated**: 2026-01-11  
**Author**: UBT Research Team  
**License**: MIT (code) / CC BY-NC-ND 4.0 (documentation)
