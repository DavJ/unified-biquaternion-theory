# UBT Forensic Fingerprint - Stress Test Results
**Version**: 1.0  
**Date**: 2026-01-11  
**Author**: UBT Research Team  
**License**: MIT (code) / CC BY-NC-ND 4.0 (documentation)

---

## Executive Summary

This document consolidates results from **four independent, falsification-oriented stress tests** applied to the candidate structural anomaly at Δℓ ≈ 255 in CMB power spectrum residuals.

**Objective**: Actively attempt to destroy the signal through rigorous testing. Only survival across ALL tests upgrades the candidate status from "initial observation" to "replicated anomaly."

**Critical Disclaimer**: This analysis uses the language of "candidate structural anomaly" throughout. **No claims of discovery are made**. All results are presented as falsification tests, not confirmations.

---

## Test Summary

| Test | Name | Status | Result |
|------|------|--------|--------|
| **#1** | Whitening / Full Covariance | ☐ PENDING | Results: TBD |
| **#2** | Polarization Channels (EE, TE) | ☐ PENDING | Results: TBD |
| **#3** | ℓ-Range Ablation | ☐ PENDING | Results: TBD |
| **#4** | Synthetic ΛCDM Null Controls | ☐ PENDING | Results: TBD |
| **#5** | Phase Coherence | ☐ PENDING | Results: TBD |

**Overall Verdict**: ☐ PENDING

---

## Test #1: Whitening / Full Covariance

### Rationale
The initial analysis uses diagonal uncertainties only. Correlated noise and mode coupling could create spurious periodic signals. This test validates the signal against covariance-aware whitening.

### Methodology
- Run CMB comb test with four whitening modes:
  1. `none` - No whitening (raw residuals)
  2. `diagonal` - Diagonal uncertainties only (baseline)
  3. `block-diagonal` - Approximate covariance with local correlations
  4. `covariance` - Full covariance matrix (if available)
- Compare best-fit Δℓ, amplitude, phase, p-value across modes
- Generate comparison plots

### PASS / FAIL Criteria
- **PASS**: Peak remains at Δℓ ≈ 255 (±1–2 bins) with p < 10⁻³ across all modes
- **FAIL**: Peak disappears or shifts arbitrarily after whitening

### Results

*To be filled after running:*
```bash
python forensic_fingerprint/stress_tests/test_1_whitening.py \
    --obs data/planck_pr3/raw/spectrum.txt \
    --model data/planck_pr3/raw/model.txt \
    --mc_trials 10000
```

**Status**: ☐ PENDING  
**Verdict**: TBD

**Interpretation**: _Results will be added here after test completion._

---

## Test #2: Polarization Channels (EE, TE)

### Rationale
A genuine structural/digital fingerprint must propagate to polarization channels. Instrumental or scalar TT-only artifacts generally will NOT appear in EE or TE.

### Methodology
- Load Planck EE and TE power spectra
- Apply identical CMB comb test to each channel independently:
  - Same Δℓ scan range [8, 16, 32, 64, 128, 255]
  - Same Monte Carlo null size
  - No retuning of parameters
- Compare results with TT channel

### PASS / FAIL Criteria
- **STRONG PASS**: Δℓ ≈ 255 appears in EE and/or TE with p ≤ 10⁻³
- **WEAK PASS**: Δℓ ≈ 255 appears with reduced amplitude but aligned phase
- **FAIL**: No structure near 255 in polarization channels

### Results

*To be filled after running:*
```bash
python forensic_fingerprint/stress_tests/test_2_polarization.py \
    --tt_obs data/planck_pr3/raw/TT_spectrum.txt \
    --tt_model data/planck_pr3/raw/TT_model.txt \
    --ee_obs data/planck_pr3/raw/EE_spectrum.txt \
    --ee_model data/planck_pr3/raw/EE_model.txt \
    --te_obs data/planck_pr3/raw/TE_spectrum.txt \
    --te_model data/planck_pr3/raw/TE_model.txt \
    --mc_trials 10000
```

**Status**: ☐ PENDING  
**Verdict**: TBD

**Interpretation**: _Results will be added here after test completion._

---

## Test #3: ℓ-Range Ablation

### Rationale
A genuine structural signal must not depend on a single narrow ℓ window. It should manifest across multiple independent multipole ranges.

### Methodology
- Run CMB comb test on five disjoint ℓ ranges:
  1. ℓ ∈ [30, 800] - Low-ℓ only
  2. ℓ ∈ [800, 1500] - High-ℓ only
  3. ℓ ∈ [30, 500] - Very low-ℓ
  4. ℓ ∈ [500, 1000] - Mid-ℓ
  5. ℓ ∈ [1000, 1500] - Very high-ℓ
- Recompute null distribution for each range
- Generate heatmap of p-value vs ℓ-range

### PASS / FAIL Criteria
- **PASS**: Δℓ ≈ 255 appears in multiple (≥2) disjoint ℓ ranges with p < 0.01
- **FAIL**: Signal exists only in one narrow window

### Results

*To be filled after running:*
```bash
python forensic_fingerprint/stress_tests/test_3_ablation.py \
    --obs data/planck_pr3/raw/spectrum.txt \
    --model data/planck_pr3/raw/model.txt \
    --mc_trials 5000
```

**Status**: ☐ PENDING  
**Verdict**: TBD

**Interpretation**: _Results will be added here after test completion._

---

## Test #4: Synthetic ΛCDM Null Controls

### Rationale
We must demonstrate that ΛCDM realizations do NOT generically produce Δℓ = 255. If they do, the real-data signal is not anomalous.

### Methodology
- Generate ≥100 synthetic TT spectra from ΛCDM:
  - Same ℓ range as real data
  - Same noise model (σ from observations)
  - No UBT structure injected
- Apply identical comb test pipeline to each realization
- Count how often Δℓ ≈ 255 appears as best-fit
- Generate histogram of best-fit periods

### PASS / FAIL Criteria
- **PASS**: Δℓ ≈ 255 appears in ≤1% of ΛCDM realizations
- **FAIL**: Δℓ ≈ 255 appears frequently in pure ΛCDM (>5%)

### Results

*To be filled after running:*
```bash
python forensic_fingerprint/stress_tests/test_4_lcdm_null.py \
    --model data/planck_pr3/raw/model.txt \
    --obs data/planck_pr3/raw/spectrum.txt \
    --n_realizations 200 \
    --mc_trials 1000
```

**Status**: ☐ PENDING  
**Verdict**: TBD

**Interpretation**: _Results will be added here after test completion._

---

## Test #5: Phase Coherence

### Rationale
If the Δℓ = 255 signal is a genuine structural feature, its phase should be stable across:
- Different datasets (Planck vs WMAP)
- Different preprocessing (raw diagonal vs covariance-whitened)

Random noise or uncorrelated instrumental artifacts would produce random phases.

### Methodology
- Extract phase φ for Δℓ = 255 from multiple conditions:
  - Planck TT (diagonal whitening)
  - Planck TT (covariance whitening, if available)
  - WMAP TT (diagonal whitening)
  - WMAP TT (covariance whitening, if available)
- Compute circular statistics:
  - Circular mean and standard deviation
  - Phase coherence score (mean resultant length)
  - Pairwise phase differences
- Test for coherent alignment vs random distribution

### PASS / FAIL Criteria
- **PASS**: Phase stable within ~15° (circular std dev ≤ 15°), coherence score ≥ 0.9
- **FAIL**: Phase is random or varies > 30° between datasets/modes

### Skeptic One-Liner
"If the Δℓ = 255 signal were caused by random noise or uncorrelated instrumental 
artifacts, phase would be random across datasets. Coherent phase across Planck 
and WMAP, both raw and whitened, would suggest a physical or systematic origin. 
It does or does not."

### Results

*To be filled after running:*
```bash
python forensic_fingerprint/stress_tests/test_5_phase_coherence.py \
    --planck_obs data/planck_pr3/raw/TT_spectrum.txt \
    --planck_model data/planck_pr3/raw/TT_model.txt \
    --planck_cov data/planck_pr3/raw/TT_covariance.txt \
    --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --wmap_model data/wmap/raw/wmap_tt_model_9yr_v5.txt \
    --ell_min 30 --ell_max 800
```

**Status**: ☐ PENDING  
**Verdict**: TBD

**Interpretation**: _Results will be added here after test completion._

---

## Overall Assessment

### Falsification Status

*This section will be updated after all tests complete.*

**Criteria for "Survives Falsification"**:
- ALL five tests must PASS
- Any FAIL result invalidates the candidate

**Current Status**: ☐ PENDING

---

## Explicit Falsification Statement

**This result [survives / does not survive] falsification attempts.**

### If All Tests PASS:
The candidate structural anomaly at Δℓ ≈ 255 survives five independent falsification tests:
1. It persists under covariance-aware whitening
2. It propagates to polarization channels (if tested)
3. It appears in multiple disjoint ℓ ranges
4. It is rare in pure ΛCDM simulations
5. It exhibits coherent phase across datasets and preprocessing

**This does NOT constitute proof.** It upgrades the status from "initial observation" to "replicated anomaly requiring independent verification."

**Next steps**:
- Independent replication with different CMB datasets (e.g., ACT, SPT)
- Theoretical modeling of mechanism
- Publication with full transparency and code release

### If Any Test FAILS:
The candidate structural anomaly at Δℓ ≈ 255 does NOT survive stress testing.

**Failure modes**:
- Test #1 FAIL: Signal is an artifact of ignoring error correlations
- Test #2 FAIL: Signal is instrumental or scalar TT-only artifact
- Test #3 FAIL: Signal is ℓ-window dependent, likely statistical fluctuation
- Test #4 FAIL: Signal is a generic feature of ΛCDM, not anomalous
- Test #5 FAIL: Signal has random/unstable phase, indicating noise origin

**Conclusion**: The hypothesis of a discrete spacetime structure imprinting on CMB is falsified in this form.

---

## Important Notes on Terminology

Throughout this analysis, we use:
- **"Candidate structural anomaly"** - NOT "detected digital structure"
- **"Survives falsification"** - NOT "proven" or "confirmed"
- **"Replication required"** - NOT "independently verified"
- **"Consistent with hypothesis"** - NOT "validates theory"

This language reflects the **Popperian falsification paradigm** where scientific claims must be testable and potentially falsifiable.

---

## Code Availability

All stress test scripts are available in:
```
forensic_fingerprint/stress_tests/
├── test_1_whitening.py
├── test_2_polarization.py
├── test_3_ablation.py
├── test_4_lcdm_null.py
└── test_5_phase_coherence.py
```

**License**: MIT  
**Reproducibility**: Fixed random seeds, version-controlled analysis pipeline  
**Transparency**: Full methodology documented in code comments

---

## Data Provenance

All tests use:
- **Planck PR3 (Release 3)** TT, EE, TE power spectra
- **ΛCDM best-fit model** from Planck Collaboration
- **SHA-256 validated datasets** (where manifests available)

See `forensic_fingerprint/RUNBOOK_REAL_DATA.md` for data download instructions.

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-11 | Initial template created |

---

**End of Report**

*This document will be updated with actual test results as they become available.*
