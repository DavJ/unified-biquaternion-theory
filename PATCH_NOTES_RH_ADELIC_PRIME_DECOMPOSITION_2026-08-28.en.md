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

# Patch notes: adelic prime-decomposition reset

**Date:** 2026-08-28  
**Scope:** active RH research track; no canonical claim changes.

<a id="apd-patch-summary"></a>
## Summary

This patch implements the first decision experiment of the adelic reset. It does not add another theta--Mellin channel. Instead, it audits and connects the existing prime-Fock, rational-revival, and theta-Mellin tracks.

The restricted tensor product of radial prime spaces is shown to be unitarily equivalent to (ell^2(\mathbb N)), with

\[
H_{\log}|n\rangle=(\log n)|n\rangle.
\]

Its closure is a positive self-adjoint multiplication operator, so the former prime-Fock self-adjointness gap F5 is closed at the classical operator level. Its thermal trace remains the standard Euler identity

\[
\operatorname{Tr}(e^{-sH_{\log}})=\zeta(s),
\qquad \Re s>1.
\]

The local oscillator is identified exactly with the radial unramified Tate integral

\[
\operatorname{Tr}(p^{-sN_p})
=\int_{\mathbb Q_p^\times}\mathbf1_{\mathbb Z_p}(x)|x|_p^s\,d^\times x
=\frac1{1-p^{-s}}.
\]

This also fixes the interpretation of the modulo-(5) character work: it is a finite quotient of the unit sector at (p=5), while the prime-Fock oscillator captures only the valuation sector.

The archimedean audit corrects a structural conflation. The theta Mellin integral gives the completed channel

\[
\frac12\int_0^\infty(\vartheta(t)-1)t^{s/2}\frac{dt}{t}
=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Therefore an independent heat-trace product (artheta(t)^d\zeta(t)) is not the completed zeta function and cannot be used as its functional-equation mechanism.

For every denominator (q), CRT idempotents factor the rational quadratic revival operator over the maximal prime-power blocks (p^{v_p(q)}). The corresponding Gauss sum factorization is exact. A second elementary result sharpens the noncircularity gate: any output listing those maximal prime powers already contains the factorization of (q). The meaningful UBT question is therefore the dynamical origin of rational/profinite local sectors, not an algorithm that hides integer factorization.

<a id="apd-patch-claim-control"></a>
## Claim control

The patch establishes standard arithmetic and operator identities. It does not derive rational denominators, prime-labelled local places, unit characters, (log p) energies, or a fermionic grading from the canonical UBT action. It produces zeta as a partition function, not zeta zeros as a self-adjoint spectrum, and does not imply RH.

<a id="apd-patch-verification"></a>
## Verification

- `tools/verify_adelic_prime_decomposition.py` checks valuation reconstruction, local and finite tensor traces, graph-norm core truncation, CRT idempotents and bijections, revival-phase and Gauss-sum factorization, the (s=2) archimedean Mellin normalization, and the factorization-output gate.
- `tests/test_adelic_prime_decomposition.py` provides eight regression tests.
- The verifier uses only Python (3.12) standard-library facilities.
- Lean is unavailable in the current runtime; status is `LEAN-PENDING`, and no formal verification is claimed.
- English was the translation source. The paired Czech edition has matching anchors, equations, status labels, tables, citations, and caveats; human semantic-equivalence review remains required before merge.

<a id="apd-patch-next"></a>
## Next gate

The next experiment must extend the radial place to the local unit sector (mathbb Z_p^\times), identify the existing modulo-(5) channels with the quotient (mathbb Z_5^\times/(1+5\mathbb Z_5)), and test the inverse system over (5^k). If this yields only standard Tate factorization without a UBT-derived operator or positive trace pairing, the route remains a classical adelic repackaging.

