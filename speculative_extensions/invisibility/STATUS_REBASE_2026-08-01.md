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

# Status rebase of ST-1--ST-5

The files `st1_...` through `st5_...` were written before the July 2026
central-anticommutator/covariant-tetrad lock-in. They are retained as historical
speculative work but must not be read as current canonical definitions.

## Obsolete assumption in the older texts

Several passages assume a symmetric metric of the direct form

\[
\mathcal G_{\mu\nu}
=g_{\mu\nu}+i h_{\mu\nu}
+\mathbf j a_{\mu\nu}+\mathbf k b_{\mu\nu}.
\]

The current algebraic result is more constrained. For the sharp-based ordered
bilinear

\[
\mathfrak G_{\mu\nu}=E_\mu^\sharp E_\nu,
\]

the symmetric part is central complex and the genuinely quaternionic part is
antisymmetric:

\[
\mathfrak G_{\mu\nu}
=\gamma_{\mu\nu}\mathbf1+\Sigma_{\mu\nu}.
\]

Accordingly, the old `j a_mu_nu + k b_mu_nu` symmetric-metric ansatz is neither
canonical nor established by the current sharp algebra.

## What survives

The following research questions remain valid after rebasing:

- can `det(gamma)=0` define a regular dynamical phase?
- can `gamma=0` while `Sigma!=0` occur on shell?
- can visible matter couple only to the central metric channel?
- can a full noncentral Hermitian or noncommutative metric be defined
  consistently?
- can exterior scattering vanish across a regular boundary?

## Reading order

Read `README.md` and `BIQUATERNIONIC_METRIC_NULLITY_PROGRAM.md` first. The older
ST files then serve as a source of candidate questions, not as proofs or current
formulae.
