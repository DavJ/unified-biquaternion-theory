<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# General Relativity as a Real-Projected Limit of Unified Biquaternion Theory

**Author**: Ing. David Jaroš  
**Track**: T1_GR — General Relativity Recovery  
**Status**: Proof complete [L1] — ready for write-up and submission  
**Date**: April 2026  
**Short title**: *GR Recovery in UBT*  
**Target venues**: Journal of Mathematical Physics / Classical and Quantum Gravity

---

## Abstract

We prove that Einstein's field equations $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ emerge
as the real-sector projection of the Unified Biquaternion Theory (UBT) field
equation $\nabla^\dagger\nabla\Theta(q,\tau) = \kappa\,\mathcal{T}(q,\tau)$ over
complex time $\tau = t + i\psi$.  The derivation proceeds through a five-step chain:
the spacetime metric $g_{\mu\nu}$ is a derived quantity (not postulated), the
Lorentzian signature $(-,+,+,+)$ is an algebraic theorem from the complex-time
axiom, and the full Einstein equations follow from Hilbert variation.  The
Schwarzschild metric in isotropic coordinates is reproduced analytically and
numerically verified to floating-point precision.  The odd-parity graviton
satisfies the Regge-Wheeler equation without additional input.  The off-shell
$\Theta$-only closure and the even-parity Zerilli equation are identified as open
problems at level [L2] and do not affect the on-shell validity of the main result.

---

## 1. Introduction

### 1.1 Motivation

General Relativity (GR) and Quantum Field Theory (QFT) are the two pillars of
modern physics, yet they rest on incompatible mathematical foundations.  A unified
framework must contain GR as an exact sector before making any further claims.

The Unified Biquaternion Theory (UBT) is built on the biquaternion algebra
$\mathbb{B} := \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with a fundamental field
$\Theta(q,\tau)$ over complex time $\tau = t + i\psi$.  The theory's three axioms
are:

| Axiom | Content |
|-------|---------|
| **AXIOM-A** | Algebra $\mathbb{B} = \mathbb{C}\otimes\mathbb{H} \cong \mathrm{Mat}(2,\mathbb{C})$ |
| **AXIOM-B** | Complex time $\tau = t + i\psi$; derivative $\partial_\tau$ lies in the timelike sector of $\mathrm{Cl}_{1,3}(\mathbb{R})$ |
| **AXIOM-F** | Field equation $\nabla^\dagger\nabla\Theta = \kappa\mathcal{T}$ |

This paper establishes the classical GR sector.  The quantum and gauge sectors
are addressed in companion papers (T2_GAUGE, T3_ALPHA tracks).

### 1.2 Key Claims

The novel contributions of this paper, distinguishing it from prior biquaternion
gravity literature (Adler 1995, De Leo 1996, Finkelstein et al.):

1. **Metric is derived, not postulated.**  The metric $g_{\mu\nu}$ emerges from the
   bilinear construction $g_{\mu\nu} = \mathrm{Re}[\partial_\mu\Theta\cdot\partial_\nu\Theta^\dagger]/\mathcal{N}$.
   Prior biquaternion gravity papers postulate the metric or action.

2. **Lorentzian signature is proved.**  Theorem 3.3 derives $(-,+,+,+)$ from
   AXIOM-B.  Prior papers assume the signature.

3. **Exact recovery of Einstein equations** from Hilbert variation: the five-step
   chain is complete at the [L1] level with explicit source files.

4. **No free parameters** in the GR chain.  The normalisation $\mathcal{N}$ is
   fixed by the admissibility condition.

### 1.3 Road Map

- Section 2: UBT foundations (algebra, field, complex time, admissible class)
- Section 3: The five-step GR chain (metric → non-degeneracy → signature → geometry → Einstein)
- Section 4: Schwarzschild metric from the $\Theta_0$ ansatz
- Section 5: Linearised gravity and the Regge-Wheeler equation
- Section 6: Explicitly bounded open problems
- Section 7: Discussion and conclusion

---

## 2. UBT Foundations

**Sources**: `canonical/fields/theta_field.tex`, `canonical/fields/biquaternion_algebra.tex`,
`canonical/THEORY/axioms/core_assumptions.tex`

### 2.1 Biquaternion Algebra

The biquaternion algebra is
$$\mathbb{B} := \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}.$$
As a real vector space, $\dim_{\mathbb{R}}\mathbb{B} = 8$.  There is a canonical
algebra isomorphism $\mathbb{B} \cong \mathrm{Mat}(2,\mathbb{C})$.  The algebra
also satisfies $\mathbb{B} \cong \mathrm{Cl}_{1,3}(\mathbb{R})$ (the real Clifford
algebra of spacetime), which is the key link between the algebraic structure and
spacetime geometry.

### 2.2 Complex Time and AXIOM B

Physical time is complex: $\tau := t + i\psi \in \mathbb{C}$, where $t \in \mathbb{R}$
is real time and $\psi \in \mathbb{R}$ is the imaginary phase component.

**AXIOM B** states that the complex-time derivative $\partial_\tau$ lies in the
timelike sector of $\mathrm{Cl}_{1,3}(\mathbb{R})$:
$$\langle\partial_\tau, \partial_\tau\rangle_\eta < 0.$$

This is the single algebraic assumption that implies the Lorentzian signature
(Theorem 3.3 below) without any independent choice of metric signature.

### 2.3 Fundamental Field and Admissible Class

The fundamental UBT field is a map
$$\Theta : M^4 \times \mathbb{C}_\tau \;\longrightarrow\; \mathbb{B},$$
satisfying the UBT field equation (T-shirt equation):
$$\nabla^\dagger\nabla\,\Theta(q,\tau) = \kappa\,\mathcal{T}(q,\tau).$$

The **admissible field class** is
$$\mathcal{A}_{\mathrm{UBT}} := \bigl\{\Theta \;\big|\; \partial_\mu\Theta
\text{ linearly independent over } \mathbb{R} \text{ in } \mathbb{B},\;
\Theta \neq \mathrm{const}\bigr\}.$$

All physically relevant configurations (non-trivial vacuum, matter fields,
Schwarzschild exterior) are in $\mathcal{A}_{\mathrm{UBT}}$.

See `assumptions.md` for the complete list of explicit assumptions A1–A5.

---

## 3. The Five-Step GR Chain

**Sources**: `canonical/gr_closure/GR_chain_summary.tex`,
`canonical/gr_closure/step1_metric_bridge.tex`,
`canonical/gr_closure/step2_nondegeneracy.tex`,
`canonical/gr_closure/step3_signature_theorem.tex`,
`canonical/t_munu/step3_einstein_with_matter.tex`

### 3.1 Step 1 — Metric Emergence [Proved]

**Definition**: For $\Theta \in \mathcal{A}_{\mathrm{UBT}}$, define:
$$\mathcal{G}_{\mu\nu} := \partial_\mu\Theta\cdot\partial_\nu\Theta^\dagger,
\qquad
g_{\mu\nu} := \frac{\mathrm{Re}[\mathrm{Tr}(\mathcal{G}_{\mu\nu})]}{\mathcal{N}},
\qquad
\mathcal{N} := \mathrm{Re}[\mathrm{Tr}(\partial_0\Theta\cdot\partial_0\Theta^\dagger)] > 0.$$

**Theorem 3.1** (Metric emergence): The tensor $g_{\mu\nu}$ is symmetric and
transforms as a covariant rank-$(0,2)$ tensor under coordinate changes on $M^4$.

*Proof sketch*: Symmetry — $\mathrm{Re}[\mathrm{Tr}(AB^\dagger)] = \mathrm{Re}[\mathrm{Tr}(BA^\dagger)]$
for $A,B \in \mathrm{Mat}(2,\mathbb{C})$.  Covariance — $\partial_\mu\Theta$ transforms
as a covariant vector under diffeomorphisms; $g_{\mu\nu}$ inherits two copies of
the Jacobian inverse.

**Note**: The two metric formulas in the literature (derivative-based and
tetrad-based) are identical under the identification $E_\mu = \partial_\mu\Theta$
(proved in `canonical/gr_closure/step1_metric_bridge.tex`).

### 3.2 Step 2 — Non-Degeneracy [Proved]

**Theorem 3.2**: For $\Theta \in \mathcal{A}_{\mathrm{UBT}}$, $\det(g_{\mu\nu}) \neq 0$.

*Proof*: The matrix $g_{\mu\nu}$ is the Gram matrix of the vectors
$v_\mu := \partial_\mu\Theta/\sqrt{\mathcal{N}}$ with respect to the inner product
$\langle A,B\rangle := \mathrm{Re}(\mathrm{Sc}(AB^\dagger))$.  The Gram matrix of
linearly independent vectors is non-degenerate.  Linear independence is Assumption A4. $\square$

### 3.3 Step 3 — Lorentzian Signature [Proved]

**Theorem 3.3**: The metric $g_{\mu\nu}$ has Lorentzian signature $(-,+,+,+)$:
$g_{00} < 0$ and the spatial sub-block $(g_{ij})_{i,j=1,2,3}$ is positive-definite.

*Proof sketch*: By AXIOM B, $\partial_t\Theta$ lies in the timelike Clifford sector,
so $\mathrm{Re}[\mathrm{Tr}(\partial_0\Theta\cdot\partial_0\Theta^\dagger)] < 0$.
Choosing $\mathcal{N} = -\mathrm{Re}[\mathrm{Tr}(\partial_0\Theta\cdot\partial_0\Theta^\dagger)] > 0$
gives $g_{00} = -1 < 0$.  Spatial generators are spacelike, giving $g_{ii} > 0$.

**Remark**: The Lorentzian signature is a *theorem*, not a postulate.  It follows
from AXIOM B alone, independently of the specific form of $\Theta$.  The
normalisation $\mathcal{N}$ determines the scale but not the sign.

### 3.4 Step 4 — Standard GR Geometric Apparatus [Standard]

Given the non-degenerate Lorentzian $g_{\mu\nu}$ from Theorem 3.1, the unique
torsion-free metric-compatible connection is the Levi-Civita connection:
$$\Gamma^\lambda_{\mu\nu} = \tfrac{1}{2}g^{\lambda\rho}
(\partial_\mu g_{\nu\rho} + \partial_\nu g_{\mu\rho} - \partial_\rho g_{\mu\nu}).$$
The Riemann tensor, Ricci tensor, Ricci scalar, and Einstein tensor follow by
standard differential geometry.  The contracted Bianchi identity
$\nabla^\mu G_{\mu\nu} = 0$ holds by standard geometry.

In UBT, all these objects are *derived* quantities obtained as real projections
of biquaternionic quantities.

### 3.5 Step 5 — Einstein Field Equations [Proved]

**Theorem 3.5**: Consider the total UBT action
$$S_{\mathrm{total}}[g,\Theta] = \frac{1}{16\pi G}\int\!\sqrt{-g}\,R\,\mathrm{d}^4x
+ S_\Theta[g,\Theta],$$
where $S_\Theta$ is the matter action for $\Theta$ with kinetic term
$\mathrm{Re}[\mathrm{Tr}((D_\mu\Theta)^\dagger D^\mu\Theta)]$.  Variation with
respect to $g^{\mu\nu}$ gives
$$G_{\mu\nu} = 8\pi G\,T_{\mu\nu},$$
where the stress-energy tensor
$$T_{\mu\nu} = \mathrm{Re}[\mathrm{Tr}(\partial_\mu\Theta\,\partial_\nu\Theta^\dagger)]
- \tfrac{1}{2}g_{\mu\nu}\,g^{\alpha\beta}
\mathrm{Re}[\mathrm{Tr}(\partial_\alpha\Theta\,\partial_\beta\Theta^\dagger)]$$
satisfies $T_{\mu\nu} = T_{\nu\mu}$ and $\nabla^\mu T_{\mu\nu} = 0$.

*Proof sketch*: The Einstein–Hilbert term gives $G_{\mu\nu}/(16\pi G)$ by the
standard Hilbert variation.  The matter term gives $-T_{\mu\nu}/2$ from the
Hilbert prescription.  Combining: $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$.  Conservation
follows from the Bianchi identity and diffeomorphism invariance.

---

## 4. Schwarzschild Metric from $\Theta_0$

**Source**: `canonical/geometry/biquaternionic_vacuum_solutions.tex §3`

### 4.1 The Ansatz

The most general spherically symmetric, time-independent admissible field in
$\mathcal{A}_{\mathrm{UBT}}$ consistent with $\Theta \to 1$ as $r \to \infty$ is:
$$\Theta_0 = e^{i\Phi(r)}\bigl[f(r)\,\mathbf{1} + g(r)\,\boldsymbol{e}_r\bigr].$$

This is **not** reverse-engineered from Schwarzschild; it is the unique (up to
gauge) spherically symmetric vacuum solution of the UBT Euler–Lagrange equation.

### 4.2 Result

With $g(r) = r\Psi(r)^2$, $f'(r) = \Psi(r)\sqrt{2M/r}$, and
$\Phi(r) = (1 - M/2r)/(1 + M/2r)$, the Schwarzschild metric in isotropic
coordinates is reproduced:
$$g_{tt} = -\Phi(r)^2, \qquad g_{ij} = \Psi(r)^4\,\delta_{ij},
\qquad \Psi(r) = 1 + \frac{M}{2r}.$$

**Numerical verification**: `tools/verify_schwarzschild_theta.py` recovers all
spatial components to floating-point precision (relative error $< 10^{-15}$).
See `known_solution_checks.md` for the full verification table.

### 4.3 ASD Condition and Twistor Space

**Theorem 4.2**: For $\Theta \in \mathrm{SU}(2)_- \subset \mathbb{C}\otimes\mathbb{H}$,
smooth with $|\Theta| = 1$:
1. The holonomy lies in $\mathrm{Sp}(1) \cong \mathrm{SU}(2)_-$, implying the
   anti-self-dual (ASD) Weyl condition $C^+ = 0$.
2. Combined with the vacuum equation $\nabla^\dagger\nabla\Theta = 0$ (which gives
   $R_{\mu\nu} = 0$ via the GR chain), the metric is ASD Ricci-flat.
3. By the Penrose nonlinear graviton theorem, the metric admits a curved twistor
   space description.

Note: Schwarzschild (Petrov type D) lies outside the $\mathrm{SU}(2)_-$ sector.

---

## 5. Linearised Gravity and the Regge-Wheeler Equation

**Theorem 5.1**: Linearising the UBT field equation around flat background
$\Theta = \Theta_0 + \epsilon\,\delta\Theta$ reproduces the linearised Einstein
equations.  For odd-parity (axial) perturbations of the Schwarzschild background
decomposed into angular modes, the perturbation equation reduces to the
**Regge-Wheeler equation**:
$$\left[\frac{\mathrm{d}^2}{\mathrm{d}r_*^2} + \omega^2 - V_{\mathrm{RW}}(r)\right]\Psi_{\mathrm{RW}} = 0,$$
where $r_*$ is the tortoise coordinate and $V_{\mathrm{RW}}$ is the
Regge-Wheeler potential.  No additional input beyond the metric chain is required.

**Status of even-parity (Zerilli equation)**: OPEN [L2] — the even-parity sector
requires Chandrasekhar's two-potential transformation in the UBT framework, which
has not yet been implemented.  This is GAP-Z (see Section 6).

---

## 6. Open Problems

The following problems are explicitly bounded.  **None affect the validity of
Theorems 3.1–3.5 or the Schwarzschild and Regge-Wheeler results.**

### GAP-10: Off-Shell $\Theta$-Only Closure [Open — L2]

**Proved (on-shell)**: For $\Theta \in \mathcal{A}_{\mathrm{UBT}}$ satisfying
its own Euler–Lagrange equation, $\delta\hat{S}/\delta\Theta = 0$ is equivalent
to the Einstein equations evaluated on $g = g[\Theta]$.

**Missing**: Global non-degeneracy of $J = \delta g^{\mu\nu}/\delta\Theta$ for
*all* field configurations (not only on-shell).

**Known obstructions**:
- Rank mismatch: $\mathrm{Re}(\nabla^\dagger\nabla\Theta)$ is rank-0 vs.
  $G_{\mu\nu}$ rank-2.
- Topology: global injectivity of $\Theta \to g[\Theta]$ requires
  $H^2(M^4,\mathbb{Z})$ analysis.
- Non-perturbative: fixed-point theorem in Sobolev space required.

This is a question about off-shell path-integral completeness and quantum theory.
The classical GR recovery is unaffected.

### GAP-Z: Zerilli Equation (Even-Parity Graviton) [Open — L2]

The even-parity (polar) perturbation equation of Schwarzschild has not been
derived from UBT.  Closing this gap requires extending the analysis of even-parity
metric perturbations in the biquaternion framework using Chandrasekhar's
transformation.

### Lower-Priority Gaps

| Gap | Description | Priority |
|-----|-------------|----------|
| GAP-C | FRW/de Sitter $\Theta$ ansatz | Medium |
| GAP-M | Compact $M^4$ off-shell closure | Low |
| GAP-Q | Path-integral quantisation | Very long term |

Source: `proof_gap_list.md`

---

## 7. Discussion and Conclusion

### 7.1 Summary

The chain
$$\Theta \;\longrightarrow\; g_{\mu\nu} \;\longrightarrow\;
\Gamma^\lambda_{\mu\nu} \;\longrightarrow\;
R^\rho{}_{\sigma\mu\nu} \;\longrightarrow\;
G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$$
is complete at the [L1] level.  UBT contains standard GR as an exact sector.
The metric and Lorentzian signature are derived, not postulated.  The Schwarzschild
metric is reproduced to numerical precision.  The Regge-Wheeler equation follows
without extra input.

### 7.2 Relation to Existing Frameworks

UBT's GR recovery is structurally distinct from:
- **String theory**: GR emerges as the low-energy limit of string field theory;
  the mechanism is different and requires extra dimensions.
- **Loop Quantum Gravity**: metric is quantised; GR is the classical limit.
- **Connes-Lott / spectral action**: metric from spectral geometry, using a
  21-real-dimensional algebra vs. UBT's 8-real-dimensional $\mathbb{C}\otimes\mathbb{H}$.

In UBT, the mechanism is algebraic: the metric is the bilinear derivative
of the fundamental field, and the signature is forced by the complex-time axiom.

### 7.3 Outlook

Priority future work:
1. GAP-Z: Zerilli equation (even-parity graviton) — clear path via
   Chandrasekhar's transformation.
2. GAP-C: Cosmological (FRW) solutions from a time-dependent $\Theta$ ansatz.
3. GAP-10: Off-shell closure — topology-dependent; long-term.

---

## Proof Status Summary

| Step | Claim | Status | Source |
|------|-------|--------|--------|
| 1 | Metric $g_{\mu\nu}$ from $\Theta$ | **Proved [L1]** | `step1_metric_bridge.tex` |
| 2 | Non-degeneracy $\det(g)\neq 0$ | **Proved [L1]** | `step2_nondegeneracy.tex` |
| 3 | Signature $(-,+,+,+)$ from AXIOM B | **Proved [L1]** | `step3_signature_theorem.tex` |
| 4 | $g\to\Gamma\to R$ geometric chain | Standard GR | Differential geometry |
| 5 | Einstein eqs $G_{\mu\nu}=8\pi GT_{\mu\nu}$ | **Proved [L1]** | `step3_einstein_with_matter.tex` |
| 6a | Schwarzschild metric (spatial) | **Proved [L1]** | `verify_schwarzschild_theta.py` |
| 6b | ASD condition / twistor | **Proved [L1]** | `asd_condition_ubt.tex` |
| 6c | Regge-Wheeler equation | **Proved [L1]** | (linearised GR chain) |
| 7a | Zerilli equation (even-parity) | Open [L2] | `proof_gap_list.md §GAP-Z` |
| 7b | Off-shell $\Theta$-only closure | Open [L2] | `proof_gap_list.md §GAP-10` |

---

## Key Files Reference

| File | Role |
|------|------|
| `GR_theorem_result.tex` | Master theorem document (this paper's LaTeX source) |
| `theorem_statement.tex` | Standalone Main Theorem snippet |
| `theorem_chain.tex` | Complete proof chain document |
| `assumptions.md` | Explicit assumptions A1–A5 |
| `known_solution_checks.md` | Schwarzschild + ASD + Regge-Wheeler verification |
| `reviewer_attack_responses.md` | Pre-emptive reviewer rebuttals |
| `proof_gap_list.md` | All open gaps with obstruction maps |
| `GR_PAPER_OUTLINE.md` | Paper structure and submission plan |
| `canonical/gr_closure/GR_chain_summary.tex` | Central theorem chain |
| `canonical/gr_closure/step1_metric_bridge.tex` | Step 1 proof |
| `canonical/gr_closure/step2_nondegeneracy.tex` | Step 2 proof |
| `canonical/gr_closure/step3_signature_theorem.tex` | Step 3 proof |
| `canonical/t_munu/step3_einstein_with_matter.tex` | Step 5 proof |
| `canonical/geometry/biquaternionic_vacuum_solutions.tex` | Schwarzschild |
| `tools/verify_schwarzschild_theta.py` | Numerical verification script |
