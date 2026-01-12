# Forensic Fingerprint Search Space

**Purpose**: Define and classify all candidate observable channels for discrete/lattice architecture signatures  
**Status**: Living document - updated as channels are tested  
**Version**: 1.0  
**Date**: 2026-01-12  
**License**: MIT License (code) / CC BY-NC-ND 4.0 (documentation)

---

## Overview

This document catalogs all candidate observables where a "fingerprint" of underlying digital or relational structure might be detectable. We systematically classify channels by:

1. **Distance from source**: Early universe → present-day laboratory
2. **Phase preservation**: Does the observable retain phase information?
3. **Wash-out risk**: Likelihood that cosmic evolution or systematics erase signal
4. **Expected fingerprint visibility**: Theoretical prediction for signal strength

**Purpose**: Avoid data dredging by documenting the complete search space upfront.

---

## Search Space Classification Table

### A) Cosmology / Cosmic Microwave Background

| Channel | Distance | Phase Preservation | Wash-out Risk | Visibility | Status | Priority |
|---------|----------|-------------------|---------------|------------|--------|----------|
| **TT power spectrum (amplitude)** | Early universe (z~1100) | **NO** (phases averaged out) | Medium | Low | **CLOSED** (NULL) | N/A |
| **CMB map-level phases** (a_ℓm) | Early universe (z~1100) | **YES** (direct phase access) | Low | Medium-High | **OPEN** | **HIGH** |
| **E-mode polarization phases** | Early universe (z~1100) | **YES** | Low | Medium | **OPEN** | **HIGH** |
| **B-mode polarization phases** | Early universe (z~1100) | **YES** | Low | High (if detected) | **OPEN** | Medium |
| **CMB bispectrum** (3-point function) | Early universe (z~1100) | **YES** (partial) | Medium | Medium | **OPEN** | Medium |
| **CMB trispectrum** (4-point function) | Early universe (z~1100) | **YES** (partial) | Medium-High | Low | **OPEN** | Low |
| **Lensing convergence map phases** | Late universe (z<2) | Partial | Medium | Low | **OPEN** | Low |
| **Planck frequency map comparison** | Early universe (z~1100) | **YES** | Low | Medium | **OPEN** | Medium |
| **Component separation residuals** (SMICA/NILC/SEVEM) | Early universe (z~1100) | Partial | Medium | Low-Medium | **OPEN** | Medium |

**Notes**:
- **TT power spectrum (CLOSED)**: Tested on Planck PR3 + WMAP 9yr. NULL result (p ≈ 0.92). See `reports/CMB_TT_NEGATIVE_BENCHMARK.md`.
- **Map-level phases**: PRIMARY HIGH-PRIORITY TARGET. Preserves full phase information lost in power spectrum.
- **E-mode polarization**: Less contaminated by foregrounds than temperature. High priority.
- **Bispectrum**: Tests non-Gaussianity with phase information. Computationally expensive but theoretically motivated.

---

### B) Large-Scale Structure / Galaxy Surveys

| Channel | Distance | Phase Preservation | Wash-out Risk | Visibility | Status | Priority |
|---------|----------|-------------------|---------------|------------|--------|----------|
| **Matter power spectrum P(k)** | Late universe (z<1) | NO (phases averaged) | High | Low | **OPEN** | Low |
| **Galaxy 3D position phases** | Late universe (z<1) | **YES** | High | Low | **OPEN** | Low |
| **Baryon Acoustic Oscillations (BAO) scale** | Late universe (z<2) | Partial | Medium | Low | **OPEN** | Low |
| **Redshift-space distortions** | Late universe (z<1) | Partial | High | Low | **OPEN** | Low |
| **Weak lensing shear phases** | Late universe (z<2) | **YES** | Medium | Low | **OPEN** | Low |

**Notes**:
- **Wash-out risk is HIGH**: Nonlinear gravitational evolution, baryonic feedback, and galaxy formation physics scramble primordial phase information.
- **Lower priority** than CMB due to contamination and complexity.

---

### C) Astrophysical Time-Domain

| Channel | Distance | Phase Preservation | Wash-out Risk | Visibility | Status | Priority |
|---------|----------|-------------------|---------------|------------|--------|----------|
| **Pulsar timing residuals** | Galactic (kpc scale) | **YES** (nanosecond precision) | Low | Medium-High | **OPEN** | **HIGH** |
| **Pulsar timing array (PTA) phase correlations** | Galactic (kpc scale) | **YES** | Low | Medium | **OPEN** | Medium |
| **Fast Radio Burst (FRB) arrival times** | Cosmological (Gpc scale) | **YES** (discrete events) | Medium | Medium | **OPEN** | Medium |
| **FRB dispersion measure (DM) quantization** | Cosmological (Gpc scale) | Partial | Medium | Low | **OPEN** | Low |
| **Gamma-ray burst (GRB) arrival times** | Cosmological (Gpc scale) | **YES** (discrete events) | Medium | Low | **OPEN** | Low |
| **Type Ia supernova light curve phases** | Cosmological (Gpc scale) | Partial | High | Low | **OPEN** | Low |

**Notes**:
- **Pulsar timing residuals**: EXCELLENT phase preservation with ns-level precision. High priority.
- **FRBs**: Discrete event statistics may reveal quantization. Medium priority.
- **PTAs**: Correlated timing residuals across many pulsars can test phase-locking hypotheses.

---

### D) Gravitational Waves

| Channel | Distance | Phase Preservation | Wash-out Risk | Visibility | Status | Priority |
|---------|----------|-------------------|---------------|------------|--------|----------|
| **LIGO/Virgo waveform phases** | Cosmological (Gpc scale) | **YES** (direct phase measurement) | Low | Medium-High | **OPEN** | **HIGH** |
| **Gravitational wave ringdown phase** | Cosmological (Gpc scale) | **YES** | Low | Medium | **OPEN** | Medium |
| **Stochastic GW background phases** | Early universe (z>100?) | **YES** | Low (if primordial) | High (if detected) | **OPEN** | High |
| **Pulsar timing array GW phase** | Cosmological (Gpc scale) | **YES** | Low | Medium | **OPEN** | Medium |

**Notes**:
- **GW waveforms**: Direct phase measurement with excellent precision. High priority.
- **Ringdown**: Black hole quasi-normal mode frequencies may reveal discretization.
- **Stochastic background**: If primordial, could carry early-universe phase information.

---

### E) Near-Field / Laboratory Experiments

| Channel | Distance | Phase Preservation | Wash-out Risk | Visibility | Status | Priority |
|---------|----------|-------------------|---------------|------------|--------|----------|
| **Atomic clock stability (Allan deviation)** | Laboratory (m scale) | **YES** | Very Low | High | **OPEN** | **HIGH** |
| **Optical interferometer phase noise** | Laboratory (m scale) | **YES** | Very Low | High | **OPEN** | **HIGH** |
| **Laser frequency comb stability** | Laboratory (m scale) | **YES** | Very Low | High | **OPEN** | **HIGH** |
| **Maser coherence time** | Laboratory (m scale) | **YES** | Very Low | Medium | **OPEN** | Medium |
| **Superconducting cavity phase fluctuations** | Laboratory (m scale) | **YES** | Very Low | High | **OPEN** | High |
| **Josephson junction voltage quantization** | Laboratory (μm scale) | **YES** | Very Low | High | **OPEN** | Medium |
| **Quantum Hall effect resistance quantization** | Laboratory (μm scale) | **YES** | Very Low | Medium | **OPEN** | Low |
| **Rydberg atom microwave transitions** | Laboratory (m scale) | **YES** | Very Low | Medium | **OPEN** | Medium |
| **Quantum computer coherence logs** | Laboratory (μm scale) | **YES** | Very Low | Medium-High | **OPEN** | Medium |
| **Trapped ion motion phases** | Laboratory (μm scale) | **YES** | Very Low | Medium | **OPEN** | Low |

**Notes**:
- **Laboratory channels are HIGHEST PRIORITY for controlled experiments**: Zero wash-out risk, direct phase access, repeatable.
- **Atomic clocks**: State-of-the-art stability ~10⁻¹⁸ level. Ideal for detecting periodic phase noise.
- **Interferometers**: Direct phase measurement with sub-wavelength precision.
- **Quantum devices**: Coherence and decoherence timescales may reveal discrete phase structure.

---

### F) Particle Physics / High-Energy

| Channel | Distance | Phase Preservation | Wash-out Risk | Visibility | Status | Priority |
|---------|----------|-------------------|---------------|------------|--------|----------|
| **Neutrino oscillation phases** | Laboratory to Gpc | **YES** | Low | Medium | **OPEN** | Medium |
| **Meson oscillation phases** (K⁰, B⁰, D⁰) | Laboratory (m-km scale) | **YES** | Low | Low | **OPEN** | Low |
| **Lepton number violation phase (0νββ)** | Laboratory (m scale) | **YES** | Very Low | Low (if detected) | **OPEN** | Low |
| **CP-violating phase measurements** | Laboratory (m scale) | **YES** | Very Low | Low | **OPEN** | Low |

**Notes**:
- **Neutrino oscillations**: Well-measured phases but limited precision. Medium priority.
- **CP violation**: Theoretically interesting but signal strength unknown.

---

### G) Solar System / Planetary

| Channel | Distance | Phase Preservation | Wash-out Risk | Visibility | Status | Priority |
|---------|----------|-------------------|---------------|------------|--------|----------|
| **Planetary orbital phases** | AU scale | **YES** | Very Low | Low | **OPEN** | Low |
| **Lunar laser ranging timing** | Earth-Moon (km scale) | **YES** | Very Low | Low | **OPEN** | Low |
| **GPS satellite clock phase drift** | Orbital (km scale) | **YES** | Very Low | Medium | **OPEN** | Medium |
| **Solar oscillation (helioseismology) phases** | Solar (Mm scale) | **YES** | Low | Low | **OPEN** | Low |

**Notes**:
- **GPS clocks**: High-precision timing data available. Medium priority.
- **Lunar ranging**: cm-level precision but unclear signal expectation.

---

## Channel Status Definitions

### CLOSED
- **Tested and NULL result**: No significant signal detected at pre-registered significance threshold.
- **Not to be re-tested** unless new data or methods become available.
- **Example**: CMB TT power spectrum (p ≈ 0.92)

### OPEN
- **Not yet tested**, or testing in progress.
- Available for future exploratory or confirmatory tests.

### CANDIDATE
- **Exploratory signal detected** (e.g., p < 0.01 but not court-grade confirmed).
- Requires independent replication before claiming detection.

### CONFIRMED
- **Replicated signal** across multiple independent datasets.
- Meets court-grade confirmation criteria (p < 2.9×10⁻⁷, ~5σ).
- Requires follow-up investigation and interpretation.

---

## Priority Rankings

### HIGH Priority (Recommended Next Targets)
1. **CMB map-level phases** (a_ℓm phase coherence)
2. **Atomic clock Allan deviation** (laboratory phase noise)
3. **Optical interferometer phase noise** (laboratory)
4. **Pulsar timing residuals** (astrophysical time-domain)
5. **LIGO/Virgo GW waveform phases** (cosmological phase measurement)
6. **E-mode CMB polarization phases**

**Rationale**: Excellent phase preservation, low wash-out risk, high theoretical motivation, accessible data.

### MEDIUM Priority
7. CMB bispectrum (non-Gaussian phase structure)
8. FRB arrival time statistics
9. Laser frequency comb stability
10. GPS satellite clock phase drift
11. Superconducting cavity phase fluctuations

**Rationale**: Good phase preservation but higher complexity or lower data availability.

### LOW Priority
12. Matter power spectrum (phases averaged out)
13. Neutrino oscillation phases (limited precision)
14. Galaxy survey phases (high wash-out)
15. Planetary orbital phases (unclear signal expectation)

**Rationale**: Either poor phase preservation, high wash-out, or unclear theoretical motivation.

---

## Theoretical Considerations

### Why Phase Information Matters

**Power spectra and correlation functions average out phases**:
- Power spectrum: C_ℓ = (1/(2ℓ+1)) Σ_m |a_ℓm|² → phases φ_ℓm = arg(a_ℓm) are discarded
- If discrete architecture manifests as **phase relationships** (e.g., periodic phase-locking), amplitude-based tests will miss it.

**Map-level phases preserve full information**:
- Direct access to φ_ℓm allows testing phase coherence across ℓ-modes
- Can search for periodic phase differences: Δφ_ℓm(P) = φ_{ℓ+P,m} - φ_{ℓ,m}
- Phase-coherence statistic: R(P) = |mean(exp(i Δφ_ℓm(P)))|

### Why Near-Field Experiments Are Critical

**Laboratory experiments have zero wash-out**:
- No cosmic evolution to scramble phase information
- Controlled, repeatable conditions
- Direct access to phase measurements
- Can test specific frequencies and periods

**Examples**:
- Atomic clock stability: Look for periodic modulation in Allan deviation
- Interferometer phase noise: Search for comb-like structure in phase power spectrum
- Quantum coherence: Test for periodic decoherence timescales

---

## Progressive Hypothesis Narrowing Strategy

### Phase 1: Exploratory Scan (Current)
- **Goal**: Detect candidate anomalies across broad search space
- **Method**: Low-commitment tests with p < 0.01 threshold
- **Output**: List of CANDIDATE channels for confirmatory follow-up

### Phase 2: Confirmatory Tests
- **Goal**: Replicate candidates with court-grade rigor
- **Method**: Pre-registered tests, p < 2.9×10⁻⁷ threshold, independent datasets
- **Output**: CONFIRMED or NULL verdicts

### Phase 3: Replication Campaign
- **Goal**: Validate confirmed signals across multiple instruments/experiments
- **Method**: Independent teams, different analysis pipelines
- **Output**: Robust, publication-ready results

### Phase 4: Interpretation
- **Goal**: Connect confirmed signals to theoretical framework
- **Method**: Separate document (INTERPRETATION_NOTES.md) with explicit assumptions
- **Output**: Physical model relating discrete architecture to observed fingerprints

---

## Search Space Evolution

This document will be updated as channels are tested:

- **CLOSED channels**: Append to table with NULL verdict and reference to benchmark report
- **CANDIDATE channels**: Update status when exploratory signal detected
- **CONFIRMED channels**: Update status when replication successful
- **New channels**: Add to table as theoretical understanding evolves

**Version history**:
- v1.0 (2026-01-12): Initial classification with CMB TT closed

---

## Data Availability Assessment

### Publicly Available Data (Ready for Analysis)

#### Cosmology
- ✅ **Planck PR3 CMB maps** (temperature + polarization): Full-sky a_ℓm available
- ✅ **WMAP 9yr maps**: Temperature + polarization
- ✅ **SPT, ACT maps**: High-resolution ground-based CMB
- ✅ **BOSS/eBOSS galaxy catalogs**: Large-scale structure
- ✅ **DES weak lensing maps**: Shear catalogs

#### Astrophysics
- ✅ **IPTA pulsar timing data**: International Pulsar Timing Array (public releases)
- ✅ **CHIME/FRB catalog**: Fast Radio Burst arrival times and DMs
- ⚠️ **LIGO/Virgo waveforms**: Event catalogs public, raw strain data requires LIGO.ORG account

#### Laboratory (Limited Public Access)
- ⚠️ **Atomic clock logs**: Typically proprietary to national labs (NIST, PTB, etc.)
- ⚠️ **Interferometer noise logs**: LIGO public noise curves available, but detailed phase data limited
- ❌ **Quantum device logs**: Generally proprietary

### Data Access Strategy

1. **Start with publicly available data**: CMB maps, pulsar timing, FRBs
2. **Request access to proprietary data**: Contact labs for collaboration
3. **Consider new measurements**: Design bespoke experiments for high-priority channels

---

## Success Metrics

By maintaining this search space document, we ensure:

1. **No data dredging**: All channels cataloged upfront
2. **Closed channels stay closed**: NULL results are permanent (barring new data)
3. **Progressive narrowing**: Search space shrinks as channels are tested
4. **Reproducibility**: Future researchers know exactly which channels were tested and which remain open

**Goal**: In 6 months, 1 year, or 5 years, we can say:
> "We do not know where the fingerprint is, but we know which channels we tested, how we tested them, and which ones are closed."

---

**Last Updated**: 2026-01-12  
**Next Review**: After each channel test completion
