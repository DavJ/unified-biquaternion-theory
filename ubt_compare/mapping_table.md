# Object Mapping Between UBT Formulations

## Purpose

This document establishes the **correspondence between mathematical objects** in the two UBT formulations, enabling systematic comparison.

---

## Fundamental Field Structure

| **With Chronofactor** | **Without Chronofactor** | **Correspondence** |
|----------------------|-------------------------|-------------------|
| `Θ(q, τ)` | `Θ(q)` | Biquaternionic field |
| `τ = t + iψ` | — | Complex time (external parameter) |
| — | `Σ_Θ(q)` | Intrinsic phase channel (8D) |
| — | `S_Θ(q)` | Intrinsic entropy channel (8D) |

**Key Difference**: 
- **With chronofactor**: Time has imaginary component ψ as external parameter
- **Without chronofactor**: All phase information encoded in field structure Θ(q)

**Mapping Hypothesis**:
```
τ-dependence in Θ(q,τ)  ↔  Intrinsic phase Σ_Θ(q)
```

The imaginary time evolution `∂/∂(iψ)` in the chronofactor formulation may correspond to spatial gradient `∇Σ_Θ` in the chronofactor-free formulation.

---

## Polar Decomposition

| **With Chronofactor** | **Without Chronofactor** | **Mapping** |
|----------------------|-------------------------|------------|
| `Θ(q,τ) = U(τ) · H(q)` | `Θ(q) = exp(iΣ_Θ) · exp(S_Θ)` | Unitary × Hermitian |
| `U(τ)` unitary | `exp(iΣ_Θ)` unitary | Phase factor |
| `H(q)` Hermitian | `exp(S_Θ)` positive definite | Entropy/energy factor |

**Correspondence**:
- Phase structure: `Im(log U(τ))` ↔ `Σ_Θ(q)`
- Entropy structure: `log H(q)` ↔ `S_Θ(q)`

**Physical Interpretation**:
- **With chronofactor**: Phase evolves with imaginary time ψ
- **Without chronofactor**: Phase is intrinsic field property varying in space

---

## Emergence of GR

| **With Chronofactor** | **Without Chronofactor** | **Observable** |
|----------------------|-------------------------|---------------|
| `g_μν(q,τ)` from `Re(Θ)` | `g_μν(q)` from `S_Θ` entropy | Metric tensor |
| `R_μν[g]` | `R_μν[g]` | Ricci curvature |
| Einstein eqs from τ-action | Einstein eqs from S_Θ channel | GR field equations |

**Requirement**: Both must reduce to identical Einstein field equations in classical limit.

**Mapping**:
```
Re(Θ(q,τ)) channel  →  g_μν(q,τ)
S_Θ(q) entropy      →  g_μν(q)
```

**Status**: 
- With chronofactor: ✅ GR recovery proven
- Without chronofactor: 🟡 Derivation documented in `D04_emergent_metric_Re_channel.md`

---

## Emergence of QM

| **With Chronofactor** | **Without Chronofactor** | **Observable** |
|----------------------|-------------------------|---------------|
| `Im(Θ)` phase | `Σ_Θ` phase channel | Quantum phase |
| Wavefunction from τ | Wavefunction from Σ_Θ | ψ(q) quantum state |
| Dirac equation from τ-dynamics | Dirac equation from phase coupling | Fermion dynamics |

**Correspondence**:
```
Im(log Θ(q,τ))  ↔  Σ_Θ(q)
```

**Physical Meaning**:
- **With chronofactor**: Quantum behavior emerges from imaginary time evolution
- **Without chronofactor**: Quantum behavior emerges from intrinsic phase gradients

**Status**:
- With chronofactor: ✅ QM emergence established
- Without chronofactor: 🟡 Documented in `D05_dirac_coupling_phase_channel.md`

---

## Fine Structure Constant

| **With Chronofactor** | **Without Chronofactor** | **Prediction** |
|----------------------|-------------------------|---------------|
| α from τ-winding | α from Σ_Θ topology | α ≈ 1/137.036 |
| Phase wraps in τ-plane | Phase wraps in Σ_Θ manifold | Topological quantization |
| Computation: τ-dependent loop | Computation: Σ_Θ holonomy | Gauge coupling |

**Hypothesis**: Same topological structure, different parametrization.

**Expected Correspondence**:
```
∮ dτ/τ around branch cut  ↔  ∮ Σ_Θ around phase singularity
```

**Status**:
- With chronofactor: ✅ α ≈ 137.036 computed
- Without chronofactor: 🚧 Computation in progress

---

## Fermion Masses

| **With Chronofactor** | **Without Chronofactor** | **Prediction** |
|----------------------|-------------------------|---------------|
| m_e from τ-field coupling | m_e from S_Θ-Σ_Θ coupling | Electron mass |
| Mass generation via τ | Mass from entropy-phase interaction | Yukawa-like coupling |
| Generational structure from τ | Generational structure from Σ_Θ modes | Lepton/quark masses |

**Mapping Hypothesis**:
```
Yukawa coupling to τ  ↔  Yukawa coupling to Σ_Θ gradient
```

**Status**:
- With chronofactor: ✅ m_e, m_μ, m_τ computed
- Without chronofactor: 🚧 Mass mechanism being derived

---

## Dark Sector

| **With Chronofactor** | **Without Chronofactor** | **Prediction** |
|----------------------|-------------------------|---------------|
| Dark matter from τ-excitations | Dark matter from Σ_Θ solitons | Ω_DM ≈ 27% |
| Dark energy from τ-vacuum | Dark energy from S_Θ ground state | Ω_Λ ≈ 68% |

**Hypothesis**: Dark sector emerges from non-perturbative structures in either τ or Σ_Θ.

**Status**:
- With chronofactor: 🟡 Partial derivations exist
- Without chronofactor: ❌ Not yet addressed

---

## Observable Extraction Pipelines

### CMB Power Spectrum

| **With Chronofactor** | **Without Chronofactor** | **Pipeline** |
|----------------------|-------------------------|-------------|
| Input: Θ(q,τ) field | Input: Θ(q) field | Biquaternionic field |
| Extract: Im(Θ) phase map | Extract: Σ_Θ(q) phase map | Phase extraction |
| Fourier: ℱ[phase(τ)] | Fourier: ℱ[Σ_Θ(q)] | Spectral analysis |
| Output: C_ℓ power spectrum | Output: C_ℓ power spectrum | CMB observables |

**Requirement**: Both pipelines must predict the same C_ℓ for physical CMB data.

**Status**:
- With chronofactor: ✅ Pipeline implemented in `forensic_fingerprint/`
- Without chronofactor: ❌ Pipeline not yet implemented

---

### Forensic Fingerprint

| **With Chronofactor** | **Without Chronofactor** | **Test** |
|----------------------|-------------------------|---------|
| Grid 255 quantization test | Grid 255 quantization test | Phase discretization |
| CMB comb signature (τ-based) | CMB comb signature (Σ_Θ-based) | Periodic structure |
| Phase coherence (τ-plane) | Phase coherence (Σ_Θ manifold) | Long-range correlations |

**Hypothesis**: If Grid 255 is physical (not computational artifact), both formulations must predict it.

**Status**:
- With chronofactor: ✅ Full forensic suite in `ubt_with_chronofactor/forensic_fingerprint/`
- Without chronofactor: ❌ Forensic tools not yet developed

---

## Conceptual Differences

### What the Chronofactor Formulation Assumes

1. **External complex time**: τ = t + iψ exists as fundamental parameter
2. **Imaginary time evolution**: ψ evolves (mechanism TBD)
3. **Phase from τ**: Quantum phase originates from complex time structure

### What the Chronofactor-Free Formulation Assumes

1. **Standard real time**: Only real time t is fundamental
2. **Intrinsic phase field**: Σ_Θ(q) is an 8D field configuration
3. **Phase from geometry**: Quantum phase originates from biquaternionic field geometry

### Open Questions

1. **Are these equivalent?** Do they make identical predictions for all observables?
2. **Which is simpler?** Which requires fewer conceptual assumptions?
3. **Which is more testable?** Which makes more falsifiable predictions?
4. **Which is more general?** Which extends more naturally to quantum gravity?

---

## Validation Strategy

### Step 1: Establish Correspondence

For each object in formulation A, identify corresponding object in formulation B.

### Step 2: Compute Shared Invariants

Use `invariants.md` list to compute same physical observables in both formulations.

### Step 3: Compare Results

- **If results match**: Formulations are consistent (possibly equivalent)
- **If results differ**: 
  - Check for mathematical errors
  - Identify physical assumption causing difference
  - Determine which prediction is more accurate

### Step 4: Empirical Testing

Design experiments that can distinguish between formulations if predictions differ.

---

## Implementation Status

| **Component** | **With Chronofactor** | **Without Chronofactor** |
|--------------|-----------------------|-------------------------|
| Core field theory | ✅ Complete | 🟡 Scaffolding done |
| GR recovery | ✅ Proven | 🟡 Documented |
| QM recovery | ✅ Established | 🟡 Documented |
| α prediction | ✅ Computed | 🚧 In progress |
| Mass predictions | ✅ Computed | 🚧 In progress |
| CMB pipeline | ✅ Implemented | ❌ Not started |
| Forensic tests | ✅ Complete suite | ❌ Not started |

---

© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0
