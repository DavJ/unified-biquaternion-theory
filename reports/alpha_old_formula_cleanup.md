<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Alpha Old-Formula Cleanup Report

**Author**: Ing. David Jaroš  
**Date**: 2026-05-03  
**Status**: Completed  
**Related**: `canonical/alpha/modular_prime_attractor_theorem.tex`,
`reports/alpha_prime_minimizer_interval.md`

---

## 1. Purpose

Document all occurrences of erroneous alpha-derivation formulas that have been
removed or corrected as part of the transition from the correction-factor route
to the modular prime-attractor route.

**Two categories of removal:**

1. **`n* = sqrt(B/2)` used as a valid stationarity condition** — this is the
   stationarity condition of the *wrong* potential $V = q^2 - B\ln q$ (missing
   factor $q$). For $B \approx 46$, $\sqrt{B/2} \approx 4.8$, not 137.

2. **Correction factor $R \approx 1.113$** used to reach 137 from the wrong
   formula — this entire sub-route is abandoned (there is no non-circular
   derivation of $R$).

---

## 2. Occurrences of `n* = sqrt(B/2)` in Active Derivation Files

### 2.1 `canonical/alpha/best_candidate_derivation.tex` — Section 7

**Before** (Theorem 7.1, equations eq:bc:nstar and eq:bc:nstar_corrected):

```latex
n^* = \sqrt{B_{\mathrm{base}}/2} = \sqrt{N_{\mathrm{eff}}^{3/2}/2}.
...
n^* = \sqrt{12^{3/2}/2} = \sqrt{41.57/2} \approx \sqrt{20.79} \approx 4.56.
...
B = B_{\mathrm{base}} \cdot R^2 (correction factor R > 1 accounts for higher-loop)
n^* = \sqrt{B/2} = \sqrt{B_{\mathrm{base}} \cdot R^2 / 2} = R\sqrt{B_{\mathrm{base}}/2}.
```

**After** (Theorem 7.1 replaced): The theorem now states the correct
transcendental stationarity condition $2q^* = B(\ln q^* + 1)$, identifies
$B = \mu(\Gamma_0(137))/3 = 46$, and references the prime-stability interval.
The correction-factor sub-route is removed.

**Action**: Replaced equations eq:bc:nstar, eq:bc:nstar_raw, eq:bc:nstar_corrected,
and the surrounding text.  Also updated the Gap A12 warning box.

---

### 2.2 `research_tracks/T3_ALPHA/modular_bootstrap_k1_attempt.tex`

**Before** (pre-proved results table, row 5 of step-by-step summary):

```latex
V_{\mathrm{eff}}(n) = n^2 - B\ln n     [CLEAN L1]
Stationarity n^* = \sqrt{B/2}           [CLEAN L1]
...
n^* = \sqrt{B_{\mathrm{base}}/2} \approx 4.56 \to 137?  [Need B_base · R^2]
```

**After**: The pre-proved results table now lists the correct potential
$V(q;\,B) = q^2 - B\,q\ln q$ and the transcendental stationarity condition.
Step 5 of the summary is replaced with the modular prime-attractor result.

**Action**: Updated the two table rows.

---

## 3. Files Where `sqrt(B/2)` Appears in *Warning Boxes* (Retained)

The following files contain `sqrt(B/2)` only inside explicit correction notices
or warning boxes that state the formula is **wrong**. These occurrences are
**retained** because they document the historical error and explain why it was
wrong:

| File | Context | Status |
|------|---------|--------|
| `canonical/alpha/veff_corrected_statement.tex` §V4 | Identifies V4 as incorrect; $\sqrt{B/2}$ shown as wrong formula | **Retained** (warning) |
| `canonical/alpha/veff_corrected_statement.tex` §Correction | "Correct the formula ... replace $n^* = \sqrt{B/2}$" | **Retained** (instruction note) |
| `canonical/alpha/veff_corrected.tex` §Error table | Historical error table entry | **Retained** (historical record) |
| `canonical/appendices/appendix_alpha_geometry.tex` §Correction | Warning box: "previous version stated $n^* = \sqrt{B/2}$, which is wrong" | **Retained** (warning) |

---

## 4. Files Where Correction Factor `R ≈ 1.113` Appeared in Active Routes

### 4.1 Removed from `canonical/alpha/best_candidate_derivation.tex`

- Equations eq:bc:nstar_corrected ($n^* = R\sqrt{B_{\mathrm{base}}/2}$): **removed**
- Text "correction factor $R > 1$ accounts for higher-loop contributions": **removed**
- Gap A12 warning box text about $R \approx 1.114$: **updated** to note that the
  correction-factor route is superseded by the modular prime-attractor route

### 4.2 Retained in Non-Active / Archive Files

The correction factor $R$ and formula $n^* = \sqrt{B/2}$ still appear in the
following locations, which are either:
- archive/legacy files (read-only, not cited by active derivations), or
- research track files documenting abandoned routes, or
- files already containing explicit warning/correction notices

These are retained as historical record per the archival policy.

---

## 5. What Replaces the Old Route

The correction-factor route is replaced by the **Modular Prime-Attractor Route**:

| Old route | New route |
|-----------|-----------|
| Stationarity: $q^* = \sqrt{B/2}$ | Stationarity: $2q^* = B(\ln q^* + 1)$ (transcendental) |
| Reaching 137: correction factor $R \approx 1.113$ (open) | $B = \mu(\Gamma_0(137))/3 = 46$ (exact modular invariant) |
| Primary gap: derive $R$ from $S[\Theta]$ | Primary gap: derive $B = \mu(\Gamma_0(p))/3$ from $S[\Theta]$ (Gap G-Bmod) |

See `canonical/alpha/modular_prime_attractor_theorem.tex` for the full formal
statement of the new route.

---

## 6. Remaining Gap

Gap G-Bmod (**[Open]**): Derive $B = (p+1)/3$ from the UBT action $S[\Theta]$
without using $p = 137$, $\alpha$, or any phenomenological input.

Until this gap is closed, the prime-minimiser result $q = 137$ at $B = 46$ is
a **[L0] computation given the identification** — not a zero-parameter prediction.
