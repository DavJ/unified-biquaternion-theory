<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Operator Program Status Report

**Task**: Task 1 — Self-Adjoint Operator / Hilbert–Pólya Program  
**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Priority**: CRITICAL  

---

## Executive Summary

The UBT Hilbert–Pólya operator programme has established the following:

- **[PROVED]** The Hilbert space $\mathscr{H}_\psi = L^2(S^1_{2\pi})$ is well-defined.
- **[PROVED]** The free Hamiltonian $A_0 = -d^2/d\psi^2$ is self-adjoint with discrete spectrum $\{n^2 : n \in \mathbb{Z}\}$.
- **[PROVED]** If $V_\text{eff} \in L^2(S^1)$, then $\hat{H}_\psi = A_0 + V_\text{eff}$ is self-adjoint by Kato–Rellich.
- **[HEURISTIC]** The UBT compactification radius $L_\psi = 2\pi$ (not derived from moduli).
- **[OPEN GAP]** $V_\text{eff}$ has not been computed from the UBT Lagrangian.
- **[SPECULATIVE]** Any connection to the Riemann zeros.

---

## Files Created

| File | Contents | Status |
|------|----------|--------|
| `research_tracks/rh_operator/operator_definition.tex` | Hilbert space, operator definition, Sturm-Liouville form, open gaps | Complete |
| `research_tracks/rh_operator/selfadjointness_attempt.tex` | Kato-Rellich, deficiency indices, Friedrich's extension, Weyl criterion | Complete |
| `research_tracks/rh_operator/spectral_statistics.md` | Spacing distributions, comparison with GUE/Poisson/Riemann zeros | Complete |

---

## Proof Status Matrix

| Claim | Status | Condition |
|-------|--------|-----------|
| $\mathscr{H}_\psi = L^2(S^1)$ is Hilbert space | **PROVED** | None |
| $A_0$ self-adjoint on $H^2_\text{per}$ | **PROVED** | None |
| KR: $V \in L^\infty \Rightarrow$ self-adjoint | **PROVED** | $V \in L^\infty$ |
| KR: $V \in L^2 \Rightarrow$ self-adjoint | **PROVED** | $V \in L^2$ |
| Deficiency indices $(0,0)$ | **PROVED** | $V \in L^2$ |
| Friedrich's extension | **PROVED** | $V$ semibounded |
| $V_\text{eff}$ from UBT Lagrangian | **OPEN GAP** | Requires computation |
| $L_\psi$ from UBT moduli | **OPEN GAP** | Requires moduli derivation |
| Spectrum $\sim$ Riemann zeros | **SPECULATIVE** | Gaps G1-G6 all open |

---

## Critical Open Gaps

### Gap 1: Derivation of $V_\text{eff}$ from UBT Lagrangian

**What is needed**: Integrate the UBT field equations over the spatial biquaternion
directions $q$ to obtain $V_\text{eff}(\psi) = \kappa\langle\Theta^\dagger\Theta\rangle_q|_\psi$.

**Difficulty**: High — requires a known background solution $\Theta_0(q)$ and
controlled approximation (e.g., weak-field expansion).

**Impact**: All self-adjointness results are conditional on $V_\text{eff} \in L^2$.

### Gap 2: Self-adjointness verification

Once $V_\text{eff}$ is computed, verify $V_\text{eff} \in L^2(S^1)$.
Apply Kato-Rellich theorem.  This will then be **PROVED** (unconditionally).

### Gaps G1-G6 (from `rh_trace_formula/gap_inventory.md`)

All six gaps (self-adjointness, heat trace, adelic factorization, local Euler
factors, G(s) nonvanishing, explicit formula) remain **open**.

---

## Spectral Statistics: Preliminary Findings

The **free operator** ($V_\text{eff} = 0$) has:
- Spectrum $\lambda_n = n^2$ — perfectly regular spacing (not GUE).
- KS distance to Poisson: large (uniform spacing, not exponential).
- KS distance to GUE: large (no level repulsion in the right sense).

**Conclusion**: A non-trivial $V_\text{eff}$ breaking the regular spacing is
necessary before GUE statistics could emerge.

---

## Comparison with Known Candidate Operators

| Candidate | Hilbert space | Self-adjoint? | Spectrum |
|-----------|--------------|---------------|---------|
| Berry-Keating $H = xp$ | $L^2(\mathbb{R}^+)$ | Requires regularisation | Conjectured ↔ zeros |
| Connes adelic | $L^2(\mathbb{A}/\mathbb{Q}^*)$ | Yes | Conjectured ↔ zeros |
| UBT $\hat{H}_\psi$ (free) | $L^2(S^1)$ | **Proved** | $n^2$ — not zeros |
| UBT $\hat{H}_\psi$ (with $V$) | $L^2(S^1)$ | Conditional | Unknown |

---

## Next Steps (Priority Order)

1. **Derive $V_\text{eff}(\psi)$** from UBT Lagrangian (highest priority).
2. Verify $V_\text{eff} \in L^2$ and apply Kato-Rellich.
3. Compute the perturbed spectrum numerically (diagonalise on grid).
4. Compare spacing statistics with Riemann zeros.
5. If GUE-like: proceed to heat-trace and adelic factorization (Gaps G2-G6).

---

## Risk Assessment

| Risk | Probability | Impact |
|------|-------------|--------|
| $V_\text{eff}$ is not in $L^2$ | Medium | Would require Friedrich's extension |
| $V_\text{eff}$ is not computable analytically | High | Use numerical approximation |
| Spectrum does not match Riemann zeros | High | Entire programme collapses |
| Program proves too general (any $V$ works) | Medium | Loss of predictive power |

---

**Last Updated**: 2026-05-06
