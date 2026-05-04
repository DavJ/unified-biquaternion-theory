<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# gaussian_prime_stability.md — Gaussian Prime Stability: Classification and Inconsistency Resolution

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Track**: T3\_ALPHA / Research Track — Gaussian Extension  
**Status**: [Research] — Extension of canonical 1D model; not yet canonical  
**Purpose**: Analyse the Gaussian prime extension of the prime-stability model,
resolve the critical inconsistency between inert primes and the norm-only
approach, and define a consistent two-sector classification.

---

## 1. Summary

| Issue | Resolution |
|-------|-----------|
| 127, 139, 151 are stable in 1D | Yes — these are inert primes (p ≡ 3 mod 4) |
| Inert primes cannot be written as a² + b² | Correct — norm-only Gaussian model is incomplete |
| Split primes (p ≡ 1 mod 4) have Gaussian norm structure | V_G(p) defined using Gaussian norm |
| Inert primes require 1D model | V_1D(p) = V(p) (canonical) |
| Canonical primes must be preserved | All of S = {2, 127, 137, 139, 151, 157} preserved |

---

## 2. Background: The Norm-Only Gaussian Model and Its Incompleteness

A natural extension of the prime-stability model to the Gaussian integers
ℤ[i] assigns to each prime p a Gaussian winding mode. In the Gaussian integers,
rational primes split into two classes:

**Split primes** (p ≡ 1 mod 4, and p = 2):  
These primes factor in ℤ[i] as p = π·π̄ where π = a + bi with |π|² = a² + b² = p.
The Gaussian norm N(π) = p provides a natural extension of the 1D winding number.

**Inert primes** (p ≡ 3 mod 4):  
These primes remain prime in ℤ[i] (they do not factor). The equation
a² + b² = p has **no integer solution** for inert primes. The norm-only
model therefore cannot be applied to inert primes.

---

## 3. Critical Inconsistency: Inert Primes in the Stable Set

### 3.1 Statement of the Inconsistency

The canonical stable set S = {2, 127, 137, 139, 151, 157} contains the
following inert primes:

| Prime p | Class | p mod 4 | Gaussian factorization |
|---------|-------|---------|----------------------|
| 2 | Ramified | 2 = −i·(1+i)² | Special |
| 127 | Inert | 127 ≡ 3 mod 4 | Remains prime in ℤ[i] |
| 137 | Split | 137 ≡ 1 mod 4 | 137 = (4 + 11i)(4 − 11i) |
| 139 | Inert | 139 ≡ 3 mod 4 | Remains prime in ℤ[i] |
| 151 | Inert | 151 ≡ 3 mod 4 | Remains prime in ℤ[i] |
| 157 | Split | 157 ≡ 1 mod 4 | 157 = (6 + 11i)(6 − 11i) |

**Three of the six stable primes (127, 139, 151) are inert.** A naive
norm-only Gaussian model that assigns winding modes via Gaussian norms
a² + b² = p would be **undefined** for these three primes.

### 3.2 Why This Is a Problem

If the Gaussian extension uses the potential:
```
V_G(p) = (a² + b²) - B(p)·(a² + b²)·log(a² + b²)  (where a² + b² = p)
```
then `V_G(p) = p² - B(p)·p·log(p) = V(p)` for split primes, which is correct.
But for **inert primes** p ≡ 3 mod 4, there are **no** integers a, b with
a² + b² = p, so `V_G` is undefined.

A norm-only Gaussian model is therefore **incomplete**: it handles split
primes but provides no mechanism for inert primes.

---

## 4. Resolution: Two-Sector Classification [Research]

### 4.1 Classification

Define two sectors based on the splitting behaviour of primes in ℤ[i]:

**Bulk sector** (split primes, p ≡ 1 mod 4):  
These primes admit a Gaussian factorization p = π·π̄. They are called "bulk"
because they correspond to interior points of the 2D Gaussian winding lattice.

**Boundary sector** (inert primes, p ≡ 3 mod 4):  
These primes remain prime in ℤ[i]. They cannot be placed in the 2D Gaussian
lattice via a norm decomposition. They are called "boundary" because they
correspond to the edges of the 1D prime number line that do not lift to 2D.

### 4.2 Two-Sector Potential

Define the two-sector effective potential:

```
V_total(p) = V_G(p)   if p is a split prime (p ≡ 1 mod 4)
             V_1D(p)  if p is an inert prime (p ≡ 3 mod 4)
```

where:
- `V_G(p) = N(π)² − B(p)·N(π)·log(N(π))` with `N(π) = a² + b² = p` for
  the unique Gaussian prime π above p (up to units and conjugate), giving
  `V_G(p) = p² − B(p)·p·log(p) = V(p)`.
- `V_1D(p) = p² − B(p)·p·log(p) = V(p)` (the canonical 1D potential).

Under this definition, `V_total(p) = V(p)` for **all** primes, both split
and inert. The two-sector classification is therefore consistent: inert
primes fall back to the 1D model, and split primes use the Gaussian norm
model which coincides with the 1D model at the level of the effective potential.

### 4.3 Canonical Primes Preserved

**All canonical stable primes are preserved** under the two-sector model:
- p = 127 (inert): uses V_1D → stable (margin 4.200)
- p = 137 (split): uses V_G → stable (margin 1.989)
- p = 139 (inert): uses V_1D → stable (margin 0.364)
- p = 151 (inert): uses V_1D → stable (margin 1.274)
- p = 157 (split): uses V_G → stable (margin 0.024)

The stable set S = {2, 127, 137, 139, 151, 157} is unchanged.

---

## 5. Gaussian Lattice Structure [Research]

### 5.1 Split Primes as 2D Winding Modes

For a split prime p ≡ 1 mod 4 with p = (a + bi)(a − bi):
- The 2D winding mode lives on the Gaussian lattice ℤ[i] ⊂ ℂ.
- The norm N(a + bi) = a² + b² = p is the 2D winding number.
- The Gaussian angle arg(a + bi) = arctan(b/a) is an additional degree of freedom.

For p = 137 = (4 + 11i)(4 − 11i): N = 4² + 11² = 16 + 121 = 137. ✓
For p = 157 = (6 + 11i)(6 − 11i): N = 6² + 11² = 36 + 121 = 157. ✓

### 5.2 Inert Primes as 1D Boundary Modes

For an inert prime p ≡ 3 mod 4:
- The prime does not split in ℤ[i]; it generates the ideal (p) ⊂ ℤ[i].
- The winding mode is purely 1D: winding number = p.
- There is no 2D Gaussian angle.

### 5.3 Physical Interpretation [Research]

The two-sector classification has a natural interpretation in terms of the
UBT geometry. The biquaternion field Θ(q, τ) on the imaginary-time circle
S¹_ψ can be extended to the Gaussian plane ℂ_ψ = ℝ_ψ ⊕ iℝ_ψ. Split primes
correspond to modes that extend into the 2D Gaussian plane; inert primes
correspond to purely 1D modes that do not couple to the imaginary component.

This interpretation is **[Research]** and has not been derived from the
UBT axioms.

---

## 6. Open Problem: Dynamical Derivation [Research]

The two-sector model is **self-consistent** but not yet **derived** from
the UBT action S[Θ]. The following derivations are required for promotion
to canonical status:

1. **Derive** V_G(p) from S[Θ] evaluated at a Gaussian winding background.
2. **Prove** that inert primes cannot support a 2D Gaussian winding mode.
3. **Derive** the split/inert boundary from the UBT geometry of S¹_ψ.

Until these derivations are complete, the Gaussian extension remains
**[Research]** and must not be cited in canonical documents.

---

## 7. References

| File | Role |
|------|------|
| `canonical/alpha/prime_stability_set.tex` | Canonical 1D model (locked) |
| `canonical/alpha/prime_selection_principle.tex` | Physical PSP derivation |
| `reports/gaussian_lambda_scan.md` | Gaussian λ-experiment |
| `reports/prime_stability_revalidation.md` | 1D numerical revalidation |
