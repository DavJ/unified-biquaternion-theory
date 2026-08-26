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

# Patch notes: graded Möbius bridge

**Date:** 2026-08-25  
**Scope:** active RH research track; no canonical claim changes.

<a id="patch-summary"></a>
## Summary

This patch adds paired English/Czech research notes deriving the classical graded prime-Fock identity

\[
\operatorname{Str}(e^{-sH_P^-})=\prod_{p\in P}(1-p^{-s})
=\sum_n\mu_P(n)n^{-s}.
\]

It connects this identity to the existing bosonic prime-Fock track and to the rational theta-revival programme.

The patch also adds the first joint theta-Mellin decision experiment. The exact factorization establishes that the scalar Mellin channels of \(\vartheta_2,\vartheta_3,\vartheta_4\) have only one zeta degree of freedom and therefore impose no independent zero condition inside the open critical strip.

The characteristic extension modulo \(5\) then raises the coefficient-channel rank to four Dirichlet \(L\)-channels. The UBT-derived coupling between them remains open.

Phase and conjugation symmetry classify the admissible Hermitian channel metrics as \(\operatorname{diag}(g_0,g_1,g_2,g_1)\). An additional, not-yet-derived cyclic channel symmetry reduces this family to \(cI\), whose positivity alone still does not constrain the principal zeta zeros.

The primitive functional equations modulo \(5\) exchange the conjugate odd characters and fix the quadratic character, but preserve the same unequal channel weights. The principal character is imprimitive and has no constant root number at conductor \(5\), so these functional equations provide no mixing with the zeta channel.

<a id="patch-claim-control"></a>
## Claim control

The finite and \(\Re s>1\) identities are standard mathematics. The patch does not derive prime modes, \(\log p\) energies, or fermionic parity from canonical UBT and does not claim RH. It refines the already-open GAP-RH-MOEBIUS-UBT.

<a id="patch-verification"></a>
## Verification

- Exact subset, product-expansion, factorization, and Dirichlet-convolution checks are in tools/verify_graded_mobius_bridge.py.
- Regression coverage is in tests/test_graded_mobius_bridge.py.
- The theta-Mellin no-go result is independently checked by tools/verify_theta_mellin_matrix.py and tests/test_theta_mellin_matrix.py.
- Lean status is LEAN-PENDING; no formal verification is claimed.
- Bilingual structure and displayed equations must match before merge.

<a id="patch-provenance"></a>
## Provenance maintenance

The source inventory and its declared SHA-256 entry are synchronized to include the previously merged residue–Möbius pair and the four new governed Markdown sources in this patch.
