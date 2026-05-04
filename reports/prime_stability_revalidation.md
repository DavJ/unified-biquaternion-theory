<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# prime_stability_revalidation.md — Numerical Revalidation of the Canonical Stable Set

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Track**: T3\_ALPHA — Fine Structure Constant Derivation  
**Status**: [Numerical] — Revalidation of canonical stable set  
**Purpose**: Independently compute the canonical stable set using both V(p) and
V_ren(p) for primes up to 10,000, verify agreement, provide full margin table,
and highlight the smallest-margin prime.

---

## 1. Models Compared

### Model V — Canonical

```
V(p) = p² - B(p)·p·log(p)
B(p) = (p+1)/3
```

### Model V_ren — Renormalized Gamma Interpolation

```
V_ren(p) = p² - B(p)·S_ren(p)
S_ren(p) = logGamma(p+1) + p - 0.5·log(2·π·p)
B(p) = (p+1)/3
```

`S_ren(p) = p·log(p) + O(1/p)` by Stirling's formula (see
`reports/prime_stability_scan.md §2.2`).

---

## 2. Stability Criterion

For each prime p ≥ 3:
1. Solve `2·n_c = B(p)·(log(n_c) + 1)` numerically for n_c (the continuous
   minimum of V(n, B(p)) over real n > 0).
2. Compute stability boundaries:
   - `ℓ(p) = (prev_prime(p) + p) / 2`
   - `u(p) = (p + next_prime(p)) / 2`
3. Prime p is **stable** if `ℓ(p) < n_c(B(p)) < u(p)`.
4. Stability margin: `margin(p) = min(n_c - ℓ(p), u(p) - n_c)`.

For p = 2: included as a base case (V(2) > 0; the continuous minimum n_c
does not exist for B(2) = 1, so p = 2 is treated as a special prime).

Since n_c depends only on B(p) = (p+1)/3, and both V and V_ren use the same
B(p), the stability criterion is identical for both models.

---

## 3. Full Revalidation Table [Numerical]

Primes scanned: 2 through 9,973 (all 1,229 primes ≤ 10,000).

| p | B(p) | n_c | ℓ(p) | u(p) | margin | V(p) | V_ren(p) | V − V_ren |
|---|------|-----|------|------|--------|------|----------|-----------|
| 2 | 1.0000 | (special) | — | — | — | +2.6137 | +2.5724 | +0.0413 |
| 127 | 42.6667 | 124.200 | 120.0 | 129.0 | 4.200 | −10,120.04 | −10,120.06 | +0.0280 |
| 137 | 46.0000 | 135.989 | 134.0 | 138.0 | 1.989 | −12,236.72 | −12,236.75 | +0.0280 |
| 139 | 46.6667 | 138.364 | 138.0 | 144.0 | 0.364 | −12,687.29 | −12,687.32 | +0.0280 |
| 151 | 50.6667 | 152.726 | 150.0 | 154.0 | 1.274 | −15,584.54 | −15,584.56 | +0.0280 |
| **157** | **52.6667** | **159.976** | **154.0** | **160.0** | **0.024** | **−17,159.41** | **−17,159.44** | **+0.0280** |

**Both V and V_ren produce the same stable set: S = {2, 127, 137, 139, 151, 157}.**

---

## 4. Neighboring Primes (Context — Excluded from S)

| p | B(p) | n_c | ℓ(p) | u(p) | In gap? | V(p) |
|---|------|-----|------|------|---------|------|
| 113 | 38.000 | 107.952 | 109.0 | 120.0 | No (n_c < ℓ) | −7,530.40 |
| 127 | 42.667 | 124.200 | 120.0 | 129.0 | **Yes** | −10,120.04 |
| 131 | 44.000 | 128.899 | 129.0 | 137.0 | No (n_c < ℓ by 0.101) | −10,939.64 |
| 137 | 46.000 | 135.989 | 134.0 | 138.0 | **Yes** | −12,236.72 |
| 139 | 46.667 | 138.364 | 138.0 | 144.0 | **Yes** | −12,687.29 |
| 149 | 50.000 | 150.319 | 144.0 | 150.0 | No (n_c > u by 0.319) | −15,078.40 |
| 151 | 50.667 | 152.726 | 150.0 | 154.0 | **Yes** | −15,584.54 |
| 157 | 52.667 | 159.976 | 154.0 | 160.0 | **Yes** | −17,159.41 |
| 163 | 54.667 | 167.269 | 160.0 | 165.0 | No (n_c > u by 2.269) | −18,819.71 |
| 167 | 56.000 | 172.155 | 165.0 | 170.0 | No (n_c > u by 2.155) | −19,974.48 |

Key excluded primes and why:
- **p = 131**: n_c = 128.899 < ℓ(131) = 129.0 (barely misses by 0.101)
- **p = 149**: n_c = 150.319 > u(149) = 150.0 (exceeds boundary by 0.319)
- **p = 163**: n_c = 167.269, far outside u(163) = 165.0

---

## 5. Consistency Verification [Numerical]

### 5.1 V and V_ren agree on the stable set

The difference V(p) − V_ren(p) for primes in S:

| p | V(p) − V_ren(p) | Relative difference |
|---|----------------|---------------------|
| 2 | +0.041 | 1.6% |
| 127 | +0.028 | 0.00028% |
| 137 | +0.028 | 0.00023% |
| 139 | +0.028 | 0.00022% |
| 151 | +0.028 | 0.00018% |
| 157 | +0.028 | 0.00016% |

For p ≥ 127, differences are at the level of 0.028 ≈ constant, consistent with
the O(1/p) Stirling correction. The stability boundaries ℓ(p) and u(p) are
determined by B(p) alone (same in both models), so the criterion is unaffected.

### 5.2 Agreement statement

**Agreement between V and V_ren confirms that Gamma interpolation does not
alter the stability structure.** The sub-leading Stirling corrections
(O(1/p) ≈ 10⁻³ for p ≈ 100) are far too small to displace any prime from
the stable set.

---

## 6. Smallest-Margin Prime: p = 157

The stability margin is smallest for **p = 157** (margin = 0.024):

```
n_c(B(157)) = 159.976
u(157) = (157 + 163)/2 = 160.0

margin(157) = u(157) - n_c = 160.0 - 159.976 = 0.024
```

This means: if B(157) were to increase by δB such that n_c(B + δB) > 160,
then 157 would no longer be self-consistent and would exit the stable set.
The sensitivity dB/dn_c at p = 157 can be estimated from the defining
equation 2n = B(log n + 1):

```
dB/dn = 2 / (log n + 1)  →  at n=160: dB/dn ≈ 2/6.08 ≈ 0.33
→ δn_c = 0.024 ↔ δB ≈ 0.008
```

A shift of δB ≈ 0.008 in B(157) would push 157 out of S. This corresponds to
a shift of δp ≈ 3δB ≈ 0.024 in the prime label, i.e., an extremely small
perturbation.

---

## 7. No Stable Primes Found Outside S (up to 10,000)

The scan of all 1,229 primes up to 10,000 found no additional stable primes
other than those in S = {2, 127, 137, 139, 151, 157}.

A boundary artefact appears at p = 99,991 when scanning to 100,000; this is
due to the finite prime list used in the nearest-prime lookup and is not a
genuine stable prime.

---

## 8. References

| File | Role |
|------|------|
| `canonical/alpha/prime_stability_set.tex` | Canonical definition (locked) |
| `reports/prime_stability_scan.md` | Gamma classification |
| `canonical/alpha/nlogn_origin_analysis.tex` | Derivation of p log p form |
| `canonical/alpha/prime_selection_principle.tex` | Physical PSP derivation |
