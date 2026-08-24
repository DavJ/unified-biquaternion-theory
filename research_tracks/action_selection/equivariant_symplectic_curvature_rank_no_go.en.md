<!-- BILINGUAL-UNIT: equivariant-curvature-rank.provenance -->
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

# Equivariant symplectic curvature completion: exact rank boundary

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.setup -->
## Canonical equivariant completion

The invariant field-space symplectic form `omega` and the locally symplectic
spin+phase action define the standard quadratic moment map. For every Lie
algebra generator `T_r`, choose the convention

\[
\boxed{\mu_r(\Theta)=\frac12\omega(T_r\Theta,\Theta).}
\]

The symplectic-generator identity implies

\[
D\mu_r=\omega(T_r\Theta,D\Theta).
\]

With

\[
Q=\frac12\omega(D\Theta\wedge D\Theta),
\qquad
D^2\Theta=\mathcal F^rT_r\Theta,
\]

one obtains

\[
dQ=D\mu_r\wedge\mathcal F^r,
\]

where the contraction of adjoint/coadjoint indices is gauge invariant and the
Bianchi identity gives `D mathcal F=0`. Hence

\[
\boxed{\widehat Q:=Q-\mu_r\mathcal F^r,
\qquad d\widehat Q=0.}
\]

This is important: curvature can enter a UBT-native gauge-covariant exterior
form without inserting an Einstein--Hilbert scalar by hand.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.linear -->
## Linear curvature term

Consider the simplest scalar action built from this closed two-form,

\[
S_{\rm eq}=\frac12\int F(\Theta)\,\widehat Q\wedge\widehat Q,
\]

with invariant scalar `F`. Expanding by powers of curvature gives

\[
S_{\rm eq}
=\frac12\int FQ\wedge Q
-\int F\mu_rQ\wedge\mathcal F^r
+\frac12\int F\mu_r\mu_s\mathcal F^r\wedge\mathcal F^s.
\]

The coefficient of the term linear in Lorentz curvature is therefore

\[
\boxed{B_r^{\rm eq}=-F\mu_rQ.}
\]

For fixed `Theta` all six Lorentz-labelled two-forms are scalar multiples of
the **same** spacetime two-form `Q`. Consequently the map

\[
\mathfrak{so}(1,3)\longrightarrow\Lambda^2T^*M,
\qquad
T_r\longmapsto B_r^{\rm eq}
\]

has rank at most one.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.palatini -->
## Palatini requires rank six [L0]

For a nondegenerate tetrad, the Hilbert--Palatini curvature coefficient is

\[
\boxed{B_{ab}^{\rm HP}=\frac12\epsilon_{abcd}E^c\wedge E^d.}
\]

The coframe `E^a` identifies the six-dimensional internal bivector space with
the six-dimensional spacetime two-form space. Internal Hodge duality by
`epsilon_{abcd}` is invertible. Therefore

\[
\boxed{\operatorname{rank}(B^{\rm HP})=6}
\]

at every nondegenerate tetrad.

`tools/verify_equivariant_symplectic_curvature_rank.py` supplies an exact
finite certificate: at an integer tetrad with determinant `24`, the resulting
`6 x 6` Palatini bivector matrix has nonzero determinant and rank six, whereas
an arbitrary scalar outer-product coefficient `mu_r Q` has rank one.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.no-go -->
## Exact no-go for the simplest scalar completion [L1]

The rank mismatch is invariant under nonsingular changes of the Lorentz and
spacetime two-form bases. Thus on a nondegenerate tetrad branch

\[
\boxed{B_r^{\rm eq}\ne B_r^{\rm HP}}
\]

for the complete set of Lorentz curvature components. No choice of the scalar
function `F`, moment-map values `mu_r`, or nonzero two-form `Q` can raise the
rank-one factorization to rank six.

Therefore:

**THE SIMPLEST SCALAR EQUIVARIANT COMPLETION
`F (Q - <mu,Fcurv>)^2/2` CANNOT GENERATE THE HILBERT--PALATINI LINEAR
CURVATURE COUPLING ON A NONDEGENERATE FOUR-DIMENSIONAL TETRAD.**

This does not invalidate the equivariant construction. It identifies exactly
what is missing: a **Lie-algebra/bivector-valued two-form carrying six
independent curvature coefficients**, rather than one scalar spacetime
two-form multiplied by six moment-map numbers.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.next -->
## The next UBT-native object is already present

The canonical Lorentz tetrad has the antisymmetric biquaternionic companion

\[
\Sigma_{\mu\nu}
=\frac12(E_\mu^\sharp E_\nu-E_\nu^\sharp E_\mu),
\]

and the canonical Clifford lift provides the corresponding bivector algebra.
Unlike scalar `Q`, this object can carry a full six-dimensional Lorentz
bivector. The next curvature-origin test must therefore use the
**bivector-valued `E wedge E` / Clifford companion**, preferably in the already
established split-jet architecture separating the jet connection from the
physical Palatini connection.

The rank theorem does not yet establish a unique action or its normalization.
It tells us that the scalar symplectic route is too small and points to the
minimal representation content required for a viable curvature coupling.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.verification -->
## Verification

Exact executable check:

`tools/verify_equivariant_symplectic_curvature_rank.py`

It verifies the rank-six Palatini map at a nondegenerate exact tetrad and the
rank-one outer-product structure of the scalar equivariant coefficient.
The differential-form derivation of `d Qhat=0` is analytic. A Lean
formalization is `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: equivariant-curvature-rank.status -->
## Status

**CURVATURE ENTRY THROUGH THE EQUIVARIANT SYMPLECTIC FORM: AVAILABLE [L1].**

**SIMPLEST SCALAR EQUIVARIANT COMPLETION AS THE PALATINI ORIGIN:
CLOSED AS NO-GO [L1].**

**BIVECTOR/CLIFFORD CURVATURE ORIGIN AND NORMALIZATION: OPEN.**
