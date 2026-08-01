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


# B46 Master Verdict — Updated after Winding NO-GO

**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Task**: `update_B46_status_after_winding_no_go`  
**Priority**: CRITICAL  
**Mode**: status_correction_no_new_theory  
**Supersedes**: `reports/B46_master_verdict.md` (now also updated in place)

---

## Purpose

This document records the authoritative status correction for the B≈46 program
after the NO-GO result for the constant T-dual winding correction.  It supersedes
all claims of $B_\mathrm{best} \approx 43.6$ as a best estimate.

---

## Summary of NO-GO Result

The task `prove_or_reject_T_dual_winding_correction` (see `reports/t_dual_winding_verdict.md`)
established:

> The constant winding correction $\Delta B_\mathrm{wind} \approx 18.5$ is **NO-GO**.

**What was claimed** (old, now withdrawn):

$$B_\mathrm{best} = B_0 + \Delta B_\mathrm{wind} \approx 25.1 + 18.5 = 43.6 \quad [\text{HEURISTIC}]$$

**What is actually derived** (no fitting, no circular input):

$$\Delta B_\mathrm{wind}(n) = \frac{N_\mathrm{eff}\,n}{12\pi^2}$$

This expression is **$n$-dependent**.  Inserting it into $V_\mathrm{eff}$ produces
an additional $n^2 \ln n$ term, not a constant shift of the $n \ln n$ coefficient:

$$V_\mathrm{eff}(n) = n^2 - B_0\,n\ln n - \Delta B_\mathrm{wind}(n)\,n\ln n
= n^2 - \left(B_0 + \frac{N_\mathrm{eff}\,n}{12\pi^2}\right)n\ln n.$$

The quantity $B_0 + \Delta B_\mathrm{wind}(n)$ is not a universal constant B;
it is a function of $n$.  Using it as a constant requires fixing $n$, which is
circular if the target $n^* = 137$ is used as input.

---

## Claim Status Table

| Claim | Old Status | New Status |
|-------|-----------|------------|
| $N_\mathrm{eff} = 12$ | PROVED | PROVED (unchanged) |
| $b_0 = 4$ | PROVED | PROVED (unchanged) |
| $n\ln n$ shape from one-loop | PROVED | PROVED (unchanged) |
| $B_0 = 8\pi$ (one-loop) | CONDITIONAL | CONDITIONAL (unchanged) |
| $\Delta B_\mathrm{wind} \approx 18.5$ (constant) | HEURISTIC | **NO-GO** |
| $\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}n/(12\pi^2)$ | (not stated) | **PROVED** (n-dependent) |
| $B_\mathrm{best} \approx 43.6$ | HEURISTIC | **OBSOLETE HEURISTIC** |
| $B_\mathrm{max} \approx 50.6$ | HEURISTIC | **OBSOLETE HEURISTIC** |
| $B \approx 46$ in safe derivation range | NUMERICALLY PLAUSIBLE | **OPEN — not plausible from current derivation** |
| Alpha derived | NOT DERIVED | NOT DERIVED (unchanged) |
| B≈46 program | CONDITIONAL | **OPEN** |

---

## Correct Status After Update

| Quantity | Value | Status |
|---------|-------|--------|
| One-loop baseline | $B_0 = 8\pi \approx 25.133$ | CONDITIONAL on KK matching |
| Strongest safe coefficient | $B_0 = 8\pi$ | CONDITIONAL — the only safe claim |
| Winding correction (derived) | $\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}n/(12\pi^2)$ | PROVED (n-dependent) |
| $B_\mathrm{best} \approx 43.6$ | — | OBSOLETE HEURISTIC — withdrawn |
| $B \approx 46$ | — | OPEN — not derived |
| Alpha | — | NOT DERIVED |

---

## Hard Rules Reaffirmed

- No new derivation introduced by this status update.
- No new constants introduced.
- No eta(i) revival.
- No Hecke revival (modular covariance not proved).
- B≈46 remains open.

---

## Cross-References

| Document | Role |
|----------|------|
| `reports/t_dual_winding_verdict.md` | Source of the NO-GO result |
| `reports/B46_master_verdict.md` | Master verdict (updated in place) |
| `reports/B46_RG_decision_report.md` | RG decision report (updated in place) |
| `reports/B46_next_path_if_no_go.md` | Replacement paths (updated in place) |
| `reports/alpha_current_verdict.md` | Alpha program verdict (updated in place) |
| `canonical/alpha/ALPHA_MASTER_STATUS.md` | Alpha master status (updated in place) |
| `reports/alpha_B_gap_after_winding_no_go.md` | B-gap analysis after NO-GO (new) |
