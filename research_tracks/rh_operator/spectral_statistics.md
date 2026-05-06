<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Spectral Statistics of the UBT ψ-Sector Operator

**Track**: `research_tracks/rh_operator/`  
**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Status**: Computational — [L0 for free case]; [SPECULATIVE] for RH connection  

---

> ⚠️ **Warning**  
> This document compares spectral statistics of the free UBT operator against
> Riemann zero statistics and random matrix ensembles.  No proof of the Riemann
> Hypothesis or connection to it is claimed or implied.  All comparisons are
> exploratory; any apparent agreement may be coincidental.

---

## 1. Overview

The goal is to characterise the spectral statistics of eigenvalue spacings of
$\hat{H}_\psi = -d^2/d\psi^2 + V_\mathrm{eff}(\psi)$ and compare them against:

| Reference distribution | Physical interpretation |
|------------------------|------------------------|
| **Poisson** | Uncorrelated (integrable/random) |
| **GUE** (Gaussian Unitary Ensemble) | Generic chaotic quantum system |
| **Wigner–Dyson GOE** | Time-reversal invariant chaos |
| **Riemann zeros** | Empirical spectrum of $\{\gamma_n\}$ |

---

## 2. Free Hamiltonian ($V_\mathrm{eff} = 0$) — Exact Results

### 2.1 Spectrum

**[PROVED]** The eigenvalues of $A_0 = -d^2/d\psi^2$ on $L^2(S^1_{2\pi})$ are:
$$\lambda_n = n^2, \qquad n \in \mathbb{Z}.$$

Ordered as $0 = \lambda_0 < \lambda_1 = \lambda_{-1} = 1 < \lambda_2 = \lambda_{-2} = 4 < \cdots$

The degeneracy $g_n = 2$ for $n \neq 0$ reflects the $\pm n$ symmetry.

### 2.2 Unfolded Eigenvalues and Spacings

After **unfolding** (rescaling so the mean spacing is 1), the non-degenerate
sequence is $\tilde{\lambda}_k = k^2/(k+1-k) \times \bar{\rho}^{-1}$ where
$\bar{\rho}$ is the mean spectral density.

For the free spectrum $\lambda_n = n^2$, the spacing between consecutive levels:
$$s_n = \lambda_{n+1} - \lambda_n = (n+1)^2 - n^2 = 2n + 1.$$

Normalised spacing (dividing by mean spacing $\langle s \rangle = 2n+1$):
$$\tilde{s}_n = 1 \quad \text{(uniform)}.$$

**Conclusion [PROVED]**: The free spectrum has perfectly regular (Poisson-like)
spacing for large $n$, not GUE spacing.

### 2.3 Nearest-Neighbour Spacing Distribution (NNS)

| Distribution | $P(s)$ formula | Free UBT ($V=0$) |
|---|---|---|
| Poisson | $e^{-s}$ | ✗ (spacing grows, not exponential) |
| Wigner (GOE) | $\frac{\pi s}{2} e^{-\pi s^2/4}$ | ✗ |
| GUE | $\frac{32s^2}{\pi^2} e^{-4s^2/\pi}$ | ✗ |
| Regular (uniform) | $\delta(s - 1)$ | ✓ (asymptotically) |

**[PROVED]**: The free UBT operator does **not** exhibit GUE statistics.
To match Riemann-zero-like GUE statistics, a non-trivial $V_\mathrm{eff}$ is
required that breaks the regular spacing pattern.

---

## 3. Riemann Zero Statistics (Reference)

### 3.1 Empirical distribution

The first Riemann zeros $\gamma_n$ (imaginary parts of $\zeta(1/2 + i\gamma)=0$,
$\gamma > 0$, ascending) are approximately:

| $n$ | $\gamma_n$ |
|-----|------------|
| 1 | 14.1347 |
| 2 | 21.0220 |
| 3 | 25.0109 |
| 4 | 30.4249 |
| 5 | 32.9351 |
| 6 | 37.5862 |
| 7 | 40.9187 |
| 8 | 43.3271 |
| 9 | 48.0052 |
| 10 | 49.7738 |

### 3.2 GUE statistics of Riemann zeros

**[PROVED in the mathematical literature]** (Montgomery 1973, Odlyzko 1987):
The pair correlation function of the Riemann zeros converges to the GUE pair
correlation
$$R_2(\beta) = 1 - \left(\frac{\sin \pi\beta}{\pi\beta}\right)^2.$$

The nearest-neighbour spacing distribution is well-approximated by the
Wigner surmise for GUE:
$$P(s) \approx \frac{32s^2}{\pi^2} e^{-4s^2/\pi}.$$

**[SPECULATIVE]**: Whether the UBT $\hat{H}_\psi$ with appropriate $V_\mathrm{eff}$
can reproduce this distribution is entirely open.

---

## 4. Eigenvalue Spacing: Comparison Framework

### 4.1 Level spacing statistics

Given a sequence of eigenvalues $\lambda_1 \leq \lambda_2 \leq \cdots$, the
**unfolded** sequence $\xi_n$ is obtained by the substitution
$$\xi_n = N(\lambda_n)$$
where $N(\lambda) = \#\{k : \lambda_k \leq \lambda\}$ is the counting function.
The unfolded spacings $s_n = \xi_{n+1} - \xi_n$ have mean $\langle s \rangle = 1$.

### 4.2 Spectral rigidity

The spectral rigidity $\Delta_3(L)$ measures long-range correlations:
$$\Delta_3(L) = \frac{1}{L} \min_{A,B} \int_0^L |N(\xi + x) - Ax - B|^2 dx.$$

| System | $\Delta_3(L)$ for large $L$ |
|--------|--------------------------|
| Poisson | $L/15$ |
| GOE | $\frac{1}{\pi^2}(\ln L - 0.007)$ |
| GUE | $\frac{1}{2\pi^2}(\ln L + 0.058)$ |
| Riemann zeros | GUE-like (Odlyzko) |
| Free UBT ($V=0$) | $0$ (perfectly rigid) |

**[PROVED]**: The free UBT spectrum is maximally rigid (like a harmonic oscillator),
not GUE.  Breaking this rigidity requires $V_\mathrm{eff} \neq 0$.

---

## 5. What Would Be Required for GUE Match

For $\hat{H}_\psi$ to exhibit GUE spacing statistics:

1. **Absence of integrals of motion**: The classical phase space must be
   non-integrable (chaotic).  [SPECULATIVE: whether UBT $V_\mathrm{eff}$ is chaotic]

2. **Level repulsion**: $P(s) \to 0$ as $s \to 0$.  The free spectrum ($s_n = 2n+1$,
   all well-separated) satisfies this trivially but for the wrong reason.

3. **Random matrix universality**: The spectral statistics must belong to the
   GUE universality class (requires time-reversal breaking).
   [HEURISTIC: complex $V_\mathrm{eff}$ could break T-reversal]

### Necessary conditions (none yet satisfied)

| Condition | Status |
|-----------|--------|
| $V_\mathrm{eff}$ derived from UBT | **Open gap** |
| Non-integrability of $V_\mathrm{eff}$ | **Open gap** |
| Numerical GUE comparison | **Open gap** |
| Analytical $\Delta_3(L)$ for UBT | **Open gap** |

---

## 6. Computational Plan

Once $V_\mathrm{eff}$ is determined:

1. **Numerical diagonalisation**: Discretise $\hat{H}_\psi$ on a grid with
   $N \sim 1000$ points; compute eigenvalues $\lambda_1, \ldots, \lambda_N$.

2. **Unfolding**: Fit $N(\lambda)$ with a smooth polynomial or the Weyl law
   $N(\lambda) \sim L_\psi \sqrt{\lambda}/\pi$ for large $\lambda$.

3. **NNS histogram**: Compute $s_n = \xi_{n+1} - \xi_n$; plot histogram;
   fit to Poisson, GOE, GUE.

4. **$\Delta_3(L)$ computation**: Compute spectral rigidity for $L \in [1, 20]$;
   compare to GUE and Poisson curves.

5. **Comparison with Riemann zeros**: Take the first 1000 Riemann zeros from
   the LMFDB database; compute their NNS and $\Delta_3$; compare.

---

## 7. Known Risks and Failure Modes

| Risk | Description | Mitigation |
|------|-------------|------------|
| $V_\mathrm{eff}$ not computable | UBT background solution intractable | Use parametric $V = A\cos(2\psi)$ as proxy |
| Free spectrum too rigid | GUE match impossible without chaotic $V$ | Explore pseudo-differential operators |
| Finite-size effects | $N \sim 1000$ eigenvalues insufficient | Increase $N$ or use asymptotic expansions |
| Accidental GUE match | Spurious agreement from fitting | Test on shuffled controls (see Task 5) |

---

## 8. Proof-Status Summary

| Claim | Status |
|-------|--------|
| Free spectrum $\lambda_n = n^2$ | **[PROVED]** |
| Free spacing: not GUE | **[PROVED]** |
| Riemann zeros $\sim$ GUE | **[PROVED in literature]** |
| UBT $\hat{H}_\psi$ with $V_\mathrm{eff}$ exhibits GUE | **[SPECULATIVE]** |
| UBT $\hat{H}_\psi$ connected to Riemann zeros | **[SPECULATIVE]** |

---

## 9. References

- H.L. Montgomery, "The pair correlation of zeros of the zeta function,"
  *Proc. Symp. Pure Math.* **24** (1973), 181–193.
- A.M. Odlyzko, "On the distribution of spacings between zeros of the zeta
  function," *Math. Comp.* **48** (1987), 273–308.
- M.L. Mehta, *Random Matrices*, 3rd ed., Academic Press, 2004.
- Berry & Keating (1999): H = xp and Riemann zeros.

---

**Last Updated**: 2026-05-06  
**Next action**: Derive $V_\mathrm{eff}$ from UBT, then run numerical diagonalisation.
