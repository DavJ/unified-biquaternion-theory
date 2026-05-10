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

> **FINAL VERDICT**:
> **B≈46 is conditionally reachable but not proved.**

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
| 9 | T-duality doubles winding contribution: $\Delta B_\mathrm{wind} \approx 18.5$ | T-duality at $R=1$ | HEURISTIC |
| 10 | $B_\mathrm{best} = B_0 + \Delta B_\mathrm{wind} \approx 43.6$ | Steps 7+9 | HEURISTIC |
| 11 | Two-loop, ghost, curvature, zero-mode, torus shape: all negligible or zero | Explicit computation | PROVED / DERIVED |
| 12 | Gap $\Delta B \approx 2.4$ to target $B \approx 46$ | Comparison | OPEN |

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
| Winding correction | $\Delta B_\mathrm{wind}$ | $\approx 18.5$ | HEURISTIC |
| Compactification threshold | $\Delta B_\mathrm{comp}$ | $0$ | DERIVED |
| Ghost determinant | $\Delta B_\mathrm{ghost}$ | $0$ | DERIVED |
| Zero-mode subtraction | $\Delta B_\mathrm{zero}$ | $0$ | DERIVED |
| Curvature ($\xi=0$) | $\Delta B_\mathrm{curv}$ | $0$ | DERIVED |
| Torsion (bosonic) | $\Delta B_\mathrm{tors}$ | $0$ | DERIVED |
| Torus shape ($\epsilon=0$) | $\Delta B_\mathrm{shape}$ | $0$ | CONDITIONAL |
| **Best total** | $B_\mathrm{best}$ | $\approx 43.6$ | HEURISTIC |
| **Range minimum** | $B_\mathrm{min}$ | $8\pi \approx 25.1$ | CONDITIONAL |
| **Range maximum** | $B_\mathrm{max}$ | $\approx 50.6$ | HEURISTIC |
| **Phenomenological target** | $B \approx 46$ | — | INPUT: compared at end |
| **Gap** | $\Delta B = B - B_\mathrm{best}$ | $\approx 2.4$ | OPEN |

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
| T-duality doubles $B$ | ⚠️ HEURISTIC |
| $B_\mathrm{best} \approx 43.6$ | ⚠️ HEURISTIC |
| Gap $\Delta B \approx 2.4$ explained | ❌ OPEN |
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
| Modular ansatz $B(p)=(p+1)/3$ | Not derived from $S[\Theta]$ (Obstruction O1 blocked) |
| Hecke path integral | No-go (O1, O2, O3 unresolved); see `reports/hecke_path_integral_no_go_or_success.md` |

---

## 5. Surviving Route

**The single surviving derivation chain** that reaches closest to $B \approx 46$:

$$B_\mathrm{best}
= \underbrace{B_0}_{\text{one-loop, COND}}
+ \underbrace{\Delta B_\mathrm{wind}}_{\text{T-dual, HEUR}}
+ \underbrace{\Delta B_\mathrm{2-loop}}_{\text{negligible}}
\approx 25.1 + 18.5 + 0.05 = 43.65.$$

**All conditions required**:
1. Self-dual radius $R_\psi = 1$ (not derived, assumed).
2. T-duality at $R_\psi = 1$ doubles winding contribution (standard string result, applied heuristically).
3. Factor $2\pi$ from KK compactification matching (conditional).

**Remaining gap**: $\Delta B \approx 2.4$ (5.2%) is unaccounted by any identified mechanism.

---

## 6. Comparison to Structural Values

| Value | Relation to $B_\mathrm{best}$ | Relation to target 46 | Comment |
|-------|-------------------------------|----------------------|---------|
| $8\pi \approx 25.133$ | $= B_\mathrm{min}$ | $-45\%$ | One-loop only |
| $12^{3/2} \approx 41.57$ | $< B_\mathrm{best}$ | $-9.6\%$ | No mechanism |
| $46$ | $B_\mathrm{best} + 2.4$ | $+5.2\%$ from $B_\mathrm{best}$ | Target |
| $B_\mathrm{best} \approx 43.6$ | — | $-5.2\%$ | Best current estimate |

---

## 7. Final Verdict

$$\boxed{\text{B≈46 is conditionally reachable but not proved.}}$$

**Supporting facts**:
- $B \approx 46$ lies within the uncertainty range $[25.1, 50.6]$ derived from
  perturbative corrections.
- The best estimate $B_\mathrm{best} \approx 43.6$ is obtained from a
  CONDITIONAL + HEURISTIC chain; it reaches to within 5.2% of the target.
- No perturbative correction accounts for the remaining gap $\Delta B \approx 2.4$.
- The $N_\mathrm{eff} = 12$ mode count is rigorously proved and independent of
  any experimental input.

**Open gaps preventing PROVED status**:
1. $R_\psi = 1$ (self-dual radius) is not derived from the UBT moduli problem.
2. The factor $2\pi$ in $B_0 = 8\pi$ requires explicit 5D→4D coupling matching.
3. The winding correction $\Delta B_\mathrm{wind}$ requires T-duality at $R_\psi = 1$
   (depends on gap 1).
4. The residual $\Delta B \approx 2.4$ has no identified perturbative source.

**Recommended next step** (if RG/mode-counting insufficient):
→ Full Modular Covariance Route (prove $\mathrm{SL}(2,\mathbb{Z})$ invariance of $S[\Theta]$;
see `reports/B46_next_path_if_no_go.md`).

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
