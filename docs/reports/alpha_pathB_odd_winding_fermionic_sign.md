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

# Alpha Path B — odd-winding fermionic EW sign route

Status: L1 conditional.

The determinant sign audit showed that the explicit bosonic compact sector
`Z_psi = eta^{-12}` gives a positive quadratic EW mass term if directly coupled
to the electroweak doublet.  That is the wrong sign for symmetry breaking.

The repository already contains a canonical bridge result:

```math
n odd => D Theta_n is a Berezin/Grassmann measure.
```

Therefore odd-winding modes produce a fermionic determinant:

```math
Delta V_odd = - Tr log(D_odd + K_EW Phi^dagger Phi).
```

This gives

```math
d Delta V_odd / d(Phi^dagger Phi)|_0 = -Tr(D_odd^{-1} K_EW).
```

If the EW Layer2 readout is supported on the odd-winding spinor sector and the
trace is positive, then

```math
m_eff^2 < 0,
mu_EW^2 > 0.
```

## Current precise target

```math
Pi_EW Theta subset H_{odd,spinor}.
```

If this readout theorem is proved from canonical Layer2 projection rules, Path B
can promote alpha from complete conditional chain to PROVEN within canonical UBT
assumptions.

Fallback remains the explicit EW symmetry-breaking postulate.
