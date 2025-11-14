# Canonical Definitions for Unified Biquaternion Theory

**Purpose**: This document establishes the single, authoritative version of all core UBT definitions to resolve conflicts and duplications across the theory.

**Status**: Phase 2 Implementation - Canonical Definitions

---

## 1. Biquaternion Time (Canonical)

### Canonical Definition
The fundamental time coordinate in UBT is **biquaternion time**:

```
T_B = t + i(ψ + v·σ) = t + iψ + jχ + kξ
```

where:
- `t` ∈ ℝ = real time coordinate (standard physical time)
- `ψ, χ, ξ` ∈ ℝ = imaginary time components
- `i, j, k` = quaternion units (i² = j² = k² = ijk = −1)
- `v = (χ, ξ, ψ)` = vector imaginary component
- `σ = (σ₁, σ₂, σ₃)` = Pauli matrices

### Hierarchical Structure

Biquaternion time has a hierarchical reduction:

```
T_B (full biquaternion time)
  ↓ [||v|| → 0, directional isotropy]
τ = t + iψ (complex time limit)
  ↓ [ψ → 0]
t (classical real time / GR)
```

### Complex Time as Limiting Case

**Complex time** τ = t + iψ is obtained when the vector imaginary components vanish or become isotropic:

**Projection criterion**:
- Complex time τ valid when: `||v||² << |ψ|²`
- Full biquaternion T_B required when: `||v||² ~ |ψ|²` or directional anisotropy

### Physical Interpretation

**Full biquaternion time** encodes:
- **Scalar imaginary part** (ψ): Isotropic phase, consciousness substrate, dark energy
- **Vector imaginary part** (v): Directional phases, spacetime torsion, spin-dependent effects, anisotropic dark matter

**Complex time limit** (simplified):
- Valid for weakly coupled systems, low-energy QED, isotropic cosmology
- Sufficient for most Standard Model calculations

### Resolution of Conflicts
The theory previously had 3 conflicting versions:
1. ❌ Drift-diffusion Fokker-Planck variant
2. ❌ Toroidal variant with θ-functions
3. ❌ Hermitized variant (Appendix F)

**Canonical Version**: **Biquaternion time T_B** is fundamental. Complex time τ = t + iψ is a valid approximation when directional components are negligible.

---

## 2. Theta Field Θ(q,T_B)

### Canonical Definition
The fundamental field is a **biquaternion**:

```
Θ(q, T_B) ∈ B = H ⊗ ℂ
Θ = Θ₀ + Θ₁i + Θ₂j + Θ₃k,    where Θₐ ∈ ℂ
```

where:
- `B` = biquaternion algebra = H ⊗ ℂ (quaternions tensored with complex numbers)
- `H` = quaternion algebra with units {1, i, j, k}
- `i, j, k` = quaternion units satisfying i² = j² = k² = ijk = −1
- `Θₐ` (a = 0,1,2,3) = complex-valued components

### Matrix Representation

For computational purposes, Θ can be represented as a matrix:

**Spinor representation**: Θ ↔ 4×4 complex matrix (16 complex DOF = 32 real DOF)
**Extended representation**: Θ ↔ 8×8 complex matrix (for full SM with 3 generations)

**Important**: Matrix forms are **representations only**, not the canonical definition. The canonical object is the biquaternion itself.

### Field Structure
- **Coordinates**: q ∈ B (biquaternion space, 4 base dimensions)
- **Time**: T_B = t + iψ + jχ + kξ (biquaternion time)
- **DOF**: 4 complex components = 8 real DOF (before gauge/symmetry constraints)

### Biquaternion Operations

**Conjugation**:
```
Θ† = Θ₀ - Θ₁i - Θ₂j - Θ₃k    (quaternion conjugate)
Θ̄ = Θ̄₀ + Θ̄₁i + Θ̄₂j + Θ̄₃k    (complex conjugate)
```

**Norm**:
```
|Θ|² = Θ†Θ = |Θ₀|² + |Θ₁|² + |Θ₂|² + |Θ₃|²
```

### Resolution of Conflicts
Previous conflicting versions:
1. ❌ 4×4 spinor matrix (older version) - matrix as primary object
2. ❌ 8×8 matrix structure (consolidation) - matrix as primary object
3. ❌ 4D biquaternion (old preprint) - lacked clear definition

**Canonical Version**: 
- **Θ is a biquaternion** Θ(q,T_B) ∈ B = H ⊗ ℂ
- **Matrix forms** are computational representations only
- Works with full biquaternion time T_B (can reduce to complex time τ when appropriate)

---

## 3. Metric Tensor g_μν

### Canonical Definition
```
g_μν(Θ) = Re[(∂_μΘ)(∂_νΘ†)]
```

where:
- `∂_μ` = biquaternionic partial derivative with respect to spacetime coordinate x^μ
- `Θ†` = biquaternion conjugate: Θ† = Θ₀ - Θ₁i - Θ₂j - Θ₃k (with complex conjugation)
- `Re` = real part of the biquaternion product
- Product is biquaternion multiplication

**Note on notation**: When using matrix representation, this becomes Re Tr(∂_μΘ ∂_νΘ†) where Tr is the matrix trace. But the canonical definition is in terms of biquaternion operations.

### Biquaternion Form
For Θ = Θ₀ + Θ₁i + Θ₂j + Θ₃k:
```
g_μν = Re[∂_μΘ₀ ∂_νΘ̄₀ + ∂_μΘ₁ ∂_νΘ̄₁ + ∂_μΘ₂ ∂_νΘ̄₂ + ∂_μΘ₃ ∂_νΘ̄₃]
```

### Properties
- **Signature**: (+,−,−,−) [mostly minus, timelike positive] - standard convention
- **Symmetric**: g_μν = g_νμ
- **Real-valued**: Emerges from taking Re
- **Dynamic**: Depends on Θ field configuration

### Resolution of Conflicts
Previous versions:
1. ❌ Old derivation (Appendix B) - matrix-centric
2. ❌ New derivation (consolidation K2/K5) - inconsistent normalization
3. ❌ Experimental holographic version - non-standard signature

**Canonical Version**: Use formula above with:
- Standard index convention: μ,ν = 0,1,2,3
- Signature convention: (+,−,−,−) [mostly minus]
- Consistent across all derivations

---

## 4. Stress-Energy Tensor T_μν

### Canonical Definition
```
T_μν = (∂_μΘ)(∂_νΘ†) - (1/2) g_μν g^αβ (∂_αΘ)(∂_βΘ†)
```

where all products are biquaternion multiplication.

This is the **energy-momentum tensor** derived from the biquaternionic field Lagrangian via Noether's theorem.

### Biquaternion Lagrangian
```
L = (∂_μΘ)(∂^μΘ†) - V(Θ)
```

where ∂^μ = g^{μν}∂_ν and V(Θ) is a potential term.

### Matrix Representation
In matrix representation, the equivalent form is:
```
T_μν = Tr[∂_μΘ ∂_νΘ†] - (1/2) g_μν Tr[∂^αΘ ∂_αΘ†]
```

### Resolution of Conflicts
Previous conflicting definitions:
1. ❌ T_μν = ΘΘ† - incorrect (no derivatives)
2. ❌ T_μν = dΘ/dT_B × dΘ†/dT_B - incorrect (wrong derivative)
3. ❌ T_μν from Lagrangian variation (different form) - inconsistent normalization

**Canonical Version**: Use the standard field-theoretic form shown above, derived from:
```
L = Tr[(∂_μΘ)† (∂^μΘ)]
```
via Noether's theorem.

---

## 5. QED/QCD Lagrangian

### Canonical Definition
```
L = Tr[(D_μΘ)† (D^μΘ)] - (1/4) F_μν F^μν - (1/4) G^a_μν G^{aμν}
```

where:
- `D_μ` = covariant derivative = ∂_μ + ig A_μ + ig_s T^a G^a_μ
- `F_μν` = electromagnetic field strength = ∂_μA_ν - ∂_νA_μ
- `G^a_μν` = gluon field strength for color index a
- `T^a` = SU(3) generators
- `g` = electromagnetic coupling
- `g_s` = strong coupling

### QED Only (Simplified)
```
L_QED = Tr[(D_μΘ)† (D^μΘ)] - (1/4) F_μν F^μν
```

### QCD Only (Simplified)
```
L_QCD = Tr[(D_μΘ)† (D^μΘ)] - (1/4) G^a_μν G^{aμν}
```

### Resolution of Conflicts
Previous issues:
1. ❌ Lagrangian exists but not consolidated with complex time
2. ❌ Some parts use E/B from Maxwell in flat space
3. ❌ Curved space vs flat space inconsistencies

**Canonical Version**: 
- Always use covariant derivatives in curved spacetime
- F_μν and G_μν are defined in the curved metric g_μν
- Complex time τ enters through Θ(q,τ) field dependence

---

## 6. Einstein Field Equation

### Canonical Form
```
R_μν - (1/2) g_μν R = 8πG T_μν
```

where T_μν is the canonical stress-energy tensor from section 4.

### Connection to Θ Field
```
∇†∇Θ(q,τ) = κ 𝒯(q,τ)
```

where:
- `∇†∇` = biquaternionic d'Alembertian
- `κ` = coupling constant (related to 8πG)
- `𝒯` = biquaternionic stress-energy

**Important**: In the real-valued limit (ψ → 0), this **exactly recovers** Einstein's equations.

### The T-shirt Formula and Covariant Derivative Structure

The equation ∇†∇Θ(q,τ) = κ𝒯(q,τ) is called the **T-shirt formula** because it compactly unifies all fundamental interactions.

**Critical Understanding**: ∇ is **NOT** an ordinary partial derivative. It is the **full covariant derivative** in curved spacetime with gauge fields:

```
∇_μ = ∂_μ + Γ_μ^grav + A_μ^SM
```

where:
- **Γ_μ^grav** = gravitational connection (Levi-Civita or spin connection) encoding spacetime curvature
- **A_μ^SM** = Standard Model gauge connection = ig₁B_μY + ig₂W_μᵃTᵃ + ig₃G_μᴬΛᴬ

Thus:
```
∇_μ = ∂_μ + (gravitational connection) + (U(1)_Y) + (SU(2)_L) + (SU(3)_c)
```

The operator ∇†∇ in curved spacetime is the **Laplace-Beltrami/d'Alembertian operator** that depends on:
- The metric g_μν (thus on curvature)
- All gauge field strengths (F_μν, W_μν, G_μν)
- Mixed gauge-gravity couplings

**This means**: The T-shirt formula is already a combined equation where:
- **Curvature + Gauge fields** = **Source (energy-momentum)**
- Gravity is encoded in how ∇ looks (via Γ_μ and the metric)
- SM forces are encoded in the gauge part of ∇

All fundamental interactions (gravity + electroweak + strong) live inside the single differential operator ∇.

For detailed derivation, see `canonical/explanation_of_nabla.tex`.

---

## 7. Standard Model Gauge Group

### Canonical Structure
```
G_SM = SU(3)_c × SU(2)_L × U(1)_Y
```

### Generators and Indices
- **SU(3)_c**: Color symmetry, generators T^a (a = 1,...,8)
- **SU(2)_L**: Weak isospin, generators τ^i (i = 1,2,3)
- **U(1)_Y**: Hypercharge, generator Y

### Couplings
- `g_s` = strong coupling (SU(3))
- `g` = weak coupling (SU(2))
- `g'` = hypercharge coupling (U(1))

### Resolution of Conflicts
Previous issues with Appendix G and K5:
- ❌ Color indices defined differently
- ❌ Generators inconsistent notation

**Canonical Version**:
- Always use a,b,c for color indices (1-8)
- Always use i,j,k for weak isospin (1-3)
- Standard normalization: Tr(T^a T^b) = (1/2)δ^{ab}

---

## 8. Fundamental Constants

### Inputs (Measured)
These are **inputs** to the theory, not predictions:
- `c` = speed of light
- `ħ` = reduced Planck constant
- `e` = elementary charge

### Predictions (Derived)
These are **predicted** by UBT:
- `α` = fine structure constant ≈ 1/137.036
- `m_e` = electron mass
- `m_μ` = muon mass
- `m_τ` = tau mass
- `Λ_QCD` = QCD scale

### Status of Each
| Constant | Status | Source |
|----------|--------|--------|
| α | **Predicted** | Geometric/topological derivation |
| m_e | **Predicted** | From Θ field self-energy |
| m_μ | **Predicted** | From phase structure |
| m_τ | **Predicted** | From phase structure |
| Λ_QCD | **Predicted** | From SU(3) emergence |
| G | **Input** | Newton's constant |
| θ_W | **Derived** | Weak mixing angle |

---

## 9. Electron Mass

### Canonical Derivation Method
There are **three methods** that must be unified:

1. **Spinor structure approach**
2. **Phase structure approach**
3. **Self-energy approach**

**Canonical Formula** (to be consolidated):
```
m_e = f(α, ħ, c, geometric_factors)
```

The final single method and formula will be established in `canonical/fields/electron_mass.tex`.

### Resolution of Conflicts
- ❌ Three different calculation methods exist
- ❌ Different assumptions (spin vs phase)
- ❌ Need single final numerical value

**Action Required**: Consolidate in Phase 3.

---

## 10. Symbol Dictionary (Phase 4)

### Reserved Symbols - Single Meaning Only

| Symbol | **ONLY** Meaning | Notes |
|--------|------------------|-------|
| `α` | Fine structure constant ≈ 1/137 | NO other uses |
| `ψ` | Imaginary component of complex time | NOT spinor, NOT wavefunction |
| `q` | Biquaternion coordinate (4 DOF) | Base space coordinate |
| `τ` | Complex time = t + iψ | NOT proper time |
| `Θ` | Fundamental biquaternion field | Capital theta only |
| `g_μν` | Metric tensor | NO other metric symbols |
| `T_μν` | Stress-energy tensor | Canonical form only |

### Forbidden Uses
- ❌ `α` for any angle, decay rate, or other parameter
- ❌ `ψ` for wavefunction or spinor (use `Ψ` if needed)
- ❌ `q` for charge or other quantum numbers
- ❌ Multiple definitions of modulus or fundamental domain

### Additional Standardization
- Greek indices `μ,ν,ρ,σ` for spacetime (0-3)
- Latin indices `i,j,k` for spatial (1-3) or weak isospin
- Latin indices `a,b,c` for color (1-8)
- Capital Latin `A,B,C` for biquaternion components

---

## 11. Psychons and Θ-Resonance

### Canonical Definition
**Psychons** are quantum excitations of the consciousness field, defined as:
```
ψ_psychon: excitations in the imaginary time component ψ
```

### Lagrangian (to be formalized)
The psychon Lagrangian must be derived from variation of the action:
```
S[Θ,ψ] = ∫ d⁴x √(-g) L[Θ,ψ]
```

**Action Required**: Formalize in Phase 3 - currently lacks precise mathematical form.

### Θ-Resonator
Experimental device concept for detecting psychon excitations.

**Status**: Conceptual design exists, mathematical formalization needed.

---

## 12. Theta Functions and Toroidal Projection

### Canonical Definitions

#### Fundamental Domain
```
τ ∈ ℍ (upper half-plane)
Im(τ) > 0
```

Standard fundamental domain for modular group SL(2,ℤ).

#### Theta Functions
Using Jacobi theta functions with standard normalization:
```
θ_2(z,τ), θ_3(z,τ), θ_4(z,τ)
```

### Resolution of Conflicts
Previous issues:
- ❌ Two different definitions of modulus τ
- ❌ Two definitions of fundamental domain
- ❌ Conflicting normalization of θ₃ and θ₂

**Canonical Version**:
- Use standard Jacobi theta function conventions
- Fundamental domain: |Re(τ)| ≤ 1/2, |τ| ≥ 1
- Normalization: Follow Whittaker & Watson or NIST DLMF

---

## Implementation Notes

### Phase 2 Tasks
1. Create canonical field definitions in `canonical/fields/`
2. Create canonical geometry in `canonical/geometry/`
3. Create canonical interactions in `canonical/interactions/`

### Phase 3 Tasks
1. Rewrite all appendices using these definitions
2. Remove all conflicting versions
3. Single source files for QED, QCD, metric, etc.

### Phase 4 Tasks
1. Global symbol replacement
2. Notation consistency check
3. Cross-reference validation

### Phase 5 Tasks
1. Main article using canonical definitions
2. 12-section structure
3. Clean compilation

---

## Version Control

**Version**: 1.0  
**Date**: 2025-11-14  
**Status**: Phase 1 Complete - Definitions Documented  
**Next**: Phase 2 - Create canonical .tex files

---

## References

All canonical definitions derive from:
1. COPILOT_INSTRUCTIONS_CONSOLIDATION.md (Phase 2 section)
2. Conflict analysis from problem statement
3. Standard physics conventions (when applicable)

