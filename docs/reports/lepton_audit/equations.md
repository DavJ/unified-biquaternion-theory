# Lepton Ratios — Extracted Equations

Source: `consolidation_project/appendix_W2_lepton_spectrum.tex`

---

## (a) Mode Index Definition

Eigenfunctions of the internal Dirac operator on T²(τ) are labelled by integers
`(n, m) ∈ ℤ²`.

The Wilson-line (Hosotani) background induces shifts `(δ, δ')`:

- `n`-shift: `δ = ½`  (from `Q = −1`, `θ_H = π`, along the ψ-cycle)
- `m`-shift: `δ' = 0`  (spin structure; value stated implicitly via table in W.T)

---

## (b) Eigenmode Energy Formula

```
E_{n,m} = (1/R) √[ (n + δ)² + (m + δ')² ]
```

Parameters:
- `R` — torus compactification radius (single calibration, sets overall energy scale)
- `δ = ½`, `δ' = 0` — Hosotani / spin-structure shifts

**Note**: This formula is stated WITHOUT explicit dependence on the torus modulus `τ_*`.
Appendix W.5 says "For the modulus τ = τ_* determined in Appendix V we evaluate the
ratios," but the formula and table in W.2–W.T do not include `τ_*` as a parameter.

---

## (c) Energy-to-Mass Mapping  M(E)

Appendix W uses a **linear** (trivial) mapping:

```
m_lepton = E_{n,m}
```

i.e. the lepton rest mass is identified directly with the Dirac eigenvalue (in natural units,
`ħ = c = 1`). No nonlinear transformation is applied.  
The single calibration is `m_e ≡ E_{0,1}`, which fixes `R`:

```
R = 1 / m_e   (in natural units)
```

---

## (d) Scale Parameters

| Symbol | Meaning | Appears in |
|--------|---------|------------|
| `R`    | Torus compactification radius | W.2, W.3; calibrated by `m_e` |
| `τ_*` = `iy_*` | Torus modular parameter (shape) | referenced in W.5, derived in Appendix V |
| `Λ`   | UV / compactification scale `≡ 1/R` | Appendix K.5, Appendix V |
| `μ₀ ~ M_Z` | RG matching scale | Appendix V.3 |
| `y_*` | Imaginary part of `τ_*`; `α⁻¹ = 4πN/y_*` with `N=10` | Appendix V |

**Critical gap**: The eigenvalue formula in Appendix W does not include `y_*` or `τ_*`.
If the correct formula on a torus with modulus `τ = iy_*` is

```
E_{n,m} = (1/R) √[ (n + δ)² + (m + δ')² y_*² ]     (rectangular-torus formula)
```

or

```
E_{n,m} = (1/R) | (n + δ) + (m + δ') τ_* |          (general complex-modulus formula)
```

then `y_*` would enter and could, in principle, change the ratios.  
However, as shown in `missing_step.md`, even this generalisation does NOT reproduce 207.3
for any real `y_*`.

---

## Numerical Values from Formula (δ = ½, δ' = 0)

| Mode (n,m) | `E_{n,m} · R` | `E_{n,m} / E_{0,1}` | Claim (W.5) |
|------------|---------------|----------------------|-------------|
| (0,1)      | 1.11803        | 1.000                | 1.000 (ref) |
| (0,2)      | 2.06155        | **1.844**            | **207.3** ❌ |
| (1,0)      | 1.50000        | **1.342**            | **3477** ❌  |
| (1,1)      | 1.80278        | **1.612**            | —           |

The formula and the claimed ratios are **mutually inconsistent**.
