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


# Alpha EM projection theorem — closure step

This patch adds the next closure step for the alpha derivation:

```text
research_tracks/T3_ALPHA/electroweak_em_projection_theorem.tex
```

It proves, conditionally on the standard electroweak vacuum representation,
that the residual unbroken generator is the primitive compact electromagnetic
one:

```text
Q_EM = T3 + Y/2
```

and that there is no continuous charge-rescaling freedom
`Q_EM -> lambda Q_EM` once the electron Wilson-line unit charge is fixed.

This reduces the remaining alpha proof condition from:

```text
UBT EM projection = compact unit-charge U(1)_EM
```

to the sharper vacuum theorem:

```text
Theta_0 must be derived from S[Theta] as the (SU(2)_L, Y=1) electroweak doublet vacuum.
```

It does not derive the Weinberg angle.  That is intentional: the alpha route
uses the final compact U(1)_EM coupling modulus directly.  The Weinberg angle
controls the decomposition of the photon into W3 and B before symmetry breaking,
not the primitive compact electromagnetic generator.
