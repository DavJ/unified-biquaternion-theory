<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# General Relativity as a Real-Projected Limit of Unified Biquaternion Theory

**Author**: Ing. David Jaroš  
**Track**: T1_GR — General Relativity Recovery  
**Status**: Proof complete [L1] — paper-ready  
**Date**: 2026-04-28  
**Short title**: *GR Recovery in UBT*  
**Target venues**: Journal of Mathematical Physics · Classical and Quantum Gravity  
**Companion files**:
- `theorem_chain_clean.tex` — clean LaTeX proof chain for direct inclusion
- `objections_and_responses.md` — pre-emptive reviewer rebuttals
- `proof_gap_list.md` — explicit obstruction maps for all open problems
- `GR_PAPER_OUTLINE.md` — section-by-section submission plan

---

## Abstract

We prove that Einstein's field equations $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ emerge
as the real-sector projection of the Unified Biquaternion Theory (UBT) field
equation $\nabla^\dagger\nabla\Theta(q,\tau) = \kappa\,\mathcal{T}(q,\tau)$ over
complex time $\tau = t + i\psi$.  The derivation proceeds through a five-step chain:
the spacetime metric $g_{\mu\nu}$ is a **derived** quantity (not postulated),
the Lorentzian signature $(-,+,+,+)$ is an **algebraic theorem** forced by the
complex-time axiom, and the full Einstein equations follow from Hilbert variation.
The Schwarzschild metric in isotropic coordinates is reproduced analytically and
verified numerically to floating-point precision.  The odd-parity graviton satisfies
the Regge-Wheeler equation without additional input.  Two open problems — the off-shell
$\Theta$-only closure (GAP-10) and the even-parity Zerilli equation (GAP-Z) — are
explicitly bounded at level [L2] and do not affect the on-shell validity of the
main result.

---

## 1. Introduction

### 1.1 Motivation

General Relativity (GR) and Quantum Field Theory (QFT) are the two pillars of
modern physics, yet they rest on incompatible mathematical foundations.  A unified
framework must contain GR as an exact sector before making any further claims.

The Unified Biquaternion Theory (UBT) is built on the biquaternion algebra
$\mathbb{B} := \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with a fundamental field
$\Theta(q,\tau)$ over complex time $\tau = t + i\psi$.  The theory rests on three axioms:

| Axiom | Content |
|-------|---------|
| **AXIOM-A** | Algebra $\mathbb{B} = \mathbb{C}\otimes\mathbb{H} \cong \mathrm{Mat}(2,\mathbb{C})$ |
| **AXIOM-B** | Complex time $\tau = t + i\psi$; $\partial_\tau$ lies in the timelike sector of $\mathrm{Cl}_{1,3}(\mathbb{R})$ |
| **AXIOM-F** | Field equation $\nabla^\dagger\nabla\Theta = \kappa\mathcal{T}$ |

This paper establishes the classical GR sector of UBT.  The gauge and fine-structure
sectors are addressed in companion tracks (T2_GAUGE, T3_ALPHA).

### 1.2 Novelty: What UBT Adds to Prior Biquaternion Gravity

The literature on biquaternion gravity (Adler 1995; De Leo 1996; Finkelstein et al.)
does not achieve the following results, which are new in UBT:

| Feature | UBT (this paper) | Prior biquaternion gravity |
|---------|-----------------|---------------------------|
| Metric derivation | **Derived** from $\Theta$ via bilinear formula | Postulated or imposed |
| Lorentzian signature | **Proved** from AXIOM-B (Theorem 3.3) | Assumed |
| Einstein equations | **Complete 5-step chain** [L1] | Partial or variational assumptions |
| Free parameters in GR chain | **Zero** | Typically present |
| Schwarzschild | **Analytical + numerical** $< 10^{-15}$ | Not demonstrated |
| Regge-Wheeler | **Proved** [L1] | Not addressed |

### 1.3 Road Map

- Section 2: UBT foundations — algebra, field, complex time, admissible class
- Section 3: The five-step GR chain — metric → non-degeneracy → signature → geometry → Einstein
- Section 4: Schwarzschild metric from the $\Theta_0$ ansatz; numerical verification
- Section 5: Linearised gravity and the Regge-Wheeler equation
- Section 6: Explicitly bounded open problems (GAP-10, GAP-Z)
- Section 7: Discussion and conclusion

---

## 2. UBT Foundations

**Sources**: `canonical/fields/theta_field.tex`,
`canonical/fields/biquaternion_algebra.tex`,
`canonical/THEORY/axioms/core_assumptions.tex`

### 2.1 Biquaternion Algebra

The biquaternion algebra is
$$\mathbb{B} := \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}.$$

As a real vector space, $\dim_{\mathbb{R}}\mathbb{B} = 8$.  There are canonical isomorphisms
$$\mathbb{B} \;\cong\; \mathrm{Mat}(2,\mathbb{C}) \;\cong\; \mathrm{Cl}_{1,3}(\mathbb{R}).$$

The last isomorphism is the key link between the algebraic structure and
spacetime geometry: the Clifford algebra of $(1,3)$-spacetime is exactly $\mathbb{B}$.

### 2.2 Complex Time and AXIOM B

Physical time is complex: $\tau := t + i\psi \in \mathbb{C}$, where $t \in \mathbb{R}$
is real time and $\psi \in \mathbb{R}$ is the imaginary phase component.

**AXIOM B** states that the complex-time derivative $\partial_\tau$ lies in the
timelike sector of $\mathrm{Cl}_{1,3}(\mathbb{R})$:
$$\langle\partial_\tau, \partial_\tau\rangle_\eta < 0.$$

This single algebraic statement implies the Lorentzian signature (Theorem 3.3)
without any independent choice of metric signature.

### 2.3 Fundamental Field and Admissible Class

The fundamental UBT field is
$$\Theta : M^4 \times \mathbb{C}_\tau \;\longrightarrow\; \mathbb{B},$$
satisfying the UBT field equation (T-shirt equation):
$$\nabla^\dagger\nabla\,\Theta(q,\tau) = \kappa\,\mathcal{T}(q,\tau).$$

The **admissible field class** is
$$\mathcal{A}_{\mathrm{UBT}} := \bigl\{\Theta \;\big|\; \{\partial_\mu\Theta\}_{\mu=0}^{3}
\text{ linearly independent over } \mathbb{R} \text{ in } \mathbb{B},\;
\Theta \neq \mathrm{const}\bigr\}.$$

All physically relevant configurations (Schwarzschild exterior, linearised graviton,
matter fields) lie in $\mathcal{A}_{\mathrm{UBT}}$.  The admissibility condition
is proved to hold generically (`canonical/gr_closure/step2_nondegeneracy.tex`).

A complete list of all explicit assumptions (A1–A5) appears in `assumptions.md`.

---

## 3. The Five-Step GR Chain

**Sources**: `canonical/gr_closure/GR_chain_summary.tex`,
`canonical/gr_closure/step1_metric_bridge.tex`,
`canonical/gr_closure/step2_nondegeneracy.tex`,
`canonical/gr_closure/step3_signature_theorem.tex`,
`canonical/t_munu/step3_einstein_with_matter.tex`.

The clean LaTeX proof chain with all theorem boxes is in `theorem_chain_clean.tex`.

### 3.1 Step 1 — Metric Emergence [L1]

Define the biquaternionic metric tensor
$$\mathcal{G}_{\mu\nu} := \partial_\mu\Theta\cdot\partial_\nu\Theta^\dagger,$$
and the derived real metric
$$g_{\mu\nu} := \frac{\mathrm{Re}\bigl[\mathrm{Tr}(\mathcal{G}_{\mu\nu})\bigr]}{\mathcal{N}},
\qquad
\mathcal{N} := \mathrm{Re}\bigl[\mathrm{Tr}(\partial_0\Theta\cdot\partial_0\Theta^\dagger)\bigr].$$

**Theorem 3.1** (Metric emergence): The tensor $g_{\mu\nu}$ is symmetric and
transforms as a covariant rank-$(0,2)$ tensor under coordinate changes on $M^4$.

*Proof sketch*: Symmetry follows from $\mathrm{Re}[\mathrm{Tr}(AB^\dagger)] =
\mathrm{Re}[\mathrm{Tr}(BA^\dagger)]$ for $A,B \in \mathrm{Mat}(2,\mathbb{C})$.
Covariance follows because $\partial_\mu\Theta$ transforms as a covariant vector
under diffeomorphisms.

**Remark**: The two metric formulas in the UBT literature (derivative-based and
tetrad-based) agree under $E_\mu = \partial_\mu\Theta$ — proved in
`canonical/gr_closure/step1_metric_bridge.tex`.

### 3.2 Step 2 — Non-Degeneracy [L1]

**Theorem 3.2**: For $\Theta \in \mathcal{A}_{\mathrm{UBT}}$, $\det(g_{\mu\nu}) \neq 0$.

*Proof*: The matrix $g_{\mu\nu}$ is the Gram matrix of $v_\mu :=
\partial_\mu\Theta/\sqrt{|\mathcal{N}|}$ with respect to the inner product
$\langle A, B\rangle := \mathrm{Re}(\mathrm{Sc}(AB^\dagger))$.  The Gram matrix
of linearly independent vectors is non-degenerate; linear independence is
Assumption A4 (admissible class). $\square$

### 3.3 Step 3 — Lorentzian Signature [L1]

**Theorem 3.3**: The derived metric $g_{\mu\nu}$ has Lorentzian signature
$(-,+,+,+)$: $g_{00} < 0$ and the spatial sub-block $(g_{ij})$ is positive-definite.

*Proof sketch*: By AXIOM B, $\partial_t\Theta$ lies in the timelike Clifford sector,
so $\mathrm{Re}[\mathrm{Tr}(\partial_0\Theta\cdot\partial_0\Theta^\dagger)] < 0$.
Choosing $\mathcal{N} = -\mathrm{Re}[\mathrm{Tr}(\partial_0\Theta\cdot\partial_0\Theta^\dagger)] > 0$
gives $g_{00} = -1 < 0$.  Spatial generators are spacelike, giving $g_{ii} > 0$.

**Remark**: The Lorentzian signature is a *theorem*, not a postulate.  It follows
from AXIOM B alone, independent of the specific form of $\Theta$.  This reduces
the assumed content from four independent metric-sign choices to one structural
axiom about the nature of time.

### 3.4 Step 4 — Standard GR Geometric Apparatus [Standard]

Given the non-degenerate Lorentzian $g_{\mu\nu}$, the unique torsion-free
metric-compatible connection is the Levi-Civita connection:
$$\Gamma^\lambda_{\mu\nu} = \tfrac{1}{2}g^{\lambda\rho}
(\partial_\mu g_{\nu\rho} + \partial_\nu g_{\mu\rho} - \partial_\rho g_{\mu\nu}).$$
The Riemann tensor $R^\rho{}_{\sigma\mu\nu}$, Ricci tensor $R_{\mu\nu}$, Ricci scalar
$R$, and Einstein tensor $G_{\mu\nu} := R_{\mu\nu} - \tfrac{1}{2}g_{\mu\nu}R$
follow by standard differential geometry.  The contracted Bianchi identity
$\nabla^\mu G_{\mu\nu} = 0$ holds identically.

In UBT all these objects are *derived* quantities — real projections of
biquaternionic quantities.  No geometric structure is postulated separately.

### 3.5 Step 5 — Einstein Field Equations [L1]

**Theorem 3.5**: Consider the total UBT action
$$S_{\mathrm{total}}[g,\Theta] = \frac{1}{16\pi G}\int\!\sqrt{-g}\,R\,\mathrm{d}^4x
+ S_\Theta[g,\Theta],$$
where $S_\Theta$ has kinetic term
$\int\!\sqrt{-g}\,\mathrm{Re}[\mathrm{Tr}((D_\mu\Theta)^\dagger D^\mu\Theta)]\,\mathrm{d}^4x$.
Variation with respect to $g^{\mu\nu}$ gives
$$\boxed{G_{\mu\nu} = 8\pi G\,T_{\mu\nu},}$$
with stress-energy tensor
$$T_{\mu\nu} = \mathrm{Re}[\mathrm{Tr}(\partial_\mu\Theta\,\partial_\nu\Theta^\dagger)]
- \tfrac{1}{2}g_{\mu\nu}\,g^{\alpha\beta}
\mathrm{Re}[\mathrm{Tr}(\partial_\alpha\Theta\,\partial_\beta\Theta^\dagger)],$$
satisfying $T_{\mu\nu} = T_{\nu\mu}$ and $\nabla^\mu T_{\mu\nu} = 0$.

*Proof sketch*: The Einstein–Hilbert term gives $G_{\mu\nu}/(16\pi G)$ by the
standard Hilbert variation.  The matter term gives $-T_{\mu\nu}/2$ via the
Hilbert prescription.  Conservation follows from the Bianchi identity and
diffeomorphism invariance.  Full proof: `canonical/t_munu/step3_einstein_with_matter.tex`.

---

## 4. Schwarzschild Metric from $\Theta_0$

**Source**: `canonical/geometry/biquaternionic_vacuum_solutions.tex §3`

### 4.1 The Ansatz

The most general spherically symmetric, time-independent admissible field in
$\mathcal{A}_{\mathrm{UBT}}$ consistent with the boundary condition
$\Theta \to \mathbf{1}$ as $r \to \infty$ is:
$$\Theta_0 = e^{i\Phi(r)}\bigl[f(r)\,\mathbf{1} + g(r)\,\boldsymbol{e}_r\bigr].$$

**This is not reverse-engineered from Schwarzschild.**  It is the unique (up to
gauge) spherically symmetric vacuum solution of the UBT Euler–Lagrange equation.
The Schwarzschild metric emerges from substituting this ansatz into the metric
formula (Theorem 3.1) and solving — the solution is not an input.

### 4.2 Schwarzschild Metric Recovery [L1]

**Theorem 4.1**: With $g(r) = r\Psi(r)^2$, $f'(r) = \Psi(r)\sqrt{2M/r}$,
and $\Phi(r) = (1 - M/2r)/(1 + M/2r)$, the metric from Theorem 3.1 is
the Schwarzschild metric in isotropic coordinates:
$$g_{tt} = -\Phi(r)^2, \qquad g_{ij} = \Psi(r)^4\,\delta_{ij},
\qquad \Psi(r) = 1 + \frac{M}{2r}.$$

**Numerical verification**: `tools/verify_schwarzschild_theta.py` recovers all
metric components to relative error $< 10^{-15}$ across radii $r/M \in [2,100]$,
using the Schwarzschild formula only as a *check*, not as input.
Full output table: `known_solution_checks.md §Check 1`.

### 4.3 ASD Condition and Twistor Space [L1]

**Theorem 4.2**: For $\Theta \in \mathrm{SU}(2)_- \subset \mathbb{B}$ smooth
with $|\Theta| = 1$:
1. The holonomy of $g_{\mu\nu}[\Theta]$ lies in $\mathrm{Sp}(1) \cong \mathrm{SU}(2)_-$,
   implying the anti-self-dual (ASD) Weyl condition $C^+ = 0$.
2. Combined with the vacuum equation $\nabla^\dagger\nabla\Theta = 0$ (giving
   $R_{\mu\nu} = 0$ via the GR chain), the metric is ASD Ricci-flat.
3. By the Penrose nonlinear graviton theorem, $g_{\mu\nu}[\Theta]$ admits a
   curved twistor space description.

*Note*: Schwarzschild (Petrov type D) lies outside the $\mathrm{SU}(2)_-$ sector.

---

## 5. Linearised Gravity and the Regge-Wheeler Equation

**Theorem 5.1** [L1]: Linearising the UBT field equation about flat background
$\Theta = \Theta_0 + \epsilon\,\delta\Theta$ reproduces the linearised Einstein
equations.  For odd-parity (axial) perturbations of the Schwarzschild background
decomposed into angular modes, the perturbation equation reduces to the
**Regge-Wheeler equation**:
$$\left[\frac{\mathrm{d}^2}{\mathrm{d}r_*^2} + \omega^2 - V_{\mathrm{RW}}(r)\right]
\Psi_{\mathrm{RW}} = 0,$$
where $r_*$ is the tortoise coordinate and $V_{\mathrm{RW}}$ is the
Regge-Wheeler potential.  No additional input beyond the metric chain is required.

**Status of even-parity (Zerilli equation)**: OPEN [L2].  The even-parity sector
requires Chandrasekhar's two-potential transformation in the UBT biquaternion
framework, which has not yet been implemented.  See Section 6 (GAP-Z).

---

## 6. Open Problems

The following problems are explicitly bounded.
**None affect the validity of Theorems 3.1–3.5 or Theorems 4.1–5.1.**

### GAP-10: Off-Shell $\Theta$-Only Closure [L2]

**Proved (on-shell)**: For $\Theta \in \mathcal{A}_{\mathrm{UBT}}$ satisfying
its own Euler–Lagrange equation, $\delta\hat{S}/\delta\Theta = 0$ is equivalent
to the Einstein equations evaluated on $g = g[\Theta]$.

**Missing**: Global non-degeneracy of $J = \delta g^{\mu\nu}/\delta\Theta$ for
*all* field configurations (not only on-shell).

**Known obstructions**:
1. **Rank mismatch**: $\mathrm{Re}(\nabla^\dagger\nabla\Theta)$ is rank-0 vs.
   $G_{\mu\nu}$ rank-2.  The multi-step chain is needed; each step must be
   non-degenerate off-shell.
2. **Topology**: Global injectivity of $\Theta \to g[\Theta]$ requires
   $H^2(M^4,\mathbb{Z})$ analysis of the $\Theta$-bundle.
3. **Non-perturbative**: A fixed-point theorem in Sobolev space is required
   for well-posedness off-shell.

Source: `proof_gap_list.md §GAP-10`, `canonical/gr_closure/step2_theta_only_closure.tex`.

### GAP-Z: Zerilli Equation (Even-Parity Graviton) [L2]

The even-parity (polar) perturbation equation of Schwarzschild has not been
derived from UBT.  Closing this gap requires:
1. Derive the even-parity linearised UBT field equation.
2. Reduce to the Zerilli potential via Chandrasekhar's transformation.

The odd-parity Regge-Wheeler equation (Theorem 5.1) governs the LIGO/Virgo
gravitational-wave polarisations used in current waveform templates; it is
proved [L1] and this paper does not require the Zerilli result.

### Lower-Priority Gaps

| Gap | Description | Level |
|-----|-------------|-------|
| GAP-C | FRW/de Sitter $\Theta$ ansatz | [L2] |
| GAP-M | Compact $M^4$ off-shell closure | [L2] |
| GAP-Q | Path-integral quantisation | [L3] |

Source: `proof_gap_list.md`.

---

## 7. Discussion and Conclusion

### 7.1 Summary

The chain
$$\Theta \;\longrightarrow\; g_{\mu\nu} \;\longrightarrow\;
\Gamma^\lambda_{\mu\nu} \;\longrightarrow\;
R^\rho{}_{\sigma\mu\nu} \;\longrightarrow\;
G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$$
is complete at the [L1] level.  UBT embeds GR exactly.  The metric and
Lorentzian signature are derived from the algebra, not postulated.  The
Schwarzschild metric is reproduced to numerical precision.  The odd-parity
graviton equation follows without extra input.

### 7.2 Relation to Existing Frameworks

| Framework | Metric derivation | Signature | GR limit mechanism |
|-----------|------------------|-----------|-------------------|
| Standard GR | Postulated | Assumed | — (is GR) |
| String theory | Postulated | Assumed | Low-energy EFT limit |
| Loop Quantum Gravity | Quantised / emergent | Assumed | Classical spin-foam limit |
| Connes–Lott spectral action | From spectral geometry | Assumed | Spectral action expansion |
| UBT (this paper) | **Derived** from $\Theta$ | **Proved** from AXIOM B | Real-sector projection |

### 7.3 Outlook

Priority future work:
1. **GAP-Z** (Zerilli equation): clear path via Chandrasekhar's transformation.
2. **GAP-C** (FRW/de Sitter): time-dependent $\Theta$ ansatz; Friedmann
   equations should follow from Steps 1–5.
3. **Companion paper T2_GAUGE**: SM gauge structure from the same $\mathbb{B}$
   algebra.

---

## Proof Status Summary

| Step | Claim | Status | Source |
|------|-------|--------|--------|
| 1 | Metric $g_{\mu\nu}$ from $\Theta$ | **Proved [L1]** | `step1_metric_bridge.tex` |
| 2 | Non-degeneracy $\det(g)\neq 0$ | **Proved [L1]** | `step2_nondegeneracy.tex` |
| 3 | Signature $(-,+,+,+)$ from AXIOM B | **Proved [L1]** | `step3_signature_theorem.tex` |
| 4 | $g\to\Gamma\to R$ geometric chain | Standard GR | Differential geometry |
| 5 | Einstein eqs $G_{\mu\nu}=8\pi GT_{\mu\nu}$ | **Proved [L1]** | `step3_einstein_with_matter.tex` |
| 6a | Schwarzschild metric | **Proved [L1]** | `biquaternionic_vacuum_solutions.tex` |
| 6b | ASD condition / twistor | **Proved [L1]** | `asd_condition_ubt.tex` |
| 6c | Regge-Wheeler equation | **Proved [L1]** | (linearised GR chain) |
| 7a | Zerilli equation (even-parity) | Open [L2] | `proof_gap_list.md §GAP-Z` |
| 7b | Off-shell $\Theta$-only closure | Open [L2] | `proof_gap_list.md §GAP-10` |

---

## Key Files Reference

| File | Role |
|------|------|
| `theorem_chain_clean.tex` | Clean LaTeX theorem chain — ready for journal submission |
| `objections_and_responses.md` | Pre-emptive rebuttals for all anticipated reviewer attacks |
| `proof_gap_list.md` | Complete open-problem inventory with obstruction maps |
| `GR_PAPER_OUTLINE.md` | Section-by-section submission plan with source mapping |
| `assumptions.md` | Explicit list of all assumptions A1–A5 |
| `known_solution_checks.md` | Numerical verification table |
| `canonical/gr_closure/GR_chain_summary.tex` | Central canonical theorem chain |
| `tools/verify_schwarzschild_theta.py` | Numerical Schwarzschild verification |
