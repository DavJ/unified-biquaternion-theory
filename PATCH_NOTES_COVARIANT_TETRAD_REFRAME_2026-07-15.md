<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Covariant-tetrad geometry reframe — 15 July 2026

## Purpose

Return the canonical GR route to the original local biquaternionic intuition:
the covariant gradients of the single field form a tetrad; their central
anticommutator defines the metric; algebraic commutators carry bivector
information; commutators of covariant derivatives carry curvature.

## Canonical structure

- `E_mu = N0^(-1/2) D_mu Theta`.
- On `W_L = {i x^0 1 + x^k e_k}`, quaternion conjugation `sharp` gives
  `1/2(E_mu^sharp E_nu + E_nu^sharp E_mu) = g_munu 1`.
- No trace, real-part map, phase projector, preferred imaginary-time section,
  or compact-fiber average defines the local metric.
- `Omega_mu` is the internal frame connection; `Gamma^rho_munu` is the
  coordinate connection. They are related by tetrad compatibility, not by
  `Gamma = Re Omega`.
- Flat special relativity corresponds to zero connection curvature; in an
  inertial Cartesian frame one may choose `Omega=Gamma=0`.

## Rank result

The nondegenerate tetrad-to-metric differential has rank ten. Its six-dimensional
kernel is local Lorentz freedom. This closes the local kinematic rank question,
not the dynamical or integrability bridge.

## Open gaps

- `GAP-10Omega`: origin or unique elimination of the frame connection.
- `GAP-10L`: preservation of the Lorentz slice and centrality.
- `GAP-10I`: on-shell integrability and tetrad generation.
- `GAP-10D`: Einstein dynamics from the canonical action/master equation.
- `GAP-10psi`: classical stability along complex time.
- `GAP-B-MASTER` and `GAP-U2Theta` remain open.

## Repository policy

The former compact-fiber closure and phase-projection routes remain available
only as explicitly labelled exploratory/historical branches.
