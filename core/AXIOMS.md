# UBT Canonical Axioms

**Status**: LOCKED  
**Purpose**: Canonical definitions that MUST NOT be redefined  
**Date**: February 2026  
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

## AXIOM C: Unique Emergent Metric (LOCKED)

**Statement**: The spacetime metric is **emergent** from $\Theta$, defined uniquely through a two-level structure:

**Two-Level Notation**:

$$\mathcal{G}_{\mu\nu}(x,\tau) := (D_\mu \Theta(x,\tau))^\dagger D_\nu \Theta(x,\tau)$$

$$g_{\mu\nu}(x) := \text{Re}\left[\mathcal{G}_{\mu\nu}(x,\tau)\right]$$

where:
- $\mathcal{G}_{\mu\nu}$ is the **complex/biquaternionic metric object** (full structure including imaginary components)
- $g_{\mu\nu}$ is the **observable GR metric** (real-projected spacetime metric)
- $D_\mu$ is the gauge-covariant derivative acting on $\Theta$
- $(\cdot)^\dagger$ denotes the biquaternionic adjoint (conjugate transpose)
- $\text{Re}[\cdot]$ denotes taking the real part (projection to real spacetime)
- The metric is normalized to have signature $(-,+,+,+)$ in the classical limit

**Critical Distinction**:
- $\mathcal{G}_{\mu\nu}$ is **NOT an independent spacetime metric**; it is the intermediate biquaternionic construct before real projection
- $g_{\mu\nu}$ is the **unique, real-projected spacetime metric** used in General Relativity
- There is no additional metric beyond this construction

**Equivalent Forms** (allowed):
- Combined form: $g_{\mu\nu} = \text{Re}[(D_\mu \Theta)^\dagger D_\nu \Theta]$ (direct definition)
- With explicit normalization: $g_{\mu\nu} = \text{Re}[(D_\mu \Theta)^\dagger D_\nu \Theta]/\mathcal{N}$
- With inner product notation: $g_{\mu\nu} = \langle D_\mu \Theta | D_\nu \Theta \rangle_{\text{Re}}$
- Component form: $g_{\mu\nu} = \text{Re}[\partial_\mu \Theta^\dagger \cdot \partial_\nu \Theta + \ldots]$

**CRITICAL LOCK RULES**:
1. **NO background metric**: There is no fundamental metric $g^{(0)}_{\mu\nu}$ that $\Theta$ propagates on
2. **NO alternative metrics**: Do not define "effective metric", "metric v2", $\hat{g}_{\mu\nu}$, $g'_{\mu\nu}$, etc.
3. **NO metric redefinition**: The formula above is canonical and unique
4. **Emergent only**: The metric is a derived quantity, not a fundamental field
5. **$\mathcal{G}_{\mu\nu}$ is not a metric**: The complex object $\mathcal{G}_{\mu\nu}$ is an intermediate construction, not a separate spacetime metric

**Cross-References**:
- `consolidation_project/appendix_A_biquaternion_gravity_consolidated.tex` (line 56)
- `consolidation_project/appendix_R_GR_equivalence.tex` (equation 68)
- `consolidation_project/appendix_FORMAL_emergent_metric.tex` (Definition 3.1)
- `THETA_FIELD_DEFINITION.md` (Section 7.1)

**Lock Rule**: This is the **ONLY** metric definition in UBT. No alternatives, no background metric, no "metric v2".

---

## AXIOM D: General Relativity as Classical Limit

**Statement**: General Relativity (Einstein's field equations) emerges as the **real-projected, classical regime** of UBT.

$$G_{\mu\nu} \equiv R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \kappa T^{(\Theta)}_{\mu\nu}$$

where:
- $G_{\mu\nu}$ is the Einstein tensor computed from the emergent metric $g_{\mu\nu}$ (Axiom C)
- $R_{\mu\nu}$, $R$ are the Ricci tensor and scalar computed using standard differential geometry
- $T^{(\Theta)}_{\mu\nu} = \text{Re}[\mathcal{T}_{\mu\nu}]$ is the effective stress-energy derived from $\Theta$ dynamics
- $\kappa = 8\pi G/c^4$ is Einstein's gravitational constant

**Key Principles**:
- GR is **derived**, not postulated
- Einstein equations are an **effective description** in appropriate limits:
  - Real time projection: $\psi \to 0$ or $\psi$-averaged
  - Classical regime: Large-scale, slowly varying fields
  - Weak coupling: Small quantum corrections
- UBT **generalizes** GR; it does not contradict it
- All GR solutions (Schwarzschild, Kerr, FRW, etc.) emerge from appropriate $\Theta$ configurations

**GR as Real/Classical Limit** (explicit clarification):

General Relativity is recovered from UBT when two conditions are met:

1. **Real projection**: The observable metric $g_{\mu\nu}$ is obtained by taking the real part of $\mathcal{G}_{\mu\nu}$ (Axiom C). Imaginary components of the biquaternionic metric structure remain invisible to classical gravitational measurements.

2. **Classical/slow variation regime**: The $\psi$-dynamics (imaginary time evolution) is either:
   - Not directly observable (ordinary matter couples only to real metric $g_{\mu\nu}$)
   - Varies slowly compared to physical processes
   - Averaged over in the classical limit

In this limit, UBT exactly reproduces Einstein's field equations with the emergent metric $g_{\mu\nu}$ serving as the GR spacetime metric. The additional biquaternionic degrees of freedom represent phase curvature and nonlocal energy configurations that extend beyond classical GR but reduce to it when these effects are negligible or unobservable.

**Lock Rule**: GR is a limit/projection of UBT, not an independent framework. Do not introduce GR as a separate theory requiring separate metric.

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
3. **Emergent metric**: $g_{\mu\nu} = \text{Re}[(D_\mu \Theta)^\dagger D_\nu \Theta]$
4. **Einstein equations**: $G_{\mu\nu}[g] = \kappa T^{(\Theta)}_{\mu\nu}$

Everything else in UBT (quantum mechanics, gauge fields, constants, etc.) is derived from these four canonical axioms.

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
- v0.4+: Complex time finalized, emergent metric formalized

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
**Last Updated**: February 10, 2026
