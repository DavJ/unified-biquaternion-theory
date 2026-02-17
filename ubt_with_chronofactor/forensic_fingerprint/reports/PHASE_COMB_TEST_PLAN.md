# CMB Phase-Comb Test Plan: Why TT Spectrum Was Insensitive

**Date**: 2026-01-12  
**Author**: UBT Research Team  
**Status**: Technical Rationale Document

---

## Executive Summary

The **TT power spectrum comb test** (examining C_ℓ oscillations) returned null results on Planck and WMAP data. This document explains:

1. **Why the TT test was insensitive** to certain types of periodic structure
2. **What information was discarded** in the TT analysis
3. **Why a phase-based test is the next logical step**

**Key Finding**: The TT spectrum test averages |a_ℓm|² over m, **discarding phase information**. A periodic structure could exist in the **phases** φ_ℓm = arg(a_ℓm) while leaving C_ℓ unchanged.

---

## Background: What the TT Test Measured

### Definition of TT Power Spectrum

The CMB temperature field T(θ,φ) on the sphere is expanded in spherical harmonics:

```
T(θ,φ) = Σ_ℓm a_ℓm Y_ℓm(θ,φ)
```

where:
- a_ℓm are complex coefficients
- Y_ℓm are spherical harmonic basis functions

The **TT power spectrum** is:

```
C_ℓ = (1/(2ℓ+1)) Σ_m |a_ℓm|²
```

Key points:
- **Averages** |a_ℓm|² over all m ∈ [-ℓ, +ℓ]
- **Discards** phase information: φ_ℓm = arg(a_ℓm)
- **Isotropic assumption**: C_ℓ independent of m

### What the TT Comb Test Looked For

The TT comb test searched for sinusoidal oscillations:

```
C_ℓ ≈ C_ℓ^ΛCDM + A sin(2π ℓ/P + φ)
```

Testing periods: P ∈ {8, 16, 32, 64, 128, 255}

**Result**: Null. No significant periodic modulation in C_ℓ.

---

## Why TT Was Insensitive: Information Loss

### Phase Information is Orthogonal to Power

Consider two different CMB realizations with **same power spectrum** but different phases:

**Realization 1** (random phases):
```
a_ℓm = r_ℓm exp(i θ_ℓm^(1))
where θ_ℓm^(1) ~ Uniform(0, 2π)
```

**Realization 2** (phase-locked):
```
a_ℓm = r_ℓm exp(i θ_ℓm^(2))
where θ_ℓm^(2) = f(ℓ, m, P) for some periodic function f
```

**Both have identical C_ℓ**:
```
C_ℓ^(1) = (1/(2ℓ+1)) Σ_m |a_ℓm|² = (1/(2ℓ+1)) Σ_m r_ℓm² = C_ℓ^(2)
```

But they have **different phase coherence**:
- Realization 1: R(P) → 0 (random phases)
- Realization 2: R(P) > 0 (phase-locking)

### Analogy: Synchronized Clocks

**Power spectrum** = Number of clocks, average energy
**Phase coherence** = Are the clocks synchronized?

Two ensembles of clocks can have:
- **Same power**: 100 clocks, average energy E
- **Different phase structure**:
  - Ensemble A: Random hand positions → R = 0
  - Ensemble B: All hands aligned → R = 1

The TT spectrum only measures the total energy, not the synchronization.

---

## The Phase-Comb Test: Filling the Gap

### Definition

For each period P, compute:

```
R(P) = |mean over (ℓ,m) of exp(i Δφ_ℓm(P))|
```

where:
```
Δφ_ℓm(P) = arg(a_{ℓ+P,m}) - arg(a_{ℓ,m})
```

### Why This Works

1. **Uses discarded information**: Phases φ_ℓm
2. **Tests relational structure**: Δφ between modes
3. **Preserves isotropy**: Averages over m (like C_ℓ)
4. **Independent test**: Orthogonal to TT comb

---

## Conclusion

The TT power spectrum comb test was **correct but incomplete**:
- ✓ Tested amplitude structure in C_ℓ
- ✗ Did not test phase structure in arg(a_ℓm)

The phase-comb test fills this gap by:
- Using previously discarded information (phases)
- Testing orthogonal hypothesis (relational structure)
- Providing independent evidence for/against periodic models

**Both tests together** provide comprehensive coverage of periodic structure hypotheses in CMB.

---

**End of Document**
