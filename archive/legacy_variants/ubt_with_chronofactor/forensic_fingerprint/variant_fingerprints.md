# UBT Variant Fingerprints: Falsifiable Observational Signatures

**Version**: 1.0  
**Date**: 2026-01-10  
**Purpose**: Define specific, falsifiable fingerprints for each architectural variant

---

## Overview

This document specifies **concrete, falsifiable observational signatures** for each UBT architectural variant defined in `ARCHITECTURE_VARIANTS.md`. Each fingerprint is:
1. **Specific**: Precisely defined observable
2. **Falsifiable**: Clear criterion for rejection
3. **Discriminating**: Separates at least two variants

---

## Fingerprint Catalog

### FP-A1: Continuous Parameter Space (Variant A)

**Hypothesis**: Cosmological parameters (Ω_b h², Ω_c h², n_s) are **continuously distributed** with NO preferential quantization on any rational grid.

**Observable**: MCMC posterior samples from Planck 2018 chains

**Test Statistic**:
```
For grid denominator D in {2, 3, 5, 7, 11, ..., 255, 256}:
    Compute d(x) = min_m |x - m/D| for each sample x
    Compute S = median(d)
    Generate null distribution from smooth fit
    P-value = P(S_null <= S_obs)
```

**Falsification Criteria:**
- **Supports Variant A**: p > 0.05 for ALL tested denominators D
- **Falsifies Variant A**: p < 0.01 for ANY denominator D
- **Inconclusive**: 0.01 <= p <= 0.05

**Discriminates Between:**
- Variant A (continuous) vs. Variant C (255-grid)
- Variant A vs. Variant B (if B predicts discrete parameter space)

**Applicable Data:**
- Planck 2018 MCMC chains
- Alternative cosmological parameter inferences (BAO, SNe)

---

### FP-B1: Broad-Band Cutoff Without Periodicity (Variant B)

**Hypothesis**: Energy/frequency spectrum shows a **sharp cutoff** at high energy/multipole but NO periodic modulation.

**Observable**: CMB power spectrum residuals (C_ℓ^obs - C_ℓ^ΛCDM) / σ_ℓ

**Test Procedure:**
1. Fit exponential cutoff model: R(ℓ) ~ exp(-ℓ/ℓ_cutoff)
2. Test for periodic structure on top of cutoff
3. Separate cutoff significance from periodicity

**Test Statistics:**
- Cutoff: Δχ²_cutoff from adding exponential term
- Periodicity: Δχ²_periodic from adding sinusoid after cutoff

**Falsification Criteria:**
- **Supports Variant B**: Δχ²_cutoff significant (p < 0.01) AND Δχ²_periodic NOT significant (p > 0.05)
- **Falsifies Variant B**: No cutoff (Δχ²_cutoff p > 0.05) OR strong periodicity (Δχ²_periodic p < 0.01)

**Discriminates Between:**
- Variant B (cutoff only) vs. Variant A (no cutoff)
- Variant B vs. Variant C (cutoff + periodicity)

**Applicable Data:**
- Planck 2018 TT/TE/EE spectra
- High-ℓ data from ACT/SPT if available

---

### FP-C1: Periodic Comb at Δℓ = 255 or Divisor (Variant C)

**Hypothesis**: CMB power spectrum residuals contain **sinusoidal oscillation** at period Δℓ tied to RS code length n = 255.

**Observable**: CMB power spectrum residuals

**Test Statistic**: Max(Δχ²) over candidate periods Δℓ ∈ {8, 16, 32, 64, 128, 255}

**Falsification Criteria:**
- **Supports Variant C**: p < 0.01 for at least ONE candidate period AND replication in independent dataset (WMAP or alternative)
- **Falsifies Variant C**: p > 0.05 for ALL candidate periods in Planck AND WMAP

**Replication Requirement**: Signal must appear in ≥2 independent datasets (per PROTOCOL.md)

**Discriminates Between:**
- Variant C (explicit sync) vs. Variant A (no structure)
- Variant C vs. Variant B (cutoff without periodicity)

**Applicable Data:**
- **Primary**: Planck 2018 TT/TE/EE
- **Replication**: WMAP 9-year, ACT DR4, SPT-3G

**Implementation**: `forensic_fingerprint/cmb_comb/cmb_comb.py` (ONLY run if variant=C selected)

---

### FP-C2: 255-Grid Quantization (Variant C)

**Hypothesis**: Cosmological parameters cluster preferentially near m/255 grid points.

**Observable**: MCMC posterior samples for Ω_b h², Ω_c h², θ_s, τ, n_s, ln(10¹⁰ A_s)

**Test Statistic**:
```
For each parameter x:
    d(x) = min_m |x - m/255|
    S₁ = median(d)
    S₂ = mean(log₁₀ d)
    Compare to null from smooth distribution
```

**Falsification Criteria:**
- **Supports Variant C**: p < 0.01 for S₁ or S₂ for ANY parameter
- **Falsifies Variant C**: p > 0.05 for ALL parameters

**Discriminates Between:**
- Variant C (255-grid) vs. Variant A (continuous)
- Different grid denominators (255 vs. 256, 127, etc.)

**Applicable Data:**
- Planck 2018 baseline MCMC chains

**Implementation**: `forensic_fingerprint/grid_255/grid_255.py`

---

### FP-C3: Sync Overhead in Planck Mapping (Variant C)

**Hypothesis**: If θ* (sound horizon angle) and σ_8 (matter fluctuations) can be derived from RS(255,200) + OFDM WITHOUT additional parameters, Variant C is supported.

**Observable**: Planck 2018 cosmological parameters

**Test Procedure:**
1. Derive M_phase(R=255, D=200) → θ* from architecture
2. Derive M_SNR(R=255, D=200) → σ_8 from architecture
3. Compare predictions to observations

**Falsification Criteria:**
- **Supports Variant C**: 
  - |z| <= 1 for θ* (within 1σ of Planck 2018)
  - |z| <= 1 for σ_8 (within 1σ of Planck 2018)
  - NO new free parameters introduced
- **Falsifies Variant C**:
  - Cannot derive M_phase or M_SNR from architecture
  - |z| > 3 for either parameter
  - Requires new tunable parameters

**Status**: TBD (currently NotImplementedError in `tools/planck_validation/mapping.py`)

**Discriminates Between:**
- Variant C (complete RS mapping) vs. partial agreement (semi-empirical)

---

### FP-D1: Scale-Dependent Decoherence of Periodicity (Variant D)

**Hypothesis**: Periodic structure exists at **small angular scales** (high ℓ) but **decoheres** at large scales (low ℓ).

**Observable**: CMB power spectrum residuals binned by angular scale

**Test Procedure:**
1. Divide multipole range into bins: ℓ ∈ [2-50], [50-500], [500-2500]
2. Test for periodic structure separately in each bin
3. Measure coherence/amplitude as function of scale

**Test Statistic**: Amplitude A(ℓ_bin) of best-fit sinusoid vs. ℓ_bin

**Falsification Criteria:**
- **Supports Variant D**: A(ℓ) decreases with decreasing ℓ (decoherence at large scales)
- **Falsifies Variant D**: A(ℓ) constant or increases at large scales (no decoherence)

**Discriminates Between:**
- Variant D (hierarchical) vs. Variant C (scale-independent periodicity)
- Variant D vs. Variant A (no structure at any scale)

**Applicable Data:**
- Planck 2018 with binning strategy
- Combined Planck + high-ℓ experiments (ACT/SPT)

---

### FP-D2: Local Sync Domains in Lensing (Variant D)

**Hypothesis**: Gravitational lensing reveals **local coherent regions** with distinct sync phases.

**Observable**: Planck lensing convergence map

**Test Procedure:**
1. Compute local power spectra in patches across sky
2. Search for phase variations between patches
3. Measure characteristic domain size

**Test Statistic**: Variance of phase φ across sky patches

**Falsification Criteria:**
- **Supports Variant D**: σ_φ > σ_null (significant phase variation), domain size ~ predicted decoherence scale
- **Falsifies Variant D**: σ_φ ~ σ_null (phase-locked globally), or domain size << predicted

**Discriminates Between:**
- Variant D (local domains) vs. Variant C (global sync)

**Applicable Data:**
- Planck 2018 lensing
- Future: CMB-S4, Simons Observatory

---

## Cross-Variant Discriminators

### CVD-1: n_s Exact Formula Test

**Applicable to**: Variants C and D primarily

**Prediction**: 
- Variant C: n_s = 1 - 9/255 = 0.9647 (exact)
- Variant A/B: n_s emergent (no exact formula)

**Observable**: Planck 2018 n_s = 0.9649 ± 0.0042

**Test**: 
```
z = (n_s_pred - n_s_obs) / σ_ns
Variant C: z = (0.9647 - 0.9649) / 0.0042 ≈ -0.048
```

**Interpretation:**
- |z| < 1: Consistent with Variant C (exact formula)
- |z| > 3: Falsifies Variant C exact formula

**Current Status**: Variant C supported (|z| ≈ 0.05 << 1)

---

### CVD-2: Parameter Count Parsimony

**Applicable to**: All variants

**Test**: Count independent fundamental parameters

| Variant | Fundamental Parameters | Emergent | Total Predictions |
|---------|----------------------|----------|-------------------|
| **A** | 0 (pure geometry) | h, c, G, all observables | Infinite (all from Θ) |
| **B** | 1 (Δ𝒮_state) | c, G, observables | Many |
| **C** | 3 (n=255, k=200, OFDM=16) | h, c, G, 5 cosmological params | 5+ |
| **D** | 4 (n, k, OFDM, ξ_decoherence) | Same as C + scale | 5+ with scale dependence |

**Interpretation** (via Bayesian model selection or AIC):
- **More parsimonious** (fewer parameters): Higher prior probability
- **More predictive** (more observables from same parameters): Higher likelihood
- **Trade-off**: Variant A most parsimonious, Variant C most predictive

---

## Fingerprint Matrix

| Fingerprint | Variant A | Variant B | Variant C | Variant D |
|-------------|-----------|-----------|-----------|-----------|
| FP-A1 (Continuous) | ✓ Support | ? Partial | ✗ Falsify | ? Partial |
| FP-B1 (Cutoff only) | ✗ Falsify | ✓ Support | ✗ Falsify | ? Partial |
| FP-C1 (CMB comb) | ✗ Falsify | ✗ Falsify | ✓ Support | ? Partial |
| FP-C2 (255-grid) | ✗ Falsify | ? Partial | ✓ Support | ? Local |
| FP-C3 (Planck map) | ✗ (TBD) | ✗ (TBD) | ✓ (TBD) | ? (TBD) |
| FP-D1 (Decoherence) | ✗ Falsify | ✗ Falsify | ✗ Falsify | ✓ Support |
| FP-D2 (Local domains) | ✗ Falsify | ✗ Falsify | ✗ Falsify | ✓ Support |

Legend:
- ✓ Support: Fingerprint presence supports variant
- ✗ Falsify: Fingerprint presence falsifies variant
- ? Partial: Variant-dependent or intermediate behavior
- (TBD): Not yet testable

---

## Testing Priority

### Immediate (Data Available, Code Ready)

1. **FP-C1**: CMB comb test (Planck 2018 data available)
2. **FP-C2**: 255-grid quantization (MCMC chains available)
3. **CVD-1**: n_s exact formula (already calculated)

### Near-Term (Data Available, Code Development Needed)

4. **FP-A1**: Continuous parameter space (multi-denominator grid test)
5. **FP-B1**: Broad-band cutoff (requires new analysis)
6. **FP-C3**: Planck mapping completion (M_phase, M_SNR derivation)

### Long-Term (Future Data or Advanced Analysis)

7. **FP-D1**: Scale-dependent decoherence (requires binning analysis)
8. **FP-D2**: Local sync domains (requires lensing analysis)
9. **CVD-2**: Bayesian model selection (requires full likelihood)

---

## Reporting Standards

For each fingerprint test:

**Required Outputs:**
1. Test statistic value(s)
2. P-value (or Bayesian evidence)
3. Null distribution plot
4. Data vs. prediction plot
5. Interpretation statement (support/falsify/inconclusive)

**Language:**
- ✓ "Fingerprint FP-C1 is consistent with Variant C (p = 0.008)"
- ✓ "We find no evidence for Variant A (FP-A1 rejected, p < 0.001)"
- ✗ "Variant C is proven by FP-C1"
- ✗ "The universe uses explicit synchronization"

---

## Falsification Summary

### Variant A (Continuous)
**Falsified if**: ANY of FP-C1, FP-C2, FP-D1, FP-D2 show p < 0.01

### Variant B (Implicit Sync)
**Falsified if**: FP-C1 (comb) shows p < 0.01 OR FP-B1 (cutoff) fails (p > 0.05)

### Variant C (Explicit Sync)
**Falsified if**: ALL of FP-C1, FP-C2, FP-C3 fail (p > 0.05 or cannot derive)

### Variant D (Hierarchical)
**Falsified if**: FP-D1 OR FP-D2 fail (no decoherence or no local domains)

---

## Related Documents

- `ARCHITECTURE_VARIANTS.md` - Variant definitions and assumptions
- `PROTOCOL.md` - Pre-registered test protocols
- `forensic_fingerprint/cmb_comb/` - FP-C1 implementation
- `forensic_fingerprint/grid_255/` - FP-C2 implementation
- `tools/planck_validation/` - FP-C3 (partial) implementation

---

**Version History:**
- **v1.0** (2026-01-10): Initial fingerprint definitions

**Authors**: UBT Research Team  
**License**: CC BY-NC-ND 4.0 (documentation)
