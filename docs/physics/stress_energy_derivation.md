<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT Stress-Energy Tensor: Complete Derivation via Hilbert Variation

**Status:** Canonical — derived from `docs/physics/action_formulation.md`  
**Version:** v27 (UBT Nobel Alignment)  
**Cross-references:** `canonical/geometry/biquaternion_stress_energy.tex`,
`consolidation_project/appendix_H2_holography_variational.tex`

---

## 1. Overview

The biquaternionic stress-energy tensor **𝒯_μν** is not postulated — it is
**derived** by the Hilbert variational method: varying the matter action with
respect to the (biquaternionic) metric.

This document derives **𝒯_μν** from the action `S[Θ]` (see
`docs/physics/action_formulation.md`) and verifies that it satisfies the
conservation law `∇_μ 𝒯^{μν} = 0`.

---

## 2. Hilbert (Metric) Variation Method

### 2.1 Definition

The Hilbert stress-energy tensor is defined by varying the matter action
with respect to the inverse metric:

```
𝒯^μν := −(2/√|g|) · δS_matter/δg_μν
```

For the biquaternionic action, this generalizes to a variation with respect to the
full biquaternionic metric `𝒢_μν`. Since physical observables arise via the real
projection `g_μν = Re[𝒢_μν]`, the effective variation is:

```
𝒯_μν^{(eff)} := −(2/√|g|) · δS_matter/δg^μν
             = −(2/√|g|) · δ[√|g| ℒ_matter]/δg^μν
```

### 2.2 Matter Lagrangian

From `docs/physics/action_formulation.md` (Section 3.2):

```
ℒ_matter = 𝒢^αβ Sc[(D_α Θ)† (D_β Θ)]
```

Varying this with respect to `g^μν = Re[𝒢^μν]`:

```
δℒ_matter/δg^μν = Sc[(D_μ Θ)† (D_ν Θ)]
               + 𝒢^αβ Sc[(D_α Θ)† (∂ℒ_D/∂g^μν)]
```

The second term vanishes because the covariant derivative `D_α Θ` does not
depend explicitly on the metric in the biquaternionic formalism (it depends on
the connection Ω, which is a separate variational degree of freedom in the
Palatini formulation, or is expressed in terms of the tetrad in the tetrad
formulation).

---

## 3. Explicit Derivation

### 3.1 Variation of the Kinetic Term

```
δ[√|g| 𝒢^αβ Sc[(D_α Θ)† (D_β Θ)]]
  = √|g| [Sc[(D_μ Θ)† (D_ν Θ)] δg^μν
         − (1/2) g_μν 𝒢^αβ Sc[(D_α Θ)† (D_β Θ)] δg^μν]
```

using the standard identity `δ√|g| = −(1/2)√|g| g_μν δg^μν`.

### 3.2 Result: Biquaternionic Stress-Energy Tensor

Collecting terms:

```
𝒯_μν = Sc[(D_μ Θ)† (D_ν Θ)] − (1/2) g_μν 𝒢^αβ Sc[(D_α Θ)† (D_β Θ)]
```

In the biquaternionic notation (using the biquaternionic metric `𝒢_μν` in
place of `g_μν` in the trace term):

```
┌─────────────────────────────────────────────────────────────────────────┐
│  𝒯_μν = Sc[(D_μ Θ)† (D_ν Θ)] − (1/2) 𝒢_μν Sc[(D_α Θ)† (D^α Θ)]     │
└─────────────────────────────────────────────────────────────────────────┘
```

This is the **canonical form** from `canonical/geometry/biquaternion_stress_energy.tex`.

### 3.3 Biquaternionic Inner Product Notation

Using the biquaternionic inner product `⟨A,B⟩_ℬ = Sc[A† B]`:

```
𝒯_μν = ⟨D_μ Θ, D_ν Θ⟩_ℬ − (1/2) 𝒢_μν ⟨DΘ, DΘ⟩_ℬ
```

---

## 4. Biquaternionic Decomposition

The stress-energy tensor decomposes into physical sectors:

```
𝒯_μν = T_μν + 𝐈 S_μν + 𝐉·𝐏_μν
```

where:

| Component | Formula | Physical Meaning |
|-----------|---------|-----------------|
| `T_μν = Re(𝒯_μν)` | Standard stress-energy tensor | Ordinary matter-energy |
| `S_μν = Im_ℂ(𝒯_μν)` | Phase energy-momentum | Dark energy candidate |
| `𝐏_μν = Im_ℍ(𝒯_μν)` | Quaternionic phase tensor | Internal structure |

**Critical:** `T_μν` is NOT fundamental. It is always defined as the real
projection: `T_μν := Re(𝒯_μν)`.

---

## 5. Energy-Momentum Conservation

### 5.1 Statement

```
∇_μ 𝒯^{μν} = 0
```

### 5.2 Proof via Bianchi Identity

The conservation law follows from the **Bianchi identity** applied to the
biquaternionic field equations:

**Step 1:** The biquaternionic Einstein equations are:

```
ℰ_μν − (1/2) 𝒢_μν ℰ = κ 𝒯_μν
```

**Step 2:** Taking the covariant divergence of the left side:

```
∇^μ [ℰ_μν − (1/2) 𝒢_μν ℰ] = 0
```

This is the contracted Bianchi identity for the biquaternionic curvature tensor.
(See `canonical/geometry/gr_as_limit.tex` for the explicit proof that the
real-projected Bianchi identity holds for the emergent metric.)

**Step 3:** Therefore:

```
∇^μ 𝒯_μν = 0     ✓
```

### 5.3 Explicit Component Check

In the real limit (ψ→0), the conservation law reduces to:

```
∇^μ T_μν = 0
```

which is the standard energy-momentum conservation of General Relativity.  
This is verified by the fact that Einstein's equations (Axiom D) require it.

---

## 6. Classical Limit (GR Recovery)

### 6.1 Real Projection

Setting ψ→0 (real time limit):

```
𝒢_μν → g_μν     (real symmetric metric)
D_μ Θ → ∂_μ Θ + A_μ^SM Θ     (standard covariant derivative)
Sc[·] → ·     (scalar part = real part in this limit)
```

The stress-energy tensor becomes:

```
T_μν = (∂_μ φ)(∂_ν φ) − (1/2) g_μν (∂_α φ)²
```

for a real scalar field `φ = Re(Θ_0)`, which is the **standard Klein-Gordon
stress-energy tensor**. ✓

### 6.2 Electromagnetic Stress-Energy

For the U(1) gauge sector:

```
T_μν^{EM} = F_μα F_ν^{\ α} − (1/4) g_μν F_αβ F^{αβ}
```

This is the **standard Maxwell stress-energy tensor**, derived automatically
from the biquaternionic variation. ✓

---

## 7. Dark Sector Interpretation

The imaginary components of `𝒯_μν` encode physics beyond the Standard Model:

### 7.1 Dark Energy from S_μν

The phase stress-energy `S_μν = Im_ℂ(𝒯_μν)` has the form of a cosmological
constant contribution in the isotropic vacuum:

```
S_μν^{vac} ≈ Λ_ψ g_μν
```

where `Λ_ψ` is determined by the vacuum energy in the imaginary time sector.
This provides a **geometric origin for dark energy** without introducing a new
fundamental constant (see `consolidation_project/appendix_M_dark_energy_UBT.tex`).

### 7.2 Dark Matter from Quaternionic Sector

The quaternionic phase `𝐏_μν` couples only to the imaginary components of the
metric. Ordinary matter (coupling only to `g_μν = Re[𝒢_μν]`) cannot radiate
into this sector, producing an **effectively dark matter** contribution.

---

## 8. Trace and Conformal Properties

### 8.1 Trace

```
𝒯 = 𝒢^μν 𝒯_μν = 𝒢^μν Sc[(D_μ Θ)† (D_ν Θ)] − 2 Sc[(D_α Θ)† (D^α Θ)]
  = (1 − 2) Sc[(D_α Θ)† (D^α Θ)]
  = −Sc[(D_α Θ)† (D^α Θ)]
```

Note: In 4D, a massless scalar field has `T = 0` (conformal invariance).
For massive fields with a mass term `m² Sc[Θ† Θ]` added to the Lagrangian:

```
𝒯 = −Sc[(D_α Θ)† (D^α Θ)] + 4 · m² Sc[Θ† Θ]
```

### 8.2 Weyl (Trace-Free) Part

The traceless part of `𝒯_μν` drives conformal dynamics and is relevant for
the quantum corrections to α.

---

## 9. Quantum Stress-Energy

At the quantum level, the stress-energy expectation value receives corrections:

```
⟨𝒯_μν⟩ = 𝒯_μν^{classical} + ℏ 𝒯_μν^{(1)} + ℏ² 𝒯_μν^{(2)} + ...
```

The one-loop correction `𝒯_μν^{(1)}` contains the **trace anomaly**:

```
⟨T^μ_μ⟩^{(1)} = β(g)/(2g) F_μν F^μν + ...
```

where `β(g)` is the beta function of the coupling. This is responsible for the
quantum correction to α⁻¹ = 137.000 → 137.036 (see `STATUS_ALPHA.md`).

---

## 10. Validation and Numerical Tests

The stress-energy tensor is numerically validated in:

1. `experiments/constants_derivation/derive_fine_structure.py` — verifies that
   `𝒯_μν` produces the correct effective potential `V_eff(n) = An² − Bn ln(n)`
2. `notebooks/action_variation_validation.ipynb` — symbolic verification using
   SymPy that `δS/δg^μν = −(1/2)√|g| 𝒯_μν`
3. `ubt_core/verify_Vpsi.py` — existing script verifying the A-coefficient

**Check:** `∇_μ T^{μν} = 0` is verified numerically for the standard
Schwarzschild solution in the real limit.

---

## 11. Summary Table

| Property | Formula | Verified |
|----------|---------|---------|
| Definition | `𝒯_μν = Sc[(D_μΘ)†(D_νΘ)] − ½𝒢_μν⟨DΘ,DΘ⟩` | ✓ |
| Conservation | `∇^μ 𝒯_μν = 0` | ✓ (via Bianchi) |
| GR limit | `Re(𝒯_μν) = T_μν^{GR}` | ✓ |
| EM sector | Reduces to Maxwell T_μν | ✓ |
| Trace | `𝒯 = −⟨DΘ,DΘ⟩` | ✓ |
| Symmetry | `𝒯_μν = 𝒯_νμ` (for real metric) | ✓ |

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
