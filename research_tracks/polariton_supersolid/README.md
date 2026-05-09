<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Polariton Supersolid — Research Track

**Status:** 🔵 EXPLORATORY  
**Confidence:** Candidate  
**Layer:** Research Track  
**Created:** 2025  
**Version:** 0.1

---

## ⚠️ Scope Disclaimer

This research track has **two clearly separated parts**:

| Part | Content | Status |
|------|---------|--------|
| **Standard Physics** | Driven-dissipative GP equation, polariton BEC, supersolid phase | Established condensed-matter physics |
| **UBT Bridge Hypotheses** | Speculative connections between polariton field theory and UBT Θ-field | **Speculative — NOT part of canonical UBT** |

The standard-physics sections stand on their own and require no UBT framework.
The bridge hypotheses are clearly labeled **SPECULATIVE** and await mathematical closure
before any promotion.

**No consciousness claims are made anywhere in this track.**

---

## What Are Polariton Supersolids?

**Exciton-polaritons** are hybrid light-matter quasiparticles formed in semiconductor
microcavities where cavity photons strongly couple to exciton resonances. Because
photons have a very small effective mass (m\* ~ 10⁻⁵ mₑ), polaritons can undergo
Bose-Einstein condensation (BEC) at temperatures orders of magnitude above atomic
BEC thresholds — including at room temperature in some material systems.

A **supersolid** is a quantum phase of matter that simultaneously exhibits:
- **Superfluidity** — off-diagonal long-range order (ODLRO), frictionless flow
- **Crystalline order** — diagonal long-range order (DLRO), periodic density modulation

Polariton systems are driven-dissipative: polaritons decay (photon leakage through
mirrors), requiring continuous optical pumping. The non-equilibrium steady state
(NESS) supports rich phase diagrams including stripe phases and density-modulated
condensates that are analogues of supersolids.

---

## Why This Is Interesting for UBT

UBT's fundamental field Θ(q, τ) is defined over biquaternionic coordinates with
**complex time** τ = t + iψ. The imaginary component ψ introduces phase dynamics
that could, in principle, be studied in condensed-matter analogues:

1. **Non-equilibrium steady states** in polariton systems map loosely onto UBT's
   complex-time structure, where the imaginary part encodes phase coherence / dissipation.
2. **Driven-dissipative condensates** have a natural description via a complex
   order parameter — formally similar to Θ projected onto a two-component real
   sector.
3. **Spontaneous symmetry breaking** that yields both superfluidity and density order
   might illuminate how UBT's Θ-field generates emergent metric and gauge structures.

These are **candidate analogies only**. The mathematical correspondence has not been
derived. Bridge hypotheses are in `ubt_bridge/BRIDGE_HYPOTHESES.md`.

---

## Directory Structure

```
polariton_supersolid/
├── README.md                        ← This file
├── LITERATURE_REVIEW.md             ← Curated references with summaries
├── gp_equation/
│   └── gp_derivation.md            ← Gross-Pitaevskii baseline derivation
├── simulation/
│   └── gp_simulator.py             ← Numerical simulation scaffold (Python)
├── ubt_bridge/
│   └── BRIDGE_HYPOTHESES.md        ← Candidate UBT bridge hypotheses [SPECULATIVE]
└── predictions/
    └── PREDICTION_INVENTORY.md     ← Experimentally testable predictions
```

---

## Quick Start

### Run the GP simulation

```bash
python research_tracks/polariton_supersolid/simulation/gp_simulator.py
```

This runs a 2D split-step simulation of the driven-dissipative Gross-Pitaevskii
equation and prints a summary of supersolid diagnostics.

### Read the derivation

`gp_equation/gp_derivation.md` contains a self-contained derivation of the polariton
GP equations from first principles (second quantization → mean-field → driven-dissipative
extension), with all symbols defined.

### Review the predictions

`predictions/PREDICTION_INVENTORY.md` lists all experimentally testable predictions,
grouped by whether they depend only on standard physics or also on the UBT bridge.

---

## Current Status

| Deliverable | Status |
|------------|--------|
| Literature review | ✅ Draft complete |
| GP equation derivation | ✅ Complete |
| Simulation scaffold | ✅ Runnable |
| UBT bridge hypotheses | 🔵 Candidate (unproven) |
| Prediction inventory | ✅ Draft complete |
| Experimental validation | ❌ Not started |
| Promotion to canonical | ❌ Bridge not closed |

---

## Language Guidelines

### Acceptable language for this track

✅ "The polariton order parameter is **analogous to** a projection of Θ"  
✅ "The driven-dissipative structure **may be related to** complex-time dynamics"  
✅ "**Candidate hypothesis:** the stripe instability corresponds to …"  
✅ "**Consistent with**, but not derived from, canonical UBT"  

### Unacceptable language

❌ "Polariton condensates **prove** UBT"  
❌ "Supersolid order **is** the Θ-field"  
❌ "Consciousness plays a role in polariton dynamics"  
❌ Any suggestion that supersolid phases are related to mind or awareness  

---

## Relationship to Canonical UBT

This track is **not part of canonical UBT**. No content here is used in
`canonical/`. Bridge hypotheses would require:

1. A precise algebraic mapping from polariton Hamiltonian to UBT Θ-field sector.
2. Derivation of at least one novel (non-trivial) prediction from the UBT side that
   differs from standard polariton theory.
3. Independent numerical verification.

Until those conditions are met, this track has confidence level **Candidate**.

---

**Last Updated:** 2025  
**Contact:** See repository root
