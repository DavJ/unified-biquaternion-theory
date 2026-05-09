<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Alpha Remaining Contradictions Cleanup Report

**Author**: Ing. David Jaroš  
**Date**: 2026-05-09  
**Status**: Completed  
**Task**: `cleanup_remaining_alpha_canonical_contradictions`  
**Mode**: `cleanup_only_no_new_theory`

---

## 1. Purpose

Follow-up cleanup after `reports/alpha_old_formula_cleanup.md` (2026-05-03).
That report removed the bulk of `n* = sqrt(B/2)` and `V_eff = n^2 - B ln n`
occurrences. This report documents the remaining active-file contradictions
found and corrected, plus confirms which files required no changes.

**Two target errors:**

1. **Old V_eff formula**: `V_eff(n) = n^2 - B ln n` (missing factor `n`) →
   correct form: `V_eff(n) = n^2 - B n ln n`

2. **Old stationarity**: `n* = sqrt(B/2)` (stationarity of wrong V4 form) →
   correct form: `2 n* = B (ln n* + 1)` (transcendental, no closed form)

---

## 2. Files Checked and Actions Taken

### 2.1 `canonical/alpha/alpha_best_route.tex` — CORRECTED

**Location**: Complete Status Table (§ "Complete Status Table"), Step 6 row.

**Before**:
```latex
6 & $V_{\mathrm{eff}}(n) = n^2 - B\ln n$ & CLEAN [L1] given $B$ & No & — & \S\ref{sec:ar:Veff} \\
```

**After**:
```latex
6 & $V_{\mathrm{eff}}(n) = n^2 - B\,n\ln n$ & CLEAN [L1] given $B$ & No & — & \S\ref{sec:ar:Veff} \\
```

**Note**: The body of §6 (sec:ar:Veff) already correctly states
`V_eff(n) = n^2 - B_base n ln n` and the stationarity condition
`2n* = B(ln n* + 1)`. Only the summary table contained the old form.

---

### 2.2 `canonical/alpha/best_candidate_derivation.tex` — CORRECTED

**Three locations** within Step 6 (sec:bc:Veff):

#### 2.2.1 Theorem 6.1 equation (eq:bc:Veff)

**Before**:
```latex
V_{\mathrm{eff}}(n) = n^2 - B\ln n + \mathrm{const},
```

**After**:
```latex
V_{\mathrm{eff}}(n) = n^2 - B\,n\ln n + \mathrm{const},
```

#### 2.2.2 Description in Theorem 6.1 body

**Before**:
```
where the $n^2$ term is the classical winding energy and $-B\ln n$ is the
one-loop correction from vacuum polarisation...
```

**After**:
```
where the $n^2$ term is the classical winding energy and $-B\,n\ln n$ is the
one-loop correction from vacuum polarisation...
```

#### 2.2.3 Proof text

**Before**:
```
polarisation contribution shifts this energy by $-B\ln n$, where $B$ is
```

**After**:
```
polarisation contribution shifts this energy by $-B\,n\ln n$, where $B$ is
```

#### 2.2.4 Complete Status Table, Step 6 row

**Before**:
```latex
6 & $V_{\mathrm{eff}}(n) = n^2 - B\ln n$ & CLEAN [L1] given $B$ & No & \S\ref{sec:bc:Veff} \\
```

**After**:
```latex
6 & $V_{\mathrm{eff}}(n) = n^2 - B\,n\ln n$ & CLEAN [L1] given $B$ & No & \S\ref{sec:bc:Veff} \\
```

**Note**: Step 7 (sec:bc:nstar) and all later sections in this file already
used the correct formula `n^2 - B n ln n` and the correct transcendental
stationarity condition `2q* = B(ln q* + 1)`. Only Step 6 had the old form.

---

### 2.3 `canonical/alpha/alpha_equation_matrix.tex` — NO CHANGES NEEDED

All theorem statements (Theorem 2.2 at §2.2, Theorem 2.3 at §2.3) already
use the correct formulas:
- `V_eff(n) = n^2 - B · n · ln n`
- `2n* = B(ln n* + 1)`

The file includes an explicit note removing the old `n*(B) = e^{(2-B)/B} · e`
formula. No active contradictions remain.

---

### 2.4 `canonical/alpha/modular_prime_attractor_theorem.tex` — NO CHANGES NEEDED

All occurrences of `sqrt(B/2)` are contained within:
- A `\warnbox` at §"V_eff Stationarity" explicitly labelled **"Removed formula"**,
  stating the formula is **not** the correct stationarity condition.
- The comparison table at §"Comparison with the Old Correction-Factor Route",
  in the "Old route (abandoned)" column.
- The Summary list item 6, stating the correction-factor route is
  **abandoned**.

All are clearly marked as historical record of the error. No active claims.

---

### 2.5 `canonical/appendices/appendix_alpha_geometry.tex` — NO CHANGES NEEDED

Already contains the correct formula `V_eff(n) = n^2 - B n ln n` (Definition 3.1)
and `2n* = B(ln n* + 1)` (Theorem 4.1), each accompanied by an explicit
`\warnbox` correction notice referencing the old wrong form and why it was
removed.

---

### 2.6 `reports/alpha_old_formula_cleanup.md` — NO CHANGES NEEDED

This existing report (2026-05-03) documents the prior round of removals.
It correctly notes that `sqrt(B/2)` in warning boxes is **retained** as
historical record, and lists the files already cleaned. No update required.

---

## 3. eta(i) Status

Checked all `canonical/alpha/` files for `eta(i)` presented as an active
derived B-modifier. Findings:

| File | Context | Status |
|------|---------|--------|
| `canonical/alpha/veff_corrected.tex` §B-candidates table | Listed as "HISTORICAL OBSERVATION — rejected as first-principles B-modifier" | ✅ Correctly marked rejected |
| `canonical/alpha/ALPHA_MASTER_STATUS.md` | "eta(i) route: rejected as first-principles B-modifier" | ✅ Correctly marked rejected |

No active canonical file presents `eta(i)` as a derived B-modifier.

---

## 4. "Alpha is Derived" Claims

No active canonical file claims alpha is fully derived. All relevant files
(alpha_best_route.tex, best_candidate_derivation.tex, alpha_equation_matrix.tex,
modular_prime_attractor_theorem.tex) explicitly state:

- `n* = 137` is **CONDITIONAL** on Gap G137-B / Gap G-Bmod
- `alpha^{-1}_bare = 137` is **CONDITIONAL**, not a zero-parameter result until
  the gap is closed
- The kill condition (no free parameter fitted to reproduce alpha or 137) is
  stated explicitly

---

## 5. Summary of Changes

| File | Action | Locations |
|------|--------|-----------|
| `canonical/alpha/alpha_best_route.tex` | Corrected old V_eff in summary table | 1 location |
| `canonical/alpha/best_candidate_derivation.tex` | Corrected old V_eff in theorem, proof, and summary table | 4 locations |
| `canonical/alpha/alpha_equation_matrix.tex` | No changes — already correct | — |
| `canonical/alpha/modular_prime_attractor_theorem.tex` | No changes — old formula only in warning boxes | — |
| `canonical/appendices/appendix_alpha_geometry.tex` | No changes — already correct with warning boxes | — |
| `reports/alpha_old_formula_cleanup.md` | No changes — existing record sufficient | — |

---

## 6. Canonical References

- Corrected V_eff: `canonical/alpha/veff_corrected.tex`
- Corrected V_eff statement: `canonical/alpha/veff_corrected_statement.tex`
- Current alpha verdict: `reports/alpha_current_verdict.md`
- eta(i) rejection: `reports/alpha_eta_i_rejection.md`
- Prior cleanup: `reports/alpha_old_formula_cleanup.md`
