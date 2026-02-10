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

**Statement**: The spacetime metric is **emergent** from $\Theta$, defined uniquely as:

$$g_{\mu\nu}(x) := \text{Re}\left[(D_\mu \Theta(x,\tau))^\dagger D_\nu \Theta(x,\tau)\right]$$

where:
- $D_\mu$ is the gauge-covariant derivative acting on $\Theta$
- $(\cdot)^\dagger$ denotes the biquaternionic adjoint (conjugate transpose)
- $\text{Re}[\cdot]$ denotes taking the real part (projection to real spacetime)
- The metric is normalized to have signature $(-,+,+,+)$ in the classical limit

**Equivalent Forms** (allowed):
- With explicit normalization: $g_{\mu\nu} = \text{Re}[(D_\mu \Theta)^\dagger D_\nu \Theta]/\mathcal{N}$
- With inner product notation: $g_{\mu\nu} = \langle D_\mu \Theta | D_\nu \Theta \rangle_{\text{Re}}$
- Component form: $g_{\mu\nu} = \text{Re}[\partial_\mu \Theta^\dagger \cdot \partial_\nu \Theta + \ldots]$

**CRITICAL LOCK RULES**:
1. **NO background metric**: There is no fundamental metric $g^{(0)}_{\mu\nu}$ that $\Theta$ propagates on
2. **NO alternative metrics**: Do not define "effective metric", "metric v2", $\hat{g}_{\mu\nu}$, $g'_{\mu\nu}$, etc.
3. **NO metric redefinition**: The formula above is canonical and unique
4. **Emergent only**: The metric is a derived quantity, not a fundamental field

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

**Lock Rule**: GR is a limit/projection of UBT, not an independent framework. Do not introduce GR as a separate theory requiring separate metric.

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
