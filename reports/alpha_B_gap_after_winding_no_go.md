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


# Alpha Program: B-Gap Analysis after Winding NO-GO

**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Task**: `update_B46_status_after_winding_no_go`  
**Priority**: CRITICAL  
**Mode**: status_correction_no_new_theory

---

## 1. Context

The winding NO-GO result (`reports/t_dual_winding_verdict.md`) removes the
constant $\Delta B_\mathrm{wind} \approx 18.5$ from the list of usable corrections.
This document states the updated B-gap status for the alpha program.

---

## 2. Pre-NO-GO vs Post-NO-GO Comparison

| Quantity | Pre-NO-GO | Post-NO-GO |
|---------|-----------|------------|
| Strongest safe coefficient | $B_0 = 8\pi \approx 25.133$ (CONDITIONAL) | $B_0 = 8\pi \approx 25.133$ (CONDITIONAL) — unchanged |
| "Best estimate" $B_\mathrm{best}$ | $\approx 43.6$ (HEURISTIC) | **OBSOLETE HEURISTIC — withdrawn** |
| Winding correction | $\Delta B_\mathrm{wind} \approx 18.5$ (HEURISTIC) | **NO-GO** — n-dependent: $\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}n/(12\pi^2)$ |
| Gap to target (from $B_\mathrm{best}$) | $\Delta B \approx 2.4$ (5.2%) | Not applicable — $B_\mathrm{best}$ is withdrawn |
| Gap to target (from $B_0$) | $\approx 20.9$ (45%) | $\approx 20.9$ (45%) — fully open |
| Alpha status | NOT DERIVED | **NOT DERIVED** |
| B≈46 program verdict | NUMERICALLY PLAUSIBLE | **OPEN** |

---

## 3. Structure of the Remaining Gap

From $B_0 = 8\pi$, the gap to the phenomenological target is:

$$\Delta B_\mathrm{gap} = B_\mathrm{phenom} - B_0 \approx 46.298 - 25.133 = 21.165.$$

No safe perturbative mechanism is known to account for this gap:

| Mechanism | Contribution | Status |
|-----------|-------------|--------|
| Two-loop RG | $\lesssim 0.05$ | PLAUSIBLE but negligible |
| KK threshold tower | $\approx 13.9$ | PLAUSIBLE — does not close gap alone |
| Constant winding correction | $\approx 18.5$ | **NO-GO** |
| n-dependent winding $\Delta B_\mathrm{wind}(n)$ | Produces $n^2\ln n$ term | PROVED — not a constant $B$ shift |
| Ghost determinant | 0 | DERIVED |
| Curvature ($\xi = 0$) | 0 | DERIVED |
| Torus shape | 0 (at $\epsilon = 0$) | CONDITIONAL |
| **Total safe sum** | $\leq 8\pi + 13.9 \approx 39.0$ | PLAUSIBLE — falls short of 46 |

---

## 4. What the Winding NO-GO Actually Delivers

The derived formula

$$\Delta B_\mathrm{wind}(n) = \frac{N_\mathrm{eff}\,n}{12\pi^2}$$

is a genuine result: it quantifies the winding-sector contribution to the
effective potential at each KK level $n$.  However, it modifies the
**structure** of $V_\mathrm{eff}$, not the constant $B$:

$$V_\mathrm{eff}(n) \to n^2 - B_0\,n\ln n - \frac{N_\mathrm{eff}\,n}{12\pi^2}\,n\ln n
= n^2 - \left(B_0 + \frac{N_\mathrm{eff}\,n}{12\pi^2}\right)n\ln n.$$

The effective "B-coefficient" becomes $n$-dependent: $B_\mathrm{eff}(n) = B_0 + N_\mathrm{eff}n/(12\pi^2)$.
This is a different structure than $V_\mathrm{eff}(n) = n^2 - B\,n\ln n$ with constant $B$.
It does **not** provide a derivation of constant $B \approx 46$.

---

## 5. Alpha Program Gap Summary

| Gap | Description | Status |
|-----|-------------|--------|
| G137-B (main) | Derive constant $B \approx 46.298$ from $S[\Theta]$ without fitting | **OPEN — fully open after winding NO-GO** |
| G137-KK | Prove factor $2\pi$ in $B_0 = 8\pi$ from 5D→4D coupling matching | **OPEN** |
| G137-R | Derive self-dual radius $R_\psi = 1$ from UBT moduli problem | **OPEN** |
| G137-MOD | Prove $S[\Theta]$ invariant under $\mathrm{SL}(2,\mathbb{Z})$ (Obstruction O1) | **OPEN** |

---

## 6. Hard Rules Reaffirmed

- No new derivation is introduced here.
- No new constants are introduced.
- No eta(i) revival.
- No Hecke revival (Obstruction O1 unresolved).
- B≈46 remains open.
- Alpha remains not derived.

---

## 7. Recommended Next Steps

Priority order for closing Gap G137-B (see `reports/B46_next_path_if_no_go.md`):

| Priority | Route | Blocker |
|----------|-------|---------|
| 1 | Full Modular Covariance | Obstruction O1: prove $S[\Theta]$ modular-invariant |
| 2 | Spectral Operator (heat kernel) | Spectral theory of $\nabla^\dagger\nabla$ on UBT background |
| 3 | Nonperturbative Saddle | Existence of equal-action instantons not established |
| 4 | Trace Formula | Connection to constant $B$ not established |

---

## 8. Cross-References

| Document | Role |
|----------|------|
| `reports/t_dual_winding_verdict.md` | Source of the NO-GO result |
| `reports/B46_master_verdict.md` | Master verdict (updated) |
| `reports/B46_master_verdict_updated.md` | Updated master verdict (new deliverable) |
| `reports/B46_RG_decision_report.md` | RG decision report (updated) |
| `reports/B46_next_path_if_no_go.md` | Replacement paths (updated) |
| `reports/alpha_current_verdict.md` | Alpha program verdict (updated) |
| `canonical/alpha/ALPHA_MASTER_STATUS.md` | Alpha master status (updated) |
| `reports/alpha_missing_lemma.md` | Exact formulation of Gap G137-B |
