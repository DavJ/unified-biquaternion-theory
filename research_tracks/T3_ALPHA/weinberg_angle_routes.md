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


# weinberg_angle_routes.md — T3_ALPHA Derivation Program

**Track**: T3_ALPHA — Weinberg Angle Derivation (converted from direct α derivation)  
**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Objective**: Derive $\tan\theta_W = g'/g$ from UBT first principles.  No numerical fitting.  
**Strategic context**: The direct B_base/k=1 route to α has been exhausted (27+ approaches).
This document defines the three-workstream attack plan for the converted target: the
Weinberg angle $\theta_W$.  If $\theta_W$ is derived, $\alpha = g^2 \sin^2\theta_W/(4\pi)$
follows from proved identities.  
**Sources**: `canonical/alpha/weinberg_angle_derivation.md`, `reports/ew_mixing_status.md`,
`alpha_progress_log.md`, `canonical/interactions/sm_gauge.tex`

---

## The Conversion Identity

The key identity enabling the conversion:
$$\alpha = \frac{g^2 \sin^2\theta_W}{4\pi}$$

**Status of this identity**: [L1] PROVED — follows from $e = g\sin\theta_W = g'\cos\theta_W$
and the standard photon field decomposition $A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu$.

**What this means**: If either $\tan\theta_W$ or $\sin^2\theta_W$ is derived from UBT,
and if $g$ is determined (or taken from experiment as a single semi-empirical input),
then $\alpha$ is determined without the B_base/k=1 Kac-Moody calculation.

---

## Starting Point: What Is Already Proved

| Claim | Level | Source |
|-------|-------|--------|
| $\alpha = g^2\sin^2\theta_W/(4\pi)$ | [L1] | `canonical/alpha/gauge_normalization_attempt.tex §3` |
| SU(2)_L from left-unitary action on ℂ⊗ℍ | [L0] | `canonical/interactions/sm_gauge.tex` |
| U(1)_Y from right scalar phase action on ℂ⊗ℍ | [L0] | `canonical/interactions/sm_gauge.tex` |
| Generator norms: $\mathrm{Tr}(\tau^2) = \mathrm{Tr}(Y^2) = 1/2$ in fundamental | [L0] | EW1 computation |
| Photon field $A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu$ | [L1] | Standard EW algebra |
| N_eff = 12 from ℂ⊗ℍ | [L0] | `canonical/n_eff/step1_mode_decomposition.tex` |

**Excluded near-miss**: $g = g'$ (equal norms in doublet representation) gives
$\sin^2\theta_W = 1/2$ — **excluded** by experiment ($\sin^2\theta_W \approx 0.231$).
This closes the simplest algebraic route and establishes that fermion representation
content is the key discriminator.

---

## Three Workstreams

### EW1 — Pure UBT Algebra Route

**Goal**: Fix $g'/g$ from the generator normalizations of SU(2)_L and U(1)_Y within
ℂ⊗ℍ, accounting for the full fermion representation content.

**Key equation**:
$$\frac{g'^2}{g^2} = \frac{\sum_{\mathrm{all reps}} Y_i^2 \cdot \mathrm{dim}(r_i)}{\sum_{\mathrm{all reps}} T_{3,i}^2 \cdot \mathrm{dim}(r_i)}$$

If UBT ψ-winding modes give the same fermion representation content as the SM,
the Georgi-Glashow SU(5) result $g'^2/g^2 = 3/5$ follows from representation
theory without a full GUT embedding.

**Tasks**:
| ID | Description | Status | Blocker |
|----|-------------|--------|---------|
| EW1.A | Derive fermion hypercharge assignments Y from ψ-winding modes | ❌ OPEN | First task to attempt |
| EW1.B | Compute $\sum_{\mathrm{reps}} Y^2$ and $\sum_{\mathrm{reps}} T_3^2$ | ❌ OPEN | Depends on EW1.A |
| EW1.C | Derive $g'/g$ from generator ratio | ❌ OPEN | Depends on EW1.A, EW1.B |

**Best case**: If EW1.A gives the SM fermion hypercharge assignments from ψ-winding,
then EW1.B gives $g'^2/g^2 = 3/5$ (Georgi-Glashow), and $\sin^2\theta_W(M_Z) \approx 0.231$
follows after one-loop RG running.

**Priority**: MEDIUM — depends on solving EW1.A, which is non-trivial.

---

### EW2 — GUT Embedding Route

**Goal**: Test whether ℂ⊗ℍ embeds into SU(5), SO(10), or an internal UBT GUT structure,
giving the boundary condition $\sin^2\theta_W(\mathrm{GUT}) = 3/8$.

**Key algebraic question**: SU(5) gives $\sin^2\theta_W = 3/8$ from the
hypercharge-generator embedding:
$$Y_{\mathrm{SU5}} = \mathrm{diag}\!\left(-\tfrac{1}{3},-\tfrac{1}{3},-\tfrac{1}{3},+\tfrac{1}{2},+\tfrac{1}{2}\right)$$
Does ℂ⊗ℍ naturally produce this generator from its algebraic structure?

**Tasks**:
| ID | Description | Status | Notes |
|----|-------------|--------|-------|
| EW2.A | Test SU(5) embedding of the SM gauge algebra in ℂ⊗ℍ | ❌ OPEN | **Highest-priority first step** |
| EW2.B | Test SO(10) embedding via 16-dim spinor | ❌ OPEN | Alternative if EW2.A fails |
| EW2.C | Investigate internal UBT GUT via complexification | ❌ OPEN | Long-shot; speculative |
| EW2.D | One-loop RG flow: GUT scale → $M_Z$ | ❌ OPEN | Depends on EW2.A–C |

**Best case if EW2.A succeeds**:
$$\sin^2\theta_W(\mathrm{GUT}) = \frac{3}{8} \quad\xrightarrow{\text{1-loop RG}}\quad \sin^2\theta_W(M_Z) \approx 0.231 \quad\Rightarrow\quad \alpha \approx \frac{1}{137}$$

This would be a three-parameter prediction ($M_{\mathrm{GUT}}$, $g(M_{\mathrm{GUT}})$,
$\alpha(M_Z)$) comparable in depth to the original Georgi-Glashow (1974) SU(5) prediction.

**Priority**: **CRITICAL** — most tractable with highest breakthrough probability.
EW2.A is the recommended first attack.

---

### EW3 — Geometric Projection Route

**Goal**: Interpret $\theta_W$ as a geometric projection angle in the internal symmetry
fiber of the $\Theta$-bundle, derivable from the Killing metric of $\mathfrak{g}_{EW}$
induced by $\mathrm{Tr}[(D_\mu\Theta)^\dagger D^\mu\Theta]$.

**Key equation**:
$$\cos\theta_W = \frac{\langle Q, Y \rangle}{\|Q\| \|Y\|}$$
where $Q$ is the electric charge generator and $Y$ is the hypercharge generator,
with the inner product induced by the UBT kinetic term.

**Tasks**:
| ID | Description | Status | Notes |
|----|-------------|--------|-------|
| EW3.A | Compute Killing metric on $\mathfrak{g}_{EW}$ from UBT kinetic term | ❌ OPEN | Most tractable entry point |
| EW3.B | Derive $\cos\theta_W$ from generator inner product | ❌ OPEN | Depends on EW3.A |
| EW3.C | Geometric bundle interpretation | ❌ OPEN | Speculative; conceptual payoff |

**Note**: EW3 requires only a computation on known objects.
The equal-norm result gave $\theta_W = \pi/4$ (excluded).
If the induced Killing metric differs from the flat metric, EW3 could constrain
$\theta_W$ to a different value.

**Priority**: MEDIUM — tractable computation, but the result is not predictable in advance.

---

## Resource Allocation and Schedule

Per the T3_ALPHA 20% global allocation:

| Workstream | Priority | Recommended weeks | Stopping condition |
|-----------|----------|------------------|--------------------|
| EW2.A (SU(5) embedding) | **CRITICAL** | Weeks 1–3 | SU(5) embedding exists or is ruled out |
| EW3.A (Killing metric) | MEDIUM | Weeks 2–4 | $\theta_W$ determined or constrained |
| EW1.A (fermion reps) | MEDIUM | Weeks 3–6 | Y assignments from ψ-winding derived or blocked |
| EW2.B (SO(10)) | LOW | After EW2.A | Only if EW2.A blocked |
| Modular bootstrap M1–M4 | TIME-BOXED | Max 4 weeks | $k=1$ proved or abandoned |

**Global stopping rule**: If none of EW2.A, EW3.A, EW1.A produces a constraint on
$\theta_W$ after 6 weeks, activate the Layer2 coding paper (see `fallback_layer2_outline.md`).

---

## Parallel Track: Modular Bootstrap

The original k=1 Kac-Moody modular bootstrap (Steps M1–M4, `k_equals_1_attack_plan.md`)
continues in parallel, time-boxed to 4 weeks (deadline 2026-05-26).

| Step | Goal | Status |
|------|------|--------|
| M1 | Show $S[\Theta]|_{T^2}$ is a 2D CFT with $c = 3$ | In progress |
| M2 | Compute partition function $\hat{Z}(\tau) = \vartheta_3^3(\tau)$ | Planned |
| M3 | Apply crossing symmetry to constrain $k$ | Planned |
| M4 | Verify $k = 1$ is the unique solution | Planned |

If M1–M4 all succeed: $k=1$ is proved, $B_{\mathrm{base}} = 41.57$ follows,
$\alpha^{-1}_{\mathrm{bare}} = 137$ becomes a zero-parameter result.

---

## Decision Tree

```
EW2.A: SU(5) embedding of ℂ⊗ℍ?
    ├── YES → sin²θ_W(GUT) = 3/8 → RG → sin²θ_W(M_Z) → α  [TARGET MET]
    └── NO  →
              EW3.A: Killing metric on g_EW?
                  ├── CONSTRAINED → θ_W ≠ π/4 → paper on EW sector geometry
                  └── EQUAL NORMS → θ_W = π/4 (excluded) →
                                    EW1.A: fermion Y from ψ-winding?
                                        ├── DERIVED → Georgi-Glashow → α  [TARGET MET]
                                        └── BLOCKED → Layer2 fallback paper
```

---

## Publication Targets

### If EW2.A succeeds (highest-impact outcome)

**Paper title**: *Weinberg Angle from Biquaternion Algebra: SU(5) GUT Boundary from ℂ⊗ℍ*

**Claim hierarchy**:
1. [L0] ℂ⊗ℍ ≅ Mat(2,ℂ) algebraic foundation
2. [L0] SU(2)_L and U(1)_Y in Aut(ℂ⊗ℍ)
3. [L1] SU(5) embedding gives $\sin^2\theta_W(\mathrm{GUT}) = 3/8$ (**new**)
4. [L1] RG flow to $M_Z$ gives $\sin^2\theta_W(M_Z) \approx 0.231$
5. [L1] $\alpha = g^2\sin^2\theta_W/(4\pi)$ follows

**Semi-empirical**: $M_{\mathrm{GUT}}$ from phenomenological running (unless derived from $R_\psi$).

**Target journal**: *Physical Review D* (Letters) or *Physics Letters B*

### If only EW3 gives a partial result

**Paper title**: *Electroweak Mixing Angle from the Biquaternion Kinetic Metric*

Smaller-scope paper; establishes the geometric framework even if $\theta_W$ is
not fully derived.

---

## Gap Registry

| Gap ID | Description | Workstream | Tractability | Priority |
|--------|-------------|-----------|--------------|----------|
| EW-1 | $\tan\theta_W = g'/g$ | EW1/EW2/EW3 | MEDIUM | **CRITICAL** |
| EW-2.A | SU(5) embedding of ℂ⊗ℍ | EW2.A | MEDIUM-HIGH | **CRITICAL** |
| EW-2.B | SO(10) embedding | EW2.B | MEDIUM | HIGH (fallback) |
| EW-3.A | Killing metric on $\mathfrak{g}_{EW}$ | EW3.A | HIGH | HIGH |
| EW-1.A | Fermion Y from ψ-winding | EW1 | LOW-MEDIUM | MEDIUM |
| B-GAP-1 | $k=1$ Kac-Moody (original route) | Bootstrap | LOW | TIME-BOXED |

---

## References

- `canonical/alpha/weinberg_angle_derivation.md` — technical derivation document
- `reports/ew_mixing_status.md` — high-level status report
- `alpha_progress_log.md` — chronological record (Phases 1–4)
- `k_equals_1_attack_plan.md` — modular bootstrap attack plan
- `fallback_layer2_outline.md` — Layer2 coding paper fallback
- `canonical/interactions/sm_gauge.tex` — gauge structure source
- `canonical/alpha/gauge_normalization_attempt.tex` — EW coupling normalization
