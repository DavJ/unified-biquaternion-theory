# Core UBT - Geometric Foundations

**Purpose:** This directory will house core UBT geometric derivations, independent of all modeling assumptions.

**Status:** Under construction (January 2026 reorganization)

---

## What Belongs Here

Content that is **independent of subsequent coding/discretization assumptions:**

- Biquaternionic field structure: Θ(q, τ) where Θ ∈ ℂ ⊗ ℍ
- Field equations: ∇†∇Θ(q,τ) = κ𝒯(q,τ)
- Metric derivations from biquaternionic geometry
- General Relativity recovery (real limit ψ → 0)
- Standard Model gauge group emergence (SU(3)×SU(2)×U(1))
- Baseline α derivation from geometric phase structure
- Hopfion topology for fermion masses
- Quantum field theory compatibility

**Key principle:**
> "Core UBT is derived from geometric phase rotation and metric structure, **independent of subsequent coding assumptions**."

---

## What Does NOT Belong Here

- Discretization models (GF(2⁸), 256-tick framing) → Goes in `quantization_grid/`
- Reed-Solomon coding framework → Goes in `information_probes/`
- Probe-dependent predictions (Ω_b from RS) → Documented in `information_probes/`
- Exploratory hypotheses (Hubble latency, 2D FFT) → Goes in `research_front/`

---

## Current Status

**Phase 1 (January 2026):** Directory created, structure defined

**Phase 2 (Future):** Migrate core geometric content from:
- `canonical/fields/theta_field.tex`
- `canonical/geometry/metric.tex`
- `THEORY/architecture/geometry/`
- Other core derivations

**Phase 3 (Future):** Organize into clean subsections:
- `metric/` - Biquaternionic metric structure
- `field_equations/` - Core field equations and solutions
- `gr_recovery/` - GR limit derivations
- `sm_emergence/` - Gauge group emergence
- `observables/` - Baseline α, m_e from pure geometry

---

## Related Documentation

- **[STATUS_OF_CODING_ASSUMPTIONS.md](../docs/STATUS_OF_CODING_ASSUMPTIONS.md)** - Separates Core from modeling layers
- **[UBT_LAYERED_STRUCTURE.md](../UBT_LAYERED_STRUCTURE.md)** - Layer A definition
- **[SPECULATIVE_VS_EMPIRICAL.md](../SPECULATIVE_VS_EMPIRICAL.md)** - Rigor classification

---

**Created:** 2026-01-13  
**Status:** Placeholder - content migration planned for future phase
