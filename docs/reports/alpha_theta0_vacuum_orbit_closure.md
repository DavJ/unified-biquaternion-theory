<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# Theta0 electroweak vacuum orbit theorem — alpha closure step

This patch adds:

```text
research_tracks/T3_ALPHA/theta0_electroweak_vacuum_orbit_theorem.tex
```

It proves the representation/orbit part of the previous alpha condition:
any non-zero vacuum in the minimal UBT electroweak doublet sector is
gauge-equivalent to

```text
Phi0 = (0, v/sqrt(2))^T,  Y = 1.
```

Therefore the standard electroweak doublet vacuum shape is not an independent
extra assumption.  It follows from:

```text
C ⊗ H ≅ Mat(2,C),
SU(2)_L left action,
U(1)_Y right scalar phase,
SU(2) transitivity on non-zero doublets.
```

Remaining alpha condition after this patch:

```text
V(Theta) has a non-zero minimum in the minimal electroweak doublet sector.
```

No numerical fit is added.
