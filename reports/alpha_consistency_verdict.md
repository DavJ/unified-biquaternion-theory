<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# alpha_consistency_verdict.md — Alpha Route Consistency Verdict

**Author**: Ing. David Jaroš  
**Date**: 2026-05-02  
**Track**: T3_ALPHA  
**Priority**: CRITICAL  
**Mode**: prove_or_break  
**Purpose**: Definitive statement of whether the alpha route is
mathematically consistent, following the V_eff extremum correction and
the Alpha Critical Fix audit.

---

## Verdict Summary

| Claim | Status | Condition |
|-------|--------|-----------|
| V_eff functional form correct | ✅ **YES** | V1: n² − B·n·ln n (derived) |
| Stationarity condition correct | ✅ **YES** | Transcendental: 2n\* = B(ln n\*+1) |
| n\* = 137 is a valid prime minimiser | ✅ **YES** | For B ∈ [46.00, 46.50] |
| B ≈ 46.3 is independently derived | ❌ **NO** | B_phenom is phenomenological (circular) |
| Alpha route is first-principles | ❌ **NOT YET** | Conditional on Gap G137-B |
| Alpha route is internally consistent | ✅ **YES** | No internal contradiction |
| Alpha route should be abandoned | ❌ **NO** | Route is valid; B must be derived |

**One-sentence verdict**:

> **The alpha route is mathematically consistent but incomplete: the effective
> potential V_eff(n) = n² − B·n·ln n is correctly derived, n\* = 137 is the
> prime minimiser for the required B ≈ 46.284, but B itself is currently
> phenomenological and cannot be promoted to a first-principles result until
> Gap G137-B is formally resolved.**

---

## 1. The Corrected V_eff

The unique form consistent with the one-loop Coleman-Weinberg calculation
on S¹_ψ is:

```
V_eff(n) = n² − B·n·ln n
```

**Derivation**: Classical KK energy E_n = n² (natural units) plus the
one-loop functional determinant S_CW(n) ≈ (N_eff/2)·n·ln n, giving
V_eff = E_n − S_CW.

**This form is PROVED [L1]** given B (functional form only; B is open).

An earlier version of the repository wrote `V_eff = n² − B·ln n` (missing
the factor n). This is form V4; its stationarity condition is `n* = √(B/2)`,
which gives n\* ≈ 4.8 for B ≈ 46.3 — far from 137. Form V4 is **inconsistent**
with the one-loop calculation and has been corrected in all relevant documents
(2026-05-02).

---

## 2. The Stationarity Condition

```
∂V_eff/∂n|_{n*} = 2n* − B(ln n* + 1) = 0

⟹   2n* = B·(ln n* + 1)         [transcendental, no closed form]
```

For B = B_required ≈ 46.284, the numerical solution is n\*_continuous = 137.000.
The prime minimiser is p = 137, with the next nearest prime (139) having
V(139) − V(137) ≈ +3.16.

**Status**: PROVED [L1] given B (stationarity condition is exact).

The stationarity formula `n* = √(B/2)` that appeared in some older documents
belongs exclusively to form V4 (the wrong potential) and is **not** a formula
for the correct V_eff.

---

## 3. Required B for n\* = 137

From `2n* = B·(ln n* + 1)` at n\* = 137:

```
B_required = 2×137 / (ln 137 + 1)
           = 274 / (4.91998 + 1)
           = 274 / 5.91998
           ≈ 46.284
```

The phenomenological value B_phenom ≈ 46.298 in the repository differs from
B_required by 0.030%, consistent with rounding.

---

## 4. Classification of B

| B value | Origin | Classification |
|---------|--------|----------------|
| B₀ = 8π ≈ 25.13 | One-loop vacuum polarisation, N_eff=12 | **DERIVED** [L1] |
| B_base = N_eff^{3/2} ≈ 41.57 | Kac-Moody k=1 (Gap G3-k) | **CONJECTURAL** [MC] |
| μ(Γ₀(137))/3 = 46.00 | Exact group index formula | **EXACT MATH** [L0]; link to B is OPEN |
| B_required ≈ 46.284 | Inverted stationarity at n\*=137 | **CIRCULAR** if used as input |
| B_phenom ≈ 46.298 | Back-solved from n\*=137 | **PHENOMENOLOGICAL** |

The nearest derived value is B₀ = 8π ≈ 25.13, giving n\* ≈ 65 (not 137).
Reaching n\* = 137 requires an additional factor ≈ 1.84 beyond B₀ (Gap G137-B).

---

## 5. Errors Found and Fixed

| Document | Error | Fixed |
|----------|-------|-------|
| `canonical/appendices/appendix_alpha_geometry.tex` | V_eff written as `n² − B·ln n` (V4); proof used n\*=√(B/2) | ✅ 2026-05-02 |
| `ALPHA_PROGRESS_REPORT.md` §2.3 header | Section title showed wrong V4 form | ✅ 2026-05-02 |
| `ALPHA_PROGRESS_REPORT.md` §9 entry A7 | Clean-chain listed `n*=√(B/2)` | ✅ 2026-05-02 |
| `alpha_equation_matrix.tex` (pre-2026-04-29) | n\*(B) = e^{(2-B)/B}·e (wrong closed form) | ✅ Fixed prior session |

---

## 6. Status of the Alpha Route

### What is proved (zero free parameters):

- ℂ⊗ℍ axiom → N_eff = 12 → B₀ = 8π [L0/L1 proved]
- Functional form V_eff(n) = n² − B·n·ln n [L1 proved]
- Stationarity condition 2n\* = B(ln n\*+1) [L1 proved]
- Prime stability of n\*=137 (homotopy argument) [L1 proved]
- Primality of 137 [mathematical fact]

### What is not yet proved:

- B ≈ 46.3 from first principles (**Gap G137-B** — the blocking gap)
- Kac-Moody level k=1 from S[Θ] (**Gap G3-k** — prerequisite for B_base)
- Connection of μ(Γ₀(137))/3 = 46.00 to B in S[Θ] (**Gap G-hecke**)

### The missing factor:

```
R = B_phenom / B_base ≈ 46.298 / 41.569 ≈ 1.1134
```

This factor has no non-circular derivation. All 27+ tested approaches have
been exhausted without finding R from first principles (see
`ALPHA_PROGRESS_REPORT.md §3.3`).

---

## 7. Decision

### Per the problem-statement decision tree:

**Is V_eff consistent?** → **YES** (form V1 is correct and derived).

**Does consistent V_eff yield n\* ~ 137?** → **YES, conditionally** (for B ≈ 46.28–46.30).

**Is B independently derived?** → **NO** (phenomenological; circular unless Gap G137-B is formally resolved).

**Action**:

> Keep the alpha route.
> Mark B as the primary target for derivation (Gap G137-B).
> Classify current status as: **alpha route MATHEMATICALLY CONSISTENT, proof status CONDITIONAL [L1]**.
> Do NOT downgrade to CONJECTURAL — the mathematics is valid.
> Do NOT promote to PROVED — B is not derived.

---

## 8. Next Steps

1. **Attack Gap G137-B** (primary):
   - Modular bootstrap on Z(τ) = ϑ₃³(τ) + crossing symmetry constraints
   - Time-box: 4 weeks from 2026-05-02 (deadline 2026-06-02)

2. **Explore Route A** (Modular-Hecke):
   - Derive B from μ(Γ₀(n\*))/3 via Hecke eigenform structure of S[Θ]
   - The 0.64% gap between μ(Γ₀(137))/3 = 46.00 and B_required = 46.284 may
     be bridgeable via a two-loop correction

3. **Maintain honest status labelling**:
   - n\*(B_phenom) = 137 → label as **CONDITIONAL [L1]**
   - B_phenom → label as **PHENOMENOLOGICAL** in all documents

---

## References

| File | Role |
|------|------|
| `canonical/alpha/veff_corrected.tex` | First-principles V_eff derivation |
| `canonical/alpha/veff_corrected_statement.tex` | Formal theorem list |
| `reports/veff_extremum_audit.md` | Derivative check and variant table |
| `reports/alpha_veff_sanity_audit.md` | Prior comprehensive audit |
| `canonical/alpha/alpha_equation_matrix.tex` | Three-route equation chain |
| `canonical/alpha/alpha_best_route.tex` | Full derivation chain |
| `ALPHA_PROGRESS_REPORT.md` | Strategy and progress |
| `reports/alpha_missing_lemma.md` | Gap G137-B formal statement |
| `reports/alpha_no_fit_audit.md` | No-fit audit of all routes |
