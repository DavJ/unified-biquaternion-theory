# Canonical Definitions for Unified Biquaternion Theory

**Purpose**: This document establishes the single, authoritative version of all core UBT definitions to resolve conflicts and duplications across the theory.

**Status**: Active canonical reference — definitions complete; derivation gaps documented below.

**Confidence labels used in this document:**

| Label | Meaning |
|-------|---------|
| **Strong** | Rigorous derivation; zero free parameters |
| **Strong Partial** | Structural derivation substantially complete; ≤1 open sub-gap |
| **Candidate** | Proposed mechanism with supporting evidence; ≥1 gap unresolved |
| **Experimental** | Hypothesis supported by numerical/observational tests; no algebraic proof |
| **Open** | No complete derivation known; active problem |
| **Deprecated** | Approach proved to fail or superseded; preserved for reference |

---

## 1. Complex Time τ (Canonical)

### Canonical Definition
The canonical UBT time coordinate is **complex time**:

```
τ = t + iψ
```

where:
- `t` ∈ ℝ = real time coordinate (standard physical time)
- `ψ` ∈ ℝ = scalar imaginary time component
- `i` = imaginary unit

### Physical Interpretation

**Real component (t)**:
- Ordinary physical time
- Observable temporal evolution
- Causality structure

**Scalar imaginary (ψ)**:
- Isotropic phase structure of Θ field
- Scalar dark-sector degree of freedom *(interpretation: speculative/open)*
- Universal quantum coherence (direction-independent)

**Critical**: Both components are **dynamical variables**, not passive parameters.

### Classical Limit

When the imaginary component vanishes:
```
ψ → 0  ⇒  τ → t  ⇒  UBT reduces to standard GR/QFT
```

### Relation to Standard Physics

In the limit τ → t:
- The special-relativistic flat sector is recovered when the connection curvature vanishes and an inertial frame is chosen.
- Recovery of the complete Einstein dynamics and the full Standard Model remains a derivation target, not an unconditional proved statement.

### Resolution of Conflicts
The theory previously had 3+ conflicting versions:
1. ❌ Drift-diffusion Fokker-Planck variant
2. ❌ Toroidal variant with θ-functions  
3. ❌ Hermitized variant (Appendix F)
4. ❌ Biquaternion time T_B — exploratory extension, now noncanonical

**Canonical Version**: `τ = t + iψ` is the single canonical time coordinate of UBT. Earlier biquaternionic time T_B was exploratory and is now noncanonical.

---

### Historical/Speculative Extension: Biquaternion Time T_B

> **Status**: Deprecated / historical. The biquaternionic time T_B was an earlier exploratory formulation and is **not part of the canonical minimal theory**. It is preserved here for historical reference only.

The earlier biquaternion time extension was:

```
T_B = t + iψ + jχ + kξ
```

where `ψ, χ, ξ` ∈ ℝ are imaginary time components and `i, j, k` are quaternion units.

This formulation admitted the hierarchical structure **T_B → τ → t** in isotropic and classical limits respectively. However, the additional degrees of freedom (χ, ξ) lack closed derivations within canonical UBT, and their physical interpretation (torsion, anisotropic dark-sector fields) remains speculative and open. They are therefore not part of the canonical minimal theory.

Any work using T_B should be placed in `research_tracks/` or `speculative_extensions/`.

---

## 2. Theta Field Θ(q,τ)

### Canonical Definition
The fundamental field is a **biquaternion**:

```
Θ(q, τ) ∈ B = H ⊗ ℂ
Θ = Θ₀ + Θ₁i + Θ₂j + Θ₃k,    where Θₐ ∈ ℂ
```

where:
- `B` = biquaternion algebra = H ⊗ ℂ (quaternions tensored with complex numbers)
- `H` = quaternion algebra with units {1, i, j, k}
- `i, j, k` = quaternion units satisfying i² = j² = k² = ijk = −1
- `Θₐ` (a = 0,1,2,3) = **complex-valued** components
- `q` ∈ B = biquaternion coordinate (4 DOF)
- `τ = t + iψ` = complex time (canonical)
  - Earlier biquaternion time T_B = t+iψ+jχ+kξ is a deprecated/historical extension

### Matrix Representation

For computational purposes, Θ can be represented as a matrix:

**Spinor representation**: Θ ↔ 4×4 complex matrix (16 complex DOF = 32 real DOF)
**Extended representation**: Θ ↔ 8×8 complex matrix (for full SM with 3 generations)

**Important**: Matrix forms are **representations only**, not the canonical definition. The canonical object is the biquaternion itself.

### Biquaternion Operations

Two involutions must be distinguished.

**Quaternion conjugation** (used in the Lorentzian metric identity):
```
(z⁰·1 + zᵏe_k)^sharp = z⁰·1 - zᵏe_k
```
It reverses the quaternion units but does not complex-conjugate the commuting complex coefficients.

**Hermitian conjugation** (used where a positive inner product is required):
```
Θ^ddagger = complex-conjugate coefficients followed by quaternion conjugation
```
These operations are not interchangeable.  In particular, the Lorentzian time sign in the classical tetrad sector comes from quaternion conjugation on
`i e⁰·1 + eᵏe_k`, not from a positive Hermitian norm.

### Resolution of Conflicts
Previous conflicting versions:
1. ❌ 4×4 spinor matrix (older version) - matrix as primary object
2. ❌ 8×8 matrix structure (consolidation) - matrix as primary object
3. ❌ 4D biquaternion (old preprint) - lacked clear definition

**Canonical Version**: 
- **Θ is a biquaternion** Θ(q,τ) ∈ B = H ⊗ ℂ
- **Matrix forms** are computational representations only
- Works with complex time τ = t + iψ

---

## 3. Covariant Tetrad and Metric Tensor g_μν

### Canonical Definition

The classical local geometric carrier is the covariant first jet of the single field:

```
E_μ := N₀^(-1/2) D_μΘ
```

where `N₀ > 0` is a fixed global unit-setting constant and `D_μ` is the UBT covariant derivative.  On the classical Lorentz slice,

```
E_μ = i e_μ^0 · 1 + e_μ^k e_k,     e_μ^a ∈ ℝ,
```

and quaternion conjugation `sharp` reverses the three quaternion units while leaving the commuting complex unit `i` untouched.

The metric is defined by the central anticommutator identity

```
1/2 (E_μ^sharp E_ν + E_ν^sharp E_μ) = g_μν · 1.
```

Equivalently,

```
g_μν = e_μ^a e_ν^b η_ab,     η_ab = diag(-1,+1,+1,+1).
```

The left-hand side is already a real central element of the biquaternion algebra.  No trace, `Re(...)`, phase projector, preferred ψ-section, or compact-ψ average is part of the canonical metric definition.

### Rank and status

At every nondegenerate tetrad the differential `e_μ^a -> g_μν` has rank ten.  Its six-dimensional kernel is the infinitesimal local Lorentz freedom.  Thus the old comparison “Θ has eight real components but g has ten” is not a local kinematic obstruction: the metric is built from four covariant first derivatives, not from the value of Θ alone.

The local rank theorem does **not** by itself prove that every required curved
tetrad is generated on shell by one $\Theta$.  The connection and integrability
results refine this statement substantially.

### Connection and Christoffel symbols

`Ω_μ` transports the internal Lorentz/biquaternionic frame;
`Γ^ρ_{μν}` transports coordinate indices.  They are related by tetrad
compatibility, not by `Γ = Re Ω`:

```text
∂_μe_ν^a - Γ^ρ_{μν}e_ρ^a + ω_μ^a_b e_ν^b = 0.
```

For every nondegenerate tetrad and specified torsion

```text
T^a = de^a + ω^a_b ∧ e^b,
```

the metric-compatible frame connection is uniquely

```text
ω = ω_LC(e) + K(T),
K_abc = 1/2 (T_cab - T_abc - T_bca).
```

This closes `GAP-10Ω-KIN`.  In the torsion-free classical GR branch,
`T=K=0` and `ω=ω_LC(e)`, closing `GAP-10Ω-GR`.  The remaining question is
`GAP-10T-DYN`: derive torsion or its absence from the canonical UBT action.
Every metric-compatible Lorentz connection preserves `η_ab` and the Lorentz
slice, closing `GAP-10L-CONN`; preservation by the complete $\Theta$ dynamics
remains `GAP-10L-DYN`.

### Flat representer and partial integrability closure

Every constant Lorentz tetrad has the explicit inertial-gauge representer

```text
Theta_aff(x) = Theta_0 + sqrt(N0) E_mu x^mu.
```

For `E_0=i 1` and `E_k=e_k`, this gives Minkowski spacetime and has zero
second spacetime derivatives.  This closes `GAP-10I-SR`.

A naive one-sided regular derivative

```text
D_mu^L Theta = partial_mu Theta + A_mu Theta
```

obeys `[D_mu^L,D_nu^L]Theta = F^L_mu_nu Theta`.  Under torsion-free tetrad
compatibility, invertible `Theta` then forces `F^L_mu_nu=0`.  This closes the
one-sided generic curved route as `GAP-10I-1S: NO-GO`.

The viable algebra-native curved form is two-sided:

```text
D_mu Theta = partial_mu Theta + A_mu Theta - Theta B_mu,
[D_mu,D_nu]Theta = F^A_mu_nu Theta - Theta F^B_mu_nu.
```

For invertible `Theta`, integrability permits nonzero curvatures related by

```text
F^A_mu_nu = Theta F^B_mu_nu Theta^(-1).
```

This narrows `GAP-10I-2S`, but the action must still determine the paired
connections, involution, torsion, and boundary conditions.  Curved-space local
and global existence remains `GAP-10I-CURVED: OPEN`.

### Implicit versus transcendental

After connection reconstruction, the curved tetrad equation is an implicit
nonlinear first-order PDE/fixed-point system because `E` appears on both sides
through the connection.  If the allowed $\Theta(q,\tau)$ is a Jacobi-theta or
other transcendental function, the concrete system may additionally be
transcendental.  These are distinct mathematical properties.

In a flat inertial branch one may choose `Ω_μ=0`, `Γ^ρ_{μν}=0`, and
`D_μ=∂_μ`.

### Superseded definitions

Earlier formulas such as `g_μν = Re[(∂_μΘ)(∂_νΘ†)]`, matrix traces, local denominators, phase projections, and compact-fiber averages are not the canonical local metric.  They remain only in historical or explicitly exploratory documents.

---

## 4. Stress-Energy Tensor T_μν

### Current canonical status

The stress-energy source must be derived by varying the same UBT action that
defines the covariant derivative and the central tetrad metric.  Schematically,

```
T_μν := -(2/√(-g)) δS_matter/δg^{μν},
```

with `g_μν` constrained by

```
1/2 (E_μ^sharp E_ν + E_ν^sharp E_μ) = g_μν · 1,
E_μ = N₀^(-1/2) D_μΘ.
```

Earlier component formulas built only from `∂_μΘ` are useful scalar-field
analogies but are not a complete canonical result once the frame connection is
active.  A full derivation must include the dependence of `D_μ`, the connection
equation, and any gauge sectors.  The exact unified stress-energy formula is
therefore **OPEN / representation-dependent**, not locked by the former
projection-based expression.

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

**Important**: The real-valued limit `ψ → 0` recovers the ordinary real-time domain and the flat special-relativistic branch when the connection curvature vanishes.  Complete Einstein dynamics from the T-shirt/master equation remains `GAP-10D: OPEN`; it must not be described as already derived.

### The T-shirt Formula and Covariant Derivative Structure

The equation ∇†∇Θ(q,τ) = κ𝒯(q,τ) is called the **T-shirt formula** because it compactly unifies all fundamental interactions.

**Critical Understanding**: ∇ is **NOT** an ordinary partial derivative. It is the **full covariant derivative** in curved spacetime with gauge fields:

```
∇_μ = ∂_μ + Γ_μ^grav + A_μ^SM
```

where:
- **Γ_μ^grav** = shorthand for the gravitational covariant structure; coordinate `Γ^ρ_{μν}` and frame/spin `Ω_μ` must be distinguished.  In the torsion-free classical branch `Ω_μ` is the unique spin lift of the Levi--Civita tetrad connection.
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
| Constant | Confidence | Source |
|----------|-----------|--------|
| α | **Open** | B_base gap unresolved — bare value follows from framework given B≈46.3 but B itself not zero-free-parameter; see DERIVATION_INDEX.md |
| m_e | **Strong Partial** | From Θ field self-energy (mechanism partially derived; Gaps Y1/Y2 open) |
| m_μ | **Candidate** | Hecke eigenvalue match at p=139 (0.05% + 1.6%); algebraic mechanism not closed |
| m_τ | **Candidate** | Hecke eigenvalue match; same mechanism as m_μ; instanton approach Dead End |
| Λ_QCD | **Candidate** | From SU(3) emergence (≥1 free parameter) |
| G | **Input** | Newton's constant; not predicted |
| θ_W | **Candidate** | Weak mixing angle structural argument; g/g' ratio not algebraically fixed |

---

## 9. Electron / Lepton Mass Spectrum

**Confidence: Open**

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
- ❌ Lepton mass ratios m_μ/m_e ≈ 207 and m_τ/m_μ ≈ 16.8 not reproduced from first principles (KK mismatch theorem forbids reproduction from W2 formula — Gap M4)
- ❌ Hecke eigenvalue match at p=137/139 supports m_μ, m_τ at **Candidate** level but mechanism not algebraically closed

**Status**: All three lepton masses remain **Open** at the level of zero-free-parameter algebraic derivation.  
Hecke numerical support for m_μ, m_τ is at **Candidate** level.  
See DERIVATION_INDEX.md (Three Fermion Generations / Lepton Sector) for full detail.

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

## 11. Speculative Boundary Note (Non-canonical)

> **Note**: Psychon content has been moved out of `canonical/` into
> `speculative_extensions/consciousness/psychons.tex`.
> Consciousness/psychon content is explicitly **non-canonical** and tracked only in `speculative_extensions/`.
>
> The imaginary time component ψ is a genuine mathematical degree of freedom
> of complex time τ = t + iψ.  Its possible physical interpretation as a "consciousness
> substrate" is *speculative / open* and must not be treated as a proved or mainline result.
>
> For the speculative consciousness formulation see `speculative_extensions/consciousness/`.

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

**Version**: 2.0  
**Date**: 2026-04-27  
**Status**: Active canonical reference — definitions complete; confidence labels added  
**Next**: Phase 3 — rewrite all appendices using these definitions

---

## References

All canonical definitions derive from:
1. COPILOT_INSTRUCTIONS_CONSOLIDATION.md (Phase 2 section)
2. Conflict analysis from problem statement
3. Standard physics conventions (when applicable)

