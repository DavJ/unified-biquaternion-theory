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

# Alpha Path B — EW odd-spinor readout theorem

Status: L1, relative to existing canonical bridge inputs.

This patch proves the target condition required by the odd-winding fermionic
sign route:

```math
Pi_EW Theta subset H_{odd,spinor}.
```

The proof uses three existing repository inputs:

1. SU(2)_L weak fields arise from the left action on the spinorial component of
   Theta.
2. P_psi acts as gamma^5 on spinors; odd winding modes n > 0 are left-handed.
3. Odd winding modes carry a Berezin/Grassmann measure.

Therefore the electroweak Layer2 readout lies in the odd-winding spinor sector,
and the electroweak compact determinant has fermionic sign:

```math
Delta V_EW^(2) = -Tr(D_odd^{-1} K_EW) Phi^dagger Phi.
```

For positive spectral coupling this gives

```math
m_eff^2 < 0,
mu_EW^2 > 0.
```

Combined with the previous chain, alpha can be marked as PROVEN within the
current UBT bridge assumptions.  This is an internal repository proof status,
not a claim of external peer-reviewed acceptance.
