<!-- BILINGUAL-UNIT: spectral-underdetermination.provenance -->
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

# Spectral-action underdetermination from the Clifford principal symbol

<!-- BILINGUAL-UNIT: spectral-underdetermination.scope -->
## Scope

The canonical generalized-Dirac lift fixes an exact first-order Clifford
principal symbol,

\[
\sigma_4(\xi)^2=g^{\mu\nu}\xi_\mu\xi_\nu I_4,
\qquad
\det\sigma_4(\xi)=\bigl(g^{\mu\nu}\xi_\mu\xi_\nu\bigr)^2.
\]

This determines the metric causal cone carried by the operator. A spectral
action, however, depends on the **complete** elliptic/Laplace-type operator,
not only on its principal symbol. This note gives an exact one-parameter
counterfamily showing that the Clifford principal symbol cannot by itself fix
the heat-kernel coefficients that generate the low-energy gravitational and
gauge action.

<!-- BILINGUAL-UNIT: spectral-underdetermination.family -->
## Exact one-parameter family [L0]

Let `P0` be any positive Laplace-type realization with the principal symbol
selected by the canonical UBT metric, and let `u` be a real constant. Define

\[
\boxed{P_u=P_0+uI.}
\]

The addition is zeroth order. Therefore every `P_u` has exactly the same
principal symbol as `P0`, hence the same metric and characteristic cone.
Because `uI` commutes with `P0`, the heat semigroup obeys the exact identity

\[
\boxed{e^{-tP_u}=e^{-tu}e^{-tP_0}.}
\]

If in four dimensions

\[
\operatorname{Tr}e^{-tP_0}
\sim a_0t^{-2}+a_2t^{-1}+a_4+a_6t+\cdots,
\]

then multiplication by

\[
e^{-tu}=1-ut+\frac{u^2t^2}{2}-\frac{u^3t^3}{6}+\cdots
\]

gives exactly

\[
\boxed{
\begin{aligned}
a_0(u)&=a_0,\\
a_2(u)&=a_2-u a_0,\\
a_4(u)&=a_4-u a_2+\frac{u^2}{2}a_0.
\end{aligned}}
\]

Thus operators with the **same UBT Clifford principal symbol** have different
subleading heat coefficients.

<!-- BILINGUAL-UNIT: spectral-underdetermination.consequence -->
## Consequence for the UBT spectral route

The canonical Clifford lift and its exact principal-symbol factorization are
not enough to determine a unique spectral action. At minimum the following
lower-order data must also be selected or derived:

- the complete generalized-Dirac zero-order endomorphism / mass block;
- the physical spin/gauge connection and torsion completion entering the
  lower-order symbol;
- the `psi` realization and signature/Euclidean continuation used to obtain an
  admissible spectral problem;
- the physical Hilbert-space/mode quotient and boundary conditions;
- the spectral profile/cutoff prescription if a cutoff spectral action is used.

Changing such data can leave the exact Clifford principal symbol unchanged
while changing `a2`, `a4`, and therefore the coefficients multiplying the
Einstein--Hilbert, cosmological, gauge, and other lower-energy invariants.

The existing generalized-Dirac formula in the canonical source is explicitly
an architectural candidate until derived from the UBT action, and its
zero-order block is not currently fixed by the proved Clifford relation. The
existing NCG/spectral note is likewise a working/speculative construction.

<!-- BILINGUAL-UNIT: spectral-underdetermination.no-go -->
## What is closed as a no-go

The following inference is invalid:

> the UBT Clifford principal symbol is uniquely fixed, therefore its spectral
> action and Einstein--Hilbert coefficient are uniquely fixed.

The family `P_u` is an exact counterexample to that inference.

This does **not** rule out the spectral route. It sharpens its closure target:
one must derive the complete admissible operator and spectral prescription,
not only the causal principal symbol.

<!-- BILINGUAL-UNIT: spectral-underdetermination.verification -->
## Verification

`tools/verify_spectral_symbol_underdetermination.py` multiplies the formal heat
series by `exp(-u t)` and checks the coefficient identities exactly with
SymPy. `tests/test_spectral_symbol_underdetermination.py` keeps the identities
in CI.

The semigroup identity follows directly because the constant scalar shift
commutes with `P0`; no numerical approximation is involved. A Lean
formalization of the abstract semigroup/heat-asymptotic implication is
`LEAN-PENDING`.

<!-- BILINGUAL-UNIT: spectral-underdetermination.status -->
## Status impact

**SPECTRAL ACTION FROM CLIFFORD PRINCIPAL SYMBOL ALONE: CLOSED AS NO-GO [L0].**

**SPECTRAL/GENERALIZED-DIRAC ACTION ROUTE: NARROWED, STILL OPEN.**

To close it, UBT must derive a complete operator and spectral prescription
whose lower-order data are fixed by the single fundamental structure rather
than chosen after the desired GR/gauge endpoint is known.
