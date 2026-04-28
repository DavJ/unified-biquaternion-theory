<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Weinberg Angle Derivation in UBT

**File**: `canonical/alpha/weinberg_angle_derivation.md`  
**Track**: T3_ALPHA (converted) — Electroweak Mixing Problem  
**Goal**: Derive $\tan\theta_W = g'/g$ from first principles in UBT.  No numerical fitting.  
**Date**: 2026-04-28  
**Priority**: CRITICAL  
**Sources**: `canonical/interactions/sm_gauge.tex`,
`canonical/alpha/gauge_normalization_attempt.tex`,
`canonical/alpha/symmetry_breaking_alpha_attempt.tex`,
`canonical/algebra/involutions_Z2xZ2xZ2.tex`,
`reports/ew_mixing_status.md`

---

## Context: Why This Is the Right Problem

The fine-structure constant satisfies:
$$\alpha = \frac{e^2}{4\pi} = \frac{g^2 \sin^2\theta_W}{4\pi}$$

where $e = g\sin\theta_W = g'\cos\theta_W$.  The two previous blocking gaps in
the α derivation were:

1. **B_base gap**: Prove k=1 for the Kac-Moody level (27+ approaches exhausted).
2. **δ gap**: Derive the 0.036 correction without α, m_e as inputs.

Both gaps are bypassed if $\tan\theta_W = g'/g$ is derived algebraically from
$\mathbb{C}\otimes\mathbb{H}$:
$$\tan\theta_W = \frac{g'}{g} \;\Longrightarrow\; \sin^2\theta_W \;\Longrightarrow\;
\alpha = \frac{g^2\sin^2\theta_W}{4\pi}$$
(with $g$ from canonical normalization, no fitting).

**Acceptance criterion**: A derivation is accepted if and only if:
1. No number is chosen to reproduce $\sin^2\theta_W \approx 0.231$.
2. The ratio $g'/g$ emerges from the algebraic structure of $\mathbb{C}\otimes\mathbb{H}$,
   the representation theory of SU(2)_L × U(1)_Y within Aut(ℂ⊗ℍ), or a GUT
   embedding — not from experiment.
3. Every step is explicitly referenced to a proof file.

---

## Known Starting Points

### Proved results (imported from `gauge_exactly_proved_vs_open.md`)

| Claim | Status | Source |
|-------|--------|--------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) ≅ Cl₁,₃(ℝ) | [L0] | `canonical/fields/biquaternion_algebra.tex` |
| SU(2)_L from left norm-preserving action on Mat(2,ℂ) | [L0] | `canonical/interactions/sm_gauge.tex` |
| U(1)_Y from right scalar phase action | [L0] | `canonical/interactions/sm_gauge.tex` |
| Photon field $A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu$ | [L1] | Standard EW algebra |
| $e = g\sin\theta_W = g'\cos\theta_W$ | [L1] | Standard EW algebra; `gauge_normalization_attempt.tex` |
| $\tan\theta_W = g'/g$ — **value not derived** | [SE] | Experiment: $\sin^2\theta_W \approx 0.231$ |

### The gap

**Gap EW-1** (from `canonical/alpha/alpha_derivation_routes.md §Route A2`):

> Derive the ratio $g'/g$ of the SU(2)_L and U(1)_Y coupling constants from the
> biquaternion algebra representation theory.

---

## Workstream EW1 — Pure UBT Algebra Route

**Question**: Do the generator normalizations of SU(2)_L and U(1)_Y within
ℂ⊗ℍ fix the ratio $g'/g$?

### Generator Norms in Mat(2,ℂ)

In ℂ⊗ℍ ≅ Mat(2,ℂ), the SU(2)_L generators are $\tau^i = \sigma^i/2$:
$$\mathrm{Tr}(\tau^i \tau^j) = \tfrac{1}{2}\delta^{ij}$$

The U(1)_Y generator in the fundamental (doublet) representation is $Y = \tfrac{1}{2}I$:
$$\mathrm{Tr}(Y^2) = \mathrm{Tr}\bigl((\tfrac{1}{2}I)^2\bigr) = \tfrac{1}{4}\mathrm{Tr}(I) = \tfrac{1}{2}$$

The two normalizations are **equal**:
$$\mathrm{Tr}(Y^2) = \mathrm{Tr}(\tau^i \tau^i) = \tfrac{1}{2} \quad (\text{no sum})$$

This equality, combined with the canonical kinetic term
$\mathrm{Tr}[(D_\mu\Theta)^\dagger D^\mu\Theta]$, would give $g' = g$ at the
fundamental scale, hence $\tan\theta_W = 1$ and $\sin^2\theta_W = 1/2$.

**Experimental value**: $\sin^2\theta_W \approx 0.231 \neq 1/2$.

### EW1 Verdict: $g' = g$ Route is Excluded

The naive equal-norm computation gives $\sin^2\theta_W = 1/2$, excluded by
experiment.  The equal-norm result is recorded as a tested near-miss:
`reports/alpha_no_fit_audit.md §Near-misses`.

### EW1 — Refined Strategy: Representation Mismatch

The standard norm computation above assumes the fundamental (2-dim) representation
of both SU(2)_L and U(1)_Y.  However, in the SM and in UBT:

- SU(2)_L acts on the left-chiral doublet (2-dim): correct normalisation
  $\mathrm{Tr}(\tau^i\tau^j) = \delta^{ij}/2$.
- U(1)_Y must also include the **singlet** representations (right-handed fermions),
  which carry only hypercharge, not isospin.

The full generator norm across all SM representations (in one generation) is:

$$\mathrm{Tr}[\text{all reps}]\,(Y^2)
= 3\left[2\left(\tfrac{1}{6}\right)^2 + \left(\tfrac{2}{3}\right)^2 + \left(\tfrac{1}{3}\right)^2\right]
+ 2\left(\tfrac{1}{2}\right)^2 + 1^2 = \tfrac{10}{3}$$

$$\mathrm{Tr}[\text{doublets only}]\,(T_3^2)
= 3 \times 2 \times \tfrac{1}{4} + 1 \times 2 \times \tfrac{1}{4} = \tfrac{8}{4} = 2$$

where the first term counts 3 quark-colour copies of the SU(2)_L doublet $Q_L$
and the second counts the lepton doublet $L_L$, each contributing
$\mathrm{Tr}(\tau^3\tau^3) = \tfrac{1}{4}$ per component.

The generator ratio then gives:
$$\frac{g'^2}{g^2} = \frac{\mathrm{Tr}_{\text{doublets}}(T_3^2)}{\mathrm{Tr}_{\text{all reps}}(Y^2)}
= \frac{2}{10/3} = \frac{3}{5}$$

which is the **SU(5) GUT result**: $g'/g = \sqrt{3/5}$, $\sin^2\theta_W = 3/8$.

This computation assumes the SM fermion representation content; Task EW1.A is to
derive that same content from the ψ-winding mode decomposition of ℂ⊗ℍ.

**Task EW1.A**:
- [ ] Derive the fermion representation content of one generation from the ψ-winding
  mode decomposition of ℂ⊗ℍ.
- [ ] Compute $\mathrm{Tr}_\mathrm{all\,reps}(Y^2)$ and $\mathrm{Tr}_\mathrm{all\,reps}(T_3^2)$
  from UBT representation theory.
- [ ] If the ratio $\mathrm{Tr}(Y^2)/\mathrm{Tr}(T_3^2)$ is fixed by the ℂ⊗ℍ mode
  structure, then $g'^2/g^2 = \mathrm{Tr}(T_3^2)/\mathrm{Tr}(Y^2)$ follows from
  the canonical kinetic term normalisation.

**Source to extend**: `canonical/interactions/sm_gauge.tex §Generators`,
`gauge_normalization_attempt.tex §3`

**Status**: OPEN — EW1.A not attempted.

---

## Workstream EW2 — GUT Embedding Route

**Question**: Does ℂ⊗ℍ embed into a simple Lie group G_GUT such that the
GUT boundary condition fixes $\sin^2\theta_W$?

### SU(5) Prediction

In SU(5) grand unified theory, the SM subgroup SU(3)×SU(2)×U(1) embeds with
the hypercharge generator:
$$Y_{\mathrm{SU5}} = \mathrm{diag}\bigl(-\tfrac{1}{3},-\tfrac{1}{3},-\tfrac{1}{3},
\tfrac{1}{2},\tfrac{1}{2}\bigr)$$
Normalised to $\mathrm{Tr}_{5}(Y^2) = \tfrac{1}{2}$ (same as SU(5) generators),
this requires $Y_{\mathrm{phys}} = \sqrt{3/5}\,Y_{\mathrm{SU5}}$.

The GUT boundary condition is:
$$g^{-2}_{\mathrm{SU5}} = g^{-2}_{\mathrm{SU2}} = g'^{-2}_{\mathrm{SU2}}\cdot\tfrac{5}{3}$$

which gives at the GUT scale:
$$\sin^2\theta_W(\mathrm{GUT}) = \frac{3}{8}$$

Running the renormalization group to the electroweak scale $M_Z$:
$$\sin^2\theta_W(M_Z) \approx 0.231\quad(\text{one-loop SM running from } M_{\mathrm{GUT}} \approx 2\times10^{16}\,\mathrm{GeV})$$

This matches experiment to 1% and is a well-known result of the SU(5) GUT.

### EW2 UBT Tasks

**Task EW2.A — Test SU(5) embedding of ℂ⊗ℍ**:
- [ ] Determine whether the SM gauge algebra $\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak{u}(1)$
  embedded in ℂ⊗ℍ admits a natural extension to $\mathfrak{su}(5)$.
  - dim_ℝ(𝔰𝔲(5)) = 24; dim_ℝ(𝔰𝔲(3)⊕𝔰𝔲(2)⊕𝔲(1)) = 12; ℂ⊗ℍ contributes 8 real dims.
  - Key question: is the 12-dimensional SM gauge subalgebra of Mat(2,ℂ) a real
    sub-algebra of a 24-dimensional SU(5) Lie algebra?
- [ ] If yes: show that the embedding uniquely fixes the Y generator normalization
  to the SU(5) form, giving sin²θ_W(GUT) = 3/8.

**Task EW2.B — Test SO(10) embedding**:
- [ ] SO(10) contains SU(5) and has a 16-dimensional spinor representation that
  accommodates exactly one SM generation (including right-handed neutrino).
- [ ] dim_ℝ(𝔰𝔬(10)) = 45; the 16 spinor coincides with the UBT ψ-mode counting
  (N_eff = 12 ≈ 16 modes, though not exact — investigate).
- [ ] If the UBT field Θ is in a 16-dimensional representation of some extension of
  ℂ⊗ℍ, the SO(10) GUT boundary condition sin²θ_W(GUT) = 3/8 would apply.

**Task EW2.C — Internal UBT GUT**:
- [ ] The ℂ⊗ℍ algebra has an automorphism group that may contain an SU(5)-like
  structure via its complexification or double-covering.
- [ ] Investigate whether the 8-dimensional real structure of ℂ⊗ℍ admits a
  natural 5-dimensional complex representation that would carry GUT quantum numbers.
- [ ] Key relation: ℂ⊗ℍ ≅ Mat(2,ℂ) has complex irreducibles of dimension 2 (fundamental)
  and 1 (trivial). Complexifying: ℂ ⊗_ℝ (ℂ⊗ℍ) ≅ Mat(2,ℂ)⊕Mat(2,ℂ). Neither is 5-dim.
  The 5-dim representation must come from a different construction.

**Task EW2.D — RG flow from GUT to EW scale**:
- [ ] If sin²θ_W(GUT) = 3/8 is derived (EW2.A–C), apply one-loop SM RG flow:
  $$\sin^2\theta_W(M_Z) = \frac{3/8}{1 + (55/24\pi)\alpha(M_Z)\ln(M_{\mathrm{GUT}}/M_Z)}$$
- [ ] Determine M_GUT from the ψ-circle compactification radius (if derivable).
- [ ] Check agreement with sin²θ_W(M_Z) ≈ 0.231.

**Status**: EW2.A–D not yet attempted. EW2 is fresh and promising.

**Potential blocker**: If ℂ⊗ℍ does not embed into SU(5) or SO(10), the GUT
boundary condition cannot be used. An internal UBT GUT (EW2.C) would be needed.

---

## Workstream EW3 — Geometric Projection Route

**Question**: Is $\theta_W$ a projection angle in the fiber of the internal symmetry
bundle, derivable from the metric or connection eigenstructure of ℂ⊗ℍ?

### Mathematical Framework

The electroweak gauge group SU(2)_L × U(1)_Y acts on the fiber of the
$\Theta$-field bundle.  The photon direction in the Lie algebra
$\mathfrak{g}_{EW} = \mathfrak{su}(2)_L \oplus \mathfrak{u}(1)_Y$ is:
$$Q = T_3 + Y/2 = \tau^3 + \tfrac{1}{2}I$$
The Weinberg angle is the angle between the U(1)_EM direction Q and the
U(1)_Y direction Y in $\mathfrak{g}_{EW}$:
$$\cos\theta_W = \frac{\langle Q, Y\rangle_{\mathfrak{g}_{EW}}}{\|Q\|_{\mathfrak{g}_{EW}}\|Y\|_{\mathfrak{g}_{EW}}}$$
where $\langle\cdot,\cdot\rangle_{\mathfrak{g}_{EW}}$ is the Killing form on $\mathfrak{g}_{EW}$.

### EW3 UBT Tasks

**Task EW3.A — Define inner product on $\mathfrak{g}_{EW}$ from UBT**:
- [ ] The kinetic term $\mathrm{Tr}[(D_\mu\Theta)^\dagger D^\mu\Theta]$ induces
  an inner product on $\mathfrak{g}_{EW}$ via $\langle A,B\rangle = \mathrm{Tr}[A,\Theta][B,\Theta]^\dagger$.
- [ ] Compute this inner product for the generators $\tau^i$ and $Y$.
- [ ] Show whether the induced inner product on $\mathfrak{g}_{EW}$ is proportional
  to the Killing form or differs.

**Task EW3.B — Compute the projection angle**:
- [ ] Using the inner product from EW3.A, compute:
  $$\cos\theta_W = \frac{\langle Q, Y\rangle}{\|Q\|\|Y\|}$$
- [ ] If this gives a specific numerical value (not 1/√2), that value is the
  UBT prediction for $\theta_W$.

**Task EW3.C — Geometric interpretation in the fiber bundle**:
- [ ] Interpret $\theta_W$ as the projection angle of the mass-eigenstate basis
  onto the gauge-eigenstate basis in the internal fiber of the $\Theta$-bundle.
- [ ] Relate to the eigenstructure of the $\Theta$ vacuum ($\Theta_0$).

**Status**: EW3.A is the most tractable entry point; computation is explicit.

**Potential obstruction**: The induced inner product from $\mathrm{Tr}[(D_\mu\Theta)^\dagger D^\mu\Theta]$
is representation-dependent.  For the fundamental (doublet) representation, the
equal-norm result $g = g'$ was found in EW1 above, corresponding to $\theta_W = \pi/4$.
The difference with experiment must come from either representation mixing (EW1 refined)
or GUT normalisation (EW2).

---

## Priority and Recommended Order

| Workstream | Entry point | Tractability | Impact if successful |
|-----------|-------------|--------------|---------------------|
| EW2 (GUT) | EW2.A: SU(5) test | HIGH | sin²θ_W = 3/8 GUT boundary condition |
| EW1 (algebra) | EW1.A: fermion rep content | MEDIUM | sin²θ_W from generator ratio |
| EW3 (geometric) | EW3.A: induced inner product | MEDIUM | sin²θ_W as projection angle |

**Recommended first attack**: EW2.A (SU(5) embedding test) because:
- The SU(5) result sin²θ_W = 3/8 is a clean algebraic fact if the embedding exists.
- Running to M_Z gives the observed value with no additional free parameters.
- The computation is explicit and does not require specifying fermion hypercharge assignments.

---

## What a Successful EW Derivation Gives

If any workstream produces $\sin^2\theta_W$ without fitting:

$$\boxed{\alpha = \frac{g^2 \sin^2\theta_W}{4\pi}}$$

With $g^2/(4\pi) = \alpha_2(M_Z) \approx 1/30$ from the EW sector (or from canonical
kinetic normalisation), the electromagnetic coupling follows immediately.

**This bypasses the B_base gap entirely** — no need to prove k=1.

---

## Open Gaps Registered by This Document

| Gap ID | Description | Priority |
|--------|-------------|----------|
| EW-1 | Derive $\tan\theta_W = g'/g$ from UBT algebra | **CRITICAL** |
| EW-2 | Derive $\Theta_0$ VEV as SU(2)_L doublet from S[Θ] | HIGH |
| GUT-UBT | Test SU(5)/SO(10) embedding of ℂ⊗ℍ | HIGH |
| EW-g | Derive g (SU(2)_L coupling) from canonical normalisation | MEDIUM |
| RG-UBT | Determine M_GUT from ψ-circle radius R_ψ | MEDIUM |

---

## Cross-References

- `reports/ew_mixing_status.md` — status report for all three workstreams
- `canonical/alpha/gauge_normalization_attempt.tex` — Route A1 (EW1 foundation)
- `canonical/alpha/symmetry_breaking_alpha_attempt.tex` — Route A2 (EW2 precursor)
- `canonical/interactions/sm_gauge.tex` — canonical SM gauge structure
- `research_tracks/T3_ALPHA/alpha_progress_log.md` — full T3 history and EW pivot rationale
- `DERIVATION_INDEX.md §EW` — derivation inventory entry point
