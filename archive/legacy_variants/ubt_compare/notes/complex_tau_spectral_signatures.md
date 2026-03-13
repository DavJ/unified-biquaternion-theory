# Complex τ Spectral Signatures: Measurable Checklist

**Author**: UBT Team  
**Date**: February 2026  
**Purpose**: Practical checklist for identifying complex chronofactor signatures in spectral data  
**License**: © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0

---

## Overview

This document provides a practical checklist for detecting complex chronofactor (τ = t + iψ) signatures in observational data. It connects the formal derivations in `DERIVATION_P2_complex_chronofactor_spectrum.md` to measurable quantities.

---

## Primary Observables

### 1. Entropy Channel: S_Θ(t)

**Definition**: S_Θ(t) = k_B log det(Θ†Θ)

**How to Measure**:
- Compute eigenvalues λ_i(t) of observable matrix O(t) = Θ†Θ
- S_Θ(t) = k_B Σ_i log λ_i(t)

**What to Look For**:
- [ ] **Linear growth/decay**: ∂_t S_Θ = constant (consistent with linear flow)
- [ ] **Non-monotonic evolution**: S_Θ increases then decreases (possible transient growth)
- [ ] **Sudden jumps**: Discontinuities in ∂_t S_Θ (phase transitions or singularities)
- [ ] **Correlation with external parameters**: S_Θ varies with ψ if complex τ is active

### 2. Phase Channel: Σ_Θ(t)

**Definition**: Σ_Θ(t) = k_B arg det Θ(t) = k_B Im[log det Θ(t)]

**How to Measure**:
- Compute det Θ(t) in complex representation
- Extract argument: Σ_Θ(t) = k_B arctan(Im[det Θ] / Re[det Θ])
- Alternative: Σ_Θ(t) = k_B Σ_i arg(eigenvalue_i) for complex eigenvalues

**What to Look For**:
- [ ] **Monotonic winding**: Σ_Θ increases/decreases linearly (constant phase precession)
- [ ] **Oscillatory behavior**: Σ_Θ(t) = Σ_0 + A sin(ωt + φ) (complex eigenvalue pair)
- [ ] **Phase jumps**: Discontinuities at det Θ = 0 (branch cuts in complex plane)
- [ ] **Coupling to entropy**: Correlation between Σ_Θ oscillations and S_Θ features

### 3. Observable Matrix Eigenvalues: λ_i(t)

**Definition**: Eigenvalues of O(t) = Θ†Θ

**How to Measure**:
- Diagonalize O(t) at each time step
- Track individual eigenvalues λ_i(t) over time

**What to Look For**:
- [ ] **Spectral broadening**: σ[{λ_i}] increases with time (modes spreading)
- [ ] **Spectral narrowing**: σ[{λ_i}] decreases with time (modes converging)
- [ ] **Mode crossing**: λ_i(t) and λ_j(t) intersect (degeneracy)
- [ ] **Exponential growth/decay**: log λ_i(t) ∝ t (eigenmode dominance)
- [ ] **Oscillatory modulation**: λ_i(t) = λ̄_i + δλ_i sin(ωt) (complex-τ signature)

---

## Discriminator Tests

### Discriminator D1: Phase-Entropy Coupling Coefficient

**Formula**: C_ΣS(t) = (∂_t Σ_Θ) / (∂_t S_Θ)

**Measurement Protocol**:
1. Compute time derivatives numerically:
   - ∂_t S_Θ ≈ [S_Θ(t+Δt) - S_Θ(t)] / Δt
   - ∂_t Σ_Θ ≈ [Σ_Θ(t+Δt) - Σ_Θ(t)] / Δt
2. Compute ratio C_ΣS(t) at each time step
3. Plot C_ΣS(t) vs. t

**Expected Signatures**:
- [ ] **Real τ**: C_ΣS = constant (horizontal line)
- [ ] **Complex τ (fixed ψ)**: C_ΣS = constant but ≠ expected value from pure real evolution
- [ ] **Complex τ (varying ψ)**: C_ΣS(t) varies in time (smoking gun!)

**Interpretation**:
- Constant C_ΣS → Simple linear flow with fixed G
- Time-varying C_ΣS → Either ψ(t) varies or G = G(t, ψ)
- C_ΣS → ∞ → Entropy channel stationary (∂_t S_Θ ≈ 0), phase dominates
- C_ΣS → 0 → Phase channel stationary (∂_t Σ_Θ ≈ 0), entropy dominates

### Discriminator D2: Spectral Variance Conservation Test

**Formula**: Var_O(t) = Tr(O²) / (Tr O)² - 1/n

**Measurement Protocol**:
1. Compute O(t) = Θ†Θ at each time step
2. Compute Tr(O) = Σ_i λ_i and Tr(O²) = Σ_i λ_i²
3. Var_O(t) = [Σ_i λ_i²] / [Σ_i λ_i]² - 1/n
4. Plot Var_O(t) vs. t

**Expected Signatures**:
- [ ] **Anti-Hermitian G, real τ**: Var_O(t) = constant (conserved spectrum)
- [ ] **Hermitian G**: Var_O(t) drifts monotonically (spectral evolution)
- [ ] **Complex τ with non-zero Herm(G)**: Var_O(t) drifts
- [ ] **Non-normal G**: Var_O(t) exhibits transient spike (temporary broadening)

**Interpretation**:
- d(Var_O)/dt = 0 → Unitary evolution (anti-Hermitian generator)
- d(Var_O)/dt > 0 → Spectral broadening (modes spreading)
- d(Var_O)/dt < 0 → Spectral narrowing (modes converging)
- Transient spike → Non-normal G (pseudospectrum effects)

### Discriminator D3: Mode Pairing and Cross-Correlation

**Measurement Protocol**:
1. Compute FFT of Σ_Θ(t) to extract dominant frequencies
2. Compute FFT of S_Θ(t) to check for oscillatory components
3. Compute cross-correlation: R_ΣS(τ) = ⟨Σ_Θ(t) S_Θ(t+τ)⟩_t
4. Look for peaks in FFT[S_Θ] at frequencies found in FFT[Σ_Θ]

**Expected Signatures**:
- [ ] **Real τ**: FFT[S_Θ] shows only DC component (no oscillations)
- [ ] **Complex τ**: FFT[Σ_Θ] shows peaks at ω_k (oscillatory phase)
- [ ] **Cross-channel leakage**: FFT[S_Θ] shows small peaks at same ω_k
- [ ] **Phase shift**: R_ΣS(τ) peaks at τ ≠ 0 (delayed correlation)

**Specific Tests**:
- [ ] Extract peak frequency ω_obs from FFT[Σ_Θ(t)]
- [ ] Check FFT[S_Θ(t)] for feature at ω_obs (should be absent for real τ)
- [ ] Compute |FFT[S_Θ](ω_obs)| / |FFT[S_Θ](0)| (cross-leakage ratio)
- [ ] If ratio > 0.01 (1%), suspect complex-τ coupling

---

## Secondary Observables

### 4. Condition Number: κ(O)

**Definition**: κ(O) = λ_max / λ_min (ratio of largest to smallest eigenvalue)

**What to Look For**:
- [ ] **Ill-conditioning**: κ(O) → ∞ (matrix near-singular, det → 0)
- [ ] **Well-conditioned**: κ(O) ≈ O(1) (balanced spectrum)
- [ ] **Time evolution**: κ(O(t)) increases → spectral stretching

**Connection to Complex τ**:
- Large κ signals potential logarithmic divergence in S_Θ
- Rapid changes in κ suggest non-unitary evolution

### 5. Trace of Generator: Tr G

**Extraction Method**:
- If linear flow is established: Tr G = (d/dt) log det Θ(t)
- Numerically: Tr G ≈ [log det Θ(t+Δt) - log det Θ(t)] / Δt

**Decomposition**:
- Tr A = Re(Tr G) → controls entropy growth rate
- Tr B = Im(Tr G) → controls phase precession rate

**What to Look For**:
- [ ] **Constant Tr A, Tr B**: Confirms time-independent generator G
- [ ] **Time-varying Tr G**: G = G(t) or non-linear effects
- [ ] **Relationship to data**: ∂_t S_Θ = 2k_B Tr A, ∂_t Σ_Θ = k_B Tr B

### 6. Non-Normality Measure: ||[G, G†]||

**Definition**: Deviation from normality

**Practical Estimate**:
- If G is not directly known, estimate from eigenvector orthogonality
- For eigenvectors v_i of O(t): check ⟨v_i|v_j⟩ ≈ δ_ij
- Non-orthogonal eigenvectors → non-normal G

**What to Look For**:
- [ ] **Orthogonal eigenvectors**: Normal generator (commuting real/imaginary parts)
- [ ] **Non-orthogonal eigenvectors**: Non-normal G (potential transient growth)
- [ ] **Sudden loss of orthogonality**: Phase transition or instability

---

## Data Analysis Pipeline

### Step 1: Extract Time Series

From observational data, extract:
- [ ] O(t) = Θ†Θ (observable matrix) at discrete time steps t_i
- [ ] det Θ(t) (complex determinant) if available
- [ ] Eigenvalues λ_i(t) of O(t)

### Step 2: Compute Primary Channels

- [ ] S_Θ(t) = k_B Σ_i log λ_i(t)
- [ ] Σ_Θ(t) = k_B arg det Θ(t) OR k_B Σ_i arg(μ_i(t)) for complex eigenvalues μ_i

### Step 3: Apply Discriminator Tests

- [ ] D1: Compute C_ΣS(t) = (∂_t Σ_Θ) / (∂_t S_Θ), check for constancy
- [ ] D2: Compute Var_O(t), check for conservation or drift
- [ ] D3: FFT both channels, check for cross-correlation

### Step 4: Characterize Spectral Properties

- [ ] Condition number κ(O(t))
- [ ] Spectral variance σ[{λ_i}]
- [ ] Eigenvalue growth rates: α_i = (d/dt) log λ_i(t)

### Step 5: Interpret Results

Create decision tree:

```
Is C_ΣS(t) constant?
├─ YES: Check D2 (variance conservation)
│   ├─ Conserved → Real τ, anti-Hermitian G
│   └─ Drifts → Real τ, non-anti-Hermitian G OR complex τ with fixed ψ
└─ NO: Complex τ with varying ψ(t) OR time-dependent G(t)
    └─ Check D3 (cross-correlation)
        ├─ Present → Complex τ confirmed
        └─ Absent → Time-dependent generator G(t)
```

---

## Connection to Existing Repository Observables

### Mapping to UBT Repository Files

| Spectral Observable | Likely Location in Repo | Notes |
|---------------------|-------------------------|-------|
| S_Θ(t) | Entropy channel outputs from CMB analysis | Check `cmb_comb.py` outputs |
| Σ_Θ(t) | Phase channel, grid 255 quantization | See `grid_255.py`, forensic fingerprint |
| Eigenvalues λ_i(t) | Spectral scans | Check `scans/` directory |
| FFT[Σ_Θ] | Phase comb signature | See CMB power spectrum analysis |
| Condition number | May need to be computed | Not directly in current outputs |

### Scripts to Enhance

Consider adding diagnostic outputs to:
- [ ] `cmb_comb.py`: Add discriminator D1, D2, D3 calculations
- [ ] `grid_255.py`: Output time series of S_Θ and Σ_Θ
- [ ] New script: `spectral_discriminators.py` to compute D1-D3 from existing data

---

## Practical Considerations

### Numerical Stability

- [ ] **Regularization**: When computing log det Θ, add small ε if det → 0
- [ ] **Derivative estimation**: Use centered differences when possible
- [ ] **FFT resolution**: Ensure sufficient time samples (N > 2·ω_max/Δω)

### Statistical Significance

- [ ] **Bootstrap**: Resample data to estimate error bars on C_ΣS
- [ ] **Hypothesis testing**: Null hypothesis H0: C_ΣS = constant
- [ ] **Threshold**: Define α-level for rejecting H0 (e.g., 5% significance)

### False Positives

Beware of:
- [ ] Numerical artifacts in derivatives (use smoothing)
- [ ] Aliasing in FFT (ensure Nyquist criterion)
- [ ] Noise amplification in ratios (check denominators ≠ 0)

---

## Summary: Quick Diagnostic Checklist

For rapid assessment of whether complex τ is active in a dataset:

1. [ ] Plot S_Θ(t) and Σ_Θ(t) side by side
2. [ ] Compute C_ΣS(t) = (∂_t Σ_Θ) / (∂_t S_Θ)
3. [ ] Check if C_ΣS is constant (within error bars)
4. [ ] If not constant → likely complex τ or time-dependent G
5. [ ] Compute FFT[Σ_Θ] and FFT[S_Θ]
6. [ ] Check for cross-peaks at same frequencies
7. [ ] If cross-peaks present → strong evidence for complex τ

**Decision Rule**:
- All discriminators negative → Real τ evolution
- Any discriminator positive → Complex τ candidate
- Multiple discriminators positive → Complex τ highly likely

---

**Next Steps**:
- Implement discriminator calculations in analysis pipeline
- Apply to existing CMB fingerprint data
- Document results in comparison report

---

© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0
