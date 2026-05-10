<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

<!-- [SPECULATIVE — SCOPING ONLY] per AGENTS.md §3 -->
<!-- This document does NOT contain new physics claims. -->
<!-- It maps the problem of quantising UBT and classifies the difficulty -->
<!-- of each component. No result in this document should be cited as -->
<!-- established UBT physics. -->

# GAP-Q Scope: Quantisation of Unified Biquaternion Theory

**Author**: Ing. David Jaroš  
**Date**: 2026-05-10  
**Classification**: `[SPECULATIVE — SCOPING ONLY]`  
**Priority**: Medium-Long (multi-year; foundational for any ToE claim)  
**Reference**: `ROADMAP.md §Phase 4`

---

## 1. Preamble

UBT is currently a **classical field theory**.  The fundamental field
`Θ(q,τ) ∈ ℂ⊗ℍ` is treated as a classical configuration; the field equations
`∇†∇Θ = κ𝒯` are classical Euler-Lagrange equations.

A theory of everything (ToE) requires a **quantum** version:
- A path integral formulation over Θ
- Feynman rules for scattering amplitudes
- Renormalisability (or finiteness) of quantum corrections
- Recovery of the Standard Model Feynman rules in an appropriate limit

This document maps the problem.  **It does not solve it.**

---

## 2. What "Quantisation of UBT" Would Require

### 2.1 Path integral over Θ(q,τ)

**What is needed**:

Define the path integral:
```
Z = ∫ 𝒟Θ  exp(iS[Θ]/ℏ)
```
where `S[Θ]` is the canonical UBT action
(see `canonical/THEORY/canonical/canonical_action.tex`).

**Components requiring specification**:

1. **The integration measure `𝒟Θ`**: Θ takes values in `ℂ⊗ℍ ≅ Mat(2,ℂ)`,
   so the path integral is over the space of maps
   `Θ: M⁴ × S¹_ψ → Mat(2,ℂ)`.
   The natural measure is a Gaussian measure on `L²(M⁴ × S¹_ψ, Mat(2,ℂ))`,
   but defining this rigorously requires:
   - A choice of functional measure compatible with the `ℂ⊗ℍ` symmetry
   - Gauge-fixing for the `SU(3) × SU(2)_L × U(1)_Y` local symmetry
   - Ghost fields (Faddeev-Popov procedure)

2. **Convergence**: The Euclidean path integral (Wick-rotated to `τ → iτ_E`)
   is better-defined if `S_E[Θ] > 0` for all non-trivial configurations.
   The canonical UBT action in Euclidean signature should be checked for positivity.

3. **Renormalisation scale**: The path integral must be defined with a UV cutoff
   Λ; the physical predictions must be independent of Λ (renormalisability or
   finiteness).

**Classification**: *(ii) Hard open problem*  
The `ℂ⊗ℍ`-valued nature of Θ is non-standard; no standard reference applies
directly.  The gauge structure is the same as the Standard Model (which is
fully quantised), but the biquaternionic source of the gauge group adds
technical complications.

---

### 2.2 Propagator and vertex rules from the canonical action

**What is needed**:

Extract the propagator `⟨Θ(x)Θ†(y)⟩₀` and vertex factors from `S[Θ]`
by expanding around a saddle point `Θ = Θ_c + δΘ` where `Θ_c` is a
classical solution.

**Components**:

1. **Free propagator**: The kinetic term `Tr[(D_μΘ)†(D^μΘ)]` gives a
   Klein-Gordon-like kinetic operator `K = −∇†∇ + m²_c` (where `m_c` is
   the effective mass from the background).  The free propagator is `K^{-1}`,
   which in momentum space is the standard scalar propagator
   `i/(p² − m²_c + iε)` with `Mat(2,ℂ)` matrix structure.

2. **Interaction vertices**: Expanding `S[Θ]` beyond quadratic order in
   `δΘ` generates 3-point, 4-point, and higher-point vertices.  For the
   gauge sector, these are the standard SM gauge vertices (already
   well-known); the UBT contribution adds vertices from the non-minimal
   coupling of Θ to the geometry.

3. **Gravity vertices**: The UBT metric `g_μν = Re[Tr(∂_μΘ·∂_νΘ†)]/𝒩`
   introduces graviton-Θ couplings that are not present in standard QFT.
   These vertices are non-polynomial in Θ and would complicate the
   perturbative expansion.

**Classification**:

- Standard SM gauge vertices: *(i) Straightforward* given existing canonical material
- UBT-specific (gravity-Θ) vertices: *(ii) Hard open problem*

---

### 2.3 Power-counting and renormalisability

**What is needed**:

Determine whether UBT is:
(a) **Renormalisable**: All UV divergences can be absorbed by a finite number
    of counterterms.
(b) **Non-renormalisable** (but UV-complete via asymptotic safety or
    non-perturbative effects).
(c) **Finite**: No UV divergences at any loop order (analogous to N=4 SYM).

**Power-counting argument**:

The UBT action in 4D spacetime has the schematic form:
```
S[Θ] ∼ ∫ d⁴x d¹ψ  [Tr(∂Θ)² + gauge terms + gravity terms]
```
The integral over the fifth dimension `S¹_ψ` (after KK reduction) produces
an effective 4D theory with an infinite tower of KK modes.

- If the KK tower is truncated at a finite cutoff `Λ_KK = 1/R_ψ`: the
  low-energy effective theory is a standard 4D QFT, which inherits the
  renormalisability of the SM gauge sector.
- If the KK tower is kept: the full 5D theory must be analysed.
  Five-dimensional Yang-Mills theory is **non-renormalisable** by power
  counting (`[g²] = −1` in mass units).

**Possible paths to UV completeness**:
- Asymptotic safety (à la Reuter-Saueressig for gravity)
- String theory embedding of the `ℂ⊗ℍ` structure
- Finite quantum correction cancellation (requires extended SUSY or
  similar mechanism, not currently present in UBT)

**Classification**: *(ii) Hard open problem* (possibly *(iii) possible dead end*
for strict renormalisability in the 5D sense)

---

### 2.4 Recovery of Standard Model Feynman rules

**What is needed**:

Show that in the limit `R_ψ → 0` (or `Λ_KK → ∞` kept fixed),
the UBT quantum field theory reduces to the Standard Model:
- Same gauge structure `SU(3) × SU(2)_L × U(1)_Y`
- Same Feynman rules for gauge bosons and fermions
- Same low-energy cross sections for well-tested processes (e+e- → μ+μ-,
  Compton scattering, etc.)

**Assessment**:

The classical limit is established: the UBT field equations reproduce the
SM gauge equations in the real-sector limit (proved at [L1] for the
graviton sector; for the gauge sector at [L0]).

The quantum limit requires:
1. The one-loop effective action of UBT must reduce to the SM one-loop
   effective action for energies `E ≪ Λ_KK`.
2. The KK modes must decouple at low energy (consistent with
   Appelquist-Carazzone decoupling theorem if KK masses are large).
3. No anomaly introduced by the UBT structure that is absent from the SM.

**Classification**: *(i) Straightforward at the classical level*;
*(ii) Hard open problem at the quantum level*

---

## 3. Classification Summary

| Requirement | Classification | Notes |
|-------------|----------------|-------|
| Path integral measure `𝒟Θ` | (ii) Hard open problem | Non-standard `ℂ⊗ℍ`-valued field |
| Gauge fixing (FP procedure) | (i) Straightforward | Standard SM gauge fixing applies |
| Free propagator | (i) Straightforward | Standard Klein-Gordon structure |
| SM gauge vertices | (i) Straightforward | Same as known SM vertices |
| Gravity-Θ vertices | (ii) Hard open problem | Non-polynomial coupling |
| Power-counting (4D effective) | (i) Straightforward | Inherited from SM renormalisability |
| Power-counting (full 5D) | (ii)/(iii) Hard/Dead end | 5D YM is non-renormalisable |
| Asymptotic safety route | (ii) Hard open problem | Requires non-perturbative analysis |
| SM Feynman rules in KK limit | (i) at classical level | Proved [L1] |
| SM Feynman rules at 1-loop | (ii) Hard open problem | Not yet attempted |
| Anomaly cancellation | (i) Likely straightforward | SM anomalies cancel; check UBT adds none |

---

## 4. Parallel Lessons from Other Approaches

### 4.1 String theory

String theory provides a UV-complete quantum theory of gravity and gauge
fields via the compactification of extra dimensions.  The `ℂ⊗ℍ` structure
of UBT has a natural string-theory analogue: the field `Θ(q,τ)` with
`τ ∈ ℂ` (complex time) is formally similar to a string worldsheet action
with complex modular parameter.

**Lesson**: String theory achieves UV completeness via an infinite tower of
modes at the string scale `M_s`.  A UBT quantisation might similarly require
treating the `S¹_ψ` compactification at the level of the full string theory,
not just as a KK reduction.

**Applicable to UBT**: Potentially, if the UBT structure can be embedded in
a string compactification.  This is speculative.

### 4.2 Loop Quantum Gravity (LQG)

LQG quantises GR directly by promoting the connection `A` and the
frame field `E` to operators.  The UBT analogue would be to promote
`Θ` and `∂_μΘ` to operators acting on a Hilbert space.

**Lesson**: LQG achieves background-independence but has difficulty
recovering the SM gauge sector.  UBT has the SM gauge sector built in
algebraically; the challenge is background-independence in the gravity sector.

**Applicable to UBT**: The `ℂ⊗ℍ`-valued field `Θ` provides a natural
connection-like object (the UBT covariant derivative `D_μΘ`).  Spin foam
methods might apply to the imaginary-time sector.

### 4.3 Asymptotic safety

Asymptotic safety (Reuter-Saueressig) posits that gravity has a
non-Gaussian UV fixed point making it non-perturbatively renormalisable.

**Lesson**: The fixed point is not achieved in naive perturbation theory
but may be found by exact RG methods (functional RG, truncated flow
equations).

**Applicable to UBT**: If the full 5D UBT has a UV fixed point under the
functional RG, it would be non-perturbatively UV-complete.  The presence of
`N_eff = 12` propagating modes (fixed by algebra [L0]) provides a specific
input to the graviton running.

---

## 5. Conclusion: What Is Tractable Now

Given the current state of UBT, the following quantum calculations are
tractable without solving GAP-Q completely:

1. **One-loop effective potential** for the winding modes (this is already
   computed as `V_eff(n) = n² - Bn·ln n` at [L1]).  This is the quantum
   computation that generates the α result.

2. **One-loop beta function for U(1)_Y** from UBT: compare with SM value
   `β₀ = 41/6` for confirmation.

3. **Anomaly cancellation check**: Verify that the fermion content of UBT
   (three generations, SM representations) satisfies the SM anomaly
   cancellation conditions.  This is straightforward since the fermion
   content is identical to the SM.

4. **Heat kernel expansion**: The one-loop effective action can be computed
   via the Seeley-DeWitt expansion, giving low-energy corrections to the
   UBT metric and gauge action.  This is the `B_base` computation in the
   `T3_ALPHA` track.

**These four items are at [L1] accessibility level and should be prioritised
over the full quantum-UBT programme.**

---

## 6. Deliverables from This Scoping Document

- [ ] No canonical promotions from this document (per problem statement)
- [x] GAP-Q scoped: see §2 for requirements, §3 for classification
- [x] Parallel lessons documented: §4
- [x] Tractable near-term quantum calculations identified: §5
- [ ] Full quantum-UBT programme: deferred to long-term (ROADMAP.md Phase 4)

---

*This document is `[SPECULATIVE — SCOPING ONLY]` per AGENTS.md §3.
No result herein constitutes a claim of UBT physics at any proof level.*
