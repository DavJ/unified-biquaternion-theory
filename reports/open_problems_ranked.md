<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Open Problems Ranked: UBT Spectral/RG Framework

**Author**: Ing. David Jaroš  
**Date**: May 2026  

---

> Problems are ranked by: (1) impact on the overall programme if solved,
> (2) feasibility of solution with current tools, and (3) logical priority
> (must be solved before other problems).

---

## Tier 1: Blocking Problems (Must Be Solved First)

### Problem P1: Derive $V_\text{eff}(\psi)$ from UBT Lagrangian

**Status**: Open gap  
**Impact**: CRITICAL — blocks T1 (operator), T4 (theta), and validates T2 (RG)  
**Difficulty**: Hard  
**Approach**: 
1. Fix a background solution $\Theta_0(q)$ (e.g., the lowest KK mode).
2. Compute $\langle\Theta^\dagger\Theta\rangle_q = \int |\Theta_0(q)|^2 d^4q$ (spatial average).
3. This gives $V_\text{eff}(\psi) = \kappa \langle\Theta^\dagger\Theta\rangle_q|_\psi$.
**Falsification**: If $V_\text{eff}$ diverges or is not in $L^2$, the operator programme collapses.

---

### Problem P2: Derive $B = 46$ from First Principles

**Status**: FAILING — current best estimate $B \approx 43.6$ (5.2% below target)  
**Impact**: CRITICAL — the prime-stability/RG connection is unvalidated  
**Difficulty**: Hard  
**Approach**:
1. Compute two-loop diagrams for the UBT KK effective potential.
2. Include gauge field and ghost contributions.
3. Derive the threshold corrections at the compactification scale.
**Falsification**: If complete two-loop + gauge gives $B \notin [45, 47]$, the RG origin of $B$ is disproved.

---

### Problem P3: Derive compactification radius $L_\psi$ from UBT moduli

**Status**: Open gap  
**Impact**: HIGH — $L_\psi$ sets the spectral scale; currently assumed to be $2\pi$  
**Difficulty**: Medium-hard  
**Approach**: Study the UBT moduli space; identify the vacuum expectation value of the metric in the $\psi$-direction.  
**Falsification**: If UBT has no compact $\psi$-direction, the entire $\hat{H}_\psi$ programme collapses.

---

## Tier 2: High-Priority Open Problems

### Problem P4: Nearest-Prime Dominance (Analytic Proof)

**Status**: Heuristic (numerical only)  
**Impact**: HIGH — all stability window formulas rely on this  
**Difficulty**: Medium  
**Approach**: Prove $f'(q) < 0$ for $f(q) = (p^2-q^2)/(p\ln p - q\ln q)$ and $q < p$.  
**Required**: Estimate $\frac{d}{dq}\left[\frac{p^2-q^2}{p\ln p - q\ln q}\right] < 0$ for $1 < q < p$.

---

### Problem P5: Modular Transformation of UBT Field

**Status**: Speculative  
**Impact**: HIGH — enables theta/modular connection  
**Difficulty**: Very Hard  
**Approach**: Compute how $\Theta(q, -1/\tau)$ relates to $\Theta(q, \tau)$ using the UBT field equations.  
**Prerequisite**: P1 (needs explicit $V_\text{eff}$ hence $\Theta$).

---

### Problem P6: UBT Prime Orbits in Trace Formula

**Status**: Speculative  
**Impact**: HIGH — would connect prime-stability to spectral theory  
**Difficulty**: Very Hard  
**Approach**: Identify geometric objects in UBT with lengths $\ell = \ln p$ for primes $p$.  
**Prerequisite**: P5 (modular structure), P1 ($V_\text{eff}$).

---

### Problem P7: No Stable Prime Above $10^6$ (Asymptotic Proof)

**Status**: Proved computationally up to $10^6$; asymptotic argument is approximate  
**Impact**: MEDIUM — completes finiteness proof  
**Difficulty**: Medium  
**Approach**: Prove $B_\text{high}(p) < B(p)$ for all $p > 157$ using exact prime-gap bounds.  
**Tools**: Bertrand's postulate; explicit prime-gap results (Baker, Harman, Pintz).

---

## Tier 3: Medium-Priority Open Problems

### Problem P8: Explanation of Factor 1.054

The ratio $B(p)/B_\text{KK+wind}(p) \approx 1.054$ is constant across stable primes.
Origin unknown.

**Difficulty**: Medium-hard  
**Approach**: Check if 1.054 arises from a specific group-theory factor, normalisation
convention, or non-perturbative effect.

---

### Problem P9: Two-Loop Beta Function for UBT KK Tower

**Status**: Not computed  
**Difficulty**: Hard (requires UBT coupling constants)  
**Impact**: MEDIUM — needed for P2

---

### Problem P10: Spectral Rigidity $\Delta_3(L)$ for UBT Operator

**Status**: Known for free case (perfectly rigid); open for perturbed case  
**Difficulty**: Medium  
**Approach**: Numerically compute $\Delta_3(L)$ after deriving $V_\text{eff}$ (P1).

---

## Tier 4: Low-Priority / Long-Term Problems

### Problem P11: Adelic Structure of UBT

Whether the UBT $\psi$-sector Hamiltonian has an adelic factorisation
(analogous to Tate's thesis) — required for Gaps G3-G5 in `rh_trace_formula/`.

**Difficulty**: Extremely Hard  
**Prerequisite**: P5, P6.

---

### Problem P12: Nonvanishing of $G(s)$ Factor

The correction factor $G(s)$ in $\zeta_H(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)G(s)$
must be shown holomorphic and nonvanishing — required for Gap G5.

**Difficulty**: Extremely Hard  
**Prerequisite**: P2, P5, P11.

---

## Summary Ranking Table

| Rank | Problem | Impact | Difficulty | Tier |
|------|---------|--------|------------|------|
| 1 | P1: $V_\text{eff}$ from Lagrangian | Critical | Hard | Blocking |
| 2 | P2: $B = 46$ derivation | Critical | Hard | Blocking |
| 3 | P3: $L_\psi$ from moduli | High | Medium | Blocking |
| 4 | P4: Nearest-prime dominance proof | High | Medium | High |
| 5 | P5: Modular structure of UBT | High | Very Hard | High |
| 6 | P6: Prime orbits in trace formula | High | Very Hard | High |
| 7 | P7: No stable prime > $10^6$ | Medium | Medium | High |
| 8 | P8: Factor 1.054 origin | Medium | Medium | Medium |
| 9 | P9: Two-loop beta function | Medium | Hard | Medium |
| 10 | P10: Spectral rigidity $\Delta_3$ | Low-Medium | Medium | Medium |
| 11 | P11: Adelic structure | Low | Extreme | Long-term |
| 12 | P12: $G(s)$ nonvanishing | Low | Extreme | Long-term |

---

**Last Updated**: 2026-05-06  
**Companion reports**: `top5_master_summary.md`, `proof_dependency_graph.md`
