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

# Patch notes — EW odd-spinor readout proof

Adds:

- `research_tracks/T3_ALPHA/ew_odd_spinor_readout_theorem.tex`
- `docs/reports/alpha_ew_odd_spinor_readout_closure.md`

Also includes the missing determinant audit file:

- `research_tracks/T3_ALPHA/psi_determinant_ew_mass_sign_theorem.tex`

Updates:

- `research_tracks/T3_ALPHA/odd_winding_fermionic_ew_sign_theorem.tex`
- `research_tracks/T3_ALPHA/alpha_derivation_complete.tex`

Result:

The target condition

```math
Pi_EW Theta subset H_{odd,spinor}
```

is derived from existing repository bridges: SU(2)_L left action on the spinorial
component, psi-parity chirality, and Grassmannian measure for odd winding modes.

This gives the fermionic determinant sign required for the non-zero EW vacuum
and allows the alpha chain to be marked PROVEN relative to current UBT bridge
assumptions.
