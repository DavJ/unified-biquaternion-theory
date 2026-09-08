<!-- BILINGUAL-UNIT: curvature-equivalence.provenance -->
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

# Curvature-channel ambiguity and the exact classical GR target

<!-- BILINGUAL-UNIT: curvature-equivalence.scope -->
## Scope

The existing Clifford audit classifies two Lorentz-invariant curvature
channels. It is necessary to distinguish uniqueness of an action from
equivalence of its local classical equations. This note proves the relevant
equivalence within two specified families, including their failure cases.
It does not select either family as the fundamental UBT action.

The classical Palatini--Holst mechanism is standard, as in
[Sören Holst's generalized Hilbert--Palatini action](https://arxiv.org/abs/gr-qc/9511026).
The extended-connection context is the standard MacDowell--Mansouri
construction; see [Derek Wise's Cartan-geometric treatment](https://arxiv.org/abs/gr-qc/0611154).
No novelty is claimed for these gravity constructions. The application here
is to the precise remaining selection requirements in the canonical UBT
Clifford and split-jet candidates.

Work locally on an oriented smooth four-dimensional patch with a
nondegenerate real coframe \(E^a\), Lorentz metric
\(\eta=\operatorname{diag}(-1,1,1,1)\), and physical Lorentz connection
\(\omega^{ab}=-\omega^{ba}\). All fields are smooth; variations have compact
support. Initially the coframe and connection are independent.

\[
R^{ab}=d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb},\qquad
T^a=dE^a+\omega^a{}_b\wedge E^b,\qquad
\Sigma_{ab}=E_a\wedge E_b.
\]

The internal dual acts on Lorentz indices, not on spacetime form degree:

\[
(\star Y)_{ab}=\frac12\epsilon_{ab}{}^{cd}Y_{cd},\qquad
\epsilon_{0123}=1,\qquad \star^2=-I.
\]

<!-- BILINGUAL-UNIT: curvature-equivalence.holst -->
## H1 — A whole real Palatini--Holst family gives vacuum GR [L1]

For constant real coefficients consider

\[
S_{u,v,\lambda}
=\frac u4\int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}
 +\frac v2\int E^a\wedge E^b\wedge R_{ab}
 -\frac{\lambda}{24}\int\epsilon_{abcd}
 E^a\wedge E^b\wedge E^c\wedge E^d.
\]

**Theorem.** For this action alone in vacuum, with \(u\ne0\), the equations
are exactly

\[
\boxed{T^a=0,\qquad
G_{\mu\nu}+\frac{\lambda}{u}g_{\mu\nu}=0.}
\]

Every constant real \(v\) gives the same local vacuum equations at fixed
\(u,\lambda\). No matter source or additional action sector is included.

**Proof: connection equation.** Vary the curvature before eliminating the
connection, use \(\delta R=D_\omega\delta\omega\), and integrate by parts.
The equation is

\[
\mathcal P_{u,v}D_\omega\Sigma=0,\qquad
\mathcal P_{u,v}=u\star+vI.
\]

The Lorentz-signature identity gives

\[
\det\mathcal P_{u,v}=(u^2+v^2)^3,\qquad
\mathcal P_{u,v}^{-1}
=\frac{vI-u\star}{u^2+v^2}.
\]

Thus \(D_\omega\Sigma=0\). The map
\(T^a\mapsto T^a\wedge E^b-E^a\wedge T^b\) is injective for a
nondegenerate coframe. One direct proof uses its dual frame \(\iota_a\).
Set \(\zeta=\sum_a\iota_aT^a\). Contracting
\(E^a\wedge T^b-E^b\wedge T^a=0\) and summing over the second index gives
\(T^a=-E^a\wedge\zeta\). Contracting once more gives
\(\zeta=-3\zeta\), hence \(\zeta=0\) and \(T^a=0\).
Consequently the physical connection is the Levi-Civita connection.

**Proof: coframe equation.** Independent coframe variation gives

\[
\frac u2\epsilon_{abcd}E^b\wedge R^{cd}
 +vE^b\wedge R_{ab}
 -\frac{\lambda}{6}\epsilon_{abcd}E^b\wedge E^c\wedge E^d=0.
\]

After the connection equation has been imposed, the first Bianchi identity
\(D_\omega T^a=R^a{}_b\wedge E^b\) annihilates the Holst term.
The remaining equation is the displayed Einstein equation. Conversely,
a torsion-free Einstein solution satisfies both original variational
equations. This argument varies first; it does not erase the Holst term
by substituting a torsion-free connection into the action beforehand.

Within this specified family the identifications are

\[
\kappa=\frac1u,\qquad \Lambda=\frac{\lambda}{u}.
\]

The theorem does not determine these constants or the physical sign of \(u\).

<!-- BILINGUAL-UNIT: curvature-equivalence.limits -->
## H2 — Exact boundaries of the equivalence

**Pure Holst.** If \(u=0\), \(v\ne0\) and \(\lambda=0\), the connection
equation still enforces zero torsion, but the coframe equation is then only
the Bianchi identity. Every torsion-free coframe satisfies it, including
noneinsteinian metrics. If instead \(\lambda\ne0\), its volume equation
has no nondegenerate coframe solution. A nonzero Palatini component is essential.

**Complex coefficients.** For \(v=\pm iu\ne0\), the complex bivector map
has rank three and the displayed inverse does not exist. Chiral formulations
require their own variables and reality conditions; this theorem does not
exclude them.

**Spin current.** Define a specified current by

\[
\delta_\omega S_{\rm m}=\frac12\int\tau_{ab}\wedge\delta\omega^{ab}.
\]

The connection equation becomes

\[
\mathcal P_{u,v}D_\omega\Sigma=\tau,\qquad
D_\omega\Sigma=\frac{vI-u\star}{u^2+v^2}\tau.
\]

For a nonzero current the torsion response generally depends on \(v\).
The vacuum theorem cannot fix the matter coupling or the physical mode quotient.

**Variable coefficient.** If \(u\ne0\) is constant but \(v=v(x)\), then

\[
(u\star+vI)D_\omega\Sigma+dv\wedge\Sigma=0.
\]

On a torsion-free nondegenerate branch this requires \(dv=0\): a one-form
whose wedge with every coframe two-form vanishes must itself vanish.
Thus an arbitrary field-dependent Holst coefficient is not covered by H1.

<!-- BILINGUAL-UNIT: curvature-equivalence.commutant -->
## C1 — Constant Lorentz-scalar Clifford insertions [L0]

Use the canonical matrices \(\Gamma_a,\Gamma_*\) and
\(\mathcal J_{ab}=\Gamma_a\Gamma_b/2\) for distinct indices.
The Clifford, grading and trace conventions are

\[
\{\Gamma_a,\Gamma_b\}=2\eta_{ab}I_4,\qquad
\Gamma_*^2=I_4,\qquad \{\Gamma_*,\Gamma_a\}=0,\qquad
\operatorname{Tr}(\Gamma_*\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
=-4i\epsilon_{abcd}.
\]

The fifth matrix is fixed as

\[
\Gamma_\psi=
\begin{cases}
\Gamma_* & \varepsilon_\psi=+1,\\
i\Gamma_* & \varepsilon_\psi=-1.
\end{cases}
\]

For a constant complex matrix \(Z\), the exact commutant is

\[
[Z,\mathcal J_{ab}]=0\quad(\forall a<b)
\quad\Longleftrightarrow\quad
Z=z_0I_4+z_*\Gamma_*.
\]

In the canonical block basis, commuting with the three rotations makes each
of the four matrix blocks a scalar multiple of the identity. Commuting with
the three boosts forces the off-diagonal blocks to zero. The remaining two
scalar diagonal blocks are precisely the stated span. The verifier also
solves the full matrix system without imposing a block ansatz.

For either fifth-channel sign, adding all translation generators
\(P_a=\Gamma_a\Gamma_\psi/2\) to the commuting conditions forces
\(z_*=0\). Hence the commutant of the full extended representation contains
only scalar matrices.

This classifies constant insertions that are themselves symmetry scalars.
It is not a classification of all possible field-dependent actions.

<!-- BILINGUAL-UNIT: curvature-equivalence.topology -->
## C2 — The ungraded extended curvature square is locally inert [L1]

Keep the already proposed extended connection, with constant
\(\ell>0\) and \(\varepsilon_\psi=\pm1\):

\[
\mathcal A=\frac14\omega^{ab}\Gamma_a\Gamma_b
 +\frac1{2\ell}E^a\Gamma_a\Gamma_\psi,\qquad
\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A.
\]

The existing curvature decomposition and the ungraded Clifford traces give

\[
\boxed{
\operatorname{Tr}(\mathcal F\wedge\mathcal F)
=-\frac12R^{ab}\wedge R_{ab}
 +\frac{\varepsilon_\psi}{\ell^2}
 \left(E^a\wedge E^b\wedge R_{ab}-T^a\wedge T_a\right).}
\]

The Lorentz/translation mixed trace vanishes. The contracted four-coframe
term vanishes because it repeats one-forms. The translation-square trace
supplies the displayed torsion-square coefficient. These statements hold
before imposing zero torsion.

The identity

\[
d(E^a\wedge T_a)
=T^a\wedge T_a-E^a\wedge E^b\wedge R_{ab}
\]

follows from the first Bianchi identity. Thus the ungraded density is
Lorentz Pontryagin density plus a Nieh--Yan boundary term.
Equivalently, the full extended Bianchi identity gives

\[
\boxed{
\delta\operatorname{Tr}(\mathcal F\wedge\mathcal F)
=2\,d\operatorname{Tr}(\delta\mathcal A\wedge\mathcal F).}
\]

Its integral with a constant coefficient has zero local bulk variation,
also when the extended connection is a smooth composite of the varied fields.
This includes the complete induced variation of the coframe and connection.
Global topology, boundary observables and quantum phases can still depend
on that coefficient.

For a prescribed nonconstant coefficient \(c(x)\), compactly supported
connection variation instead gives

\[
\delta\int c\,\operatorname{Tr}(\mathcal F\wedge\mathcal F)
=-2\int dc\wedge
\operatorname{Tr}(\delta\mathcal A\wedge\mathcal F).
\]

A dynamical coefficient also contributes its own variation. The constant
coefficient assumption must not be silently dropped.

<!-- BILINGUAL-UNIT: curvature-equivalence.extended -->
## C3 — What the graded channel must actually supply [L1]

For constant real coefficients consider the full two-insertion family

\[
S_{c_g,c_t}=\int
\left[
c_g\,i\operatorname{Tr}(\Gamma_*\mathcal F\wedge\mathcal F)
+c_t\,\operatorname{Tr}(\mathcal F\wedge\mathcal F)
\right].
\]

C2 removes the second term from the local bulk equations. Expansion of the
first, including its Euler density, identifies

\[
u=-\frac{2\varepsilon_\psi c_g}{\ell^2},\qquad
\lambda=-\frac{6c_g}{\ell^4},\qquad
\kappa=-\frac{\ell^2}{2\varepsilon_\psi c_g},\qquad
\Lambda=\frac{3\varepsilon_\psi}{\ell^2}
\quad(c_g\ne0).
\]

Every constant \(c_t\) gives exactly the same bulk Euler forms at fixed
\(c_g,\ell,\varepsilon_\psi\), including away from zero torsion.
If \(c_g=0\), the whole action is locally topological and supplies no
Einstein-selection equation.

Therefore local classical GR does not require proving that the ungraded
coefficient is absent. It requires a nonzero graded coefficient and the
already stated variational assumptions. Full extended symmetry acting on
constant scalar insertions permits only the locally topological direction
by C1. A UBT origin for the required symmetry reduction remains essential.
The existence of \(\Gamma_*\) alone does not force its coefficient to be
nonzero.

This conclusion narrows the selection target. It fixes neither the length
scale nor the Newton coupling and does not authorize a new fundamental action.

<!-- BILINGUAL-UNIT: curvature-equivalence.splitjet -->
## Application to the existing single-field split jet

Use the existing Lorentz-real representative \(X\) and the existing
two-sided spin representation, with Lorentz jet correction \(K\) and
central relative correction \(w\):

\[
E^a=c_0^{-1}
\left(dX^a+\omega^a{}_bX^b+K^a{}_bX^b+wX^a\right),\qquad
c_0=\sqrt{\mathcal N_0},\qquad K_{ab}=-K_{ba}.
\]

In matrix notation the multiplication sides are explicitly

\[
\widehat D X=dX+A^JX-XB^J,\qquad
A^J=\Omega+\mathcal K+\tfrac12wI_2,\qquad
B^J=-\Omega^\dagger-\mathcal K^\dagger-\tfrac12wI_2.
\]

Here \(\Omega\) and \(\mathcal K\) are the established spin lifts of
\(\omega\) and \(K\).

The independent variational variables are \(X,\omega,K,w\); physical curvature
uses \(\omega\). Suppose \(X\ne0\), the coframe is nondegenerate, and the
null-norm set is a regular hypersurface or empty. Require that these action
sectors have no additional explicit dependence on the representative or
jet variables outside the displayed coframe.

On the non-null complement, variation of the jet variables reaches every
coframe direction. Their equations therefore imply the complete coframe
Euler form. Smoothness extends its vanishing across a compatible null
hypersurface. The induced coframe part of the physical connection variation
then vanishes, leaving the full independent connection equation. The
representative equation follows as well. The converse follows by the chain
rule. This is the same precise argument as
[the smooth Palatini continuation theorem](split_jet_null_continuation.en.md).

Thus H1 and C3 carry over to this chosen split-jet action on these patches.
For C3, the constant topological terms do not alter the argument. Local lifts
of Einstein configurations are available on sufficiently small non-null
patches by the established right inverse. Lifts through a prescribed null
crossing still require its smooth compatibility condition.

The map forgetting jet representatives is surjective locally, but is not a
bijection modulo only the stabilizer at fixed \(X\). Distinct representatives
of the same coframe remain possible. No global lift or full quantum
equivalence is asserted.

<!-- BILINGUAL-UNIT: curvature-equivalence.verification -->
## Verification and remaining gap

Run `tools/verify_curvature_channel_equivalence.py`; the record is
`reports/curvature_channel_equivalence_2026_09_08.json`.
Its nine groups cover the exact bivector inverse; the full torsion-map
determinant; the variable-coefficient obstruction; Bianchi cancellation;
the Lorentz and extended commutants; all graded and ungraded trace blocks;
coefficient matching; independent coordinate-curvature calculations in a
different Dirac representation; and independent sourced-torsion solves.
SymPy and NumPy versions, source hashes and scopes are recorded.

The smooth variational, transgression and continuation arguments are analytic.
They are not proved by finite sampling. Formal status is `LEAN-PENDING`:
Lean and Lake are absent in the inspected runtime and no compiled
formalization is supplied.

**CONSTANT REAL PALATINI--HOLST VACUUM EQUIVALENCE: PROVED [L1].**

**CONSTANT UNGRADED EXTENDED TRACE: ZERO LOCAL BULK VARIATION [L1].**

**UBT ORIGIN OF THE NONZERO GRAVITATIONAL CHANNEL, NORMALIZATION,
FULL SECTORS AND RH: OPEN.**

The canonical claim ledger is unchanged. A unique fundamental action can
still require coefficient selection even where the classical bulk equations
cannot distinguish those coefficients.
