<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# B46 Master Verdict: Can B≈46 Be Derived from UBT RG/Mode-Counting?

**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Task**: `derive_or_kill_B46_from_RG_and_mode_counting`  
**Priority**: CRITICAL  
**Hard rules**: No use of α, 137, B_required, or B(p)=(p+1)/3 as input; no new alpha routes;
no modular ansatz as derivation; no modification of canonical/.

---

## Executive Summary

This report collects the results of five targets (T1–T5) in the `research_tracks/rg_B46/`
track and delivers the master verdict on whether the coefficient $B \approx 46$ in

$$V_\mathrm{eff}(n) = n^2 - B\,n\ln n$$

can be derived from the UBT action $S[\Theta]$ through RG flow, vacuum polarisation,
KK/winding mode counting, or higher-loop corrections.

> **FINAL VERDICT** (updated after winding NO-GO):
> **B≈46 is open. The constant winding correction ΔB_wind ≈ 18.5 is NO-GO.**
> **B_best ≈ 43.6 is downgraded from best estimate to OBSOLETE HEURISTIC.**
> **The strongest safe coefficient remains B₀ = 8π (conditional on KK matching).**

---

## 1. Derivation Chain

The complete derivation chain, with proof-status labels at each step, is:

| Step | Claim | Source | Status |
|------|-------|--------|--------|
| 1 | $S_\mathrm{quad}[\Theta]$ on $\mathcal{M}^4 \times S^1_\psi$ | UBT axioms | PROVED |
| 2 | KK mass: $m_n^2 = n^2$ (natural units, $R_\psi = 1$) | KK reduction | PROVED |
| 3 | $V_\mathrm{tree}(n) = n^2$ | From step 2 | PROVED |
| 4 | $N_\mathrm{eff} = 12$ charged complex scalar modes | $\mathcal{B} = \mathbb{C}\otimes\mathbb{H}$, 5 routes | PROVED |
| 5 | One-loop beta coefficient: $b_0 = N_\mathrm{eff}/3 = 4$ | Standard scalar QED | PROVED |
| 6 | $n\ln n$ shape in $V_\mathrm{eff}$ from one-loop | Scheme-independent | PROVED |
| 7 | Factor $2\pi$ from KK compactification: $B_0 = 2\pi b_0 = 8\pi$ | KK matching | CONDITIONAL |
| 8 | $R_\psi = 1$ is self-dual radius | Assumed, not derived | HEURISTIC |
| 9 | T-duality winding correction $\Delta B_\mathrm{wind} \approx 18.5$ = constant | T-duality at $R=1$ | **NO-GO** — see `reports/t_dual_winding_verdict.md` |
| 9′ | Derived winding increment: $\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}\,n/(12\pi^2)$ | Compact tower (no fitting) | PROVED (n-dependent) |
| 10 | $B_\mathrm{best} = B_0 + \Delta B_\mathrm{wind} \approx 43.6$ | Steps 7+9 | **OBSOLETE HEURISTIC** (step 9 is NO-GO) |
| 11 | Two-loop, ghost, curvature, zero-mode, torus shape: all negligible or zero | Explicit computation | PROVED / DERIVED |
| 12 | Gap $\Delta B$ to target $B \approx 46$ | Comparison | OPEN (fully open after NO-GO) |

---

## 2. Table of All Coefficients

| Quantity | Symbol | Value | Status |
|---------|--------|-------|--------|
| KK mass | $m_n^2$ | $n^2$ | PROVED |
| Effective mode count | $N_\mathrm{eff}$ | 12 | PROVED |
| Beta coefficient | $b_0 = N_\mathrm{eff}/3$ | 4 | PROVED |
| One-loop baseline | $B_0 = 2\pi b_0$ | $8\pi \approx 25.133$ | CONDITIONAL |
| Two-loop correction | $\Delta B_\mathrm{2-loop}$ | $\lesssim 0.05$ | PLAUSIBLE |
| KK threshold tower | $\Delta B_\mathrm{KK}$ | $\approx 13.9$ | PLAUSIBLE |
| Winding correction (constant) | $\Delta B_\mathrm{wind}$ | $\approx 18.5$ | **OBSOLETE HEURISTIC** (NO-GO) |
| Winding increment (derived) | $\Delta B_\mathrm{wind}(n)$ | $N_\mathrm{eff}\,n/(12\pi^2)$ | PROVED (n-dependent; adds $n^2\ln n$ term, not constant $B$ shift) |
| Compactification threshold | $\Delta B_\mathrm{comp}$ | $0$ | DERIVED |
| Ghost determinant | $\Delta B_\mathrm{ghost}$ | $0$ | DERIVED |
| Zero-mode subtraction | $\Delta B_\mathrm{zero}$ | $0$ | DERIVED |
| Curvature ($\xi=0$) | $\Delta B_\mathrm{curv}$ | $0$ | DERIVED |
| Torsion (bosonic) | $\Delta B_\mathrm{tors}$ | $0$ | DERIVED |
| Torus shape ($\epsilon=0$) | $\Delta B_\mathrm{shape}$ | $0$ | CONDITIONAL |
| **Best total** | $B_\mathrm{best}$ | $\approx 43.6$ | **OBSOLETE HEURISTIC** (based on NO-GO step) |
| **Range minimum** | $B_\mathrm{min}$ | $8\pi \approx 25.1$ | CONDITIONAL |
| **Range maximum** | $B_\mathrm{max}$ | $\approx 50.6$ | **OBSOLETE HEURISTIC** |
| **Phenomenological target** | $B \approx 46$ | — | INPUT: compared at end |
| **Current safe coefficient** | $B_0 = 8\pi$ | $\approx 25.133$ | CONDITIONAL (strongest safe claim) |
| **Gap** | $\Delta B = B - B_0$ | $\approx 20.9$ | FULLY OPEN |

---

## 3. Proof-Status Table

| Claim | Proof Status |
|-------|-------------|
| $n^2$ term from KK compactification | ✅ PROVED |
| $n\ln n$ shape from one-loop | ✅ PROVED |
| Gauge invariance of $n$ as U(1)$_\psi$ charge | ✅ PROVED |
| Scheme independence of $\ln n$ coefficient | ✅ PROVED |
| $N_\mathrm{eff} = 12$ from field content | ✅ PROVED |
| $b_0 = 4$ from scalar QED | ✅ PROVED |
| $B_0 = 8\pi$ (with $2\pi$ factor) | ⚠️ CONDITIONAL |
| Self-dual radius $R_\psi = 1$ derived | ❌ OPEN |
| Constant winding correction $\Delta B_\mathrm{wind} \approx 18.5$ | ❌ **NO-GO** — correction is $n$-dependent, not a constant $B$ shift |
| Derived winding increment $\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}n/(12\pi^2)$ | ✅ PROVED (n-dependent; adds $n^2\ln n$ structure) |
| $B_\mathrm{best} \approx 43.6$ | ❌ **OBSOLETE HEURISTIC** |
| Gap from $B_0 = 8\pi$ to $B \approx 46$ fully open | ❌ OPEN |
| $B = 46$ proved | ❌ NOT PROVED |

---

## 4. Failed Routes

| Route | Why it fails |
|-------|-------------|
| Pure one-loop 4D (no winding) | $B_0 = 8\pi \approx 25.1 \ll 46$ |
| Pure one-loop 1D (naive) | Gives $n$-dependent $B = n/(2\pi)$, not constant |
| Two-loop alone | $\Delta B \lesssim 0.05$, negligible |
| Ghost determinant | $\Delta B_\mathrm{ghost} = 0$ (U(1) abelian) |
| Curvature correction (flat bg) | $\Delta B_\mathrm{curv} = 0$ |
| KK + winding double-counted | Overcounts; double-counting excluded |
| **Constant winding correction** $\Delta B_\mathrm{wind} \approx 18.5$ | **NO-GO**: derived correction is $n$-dependent $\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}n/(12\pi^2)$, producing an $n^2\ln n$ term, not a constant $B$ shift; see `reports/t_dual_winding_verdict.md` |
| Modular ansatz $B(p)=(p+1)/3$ | Not derived from $S[\Theta]$ (Obstruction O1 blocked) |
| Hecke path integral | No-go (O1, O2, O3 unresolved); see `reports/hecke_path_integral_no_go_or_success.md` |

---

## 5. Surviving Route

**After the winding NO-GO, the only surviving safe coefficient is**:

$$B_0 = 8\pi \approx 25.133 \quad \text{(CONDITIONAL on KK matching)}.$$

The former "best estimate" $B_\mathrm{best} \approx 43.6$, which relied on the constant
winding correction $\Delta B_\mathrm{wind} \approx 18.5$, is **downgraded to OBSOLETE
HEURISTIC**.  That correction is not a universal constant derivable from
$S[\Theta]$; the actual derived expression is:

$$\Delta B_\mathrm{wind}(n) = \frac{N_\mathrm{eff}\,n}{12\pi^2},$$

which is $n$-dependent and produces an additional $n^2\ln n$ term in $V_\mathrm{eff}$,
not a constant shift of the $n\ln n$ coefficient.

**Alpha remains not derived.** The gap from $B_0 = 8\pi$ to $B \approx 46$ is fully open.

---

## 6. Comparison to Structural Values

| Value | Relation to $B_0$ | Relation to target 46 | Comment |
|-------|-------------------------------|----------------------|---------|
| $8\pi \approx 25.133$ | $= B_0$ (one-loop, CONDITIONAL) | $-45\%$ | Strongest safe coefficient |
| $12^{3/2} \approx 41.57$ | $> B_0$ | $-9.6\%$ | No mechanism |
| $43.6$ | $B_\mathrm{best}$ (OBSOLETE HEURISTIC) | $-5.2\%$ | Based on NO-GO winding step |
| $46$ | target | — | Not derived; gap fully open |

---

## 7. Final Verdict

$$\boxed{\text{B≈46 is OPEN. Constant winding correction is NO-GO. B\_best ≈ 43.6 is OBSOLETE HEURISTIC.}}$$

**Status after winding NO-GO**:
- The constant winding correction $\Delta B_\mathrm{wind} \approx 18.5$ is **NO-GO**.
  The derived winding term is $n$-dependent:
  $\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}n/(12\pi^2)$,
  producing an $n^2\ln n$ contribution, not a constant $B$ shift.
- $B_\mathrm{best} \approx 43.6$ is **downgraded to OBSOLETE HEURISTIC**; it relied on
  the now-rejected constant winding step.
- Alpha remains **not derived**.
- The **current strongest safe coefficient** is the one-loop baseline:
  $$B_0 = 8\pi \approx 25.133 \quad (\text{CONDITIONAL on KK matching}).$$
- $B \approx 46$ remains **OPEN**.

**Open gaps preventing any PROVED status**:
1. Constant winding correction is NO-GO; derived correction is $n$-dependent.
2. $R_\psi = 1$ (self-dual radius) is not derived from the UBT moduli problem.
3. The factor $2\pi$ in $B_0 = 8\pi$ requires explicit 5D→4D coupling matching.
4. No perturbative mechanism bridges $B_0 = 8\pi$ to $B \approx 46$.

**Recommended next step** (if RG/mode-counting insufficient):
→ Full Modular Covariance Route (prove $\mathrm{SL}(2,\mathbb{Z})$ invariance of $S[\Theta]$;
see `reports/B46_next_path_if_no_go.md`).  Or spectral operator route (heat-kernel derivation
of $B$ as geometric invariant).

See `reports/alpha_B_gap_after_winding_no_go.md` for the updated B-gap status.

---

## 8. References

| Document | Role |
|----------|------|
| `research_tracks/rg_B46/one_loop_rg_derivation.tex` | Target 1: one-loop derivation of $B_0$ |
| `research_tracks/rg_B46/neff_field_content_audit.md` | Target 2: $N_\mathrm{eff}=12$ audit |
| `research_tracks/rg_B46/higher_loop_thresholds.tex` | Target 3: corrections $\Delta B_i$ |
| `reports/B46_RG_decision_report.md` | Target 4: numerical range and verdict |
| `reports/B46_next_path_if_no_go.md` | Target 5: replacement paths |
| `research_tracks/rg_nlogn/full_rg_derivation.tex` | Prior work: 1D one-loop derivation |
| `research_tracks/rg_nlogn/b_coefficient_analysis.md` | Prior work: B sensitivity analysis |
| `reports/B_gap_final_verdict.md` | Prior work: master B-gap verdict (including Hecke no-go) |
| `reports/neff_12_dimension_count_audit.md` | Prior work: 5-route $N_\mathrm{eff}=12$ proof |
| `reports/hecke_path_integral_no_go_or_success.md` | Prior work: Hecke route no-go |
