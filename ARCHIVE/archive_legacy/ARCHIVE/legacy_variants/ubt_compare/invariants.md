# Shared Invariants for UBT Formulation Comparison

## Purpose

This document lists the **physical invariants** that both UBT formulations must predict consistently. These serve as validation criteria for the A/B comparison.

## Geometric Invariants

### Determinant of Θ Field

**Definition**: `det(Θ)`

**Physical Meaning**: 
- Volume element in biquaternionic space
- Related to probability density in quantum interpretations
- Must remain positive for physical configurations

**Requirements**:
- Both formulations must predict the same `det(Θ)` for equivalent physical states
- Real part must be positive for physical solutions

**Status**: 🟡 Validation pending

---

### Trace of log(Θ)

**Definition**: `Tr(log Θ)`

**Physical Meaning**:
- Entropy-like quantity encoding information content
- Related to action in field theory
- Connection to S_Θ entropy channel (no-chronofactor formulation)

**Requirements**:
- Must match between formulations for equivalent states
- Should reduce to classical entropy in appropriate limits

**Status**: 🟡 Validation pending

---

### Real/Imaginary parts of log(det Θ)

**Definition**: `Re(log det Θ)` and `Im(log det Θ)`

**Physical Meaning**:
- `Re(log det Θ)`: Related to energy/mass density
- `Im(log det Θ)`: Related to phase/quantum information
- Decomposes biquaternionic structure into GR and QM channels

**Requirements**:
- Real part → gravitational sector (must match GR predictions)
- Imaginary part → quantum sector (must match QM predictions)

**Status**: 🟡 Validation pending

---

### Hermitian Product Θ†Θ

**Definition**: `Θ†Θ` where `†` is biquaternionic conjugation

**Physical Meaning**:
- Positive-definite norm on biquaternionic field
- Related to energy density
- Invariant under gauge transformations

**Requirements**:
- Must be positive definite for physical states
- Should reduce to energy density in appropriate limits

**Status**: 🟡 Validation pending

---

## Decomposition Invariants

### Unitary Decomposition

**With Chronofactor**: `Θ = U(τ) · H(q)` where U is unitary, H is Hermitian

**Without Chronofactor**: `Θ = exp(iΣ_Θ) · exp(S_Θ)` where Σ_Θ is phase, S_Θ is entropy

**Requirement**:
- The extracted phase structure Σ_Θ should relate consistently to U(τ)
- The entropy structure S_Θ should relate consistently to H(q)

**Mapping**:
```
With chronofactor:     Without chronofactor:
U(τ) · H(q)      ↔     exp(iΣ_Θ) · exp(S_Θ)

Correspondence:
Im(log U(τ))     ↔     Σ_Θ(q)
log H(q)         ↔     S_Θ(q)
```

**Status**: 🟡 Mapping established, validation pending

---

## Physical Observables

### Fine Structure Constant

**Definition**: `α ≈ 1/137.036`

**Prediction Source**:
- **With chronofactor**: Derived from chronofactor phase winding combined with field geometry
- **Without chronofactor**: Derived from intrinsic phase structure Σ_Θ

**Requirement**: Both must predict α within experimental uncertainty

**Status**: 
- With chronofactor: ✅ α ≈ 137.036 derived
- Without chronofactor: 🚧 Derivation in progress

---

### Electron Mass

**Definition**: `m_e ≈ 0.511 MeV/c²`

**Prediction Source**:
- **With chronofactor**: From mass generation mechanism in τ-dependent field
- **Without chronofactor**: From phase-entropy coupling in Θ field

**Requirement**: Both must predict m_e within experimental uncertainty

**Status**:
- With chronofactor: ✅ m_e ≈ 0.511 MeV derived
- Without chronofactor: 🚧 Derivation in progress

---

### GR Metric Recovery

**Definition**: Recover Einstein field equations in classical limit

**Requirement**:
- Both formulations must reduce to `R_μν - ½g_μν R = 8πG T_μν` in real-valued limit
- Schwarzschild solution must emerge for spherical symmetry
- Cosmological solutions must match ΛCDM in appropriate regime

**Status**:
- With chronofactor: ✅ GR recovery proven
- Without chronofactor: 🟡 Formal proof needed

---

### Standard Model Gauge Structure

**Definition**: Recover SU(3) × SU(2) × U(1) gauge symmetry

**Requirement**:
- Both must derive the Standard Model gauge group from biquaternionic geometry
- Coupling constants must be predicted or constrained

**Status**:
- With chronofactor: ✅ SM emergence derived
- Without chronofactor: 🚧 Derivation in progress

---

## CMB Fingerprint Invariants

### Grid 255 Quantization

**Definition**: Phase structure quantized on grid with N=255 levels

**Requirement**: 
- If this is a physical prediction (not just computational artifact), both formulations must predict it
- If formulation-dependent, document the difference

**Status**: 🟡 Clarification needed (is this physical or computational?)

---

### Phase Comb Signature

**Definition**: Periodic phase structure in CMB power spectrum

**Requirement**:
- If physical, both formulations must predict the same signature
- Frequency and amplitude must match

**Status**: 
- With chronofactor: ✅ Signature detected in forensic fingerprint analysis
- Without chronofactor: ❌ Not yet implemented

---

## What is Allowed to Differ

The following **may differ** between formulations without invalidating either:

1. **Mathematical complexity** - One formulation may be more elegant
2. **Conceptual interpretation** - Physical meaning of τ vs intrinsic phase
3. **Computational efficiency** - Algorithms may differ
4. **Intermediate steps** - Derivation paths can diverge as long as final predictions match
5. **Additional predictions** - One formulation may make novel predictions the other doesn't

## Validation Protocol

To validate consistency:

1. **Compute invariant in formulation 1**
2. **Compute same invariant in formulation 2**
3. **Compare results** within numerical precision
4. **Document any discrepancies**

If discrepancies exist:
- Check for mathematical errors
- Verify equivalent physical assumptions
- Identify which formulation is more accurate

## Status Legend

- ✅ **Complete** - Invariant validated in both formulations
- 🟡 **Pending** - Computed in one formulation, awaiting other
- 🚧 **In Progress** - Derivation underway
- ❌ **Not Implemented** - Not yet addressed

---

© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0
