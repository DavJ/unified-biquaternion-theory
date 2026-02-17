# UBT Object Mapping Table

Correspondence between objects in the two first-class formulations.

## Core Object Mapping

| Concept | With Chronofactor (`ubt_with_chronofactor`) | Without Chronofactor (`ubt_no_chronofactor`) |
|---|---|---|
| Time evolution driver | Complex time τ = t + iψ via chronofactor χ | Phase channels Σ_Θ of the 8D Θ field |
| Primary field | Θ(q, τ) — field over complex time | Θ(q) — field over real coordinates |
| Chronofactor | Explicit χ(τ) coupling phase and real time | Absent; encoded in Σ_Θ structure |
| Phase channel | Im(Θ) sector modulated by τ | Σ_Θ = polar-phase component of Θ |
| Metric projection | g_μν = Re(Θ†Θ)_μν | g_μν = Re(Θ†Θ)_μν (same projection) |
| Gauge currents | Derived from ∂_τΘ via complex derivative | Derived from ∂_q Θ without τ-extension |
| Observable: α | Extracted from Re(log det Θ) + chrono-correction | Extracted from Re(log det Θ) directly |
| Observable: CMB | Residual modulation depends on χ-mode spectrum | Residual modulation from Σ_Θ only |

## Shared Observable Pipelines

The following observables use the same extraction pipeline but differ in input assumptions:

| Observable | Shared pipeline? | Where assumptions diverge |
|---|---|---|
| CMB fingerprint / comb signature | Yes — `forensic_fingerprint` tools | Chronofactor shifts comb period by δ(χ) |
| Fine structure constant α | Yes — α-from-log-det route | Phase-winding correction term differs |
| Fermion masses | Partially — same projection mechanism | Chronofactor adds Yukawa-like renormalization |
| Dark matter density | No shared pipeline yet | Open research area |

## Status

This mapping is preliminary. Both formulations are under active development.
Entries marked "Open" indicate unresolved correspondences requiring further derivation.

| Item | Status |
|---|---|
| Chronofactor ↔ Σ_Θ identification | Open hypothesis |
| Comb period shift δ(χ) derivation | Open |
| Full Lagrangian equivalence proof | Open |
| UV/IR behaviour comparison | Open |
