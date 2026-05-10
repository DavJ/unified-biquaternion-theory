<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# B≈46: Next Path if RG/Mode-Counting Fails

**Track**: `research_tracks/rg_B46/` / `reports/`  
**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Task**: `derive_or_kill_B46_from_RG_and_mode_counting` — Target 5  
**Trigger condition**: RG/mode-counting cannot produce $B \approx 46$ (gap $\Delta B \approx 2.4$ unaccounted).

---

## 1. Status of the RG/Mode-Counting Route

From `B46_RG_decision_report.md`:

- Best perturbative estimate: $B_\mathrm{best} \approx 43.6$ (KK+winding, heuristic)
- Phenomenological target: $B \approx 46$
- Unaccounted gap: $\Delta B \approx 2.4$ (5.2%)
- Two-loop, ghost, curvature, zero-mode: all negligible or zero
- **Verdict**: NUMERICALLY_PLAUSIBLE but not PROVED

The gap is small but persistent.  No perturbative correction within the
current framework accounts for it without fitting.  This document states
the **recommended non-fitted replacement path** if the gap remains.

---

## 2. Why the RG Route Falls Short

The fundamental obstruction is that the one-loop RG formula
$$B_\mathrm{1-loop} = \frac{N_\mathrm{eff}\,n}{12\pi^2}$$
is $n$-dependent.  The only way to obtain a constant $B$ is:
1. Fix $n$ to a specific value (prime attractor) — circular if $n^* = 137$ is used.
2. Evaluate the formula at a reference scale where the result is $n$-independent — not achieved.

Furthermore, the formula $B(p) = (p+1)/3$ has a modular-arithmetic structure
(coset count $|\Gamma_0(p) \backslash \mathrm{SL}(2,\mathbb{Z})| = p+1$) that the
RG beta function does not naturally produce.

---

## 3. Allowed Replacement Paths

### 3.1 Spectral Operator Route

**What it is**: Compute $B$ from the spectral zeta function of the operator
$\nabla^\dagger\nabla$ on the complex-time manifold $\mathcal{M}^4 \times S^1_\psi$.

**How it differs from RG**: Instead of computing one-loop diagrams, one uses
the heat-kernel expansion:
$$\ln\det(\nabla^\dagger\nabla) = -\int_0^\infty \frac{dt}{t}\,\mathrm{Tr}[e^{-t\nabla^\dagger\nabla}]$$
and extracts the coefficient of $n\ln n$ from the Seeley-DeWitt expansion.

**Key advantage**: The spectral coefficients $a_k$ in the heat-kernel expansion
are geometric invariants — they could produce a constant $B$ independent of $n$
through global topology.

**Required input**: Spectral geometry of $\nabla^\dagger\nabla$ on the UBT background.
In particular, the spectral zeta function $\zeta_{\nabla}(s)$ evaluated at
$s = -1/2$.

**Prior work**: None in current repository.

**Obstruction**: The spectrum of $\nabla^\dagger\nabla$ on $\mathcal{M}^4 \times S^1_\psi$
is not fully derived; the operator itself is defined in `canonical/fields/` but
its spectral theory on the compact factor is open.

**Probability of success**: Medium.  The spectral route is standard in string
theory and Casimir energy calculations; the biquaternion structure may produce
the factor $p+1$ from a spectral-geometric counting.

**Next step**: Compute $\mathrm{Tr}[e^{-t\nabla^\dagger\nabla}]$ for the KK
tower on $S^1_{R_\psi=1}$ using the Jacobi theta function
$\vartheta_3(0|it/\pi) = \sum_{n=-\infty}^\infty e^{-tn^2}$.

---

### 3.2 Trace Formula Route

**What it is**: Use a Selberg/Gutzwiller-type trace formula for the KK spectrum
to express $B$ in terms of periodic orbits on $S^1_\psi$.

**How it differs from RG**: Instead of momentum-space Feynman diagrams, one
works in position space and sums over classical trajectories.

**Key formula** (Selberg trace formula for $-\partial_\psi^2$ on $S^1$):
$$\sum_{n} f(\lambda_n)
= \frac{L}{2\pi}\int_0^\infty f(k^2)\,dk
  + \sum_{m=1}^\infty \sum_\gamma \frac{L_\gamma}{2\pi m L_\gamma}\,\hat{f}(m L_\gamma),$$
where $L_\gamma$ are lengths of periodic orbits and $\hat{f}$ is the Fourier transform.

**Key advantage**: For $S^1$ the periodic orbits are simple (multiples of the
circumference $2\pi$), and the trace formula is exact.  It might reproduce
the factor $p+1$ through arithmetic of the orbit lengths at prime winding numbers.

**Obstruction**: The connection between the orbit sum and the coefficient of
$n\ln n$ in $V_\mathrm{eff}$ is not established.  The Selberg trace formula
applies to the spectral problem, not directly to the effective potential.

**Probability of success**: Low–Medium.  The trace formula is well-defined but
the link to $B$ requires additional steps.

---

### 3.3 Full Modular Covariance Route

**What it is**: Prove that $S[\Theta]$ is invariant under
$\mathrm{SL}(2,\mathbb{Z})$ acting on the complex time $\tau = t + i\psi$,
then derive $B$ from the modular structure.

**How it differs from RG**: Does not use perturbation theory; instead uses
the exact symmetry of the action under modular transformations.

**Known results** (from `reports/B_gap_final_verdict.md`, `reports/hecke_path_integral_no_go_or_success.md`):
- Arithmetic: $|\Gamma_0(p)\backslash\mathrm{SL}(2,\mathbb{Z})| = p+1$ (PROVED, exact)
- $\mathrm{vol}(X_0(p))/\pi = (p+1)/3 = B(p)$ (PROVED, arithmetic)
- $S[\Theta]$ modular-invariant under $\mathrm{SL}(2,\mathbb{Z})$: **OPEN** (Obstruction O1)
- $\mathrm{SL}(2,\mathbb{Z})$ action on winding modes: **OPEN** (Obstruction O2)

**Required breakthrough**: Prove Obstruction O1 — that the UBT action $S[\Theta]$
is modular-invariant.  A candidate approach: $\eta$-function regularisation of
the one-loop determinant on the torus $\mathbb{C}/(\mathbb{Z}+\mathbb{Z}\tau)$,
analogous to Polchinski Ch.\ 7.

**Probability of success**: Medium (if O1 is resolved; once O1 is resolved,
O2 and O3 follow).  This is the **highest-priority route** identified in prior work.

**Recommended time-box**: 4–8 weeks for an attempt on O1.

---

### 3.4 Nonperturbative Saddle Route

**What it is**: Compute the path integral $Z[\Theta]$ in the saddle-point
approximation around non-trivial classical solutions (instantons) with winding
number $n = p$.

**How it differs from RG**: Non-perturbative; does not rely on small coupling expansion.

**Setup**: Look for saddle-point solutions $\bar\Theta$ satisfying the UBT field
equations with winding number $n = p$ along $S^1_\psi$.

**Key claim**: The saddle-point degeneracy at prime $p$ should be $p+1$
(one saddle per coset of $\Gamma_0(p)$ in $\mathrm{SL}(2,\mathbb{Z})$),
giving $B = (p+1)/3$ from the effective action.

**Obstruction**: Obstruction O3 (from Hecke route): equal-action of the
$p+1$ saddles is not established.  Requires:
1. Existence of $p+1$ distinct saddle-point solutions.
2. Equal action $S[\bar\Theta_a] = S[\bar\Theta_b]$ for all $a,b$.
3. Derivation of the $1/3$ factor from the saddle contribution.

**Probability of success**: Low–Medium.  Non-perturbative computations in UBT
are difficult; the existence of instanton-like solutions is not established.

**Recommended check**: Numerical saddle-point computation for small $p$ ($p = 2, 3$)
to verify or falsify equal-action conjecture before investing in analytic work.

---

## 4. Recommended Priority Order

| Priority | Route | Reason |
|----------|-------|--------|
| 1 | **Full Modular Covariance** | Most structured; arithmetic is already proved; only O1 blocks |
| 2 | **Spectral Operator** | Standard technique; might produce constant $B$ naturally |
| 3 | **Nonperturbative Saddle** | Directly targets the $p+1$ degeneracy; risky but elegant |
| 4 | **Trace Formula** | Well-defined mathematics; connection to $B$ needs work |

---

## 5. What to Do If All Routes Fail

If none of the four routes succeed:

1. **Publish the partial results** as CONDITIONAL:
   - $B_\mathrm{KK+wind} \approx 43.6$ (heuristic, $5.2\%$ error from 46).
   - $B(p) = (p+1)/3$ as a **conditional modular ansatz** (strongly motivated,
     not derived from $S[\Theta]$).

2. **State the gap explicitly** in any publication:
   > "The coefficient $B \approx 46$ is currently not derivable from the
   > perturbative RG framework of UBT.  The best perturbative estimate is
   > $B_\mathrm{best} \approx 43.6$.  The gap $\Delta B \approx 2.4$ (5.2\%)
   > remains open.  The modular ansatz $B(p) = (p+1)/3$ is supported by strong
   > arithmetic evidence but blocked at Obstruction O1."

3. **Redirect resources**: T1\_GR (GR equivalence) and T2\_GAUGE (gauge structure)
   have stronger derivations and are closer to publication-ready.
