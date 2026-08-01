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

# Patch notes — Weinberg angle GUT-normalisation theorem

Adds:

- `research_tracks/EW/weinberg_angle_gut_norm_theorem.tex`
- `docs/reports/weinberg_angle_gut_norm_status.md`
- `tools/compute_weinberg_gut_norm.py`

Updates:

- `research_tracks/EW/weinberg_angle_ew1_rg.tex`

Result:

Using the UBT hypercharge bridge, the one-generation norm sums are

```math
sum Y_i^2 dim(r_i) = 10/3,
sum T_3^2 dim(r_i) = 2.
```

Therefore

```math
k_Y = 5/3,
g_Y^2/g_2^2 = 3/5,
sin^2(theta_W)(M_GUT) = 3/8.
```

This proves the GUT boundary value.  The remaining low-energy task is RG/scale
closure down to the measured electroweak scale.
