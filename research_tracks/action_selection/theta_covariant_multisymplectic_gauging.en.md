<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.provenance -->
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

# Local gauge covariantization of the Theta multisymplectic family

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.scope -->
## Scope

The preceding note constructs the nondegenerate real field-space symplectic
form

\[
\omega(u,v)=\operatorname{Im}(u^\dagger Gv)
\]

from the unique quadratic invariant of the connected spin+phase action. This
note asks two sharper questions:

1. can the ordinary derivative in the first-order pullback family be replaced
   by a local covariant derivative without restoring second-jet equations?;
2. can the required connection be made a purely auxiliary variable while
   retaining a nondegenerate four-dimensional UBT tetrad?

The answers are respectively **yes** and, on the generic nondegenerate branch,
**no**.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.symplectic-connection -->
## The UBT connected generators are symplectic [L0]

Let `V` be the underlying eight-dimensional real field space and let
`rho_*` be the realified infinitesimal representation of the six
`SL(2,C)` spin generators together with the central phase generator. For every
generator `T`, exact matrix algebra gives

\[
\boxed{T^T\Omega+\Omega T=0.}
\]

Thus the connected representation lies in `Sp(V,omega)`. Equivalently, a local
connection `A` valued in this represented Lie algebra is a symplectic
connection:

\[
D\omega=0.
\]

The exact generator matrices and this condition are checked in
`tools/verify_theta_covariant_multisymplectic_gauging.py`.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.action -->
## Gauge-covariant first-order family with a fixed connection [L1]

Let

\[
D\Theta=d\Theta+\mathcal A\Theta
\]

in the represented real field space; the same statement applies after packing
a two-sided biquaternionic connection into its real linear representation.
Define the gauge-invariant spacetime two-form

\[
Q:=\frac12\,\omega(D\Theta\wedge D\Theta)
\]

and, for any invariant real scalar `F(Theta)`, define

\[
\boxed{S_F^{\rm cov}[\Theta;\mathcal A]
=\frac12\int_{M_4}F(\Theta)\,Q\wedge Q.}
\]

Under a local represented transformation `R(x)`,

\[
\Theta\mapsto R\Theta,
\qquad
\mathcal A\mapsto R\mathcal A R^{-1}-dR\,R^{-1},
\qquad
D\Theta\mapsto R D\Theta.
\]

Because `R` preserves `omega` and `F` is invariant, both `Q` and the action are
locally gauge invariant. The action is also diffeomorphism invariant because it
integrates a four-form and requires no background spacetime metric.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.first-order -->
## Covariant second-jet cancellation [L1]

Hold the connection fixed during the `Theta` variation and put

\[
\alpha:=\omega(\delta\Theta,D\Theta),
\qquad
\mathcal R\Theta:=D^2\Theta.
\]

Symplectic compatibility gives the exact identities

\[
\delta Q=d\alpha-\omega(\delta\Theta,\mathcal R\Theta),
\qquad
 dQ=\omega(\mathcal R\Theta,D\Theta).
\]

Therefore, modulo the boundary term `d(F alpha wedge Q)`,

\[
\begin{aligned}
\delta S_F^{\rm cov}
={}&\frac12\int \delta F\,Q\wedge Q
-\int dF\wedge\alpha\wedge Q\\
&+\int F\,\alpha\wedge dQ
-\int F\,\omega(\delta\Theta,\mathcal R\Theta)\wedge Q.
\end{aligned}
\]

No symmetric `D_mu D_nu Theta` principal term remains. The only second
covariant derivative appears through the curvature commutator
`D^2 Theta = mathcal R Theta`. For a connection that is independent of
`Theta` and its derivatives during this variation, the `Theta` Euler--Lagrange
equation is therefore genuinely first order in `Theta`.

This is the locally gauge-covariant analogue of the double-antisymmetric
first-jet Hessian criterion. This establishes that local gauging itself does **not**
destroy the first-order cancellation.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.auxiliary -->
## Purely auxiliary connection equation

The same action contains no derivative of `mathcal A`. If the connection is
varied independently in this sector, then

\[
\delta_{\mathcal A}D\Theta=(\delta\mathcal A)\Theta
\]

and the connection Euler--Lagrange equation is algebraic. For every represented
Lie generator `T_r` it is

\[
\boxed{
F\,\omega(T_r\Theta,D\Theta)\wedge Q=0.
}
\]

Thus a connection introduced only through this action is nonpropagating, but
its algebraic equation is a moment-map constraint rather than the desired UBT
connection-reconstruction theorem.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.no-go -->
## Generic auxiliary-gauging no-go for a nondegenerate tetrad [L1]

Assume at a point that

\[
F(\Theta)\ne0,
\qquad
Q\wedge Q\ne0.
\]

In four dimensions a two-form with `Q wedge Q != 0` is symplectic, and the map

\[
\Lambda^1T^*M\longrightarrow\Lambda^3T^*M,
\qquad
\beta\longmapsto\beta\wedge Q
\]

is an isomorphism. Hence the auxiliary connection equation implies

\[
\omega(T_r\Theta,D_\mu\Theta)=0
\quad\text{for every }r,\mu.
\]

Equivalently,

\[
\boxed{D_\mu\Theta\in(\mathfrak g\cdot\Theta)^\omega.}
\]

The exact invariant classification supplies two functionally independent
invariants `H` and `D=|det X|^2` on a generic stratum, so the group orbit has
real dimension at most six there. The exact rational witness

\[
z=(1+i,\;2+3i,\;4+5i,\;6+7i)
\]

has orbit rank exactly six. A nonzero `6 x 6` minor and independence of `dH`
and `dD` therefore certify a nonempty open stratum with

\[
\dim(\mathfrak g\cdot\Theta)=6.
\]

Because `omega` is nondegenerate on the eight-dimensional field space,

\[
\boxed{\dim(\mathfrak g\cdot\Theta)^\omega=8-6=2.}
\]

Thus all four covariant derivatives `D_mu Theta` lie in the same at-most
two-dimensional field-space subspace. On the classical Lorentz slice,

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L,
\]

so the four tetrad vectors span at most two dimensions. Consequently

\[
\boxed{\operatorname{rank}e\le2,\qquad\det e=0.}
\]

A nondegenerate Lorentzian metric is impossible on this generic
`F != 0`, `Q wedge Q != 0` branch.

Therefore:

**THE COVARIANT MULTISYMPLECTIC ACTION WITH THE FULL SPIN+PHASE CONNECTION
VARIED AS A PURELY AUXILIARY VARIABLE CANNOT SUPPORT THE GENERIC
NONDEGENERATE UBT TETRAD.**

This is a no-go for the pure auxiliary implementation of this particular
connection sector, not for every connection completion of UBT.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.fork -->
## Consequence: the connection fork is now sharp

The results leave three logically distinct routes:

1. **Fixed/external symplectic connection:** local gauge invariance and
   first-order `Theta` equations are exact, but this is not acceptable as the
   final single-field UBT dynamics because the geometry would be supplied
   externally.
2. **Pure auxiliary full spin+phase connection:** the connection does not
   propagate, but its moment-map equation collapses the generic tetrad rank and
   is excluded by the theorem above.
3. **Composite or enlarged connection dynamics:** the physical UBT connection
   must instead be reconstructed from `Theta`/tetrad/torsion or supplied with
   additional action structure whose connection equation is not the pure
   moment-map constraint. Eliminating a Levi--Civita-type composite connection
   generally introduces derivatives of the tetrad and hence higher jets of
   `Theta`; the first-order theorem above cannot simply be reused after that
   substitution.

This sharply moves the action-selection problem. The next viable target is a
**Theta-only higher-jet/composite completion, or a connection action whose
extra structure is itself derived from UBT and whose elimination reproduces
the canonical connection without rank collapse**.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.verification -->
## Verification

`tools/verify_theta_covariant_multisymplectic_gauging.py` checks exactly:

- pseudo-unitary preservation of the Hermitian form by all seven connected
  spin+phase generators;
- symplectic preservation `T^T Omega + Omega T = 0`;
- functional independence of `H` and `|det X|^2` at the exact witness;
- exact generic-stratum orbit rank six;
- exact rank six of the moment-map constraint matrix and its two-dimensional
  nullspace.

The exterior-calculus statements, the four-dimensional wedge isomorphism and
the covariant variation are analytic. Lean formalization is `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.status -->
## Status

**LOCAL GAUGE COVARIANTIZATION WITH FIXED SYMPLECTIC CONNECTION:
PROVED [L1].**

**PURE AUXILIARY FULL SPIN+PHASE GAUGING ON THE GENERIC NONDEGENERATE BRANCH:
CLOSED AS NO-GO [L1].**

**COMPOSITE/HIGHER-JET CONNECTION COMPLETION AND UNCONDITIONAL GR:
OPEN.**
