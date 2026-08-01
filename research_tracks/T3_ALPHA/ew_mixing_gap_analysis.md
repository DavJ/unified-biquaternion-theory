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


# ew_mixing_gap_analysis.md — T3_ALPHA Electroweak Mixing Gap Analysis

**Track**: T3_ALPHA — Weinberg Angle Derivation Program  
**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Purpose**: Detailed gap analysis for the electroweak mixing sector of UBT.
Identifies every open sub-problem, its precise obstruction, status of each
attack approach, and the minimum closure requirement for publication.  
**Companion**: `weinberg_angle_routes.md` (attack plan), `reports/ew_mixing_status.md`

---

## Problem Statement

**Target**: Derive $\tan\theta_W = g'/g$ from UBT axioms without numerical fitting.

**Acceptance criterion**: No parameter is chosen to reproduce $\sin^2\theta_W \approx 0.231$.
The derivation must be falsifiable: if UBT gives a different value, that constitutes
a scientific failure.

**Why this is the right target**:
- The original $\alpha$ derivation via B_base / k=1 has been blocked after 27+
  approaches (documented in `alpha_progress_log.md §Phase 2`).
- The EW conversion exploits proved identities: $\alpha = g^2\sin^2\theta_W/(4\pi)$.
- $\theta_W$ is a dimensionless mixing angle — a more natural output from an algebraic
  construction than a small coupling constant like $\alpha$.

---

## Summary of Proved Identities (No Gaps)

These are the starting scaffolding for all gap-closure work.

| Identity | Level | Source |
|----------|-------|--------|
| $e = g\sin\theta_W = g'\cos\theta_W$ | [L1] | `canonical/alpha/gauge_normalization_attempt.tex §3` |
| $\alpha = g^2\sin^2\theta_W/(4\pi)$ | [L1] | From above |
| $A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu$ | [L1] | Standard EW algebra |
| SU(2)_L in ℂ⊗ℍ: $\{U \in \mathrm{Mat}(2,\mathbb{C}) : U^\dagger U = I, \det U = 1\}$ | [L0] | `canonical/interactions/sm_gauge.tex` |
| U(1)_Y in ℂ⊗ℍ: right scalar phase $\Theta \mapsto \Theta \cdot e^{i\phi}$ | [L0] | `canonical/interactions/sm_gauge.tex` |
| $\mathrm{Tr}(\tau^a\tau^b) = \frac{1}{2}\delta^{ab}$ (SU(2)_L generators, fundamental) | [L0] | Standard algebra |
| $\mathrm{Tr}(Y^2) = \frac{1}{2}$ (U(1)_Y, normalised fundamental) | [L0] | Normalisation convention |

---

## Gap EW-1: tan θ_W = g'/g

**Description**: The value of the Weinberg angle is not derived from ℂ⊗ℍ.

**Precise obstruction**: The ratio $g'/g$ depends on the relative normalisation of
the SU(2)_L and U(1)_Y kinetic terms, which in turn depends on the fermion
representation content.  The abstract algebra ℂ⊗ℍ fixes the gauge group but
not the normalisation of the kinetic terms relative to each other — this requires
knowing which representations the fermions occupy.

**Obstruction map**:
$$\frac{g'^2}{g^2} = \frac{\sum_i Y_i^2 \cdot d_i}{\sum_i T_{3,i}^2 \cdot d_i}$$
where the sum is over all fermion representations with hypercharge $Y_i$,
isospin $T_{3,i}$, and dimension $d_i$.  This ratio is not fixed by the abstract
algebra — it requires knowledge of the fermion content.

### Sub-gap EW-1.A: Fermion Hypercharge Assignments from ψ-Winding

**Status**: ❌ OPEN (not yet attempted)

**What is needed**: Show that the hypercharge assignments $Y$ of the SM fermions
(quarks and leptons) are determined by the ψ-winding mode quantum numbers on the
imaginary time circle $\psi \sim \psi + 2\pi$.

**Current knowledge**: 
- Three generations from $\dim_\mathbb{R}(\mathrm{Im}\mathbb{H}) = 3$ [L0 proved]
- Quarks in fundamental **3** of SU(3)_c [L0 proved]  
- Leptons carry no colour charge [algebraically consistent, not derived from UBT]
- **Not derived**: The hypercharge quantum numbers $Y = -1/3$ (quarks), $Y = -1$ (leptons), etc.

**Potential route**: The ψ-winding mode number $n \in \mathbb{Z}$ may determine
$Y$ via $Y = n/6$ or a similar formula.  If the fermion representations fill the
ψ-winding spectrum compatibly with the SM hypercharge assignments, EW-1.A is closed.

**Difficulty**: MEDIUM — requires careful matching of ψ-winding quantum numbers to SM
hypercharge assignments.  No known obstruction, but the calculation has not been done.

---

### Sub-gap EW-1.B: g'/g from Generator Ratio

**Status**: ❌ OPEN (blocked by EW-1.A)

**What is needed**: Given EW-1.A, compute the ratio
$$\frac{g'^2}{g^2} = \frac{\sum_i Y_i^2 d_i}{\sum_i T_{3,i}^2 d_i}$$
using the SM fermion content or the UBT-derived fermion content.

**Known result if SM fermion content is used**:
$$\frac{g'^2}{g^2} = \frac{3}{5} \quad\Longrightarrow\quad \sin^2\theta_W(\mathrm{GUT}) = \frac{3}{8}$$
This is the Georgi-Glashow SU(5) result.  If UBT gives the same fermion content
as the SM, EW-1.B follows immediately.

---

## Gap EW-2: SU(5) / GUT Embedding

**Description**: The embedding of SU(2)_L × U(1)_Y into a larger group
within ℂ⊗ℍ has not been investigated.

### Sub-gap EW-2.A: SU(5) Embedding

**Status**: ❌ OPEN (highest priority, fresh)

**What is needed**: Determine whether the SM gauge algebra
$\mathfrak{su}(3) \oplus \mathfrak{su}(2)_L \oplus \mathfrak{u}(1)_Y$
can be embedded into $\mathfrak{su}(5)$ using the algebraic structure of ℂ⊗ℍ.

**Key algebraic test**: SU(5) has rank 4 and dimension 24.
ℂ⊗ℍ has real dimension 8.  Direct containment of SU(5) in ℂ⊗ℍ is impossible
($\dim_\mathbb{R}\mathfrak{su}(5) = 24 > 8$).

However, the question is whether **the generator structure** of SU(5) is
encoded in ℂ⊗ℍ in the same way that SU(3) is encoded via ℤ₂×ℤ₂×ℤ₂ involutions:
not a direct subgroup, but an algebraic realisation in a larger space.

**Possible route**: The tensor product
$$(\mathbb{C}\otimes\mathbb{H}) \otimes (\mathbb{C}\otimes\mathbb{H}) \cong \mathrm{Mat}(4,\mathbb{C})$$
has real dimension 32 and may contain $\mathfrak{su}(5)$ as a sub-Lie-algebra.
If the SM fermion representations decompose according to the SU(5) multiplet
structure, the GUT boundary condition $\sin^2\theta_W = 3/8$ follows.

**Difficulty**: MEDIUM — requires systematic search in Mat(4,ℂ) for the SU(5) generators.

---

### Sub-gap EW-2.B: SO(10) Embedding

**Status**: ❌ OPEN (fallback to EW-2.A)

**What is needed**: Test whether the SM+right-handed neutrinos (16-plet of SO(10))
fit within the ψ-winding mode structure of ℂ⊗ℍ.  SO(10) also predicts
$\sin^2\theta_W = 3/8$ at the GUT scale.

**Difficulty**: MEDIUM-HIGH — the 16-dimensional SO(10) spinor representation
is significantly larger than the ℂ⊗ℍ algebra.

---

## Gap EW-3: Geometric Projection Route

### Sub-gap EW-3.A: Killing Metric on $\mathfrak{g}_{EW}$ from UBT Kinetic Term

**Status**: ❌ OPEN (tractable)

**What is needed**: Compute the inner product on $\mathfrak{g}_{EW} = \mathfrak{su}(2)_L \oplus \mathfrak{u}(1)_Y$ induced by the UBT kinetic term
$$K(X,Y) = \mathrm{Tr}\!\left[(D_\mu\Theta)^\dagger D^\mu\Theta\right]\Big|_{X,Y}$$
where $D_\mu = \partial_\mu + W^a_\mu \tau^a + B_\mu Y$ is the EW covariant derivative.

**What is already known**:
- In the fundamental (doublet) representation with equal normalisation: $K(\tau^a, \tau^b) = g^2\delta^{ab}/2$, $K(Y,Y) = g'^2/2$.
- The equal-norm assumption ($g = g'$) gives $K(\tau^a,\tau^a) = K(Y,Y)$, so $\theta_W = \pi/4$.
- This is **excluded** ($\sin^2\theta_W = 1/2$; experiment gives 0.231).

**What EW-3.A adds**: If the UBT kinetic term evaluated on the **full fermion
content** (quarks + leptons, all three generations) gives $K(\tau^a,\tau^a)/K(Y,Y) \neq 1$,
then EW-3.A constrains $\theta_W \neq \pi/4$.

**Difficulty**: LOW-MEDIUM — this is a direct computation on known algebraic objects
once the fermion content is specified.  The main obstacle is EW-1.A (hypercharge
assignments).

---

## Confirmed Dead Ends

These routes have been definitively ruled out as paths to $\theta_W$:

| Route | Why it fails |
|-------|-------------|
| $g = g'$ (equal norms in doublet) | Gives $\sin^2\theta_W = 1/2$; excluded by experiment |
| Direct derivation from three axioms (A, B, F) without representation content | $g'/g$ is representation-theory dependent; axioms alone do not fix it |
| B_base / k=1 route (original α program) | 27+ approaches exhausted; documented in `alpha_progress_log.md §Phase 2` |

---

## Minimum Closure Requirement for Publication

A paper on the EW mixing angle in UBT is publishable if **any one** of the following
is achieved:

| Closure | Content | Journal |
|---------|---------|---------|
| EW-2.A succeeds | $\sin^2\theta_W(\text{GUT}) = 3/8$ from ℂ⊗ℍ | *Phys. Rev. D* Letters |
| EW-1.A + EW-1.B succeed | $g'/g$ from ψ-winding fermion representations | *Phys. Rev. D* or *JHEP* |
| EW-3.A constrains $\theta_W$ | Geometric bound on mixing angle | *J. Math. Phys.* |

Even if none closes: a **negative result paper** (UBT cannot derive $\theta_W$
without fermion hypercharge input, and here is the precise obstruction) is
publishable and scientifically valuable.

---

## Gap Status Matrix

| Gap | Description | Level | Status | Priority |
|-----|-------------|-------|--------|----------|
| EW-1 | $\tan\theta_W = g'/g$ | [OPEN] | ❌ | CRITICAL |
| EW-1.A | Fermion Y from ψ-winding | [OPEN] | ❌ | CRITICAL (prerequisite) |
| EW-1.B | $g'/g$ from generator ratio | [OPEN] | ❌ | HIGH (depends EW-1.A) |
| EW-2.A | SU(5) embedding of ℂ⊗ℍ | [OPEN] | ❌ | **CRITICAL (recommended first)** |
| EW-2.B | SO(10) embedding | [OPEN] | ❌ | HIGH (fallback) |
| EW-3.A | Killing metric on $\mathfrak{g}_{EW}$ | [OPEN] | ❌ | HIGH (parallel) |
| EW-3.B | $\cos\theta_W$ from generator inner product | [OPEN] | ❌ | MEDIUM |
| EW-2.C | Internal UBT GUT | [OPEN/SPECULATIVE] | ❌ | LOW |
| $g = g'$ (excluded) | Equal norms | [DEAD END] | ✅ tested | — |

---

## Impact on Existing Results

**No impact on T1_GR**: The GR derivation chain is independent of $\theta_W$.

**No impact on T2_GAUGE proved results**: The SU(3), SU(2)_L, U(1)_Y
algebraic derivations (Theorems G.A–G.D) are independent of $\theta_W$.

**Replaces B_base strategy**: The EW conversion supersedes the k=1 Kac-Moody
approach as the primary T3_ALPHA strategy.

---

## References

- `weinberg_angle_routes.md` — three-workstream attack plan
- `canonical/alpha/weinberg_angle_derivation.md` — technical derivation document
- `reports/ew_mixing_status.md` — high-level status
- `alpha_progress_log.md §Phase 3–4` — EW conversion decision record
- `canonical/interactions/sm_gauge.tex` — SM gauge structure source
- `canonical/alpha/gauge_normalization_attempt.tex` — EW coupling normalization
- `research_tracks/T2_GAUGE/gauge_exactly_proved_vs_open.md §5` — EW sector in T2_GAUGE
