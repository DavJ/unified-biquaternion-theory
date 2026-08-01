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

# UBT Layered Architecture: Layer 1 vs Layer 2 Contract

## Purpose

This document defines the distinction between **Layer 1** (physics-derived) and **Layer 2** (protocol/engineering choices) in UBT to prevent mixing derived constants with arbitrary selections.

## The Problem

Without clear layer separation, there's a risk of claiming that **protocol choices** (e.g., picking channel 137 in a coding scheme) are **fundamental physics constants** (e.g., the fine structure constant is exactly 1/137 because of deep geometric principles).

This document establishes rules to prevent such confusion.

## Layer Definitions

### Layer 1: Geometry/Topology/Dynamics
**What it is**: Continuous symmetries, structural invariants, and dynamical laws

**Examples**:
- Biquaternionic field structure ℂ⊗ℍ
- Complex time manifold τ = t + iψ
- Field equation ∇†∇Θ = κ𝒯
- General Relativity recovery (ψ → 0 limit)
- Standard Model gauge group SU(3)×SU(2)×U(1) emergence from Aut(ℂ⊗ℍ)
- GR equivalence in real limit: R_μν - ½g_μν R = 8πG T_μν

**Characteristics**:
- ✅ Derived from axioms/symmetries
- ✅ Continuous parameters
- ✅ Independent of implementation details
- ✅ Testable via multiple observables
- ✅ Framework-level predictions

**Status markers**: "Derived", "Proven", "Follows from axioms"

### Layer 2: Coding/Modulation/Protocol
**What it is**: Discrete choices, channel selections, implementation parameters

**Examples**:
- Winding number selection n=137 vs n=139 vs n=191
- OFDM channel indexing
- Prime gating patterns (which primes to use)
- RS(255,201) error correction code parameters
- GF(2⁸) finite field choice (256 states)
- Master Clock tick count (256-tick framing)
- Quantization grid discretization

**Characteristics**:
- ⚠️ Chosen to match observations or for engineering reasons
- ⚠️ Discrete/integer parameters
- ⚠️ Implementation-dependent
- ⚠️ Multiple valid choices possible
- ⚠️ Calibration parameters

**Status markers**: "Selected", "Chosen to match", "Calibrated", "Channel index", "Hypothesis"

## The Contract: Layer Separation Rules

### Rule 1: Layer 2 Choices Cannot Be Claimed as Layer 1 Derivations

**Forbidden**:
- "α⁻¹ = 137 is derived from first principles" (if n=137 is a Layer 2 channel choice)
- "The universe must have 137 dimensions" (if 137 is just an index)
- "Fundamental proof that α⁻¹ is exactly 137.000" (if it's a selection, not derivation)

**Allowed**:
- "α⁻¹ ≈ 137 is used as geometric reference point" ✓
- "Channel n=137 selected to match experimental α" ✓
- "Hypothesis: n=137 emerges from [specify selection principle]" ✓ (if principle stated and testable)

### Rule 2: Selection Principles Must Be Explicit and Testable

If claiming a Layer 2 choice is actually Layer 1 (i.e., derived), you MUST provide:

1. **Explicit selection functional**: S(n) that picks n=137 uniquely
2. **Falsifiability**: Scan showing n=137 is a maximum/minimum/fixed point
3. **Independence**: Selection doesn't use the outcome being explained (no circularity)

**Example of proper escalation**:
- "n=137 is chosen to match α" (Layer 2, honest) →
- "n=137 maximizes stability functional S(n)" (claim of Layer 1) →
- **Requirement**: Run stability scan, show n=137 is unique maximum
- **Result**: Scan shows n=137 ranks 53/99, NOT a maximum →
- **Conclusion**: Remains Layer 2

### Rule 3: Layer 1 → Layer 2 is Allowed, Layer 2 → Layer 1 Requires Proof

**Allowed** (no proof needed):
- Use Layer 1 dynamics to constrain Layer 2 choices
- "Only primes allowed due to gauge quantization" (topology constrains channels)
- "n must satisfy winding condition" (geometry restricts choices)

**Requires proof** (explicit demonstration):
- Claim that Layer 2 choice is actually Layer 1 consequence
- "n=137 is the unique stable configuration"
- **Must provide**: Stability scan or other falsifiable selection principle

### Rule 4: Transparency Required in All Documentation

**README.md must include**:
- Explicit table with "Derivation Status" column
- Clear separation: "Layer 1 (geometry)" vs "Layer 2 (coding/channel)"
- No mixing of derived and selected parameters without labeling

**FITTED_PARAMETERS.md remains authoritative** for parameter status

## Application to Alpha

### Current Status (Post Stability Scan)

**Layer 1 (Geometry)**:
- Biquaternionic structure permits winding number quantization
- Compact U(1) requires integer n
- Prime constraint from gauge structure (n must be prime)
- α⁻¹ ≈ n + corrections (geometric framework)

**Layer 2 (Channel Selection)**:
- Choice of n=137 specifically (not uniquely derived)
- Stability scan shows n=137 is NOT a maximum
- Better candidates: n=199, 197, 193, 191, ... (all score higher)
- Even neighbor n=139 is more stable

**Honest Statement**:
> "UBT uses n=137 as a geometric reference point, selected to match the experimental fine structure constant α⁻¹ ≈ 137.036. Stability analysis indicates this is a Layer 2 channel selection rather than a Layer 1 derivation. The geometric framework predicting α⁻¹ ≈ n + corrections remains valid, but the specific choice n=137 is not uniquely determined by stability principles."

**Dishonest Statement** (to avoid):
> ❌ "UBT derives α⁻¹ = 137 from pure geometry with no free parameters"
> ❌ "First-principles proof that α⁻¹ must equal 137.000"
> ❌ "Only theory predicting α exactly from topology"

## Layer Status Table (Examples)

| Observable | Value | Layer | Derivation Status | Evidence |
|------------|-------|-------|-------------------|----------|
| Biquaternion structure | ℂ⊗ℍ | L1 | Axiom | Definition |
| GR recovery | R_μν - ½g_μν R = 8πG T_μν | L1 | Derived | Proven in Appendix R |
| SM gauge group | SU(3)×SU(2)×U(1) | L1 | Derived | Aut(ℂ⊗ℍ) calculation |
| Prime constraint | n ∈ primes | L1→L2 | Constrained | Gauge quantization |
| Winding number | n=137 | L2 | Selected | Matches α, NOT stability max |
| α baseline | 137.000 | L2 | Selected | Same as n selection |
| α corrections | +0.036 | L1 | Partly derived | ~90% structural, ~12% gap |
| Electron mass baseline | 0.509856 MeV | L1 | Derived | Hopfion topology |
| Electron mass corrections | +0.001 MeV | L2 | Fitted | Parameters A,p,B |
| RS(255,201) code | 255,201 | L2 | Chosen | Optimal for 256-state system |
| GF(2⁸) field | 256 states | L2 | Chosen | Engineering choice |

## Enforcement

This contract is enforced through:

1. **Documentation reviews** - All claims must respect layer separation
2. **Stability scans** - Required before claiming Layer 2 → Layer 1
3. **Parameter transparency** - FITTED_PARAMETERS.md lists all Layer 2 choices
4. **Test non-circularity** - Tests must not assume conclusions

## Revision Process

If a parameter moves between layers:

**Layer 2 → Layer 1** (selection becomes derivation):
1. Provide explicit selection principle
2. Run falsifiable test (e.g., stability scan)
3. Show target is unique maximum/minimum
4. Update docs with "Upgraded: Now derived via [principle]"

**Layer 1 → Layer 2** (derivation fails):
1. Acknowledge failure honestly
2. Update docs: "Previously claimed derived, now recognized as selection"
3. Maintain parameter value if empirically successful
4. Document as calibration/channel choice

## Conclusion

**Layer separation prevents**:
- Claiming engineering choices as fundamental laws
- Circular reasoning (selecting to match, then claiming derived)
- Overstating theoretical achievements

**Layer separation enables**:
- Scientific honesty about what's derived vs chosen
- Clear falsifiability (Layer 1 can be tested, Layer 2 can be calibrated)
- Productive research (knowing what needs derivation vs what needs measurement)

**One-sentence rule**:
> If it's chosen to match data, it's Layer 2 until proven otherwise via a falsifiable selection principle.

---

**Established**: 2026-02-12  
**Authority**: Repository governance  
**Enforcement**: Code review + stability scans  
**Updates**: This document lives at `docs/architecture/LAYERS.md`
