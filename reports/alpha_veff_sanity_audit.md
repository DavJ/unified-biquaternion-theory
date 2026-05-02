<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# alpha_veff_sanity_audit.md — V_eff(n) Sanity Audit and Next-Step Decision

**Author**: Ing. David Jaroš  
**Date**: 2026-05-02  
**Track**: T3_ALPHA — Fine Structure Constant Derivation  
**Priority**: CRITICAL  
**Mode**: proof_sanity_first  
**Purpose**: Verify the exact effective potential and determine whether the
n\* = 137 extremum claim is mathematically valid.

---

## 1. All V_eff(n) Variants Found in the Repository

A systematic grep for `V_eff`, `Veff`, and related notation across all `.tex`, `.md`,
and `.py` files produced the following distinct formulas.

### V1 — Primary Canonical Form (correct)

```
V_eff(n) = n² − B · n · ln n
```

**Sources**:
- `canonical/alpha/alpha_equation_matrix.tex` Theorem [L1] §2.2
- `canonical/alpha/alpha_best_route.tex` §6 (eq:ar:Veff)
- `canonical/alpha/neff_32_alpha_route.tex` §G5 (eq:g5:Veff)
- `canonical/appendices/appendix_alpha_geometry.tex §3`
- `ALPHA_PROGRESS_REPORT.md §2.3`
- `docs/papers/papers/generated/ubt_action_and_alpha.tex` (eq:V_eff)

The A = 1 coefficient arises from setting the classical KK winding energy scale
(ℏ²/(2mR²_ψ)) to 1 in natural units. This is stated explicitly in
`docs/papers/papers/generated/ubt_action_and_alpha.tex`: "A = ℏ²/(2mR²_ψ) = 1
(natural units; derived, zero free parameters)".

### V2 — Legacy Code Variant (A explicit)

```python
def V_eff(n, A=1.0, B=20.3):
    return A * n**2 - B * n * np.log(n)
```

**Source**: `ARCHIVE/archive_legacy/tex/emergent_alpha_calculations.tex` §code block

Same functional form as V1; A = 1.0 default. The coefficient B = 20.3 is
an early exploratory value. The script restricts the prime search to the
range 100–200, creating the *false* impression that B = 20.3 selects n = 137.
**The global prime minimum for B = 20.3 is at p = 47, not p = 137.**

### V3 — Non-Hermitian mass potential (unrelated to α)

```
V_eff = (m² + iγ) · Tr[Θ†Θ],   γ ∈ ℝ
```

**Source**: `canonical/symmetry/step3_breaking_catalogue.tex` eq:cat:V_eff

This is an open-system effective description of PT-symmetric dynamics.
**It has no role in the α derivation.** Listed only for completeness.

### V4 — Misquoted form (erroneous stationarity)

```
V(n) = n² − B · ln n   (WITHOUT the n factor)
```

This form appears *implicitly* in `ALPHA_PROGRESS_REPORT.md §2.4` where
the stationarity condition is stated as `n* = √(B/2)`.

**This formula is incorrect.** See §3 for the full derivation.

### V5 — Graviton effective potential (unrelated to α)

Referred to in `research_tracks/research/graviton_schwarzschild.tex §v71`.
This is the Zerilli-Regge–Wheeler potential for gravitational perturbations.
It has no connection to the α route.

---

## 2. Derivation of dV_eff/dn for Each α-Route Variant

### 2.1 V1: V(n) = n² − B·n·ln n

```
dV/dn = 2n − B·(ln n + 1)

Stationarity: dV/dn = 0  ⟹  2n* = B·(ln n* + 1)
```

This is a **transcendental equation** — no closed algebraic form for n\*(B).

Numerical solutions (bisection):

| B value | n\*_continuous | Note |
|---------|---------------|------|
| 8π ≈ 25.13 | 65.02 | B₀ (proved one-loop) |
| N_eff^{3/2} ≈ 41.57 | 120.35 | B_base (conjectural) |
| 46.00 | 135.99 | μ(Γ₀(137))/3 |
| **46.284** | **137.000** | Exact value for n\*=137 |
| 46.298 | 137.050 | B_phenom (phenomenological) |

**Conclusion for V1**: The formula is mathematically correct. The extremum
condition is valid. For B ≈ 46.284, the continuous minimum lands exactly at n = 137.

### 2.2 V4 (erroneous): V(n) = n² − B·ln n

```
dV/dn = 2n − B/n

Stationarity: 2n² = B  ⟹  n* = √(B/2)
```

For B = 46.298: n\* = √(23.149) ≈ 4.81.
**This is nowhere near 137.** The `√(B/2)` stationarity formula in
`ALPHA_PROGRESS_REPORT.md §2.4` belongs to this wrong variant and is a
transcription error.

---

## 3. Which Formula Gives n\* = 137?

Only **V1** (`V(n) = n² − B·n·ln n`) gives n\* = 137 for a reasonable coefficient.

The prime-restricted minimum of V1 for B ≈ 46.298 is:

| Prime p | V_eff(p) | ΔV = V(p) − V(137) |
|---------|---------|-------------------|
| **137** | **−12437.58** | **0.00** |
| 139     | −12434.42 | +3.16 |
| 131     | −12407.26 | +30.32 |
| 127     | −12354.07 | +83.51 |
| 149     | −12318.23 | +119.35 |

**137 is the prime minimizer of V1 for B ≈ 46.3.**

---

## 4. Required Coefficient for n\* = 137

From the stationarity condition `2n* = B·(ln n* + 1)`:

```
B_required = 2 × 137 / (ln 137 + 1)
           = 274 / (4.91998 + 1)
           = 274 / 5.91998
           = 46.2839...
```

The repo's phenomenological value B_phenom = 46.298 differs from this by only
**0.030%** — consistent with rounding in the source documents.

---

## 5. Status of B ≈ 46.3: Derivation Classification

| B value | Numerical value | Classification | Source |
|---------|----------------|----------------|--------|
| B₀ = 8π | 25.133 | **DERIVED [L1]** | One-loop vacuum polarisation, N_eff=12 modes on S¹_ψ |
| B_base = N_eff^{3/2} | 41.569 | **CONJECTURAL [MC]** | Conditional on Kac-Moody level k=1 (Gap G3-k open) |
| B_full = B_base × R | ≈ 46.31 | **PHENOMENOLOGICAL** | R ≈ 1.114 has no non-circular derivation |
| μ(Γ₀(137))/3 = 138/3 | 46.000 | **EXACT MATH** | Group-index formula; 0.64% from B_phenom; not yet proved = B |
| **B_phenom** | **46.298** | **PHENOMENOLOGICAL** | Back-solved from n\*(B)=137 using α as input; circular |
| B_required | 46.284 | **EXACT CONSTRAINT** | The unique B giving n\*_continuous = 137 exactly |

### Key conclusion on B ≈ 46.3

**B ≈ 46.3 is phenomenological.** Its current status in the repo is:

1. `B_phenom ≈ 46.298` is derived by inverting the stationarity condition with
   n\* = 137 as input. This is circular by construction.

2. The closest derived quantity is `B_base = N_eff^{3/2} ≈ 41.57`, which is
   itself conditional on proving the Kac-Moody level k = 1 (Gap G3-k, unresolved).

3. The closest mathematical coincidence is `μ(Γ₀(137))/3 = 46.00` (exact index
   formula), which lies 0.64% below B_phenom. This is a **supporting structural
   signal**, not a derivation. (See `reports/gamma0_137_invariants.md`.)

4. **No normalization convention converts B_base to B_phenom without introducing
   a free factor.** The correction factor R ≈ 1.114 has no non-circular derivation
   in the repo (confirmed in `alpha_best_route.tex §7 Remark` and stress-test §8.2).

---

## 6. Verification of the n\*(B) Closed-Form Formula in alpha_equation_matrix.tex

`canonical/alpha/alpha_equation_matrix.tex` Theorem [L1] states:

```
n*(B) = e^{(2−B)/B} · e
```

**This formula is wrong.** Algebraically:

```
e^{(2−B)/B} · e = e^{(2−B)/B + 1} = e^{2/B}
```

For B = 46.298: `e^{2/46.298} ≈ 1.044`. This is nothing like 137.

The correct stationarity relation is the transcendental equation:

```
2n* = B · (ln n* + 1)
```

This has no elementary closed form. The formula in the tex must be corrected.

---

## 7. Errors and Inconsistencies Found

| Document | Section | Error | Severity |
|----------|---------|-------|----------|
| `alpha_equation_matrix.tex` | Theorem [L1], §2.3 | Wrong closed-form `n*(B) = e^{(2-B)/B}·e`; this gives ~1.04, not 137 | HIGH |
| `ALPHA_PROGRESS_REPORT.md` | §2.4 | Stationarity stated as `n* = √(B/2)` — belongs to wrong variant V4; gives ~4.8 not 137 | HIGH |
| `emergent_alpha_calculations.tex` | Python code | B=20.3 appears to select n=137 but only because prime search is restricted to [100,200]; global prime min at B=20.3 is p=47 | MEDIUM |

---

## 8. B = 46.3 and Hidden Normalization

**Is there a hidden scale factor or normalization that converts B_base → B_phenom?**

Analysis (`alpha_best_route.tex §7`, `alpha_hidden_fit_audit.md`):

- The factor R = B_phenom / B_base = 46.298 / 41.569 = **1.1134**
- Candidates explored (all rejected or circular):
  - `R ≈ 1 + α·(N_eff + π + 1/4)` — 0.15% accuracy but uses α as input → **circular**
  - Two-loop β-function corrections → all dead-ended (see ALPHA_PROGRESS_REPORT §3.3)
  - Seeley-DeWitt curvature corrections → vanish in UV → **dead end**
  - Instanton corrections → require negative action → **impossible**
  - Hausdorff/NCG a₄ → restatements of 3/2 exponent without new coefficient → **partial only**
- The modular index coincidence `μ(Γ₀(137))/3 = 46.00` requires a **0.64% correction**
  even to reach B_phenom, and has no derivation tying it to S[Θ].

**Verdict: B ≈ 46.3 requires a hidden normalization that is currently not derived.
The factor 1.1134 has no first-principles derivation. It is an open problem (Gap G137-B).**

---

## 9. Decision After Audit

Per the problem statement decision tree:

### Is V_eff correct?

**Partially.** The functional form V(n) = n² − B·n·ln n is correct (V1).
Two documents contain errors in the stationarity formula (§7 above).
The form itself needs no correction; only the closed-form formula for n\*(B)
must be fixed.

### Is the 137 extremum claim valid?

**Yes, conditionally.** For V1 with B ≈ 46.284–46.298, n\* = 137 is the
prime minimizer. The mathematical claim is valid.

### Is B ≈ 46.3 derived, phenomenological, or inconsistent?

**Phenomenological.** B_phenom is back-solved from the requirement n\* = 137.
B_base = N_eff^{3/2} ≈ 41.57 is the nearest theoretically motivated value, but it
is itself conjectural (Gap G3-k) and gives n\* = 127, not 137.

### Is the missing factor R ≈ 1.113 a hidden normalization?

**Yes.** R = B_phenom / B_base ≈ 1.113 has no non-circular derivation.
It must be classified as **OPEN/PHENOMENOLOGICAL** until Gap G137-B is closed.

### Next step

**Continue deriving B**, specifically:

1. **Fix the two document errors** (wrong closed-form for n\*(B)) — see
   `canonical/alpha/veff_corrected_statement.tex` for the corrected statement.

2. **Attack Gap G137-B** (derive B from S[Θ] without using α as input):
   - Primary path: modular bootstrap on Ẑ(τ) = ϑ₃³(τ)
   - Secondary path: explicit two-loop heat-kernel determinant on T²×S¹_ψ
   - Corroborative path: prove μ(Γ₀(n\*))/3 = B from Hecke eigenform structure

3. **Do not promote** n\*(B_phenom) = 137 to PROVED until Gap G137-B is closed.
   Current honest status: **CONDITIONAL [L1]**.

---

## 10. References

| File | Role |
|------|------|
| `canonical/alpha/alpha_equation_matrix.tex` | Contains wrong n*(B) formula |
| `canonical/alpha/alpha_best_route.tex` | Correct V_eff derivation chain |
| `canonical/alpha/neff_32_alpha_route.tex` | G5 derivation with classification table |
| `canonical/alpha/veff_corrected_statement.tex` | Corrected V_eff statement (this audit's output) |
| `canonical/appendices/appendix_alpha_geometry.tex` | Source of V_eff form |
| `ALPHA_PROGRESS_REPORT.md §2.4` | Contains n*=√(B/2) error |
| `reports/alpha_hidden_fit_audit.md` | Prior hidden-fit analysis |
| `reports/alpha_missing_lemma.md` | Gap G137-B formal statement |
