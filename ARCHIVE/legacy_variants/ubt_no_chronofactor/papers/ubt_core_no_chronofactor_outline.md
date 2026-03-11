# UBT Core: A Chronofactor-Free Formulation

**Outline for Main Research Paper**

---

## Abstract

We present a reformulation of Unified Biquaternion Theory (UBT) in which all physical phenomena emerge from a single 8-dimensional phase-capable field Θ(q) defined at each spacetime point. Unlike the legacy formulation, this approach does **not** invoke an external chronofactor parameter τ = t + iψ. Instead, phase information is intrinsic to the biquaternionic field structure itself. We demonstrate that:

1. **General Relativity** emerges from the entropy channel S_Θ = 2k_B ln|det Θ|
2. **Quantum mechanics** emerges from the phase channel Σ_Θ = k_B arg det Θ  
3. **Nonlocal correlations** arise from topological holonomy of Σ_Θ, without extra dimensions

This chronofactor-free formulation provides a cleaner conceptual foundation while preserving all physical predictions of the legacy theory.

---

## 1. Introduction

### 1.1 Motivation

The legacy UBT formulation uses complex time τ = t + iψ as a fundamental parameter. While this approach yields correct predictions, it introduces conceptual complications:

- What is the physical interpretation of imaginary time ψ?
- How does ψ evolve dynamically?
- Is τ observer-dependent or universal?

**UBT Core** eliminates these questions by removing the external chronofactor entirely.

### 1.2 Core Principles

All physics emerges from:
- **Single field**: Θ(q) ∈ ℍ⊗ℂ (8 real DOF per point)
- **Two channels**: Entropy S_Θ (amplitude) and phase Σ_Θ
- **No chronofactor**: τ is not a parameter

### 1.3 Relation to Standard Model + GR

| Framework | Primitives | Status |
|-----------|------------|--------|
| SM + GR | g_μν, ψ, A_μ, ... (many) | Standard |
| Legacy UBT | Θ(q, τ) + chronofactor | Legacy |
| **UBT Core** | **Θ(q) only** | **This work** |

---

## 2. The Fundamental Field

### 2.1 Biquaternion Definition

```
Θ(q) = Θ₀ + iΘ₁ + jΘ₂ + kΘ₃
```

where Θᵢ ∈ ℂ, giving **8 real degrees of freedom**.

**Representation**:
```
Θᵢ = Aᵢ + i·φᵢ    (Aᵢ, φᵢ ∈ ℝ)
```

- **Amplitude**: Aᵢ (4 real amplitudes)
- **Phase**: φᵢ (4 real phases)

### 2.2 Field Operations

- Conjugate: Θ† = Θ₀* - iΘ₁* - jΘ₂* - kΘ₃*
- Norm: ||Θ||² = Θ†Θ
- Determinant: det Θ (quaternionic determinant)

### 2.3 No Chronofactor Axiom

**Axiom**: Θ depends only on spacetime coordinates q = (t,x,y,z).

There is **no** dependence on an external parameter τ = t + iψ.

---

## 3. Observable Channels

### 3.1 Entropy Channel

**Definition**:
```
S_Θ(x) = 2 k_B ln |det Θ(x)|
```

**Physical interpretation**: Configurational entropy, volume in field space.

### 3.2 Phase Channel

**Definition**:
```
Σ_Θ(x) = k_B arg det Θ(x)
```

**Physical interpretation**: Topological charge, holonomy carrier.

### 3.3 Complementarity

S_Θ and Σ_Θ are orthogonal observables extracting amplitude and phase from det Θ = |det Θ| exp(i arg det Θ).

---

## 4. Emergent General Relativity

### 4.1 Metric from Entropy

**Mechanism**:
```
g_μν(q) = f(S_Θ, ∂_μ S_Θ, ∂_μ∂_ν S_Θ)
```

where f is a functional to be determined from field dynamics.

### 4.2 Einstein Equations

In the classical limit:
```
R_μν - (1/2) g_μν R = (8πG/c⁴) T_μν
```

where T_μν is derived from Θ dynamics.

### 4.3 Solutions

- **Schwarzschild**: Spherically symmetric static Θ
- **FLRW**: Homogeneous isotropic Θ
- **Gravitational waves**: Θ perturbations

---

## 5. Emergent Quantum Mechanics

### 5.1 Spinor Coupling

**Mapping**:
```
ψ_i ∝ sqrt(A_i) exp(iφ_i)
```

from Θ components to Dirac spinor.

### 5.2 Gauge Field from Phase

**Minimal coupling**:
```
A_μ = (1/k_B) ∂_μ Σ_Θ
```

gives U(1) gauge field.

### 5.3 Dirac Equation

```
(iγ^μ D_μ - m)ψ = 0
```

with D_μ = ∂_μ + i(e/k_B) ∂_μ Σ_Θ.

---

## 6. Nonlocality and Topology

### 6.1 Phase Holonomy

For closed path γ:
```
H[γ] = ∮_γ dΣ_Θ = 2πn k_B    (n ∈ ℤ)
```

### 6.2 EPR Correlations

Entangled Θ configurations satisfy:
```
Σ_Θ(A) + Σ_Θ(B) = const (mod 2π k_B)
```

giving nonlocal correlations.

### 6.3 No Extra Dimensions

Nonlocality arises from **global phase constraints**, not hidden dimensions.

---

## 7. Comparison to Legacy Formulation

### 7.1 Conceptual Mapping

| Legacy (Chronofactor) | Core (No Chronofactor) |
|-----------------------|------------------------|
| Θ(q, τ) | Θ(q) |
| External τ = t + iψ | No external parameter |
| Phase from ψ | Phase intrinsic to Θ |

### 7.2 Physical Equivalence

In observable sector:
- Same predictions for g_μν, ψ, etc.
- Same numerical results

### 7.3 Conceptual Advantages

- **Simpler ontology**: One field, not field + chronofactor
- **Clearer causality**: No ambiguity about ψ evolution
- **Gauge-invariant**: No gauge choice for τ

---

## 8. Open Questions

1. **Field dynamics**: What Lagrangian governs Θ evolution?
2. **Quantization**: How to quantize Θ field?
3. **Cosmology**: Initial conditions for Θ in early universe?
4. **Standard Model**: Full SM gauge group from Θ structure?
5. **Experimental tests**: Observational signatures unique to UBT Core?

---

## 9. Conclusions

We have presented UBT Core, a chronofactor-free formulation where:
- All physics emerges from 8D field Θ(q)
- GR from entropy channel S_Θ
- QM from phase channel Σ_Θ
- Nonlocality from holonomy

This provides a cleaner, more parsimonious foundation than the legacy chronofactor approach.

---

## Appendices

### A. Biquaternion Algebra
### B. Derivation Details
### C. Numerical Examples
### D. Comparison to String Theory

---

**Status**: Outline complete, full paper in development  
**Dependencies**: Derivations D01-D06  
**Next Steps**: Complete individual sections with detailed proofs
