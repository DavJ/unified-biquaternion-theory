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

# Student paper: indices, torsion, curl, and the UBT anticommutator

**Date:** 2026-08-02  
**Provenance:** Tier C working / explicitly AI-generated educational draft

This patch adds a Czech standalone student paper to `docs/textbook/`:

- `docs/textbook/indices_torsion_anticommutator_rot_student_paper_cs.tex`
- `docs/textbook/student_papers/indices_torsion_anticommutator_rot_cs.tex`
- `docs/pdfs/UBT_Studentske_texty_Indexy_torze_antikomutator_rot_2026-08-02.pdf`

The paper explains:

1. upper/lower, free/dummy, input/output and direction indices;
2. `Gamma^rho_{mu nu}` as a matrix `Gamma_mu` for every derivative direction;
3. the distinction between curl, torsion, curvature, off-diagonal matrix entries,
   and the algebraic bivector channel;
4. the UBT anticommutator metric readout and the complementary `Sigma` channel;
5. why `gamma=0, Sigma!=0` does not imply or require torsion;
6. why algebraic metric nullity is not yet physical invisibility.

No canonical scientific claim or provenance-tier assignment is changed. The new
sources inherit Tier C from the existing `docs/**` rule in
`PROVENANCE_TIERS.yaml`.
