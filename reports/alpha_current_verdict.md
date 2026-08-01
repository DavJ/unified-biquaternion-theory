<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# alpha_current_verdict.md — Current Alpha Program Verdict

**Date**: 2026-05-09  
**Track**: T3_ALPHA  
**Priority**: CRITICAL

---

## Canonical potential (fixed)

\[
V_{\mathrm{eff}}(n)=n^2-B\cdot n\ln n
\]

Legacy forms without the multiplicative `n` are deprecated and not valid for active claims.

---

## Current verdict (authoritative)

| Item | Verdict |
|---|---|
| alpha derived from first principles | **NO** |
| prime-stability set derived | **YES** |
| B-gap status | **OPEN** (fully open after winding NO-GO) |
| eta(i) route | **REJECTED** as first-principles B-modifier; allowed only as numerical observation / partition-normalization clue |
| Hecke path-integral route | **NO-GO at current level** |
| Constant winding correction ΔB_wind ≈ 18.5 | **NO-GO** — derived correction is n-dependent: ΔB_wind(n) = N_eff·n/(12π²); produces n²·ln n term, not constant B shift |
| B_best ≈ 43.6 | **OBSOLETE HEURISTIC** — based on NO-GO winding step |
| Current strongest safe coefficient | **B₀ = 8π** (conditional on KK matching) |

### Canonical wording lock

UBT currently provides a conditional structural route to the bare integer alpha
inverse alpha_bare^{-1} = 137 through a prime winding-mode attractor,
conditional on deriving the effective coupling B ≈ 46.284–46.298 from the UBT
action. This unresolved step is Gap G137-B. The physical correction from 137
to 137.036 is not yet derived from first principles.

---

## Route policy constraints

1. No claim of alpha derivation until B is derived from `S[Θ]` without circular input.
2. eta(i) is **rejected as first-principles B-modifier** and cannot be used as canonical closure.
3. eta(i) may be referenced only as:
   - a numerical observation, or
   - a partition-function normalization clue.
4. Hecke path-integral remains classified as no-go under current proof state.
5. No claim is permitted that eta(i) derives alpha or that alpha is solved.
6. **Constant winding correction ΔB_wind ≈ 18.5 is NO-GO.** The derived winding term
   is n-dependent: ΔB_wind(n) = N_eff·n/(12π²). It cannot be cited as a constant B shift.
7. **B_best ≈ 43.6 is OBSOLETE HEURISTIC.** No claim may reference it as an estimate.
8. The current strongest safe coefficient is **B₀ = 8π** (CONDITIONAL on KK matching).
   It may be cited as such.

---

## Self-dual torus synchronization note

- `tau=i` / `R_t=R_ψ` remains **CONDITIONAL**.
- Shape mode is stationary and locally stable (under explicit assumptions).
- Scale modulus `sqrt(R_t R_ψ)` remains unfixed.
- Therefore this does not provide unconditional alpha closure.

---

## Deprecated / rejected claims

- Rejected as derived first-principles n log n coefficient:
  `B = 12^(3/2)*(2 eta(i))^(1/4)`.

---

## Cross-reference anchors

- `reports/hecke_path_integral_no_go_or_success.md`
- `reports/hecke_trace_B_verdict.md`
- `reports/t_dual_winding_verdict.md`
- `reports/alpha_B_gap_after_winding_no_go.md`
- `canonical/alpha/ALPHA_MASTER_STATUS.md`
