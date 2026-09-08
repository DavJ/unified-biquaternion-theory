<!-- BILINGUAL-UNIT: null-jet.header -->
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


# Smooth continuation of the existing split jet through a null field

**Date:** 2026-09-08. **Status:** ANALYTIC PROOF [L1]; LEAN-PENDING.
**Scope:** research mathematics within the existing split-jet architecture.
This is a local compatibility theorem for prescribed smooth data, not a
derivation of the gravitational action or a global existence theorem.

<!-- BILINGUAL-UNIT: null-jet.setup -->
## 1. Data, conventions and the precise question

Work on a smooth four-dimensional patch with a prescribed smooth nondegenerate
tetrad, its central metric and physical Levi-Civita connection. All fields in
this note are smooth. Use the existing Lorentz-real vector representative of
the single field; no alternative metric readout is introduced:

\[
\eta=\operatorname{diag}(-1,1,1,1),\quad
X=X^a\mathbf u_a\in W_L,\quad X\ne0,\quad
c_0=\sqrt{\mathcal N_0}>0,\quad
g_{\mu\nu}=e_\mu{}^a e_\nu{}^b\eta_{ab}.
\]

All contractions below use the Lorentz form. The jet correction acts in the
vector representation of the existing Lorentz spin lift:

\[
\widehat D_\mu X^a=\mathring D_\mu X^a
  +K_\mu{}^a{}_bX^b+w_\mu X^a,
\qquad K_{\mu ab}=-K_{\mu ba}.
\]

In biquaternion notation the multiplication sides remain

\[
A^J_\mu=\mathring\Omega_\mu+\mathcal K_\mu+\tfrac12w_\mu\mathbf1,
\quad B^J_\mu=-\mathring\Omega_\mu^\ddagger-\mathcal K_\mu^\ddagger
 -\tfrac12w_\mu\mathbf1,
\quad \widehat D_\mu X=\partial_\mu X+A^J_\mu X-XB^J_\mu.
\]

Here \(\mathcal K\) is the spin lift of \(K\). Physical curvature still uses
only the Levi-Civita connection. Define the norm, mismatch and contraction:

\[
\chi=X\cdot X,\qquad
Z_\mu{}^a=c_0e_\mu{}^a-\mathring D_\mu X^a,\qquad
r_\mu=X\cdot Z_\mu.
\]

The question is whether smooth finite jet coefficients solve

\[
K_\mu X+w_\mu X=Z_\mu
\]

through \(\chi=0\). The non-null formula in
`../../canonical/gr_closure/gap_10t_split_jet_right_inverse.tex`
divides by \(\chi\). A singularity of that particular representative alone
does not establish a singularity of every representative.

<!-- BILINGUAL-UNIT: null-jet.divisibility -->
## 2. Exact smooth divisibility criterion

**Theorem N1 [L1].** Near any point with \(X\ne0\), a smooth pair
\((K,w)\) exists if and only if each \(r_\mu\) is smoothly divisible by
\(\chi\):

\[
\exists\,w_\mu\in C^\infty:\qquad r_\mu=\chi w_\mu.
\]

**Proof.** Lorentz antisymmetry gives \(X\cdot K_\mu X=0\), so contraction
of the required equation gives the necessary divisibility condition.
Conversely choose a smooth local vector \(Y\) with \(X\cdot Y=1\). Such a
choice exists near every nonzero vector by nondegeneracy of the Lorentz form;
one nonvanishing local component suffices. Put

\[
U_\mu=Z_\mu-w_\mu X,\qquad
K_\mu{}^a{}_b=U_\mu{}^aY_b-Y^aU_{\mu b}.
\]

Then

\[
X\cdot U_\mu=r_\mu-w_\mu\chi=0,\qquad
K_\mu X=U_\mu(X\cdot Y)-Y(X\cdot U_\mu)=U_\mu.
\]

The tensor is Lorentz antisymmetric and smooth, and the required equation
follows. This proves both directions. No division by \(\chi\) occurs in this
representative once a smooth quotient \(w\) is available. Different choices
of \(Y\), at fixed \(w\), differ by a stabilizer tensor annihilating \(X\).
The vector \(Y\) is a choice in a proof, not a new fundamental or propagating
field; no preferred choice is asserted to follow from the action.

<!-- BILINGUAL-UNIT: null-jet.crossing -->
## 3. Regular null crossings and the tetrad compatibility condition

**Corollary N2 [L1].** Suppose \(\Sigma=\{\chi=0\}\) is a regular
hypersurface, meaning \(d\chi\ne0\) there. Smooth continuation exists
locally if and only if

\[
r_\mu|_\Sigma=0\quad(\forall\mu).
\]

**Proof.** Use \(\chi\) as a local coordinate. A smooth function vanishing
on its zero hypersurface has the local factorization

\[
r_\mu(\chi,y)=\chi\int_0^1
  (\partial_\chi r_\mu)(t\chi,y)\,dt.
\]

This supplies the smooth quotient in N1. Necessity follows by restriction.
Vanishing only at one point is insufficient: the condition holds along the
local hypersurface.

Metric compatibility gives a useful expression independent of connection
components:

\[
r_\mu=c_0X_a e_\mu{}^a-\tfrac12\partial_\mu\chi.
\]

Consequently every smooth solution at a nonzero null field obeys

\[
(\partial_\mu\chi)|_\Sigma=2c_0X_a e_\mu{}^a|_\Sigma,
\qquad
g^{\mu\nu}\partial_\mu\chi\,\partial_\nu\chi|_\Sigma=0.
\]

Since the tetrad is invertible and \(X\ne0\), the first covector is nonzero.
Thus a compatible nonzero null point necessarily lies on a regular null
hypersurface. An open region with \(X\ne0\) and \(X^2\equiv0\) cannot
satisfy the full jet relation with a nondegenerate tetrad. This is a restriction
on the existing Lorentz-plus-dilation jet, not a no-go theorem for UBT as a
whole. A surface where the field norm vanishes is not automatically a black
hole horizon.

<!-- BILINGUAL-UNIT: null-jet.rank -->
## 4. Rank and auxiliary variation at the crossing

**Proposition N3 [L1].** For a fixed vector define

\[
L_X:\mathfrak{so}(1,3)\oplus\mathbb R\longrightarrow\mathbb R^{1,3},
\qquad L_X(K,w)=KX+wX.
\]

Its rank is

| Field | Image | Rank |
|---|---|---|
| \(X^2\ne0\) | \(\mathbb R^{1,3}\) | 4 |
| \(X^2=0,\ X\ne0\) | \(X^\perp\) | 3 |
| \(X=0\) | \(\{0\}\) | 0 |

**Proof.** The non-null result is the existing right inverse. For nonzero null
\(X\), contraction places the image in \(X^\perp\). For every target in
that hyperplane, the construction in N1 with \(w=0\) reaches the target.
The zero-vector case is immediate.

The algebraic multiplier equations from the existing auxiliary action are

\[
\lambda_a{}^\mu X^a=0,\qquad
\lambda^{\mu[a}X^{b]}=0.
\]

At a nonzero null point alone they allow
\(\lambda_a{}^\mu=b^\mu X_a\); the usual pointwise argument forcing the
multiplier to vanish loses one condition. Nevertheless, across a regular
hypersurface any continuous multiplier vanishes there too if it solves these
equations nearby: it vanishes on the dense non-null complement and hence by
continuity on the hypersurface. For a smooth solution it is identically zero
on the neighbourhood, so its derivatives also vanish. Thus the existing
auxiliary decoupling argument extends to these smooth compatible crossings.
This does not cover distributional sources, singular fields, a quantum
constraint measure. The next theorem treats full Palatini variation across a
smooth hypersurface; it does not argue from a null point in isolation.

<!-- BILINGUAL-UNIT: null-jet.palatini -->
## 5. Conditional Palatini dynamics through the crossing

**Theorem N4 [L1].** In the existing split-jet Palatini candidate let the fields
be smooth, the composite tetrad nondegenerate, the field nowhere zero, and the
null-norm set a regular hypersurface or empty. Take a nonzero Palatini coupling
and a fixed cosmological coefficient. Require that the action depend on the
field and jet variables only through the composite tetrad:

\[
E^a=c_0^{-1}(dX^a+\omega^a{}_bX^b+K^a{}_bX^b+wX^a),\qquad
S_{\rm SJHP}=S_{\rm HP}[E,\omega].
\]

The physical Lorentz connection is independent during variation. All variations
have compact support. Stationarity is then equivalent to the Palatini equations
evaluated on the composite tetrad, including on the null hypersurface.

**Proof.** Write the tetrad and connection Euler forms as

\[
\delta S_{\rm HP}=\int\mathcal E_a\wedge\delta E^a
 +\int\mathcal C_{ab}\wedge\delta\omega^{ab}.
\]

Away from the null set, N3 and arbitrary jet variations force
\(\mathcal E_a=0\). This complement is dense, so continuity of the Euler
forms forces the same equation on the hypersurface. The physical-connection
variation is

\[
\delta_\omega S_{\rm SJHP}=\int\mathcal C_{ab}\wedge\delta\omega^{ab}
 +c_0^{-1}\int\mathcal E_a\wedge(\delta\omega^a{}_bX^b).
\]

It gives \(\mathcal C_{ab}=0\) everywhere. Field variation is a differential
consequence of the identically vanishing tetrad Euler form. Conversely, if
both Palatini Euler forms vanish, the chain rule makes every composite
variation stationary, without using pointwise jet rank on the null surface.
This proves equivalence of equations at a given smooth configuration, not
existence of that configuration.

For a prescribed smooth vacuum Palatini solution and a nowhere-zero field
satisfying N2, N1 constructs a smooth lift across the null hypersurface.
The usual spinless vacuum Cartan equation gives the physical Levi-Civita
connection. Conditional local GR recovery therefore extends across these
compatible smooth crossings. The Palatini action and its coefficients are
still inputs, not derived microscopic UBT dynamics.

<!-- BILINGUAL-UNIT: null-jet.fibres -->
### 5.1 Equation equivalence does not identify all representatives

Forgetting the field representative and jet variables gives a surjection onto
admissible Palatini solutions. Quotienting only by the jet tensor's stabilizer
does not make it injective, since that stabilizer does not change the field.
For the flat standard tetrad, zero physical connection, \(c_0=1\) and zero
cosmological term, both constant fields

\[
X=(1,0,0,0),\qquad \widetilde X=(2,0,0,0)
\]

have non-null right inverses and produce the same vacuum Palatini solution.
They cannot be related by changing only a tensor annihilating a fixed field.
A bijection would require quotienting the entire representation fibre; no
physical gauge interpretation of that whole fibre is established here.
The earlier diagram in `split_jet_palatii_variational_lift.en.md` is corrected
to a surjective solution map.

<!-- BILINGUAL-UNIT: null-jet.examples -->
## 6. Exact examples and limits

For the flat standard tetrad take \(c_0=1\) and \(X^a=x^a\). Then
\(Z=0\) and \(K=w=0\) everywhere. The field norm crosses the null cone
regularly away from its vertex; the coefficients remain smooth. The vertex
has \(X=0\) and falls outside N1, although this particular affine example
also extends there.

For a flat standard tetrad and the constant null vector
\(X=(1,1,0,0)\), the mismatch is \(Z_\mu=e_\mu\), and
\(r_0=-1\) at \(c_0=1\). Smooth jet coefficients cannot solve the full
relation. Therefore arbitrary prescribed null representatives are not
universally admissible.

The regularity hypothesis in the abstract divisibility corollary matters.
The smooth algebraic data

\[
X(v)=(1,1,v,0),\qquad Z(v)=(0,0,1,0),\qquad
\chi(v)=v^2,\quad r(v)=v
\]

satisfy pointwise compatibility at \(v=0\), but the necessary quotient is
\(w=1/v\) away from zero. There is no smooth solution through zero. This
is an algebraic example for one mismatch slot, not an asserted solution of
the full field equations.

<!-- BILINGUAL-UNIT: null-jet.verification -->
## 7. Verification and remaining work

Run `python tools/verify_null_and_spectral_gap_steps.py`. The recorded result is
`../../reports/null_and_spectral_gap_steps_2026_09_08.json`.
SymPy checks exact tensor identities, ranks and the divisibility counterexample.
An independent NumPy implementation solves the full linear system near and on
the null cone. The record gives versions, tolerances, scope and limitations.

**LEAN-PENDING:** the inspected runtime has neither Lean nor Lake installed;
no compiled formal proof is claimed. The smooth factorization, spectral and
continuity arguments are analytic proofs, not consequences of the finite tests.
Provenance remains `C_working`; no author attestation or canonical tier changes.

This narrows the null-continuation portion of `UBT-FUND-GLOBAL: OPEN` by giving
an exact local criterion. `UBT-FUND-GR-ACTION: OPEN` and
`UBT-UV-G-PREDICTION: OPEN` remain. Deriving compatible data from the microscopic
action, continuation at zeros of the field, global topology, uniqueness and
quantum measure remain separate problems. The canonical status surfaces are
unchanged; this research result does not close a fundamental GR gap.

Related work within the repository:
`../../canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`,
`split_jet_palatii_variational_lift.en.md`, and
`../complex_time_branch_selection/bounded_selector_domain_completion.en.md`.
