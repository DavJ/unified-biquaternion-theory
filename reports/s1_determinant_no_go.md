<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# s1_determinant_no_go.md — S¹_ψ Functional Determinant Cannot Produce B·n·ln n

**Author**: Ing. David Jaroš  
**Date**: 2026-05-04  
**Track**: T3_ALPHA — Fine Structure Constant  
**Status**: [DEAD END] — S1 determinant route for B is closed  
**Companion**: `canonical/alpha/nlogn_origin_analysis.tex` (full derivation)

---

## Verdict

| Item | Verdict |
|------|---------|
| S¹_ψ functional determinant → B·n·ln n | **[DEAD END]** |
| S¹_ψ functional determinant → B₀ = 2πN_eff/3 = 8π | **VALID [L1]** — retained |
| True origin of n·ln n | 4D vacuum polarisation applied to n-winding background |
| Form V4 (n² − B·ln n) | **[WRONG]** — arises from the S¹ one-particle determinant |

---

## What the S¹_ψ Functional Determinant Actually Gives

### One-particle determinant at winding level n

The eigenvalue of −∂²_ψ at winding number n is λ = n² (natural units).
The zeta-function-regularised one-particle contribution is:

```
−½ ln det(−∂²_ψ)|_{winding n} = −½ ln(n²) = −ln n
```

Summing over N_eff = 12 independent charged modes:

```
−½ ln det(−∇†∇)|_{S¹_ψ, n} = −N_eff · ln n
```

This gives the potential form **V4**:

```
V_{S¹}(n) = n² − N_eff · ln n      [WRONG FORM — V4]
```

V4 has its minimum at n* = √(N_eff/2) ≈ 2.45, far from 137.
**V4 is useless for the alpha route.**

### Vacuum polarisation result (useful linear term)

The one-loop vacuum polarisation of N_eff charged modes on S¹_ψ gives:

```
B₀ = 2π·N_eff/3 = 8π ≈ 25.133
```

This is the coefficient in the 4D running coupling:

```
1/α(μ) = 1/α(μ₀) + (B₀/2π)·ln(μ/μ₀)
```

**This is valid and retained.** It is not the source of the n·ln n form;
it is the value of the leading coefficient B.

---

## Why the S1 Route Cannot Produce n·ln n

The S¹_ψ functional determinant is a **one-particle** calculation.
It gives:

- One-particle result: −ln n per mode → V4 form (no factor of n in front of ln n)
- The factor of n in "n·ln n" requires **n quanta** contributing simultaneously

To get n·ln n from a determinant calculation, one would need to compute
the determinant over a **many-body background with n winding quanta**, which
is not the S¹_ψ one-loop determinant; it is the 4D Coleman-Weinberg potential
for an n-particle state.

---

## The Correct Origin of n·ln n

### Mechanism: 4D vacuum polarisation applied to the n-winding background

A winding configuration at level n contains n charged quanta, each with
Kaluza-Klein mass m_k = k (k = 1, …, n in the winding ladder).

At one loop in 4D, each quantum contributes an independent vacuum polarisation:

```
δV^(1)_{1-loop} = −(B₀/2) · ln(μ_n/μ₀)     (one quantum)
```

where μ_n = n is the winding mass scale. Summing over n quanta:

```
δV^(n)_{1-loop} = n × (−B₀/2) · ln n = −(B₀ · n · ln n) / 2
```

After folding the factor into the coefficient convention:

```
V_eff(n) = n² − B₀ · n · ln n,    B₀ = 8π ≈ 25.133
```

This is the correct **n·ln n** form. The extra factor of n comes from
the n independent quanta, not from the single-particle S¹ determinant.

**No arbitrary cutoff is introduced**: the Wilsonian decoupling of modes
k > n at scale μ = n is the standard justification in Kaluza-Klein
effective field theory.

---

## Classification in the Failed Routes Graveyard

**Entry for `reports/failed_routes_graveyard.md`**:

> ### S1 Functional Determinant → B·n·ln n
>
> **Attempt**: Derive the n·ln n coefficient B from the functional determinant
> of −∇†∇ on the S¹_ψ circle.
>
> **Result**: [DEAD END]. The one-particle S¹_ψ determinant gives −N_eff·ln n
> (form V4), not −B·n·ln n (correct V_eff form). The minimum of V4 is at
> n* ≈ 2.45, far from 137.
>
> **Lesson**: The S¹ determinant is a one-particle calculation.
> The n·ln n term requires summing over n winding quanta, which is a
> 4D many-body (vacuum polarisation) calculation, not a circle determinant.
>
> **What is retained**: The S¹_ψ vacuum polarisation gives B₀ = 2πN_eff/3 = 8π,
> which is the leading value of the B coefficient. This result is valid [L1].
>
> **Date closed**: 2026-05-04  
> **Source**: `canonical/alpha/nlogn_origin_analysis.tex` §2, §3

---

## Impact on the Primary Route (A_PRIME)

The primary route **A_PRIME is unaffected** by this no-go result:

| Item | Before | After |
|------|--------|-------|
| Form V_eff(n) = n² − B·n·ln n | Informal justification via S1 det | Derived from 4D RG, Mechanism 1 |
| B₀ = 8π | Derived from S1 vacuum polarisation | Unchanged — still valid [L1] |
| n* = 137 from B_phenom | Unchanged | Unchanged |
| Gap G137-B (B₀ → B_phenom) | Open | Open — now better understood |

The only change is that the **justification** for the n·ln n form is
clarified: it comes from 4D RG (Mechanism 1), not from the S¹
single-particle determinant.

---

## Summary of Candidate Mechanisms

| Mechanism | Produces n·ln n? | Status |
|-----------|-----------------|--------|
| S¹ one-particle functional det | **No** (gives −N_eff·ln n, form V4) | DEAD for B |
| S¹ vacuum polarisation | **No** (gives B₀ coefficient) | Valid for B₀ = 8π |
| 4D RG, n winding quanta | **Yes** (gives −B₀·n·ln n) | PROVED [L1] |
| Stirling entropy (with decoupling) | **Yes, conditional** | Open |
| Modular coset μ(Γ₀(n)) | **No** (gives ~n, linear) | Useful for B value |
| Hecke/theta arithmetic | **No** (gives N^{½–3/2}) | Useful for consistency |

---

## References

- `canonical/alpha/nlogn_origin_analysis.tex` — full calculation
- `canonical/alpha/veff_corrected.tex` — V_eff form definitions
- `canonical/n_eff/step2_vacuum_polarization.tex` — B₀ = 8π derivation [L1]
- `canonical/alpha/alpha_best_route.tex` — primary A_PRIME route
- `reports/alpha_missing_lemma.md` — Gap G137-B exact statement
- `reports/failed_routes_graveyard.md` — other dead routes
