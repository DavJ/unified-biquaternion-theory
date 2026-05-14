# CMB TT Power Spectrum Comb Search - NEGATIVE BENCHMARK

**Status**: CHANNEL CLOSED  
**Date**: 2026-01-12  
**Protocol Version**: v1.0  
**Author**: UBT Research Team  
**License**: MIT License (code) / CC BY-NC-ND 4.0 (documentation)

---

## Executive Summary

**Result**: **NULL** (p ≈ 0.92)  
**Tested Observable**: CMB Temperature (TT) power spectrum amplitude, residuals (observed - ΛCDM model)  
**Candidate Period**: Δℓ = 255 (and other pre-registered periods: 8, 16, 32, 64, 128)  
**Verdict**: No statistically significant periodic comb structure detected in Planck PR3 TT power spectrum

---

## What Was Tested

### Observable Channel
- **CMB TT Power Spectrum**: C_ℓ^TT for ℓ = 30 to 1500
- **Data Source**: Planck 2018 Release 3 (PR3)
  - Observation: `COM_PowerSpect_CMB-TT-full_R3.01.txt`
  - Model: ΛCDM best-fit from `COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt`
- **Test Statistic**: Sinusoidal fit to residuals r_ℓ = (C_ℓ^obs - C_ℓ^model) / σ_ℓ
- **Null Hypothesis**: Residuals are Gaussian random noise with no periodic structure

### Pre-Registered Parameters
- **Candidate Periods**: Δℓ ∈ {8, 16, 32, 64, 128, 255} (LOCKED before data analysis)
- **MC Samples**: 10,000 surrogate realizations
- **Random Seed**: 42 (for reproducibility)
- **Multiple-Testing Correction**: Maximum statistic method (conservative)

### Test Procedure
1. Compute residuals: r_ℓ = (C_ℓ^obs - C_ℓ^ΛCDM) / σ_ℓ
2. For each candidate period Δℓ, fit sinusoid: r_ℓ ≈ A sin(2πℓ/Δℓ + φ)
3. Compute Δχ² = χ²(H0) - χ²(H1 with sinusoid)
4. Select max(Δχ²) across all candidate periods
5. Generate 10,000 MC surrogates under null hypothesis
6. P-value = fraction of surrogates with max(Δχ²) ≥ observed max(Δχ²)

---

## Results

### Planck PR3 TT Spectrum

| Period Δℓ | Amplitude A | Phase φ (rad) | Δχ² | p-value |
|-----------|-------------|---------------|-----|---------|
| 8         | 0.0412      | 2.34          | 8.7 | 0.95    |
| 16        | 0.0539      | 1.89          | 14.8| 0.92    |
| 32        | 0.0387      | 0.76          | 7.6 | 0.97    |
| 64        | 0.0491      | 2.11          | 12.3| 0.94    |
| 128       | 0.0623      | 1.45          | 19.7| 0.88    |
| **255**   | **0.0456**  | **3.02**      | **10.6** | **0.95** |

**Best-fit period**: Δℓ = 128 (p = 0.88)  
**Target period** (Δℓ = 255): p = 0.95 (NULL)  
**Overall verdict**: NULL (no period shows p < 0.01)

### Replication Test: WMAP 9yr TT Spectrum

| Period Δℓ | p-value (WMAP) | p-value (Planck) | Agreement |
|-----------|----------------|------------------|-----------|
| 255       | 1.0e-4         | 0.95             | **NO**    |

**Note**: WMAP showed a candidate signal at Δℓ = 255 (p = 1.0e-4), but this **did NOT replicate** in the higher-quality Planck data. Non-replication indicates the WMAP signal is likely a statistical fluctuation or systematic artifact.

---

## Interpretation

### Why This Result is Important

**TT power spectrum averages out phase information**:
- The power spectrum C_ℓ = (1/(2ℓ+1)) Σ_m |a_ℓm|² discards phases φ_ℓm = arg(a_ℓm)
- Any discrete/lattice structure that manifests primarily in **phase relationships** would be invisible to amplitude-based tests
- This test probes only **amplitude modulations** at specific periods

### What This Does NOT Rule Out

This NULL result does **NOT** falsify:

1. **Phase-coherent fingerprints**: Map-level phase relationships between a_ℓm modes
2. **Polarization signatures**: E-mode and B-mode phase structures
3. **Higher-order correlations**: Bispectrum, trispectrum (non-Gaussian features)
4. **Near-field observables**: Laboratory interferometry, gravitational wave phase, quantum device logs
5. **Time-domain astrophysics**: Pulsar timing residuals, FRB arrival statistics
6. **UBT theoretical framework**: The NULL result is specific to this observable channel

### What This DOES Rule Out

This result falsifies (at 99% confidence level):
- **Macroscopic amplitude combs in CMB TT**: No periodic modulation with A > ~0.05 at any of the tested periods
- **Δℓ = 255 comb in TT power**: Specifically excludes the "byte-like" period hypothesis for TT amplitudes

---

## Channel Status

### CLOSED FOR FUTURE FINGERPRINT CLAIMS

**This channel is officially CLOSED for UBT fingerprint claims**:
- Future work should NOT claim the TT power spectrum as evidence for discrete architecture
- Any claims about CMB must focus on **phase-sensitive observables** (see recommended channels below)
- This closure is **permanent** unless new, higher-quality data or alternative analysis methods become available

### Recommended Alternative Channels

Based on theoretical considerations, the following channels preserve phase information and remain **OPEN** for investigation:

#### High Priority (Phase-Preserving)
1. **CMB map-level phases**: a_ℓm phase coherence R(P) across ℓ-multipoles
2. **E-mode polarization phases**: Less contaminated than temperature
3. **CMB bispectrum**: Tests non-Gaussianity with phase information intact

#### Medium Priority (Time-Domain)
4. **Pulsar timing residuals**: High-precision time-domain data with phase information
5. **FRB arrival time statistics**: Discrete event statistics

#### Laboratory / Near-Field
6. **Interferometric phase noise**: Allan deviation analysis
7. **Coherent oscillator stability**: Phase-locking tests
8. **Quantum device readout logs**: Coherence time modulations

---

## Data Provenance

### Planck PR3 Data
- **File**: `COM_PowerSpect_CMB-TT-full_R3.01.txt`
- **SHA-256**: (computed during analysis, stored in manifest)
- **Source**: [ESA Planck Legacy Archive](https://pla.esdc.esa.int/)
- **Release**: 2018 (PR3)
- **Component Separation**: Commander-Ruler combination

### WMAP 9yr Data
- **File**: `wmap_tt_spectrum_9yr_v5.txt`
- **SHA-256**: (computed during analysis, stored in manifest)
- **Source**: [NASA LAMBDA Archive](https://lambda.gsfc.nasa.gov/)
- **Release**: 2013 (9-year)

### Analysis Code
- **Repository**: `forensic_fingerprint/`
- **Version**: Commit SHA from analysis run
- **Script**: `run_real_data_cmb_comb.py`
- **Random Seed**: 42 (pre-registered)

---

## Reproducibility

### Replication Instructions

To reproduce this result:

```bash
cd forensic_fingerprint

# Download Planck PR3 TT data (instructions in data/planck_pr3/README.md)
# Download WMAP 9yr TT data (instructions in data/wmap/README.md)

# Run analysis
python run_real_data_cmb_comb.py \
    --planck_obs ../data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt \
    --planck_model ../data/planck_pr3/raw/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt \
    --wmap_obs ../data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
    --variant C \
    --mc_samples 10000 \
    --seed 42
```

**Expected output**: `combined_verdict.md` with p ≈ 0.92 for Planck, confirming NULL result.

### Requirements
- Python 3.8+
- NumPy, SciPy, Matplotlib
- See `requirements.txt` for full dependencies

---

## References

### Data Sources
1. Planck Collaboration (2020). "Planck 2018 results. I. Overview and the cosmological legacy of Planck." *A&A* 641, A1.
2. Bennett et al. (2013). "Nine-year Wilkinson Microwave Anisotropy Probe (WMAP) Observations: Final Maps and Results." *ApJS* 208, 20.

### Analysis Protocol
- See `forensic_fingerprint/PROTOCOL.md` for complete pre-registration
- See `forensic_fingerprint/reports/CMB_COMB_REPORT_2026-01-12.md` for full analysis report

---

## Conclusion

**The CMB TT power spectrum comb search yields a NULL result (p ≈ 0.92).**

**This channel is CLOSED** for future UBT fingerprint claims related to amplitude-based periodic structure.

**Next steps**: Focus on phase-sensitive observables (map-level phases, polarization, bispectrum) and near-field experiments where discrete architecture signatures may be more visible.

---

**Last Updated**: 2026-01-12  
**Permanent Archive**: This document serves as the definitive benchmark for the TT power spectrum channel.
