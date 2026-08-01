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

# Weinberg angle — GUT-normalised boundary theorem

Status: L1 conditional on the UBT hypercharge bridge.

This patch proves the group-theoretic Weinberg-angle boundary value

```math
sin^2(theta_W)(M_GUT) = 3/8.
```

The proof uses the one-generation hypercharge assignments derived in
`research_tracks/EW/hypercharge_from_ubt.tex`:

```math
Y_Q=1/6, Y_u=2/3, Y_d=-1/3, Y_L=-1/2, Y_e=-1, Y_nu=0.
```

The norm sums are

```math
sum Y_i^2 dim(r_i) = 10/3,
sum T_{3,i}^2 dim(r_i) = 2.
```

Therefore

```math
k_Y = (10/3)/2 = 5/3.
```

At a unified boundary `g_1 = g_2` with `g_1^2 = k_Y g_Y^2`, this gives

```math
g_Y^2/g_2^2 = 3/5,
sin^2(theta_W) = (3/5)/(1+3/5) = 3/8.
```

## Remaining work

The GUT boundary is now clean.  The low-energy value near 0.231 still requires
RG running and scale closure from the UBT compactification scale to the measured
electroweak scale.
