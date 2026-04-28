<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# Fine-Structure Constant α — Derivation Routes Survey

**Author**: Ing. David Jaroš  
**Date**: 2026-04-27  
**Status**: Research — four active routes catalogued  
**Canonical source**: `docs/STATUS_ALPHA.md`  
**Companion files**: `gauge_normalization_attempt.tex`, `symmetry_breaking_alpha_attempt.tex`,
`../../research_tracks/alpha/layer2_coding_alpha_scan.py`,
`../../reports/alpha_no_fit_audit.md`

---

## Purpose

This document surveys four independent routes to deriving the fine-structure constant
α ≈ 1/137.036 from UBT without numerical fitting.  Each route is described, its
assumptions are listed explicitly, its current status is classified, and its failure
modes are recorded.

**Acceptance criteria** (from the task specification):

| Criterion | Requirement |
|-----------|-------------|
| No fitted parameter | Every numerical input must come from another UBT sector |
| Reproducibility | Every numerical claim must be reproducible from a script |
| Status classification | `proven` / `conditional` / `numerical coincidence` / `failed` |

---

## Route A1: Gauge Normalization

**File**: `gauge_normalization_attempt.tex`  
**Question**: Does the canonical normalization of the UBT U(1) gauge connection fix e,
and hence α, without additional input?

### Strategy

The electromagnetic coupling e appears in the covariant derivative
`D_μ = ∂_μ + ie A_μ` acting on Θ.  In the Standard Model,
`e = g sin(θ_W)` where g is the SU(2)_L coupling and θ_W is the Weinberg angle.
UBT must either:
(a) derive both g and θ_W from the biquaternion structure, or  
(b) derive the combination e directly from A-field normalization.

### Current Status

| Step | Status |
|------|--------|
| Identify UBT U(1) connection | ✅ DONE — B_μ component of canonical D_μ |
| Canonical kinetic-term normalization of A_μ | ✅ DONE — follows from Tr[(D_μΘ)†(D^μΘ)] |
| Derive e from A-field normalization | ⚠️ CONDITIONAL — requires SU(2)_L × U(1)_Y → U(1)_EM projection |
| Derive θ_W from UBT symmetry breaking | ❌ OPEN — see Route A2 |
| Derive α = e²/(4π) without fitting | ❌ OPEN — blocked by θ_W gap |

### Assumptions Explicitly Listed

1. The UBT kinetic Lagrangian `Tr[(D_μΘ)†(D^μΘ)]` is canonically normalized (factor 1 in front).
2. The gauge group embeds as SU(3)_c × SU(2)_L × U(1)_Y → U(1)_EM by the Higgs-like mechanism.
3. The UBT Θ-field VEV plays the role of the SM Higgs doublet VEV.
4. Natural units ħ = c = 1.

### Failure Modes

- If `Tr[(D_μΘ)†(D^μΘ)]` has a non-trivial normalization factor from the UBT trace definition,
  the canonical A-field normalization acquires a free parameter.
- If the SU(2)_L × U(1)_Y embedding into the biquaternion algebra is not unique,
  the coupling ratio g'/g is not fixed.

### Classification: **conditional**

---

## Route A2: Symmetry-Breaking Projection

**File**: `symmetry_breaking_alpha_attempt.tex`  
**Question**: Does the UBT symmetry-breaking mechanism SU(2)_L × U(1)_Y → U(1)_EM
fix the Weinberg angle θ_W, and hence e and α?

### Strategy

After spontaneous symmetry breaking (SSB) of SU(2)_L × U(1)_Y → U(1)_EM:

- The unbroken U(1)_EM generator is Q = T₃ + Y/2.  
- The physical photon field is A_μ = sin(θ_W) W³_μ + cos(θ_W) B_μ.  
- The Weinberg angle satisfies tan(θ_W) = g'/g.

For UBT to fix θ_W without fitting, the ratio g'/g must be determined by
the algebra of the biquaternion field and the breaking structure.

### Current Status

| Step | Status |
|------|--------|
| Embed SU(2)_L × U(1)_Y in biquaternion algebra | ✅ DONE — `canonical/interactions/sm_gauge.tex` |
| Derive unbroken generator Q = T₃ + Y/2 | ✅ DONE — standard electroweak algebra |
| Derive VEV structure that breaks SU(2)_L × U(1)_Y | ⚠️ CANDIDATE — Θ₀ as doublet VEV |
| Fix tan(θ_W) = g'/g from UBT algebra | ❌ OPEN — Gap EW-1 |
| Derive α from fixed θ_W and e = g sin(θ_W) | ❌ BLOCKED by Gap EW-1 |

**Gap EW-1** (new, registered here): Derive the ratio g'/g of the SU(2)_L and U(1)_Y
coupling constants from the biquaternion algebra representation theory.  This is the
key missing step for fixing θ_W from first principles.

### Assumptions Explicitly Listed

1. The SSB pattern is SU(2)_L × U(1)_Y → U(1)_EM (i.e., exactly SM electroweak breaking).
2. The Θ₀ VEV transforms as a doublet under SU(2)_L with hypercharge Y = 1/2.
3. The coupling constants g, g' are independent at the UBT Lagrangian level;
   they become equal only if the algebra provides a relation.
4. The Standard Model relation `sin²(θ_W) ≈ 0.231` is not used as an input.

### Failure Modes

- The biquaternion algebra may not enforce any specific ratio g'/g;
  the two couplings remain independent free parameters.
- The Θ-field VEV may not transform as a doublet; the SSB pattern may differ from SM.
- Even if θ_W is fixed, further UV physics (renormalization group running) shifts α(μ)
  at any given scale, requiring an additional scale input.

### Classification: **conditional** (gap EW-1 blocks completion)

---

## Route A3: Theta/Modular Route

**Question**: Does the modular structure of the complex-time parameter τ = t + iψ,
when treated as a modular parameter τ ∈ ℍ, produce modular invariants or Hecke
eigenvalues at the scale of α?

### Strategy

The complex time τ transforms under SL(2,ℤ): τ → (aτ + b)/(cτ + d).
Modular forms f(τ) of weight k satisfy f((aτ+b)/(cτ+d)) = (cτ+d)^k f(τ).
Modular-invariant combinations (k = 0) are functions of the j-invariant j(τ).

For α, one asks: is there a modular invariant that equals α or 1/α = 137.036 exactly,
constructed only from UBT data (τ, the spectrum of ∇†∇, Hecke eigenvalues)?

### Search Results

| Expression | Numerical value | α⁻¹ = 137.036? | Assessment |
|------------|-----------------|-----------------|------------|
| e^π (Gelfond) | 23.140... | No | Unrelated |
| 16π³ | 4961.2... | No | Unrelated |
| Γ(1/4)⁴/(4π³) | 1.181... | No | Unrelated |
| j(i)/1000 | 1.728 | No | Unrelated |
| KK ground mode n=137 (prime) | 137 (integer) | ✅ (bare) | V_eff attractor (existing) |
| Hecke T₁₃₇ eigenvalue of Δ | τ(137) = −182213... | No | Large integer |
| Modular discriminant η(τ)²⁴ at τ = i·137 | Exponentially small | No | No match |

### Conclusion

No modular invariant or Hecke eigenvalue naturally produces α⁻¹ = 137.036 from
the complex-time structure alone.  The prime-attractor result (n* = 137 from
the V_eff minimum) already uses the modular ψ-circle, but this gives the bare
integer 137, not the full 137.036.

The modular route does not produce α without additionally specifying the one-loop
correction Δ from outside the modular structure.

### Classification: **numerical coincidence** (for integer 137 as a modular/prime feature)
or **failed** (for producing 137.036 from modular invariants)

---

## Route A4: Layer 2 Coding Constraint

**File**: `../../research_tracks/alpha/layer2_coding_alpha_scan.py`  
**Question**: Do the Hamming (8,4,4), Gray transport, or the 1⊕3⊕3̄⊕1 decomposition
constraints fix the U(1) phase quantization in a way that determines α?

### Strategy

The Layer 2 coding structure of UBT (see `research_tracks/gray_transport_layer/`)
distinguishes two sub-layers:

- **L2S** (State, Hamming): states must satisfy parity checks of the (8,4,4) code.
- **L2T** (Transport, Gray): phase transitions prefer Gray-adjacent steps.

The 1⊕3⊕3̄⊕1 decomposition under SU(2) of the biquaternion algebra occupies 8
real dimensions, matching the Hamming block length.

For α, the question is whether these coding constraints:
(a) fix the charge quantum (integer multiples of e), and  
(b) fix the *magnitude* of e (which would determine α).

### Current Status

| Step | Status |
|------|--------|
| Hamming (8,4,4) enforces charge quantization (integers) | ⚠️ PLAUSIBLE — minimum distance 4 = 2×(isospin multiplicity) |
| Gray code constrains U(1) phase steps | ⚠️ HYPOTHESIS — sequential ψ-steps prefer single-bit changes |
| 1⊕3⊕3̄⊕1 fixes normalization of U(1) embedding | ❌ OPEN — decomposition fixes *structure*, not coupling magnitude |
| Coding constraints fix the magnitude of e | ❌ FAILED — coding fixes quantization rules, not coupling strength |

**Key finding** (from scan script): The coding layer fixes *which charges are allowed*
(specifically: integer or half-integer multiples of a unit charge, depending on the
representation), but it does NOT fix the magnitude of that unit charge.  The magnitude
of e = √(4πα) requires additional dynamical input from the S[Θ] action.

### Assumptions Explicitly Listed

1. The biquaternion algebra 1⊕3⊕3̄⊕1 is an 8-dimensional real representation of SU(2).
2. The Hamming (8,4,4) code operates on the 8 real dimensions of this decomposition.
3. Gray adjacency applies to sequential phase-symbol transitions in the ψ-direction.
4. The coding layer selects admissible field configurations but does not determine coupling strengths.

### Failure Modes

- The 8-dimensional coincidence (Hamming block length = real dim of 1⊕3⊕3̄⊕1) may be
  an accidental structural match rather than a physical constraint.
- Even if coding fixes the charge spectrum to integers, α = e²/(4π) requires knowing e
  in physical units, which depends on the UV cutoff and renormalization scheme.

### Classification: **failed** (coding does not fix coupling magnitude; quantization only)

---

## Summary Table

| Route | ID | Status | Gap | Next step |
|-------|----|--------|-----|-----------|
| Gauge normalization | A1 | conditional | θ_W not derived | Solve Gap EW-1 |
| Symmetry breaking projection | A2 | conditional | g'/g ratio free | Derive from algebra |
| Theta/modular route | A3 | failed/coincidence | No modular invariant = 137.036 | Abandon |
| Layer 2 coding constraint | A4 | failed | Coding ≠ coupling magnitude | Clarify scope |

**Definitive bottleneck**: All routes capable of deriving α converge on the need to
fix the ratio g'/g = tan(θ_W) from the UBT biquaternion algebra.  This is Gap EW-1.

**What is already proved** (not changed by this survey):
- The bare value α⁻¹ = 137 from the prime attractor (V_eff minimum, existing L1 result).
- The one-loop QED correction to α (two-loop reproduction, existing L1 result).
- The charge quantization (Dirac condition from ψ-circle winding, existing L0 result).

---

## Open Problems Registered by This Survey

| Gap ID | Description | Priority |
|--------|-------------|----------|
| EW-1 | Derive tan(θ_W) = g'/g from biquaternion algebra | **CRITICAL** |
| EW-2 | Derive Θ₀ VEV as SU(2)_L doublet from S[Θ] | HIGH |
| L2-α | Clarify whether L2S/L2T constrain coupling *magnitude* or only *spectrum* | MEDIUM |

---

## References (Internal)

- `docs/STATUS_ALPHA.md` — master α derivation status
- `canonical/THEORY/topic_indexes/alpha_index.md` — topic index
- `canonical/appendices/appendix_alpha_geometry.tex` — toroidal/prime-attractor approach
- `canonical/interactions/sm_gauge.tex` — Standard Model gauge structure
- `canonical/symmetry/step3_breaking_catalogue.tex` — symmetry breaking catalogue
- `research_tracks/gray_transport_layer/gray_vs_hamming_layer2.md` — L2 coding structure
- `DERIVATION_INDEX.md` — full derivation inventory
