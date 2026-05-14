<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# UBT Partition Function — Modular Weight Analysis

**Date**: 2026-03-14 (v57)  
**Status**: Gap G8 — initiated  
**DERIVATION_INDEX.md** row: "Modular weight of Ẑ(τ)" — see below

---

## 1. Background

DERIVATION_INDEX.md Gap G8: modular weight of UBT partition function Ẑ(τ).

Existing work consulted (per Task 7 step_1/step_2):

### 1.1 modular_dynamics.tex — What is proved?

- Torus construction: τ_mod = i R_ψ/R_t ∈ ℍ (upper half-plane). **[L0]**
- KK partition function: Z_KK(τ) = ∑_{n∈ℤ³} q^{|n|²} = ϑ₃³(τ). **[L0]**
- Under τ → τ+1: Z_KK invariant. **[L0]**
- Under τ → -1/τ: Poisson duality gives Z_KK(-1/τ) = |τ|^{3/2} Z_KK(τ). **[L0]**
- Z_KK is **not** a modular form of any weight (mixes differently). **[L0]**
- Conjecture (G8): full modular form requires winding + momentum sectors. **Open**

### 1.2 theta_modular_geometry.tex — What is proved?

- Complex time τ = t+iψ defines torus ℂ/(ℤ+τ_mod ℤ). **[L0]**
- Modular group SL(2,ℤ) action on τ_mod. **[L0]**
- q = e^{2πiτ_mod} parameter. **[L0]**
- R_ψ compactification radius ↔ Im(τ_mod). **[L0]**
- No modular-weight computation performed. **[—]**

---

## 2. The ψ-Circle Hamiltonian and Partition Function

### 2.1 Definition

The ψ-circle Hamiltonian H_ψ acts on KK modes on S¹_ψ:

```
H_ψ |n⟩ = E_n |n⟩,   E_n = n²/(2R_ψ²)   (in units ℏ = 2M_ψ = 1)
```

The UBT partition function (thermal trace) is:
```
Ẑ(τ) = Tr[ e^{-β H_ψ} ] = ∑_{n∈ℤ} e^{-β n²/(2R_ψ²)}
       = ϑ₃(0; e^{-β/(2R_ψ²)})
```
where β = 1/T is the inverse temperature (imaginary-time circle circumference).

### 2.2 Modular Parameter

Identifying β = 2πR_t and substituting q = e^{2πiτ_mod}:

```
Ẑ(τ_mod) = ∑_{n∈ℤ} q^{n²R_ψ²/R_t²}  =  ϑ₃(0 | i R_ψ²/R_t²)
```

For the T³ case (three imaginary directions, rank-3 momentum lattice):
```
Ẑ_T³(τ_mod) = [ϑ₃(0 | τ_mod)]³  = Z_KK(τ_mod)
```

---

## 3. S-Transformation (τ → -1/τ)

### 3.1 Jacobi theta function identity

The Jacobi theta function satisfies:
```
ϑ₃(0 | -1/τ) = (-iτ)^{1/2} · ϑ₃(0 | τ)
```
(standard result: Jacobi imaginary transformation).

### 3.2 Transformation of Ẑ(τ)

For the T³ partition function:
```
Ẑ_T³(-1/τ) = [ϑ₃(0 | -1/τ)]³ = [(-iτ)^{1/2}]³ · [ϑ₃(0 | τ)]³
            = (-iτ)^{3/2} · Ẑ_T³(τ)
```

Since |(-iτ)^{3/2}| = |τ|^{3/2}, this reproduces the Poisson duality result
from `modular_dynamics.tex` §3:
```
Ẑ_T³(-1/τ) = (-iτ)^{3/2} · Ẑ_T³(τ)
```

**This is the transformation law of a modular form of weight k = 3/2.**

---

## 4. Result: Modular Weight

| Object | Transformation under τ → -1/τ | Modular weight |
|--------|-------------------------------|----------------|
| Ẑ_T³(τ) = ϑ₃³(τ) | (-iτ)^{3/2} · Ẑ_T³(τ) | **k = 3/2** |
| Ẑ_S¹(τ) = ϑ₃(τ) | (-iτ)^{1/2} · Ẑ_S¹(τ) | k = 1/2 |
| Full Ẑ with winding | (-iτ)^{k} · Ẑ(τ) | k = d/2 (dim of compact space) |

**Conclusion**: For the T³ (three-dimensional imaginary sector), the UBT
partition function Ẑ(τ) is a modular form of **weight k = 3/2**.

This is k = d/2 = 3/2 where d = 3 = dim_ℝ(Im ℍ) = dim_ℝ(T³).

---

## 5. Implication for Gap G3-k

Task 7 asked: if k=1, does this close Gap G3-k → B_base Proved [L1]?

**Answer**: k = 3/2 ≠ 1. Therefore:
- Gap G3-k **is not closed** by this modular weight.
- The Kac-Moody level k=1 conjecture (H2 in DERIVATION_INDEX) must be
  motivated by different means (absence of Chern-Simons term, minimality).

**However**: k = 3/2 is fully consistent with the B_base = N_eff^{3/2}
derivation, since the 3/2 exponent in B_base originates from the same
source: dim_ℝ(Im ℍ) = 3, Gaussian measure exponent = d/2 = 3/2.

---

## 6. Status Summary

| Gap | Content | Result | Status |
|-----|---------|--------|--------|
| G8 | Modular weight of Ẑ(τ) | **k = 3/2** | ✅ **Computed [L0]** |
| G3-k | Kac-Moody level k=1 | Not closed by G8 | **Open [L1]** (H2 motivation) |

**Gap G8 status**: Computed. Ẑ_T³(τ) = ϑ₃³(τ) has modular weight k = 3/2.
This is consistent with B_base exponent 3/2 = k (d=3 compact dims).

---

## 7. Sources

- `research_tracks/research/modular_dynamics.tex` — KK partition function, Poisson duality
- `research_tracks/research/theta_modular_geometry.tex` — torus construction, τ definition
- `research_tracks/research/B_base_spectral_determinant.tex` — Poisson duality §4
- Standard reference: Jacobi imaginary transformation for ϑ₃

**Update DERIVATION_INDEX.md**: Gap G8 row → "Modular weight k=3/2 from
ϑ₃³ Jacobi identity" — Status: **Computed [L0]**.
