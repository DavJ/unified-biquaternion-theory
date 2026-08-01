<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# PAPER_OUTLINE.md — T1_GR Flagship Paper

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T1_GR — General Relativity Recovery  
**Status**: Outline ready; LaTeX draft (`research_tracks/T1_GR/theorem_chain.tex`) exists  
**Target journals**: Journal of Mathematical Physics; Classical and Quantum Gravity  

---

## Title

*General Relativity as a Real-Projected Limit of Unified Biquaternion Theory*

Short title: *GR Recovery in UBT*

---

## Abstract

We prove that Einstein's field equations $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$
emerge as the real-sector projection of the Unified Biquaternion Theory (UBT)
field equation $\nabla^\dagger\nabla\Theta(q,\tau) = \kappa\mathcal{T}(q,\tau)$
over complex time $\tau = t + i\psi$.  The derivation proceeds through five steps:
(1) the spacetime metric $g_{\mu\nu}$ is a derived quantity, not a postulate;
(2) non-degeneracy of $g$ follows from the linear independence condition on the
admissible field class; (3) the Lorentzian signature $(-,+,+,+)$ is an algebraic
theorem from AXIOM B, not an assumption; (4) the Levi-Civita connection and full
Riemannian apparatus follow by standard differential geometry; (5) the Einstein
equations follow from Hilbert variation of the UBT total action.
The Schwarzschild metric in isotropic coordinates is recovered analytically from a
specific $\Theta_0$ ansatz and verified numerically to relative error $< 10^{-8}$.
The odd-parity graviton equation (Regge-Wheeler) is derived from linearised UBT
without additional input.  Two open problems — off-shell $\Theta$-only closure and
the even-parity (Zerilli) equation — are precisely stated and bounded; neither
affects the validity of the main result.

---

## Central Theorem

**Theorem (GR Recovery).**  Let $\mathcal{A}_{\mathrm{UBT}}$ be the admissible
class of biquaternionic fields:
$$\mathcal{A}_{\mathrm{UBT}} := \bigl\{\Theta : M^4\times\mathbb{C}_\tau \to
\mathbb{C}\otimes\mathbb{H} \;\big|\; \partial_\mu\Theta \text{ linearly independent},
\; \Theta \neq \mathrm{const}\bigr\}.$$
For $\Theta \in \mathcal{A}_{\mathrm{UBT}}$, define
$$g_{\mu\nu} := \frac{\mathrm{Re}\bigl[\mathrm{Tr}(\partial_\mu\Theta\cdot
\partial_\nu\Theta^\dagger)\bigr]}{\mathcal{N}}, \qquad \mathcal{N} > 0.$$
Then:
1. $g_{\mu\nu}$ is a non-degenerate Lorentzian metric with signature $(-,+,+,+)$.
2. Stationary variation of the total UBT action $S_{\mathrm{total}}[g,\Theta]$
   with respect to $g^{\mu\nu}$ gives $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$.
3. The Schwarzschild exterior metric is reproduced by an explicit $\Theta_0$ ansatz.
4. The Regge-Wheeler equation for odd-parity Schwarzschild perturbations follows
   from linearised UBT.

---

## Assumptions

The paper rests on the following assumptions, stated explicitly:

| Label | Assumption | Type |
|-------|-----------|------|
| AXIOM-A | Fundamental algebra is $\mathbb{C}\otimes\mathbb{H}$ | Foundational postulate |
| AXIOM-B | Complex-time derivative $\partial_\tau$ lies in the timelike sector of $\mathrm{Cl}_{1,3}(\mathbb{R})$ | Foundational postulate |
| AXIOM-F | Field equation $\nabla^\dagger\nabla\Theta = \kappa\mathcal{T}$ | Dynamical postulate |
| DEF-A | Admissible class $\mathcal{A}_{\mathrm{UBT}}$: linearly independent $\partial_\mu\Theta$ | Definition |
| STD | Hilbert action principle for GR | Standard |

No assumption involves $G_{\mu\nu}$, $g_{\mu\nu}$, or the Lorentzian signature —
these are all derived.

---

## Derivation Roadmap

### Step 1 — Metric emergence (Theorem 3.1)

**Claim**: For $\Theta\in\mathcal{A}_{\mathrm{UBT}}$, the tensor
$g_{\mu\nu} = \mathrm{Re}[\mathrm{Tr}(\partial_\mu\Theta\cdot\partial_\nu\Theta^\dagger)]/\mathcal{N}$
is symmetric and transforms as a covariant rank-2 tensor.

**Source**: `canonical/gr_closure/step1_metric_bridge.tex`  
**Status**: Proved [L1]

---

### Step 2 — Non-degeneracy (Theorem 3.2)

**Claim**: $\det(g_{\mu\nu}) \neq 0$ for $\Theta\in\mathcal{A}_{\mathrm{UBT}}$.

**Proof route**: The Gram matrix of $n$ vectors satisfies $\det G = 0$ iff the
vectors are linearly dependent.  Linear independence is the defining condition of
$\mathcal{A}_{\mathrm{UBT}}$.

**Source**: `canonical/gr_closure/step2_nondegeneracy.tex`  
**Status**: Proved [L1]

---

### Step 3 — Lorentzian signature (Theorem 3.3)

**Claim**: $g_{00} < 0$; the spatial block $(g_{ij})$ is positive-definite.
Signature is $(-,+,+,+)$.

**Proof route**: AXIOM B places $\partial_\tau$ in the timelike sector of
$\mathrm{Cl}_{1,3}(\mathbb{R})$.  The temporal derivative $\partial_t\Theta$
inherits the Clifford-algebraic timelike property, giving $g_{00} < 0$.
Spatial generators are spacelike, giving $g_{ii} > 0$.

**Source**: `canonical/gr_closure/step3_signature_theorem.tex`  
**Status**: Proved [L1]

---

### Step 4 — Standard GR apparatus (Propositions 3.4–3.6)

Standard application of differential geometry to the derived non-degenerate
Lorentzian metric: Levi-Civita connection $\Gamma^\lambda_{\mu\nu}$, Riemann
tensor, Ricci tensor, Einstein tensor.  Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$
holds by standard geometry.

**Source**: `canonical/geometry/curvature.tex`; standard references  
**Status**: Standard — cite Wald, Misner-Thorne-Wheeler

---

### Step 5 — Einstein field equations (Theorem 3.7)

**Claim**: Variation $\delta S_{\mathrm{total}}/\delta g^{\mu\nu} = 0$ gives
$G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ with
$T_{\mu\nu} = \mathrm{Re}(\partial_\mu\Theta\,\partial_\nu\Theta^\dagger)
- \frac{1}{2}g_{\mu\nu}\,g^{\alpha\beta}\mathrm{Re}(\partial_\alpha\Theta\,
\partial_\beta\Theta^\dagger)$.

**Proof route**: Standard Hilbert variation; $T_{\mu\nu}$ symmetry and conservation
$\nabla^\mu T_{\mu\nu} = 0$ proved separately.

**Source**: `canonical/t_munu/step3_einstein_with_matter.tex`,
`canonical/geometry/stress_energy.tex`  
**Status**: Proved [L1]

---

### Step 6a — Schwarzschild metric (Theorem 4.1)

**Claim**: The ansatz
$\Theta_0 = e^{i\Phi(r)}[f(r)\mathbf{1} + g(r)\boldsymbol{e}_r]$
with appropriate radial functions reproduces the Schwarzschild metric in isotropic
coordinates.  Numerical error < $10^{-8}$.

**Source**: `canonical/geometry/biquaternionic_vacuum_solutions.tex §3`;
`tools/verify_schwarzschild_theta.py`  
**Status**: Proved [L1] + numerically verified

---

### Step 6b — ASD condition (Theorem 4.2)

**Claim**: For $\Theta\in\mathrm{SU}(2)_-\subset\mathbb{C}\otimes\mathbb{H}$
smooth with $|\Theta|=1$, the induced metric is anti-self-dual Ricci-flat, admitting
a curved twistor space description (Penrose nonlinear graviton theorem).

**Source**: `canonical/gr_closure/asd_condition_ubt.tex`  
**Status**: Proved [L1]

---

### Step 6c — Regge-Wheeler equation (Theorem 5.1)

**Claim**: Linearisation $\Theta = \Theta_0 + \epsilon\,\delta\Theta$ about
Schwarzschild, restricted to the odd-parity (axial) sector, yields the
Regge-Wheeler equation for graviton frequency $\omega$ and tortoise coordinate
$r_*$.

**Source**: Linearised UBT analysis in `canonical/gr_closure/`  
**Status**: Proved [L1]

---

## Paper Section Map

| Section | Content | Pages | Source |
|---------|---------|-------|--------|
| 1 Introduction | Motivation, novel claims, road map | ~1.5 | — |
| 2 UBT Foundations | Algebra, field, axioms, admissible class | ~2 | `canonical/fields/`, `canonical/THEORY/axioms/` |
| 3 Five-Step GR Chain | Theorems 3.1–3.7 | ~5 | `canonical/gr_closure/` |
| 4 Schwarzschild and ASD | Theorems 4.1–4.2 | ~2 | `canonical/geometry/` |
| 5 Linearised Gravity | Theorem 5.1 (Regge-Wheeler) | ~2 | `canonical/gr_closure/` |
| 6 Open Problems | GAP-10 and GAP-Z with obstruction maps | ~1 | `research_tracks/T1_GR/proof_gap_list.md` |
| 7 Discussion | Summary, comparison with literature, outlook | ~1 | — |
| Appendix A | Full signature theorem proof | ~1 | `canonical/gr_closure/step3_signature_theorem.tex` |
| Appendix B | $T_{\mu\nu}$ derivation and conservation | ~1 | `canonical/t_munu/`, `canonical/geometry/stress_energy.tex` |
| Appendix C | Numerical verification details | ~0.5 | `tools/verify_schwarzschild_theta.py` |

Total estimated length: **16–18 pages** (standard journal format)

---

## Validation Section

The paper includes the following independent validations:

1. **Numerical**: `tools/verify_schwarzschild_theta.py` — Schwarzschild metric
   components from $\Theta_0$ vs. exact formula, relative error < $10^{-8}$.
   Output table to be reproduced as Appendix C.

2. **Algebraic consistency**: Verification that $T_{\mu\nu}$ defined by Hilbert
   prescription satisfies $\nabla^\mu T_{\mu\nu} = 0$ identically — required for
   consistency of the Einstein equations.

3. **ASD check**: The twistor-space correspondence for ASD Ricci-flat metrics
   (Penrose theorem) serves as an independent structural check on the metric
   derivation.

4. **Signature theorem**: The proof that AXIOM B $\Rightarrow$ Lorentzian signature
   is algebraic and self-contained; it can be checked independently by a reader
   familiar with Clifford algebras.

5. **Regge-Wheeler reduction**: The perturbation analysis reduces to a known
   exact result of classical GR, providing an independent check on Steps 1–5.

---

## Limitations (to be stated explicitly in paper)

| Limitation | Exact statement | Location in paper |
|-----------|----------------|-------------------|
| Off-shell closure | GAP-10: global non-degeneracy of $J = \delta g^{\mu\nu}/\delta\Theta$ not proved for all $\Theta$ off-shell | Section 6 |
| Zerilli equation | Even-parity graviton perturbation not yet derived from UBT | Section 5, remark |
| Cosmological solutions | FRW/de Sitter ansatz not constructed from $\Theta$ | Section 7, outlook |
| Quantum GR | Path-integral quantisation requires off-shell closure and additional input; not addressed | Section 7, outlook |
| Fine structure constant | $\alpha$ not derived; unrelated to GR recovery | Not discussed |

These limitations are scientific facts.  Stating them precisely is a strength,
not a weakness.

---

## Key File List

| File | Role in paper |
|------|---------------|
| `research_tracks/T1_GR/theorem_chain.tex` | Existing LaTeX draft; core of Sections 2–5 |
| `canonical/gr_closure/GR_chain_summary.tex` | Central theorem chain source |
| `canonical/gr_closure/step1_metric_bridge.tex` | Step 1 proof |
| `canonical/gr_closure/step2_nondegeneracy.tex` | Step 2 proof |
| `canonical/gr_closure/step3_signature_theorem.tex` | Step 3 proof + Appendix A |
| `canonical/t_munu/step3_einstein_with_matter.tex` | Step 5 proof |
| `canonical/geometry/biquaternionic_vacuum_solutions.tex` | Schwarzschild derivation |
| `canonical/geometry/stress_energy.tex` | $T_{\mu\nu}$ conservation (Appendix B) |
| `tools/verify_schwarzschild_theta.py` | Numerical verification (Appendix C) |
| `research_tracks/T1_GR/proof_gap_list.md` | Source for Section 6 |
| `canonical/gr_closure/asd_condition_ubt.tex` | ASD / twistor theorem |

---

## Submission Plan

| Milestone | Target |
|-----------|--------|
| Notation unification pass across `canonical/gr_closure/` | Week 1 |
| Draft Sections 2–5 from `theorem_chain.tex` | Weeks 1–4 |
| Draft Sections 4–5 (Schwarzschild + Regge-Wheeler) | Weeks 4–6 |
| Draft Sections 1, 6, 7 + appendices | Weeks 6–8 |
| First complete draft | Week 9 |
| Internal consistency check + revision | Week 10–11 |
| arXiv submission | Week 12 |
| Journal submission (JMP or CQG) | Week 13 |
