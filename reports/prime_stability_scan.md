<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# prime_stability_scan.md — Gamma Entropy Classification and Prime Stability Scan

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Track**: T3\_ALPHA — Fine Structure Constant Derivation  
**Status**: [Canonical] — Gamma entropy handling locked  
**Purpose**: Classify the role of Gamma-based entropy in the prime-stability
model, document the exclusion of the ∼400 cluster, and provide a complete
scan of the stable set under the canonical model.

---

## 1. Executive Summary

| Item | Verdict |
|------|---------|
| Canonical entropy form | **p log p** — fixed, must not be replaced |
| S_ren role | Renormalized Stirling interpolation of p log p — not a new model |
| Bare Gamma model | Excluded — produces a different (non-canonical) stable cluster |
| ∼400 cluster | Excluded — arises only from non-renormalized Gamma entropy |
| Stable set under canonical model | **S = {2, 127, 137, 139, 151, 157}** |

---

## 2. Canonical Entropy vs Gamma Variants

### 2.1 Canonical: p log p [Canonical]

The canonical entropy factor in the prime-stability potential is:

```
V(p) = p² - B(p)·p·log(p),    B(p) = (p+1)/3
```

This definition is **locked**. The term `p·log p` is the entropy contribution
and must not be modified or replaced.

**Physical basis**: `p·log p` arises from the 4D vacuum polarisation of `p`
winding quanta, each contributing a one-loop logarithm at scale µ = p.
See `canonical/alpha/nlogn_origin_analysis.tex` §3 for the derivation.

### 2.2 Renormalized Gamma: S_ren [Canonical] [Derived]

The renormalized Stirling interpolation is defined as:

```
S_ren(p) = logGamma(p+1) + p - 0.5·log(2·π·p)
```

By Stirling's formula:

```
logGamma(p+1) = log(p!) = p·log(p) - p + 0.5·log(2·π·p) + O(1/p)
```

Substituting:

```
S_ren(p) = [p·log(p) - p + 0.5·log(2·π·p)] + p - 0.5·log(2·π·p) + O(1/p)
         = p·log(p) + O(1/p)
```

**Key statement**: `S_ren` is a renormalized interpolation of `p·log p`,
not a new entropy model. Sub-leading Stirling corrections cancel, leaving
`p·log p` as the dominant term. The renormalization does not alter the
stability structure.

Using `S_ren` in place of `p·log p`:

```
V_ren(p) = p² - B(p)·S_ren(p)
```

produces **the same stable set** S = {2, 127, 137, 139, 151, 157} with
negligible numerical differences (|V(p) - V_ren(p)| < 0.05 for all p ∈ S).

### 2.3 Non-canonical Gamma Variant [Excluded] [NOT USED]

Direct substitution of `p·log p → logGamma(p+1)` **without** the Stirling
renormalization defines a **different model**:

```
V_Γ(p) = p² - B(p)·logGamma(p+1)           ← NON-CANONICAL
```

This model has a **different stability structure** centered near `p ≈ e⁶ ≈ 403`,
not near `p = 137`.

> **Warning**: Direct substitution `p·log p → logGamma(p+1)` defines a
> different model with stability centered near `p ≈ e⁶ ≈ 403`, and is NOT
> part of the canonical model.

---

## 3. Non-canonical Gamma Variant — Analysis [Excluded]

This section analyses the excluded `V_Γ` model for completeness.
All results below are **excluded from the canonical model**.

### 3.1 Why the minimum shifts to p ≈ 403

For the bare Gamma model:

```
V_Γ(p) = p² - B(p)·log(p!)
```

For large p, `log(p!) ≈ p·log(p) - p`, so:

```
V_Γ(p) ≈ p² - B(p)·(p·log(p) - p) = p² - B(p)·p·log(p) + B(p)·p
```

The extra `+B(p)·p = p(p+1)/3` term adds a positive quadratic correction
that shifts the balance point. The minimum of `V_Γ` occurs approximately where:

```
dV_Γ/dp ≈ 0  →  log(p) ≈ 6  →  p ≈ e⁶ ≈ 403
```

This is why the bare Gamma model has a stable cluster near `p ≈ 400`.

### 3.2 Non-canonical Gamma Scan (excluded region)

The following is a **non-canonical Gamma scan** provided for completeness
only. These results do **not** belong to the canonical model.

| p | V_Γ(p) | Note |
|---|--------|------|
| 389 | −100,194 | Still decreasing |
| 397 | −105,407 | Still decreasing |
| 401 | −108,069 | Near minimum |
| 409 | −113,506 | Past minimum |
| 421 | −121,941 | Past minimum |

**Status**: [NOT USED] — excluded from canonical derivations.

---

## 4. The ∼400 Cluster: Exclusion Statement

```
The cluster near p ≈ 400 arises only from the non-renormalized Gamma
entropy V_Γ(p) = p² - B(p)·logGamma(p+1) and is EXCLUDED from the
canonical prime-stability model.

No prime near p = 400 belongs to the canonical stable set S = {2, 127,
137, 139, 151, 157}. Any such claim in a canonical document is incorrect
and must be corrected or removed.
```

---

## 5. Canonical Stable Set Scan [Canonical] [Numerical]

The following table gives the full canonical scan for primes up to 10,000.
Stability is determined by the self-consistency criterion of
`canonical/alpha/prime_stability_set.tex` Definition 2.1.

### 5.1 Summary

| Prime p | B(p) | n_c(B(p)) | ℓ(p) | u(p) | Margin | V(p) | V_ren(p) |
|---------|------|-----------|------|------|--------|------|----------|
| 2   | 1.000 | (special) | —     | —     | —      | +2.614  | +2.572  |
| 127 | 42.667 | 124.200  | 120.0 | 129.0 | 4.201  | −10,120.04 | −10,120.06 |
| 137 | 46.000 | 135.989  | 134.0 | 138.0 | 1.989  | −12,236.72 | −12,236.75 |
| 139 | 46.667 | 138.364  | 138.0 | 144.0 | 0.364  | −12,687.29 | −12,687.32 |
| 151 | 50.667 | 152.726  | 150.0 | 154.0 | 1.274  | −15,584.54 | −15,584.56 |
| **157** | **52.667** | **159.976** | **154.0** | **160.0** | **0.024** | **−17,159.41** | **−17,159.44** |

### 5.2 Numerical Consistency

Both `V(p)` and `V_ren(p)` produce **identical stable set** S = {2, 127, 137, 139, 151, 157}.

The differences `|V(p) - V_ren(p)|` are at most ~0.028 for the large primes,
consistent with the O(1/p) Stirling corrections. These differences are too
small to change the stability criterion for any prime.

**Agreement between V and V_ren confirms that Gamma interpolation does not
alter the stability structure.**

### 5.3 Smallest-Margin Prime

`p = 157` has stability margin **0.024** — the smallest in S. Its continuous
minimum `n_c(B(157)) ≈ 159.976` lies only 0.024 below the upper stability
boundary `u(157) = (157 + 163)/2 = 160.0`. This means 157 is marginally
stable: a perturbation of order 0.024 in `n_c` would push 157 outside the
stable set.

---

## 6. References

| File | Role |
|------|------|
| `canonical/alpha/prime_stability_set.tex` | Canonical model definition (locked) |
| `canonical/alpha/prime_selection_principle.tex` | Physical derivation of PSP |
| `canonical/alpha/nlogn_origin_analysis.tex` | Origin of n log n term |
| `reports/prime_stability_revalidation.md` | Full numerical revalidation |
| `reports/gaussian_lambda_scan.md` | Gaussian extension λ-experiment |
