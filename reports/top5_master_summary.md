<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Top-5 Critical Tasks: Master Summary Report

**Programme**: UBT Spectral/RG Framework — May 2026  
**Author**: Ing. David Jaroš  
**Date**: 2026-05-06  

---

> This report synthesises the results of the five critical tasks identified
> as bottlenecks to UBT's mathematical credibility as a spectral/RG framework.

---

## Task Overview

| Task | Priority | Core Goal | Status |
|------|----------|-----------|--------|
| T1: Operator Program | CRITICAL | Self-adjoint operator for Hilbert–Pólya | Framework built; $V_\text{eff}$ gap open |
| T2: RG Derivation | CRITICAL | Rigorous derivation of $n^2 - Bn\ln n$ | $n^2$ and $\ln n$ proved; $B=46$ open |
| T3: Prime Stability | HIGH | Rigorous bounds for stable set | Fully formalised; all bounds proved |
| T4: Theta/Heat-Kernel | HIGH | Bridge theta structures to spectral ops | Standard math proved; UBT-specific open |
| T5: Falsification | CRITICAL | Null-model and significance pipeline | Implemented; B=46 claim fails |

---

## Strongest Results

### 1. Prime Stability: Complete Formalization [PROVED]

The prime-stability programme is now a completely rigorous mathematical statement.

- **Stable set**: $\mathcal{S} = \{2, 127, 137, 139, 151, 157\}$ — proved computationally.
- **Exact inequalities**: Closed-form bounds on stability windows.
- **Finiteness**: Proved (asymptotic argument + numerical exhaustion).
- **Perturbation robustness**: $p = 137$ survives $|\delta B| < 0.56$.

**Significance**: This is the most mathematically complete result in UBT.

### 2. Self-Adjointness Framework [PROVED, conditional]

All self-adjointness results for $\hat{H}_\psi = -d^2/d\psi^2 + V_\text{eff}$ are proved:
- Kato–Rellich applies if $V_\text{eff} \in L^2$
- Friedrich's extension exists if $V_\text{eff}$ is semibounded
- Deficiency indices vanish if $V_\text{eff} \in L^2$

**Condition**: $V_\text{eff}$ must be computed from the UBT Lagrangian.

### 3. Heat Kernel / Theta Bridge [PROVED for free case]

Exact results:
- $Z_H(t) = \theta_3(4\pi it)$ for free operator
- Spectral zeta = $\zeta_R(2s)$ (free case)
- Functional equation of $\zeta_H$ via Jacobi modular transformation

### 4. Loop Integrals and $n^2\ln n$ Term [PROVED]

The $n^2\ln n$ coefficient in $V_\text{eff}$ is derived from standard $d=1$
one-loop QFT (Coleman–Weinberg), is scheme-independent, and is gauge-invariant.

---

## Weakest Assumptions / Biggest Gaps

### Gap 1: $V_\text{eff}$ from UBT Lagrangian [OPEN — CRITICAL]

**All** of the following depend on this gap:
- Self-adjointness of $\hat{H}_\psi$
- Heat trace $Z_H^\text{UBT}(t)$
- Spectral statistics vs. Riemann zeros
- Theta/modular structure of UBT

Until $V_\text{eff}(\psi)$ is derived from the UBT action integral, the
entire spectral programme remains conditional.

### Gap 2: $B = 46$ from RG [OPEN — CRITICAL, FAILING]

The one-loop RG gives $B \approx 43.6$ (KK+winding at self-dual radius).
The target is $B = 46$.  **Discrepancy = 2.4** (5.2%).

No mechanism currently known closes this gap.

**This is the most urgent open problem in UBT.**

### Gap 3: UBT modular structure [OPEN]

Whether $\Theta(q,\tau)$ transforms as a modular form under $\tau \to -1/\tau$
is entirely unknown.  Without this, the theta/spectral programme remains at the
level of structural analogy.

### Gap 4: Prime orbits in trace formula [SPECULATIVE]

The identification of "prime orbits" in a UBT Selberg-type trace formula
has no derivation.  The analogy with Riemann–Weil is structural only.

---

## Most Promising Directions

### Direction 1: Compute $V_\text{eff}$ numerically

Even if an analytic derivation of $V_\text{eff}$ from the UBT Lagrangian is
hard, a numerical computation (using a discretised biquaternion background field)
would close the main blocking gap.

**Impact**: Unblocks T1, T2 (partially), T4.

### Direction 2: Close the $B = 46$ gap

Two strategies:
1. **Two-loop + gauge**: Add gauge field contributions and compute two-loop
   diagrams explicitly.
2. **Modular/number-theoretic**: Explore whether $B(p) = (p+1)/3$ has a
   modular arithmetic interpretation independent of loop integrals.

**Impact**: Validates the prime-stability/RG connection; currently FAILING.

### Direction 3: Numerical spectral statistics

With a parametric $V_\text{eff}$ (even if not derived), compute the spectrum
of $\hat{H}_\psi$ numerically and compare NNS distribution to Riemann zeros.

**Impact**: Fast preliminary check; falsifies or encourages the Hilbert–Pólya programme.

---

## Proof Status Overview

| Component | Proved | Heuristic | Speculative | Open Gap |
|-----------|--------|-----------|-------------|----------|
| Hilbert space $\mathscr{H}_\psi$ | ✓ | | | |
| $A_0$ self-adjoint | ✓ | | | |
| SA of $\hat{H}_\psi$ (conditional) | ✓ cond | | | |
| Free spectrum $\lambda_n = n^2$ | ✓ | | | |
| Heat trace $= \theta_3$ (free) | ✓ | | | |
| Spectral zeta $= \zeta_R$ (free) | ✓ | | | |
| Functional equation | ✓ | | | |
| Finiteness of $\mathcal{S}$ | ✓ | | | |
| $\mathcal{S} = \{2,127,137,139,151,157\}$ | ✓ | | | |
| $V_\text{tree}(n) = n^2$ | ✓ | | | |
| 1-loop $\delta V \propto n^2\ln n$ | ✓ | | | |
| $B \approx 43.6$ (KK+winding) | | ✓ | | |
| $L_\psi$ from UBT moduli | | | | ✓ |
| $V_\text{eff}$ from UBT Lagrangian | | | | ✓ |
| $B = 46$ exact | | | | ✓ (FAILING) |
| UBT modular transformation | | | ✓ | |
| UBT trace formula | | | ✓ | |
| Spectrum $\sim$ Riemann zeros | | | ✓ | |

---

## Dependency Graph (Summary)

```
V_eff from Lagrangian ──┬──> Self-adjointness (T1)
                         ├──> Heat trace Z_H (T4)
                         └──> Spectral statistics (T1)

B = 46 derivation ──────┬──> Prime-stability (T3) validation
                         └──> RG derivation (T2) completion

Modular structure ───────> Trace formula (T4) ──> Riemann-Weil (T4)

Prime stability (T3) ────> Operator (T1) [discrete → continuous spectrum]

Falsification (T5) ──────> Validates all other tasks
```

---

## Recommended Action Priority

1. **[Immediate]** Derive $V_\text{eff}(\psi)$ from UBT Lagrangian — unblocks everything.
2. **[Urgent]** Close the $B = 46$ gap — currently FAILING.
3. **[Soon]** Numerical diagonalisation of $\hat{H}_\psi$ with parametric $V$.
4. **[Medium]** Establish modular structure of UBT field $\Theta$.
5. **[Ongoing]** Run full falsification suite with $n_\text{trials} = 50{,}000$.

---

**Last Updated**: 2026-05-06  
**Companion reports**: `open_problems_ranked.md`, `proof_dependency_graph.md`
