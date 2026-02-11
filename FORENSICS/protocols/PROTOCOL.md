# UBT Forensic Fingerprint Protocol
**Version 1.0 - Pre-Registered**  
**Date**: 2026-01-10  
**Author**: UBT Research Team  
**License**: MIT License (code) / CC BY-NC-ND 4.0 (documentation)

## Purpose

This protocol defines three pre-registered, court-grade statistical tests to search for potential signatures of digital/lattice architecture in cosmological data that might be consistent with the Unified Biquaternion Theory (UBT). This is **not** a claim of discovery—it is a rigorous falsification protocol.

**Falsifiability Statement**: If these tests fail to show statistically significant signals after replication, the digital-architecture interpretation of UBT is falsified in this form.

---

## General Principles

### Pre-Registration
- All hypotheses, candidate parameters, significance thresholds, and analysis methods are **fixed before examining data**
- No p-hacking, no post-hoc parameter tuning
- Dataset identities and versions documented with cryptographic hashes
- Fixed random seeds for all Monte Carlo simulations

### Neutral Language
- Use "candidate signal" not "detection"
- Use "replication required" not "confirmed"
- Use "falsified if..." not "proven if..."
- Report all null results with equal prominence

### Reproducibility
- All code open-source with version tags
- All intermediate outputs saved with timestamps
- Analysis pipeline runs from raw data to final p-values
- Independent replication encouraged

---

## Test #1: CMB Comb Signature

### Scientific Hypothesis
**H0 (Null)**: CMB power spectrum residuals (observed - ΛCDM model) are consistent with Gaussian random noise with no periodic structure.

**H1 (Alternative)**: Residuals contain a sinusoidal oscillation at one of the candidate periods, suggesting a comb-like structure potentially arising from discrete spacetime architecture.

### Pre-Fixed Parameters

#### Candidate Periods
Δℓ ∈ {8, 16, 32, 64, 128, 255} (LOCKED - no additions or modifications)

**Rationale**: These span plausible discretization scales from fine (8) to coarse (255), with 255 chosen as the maximum based on potential byte/grid structure. This set is **pre-registered and fixed** - no additional candidate periods can be added based on data analysis.

#### Datasets
- **Primary**: Planck 2018 TT power spectrum (ℓ = 2 to 2500)
- **Replication**: 
  - Planck 2018 TE and EE spectra (if available)
  - WMAP 9-year TT spectrum (independent satellite)
  - Alternative Planck frequency maps (100 GHz vs 143 GHz)

#### Model
Residuals modeled as:
```
r_ℓ = (C_ℓ^obs - C_ℓ^ΛCDM) / σ_ℓ
r_ℓ ≈ A sin(2πℓ/Δℓ + φ) + noise
```

Fit via linear regression on cos(2πℓ/Δℓ) and sin(2πℓ/Δℓ) bases.

### Test Statistic
For each candidate period Δℓ:
1. Compute Δχ² = χ²(H0) - χ²(H1 with sinusoid)
2. Select **max(Δχ²)** across all candidate periods

### Significance Thresholds
- **Candidate (interesting)**: p < 0.01 (2.6σ equivalent)
- **Strong (publication-worthy)**: p < 2.9×10⁻⁷ (~5σ equivalent)
- **Replication required**: Signal must appear in at least 2 independent datasets

### Look-Elsewhere Correction
- Maximum statistic method: For each Monte Carlo trial, compute max(Δχ²) across all 6 candidate periods
- This accounts for trying multiple periods without Bonferroni over-correction
- P-value computed from empirical distribution of max(Δχ²) under H0

### Monte Carlo Null Distribution
1. Generate N = 10,000 synthetic residuals under H0:
   - Draw from Gaussian with same σ_ℓ as data (or full covariance if available)
2. For each trial:
   - Fit sinusoids at all candidate periods
   - Record max(Δχ²)
3. P-value = fraction of trials with max(Δχ²) ≥ observed max(Δχ²)

### Required Outputs
- Best-fit period Δℓ, amplitude A, phase φ
- Observed max(Δχ²) and p-value
- Histogram of MC null distribution
- Plot: residuals with fitted sinusoid overlaid
- Dataset hash (SHA-256 of input files)
- Random seed used for MC

---

## Test #2: Parameter Grid Quantization (1/255)

### Scientific Hypothesis
**H0 (Null)**: MCMC posterior samples for cosmological parameters are smooth and continuous, with no preferential alignment to rational grid m/255.

**H1 (Alternative)**: Parameters show statistically significant clustering near multiples of 1/255, suggesting quantization on a byte-like grid.

### Pre-Fixed Parameters

#### Grid Denominator
**D = 255** (LOCKED - no alternatives)

**Rationale**: 255 = 2⁸ - 1 is the maximum value in 8-bit unsigned representation (Galois field GF(2⁸)), potentially relevant if spacetime has digital substrate. This value is **pre-registered and fixed** - it cannot be changed based on data analysis results. Any future protocol with different denominator would require version 2.0.

#### Parameters to Test
Select from MCMC chains (Planck 2018 baseline):
- Ω_b h² (baryon density)
- Ω_c h² (cold dark matter density)
- θ_s (sound horizon angle)
- τ (optical depth)
- n_s (scalar spectral index)
- ln(10¹⁰ A_s) (primordial amplitude)

**Note**: Only parameters with physical prior support fully covering at least one grid cell tested.

#### Distance Metric
For each sample x, compute:
```
d(x) = min_{m ∈ ℤ} |x - m/255|
```
(Minimum distance to nearest grid point)

### Test Statistic
Two summary statistics:
1. **S₁ = median(d)**
2. **S₂ = mean(log₁₀ d)** (more sensitive to clustering near grid)

### Null Distribution
1. Fit smooth distribution to MCMC samples:
   - Use Kernel Density Estimate (KDE) with bandwidth chosen by Scott's rule
   - Or fit Gaussian approximation if unimodal
2. Resample N_samples from fitted distribution
3. Compute S₁_null and S₂_null on resampled data
4. Repeat 10,000 times to build null distributions

### Significance Thresholds
- **Candidate**: p < 0.01 (for either S₁ or S₂)
- **Strong**: p < 2.9×10⁻⁷
- **No look-elsewhere correction** needed here (denominator fixed a priori)

### Required Outputs
- S₁_obs, S₂_obs (observed statistics)
- P-values for both statistics
- Histogram of d(x) with null expectation overlaid
- KDE fit parameters
- MCMC chain hash and sample size

---

## Test #3: Cross-Dataset Invariance

### Scientific Hypothesis
**H0 (Null)**: UBT-predicted invariant quantities derived from different datasets are inconsistent, suggesting the mapping is ad hoc.

**H1 (Alternative)**: UBT invariants show statistical agreement across independent datasets (Planck, BAO, SNe, lensing), supporting theoretical coherence.

### Pre-Fixed UBT Invariant

Define one specific UBT invariant with fixed formula (example):

**Invariant κ**: Derived from baryon-photon ratio via UBT biquaternionic mapping
```
κ = f(Ω_b h²)
```
where f is a **fixed mathematical function** specified by UBT equations (must be documented in main theory).

Alternative invariant (if above not available):
**Phase Index η**: Derived from n_s via complex-time mapping
```
η = g(n_s)
```

### Datasets
- Planck 2018 TT,TE,EE + lowE
- BAO compilation (BOSS DR12 + eBOSS)
- Pantheon SNe Ia
- Planck lensing (2018)

Each dataset provides:
- Parameter estimate θ̂ ± σ_θ
- Derived invariant κ̂ ± σ_κ (via UBT formula)

### Test Statistic
Consistency chi-square:
```
χ² = Σᵢ (κ̂ᵢ - κ̄)² / σᵢ²
```
where:
- κ̄ = weighted mean of all κ̂ᵢ
- Sum over N datasets

**Degrees of freedom**: N - 1

P-value from χ²_{N-1} distribution.

### Significance Thresholds
- **Consistent (supports UBT)**: p > 0.05 (fail to reject consistency)
- **Inconsistent (falsifies UBT)**: p < 0.01 (strong evidence of inconsistency)

**Note**: This test is "backwards"—UBT is *supported* if p is large (datasets agree).

### Required Outputs
- κ̂ᵢ ± σᵢ for each dataset
- Weighted mean κ̄ and uncertainty
- χ² statistic and p-value
- Table comparing all estimates
- Dataset provenance (papers, data release versions)

---

## Data Provenance and Versioning

### Dataset Hashes
All input files must be documented with:
- File name
- SHA-256 hash
- Source URL
- Date downloaded
- Data release version

Example:
```
File: COM_PowerSpect_CMB-TT-full_R3.01.txt
SHA-256: a1b2c3d4...
Source: https://pla.esac.esa.int/pla/
Downloaded: 2026-01-10
Release: Planck 2018 Legacy
```

### Random Seeds
All Monte Carlo simulations use **fixed random seeds** documented in code (LOCKED):
```python
np.random.seed(42)  # CMB comb test - FIXED, DO NOT CHANGE
np.random.seed(137) # Grid test - FIXED, DO NOT CHANGE
```

These seeds are **pre-registered and must not be changed**. Different seeds would constitute a new protocol version.

### Output Versioning
All output files tagged with:
- Protocol version (v1.0)
- Timestamp (ISO 8601)
- Git commit hash of analysis code

---

## Reporting Standards

### Publication of Results
Both positive and null results reported with equal prominence:
- If p < 0.01: "Candidate signal detected, replication required"
- If p > 0.01: "No significant signal, H0 not rejected"
- If replication fails: "Initial signal not replicated, likely statistical fluctuation"

### Required Plots
1. **CMB Comb**: 
   - Residuals vs ℓ with fitted sinusoid
   - Histogram of MC null distribution with observed value marked
2. **Grid 255**:
   - Histogram of d(x) with null expectation
   - Q-Q plot comparing observed to null
3. **Invariance**:
   - Forest plot of κ estimates across datasets
   - Chi-square comparison table

### Archive Requirements
Upon completion, archive to public repository (Zenodo/OSF):
- This protocol document
- All code (with Git tags)
- All input data files (or links if too large)
- All output files
- Analysis log with timestamps

---

## Ethical Considerations

### No Cherry-Picking
- All datasets examined, even if results are null
- No selective reporting of "interesting" subsets
- No post-hoc exclusion of outliers without justification

### Correction for Negative Results
If initial results are null, this does **not** justify:
- Expanding candidate period list
- Changing grid denominator
- Redefining the UBT invariant
- Relaxing significance thresholds

Such changes would constitute a **new** pre-registered protocol (version 2.0).

### Independent Replication
External researchers encouraged to:
- Run this protocol on same/different datasets
- Propose alternative UBT invariants for Test #3
- Suggest improvements for version 2.0

---

## Summary Table

| Test | H0 | Test Statistic | Threshold (Candidate) | Threshold (Strong) | Look-Elsewhere Correction |
|------|-----|----------------|----------------------|-------------------|--------------------------|
| CMB Comb | No periodic structure | max(Δχ²) over Δℓ ∈ {8,16,32,64,128,255} | p < 0.01 | p < 2.9×10⁻⁷ | Max statistic in MC |
| Grid 255 | No quantization on m/255 grid | median(d) or mean(log d) | p < 0.01 | p < 2.9×10⁻⁷ | Not needed (fixed grid) |
| Invariance | UBT invariants inconsistent | χ² across datasets | p > 0.05 (consistent) | p > 0.32 (strong agreement) | N/A |

---

## Version History

- **v1.0** (2026-01-10): Initial pre-registered protocol

---

## Contact

For questions or replication requests:
- GitHub: https://github.com/DavJ/unified-biquaternion-theory
- Issues: Submit via GitHub issue tracker

---

**END OF PROTOCOL**
