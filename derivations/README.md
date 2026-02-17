# UBT Core Derivations: Clean-Room Reconstruction

This directory contains **clean-room derivations** of UBT core physics, written from first principles **without chronofactor assumptions**.

## Purpose

These derivations systematically rebuild the theoretical structure of UBT starting from:
- The 8D biquaternionic field Θ(q) as the sole primitive
- Entropy channel S_Θ and phase channel Σ_Θ as observables
- NO external/global chronofactor parameter

Each derivation is self-contained and builds on previous ones.

## Derivation Roadmap

### D01: Theta and 8D Structure
**File**: `D01_theta_and_8D.md`

**Intent**: Establish the fundamental field Θ(q) as a biquaternion with 8 real degrees of freedom. Define basic operations: conjugation, multiplication, norm, determinant. Clarify why we need exactly 8D (not 4D quaternions, not 16D bi-biquaternions).

**Status**: 🚧 Stub created

---

### D02: Polar Decomposition
**File**: `D02_polar_decomposition.md`

**Intent**: Develop the split of Θ into amplitude and phase sectors. Explore different decomposition schemes (exponential map, logarithmic coordinates, etc.). Establish which decomposition is most natural for physical observables.

**Status**: 🚧 Stub created

---

### D03: Entropy and Phase Observables
**File**: `D03_entropy_and_phase.md`

**Intent**: Rigorously define S_Θ = 2 k_B ln |det Θ| and Σ_Θ = k_B arg det Θ. Prove key properties: positivity of entropy, 2π periodicity of phase, relationship to field norm. Connect to thermodynamic and topological interpretations.

**Status**: 🚧 Stub created

---

### D04: Emergent Metric (Real Channel)
**File**: `D04_emergent_metric_Re_channel.md`

**Intent**: Show how the **real channel** (amplitude sector) gives rise to the spacetime metric g_μν. Derive the projection mechanism: Θ → S_Θ → g_μν. Recover Einstein's field equations in the appropriate limit. Demonstrate GR equivalence.

**Status**: 🚧 Stub created

---

### D05: Dirac Coupling (Phase Channel)
**File**: `D05_dirac_coupling_phase_channel.md`

**Intent**: Show how the **phase channel** (Σ_Θ and internal phases φᵢ) couples to Dirac spinors. Derive the minimal coupling mechanism. Establish connection to quantum mechanical phase and gauge structure.

**Status**: 🚧 Stub created

---

### D06: Nonlocality and Holonomy Constraints
**File**: `D06_nonlocality_holonomy_constraints.md`

**Intent**: Develop the framework for nonlocal correlations using phase holonomy. Define closed-loop integrals of Σ_Θ. Establish topological sectors via winding numbers. Show how global phase constraints arise **without external chronofactor or extra dimensions**.

**Status**: 🚧 Stub created

---

## Derivation Principles

### Clean-Room Approach
- **No chronofactor**: τ = t + iψ is never assumed or introduced
- **From scratch**: Each derivation starts from Θ(q) and builds up
- **Self-contained**: Each file can be read independently (with references to prerequisites)

### Mathematical Rigor
- **Definitions first**: Clearly state all mathematical objects before use
- **Proofs included**: Derive results, don't just assert them
- **Approximations stated**: When taking limits or approximations, state assumptions explicitly

### Physical Interpretation
- **Connect to observables**: Always link mathematical structures to measurable quantities
- **No hand-waving**: Avoid vague statements like "phase emerges naturally"
- **Legacy mapping**: Where relevant, explain how this relates to chronofactor formulation

## Development Status

| Derivation | File | Status | Next Action |
|------------|------|--------|-------------|
| D01 | `D01_theta_and_8D.md` | Stub | Define biquaternion algebra |
| D02 | `D02_polar_decomposition.md` | Stub | Develop amplitude/phase split |
| D03 | `D03_entropy_and_phase.md` | Stub | Prove observable properties |
| D04 | `D04_emergent_metric_Re_channel.md` | Stub | Derive GR recovery |
| D05 | `D05_dirac_coupling_phase_channel.md` | Stub | Establish quantum coupling |
| D06 | `D06_nonlocality_holonomy_constraints.md` | Stub | Develop topological framework |

**Overall Progress**: Initial scaffolding complete. Full derivations pending.

## How to Read

### Sequential Reading (Recommended)
1. Start with D01 to understand the fundamental field
2. Proceed through D02-D06 in order
3. Each derivation assumes knowledge of previous ones

### Topic-Based Reading
- **Gravity focus**: D01 → D03 → D04
- **Quantum focus**: D01 → D02 → D05
- **Topology focus**: D01 → D03 → D06

## Contributing to Derivations

When adding content to these files:

1. **Maintain rigor**: Show your work, include proofs
2. **No chronofactor**: If you find yourself needing τ, reconsider the approach
3. **Clear notation**: Define all symbols before use
4. **Physical context**: Explain why each step matters physically
5. **Open questions**: Include "Open Questions" sections for unresolved issues

## Open Questions (Global)

These questions span multiple derivations and guide future development:

1. **Uniqueness**: Is the polar decomposition Θ = |Θ| exp(iΦ) unique? If not, what physical principle selects the decomposition?

2. **Determinant convention**: What is the correct definition of det(Θ) for a biquaternion? Does it differ from quaternionic determinant?

3. **Metric emergence**: What boundary conditions on Θ ensure that g_μν is Lorentzian (signature -+++) rather than Euclidean?

4. **Phase quantization**: Are there constraints forcing Σ_Θ to be quantized? If so, what are the quantum numbers?

5. **Nonlocal range**: Over what length scales do phase holonomy effects persist? Is there a characteristic scale?

6. **Legacy equivalence**: Can the chronofactor formulation be recovered as a special case? If so, under what approximation?

## Notation Conventions

To maintain consistency across derivations:

- **Θ(q)**: Biquaternion field at spacetime point q = (t, x, y, z)
- **Θᵢ**: Complex quaternion components (i = 0,1,2,3)
- **Aᵢ, φᵢ**: Real amplitude and phase parts of Θᵢ
- **S_Θ**: Entropy channel observable
- **Σ_Θ**: Phase channel observable
- **g_μν**: Emergent spacetime metric
- **k_B**: Boltzmann constant
- **∇**: Covariant derivative (with respect to emergent metric)

## References to Core

All derivations should reference:
- **Core definitions**: `/ubt_core/README.md`
- **Python implementations**: `/ubt_core/theta_field.py`, `/ubt_core/entropy_phase.py`
- **Legacy formulation**: `/legacy/ubt_with_chronofactor/` (for comparison)

---

**Status**: Scaffolding phase complete. Detailed derivations pending.  
**Next Steps**: Populate D01 with biquaternion algebra foundations.
