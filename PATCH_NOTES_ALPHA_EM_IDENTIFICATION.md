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

# Patch notes — alpha EM identification

This patch adds:

```text
research_tracks/T3_ALPHA/em_modular_coupling_identification.tex
```

and updates:

```text
research_tracks/T3_ALPHA/alpha_derivation_complete.tex
docs/reports/alpha_em_identification_closure.md
```

Purpose: close the final alpha interpretation gap by matching the UBT
winding modulus to the standard compact-U(1) electromagnetic coupling modulus:

```text
tau_EM = theta/(2*pi) + i 4*pi/e^2
```

Therefore, at theta = 0:

```text
n = Im(tau_EM) = 4*pi/e^2 = alpha^-1
```

Status: conditional closure.  The remaining structural task is the full
low-energy electroweak projection theorem showing that the UBT EM projection is
the physical compact unit-charge U(1)_EM bundle.  No numerical fit is added.
