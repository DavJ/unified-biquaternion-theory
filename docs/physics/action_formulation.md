<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT Complete Action Functional S[Θ]

**Status:** Canonical — derived from Axioms A–D in `core/AXIOMS.md`  
**Version:** v27 (UBT Nobel Alignment)  
**Cross-references:** `consolidation_project/appendix_H2_holography_variational.tex`,
`canonical/fields/theta_field.tex`, `canonical/geometry/biquaternion_stress_energy.tex`

---

## 1. Motivation and Derivation Strategy

The UBT action functional is **not postulated** — it is uniquely determined by the
biquaternionic field structure and the requirement that the Euler–Lagrange equations
reproduce:

1. The biquaternionic field equation `∇†∇Θ = κ𝒯` (Axiom D).
2. Einstein's equations `G_μν = κ T_μν` in the real limit ψ→0 (Axiom D, GR recovery).
3. Standard Model gauge invariance under `Aut(ℂ⊗ℍ)` (Axioms A–B).
4. Conservation of biquaternionic stress-energy `∇^μ 𝒯_μν = 0`.

---

## 2. Geometric Prerequisites

### 2.1 Biquaternionic Metric

From Axiom C, the generalized metric emerges as:

```
𝒢_μν(x,τ) := (D_μ Θ)† D_ν Θ     ∈ ℂ⊗ℍ
```

Its real projection gives the observable GR metric:

```
g_μν(x) := Re[𝒢_μν(x,τ)]
```

The determinant factor for the integration measure is:

```
√|det g| = √|det Re[𝒢_μν]|
```

### 2.2 Covariant Derivative

The full covariant derivative acts on Θ as:

```
D_μ Θ = ∂_μ Θ + Ω_μ^grav Θ + Ω_μ^SM Θ
```

where:
- `Ω_μ^grav` = biquaternionic gravitational connection (see `canonical/geometry/biquaternion_connection.tex`)
- `Ω_μ^SM = ig₁ B_μ Y + ig₂ W_μ^a T^a + ig₃ G_μ^A λ^A` = Standard Model gauge connection

### 2.3 Biquaternionic Curvature

The curvature two-form:

```
ℛ_μν = [D_μ, D_ν] = ∂_μ Ω_ν − ∂_ν Ω_μ + [Ω_μ, Ω_ν]
```

In the real limit, this reduces to the Riemann tensor of GR.

---

## 3. The Complete Action Functional

### 3.1 Total Action

The complete UBT action is:

```
S[Θ] = S_matter[Θ] + S_gravity[Θ] + S_boundary[Θ]
```

### 3.2 Matter (Kinetic) Term

```
S_matter[Θ] = ∫_𝓜 d⁴x √|det g| · ℒ_matter

ℒ_matter = Sc[(D_μ Θ)† (D^μ Θ)]
          = 𝒢^μν Sc[(D_μ Θ)† (D_ν Θ)]
```

where `Sc(·)` extracts the scalar (real) part of the biquaternionic product.

**Key property:** This is uniquely the norm-squared of the covariant derivative, making
it the minimal kinetic term consistent with biquaternionic gauge invariance. No
additional coupling constants are introduced.

### 3.3 Gravitational (Curvature) Term

The gravitational contribution arises from the curvature of the biquaternionic
connection. In analogy with the Einstein–Hilbert action but extended to the full
biquaternionic structure:

```
S_gravity[Θ] = (1/2κ) ∫_𝓜 d⁴x √|det g| · Sc[ℛ_μν^† ℛ^μν]^{1/2}
             ≡ (1/2κ) ∫_𝓜 d⁴x √|det g| · R_UBT[Θ]
```

where `R_UBT[Θ]` is the biquaternionic Ricci scalar, defined as the trace of the
curvature two-form contracted with the inverse metric:

```
R_UBT = 𝒢^μα 𝒢^νβ Sc[ℛ_μν† ℛ_αβ]
```

**GR limit:** In the real limit ψ→0,

```
R_UBT → R = g^μν R_μν    (standard Ricci scalar)
```

recovering the Einstein–Hilbert Lagrangian density `R/(2κ)`.

### 3.4 Boundary Term (Gibbons–Hawking–York Extension)

For a manifold 𝓜 with boundary ∂𝓜, the variational principle requires the
Gibbons–Hawking–York boundary term (see `appendix_H2_holography_variational.tex`):

```
S_boundary[Θ] = (1/κ) ∫_{∂𝓜} d³y √|det h| · K_UBT
```

where:
- `h_{ab}` = induced metric on ∂𝓜 (real projection of biquaternionic induced metric)
- `K_UBT = Sc[K_biq]` = scalar extrinsic curvature of the boundary
- The sign convention is chosen so that `δS_boundary` exactly cancels the
  boundary contributions from varying `S_gravity`.

---

## 4. Euler–Lagrange Equations

### 4.1 Variational Derivative

Taking the variation of the total action with respect to `Θ†`:

```
δS/δΘ† = 0
```

yields the **biquaternionic field equation**:

```
∇†∇ Θ(q,τ) = κ 𝒯(q,τ)
```

where:
- `∇† = −𝒢^μν D_μ†` is the biquaternionic Laplace–Beltrami operator (Hodge adjoint)
- `∇∇ = D^μ D_μ` is the covariant d'Alembertian
- `𝒯` is the biquaternionic stress-energy tensor (source term)

### 4.2 Metric Variation (Gravitational Equations)

Varying with respect to the metric (or equivalently with respect to the connection
Ω_μ^grav), one obtains the generalized Einstein equations:

```
ℰ_μν − (1/2) 𝒢_μν ℰ = κ 𝒯_μν
```

where `ℰ_μν` is the biquaternionic Einstein tensor (see `canonical/geometry/biquaternion_curvature.tex`).

**Real projection (GR limit):**

```
Re[ℰ_μν] = G_μν,    Re[𝒯_μν] = T_μν
→  G_μν = κ T_μν       ✓ (Einstein equations recovered)
```

### 4.3 Gauge Field Equations

Varying with respect to the SM gauge connections gives the Yang–Mills equations with
biquaternionic source currents. In each gauge sector:

- **U(1):** Maxwell equations with biquaternionic current `J^μ_EM = Sc[Θ† D^μ Θ]`
- **SU(2):** Non-abelian weak equations with weak current
- **SU(3):** Yang–Mills QCD equations with color current

---

## 5. Symmetries of the Action

| Symmetry | Generator | Consequence |
|----------|-----------|-------------|
| `Diff(𝓜)` (general covariance) | ξ^μ ∂_μ | Bianchi identity `∇^μ ℰ_μν = 0` |
| `U(1)_Y` hypercharge | `e^{iα Y}` | Electromagnetic gauge invariance |
| `SU(2)_L` weak isospin | `e^{iθ^a T^a}` | Weak gauge invariance |
| `SU(3)_c` color | `e^{iφ^A λ^A}` | Color gauge invariance |
| Complex time shift `τ→τ+iε` | `∂_ψ` | Phase momentum conservation |
| PT symmetry | `(t,ψ)→(-t,-ψ)` | CPT-like invariance |

---

## 6. Limits and Special Cases

### 6.1 GR Limit (ψ→0)

Setting `ψ=0` (real time limit):

```
S[Θ]|_{ψ=0} = (1/2κ) ∫ d⁴x √|g| R + ∫ d⁴x √|g| ℒ_SM
```

This is the standard Einstein–Hilbert + Standard Model action. The UBT action
**strictly contains** GR as a special case — it does not modify it.

### 6.2 Flat Spacetime Limit

In flat spacetime (Minkowski background, `g_μν = η_μν`):

```
S_matter → ∫ d⁴x Sc[(∂_μ Θ + A_μ^SM Θ)† (∂^μ Θ + A^{μ,SM} Θ)]
```

This reproduces the Standard Model kinetic terms for all matter fields.

### 6.3 Free Field (No Gauge) Limit

Setting all gauge connections to zero:

```
ℒ_free = Sc[(∂_μ Θ)† (∂^μ Θ)]
```

This gives the biquaternionic Klein–Gordon equation, which decomposes into 16 complex
Klein–Gordon equations for the components of Θ.

---

## 7. Dimensional Analysis

In natural units (ℏ = c = 1):

| Quantity | Dimension | Value |
|----------|-----------|-------|
| `[Θ]` | mass^1 | (field dimension) |
| `[S]` | dimensionless | (action in ℏ units) |
| `[ℒ]` | mass^4 | (Lagrangian density in 4D) |
| `[κ]` | mass^{-2} | κ = 8πG/c⁴ |
| `[D_μ Θ]` | mass^2 | |

The action `S[Θ]` is dimensionless as required for a well-defined path integral
`∫ 𝒟Θ e^{iS[Θ]/ℏ}`.

---

## 8. Conservation Laws

### 8.1 Biquaternionic Noether Currents

For each continuous symmetry with generator `G`, there is a conserved biquaternionic
current `J^μ_G` satisfying `D_μ J^μ_G = 0`.

### 8.2 Stress-Energy Conservation

The Bianchi identity applied to the biquaternionic Einstein equations gives:

```
∇_μ 𝒯^{μν} = 0
```

Real projection:

```
∇_μ T^{μν} = 0     ✓ (standard energy-momentum conservation)
```

See `docs/physics/stress_energy_derivation.md` for the full derivation.

---

## 9. Validation

The action is validated in:
- `notebooks/action_variation_validation.ipynb` — symbolic verification of
  Euler–Lagrange equations and GR limit
- `experiments/constants_derivation/` — numerical verification that the
  action reproduces the correct effective potential for α
- `ubt_core/verify_Vpsi.py` — existing script verifying the A-coefficient

---

## 10. Open Problems

| Problem | Status | Impact |
|---------|--------|--------|
| B-coefficient derivation (N_eff) | Semi-empirical (N_eff=12 fitted) | Blocks exact α claim |
| Quantum correction R_UBT ≈ 1.114 | Not derived from first principles | Closes 12% gap in α |
| Path integral measure for Θ | Formal only; regularization needed | Quantum gravity |
| Non-perturbative sector | Instantons/solitons not classified | Dark matter |

**See also:** `STATUS_ALPHA.md`, `docs/DERIVATION_INDEX.md`

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
