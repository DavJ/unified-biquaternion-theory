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


# T1_GR — Explicit Assumptions

**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Standalone declaration of every assumption used in the GR recovery chain.
All claims in `GR_theorem_result.tex` and `GR_MAIN_PAPER.md` depend on exactly these
assumptions and no others.  
**Date**: 2026-04-28  
**Sources**: `canonical/THEORY/axioms/core_assumptions.tex`,
`canonical/fields/biquaternion_algebra.tex`,
`canonical/fields/theta_field.tex`,
`canonical/gr_closure/step2_nondegeneracy.tex`

---

## Summary

| ID | Name | Type | Source |
|----|------|------|--------|
| A1 | Algebra axiom (AXIOM-A) | Structural axiom | `biquaternion_algebra.tex` |
| A2 | Complex time (AXIOM-B) | Structural axiom | `core_assumptions.tex` |
| A3 | Field equation (AXIOM-F) | Dynamical axiom | `theta_field.tex` |
| A4 | Admissibility — linear independence | Regularity condition | `step2_nondegeneracy.tex` |
| A5 | Regularity — smoothness and non-degeneracy | Regularity condition | `step2_nondegeneracy.tex` |

**Three core axioms**: A1, A2, A3.  
**Two regularity conditions**: A4, A5 (define the admissible class $\mathcal{A}_{\mathrm{UBT}}$).

---

## A1 — Algebra Axiom (AXIOM-A)

**Statement**: The fundamental algebraic structure is the **biquaternion algebra**
$$\mathbb{B} := \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}.$$

**Properties**:
- As a real vector space: $\dim_{\mathbb{R}}\mathbb{B} = 8$.
- Canonical algebra isomorphism: $\mathbb{B} \cong \mathrm{Mat}(2,\mathbb{C})$.
- Real Clifford identification: $\mathbb{B} \cong \mathrm{Cl}_{1,3}(\mathbb{R})$.
  This identification is what links the algebra to spacetime geometry.
- The generators of $\mathrm{Cl}_{1,3}(\mathbb{R})$ split into one timelike
  generator $\gamma^0$ and three spacelike generators $\gamma^i$ satisfying
  $(\gamma^0)^2 = -1$, $(\gamma^i)^2 = +1$, $\{\gamma^\mu,\gamma^\nu\} = 2\eta^{\mu\nu}$.

**Why this algebra**: ℍ (Hamilton's quaternions) is the **unique** normed division
algebra of dimension 4 over ℝ containing both a complex structure (for quantum phases)
and a 3D real anti-symmetric structure (for Lorentzian geometry) — by Hurwitz's
theorem.  Tensoring with ℂ extends to the full 8-dimensional structure required by
both quantum mechanics and spacetime.

**Source**: `canonical/fields/biquaternion_algebra.tex`

---

## A2 — Complex Time (AXIOM-B)

**Statement**: Physical time is **complex**:
$$\tau := t + i\psi \in \mathbb{C},$$
where $t \in \mathbb{R}$ is real time and $\psi \in \mathbb{R}$ is the imaginary
phase component.  The complex-time derivative $\partial_\tau$ lies in the
**timelike sector** of $\mathrm{Cl}_{1,3}(\mathbb{R})$:
$$\langle\partial_\tau, \partial_\tau\rangle_\eta < 0.$$

**Consequence** (Theorem 3.3 of `GR_theorem_result.tex`): The derived metric
$g_{\mu\nu}$ has Lorentzian signature $(-,+,+,+)$.  This is a **theorem**, not
an independent postulate.

**Comparison to other frameworks**: Every approach to GR — string theory, LQG,
spinfoam models — requires some structural input to fix the signature.  AXIOM-B
reduces this input from four independent metric sign choices to one axiom about
the timelike nature of the time derivative.

**Source**: `canonical/THEORY/axioms/core_assumptions.tex`

---

## A3 — Field Equation (AXIOM-F)

**Statement**: The fundamental field $\Theta : M^4 \times \mathbb{C}_\tau \to \mathbb{B}$
satisfies the **UBT field equation** (the "T-shirt equation"):
$$\nabla^\dagger\nabla\,\Theta(q,\tau) = \kappa\,\mathcal{T}(q,\tau),$$
where $\nabla^\dagger\nabla$ is the biquaternionic wave operator and
$\mathcal{T}$ is the source (matter/energy) biquaternionic field.

**Role in the GR chain**: This axiom is used in:
- Step 5 (Einstein equations): the action $S_\Theta$ is the action associated with
  this field equation, and the Hilbert variation of the total action yields
  $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$.
- The Schwarzschild derivation: the vacuum equation
  $\nabla^\dagger\nabla\Theta = 0$ fixes the $\Theta_0$ ansatz.

**Source**: `canonical/fields/theta_field.tex`

---

## A4 — Admissibility: Linear Independence

**Statement**: The four partial derivatives $\{\partial_\mu\Theta\}_{\mu=0}^3$ are
**linearly independent over $\mathbb{R}$** in $\mathbb{B}$ at every point of $M^4$.
Equivalently, $\Theta$ is not constant and not confined to a lower-dimensional
spatial subspace.

**Role**: A4 is the condition that ensures $\det(g_{\mu\nu}) \neq 0$ (Step 2,
non-degeneracy).  The Gram matrix of linearly independent vectors is non-degenerate;
this is the entire proof of non-degeneracy.

**Physical interpretation**: A4 rules out degenerate or constant field configurations.
It is automatically satisfied by all physically relevant solutions: non-trivial vacuum,
matter fields, and the Schwarzschild exterior.

**Source**: `canonical/gr_closure/step2_nondegeneracy.tex`

---

## A5 — Regularity: Smoothness and Non-Degeneracy

**Statement**: $\Theta$ is smooth ($C^\infty$) on $M^4$ and holomorphic in $\tau$.
There exists $\varepsilon > 0$ such that $\|\partial_\mu\Theta\| > \varepsilon$ for
all $\mu$ on $M^4$.

**Role**: A5 ensures that all derivative operations in the proof chain are valid
and that the normalisation $\mathcal{N} := \mathrm{Re}[\mathrm{Tr}(\partial_0\Theta\cdot\partial_0\Theta^\dagger)]$
is strictly positive (required for the metric definition in Step 1).

**Source**: `canonical/gr_closure/step2_nondegeneracy.tex`

---

## What Is NOT Assumed

The following quantities are **derived**, not assumed:

| Quantity | Status |
|----------|--------|
| Spacetime metric $g_{\mu\nu}$ | Derived from $\Theta$ (Theorem 3.1) |
| Lorentzian signature $(-,+,+,+)$ | Theorem from AXIOM-B (Theorem 3.3) |
| Non-degeneracy $\det(g)\neq 0$ | Theorem from A4 (Theorem 3.2) |
| Einstein equations $G_{\mu\nu}=8\pi GT_{\mu\nu}$ | Theorem from Hilbert variation (Theorem 3.5) |
| Stress-energy $T_{\mu\nu}$ | Derived from $S_\Theta$ by Hilbert prescription |
| Conservation $\nabla^\mu T_{\mu\nu}=0$ | Theorem from Bianchi + diffeomorphism invariance |

---

## Axiom Count Comparison

| Framework | Core axioms | Scope |
|-----------|-------------|-------|
| Standard GR | Metric field on manifold, equivalence principle, Einstein-Hilbert action, matter coupling | Gravity only |
| Standard Model | Gauge group $G_{\mathrm{SM}}$ (postulated) + matter sector + Higgs sector | SM only |
| UBT (this paper) | A1 (algebra), A2 (complex time), A3 (field equation) | GR + SM + more |

UBT derives more from fewer axioms.

---

## Scope Declaration

These assumptions define the on-shell classical GR sector.  The off-shell closure
(GAP-10) and quantum path-integral formulation (GAP-Q) require additional work beyond
A1–A5.  See `proof_gap_list.md` for the complete gap inventory.
