# UBT Canonical Axioms

**Status**: LOCKED  
**Purpose**: Canonical definitions that MUST NOT be redefined  
**Date**: February 2026; covariant-tetrad/connection revision authorised 16 July 2026  
**Author**: David Jaroš

---

## Overview

This document defines the **canonical axioms** of the Unified Biquaternion Theory (UBT). These axioms establish the fundamental mathematical structure of the theory and must remain unchanged. Any derivations, computations, or extensions must be consistent with these axioms.

**CRITICAL**: These axioms are LOCKED against modification. Verification, formalization, and derivation of consequences are permitted, but redefinition is forbidden.

---

## AXIOM A: Fundamental Field Object

**Statement**: The fundamental dynamical object of UBT is the biquaternionic field $\Theta(q, \tau)$.

$$\Theta: \mathcal{M} \times \mathbb{C} \to \mathbb{B} \equiv \mathbb{C} \otimes \mathbb{H}$$

**Details**:
- $\Theta(q, \tau)$ is the **only** fundamental field
- Structure: Biquaternionic (complex quaternions) or matrix-valued
- The internal algebraic structure (biquaternionic, spinorial, gauge) belongs to $\Theta$ itself
- No additional fundamental fields, forces, or particles are postulated

**Lock Rule**: $\Theta$ is the unique fundamental object. Do not introduce alternative fundamental fields.

---

## AXIOM B: Complex Time (Final Formulation)

**Statement**: Time in UBT is **complex-valued**, not quaternionic.

$$\tau = t + i\psi \in \mathbb{C}$$

where:
- $t \in \mathbb{R}$ is the real (physical/observable) time coordinate
- $\psi \in \mathbb{R}$ is the imaginary time coordinate (phase space dimension)
- $i$ is the imaginary unit: $i^2 = -1$

**Historical Note**: Earlier exploratory drafts (pre-v0.4) investigated "quaternionic time" as a heuristic device. The **final formulation** uses **complex time only**. Quaternionic structure remains in the field $\Theta$ itself, not in the time coordinate.

**Clarification**:
- Complex time: $\tau = t + i\psi$ ✓ (CANONICAL)
- Quaternionic time: Exploratory only, not in final theory ✗
- The symbol $\psi$ always denotes the imaginary component of complex time
- Do NOT use $\psi$ for wave functions in UBT context (use $\Theta$ instead)

**Lock Rule**: $\tau = t + i\psi$ is the canonical time definition. Do not redefine time as quaternionic or introduce alternative time parametrizations.

---

## AXIOM C: Covariant Tetrad and Central Metric (REVISED 2026-07-16)

**Author-approved statement**: The local geometric carrier is the covariant first jet of the single fundamental field,

$$E_\mu := \mathcal N_0^{-1/2}D_\mu\Theta,$$

where $\mathcal N_0>0$ is a fixed global unit-setting constant.  $D_\mu$ is the covariant derivative in the representation carried by $\Theta$.  The connection used in $D_\mu$ is not an arbitrary additional matter field.  For every nondegenerate tetrad and specified torsion, the metric-compatible frame connection is uniquely reconstructed as

$$\omega=\mathring\omega(e)+K(T),\qquad K_{abc}=\frac12(T_{cab}-T_{abc}-T_{bca}).$$

The torsion-free classical GR branch has $T=K=0$ and the unique Levi--Civita spin connection.  The remaining full-UBT problem is to derive torsion and the exact paired left/right action on $\Theta$ from the canonical action.

Let $i$ denote the commuting complex unit and $\mathbf e_k$ the quaternion units.  The classical Lorentz sector is the real four-dimensional slice

$$W_L=\{i x^0\mathbf 1+x^k\mathbf e_k\mid x^a\in\mathbb R\}\subset\mathbb B.$$

Quaternion conjugation, denoted by $\sharp$, reverses the three quaternion units but does not conjugate the commuting complex coefficient.  For admissible classical configurations $E_\mu\in W_L$, the metric is defined by the full central anticommutator identity

$$\boxed{\frac12\left(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu\right)=g_{\mu\nu}\mathbf1.}$$

This identity is equivalent to

$$g_{\mu\nu}=e_\mu{}^a e_\nu{}^b\eta_{ab},\qquad \eta_{ab}=\operatorname{diag}(-1,1,1,1),$$

when $E_\mu=i e_\mu{}^0\mathbf1+e_\mu{}^k\mathbf e_k$.

**No projection rule**: The symmetrized product is already a real central element.  The metric is therefore not defined by an ordinary trace, `Re(...)`, a phase projector, a preferred $\psi$ section, or a compact-$\psi$ average.

**Companion bivector**:

$$\Sigma_{\mu\nu}:=\frac12\left(E_\mu^\sharp E_\nu-E_\nu^\sharp E_\mu\right)$$

is the antisymmetric algebraic part of the same product.  It may carry oriented-plane/spin information, but it is not automatically a gauge field or curvature.

**Rank theorem**: At every nondegenerate tetrad, the map $e_\mu{}^a\mapsto g_{\mu\nu}$ has rank ten and a six-dimensional kernel consisting of local Lorentz rotations/boosts.  The former comparison $\dim_\mathbb R\mathbb B=8<10$ is not a local metric-rank obstruction because the metric is built from four covariant derivatives, not from the value of $\Theta$ alone.  See `canonical/gr_closure/covariant_tetrad_rank_theorem.tex`.

**Complex-time dependence**: $\Theta$ may depend on $\tau=t+i\psi$.  The local metric formula is pointwise and does not average over $\psi$.  The classical GR sector must have a real, nondegenerate metric and, when required for ordinary four-dimensional observations, a dynamically stable $\psi$-independent metric.  Deriving that stability is open.

**CRITICAL LOCK RULES**:

1. There is no independent background metric.
2. The canonical local metric is the central anticommutator of $D_\mu\Theta$.
3. Do not reintroduce trace/real-part/phase/fiber readouts as the canonical definition.
4. Do not use a local normalization denominator; $\mathcal N_0$ is fixed globally.
5. The connection must not be treated as an arbitrary extra physical field; it is reconstructed from tetrad and torsion.
6. Do not use a naive one-sided regular connection as the generic invertible curved-GR route.
7. The canonical curved research route is the two-sided biquaternionic derivative plus a torsion equation derived from the action.
8. The compact-fiber construction is retained only as a noncanonical candidate-completion branch.

---

## AXIOM D: Classical GR Correspondence (STATUS-DISCIPLINED)

**Statement**: UBT is required to contain a classical Lorentzian sector in which the central metric defined in Axiom C obeys Einstein dynamics or a sharply specified observationally equivalent limit.

The kinematic metric relation, connection reconstruction, and flat affine
representer are proved locally.  The complete dynamical implication

$$\text{canonical UBT equations}\quad\Longrightarrow\quad G_{\mu\nu}=\kappa T_{\mu\nu}$$

is **not yet unconditional**.  The current open tasks are:

- derive vacuum or spin-sourced torsion from the canonical UBT action;
- fix the precise paired left/right connection and involution acting on $\Theta$;
- prove that the complete $\Theta$ dynamics, not only Lorentz parallel transport, preserves the Lorentz slice and central anticommutator condition;
- prove local and global existence of the implicit curved system $D_\mu\Theta=\sqrt{\mathcal N_0}E_\mu$;
- derive the Einstein equations and perturbation bridge from the canonical UBT dynamics rather than from an inserted Einstein--Hilbert branch;
- establish Schwarzschild, Kerr, FRW, and gravitational-wave sectors on shell.

**Proved classical facts**:

- every local Lorentz metric admits a tetrad representation of the Axiom-C form;
- the tetrad-to-metric differential has rank ten at every nondegenerate tetrad;
- specified tetrad and torsion uniquely determine the metric-compatible frame connection;
- the torsion-free classical branch has the unique Levi--Civita spin connection;
- every metric-compatible Lorentz connection preserves $\eta_{ab}$ and the Lorentz slice;
- every constant Lorentz tetrad has an explicit affine single-$\Theta$ representer;
- the naive one-sided invertible torsion-free curved branch is a proved no-go;
- the two-sided derivative has the exact left/right curvature identity and avoids the flatness obstruction.

**Canonical GR gap ledger**:

- **GAP-10K — CLOSED locally:** tetrad-to-metric rank ten.
- **GAP-10Ω-KIN — CLOSED [L1]:** specified $(e,T)$ uniquely determine $\omega$.
- **GAP-10Ω-GR — CLOSED [L1]:** $T=0$ gives the Levi--Civita spin connection.
- **GAP-10T-PALATINI — CLOSED CONDITIONALLY [L1]:** the minimal first-order Cartan equation algebraically determines torsion.
- **GAP-10T-DYN — NARROWED:** derive the minimal branch, exact UBT spin current, normalization, and possible extra torsion invariants.
- **GAP-10L-CONN — CLOSED [L1]:** metric-compatible Lorentz transport preserves the Lorentz slice.
- **GAP-10L-SYM — CLOSED CONDITIONALLY [L1]:** unique $\mathcal J$-equivariant dynamics preserves the Lorentz fixed set.
- **GAP-10L-DYN — NARROWED:** verify canonical equivariance and well-posed uniqueness.
- **GAP-10I-SR — CLOSED [L1]:** affine representer of constant Lorentz tetrads.
- **GAP-10I-1S — CLOSED AS NO-GO [L1]:** one-sided invertible torsion-free curved route forces zero curvature.
- **GAP-10I-2S — NARROWED [L1]:** two-sided curvature intertwining avoids flatness; action-level pairing remains open.
- **GAP-10I-PRESCRIBED — CLOSED [L1]:** specified coefficients admit an exact augmented-holonomy criterion.
- **GAP-10I-CURVED — NARROWED:** self-consistent generation, regularity, and global continuation remain.
- **GAP-10D-PALATINI / UNIQUENESS — CLOSED CONDITIONALLY [L1]:** the conditional infrared endpoint is Einstein--$\Lambda$.
- **GAP-10D — NARROWED:** derive the infrared assumptions, coefficients, and matter action from canonical UBT.
- **GAP-10ψ-KIN / SYM — CLOSED / CLOSED CONDITIONALLY [L1]:** gauge or translation symmetry protects the metric.
- **GAP-10ψ — NARROWED:** derive canonical selection and physical stability.

**Forbidden wording**: Do not state that all GR solutions or the complete Einstein dynamics have already been derived from the original UBT master equation.

---

## Historical Note: Quaternionic/Biquaternionic Time in Early UBT

**Purpose**: This section documents the historical evolution of the time formulation in UBT, explaining why early exploratory drafts considered quaternionic/biquaternionic time structures and why the final formulation uses complex time exclusively.

### Why Quaternionic/Biquaternionic Time Was Originally Introduced

In early development of UBT (pre-v0.4), quaternionic and biquaternionic time structures were explored as candidate formulations:

**Motivations**:
1. **Additional degrees of freedom**: Quaternionic time $T = t_0 + \mathbf{i} t_1 + \mathbf{j} t_2 + \mathbf{k} t_3$ provided four real temporal dimensions, potentially accommodating phase, rotation, and orientation information
2. **Exploratory unification**: Attempt to merge temporal structure with internal symmetries (spin, isospin, color) directly in the time coordinate
3. **Algebraic elegance**: Natural compatibility with biquaternionic field $\Theta$ — quaternionic time paired with quaternionic algebra seemed conceptually unified
4. **Geometric richness**: Quaternion multiplication offered non-commutative temporal evolution, potentially encoding novel physical effects

**Early hypothesis**: If $\Theta$ lives in biquaternionic space, perhaps time itself should have quaternionic structure.

### Problems That Emerged

Through theoretical analysis and attempts at physical interpretation, several fundamental issues became apparent:

**1. Mixing of coordinate and algebraic roles**:
- Time serves as a **coordinate** (external parameter for evolution)
- Quaternionic structure belongs to **internal algebra** (gauge groups, spinors, field dynamics)
- Embedding internal algebra in the time coordinate blurred this essential distinction

**2. Ambiguity of projection and measurement**:
- Physical measurements occur in real time $t \in \mathbb{R}$
- Quaternionic time requires a projection rule: which component is "physical time"?
- Multiple projection schemes are possible, leading to non-uniqueness
- Unclear how measuring apparatus couples to quaternionic temporal structure

**3. Lack of unique imaginary direction**:
- Complex time $\tau = t + i\psi$ has a unique imaginary direction (orthogonal to real time)
- Quaternionic time has **three** imaginary directions $(\mathbf{i}, \mathbf{j}, \mathbf{k})$
- No natural physical principle selects one over others for $\psi$-like phase evolution
- Results in redundant or ambiguous degrees of freedom

**4. Difficulties for black hole horizons and radiation**:
- Hawking-like radiation mechanism in UBT requires clear $\tau \to t$ projection (complex → real time)
- Quaternionic time complicates horizon structure: which imaginary component defines the thermal temperature?
- Phase space interpretation ($\psi$ as momentum conjugate to $t$) becomes unclear with three extra dimensions
- Thermal equilibrium and canonical ensemble formulation become ambiguous

**5. Overconstrained field equations**:
- Field equations in quaternionic time $(D_T \Theta = 0)$ impose more constraints than physically motivated
- Led to overly rigid solutions incompatible with observed particle spectra

### Why the Final Formulation Uses Complex Time

After extensive analysis, the **complex time formulation** $\tau = t + i\psi$ was adopted as canonical for the following reasons:

**1. Clean separation of structures**:
- **Time**: Complex coordinate $\tau = t + i\psi$ (external evolution parameter)
- **Field**: Biquaternionic $\Theta \in \mathbb{C} \otimes \mathbb{H}$ (internal algebraic structure)
- This separation clarifies which degrees of freedom are geometric (spacetime) vs internal (gauge/spin)

**2. Unique imaginary component $\psi$**:
- Complex time provides exactly **one** imaginary direction
- $\psi$ serves as the canonical phase space coordinate conjugate to real time $t$
- Enables clear $\tau \to t$ projection: $t = \text{Re}[\tau]$, $\psi = \text{Im}[\tau]$
- No ambiguity in defining the "imaginary time direction"

**3. Consistency with quantum measurement**:
- Wave function evolution in imaginary time is well-established in quantum mechanics (Wick rotation)
- Complex time $\tau$ naturally accommodates both:
  - Real-time Schrödinger evolution
  - Imaginary-time path integral formulation
- Quaternionic time would require additional projection rules incompatible with standard QM

**4. Black hole radiation and thermodynamics**:
- Hawking temperature $T_H = \frac{\hbar}{2\pi k_B \psi_H}$ emerges naturally from imaginary time period
- Horizon structure: bifurcation at $\psi = 0$ surface
- Thermal radiation: KMS boundary condition on complex time contour
- These mechanisms require unique imaginary direction — provided by complex time, not quaternionic

**5. Quaternionic structure preserved in $\Theta$**:
- All quaternionic/biquaternionic richness is retained in the **field** $\Theta(q,\tau)$
- $\Theta$ carries gauge groups, spinor structure, non-Abelian dynamics
- Separation ensures mathematical structure serves physics, not vice versa

**6. Simplicity and empirical adequacy**:
- Complex time formulation yields correct predictions for:
  - Fine structure constant $\alpha$
  - Particle masses (electrons, neutrinos, quarks)
  - Black hole thermodynamics
  - Quantum corrections to GR
- No empirical evidence requires quaternionic time; complex time suffices

### Concluding Statement

**Quaternionic/biquaternionic time** was a valuable **historical and heuristic stage** in the development of UBT. It served as an exploratory framework that:
- Revealed the importance of internal algebraic structure (which resides in $\Theta$)
- Clarified the role of imaginary time $\psi$ as a phase space coordinate
- Demonstrated that time's role as an evolution parameter is best kept simple and unique

**Complex time** $\tau = t + i\psi$ is the **final, stable, and canonical formulation** of UBT. This choice:
- Maintains mathematical clarity (separation of coordinate vs algebra)
- Ensures physical measurability (unique real time projection)
- Provides sufficient structure for all known physics
- Preserves quaternionic/biquaternionic richness in the fundamental field $\Theta$ where it belongs

**Status**: Quaternionic time remains discussed in theoretical appendices (e.g., Appendix N2) as an **extended formalism** for specialized contexts (e.g., consciousness modeling, extreme rotating spacetimes), but it is **not part of the core canonical UBT formulation** defined by the four axioms above.

All references to "biquaternionic time" in UBT literature should be understood in this context: either as historical exploration or as specialized theoretical extensions beyond the canonical complex-time framework.

---

## AI / Copilot Guardrails

**Purpose**: These guidelines prevent accidental violation of canonical axioms during automated code assistance, refactoring, or AI-assisted development.

### Permitted Actions ✓

Copilot and AI assistants **MAY**:
1. **Verify** that existing equations are consistent with axioms
2. **Compute** consequences of axioms (curvature tensors, field equations, etc.)
3. **Derive** physical predictions from the canonical framework
4. **Formalize** existing definitions mathematically
5. **Cross-reference** axioms across documents
6. **Extend** to new domains while preserving axioms (e.g., cosmology, dark sector)

### Forbidden Actions ✗

Copilot and AI assistants **MUST NOT**:
1. **Redefine** $\tau$ or change $\tau = t + i\psi$ to any other form
2. **Redefine** $\psi$ or use it for anything other than imaginary time component
3. **Redefine** $\Theta$ or introduce alternative fundamental fields
4. **Introduce** a new metric definition (no "effective metric", "background metric", "metric v2")
5. **Add** quaternionic time in the final theory (historical only)
6. **Replace** the emergent metric formula (Axiom C)
7. **Treat** GR as independent from UBT (it's a limit/projection)
8. **Invent** new physics not derivable from the four axioms above

### Violation Detection

If any of the following patterns appear in code or documentation, it indicates a potential axiom violation:

**Forbidden patterns** (case-insensitive search):
- `effective_metric` (unless clearly referring to the GR limit of Axiom C's metric)
- `background_metric` 
- `metric_v2`, `metric_version_2`
- `g0_mu_nu`, `g_0_{\mu\nu}` (as fundamental/background metric)
- `metric_hat`, `\hat{g}` (as alternative metric definition)
- `quaternionic_time` (in final formulation)
- `redefine.*Theta`, `alternative.*field.*Theta`

**Warning patterns** (require careful review):
- `new.*metric.*definition`
- `modify.*tau.*definition`
- `psi.*wave.*function` (in UBT context; should be $\Theta$)

### Enforcement

The axiom locks are enforced by:
1. **Documentation**: This file (`core/AXIOMS.md`)
2. **Automated test**: `tests/test_metric_lock.py` (or `tools/metric_lock_check.py`)
3. **Code review**: Human verification during PR review
4. **CI/CD**: Automated checks run on every commit

If you are a human developer or AI assistant and need to make a change that might violate an axiom, **STOP** and consult with the repository maintainer (David Jaroš) before proceeding.

---

## Mathematical Summary

For quick reference, the core equations are:

1. **Fundamental field**: $\Theta(q, \tau) \in \mathbb{C} \otimes \mathbb{H}$
2. **Complex time**: $\tau = t + i\psi \in \mathbb{C}$
3. **Covariant tetrad and central metric**: $E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta$ and $\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1$
4. **Classical correspondence target**: derive the conditionally identified Einstein--$\Lambda$ infrared endpoint, its coefficients and matter terms from the canonical UBT action; GAP-10D is narrowed but not fully closed

All further UBT sectors must be compatible with these canonical structures.  The complete Einstein and Standard-Model dynamics are derivation targets, not consequences to be assumed.

---

## Versioning and Changes

**Current Version**: 1.0 (February 2026)  
**Change Policy**: These axioms are **LOCKED**. Changes require:
1. Explicit approval from David Jaroš
2. Major version increment
3. Full impact analysis across all UBT documents
4. Update to all cross-references

**History**:
- v1.0 (Feb 2026): Initial canonical axioms document
- Pre-v0.4: Exploratory phase (quaternionic time considered, not adopted)
- v0.4+: Complex time finalized
- 2026-07-16: Projection-free covariant tetrad, connection reconstruction, and partial integrability formalized

---

## Cross-References

This axiom document is referenced by:
- `consolidation_project/appendix_FORMAL_qm_gr_unification.tex`
- `consolidation_project/appendix_FORMAL_emergent_metric.tex`
- `consolidation_project/appendix_FORMAL_black_hole_radiation.tex`
- `consolidation_project/appendix_FORMAL_constants_normalization.tex`
- `consolidation_project/FORMAL_VERIFICATION_FRAMEWORK.md`
- `THETA_FIELD_DEFINITION.md`
- `UBT_CORE_VERIFICATION_REPORT.md`

---

**License**: CC BY-NC-ND 4.0  
**Author**: Ing. David Jaroš  
**Repository**: unified-biquaternion-theory  
**Last Updated**: July 16, 2026
