<!-- © 2025–2026 David Jaroš — Licensed under CC BY 4.0 -->

# UBT Theory Architecture — Overview

This page gives a high-level explanation of how the Unified Biquaternion Theory is
structured, what it claims, and how its layers relate to known physics.

---

## Core Idea

UBT starts from a single mathematical object — the **biquaternion field Θ(q, τ)** —
and derives spacetime geometry, gauge symmetries, and particle content from it.

The algebra underlying the theory is **ℂ⊗ℍ** (complex tensor product of quaternions),
which is isomorphic to Mat(2, ℂ) — the algebra of 2×2 complex matrices. The Standard
Model gauge group SU(3)×SU(2)_L×U(1)_Y emerges from the automorphism and involution
structure of this algebra.

---

## Theory Layers

### Layer 0 — Pure Biquaternionic Geometry [L0]

Results that follow from the algebra ℂ⊗ℍ alone, without free parameters:

- SU(2)_L from left action of ℂ⊗ℍ on itself
- U(1)_Y from right phase rotation
- SU(3)_c from involutions on Im(ℍ)
- Non-degeneracy of emergent metric g_μν
- Lorentzian signature (−,+,+,+) of emergent spacetime

### Layer 1 — One-Loop [L1]

Results that require one-loop quantum corrections:

- Einstein field equations G_μν = 8πG T_μν from Hilbert variation of S[Θ]
- B₀ = 8π one-loop coupling baseline
- N_eff = 12 effective mode count

### Layer 2 — Higher-Loop / Non-Perturbative [L2]

Open problems requiring higher-order or non-perturbative methods:

- B_base = N_eff^{3/2} (exponent 3/2 not yet derived from first principles)
- R ≈ 1.114 loop correction factor
- Off-shell Θ-only closure of GR

---

## Separation of Concerns

UBT maintains a strict separation between three knowledge tiers:

| Tier | Directory | Contents |
|------|-----------|----------|
| **Canonical** | [`canonical/`](https://github.com/DavJ/unified-biquaternion-theory/tree/main/canonical) | Internally consistent, mathematically defined results |
| **Research tracks** | [`research_tracks/`](https://github.com/DavJ/unified-biquaternion-theory/tree/main/research_tracks) | Exploratory directions not yet canonicalised |
| **Speculative** | [`speculative_extensions/`](https://github.com/DavJ/unified-biquaternion-theory/tree/main/speculative_extensions) | Extrapolations beyond current evidence |

The wiki mirrors this separation — each section is labelled accordingly.

---

## Relation to Known Physics

### General Relativity

UBT **generalises and embeds** GR — it does not contradict or replace it.  
In the real-valued limit ψ → 0, the biquaternionic field equation

```
∇†∇Θ(q,τ) = κ𝒯(q,τ)
```

reduces exactly to Einstein's equations G_μν = 8πG T_μν.  
All experimental confirmations of GR automatically validate UBT's real sector.

→ Details: [GR Recovery](GR_Recovery)

### Standard Model

The gauge group SU(3)×SU(2)_L×U(1)_Y emerges from the algebra ℂ⊗ℍ with zero
free parameters. The Weinberg angle θ_W and fermion masses are not yet derived
from first principles.

→ Details: [Gauge Structure](Gauge_Structure), [SU(3) Structure](SU3_Structure)

### Fine Structure Constant

α ≈ 1/137.036 is reproduced in a semi-empirical framework. The structural
location of n* = 137 as the unique prime minimum of V_eff(n) is proved.
The coupling amplitude B_base = 41.57 remains a motivated conjecture.

→ Details: [Fine Structure Constant α](Alpha_Constant)

---

## Key Files in the Repository

| File | Role |
|------|------|
| [`DERIVATION_INDEX.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/DERIVATION_INDEX.md) | Single source of truth for all derivation statuses |
| [`canonical/THEORY/topic_indexes/`](https://github.com/DavJ/unified-biquaternion-theory/tree/main/canonical/THEORY/topic_indexes) | One canonical entry point per topic |
| [`canonical/UBT_canonical_main.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/UBT_canonical_main.tex) | Main canonical LaTeX document |
| [`docs/THEORY_MAP_FROM_DERIVATION_INDEX.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/docs/THEORY_MAP_FROM_DERIVATION_INDEX.md) | Full theory map derived from DERIVATION_INDEX |
