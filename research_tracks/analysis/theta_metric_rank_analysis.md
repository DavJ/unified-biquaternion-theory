# Theta → Metric Rank and Kernel Analysis

<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

## 1. Overview

This document formalises the component structure of the map

```
E : ℝ³² → ℝ¹⁰,   X ↦ g(X)
```

where `E_μ = ∂_μ Θ` is the biquaternionic tetrad derived from the UBT scalar
field `Θ ∈ 𝔹 = ℍ ⊗ ℂ`, and the classical (observable) metric is

```
g_{μν} = Re Tr(E_μ E_ν†)   (real projection of biquaternionic metric 𝒢_{μν})
```

The goal is to compute the rank of the Jacobian `J = ∂g/∂X`, determine the
kernel dimension, and separate gauge redundancies from potential new physical
degrees of freedom.

---

## 2. Real Component Basis

### 2.1 Biquaternion algebra

A biquaternion `q ∈ 𝔹 = ℍ ⊗ ℂ` can be written as

```
q = a₀ + a₁ i + a₂ j + a₃ k   (aₙ ∈ ℂ)
  = (r₀ + Is₀) + (r₁ + Is₁)i + (r₂ + Is₂)j + (r₃ + Is₃)k
```

where `I = √(−1)` is the *imaginary unit* (distinct from quaternion units
`i, j, k`), and `rₙ, sₙ ∈ ℝ` (eight real numbers per biquaternion).

### 2.2 Tetrad components

Each tetrad vector `E_μ ∈ 𝔹` carries eight real components:

```
E_μ = (e_μ¹, e_μ², e_μ³, e_μ⁴, e_μ⁵, e_μ⁶, e_μ⁷, e_μ⁸)
```

Explicit identification with the biquaternion basis:

| Index k | Component |
|---------|-----------|
| 1       | Re(a₀)    |
| 2       | Im(a₀)    |
| 3       | Re(a₁)    |
| 4       | Im(a₁)    |
| 5       | Re(a₂)    |
| 6       | Im(a₂)    |
| 7       | Re(a₃)    |
| 8       | Im(a₃)    |

### 2.3 Total real configuration vector

Stacking all four tetrad vectors gives the full configuration vector:

```
X = (e_0¹ … e_0⁸ | e_1¹ … e_1⁸ | e_2¹ … e_2⁸ | e_3¹ … e_3⁸)  ∈ ℝ³²
```

**Domain dimension: 32**

---

## 3. Metric Components as Functions of X

### 3.1 Biquaternion product formula

For two biquaternions `p, q ∈ 𝔹`:

```
Re Tr(p q†) = 2 Re(p · q̄)   (where ¯ denotes quaternion + complex conjugation)
```

Using the real-component notation for `E_μ = (r₀, s₀, r₁, s₁, r₂, s₂, r₃, s₃)`:

```
Re Tr(E_μ E_ν†) = 2 ( r₀^μ r₀^ν + s₀^μ s₀^ν
                     + r₁^μ r₁^ν + s₁^μ s₁^ν
                     + r₂^μ r₂^ν + s₂^μ s₂^ν
                     + r₃^μ r₃^ν + s₃^μ s₃^ν )
```

This is a **bilinear** form in the components of `E_μ` and `E_ν`.

### 3.2 Symmetric metric tensor (10 independent components)

```
g₀₀ = Re Tr(E₀ E₀†)   (μ=ν=0)
g₀₁ = Re Tr(E₀ E₁†)   (μ=0, ν=1)
g₀₂ = Re Tr(E₀ E₂†)
g₀₃ = Re Tr(E₀ E₃†)
g₁₁ = Re Tr(E₁ E₁†)
g₁₂ = Re Tr(E₁ E₂†)
g₁₃ = Re Tr(E₁ E₃†)
g₂₂ = Re Tr(E₂ E₂†)
g₂₃ = Re Tr(E₂ E₃†)
g₃₃ = Re Tr(E₃ E₃†)
```

**Codomain dimension: 10**

---

## 4. Jacobian Definition

The Jacobian of the map `g : ℝ³² → ℝ¹⁰` is the `10 × 32` matrix:

```
J_{(μν), k} = ∂g_{μν} / ∂X_k
```

Because each `g_{μν}` depends *only* on `E_μ` and `E_ν` (8 + 8 = 16
components when μ ≠ ν, or 8 components when μ = ν), the Jacobian is sparse:

- Diagonal block `g_{μμ}` depends only on the 8 components of `E_μ`.
- Off-diagonal `g_{μν}` (μ≠ν) depends on the 8 components of `E_μ` and the
  8 components of `E_ν` (16 columns each).

Explicit partial derivatives:

```
∂g_{μν} / ∂e_μ^k = 2 e_ν^k        (k-th component of E_ν)
∂g_{μν} / ∂e_ν^k = 2 e_μ^k        (k-th component of E_μ)
∂g_{μν} / ∂e_ρ^k = 0              (ρ ≠ μ, ν)
```

---

## 5. Rank and Kernel

### 5.1 Expected rank

For a *generic* (non-degenerate) configuration `X ∈ ℝ³²`:

- The 10 metric components are generically independent as functions of `X`.
- Therefore `rank(J) = 10` at a generic point.

**See `analysis/theta_metric_rank.py` for numerical verification.**

### 5.2 Kernel dimension

```
dim ker(J) = dim(domain) − rank(J) = 32 − 10 = 22
```

The 22-dimensional kernel consists of directions in `ℝ³²` along which `g_{μν}`
does not change to first order.

---

## 6. Kernel Decomposition

### 6.1 Local Lorentz / frame rotations (≈ 6 directions)

Lorentz transformations `Λ ∈ SO(1,3)` act on the tetrad as

```
E_μ → E_μ Λ^{-1}   (right action in the internal frame)
```

The metric is invariant: `g_{μν}[E Λ⁻¹] = g_{μν}[E]`.  
The Lie algebra `so(1,3)` is 6-dimensional, providing **6 pure gauge directions**.

### 6.2 Additional kernel directions (≈ 16 remaining)

The remaining `22 − 6 = 16` kernel directions correspond to variations of the
biquaternionic field that are *invisible to the real metric projection*. These
candidate sectors are:

| Sector                          | Dim. estimate | Metric effect | Physical interpretation       | Gauge or physical? |
|----------------------------------|---------------|---------------|-------------------------------|-------------------|
| Internal phase (imaginary part)  | ~4            | None          | Im(𝒢_{μν}) component         | Possibly physical  |
| Quaternionic internal rotations  | ~3            | None          | SU(2) inner frame rotation    | Gauge             |
| Antisymmetric / torsion-like     | ~6            | None on g_sym | Contorsion, torsion field     | Possibly physical  |
| Nonmetricity-like modes          | ~3            | None          | ∇g ≠ 0 directions            | Possibly physical  |

> **Note**: The precise decomposition is configuration-dependent and may
> change at special (e.g., flat or maximally symmetric) backgrounds. The
> estimates above correspond to a generic Lorentzian configuration.

---

## 7. Summary

| Quantity                     | Value |
|------------------------------|-------|
| Domain dimension (X)         | 32    |
| Codomain dimension (g)       | 10    |
| Generic rank of J            | 10    |
| Kernel dimension             | 22    |
| Gauge redundancies (Lorentz) | ≥ 6   |
| Remaining kernel             | ≤ 16  |

The analysis confirms:

1. The map `E_μ → g_{μν}` has maximal rank 10 at generic configurations.
2. At least 22 directions in the 32-dimensional biquaternionic tetrad space are
   *invisible* to the classical metric.
3. Of these, 6 correspond to local Lorentz frame redundancies (gauge).
4. The remaining ≤ 16 directions are candidates for new, non-metric fields.

See `reports/theta_dof_vs_gr.md` for the comparison with GR degrees of freedom.
