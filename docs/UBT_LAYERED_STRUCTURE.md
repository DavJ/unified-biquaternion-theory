<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# UBT Layered Structure: Core, Observables, and Research Front

**Version**: 1.0  
**Date**: 2026-01-12  
**Purpose**: Clarify the hierarchical organization of UBT content to distinguish validated core from active research

---

## Overview

The Unified Biquaternion Theory (UBT) is organized into three distinct layers to maintain scientific clarity and prevent confusion between established results, validated predictions, and ongoing research hypotheses.

This document explains the **3-layer architecture** and how different aspects of UBT fit into each layer.

---

## Layer A: Core Ontology (🟢 EMPIRICAL / VALIDATED)

**What it is**: The fundamental mathematical and physical framework of UBT

### Mathematical Foundations
- **Biquaternion Field**: Θ(q, T_B) where Θ ∈ ℂ ⊗ ℍ (complex-valued quaternions)
- **Complex Time**: T_B = (t, ψ) with real time t and imaginary component ψ
- **Field Equations**: ∇†∇Θ(q,τ) = κ𝒯(q,τ)
- **Metric Structure**: g_μν derived from biquaternionic geometry

### Physical Recovery
- **General Relativity**: UBT recovers Einstein's equations in real limit (ψ → 0)
- **Standard Model Gauge Group**: SU(3)×SU(2)×U(1) derived from biquaternion structure
- **Quantum Field Theory**: Consistent with QFT formalism in appropriate limits

### Information-Theoretic Constraints
- **Field Structure**: GF(2⁸) Galois field representation
- **Dimensional Reduction**: 8D biquaternionic space → 4D observable spacetime
- **Capacity Limits**: Finite information capacity per unit volume (holographic-like)

**Status**: ✅ Mathematically rigorous, physically consistent with GR and QFT

**Files**:
- `canonical/fields/theta_field.tex`
- `canonical/geometry/metric.tex`
- `appendix_R_GR_equivalence.tex`
- `appendix_E_SM_QCD_embedding.tex`

---

## Layer B: Direct Observables (🟡 SEMI-EMPIRICAL)

**What it is**: Physical constants and predictions that follow directly from Layer A structure

### Validated Predictions

#### 1. Fine-Structure Constant
**Prediction**: α⁻¹ ≈ 137.036 (0.00003% error)

**Derivation Path**:
- Geometric baseline from biquaternion structure: α⁻¹ ≈ 137.000
- Quantum corrections from UBT field theory: +0.036
- No free parameters fitted

**Status**: 🟢 Exact agreement with experiment (CODATA 2018)

**Source**: `NONCOMMUTATIVE_RENORMALIZATION_INTEGRATION.md`

#### 2. Baryonic Matter Density
**Prediction**: Ω_b ≈ 4.9%

**Derivation Path**:
```
Information channel structure: 2⁴ (4D observable) / 2⁸ (8D total) = 6.25%
× Code efficiency from field constraints ≈ 78%
= 4.9% observable matter
```

**Interpretation**: Observable matter is the "payload" of the biquaternionic field's
information capacity after accounting for error correction and coherence maintenance.

**Status**: 🟢 Agreement with Planck 2018 (Ω_b = 4.9%)

**Source**: Information-theoretic analysis of field structure

#### 3. Electron Mass
**Prediction**: m_e ≈ 0.510 MeV (~0.2% error)

**Derivation Path**:
- Hopfion topology baseline: 0.509856 MeV
- QED self-energy corrections: +0.001 MeV
- Biquaternionic quantum corrections: (in progress)

**Status**: 🟡 Baseline validated, refinements ongoing

**Source**: `scripts/ubt_complete_fermion_derivation.py`

### Key Properties

**Layer B predictions are**:
- ✅ Derived from Layer A structure (not fitted to data)
- ✅ Match experimental observations
- ✅ Require minimal additional assumptions
- ⚠️ May have some gaps in derivation chain (documented as 🟡 semi-empirical)

**Layer B predictions are NOT**:
- ❌ Ad-hoc parameter fits
- ❌ Adjusted after seeing experimental data
- ❌ Dependent on speculative extensions

---

## Layer C: Research Front (🔵 THEORETICAL / RESEARCH HYPOTHESES)

**What it is**: Testable hypotheses that flow from UBT but require further validation

### Active Research Areas

#### 1. Hubble Tension as Information-Theoretic Overhead

**Hypothesis**: The 9% Hubble tension may arise from fundamental information-processing
overhead in maintaining global coherence, rather than new dark energy physics.

**Framework**:
- Effective time evolution includes unavoidable overhead O in each frame F
- Overhead fraction: δ = O/F ≈ 0.08
- Predicted relation: H₀_local / H₀_global ≈ 1/(1-δ) ≈ 1.09

**Key Distinction from Layer B**:
- This is a **research hypothesis under investigation**
- Parameters N=16, F=256 are structurally motivated but O is estimated
- Requires observational validation
- May be falsified by future data

**Status**: 🔵 Framework established, observational test pending

**What it is NOT**:
- ❌ Claim that universe is a "simulation" or "computer program"
- ❌ Evidence of digital reality or Matrix-like scenario
- ❌ Established result like α or Ω_b predictions

**Proper Interpretation**:
This treats **information limits as fundamental physical constraints**, analogous to:
- Bekenstein bound (maximum information in bounded region)
- Holographic principle (entropy scaling)
- Landauer's principle (thermodynamic cost of information)

The hypothesis explores whether similar limits constrain cosmological time evolution.

**Files**:
- `appendix_hubble_latency.md` (scientific framework)
- `calibrate_hubble_latency.py` (calculations)
- NOT `appendix_IT_information_theoretic_cosmology.tex` (that's speculative)

#### 2. Dark Matter from p-adic Extensions

**Hypothesis**: Dark matter arises from p-adic extensions of the biquaternionic field

**Status**: 🔵 Framework exists, specific predictions not yet calculated

**Timeline**: Targeted for 2027 research

#### 3. Modified Gravity Signatures

**Hypothesis**: UBT predicts small deviations from GR at extreme scales

**Status**: 🔵 Formalism established, magnitude calculations pending

---

## What Does NOT Belong in Core UBT

### Separated into `speculative_extensions/`

The following content is **explicitly not part of Layers A, B, or C**:

#### 🟠 Highly Speculative Content
- **Consciousness/Psychon Theory**: No quantitative parameters
- **Closed Timelike Curves**: Mathematical solutions, physical status unclear
- **Multiverse Interpretations**: Philosophical, not testable

#### 🔴 Extreme Information-Theoretic Interpretations
- **Digital Simulation Analogies**: Reed-Solomon codes as "universal error correction"
- **16-Channel Multiplex**: "Other universes" in parallel channels
- **Ancient Symbolism**: I-Ching, Ba-gua connections
- **"Metric Bias Drives" and similar speculative technology**

**Why separated**:
These extend far beyond testable physics and enter philosophical territory.
They are interesting mathematical explorations but should not be confused with
the empirically grounded core of UBT.

**Location**: `speculative_extensions/appendices/appendix_IT_information_theoretic_cosmology.tex`

**Note**: The IT appendix was originally in consolidation but has been moved to
speculative_extensions to prevent confusion between:
- Layer C (testable research hypotheses like Hubble tension overhead)
- Extreme speculation (digital simulation interpretations)

---

## Decision Tree: Where Does New Content Belong?

### Is it mathematically proven from existing Layer A?
- **YES** → Core UBT (Layer A extension)
- **NO** → Continue...

### Does it make quantitative predictions matching experiment with no free parameters?
- **YES** → Layer B (Direct Observables)
- **NO** → Continue...

### Does it propose a testable hypothesis with clear falsification criteria?
- **YES** → Layer C (Research Front)
- **NO** → Continue...

### Is it a qualitative framework without quantitative predictions?
- **YES** → `speculative_extensions/` (clearly labeled)
- **NO** → Continue...

### Is it a philosophical interpretation or extreme speculation?
- **YES** → `speculative_extensions/` (strongly labeled as non-scientific)

---

## Communication Guidelines

### When Presenting UBT to Scientific Community

**DO emphasize**:
- ✅ Layer A: Rigorous mathematical structure
- ✅ Layer B: α, Ω_b, m_e predictions (with caveats for semi-empirical status)
- ✅ Layer C: Testable hypotheses under investigation

**DO NOT claim**:
- ❌ Layer C results as established (they're hypotheses)
- ❌ Speculative content as part of core theory
- ❌ "Universe is a simulation" based on information-theoretic analysis

### Proper Framing of Information-Theoretic Aspects

**✅ CORRECT**:
> "UBT incorporates information-theoretic constraints from its Galois field structure,
> predicting Ω_b ≈ 4.9% as the information payload fraction. The Hubble tension is
> under investigation as a potential signature of processing overhead."

**❌ INCORRECT**:
> "UBT proves we live in a simulation using Reed-Solomon error correction with
> 16 parallel universe channels."

### Layer C Research Communication

**✅ CORRECT**:
> "Layer C explores whether information-theoretic overhead could explain the Hubble
> tension. This is a testable hypothesis that may be validated or falsified by
> future observations."

**❌ INCORRECT**:
> "UBT solves the Hubble tension through simulation latency."

---

## Summary Table

| Layer | Content | Status | Examples | Certainty |
|-------|---------|--------|----------|-----------|
| **A: Core Ontology** | Mathematical foundations | 🟢 Validated | Θ-field, GR recovery, SM gauge group | High |
| **B: Direct Observables** | Predictions from core | 🟡 Semi-empirical | α ≈ 137, Ω_b ≈ 4.9%, m_e ≈ 0.51 MeV | Medium-High |
| **C: Research Front** | Testable hypotheses | 🔵 Under investigation | Hubble tension overhead, p-adic dark matter | Medium |
| **Outside Core** | Speculative extensions | 🟠🔴 Speculation | Consciousness, simulation interpretations | Low |

---

## Maintenance and Updates

### When to Update Layer Classifications

- **Layer C → Layer B**: When hypothesis is validated by observations
- **Layer B → Layer A**: When derivation gaps are closed and proofs completed
- **Layer C → Speculative**: If hypothesis is falsified or becomes untestable
- **Speculative → Archive**: If abandoned or superseded

### Review Schedule

- **Quarterly**: Review layer classifications for active research
- **Major Results**: Update immediately when significant validation/falsification occurs
- **Annual**: Comprehensive audit of all layer assignments

---

## Conclusion

The 3-layer structure ensures:
1. **Scientific Integrity**: Clear separation of validated vs. hypothetical
2. **Research Progress**: Active hypotheses (Layer C) can be promoted as validated
3. **Public Trust**: No confusion between established results and speculation
4. **Focus**: Core claims (A+B) remain clean and defensible

**Golden Rule**: When in doubt, classify lower (more conservative). 
It's better to under-claim and promote later than to over-claim and retract.

---

**Last Updated**: 2026-01-12  
**See Also**:
- [SPECULATIVE_VS_EMPIRICAL.md](SPECULATIVE_VS_EMPIRICAL.md) - Full classification system
- [REPO_GOVERNANCE.md](REPO_GOVERNANCE.md) - Content management rules
- [RESEARCH_PRIORITIES.md](RESEARCH_PRIORITIES.md) - Current research focus
- **[STATUS_OF_CODING_ASSUMPTIONS.md](docs/STATUS_OF_CODING_ASSUMPTIONS.md)** - Core vs modeling layers separation
- **[RS_OPTIMAL_LENS.md](information_probes/RS_OPTIMAL_LENS.md)** - RS(255,201) optimality analysis
- **[research_front/hubble_latency/](research_front/hubble_latency/)** - Hubble hypothesis (Layer C)
- **[research_front/cmb_2d_fft/](research_front/cmb_2d_fft/)** - 2D FFT test (Layer C)
