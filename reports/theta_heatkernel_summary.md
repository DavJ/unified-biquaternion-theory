<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Theta/Heat-Kernel Program Summary

**Task**: Task 4 — Theta / Heat-Kernel / Trace Formula Program  
**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Priority**: HIGH  

---

## Executive Summary

The theta/heat-kernel programme has established a rigorous mathematical
framework connecting:

1. **[PROVED]** Jacobi theta functions and modular transformations.
2. **[PROVED]** Heat kernel on $S^1$ and its theta-function representation.
3. **[PROVED]** Spectral zeta function = $\zeta_R(2s)$ (free case).
4. **[PROVED]** Functional equation of $\zeta_H$ (free case).
5. **[PROVED]** Selberg trace formula (in the literature).
6. **[PROVED]** Riemann–Weil explicit formula (in the literature).
7. **[SPECULATIVE]** UBT-specific modular structures and trace formulas.

---

## Files Created

| File | Contents |
|------|----------|
| `research_tracks/theta_spectral/theta_kernel_foundations.tex` | Heat kernel, theta function, spectral zeta, functional equation, modular transformation, Weyl law, zeta regularisation |
| `research_tracks/theta_spectral/trace_formula_connections.tex` | Selberg trace formula, Riemann–Weil explicit formula, Atiyah–Bott, spectral determinant, UBT gaps |
| `research_tracks/theta_spectral/modular_spectrum.md` | Modular forms, Hecke operators, UBT modular structure, spectral density |

---

## Core Results (Standard Mathematics)

### Heat kernel on $S^1$

$$K_t(\psi, \psi') = \frac{1}{L}\vartheta_3\!\left(\frac{\psi-\psi'}{L}\,\bigg|\,\frac{4\pi it}{L^2}\right)$$

**[PROVED]**

### Heat trace = theta function

$$Z_H(t) = \theta_3(4\pi it/L^2)$$

**[PROVED]**

### Spectral zeta function

$$\zeta_H(s) = 2(L/2\pi)^{2s} \zeta_R(2s)$$

**[PROVED]**

### Functional equation

$$\Xi_H(s) = \Xi_H(1/2 - s), \qquad \Xi_H(s) = \pi^{-s}\Gamma(s)\zeta_H(s)$$

**[PROVED]** (free case via modular transformation of $\theta_3$)

---

## UBT-Specific Status

### What generates UBT theta structures

The UBT field $\Theta(q, \tau)$ with $\tau = t + i\psi$ lives in the
upper half-plane $\mathbb{H}$ (for $\psi > 0$, $t \in \mathbb{R}$).
The free-field heat trace is $Z_H(t) = \theta_3(4\pi it)$ — a modular form.

**[SPECULATIVE]**: Whether the full UBT $\Theta(q,\tau)$ transforms as a
modular form under $\tau \to -1/\tau$.

### Does UBT generate trace formulas

**[SPECULATIVE]**: A Selberg-type trace formula for UBT would require
identifying the "closed geodesics" in the UBT geometry.  Candidate:
winding modes with lengths $\ell_n = nL_\psi$, or prime-indexed orbits
with $\ell_p = \ln p$.

If $\ell_p = \ln p$: the geometric side would involve $\sum_p \hat{h}(k\ln p)$,
matching the Riemann–Weil formula.  **This must be derived, not assumed.**

### Does UBT generate spectral densities and modular spectra

**[OPEN GAP]**: Requires computation of $V_\text{eff}$ and the perturbed spectrum.

---

## Open Gaps

| Gap | Description | Difficulty |
|-----|-------------|------------|
| G-T1 | Derive $\Theta_\text{UBT}(\psi,t)$ as a theta function | Hard |
| G-T2 | Establish modular transformation of UBT field | Hard |
| G-T3 | Identify UBT "prime orbits" in trace formula | Very Hard |
| G-T4 | Connect UBT Selberg formula to Riemann–Weil | Very Hard |
| G-T5 | Compute spectral density from $V_\text{eff}$ | Moderate |

---

## Selberg vs. Riemann–Weil: Structural Analogy

| Selberg | Riemann–Weil | UBT candidate |
|---------|-------------|----------------|
| $\lambda_n$ of $\Delta_\Sigma$ | $\rho_n - 1/2$ of $\zeta(s)$ | $\lambda_n$ of $\hat{H}_\psi$ |
| $\ell(\gamma)$ geodesics | $\ln p$ primes | ? (winding or prime orbits) |
| $\text{Area}(\Sigma)$ | $\ln\pi^{1/2}$ | $L_\psi$ |
| Hyperbolic surface | Riemann surface | UBT moduli |

The analogy is structurally suggestive but currently **[SPECULATIVE]**.

---

## Connection to Other Tasks

- **Task 1 (Operator)**: The heat trace $Z_H(t)$ is the Laplace transform of
  the spectral density; self-adjointness of $\hat{H}_\psi$ guarantees the trace is well-defined.
- **Task 2 (RG)**: The $\ln n$ in $V_\text{eff}$ enters the spectral zeta as a
  perturbation of $\zeta_R(2s)$.
- **Task 3 (Prime Stability)**: If stable primes correspond to "prime orbits,"
  the Selberg formula would connect their stability windows to spectral gaps.

---

**Last Updated**: 2026-05-06
