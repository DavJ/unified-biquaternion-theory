<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# gaussian_lambda_scan.md — Gaussian Prime Extension: λ-Experiment

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Track**: T3\_ALPHA / Research Track  
**Status**: [Research] — Exploratory; canonical model unaffected  
**Purpose**: Test the effect of a Gaussian norm correction parameter λ on
the prime-stability structure. Verify that the canonical stable set S is
preserved at λ=0 and characterise the λ-dependence for split vs inert primes.

---

## 1. Motivation and Setup

The canonical potential V(p) = p² − B(p)·p·log(p) treats all primes uniformly.
A Gaussian extension distinguishes split primes (p ≡ 1 mod 4, which factor in
ℤ[i]) from inert primes (p ≡ 3 mod 4, which remain prime in ℤ[i]).

The λ-experiment tests the following parametrized generalization:

```
V_G(p, λ) = p² − B(p)·p·(log(p) + χ(p)·λ)
```

where:

```
χ(p) = 1    if p ≡ 1 mod 4  (split prime)
χ(p) = 0    if p ≡ 3 mod 4  (inert prime)
χ(2) = 0.5  (ramified, partial correction)
```

**At λ = 0**: `V_G(p, 0) = V(p)` — the canonical model is exactly recovered.  
**For λ ≠ 0**: split primes receive a modified log factor; inert primes are
unchanged.

This parameterization is physically motivated: for split primes, the
Gaussian norm structure introduces an additional angular degree of freedom
(arg(π) for the Gaussian prime π above p), which can contribute an additive
correction to the entropy factor. The parameter λ measures the coupling to
this additional degree of freedom.

---

## 2. Constraint: λ Must Not Be Tuned to Force Specific Primes

> **Forbidden**: tuning λ to force specific primes into or out of the
> stable set. The parameter λ is an exploration parameter; no value of
> λ is special unless it can be derived from UBT first principles.

The λ-scan is exploratory. Its purpose is to determine whether the stable
set is robust under small Gaussian corrections (λ ≈ 0) and whether any
λ-value produces a structurally interesting result.

---

## 3. λ = 0 Baseline Verification [Numerical]

At λ = 0, `V_G(p, 0) = V(p)` exactly (all χ(p)·λ terms vanish). The
canonical stable set S = {2, 127, 137, 139, 151, 157} is reproduced.

| p | V_G(p, 0) | V(p) | Match? |
|---|-----------|------|--------|
| 127 | −10,120.04 | −10,120.04 | ✓ |
| 137 | −12,236.72 | −12,236.72 | ✓ |
| 139 | −12,687.29 | −12,687.29 | ✓ |
| 151 | −15,584.54 | −15,584.54 | ✓ |
| 157 | −17,159.41 | −17,159.41 | ✓ |

**The λ = 0 baseline matches the canonical model exactly. ✓**

---

## 4. λ-Scan: V_G(p, λ) for Context Primes [Numerical]

The following table gives V_G for primes near the stable set, across the
full scan range λ ∈ [−1, 1]:

| p | type | V_G(λ=−1) | V_G(λ=−0.5) | V_G(λ=0) | V_G(λ=0.5) | V_G(λ=1) |
|---|------|-----------|------------|----------|-----------|---------|
| 127 | inert | −10,120.04 | −10,120.04 | −10,120.04 | −10,120.04 | −10,120.04 |
| 131 | inert | −10,939.64 | −10,939.64 | −10,939.64 | −10,939.64 | −10,939.64 |
| 137 | split | −5,934.72 | −9,085.72 | −12,236.72 | −15,387.72 | −18,538.72 |
| 139 | inert | −12,687.29 | −12,687.29 | −12,687.29 | −12,687.29 | −12,687.29 |
| 149 | split | −7,628.40 | −11,353.40 | −15,078.40 | −18,803.40 | −22,528.40 |
| 151 | inert | −15,584.54 | −15,584.54 | −15,584.54 | −15,584.54 | −15,584.54 |
| 157 | split | −8,890.74 | −13,025.08 | −17,159.41 | −21,293.74 | −25,428.08 |
| 163 | inert | −18,819.71 | −18,819.71 | −18,819.71 | −18,819.71 | −18,819.71 |

**Key observation**: inert primes (127, 131, 139, 151, 163) are completely
unaffected by λ (since χ(p) = 0 for p ≡ 3 mod 4). Split primes (137, 149,
157) receive a correction proportional to −B(p)·p·λ.

---

## 5. Stability Set vs λ [Numerical]

Since the stability criterion (Definition 2.1 in `prime_stability_set.tex`)
depends only on n_c(B(p)) and the prime gaps, and since B(p) = (p+1)/3 is
independent of λ, the **stability criterion itself is λ-independent**.

The stable set S = {2, 127, 137, 139, 151, 157} is the same for **all λ**.

However, the V_G values change with λ, which affects the relative ordering
of V_G among primes:

| λ | Prime with lowest V_G in {127,...,157} |
|---|--------------------------------------|
| −1.00 | 151 (V_G = −15,584.54) — split primes pushed up |
| −0.50 | 151 (V_G = −15,584.54) |
| −0.25 | 151 (V_G = −15,584.54) |
|  0.00 | 157 (V_G = −17,159.41) — canonical baseline |
| +0.25 | 157 (V_G = −19,226.58) |
| +0.50 | 157 (V_G = −21,293.74) |
| +1.00 | 157 (V_G = −25,428.08) — split primes pushed down |

The canonical prime 137 is not the global V-minimum even at λ = 0 (157 is
lower), consistent with the fact that 157 is also stable and has a lower V
value. The relevance of 137 comes from the stability structure (B(137) = 46
is an integer; n_c(46) ≈ 136 is closest to 137), not from being the absolute
V-minimum.

---

## 6. Interpretation [Research]

### 6.1 λ > 0 (Positive Gaussian coupling)

For λ > 0, split primes receive a larger entropy contribution (the log factor
increases). This pushes split primes to lower V values (more negative),
strengthening their binding in the winding potential. The inert primes remain
unaffected.

### 6.2 λ < 0 (Negative Gaussian coupling)

For λ < 0, split primes receive a reduced entropy factor. At λ = −1, the
canonical log(p) is replaced by log(p) − χ(p), which is significantly smaller
for split primes (log(137) − 1 ≈ 3.92 vs log(137) ≈ 4.92). The inert primes
151, 163, 139 become the most stable.

### 6.3 No Special λ Value Identified

No value of λ in [−1, 1] produces a qualitatively new structure (new stable
prime, crossing of stability boundaries, etc.). The stable set is always
{2, 127, 137, 139, 151, 157}. The λ-experiment is **consistent** with the
canonical model being the correct λ = 0 baseline.

---

## 7. Conclusion [Research]

1. **λ = 0 exactly reproduces the canonical model.** ✓
2. **No λ-value forces 137 to be the unique prime minimum** — this is expected
   and correct (the Gaussian correction should not be tuned to reproduce the
   desired prime).
3. **The stable set S is λ-independent** (the stability criterion depends on
   B(p), not on V_G values directly).
4. **Inert primes are completely λ-independent**, consistent with the two-sector
   classification in `research_tracks/gaussian_prime_stability/gaussian_prime_stability.md`.
5. **No first-principles derivation of λ exists.** Until λ can be derived from
   S[Θ], the Gaussian extension remains [Research].

---

## 8. References

| File | Role |
|------|------|
| `canonical/alpha/prime_stability_set.tex` | Canonical model (λ=0 baseline) |
| `research_tracks/gaussian_prime_stability/gaussian_prime_stability.md` | Two-sector classification |
| `reports/prime_stability_revalidation.md` | 1D revalidation (λ=0 confirmed) |
| `canonical/alpha/prime_selection_principle.tex` | Physical basis of prime selection |
