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

# Status of Coding Assumptions in UBT

**Version:** 1.0  
**Date:** 2026-01-13  
**Purpose:** Clarify the relationship between Core UBT geometry and subsequent coding/discretization models

---

## Executive Summary

The Unified Biquaternion Theory (UBT) is organized into distinct conceptual layers. This document separates **what is Core UBT** (geometric phase structure) from **modeling choices** (discretization, coding probes) to maintain clarity about which results are geometry-derived and which depend on additional assumptions.

---

## 1. Core UBT: Geometric Phase Structure

**What it is:**
- Biquaternionic metric Θ(q, τ) where Θ ∈ ℂ ⊗ ℍ (complex-valued quaternions)
- Complex time τ = t + iψ with real time t and imaginary component ψ
- Field equations: ∇†∇Θ(q,τ) = κ𝒯(q,τ)
- Geometric phase rotation framework

**Key derivations:**
- **General Relativity recovery:** UBT recovers Einstein's field equations R_μν - ½g_μν R = 8πG T_μν in the real limit (ψ → 0). This holds for all curvature regimes including flat spacetime, weak fields, strong fields, and cosmological solutions.
- **Standard Model gauge group:** SU(3)×SU(2)×U(1) emerges from biquaternionic structure
- **Fine-structure constant:** α⁻¹ ≈ 137 derived from geometric phase structure (baseline value)
- **Quantum field theory compatibility:** Consistent with QFT formalism in appropriate limits

**Independence statement:**
> Core UBT is derived from geometric phase rotation and metric structure, **independent of subsequent coding assumptions**. All fundamental results (GR recovery, SM gauge structure, baseline α) emerge from pure biquaternionic geometry.

**Location:** `core_ubt/`, `canonical/`, `THEORY/architecture/geometry/`

---

## 2. Quantization Grid: Discretization Model

**What it is:**
- A *model* of finite resolution in the biquaternionic field
- GF(2⁸) Galois field representation (256-state discrete structure)
- Master Clock framing: 256-tick discrete time steps
- 8D biquaternionic space → 4D observable spacetime mapping

**Status:**
- This is a **discretization choice**, not an ontological claim
- Models the field as having finite information capacity per unit volume
- Provides computational framework for calculations
- Analogous to lattice QCD: useful model, not assertion of fundamental discreteness

**Key question:**
Is the universe fundamentally discrete at Planck scale? **UBT does not require this.** The quantization grid is a modeling tool that:
- Simplifies certain calculations
- Provides information-theoretic intuition
- May or may not reflect physical reality

**Location:** `quantization_grid/`

---

## 3. Information Probes: RS as Optimal Lens

**What it is:**
- Reed-Solomon RS(255,201) error-correcting code
- Used as a **probe/lens** for mapping finite-resolution constraints to observable scalars
- MDS (Maximum Distance Separable) code: optimal for given (n,k) over GF(2⁸)

**Critical distinction:**
> RS(255,201) is **NOT asserted as the universe's actual codec**. It is an "optimal lens" - a canonical choice for exploring information-theoretic limits in the discrete model.

**What RS provides:**
- Clean mathematical framework for exploring capacity limits
- Specific parameter choices (n=255, k=201) yield observables:
  - Ω_b ≈ 4.9% (baryonic matter fraction from payload/total ratio)
  - Potential constraints on other observables
- Testable predictions that depend on RS choice (labeled "probe-dependent")

**Alternatives:**
- Other MDS codes (Generalized RS, BCH variants)
- Different (n,k) parameters
- Non-RS coding schemes (LDPC, Polar codes)
- See `information_probes/RS_OPTIMAL_LENS.md` for detailed analysis

**Status:**
- RS is chosen for its **extremal properties** (MDS optimal)
- Other codes would yield different numerical predictions
- Observable derivations using RS are **probe-dependent** and labeled as such

**Location:** `information_probes/`

---

## 4. Forensic Fingerprint: Pre-Registered Tests

**What it is:**
- Court-grade validation pipelines
- CMB phase comb analysis
- Pre-registered tests with null results included
- Designed for falsification

**Key properties:**
- Negative results are equally important as positive
- All tests documented before execution
- Transparent methodology
- No selective reporting

**Examples:**
- CMB TT spectrum comb search (NULL result - no macroscopic comb detected)
- Phase coherence tests across redshift
- Stress tests and robustness campaigns

**Status:**
Pre-registered, falsifiable tests of specific UBT predictions. Results inform theory development regardless of outcome.

**Location:** `forensic_fingerprint/`, `FORENSICS/`

---

## 5. Research Front: Active Hypotheses

**What it is:**
- Testable hypotheses under investigation
- **Not part of Core UBT**
- Exploratory research requiring validation
- Falsification is scientifically valuable

**Current hypotheses:**

### H0 Latency Hypothesis
- **Claim:** Observed Hubble tension may be consistent with synchronization drift under finite-resolution sampling
- **Status:** Hypothesis - requires validation from standard sirens, other independent tests
- **Location:** `research_front/hubble_latency/`
- **Label:** EXPLORATORY / HYPOTHESIS

### 2D FFT CMB Shear
- **Claim:** Small anisotropic tilt (~arctan(1/256)) might be detectable in 2D Fourier space of CMB patches
- **Status:** Proof-of-concept stage - synthetic tests only, no Planck results claimed
- **Location:** `research_front/cmb_2d_fft/`
- **Label:** EXPLORATORY / POC

**Key principle:**
> Research Front hypotheses are **scientific proposals**, not established results. They represent active research directions that may succeed (→ Layer B) or fail (equally valuable for science).

---

## Observable Dependency Table

| Observable | Core UBT | Quant. Grid | RS Probe | Status |
|------------|----------|-------------|----------|--------|
| GR recovery | ✅ Yes | ❌ No | ❌ No | Proven |
| SM gauge group | ✅ Yes | ❌ No | ❌ No | Derived |
| α⁻¹ baseline ≈ 137 | ✅ Yes | ❌ No | ❌ No | Geometric |
| α⁻¹ corrections → 137.036 | ✅ Yes | ⚠️ Partial | ❌ No | Semi-empirical |
| m_e (Hopfion baseline) | ✅ Yes | ❌ No | ❌ No | Topological |
| m_e (QED corrections) | ✅ Yes | ❌ No | ❌ No | Field theory |
| Ω_b ≈ 4.9% | ❌ No | ✅ Yes | ✅ Yes | Probe-dependent |
| H₀ tension "explanation" | ❌ No | ⚠️ Partial | ⚠️ Partial | Hypothesis |
| 2D FFT shear | ❌ No | ⚠️ Partial | ⚠️ Partial | Exploratory |

**Legend:**
- ✅ Yes: Observable derived from this layer
- ⚠️ Partial: Layer contributes but not sufficient alone
- ❌ No: Observable independent of this layer

---

## Stack Overview

```
┌─────────────────────────────────────────────┐
│  Research Front (Layer C)                    │
│  - Hubble latency hypothesis                 │
│  - 2D FFT CMB shear                           │
│  - Other exploratory tests                   │
│  Status: HYPOTHESIS / EXPLORATORY            │
└─────────────────────────────────────────────┘
                    ↑
┌─────────────────────────────────────────────┐
│  Forensic Fingerprint                        │
│  - Pre-registered tests                      │
│  - CMB comb (NULL)                           │
│  - Falsification campaigns                   │
│  Status: VALIDATION / COURT-GRADE            │
└─────────────────────────────────────────────┘
                    ↑
┌─────────────────────────────────────────────┐
│  Information Probes (Modeling Layer)         │
│  - RS(255,201) optimal lens                  │
│  - Probe-dependent observables               │
│  Status: MODELING CHOICE                     │
└─────────────────────────────────────────────┘
                    ↑
┌─────────────────────────────────────────────┐
│  Quantization Grid (Modeling Layer)          │
│  - GF(2⁸) discretization                     │
│  - 256-tick Master Clock                     │
│  - Finite resolution model                   │
│  Status: DISCRETIZATION MODEL                │
└─────────────────────────────────────────────┘
                    ↑
┌─────────────────────────────────────────────┐
│  Core UBT (Layer A)                          │
│  - Biquaternionic geometry                   │
│  - GR recovery                               │
│  - SM gauge structure                        │
│  - Baseline α, m_e                           │
│  Status: GEOMETRIC / PROVEN                  │
└─────────────────────────────────────────────┘
```

---

## Implications for Readers

**If you accept only Core UBT:**
- You get: GR recovery, SM emergence, geometric α and m_e derivations
- You can ignore: Quantization grid, RS codes, Hubble hypotheses

**If you also accept discretization models:**
- You add: Information-theoretic framework, capacity limits
- You get additional: Probe-dependent predictions (Ω_b with caveats)

**If you explore Research Front:**
- You engage with: Testable but unvalidated hypotheses
- You understand: These are research proposals, not established science

---

## Summary

UBT's conceptual stack is:

1. **Core UBT (Layer A):** Geometric phase structure - proven, independent of coding
2. **Quantization/RS (Modeling):** Discretization choices - useful models, not ontological claims
3. **Forensic (Validation):** Pre-registered tests - falsification-focused
4. **Research Front (Layer C):** Active hypotheses - exploratory, require validation

**The key principle:** Core UBT stands on its own geometric foundations. All subsequent layers are tools, models, or hypotheses that extend the framework without being necessary for its fundamental validity.

---

## References

- **Core UBT structure:** [UBT_LAYERED_STRUCTURE.md](../UBT_LAYERED_STRUCTURE.md)
- **Rigor classification:** [SPECULATIVE_VS_EMPIRICAL.md](../SPECULATIVE_VS_EMPIRICAL.md)
- **RS optimality analysis:** [information_probes/RS_OPTIMAL_LENS.md](../information_probes/RS_OPTIMAL_LENS.md)
- **Repository organization:** [README.md](../README.md)
