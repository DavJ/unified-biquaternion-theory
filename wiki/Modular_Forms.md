<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Modular Forms in UBT

Modular forms and Hecke operators provide the mathematical bridge between the
abstract biquaternion structure and the physical lepton mass spectrum.

---

## Role in UBT

The connection between UBT and modular forms operates at two levels:

1. **Hecke eigenvalues at prime p** encode lepton mass ratios
2. **Modular weight k = 6** is selected by the spin structure of the theory

The physical prime p = 137 is the unique Hecke prime in [50, 300] whose
eigenvalue coefficients reproduce the (e, μ, τ) mass ratios with < 0.1% error.

---

## Modular Forms — Basics

A modular form of weight k for the congruence subgroup Γ₀(N) is a holomorphic
function f : ℍ → ℂ satisfying:

```
f((aτ+b)/(cτ+d)) = (cτ+d)^k · f(τ)   for  (a b; c d) ∈ Γ₀(N)
```

with appropriate growth conditions.

The Fourier expansion is:

```
f(τ) = Σ_{n≥0}  a_n · q^n,   q = e^{2πiτ}
```

The coefficients a_n carry arithmetic information; for eigenforms, a_p gives
the Hecke eigenvalue at prime p.

---

## Hecke Operators

The Hecke operator T_p acts on modular forms of weight k:

```
(T_p f)(τ) = p^{k-1} f(pτ) + p^{-1} Σ_{j=0}^{p-1} f((τ+j)/p)
```

A **Hecke eigenform** f satisfies T_p f = a_p · f for all primes p.
The eigenvalue a_p = a(p) is the p-th Fourier coefficient.

---

## Connection to Lepton Masses

In UBT, lepton masses are proposed to be related to Hecke eigenvalues at prime p:

```
m_e : m_μ : m_τ  =  |a_1(p)| : |a_2(p)| : |a_3(p)|
```

where a_1, a_2, a_3 are the first three non-trivial Fourier coefficients of the
weight-6 Hecke eigenform at prime p.

**Key result**: Scanning all primes in [50, 300], only p = 137 gives a match
to the physical lepton mass ratios (μ error 0.02%, τ error 0.10%).

→ Details: [Hecke / Modular Structure](Hecke_Modular_Structure)

---

## Status and Open Problems

| Claim | Status |
|-------|--------|
| Weight k = 6 selection | **Conjecture** |
| CM forms at any level | **Dead End** — |a_137| ≫ target value |
| Non-CM forms, N ≤ 4 | **Dead End** — no such forms exist |
| Non-CM forms, N ∈ [50, 500] | **Extended Dead End (partial search)** |
| p = 137 as unique Hecke prime | **Strong Numerical Support** |

---

## Canonical Files

| File | Content |
|------|---------|
| [`docs/reports/hecke_lepton/`](https://github.com/DavJ/unified-biquaternion-theory/tree/main/docs/reports/hecke_lepton) | Full Hecke numerical results |
| [`step5_hecke_search_results.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/experiments/research_tracks/three_generations/step5_hecke_search_results.tex) | Search results |
| [`step6_nonCM_search.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/experiments/research_tracks/three_generations/step6_nonCM_search.tex) | Non-CM search |

---

## See Also

- [Hecke / Modular Structure](Hecke_Modular_Structure) — derivation page
- [Mirror Sector](Mirror_Sector) — Set B at p = 139
- [Particle Spectrum](Particle_Spectrum) — lepton masses
