<!-- BILINGUAL-UNIT: single-theta-mm.provenance -->
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

# Single-Theta split-jet MacDowell--Mansouri closure candidate

<!-- BILINGUAL-UNIT: single-theta-mm.goal -->
## Goal

Two independent results in the action-selection track can now be combined:

- the split-jet auxiliary map can represent and vary all four tetrad directions
  without introducing an independent fundamental tetrad;
- the canonical fifth Clifford channel turns one graded extended-curvature
  square into Euler topology plus Hilbert--Palatini gravity plus a cosmological
  term with fixed relative coefficients.

This note records the combined candidate and its exact local classical
consequence. It does not promote the candidate to the locked UBT action.

<!-- BILINGUAL-UNIT: single-theta-mm.fields -->
## Field architecture

Let `X` be the existing Lorentz-real vector representative of the single
fundamental field `Theta`, and work on a patch with

\[
X^2\ne0.
\]

Use a physical Lorentz connection `omega` and algebraic split-jet variables
`K_J,w`. Define

\[
\boxed{
E^a=\frac1{\sqrt{N_0}}
\left(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a\right).}
\]

The auxiliary variables contain no derivatives. They are not independent
physical tetrad degrees of freedom; they parameterize the locally surjective
single-Theta jet representation. Physical curvature uses `omega`, not `K_J`.

Let the fifth canonical Clifford matrix satisfy

\[
\Gamma_\psi^2=\varepsilon_\psi I_4,
\qquad
\varepsilon_\psi=\pm1.
\]

Define the extended Clifford connection

\[
\boxed{
\mathcal A
=\frac14\omega^{ab}\Gamma_a\Gamma_b
+\frac1{2\ell}E^a\Gamma_a\Gamma_\psi.}
\]

<!-- BILINGUAL-UNIT: single-theta-mm.action -->
## One curvature-square candidate

With a dimensionless gravitational curvature coupling `g_G`, consider

\[
\boxed{
S_{\rm cand}[\Theta,\omega,K_J,w]
=-\frac{i\varepsilon_\psi}{g_G^2}
\int\operatorname{Tr}
\left(\Gamma_*\mathcal F\wedge\mathcal F\right),
\qquad
\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A.}
\]

There is no independently varied tetrad in this expression. The tetrad is the
composite split-jet object above. `omega`, `K_J`, and `w` are geometric or
auxiliary variational variables; this note does not assert that they are new
fundamental propagating fields.

The exact Clifford calculation gives

\[
\boxed{
\kappa=\frac{g_G^2\ell^2}{2},
\qquad
\Lambda=\frac{3\varepsilon_\psi}{\ell^2},
\qquad
\kappa\Lambda=\frac32\varepsilon_\psi g_G^2.}
\]

With these identifications the action is

\[
\boxed{
S_{\rm cand}
=S_{\rm HP}[E,\omega;\kappa,\Lambda]
-\frac{\varepsilon_\psi\ell^2}{8\kappa}
\int\epsilon_{abcd}R^{ab}\wedge R^{cd}.}
\]

The second term is Euler topology and does not change local bulk equations on
fixed topology.

<!-- BILINGUAL-UNIT: single-theta-mm.variation -->
## Local solution-set theorem [L1]

On every patch with `X^2 != 0`, the split-jet variation map

\[
(\delta K_J,\delta w)\longmapsto\delta E
\]

is pointwise surjective onto all tetrad directions. Therefore its transpose is
injective on the Palatini tetrad Euler form. Stationarity of `S_cand` with
respect to the split-jet auxiliaries gives the complete tetrad equation

\[
\boxed{\mathcal E_a^{\rm HP}=0.}
\]

The physical connection appears both in curvature and in the composite tetrad.
The latter chain-rule contribution is proportional to
`mathcal E_a^{HP}` and vanishes after the split-jet equation is imposed. The
remaining `omega` variation is the standard Palatini connection variation. In
spinless vacuum,

\[
\boxed{T^a=0,
\qquad
\omega=\mathring\omega(E).}
\]

The `Theta`/`X` variation is a differential consequence of the complete tetrad
equation because `X` enters the bulk gravitational action through the
composite `E`. Conversely every local Palatini solution can be lifted to the
split-jet variables by the explicit non-null right inverse.

Consequently, at fixed boundary/topology data, forgetting the representative
gives a local surjection. Writing `Crit` for stationary configurations,

\[
\boxed{
\mathcal P:\operatorname{Crit}(S_{\rm cand})
\twoheadrightarrow\operatorname{Crit}(S_{\rm HP}),\qquad
\mathcal P(X,\omega,K_J,w)=(E,\omega)}
\]

on the non-null split-jet patch. Quotienting only the stabilizer at fixed
`X` does not give a bijection: distinct field representatives can yield
the same coframe and physical connection. This is the same fibre distinction
proved in the [smooth continuation note](split_jet_null_continuation.en.md).

This is a local conditional equivalence theorem for the **chosen candidate**.
It is not a derivation of that candidate from the older locked kinetic action.

The [curvature-channel equivalence theorem](curvature_channel_dynamical_equivalence.en.md)
also shows that adding the ungraded extended curvature square with a constant
coefficient preserves all these local bulk Euler forms. Smooth compatible
regular nonzero-null crossings inherit the equation equivalence by continuity;
this does not establish arbitrary or global lifts.

<!-- BILINGUAL-UNIT: single-theta-mm.advance -->
## What has genuinely advanced

The remaining GR gap is no longer the conjunction of several unrelated
problems. Within one sharply specified candidate we now have:

- no independent tetrad field;
- a local rank-surjective single-Theta tetrad representation;
- the complete tetrad Einstein equation rather than a projected equation;
- an auxiliary physical connection reducing to Levi--Civita in vacuum;
- the Palatini tensor contraction generated by the canonical Clifford grading;
- the cosmological term generated by the same extended curvature;
- only two continuous candidate parameters, `g_G` and `ell`, replacing
  independent `kappa` and `Lambda`.

The form of the classical GR sector is therefore substantially less arbitrary
than in the earlier imported-Hilbert--Palatini branch.

<!-- BILINGUAL-UNIT: single-theta-mm.remaining -->
## The exact remaining fundamental questions

Unconditional UBT GR recovery still requires microscopic answers to the
following points:

1. **extended gauge principle:** derive why the canonical fifth Clifford
   channel belongs in the physical extended connection with coefficient
   `1/(2 ell)`;
2. **grading/symmetry reduction:** derive the `Gamma_*` insertion or equivalent
   Lorentz projection from the complex-time/fifth-channel dynamics rather than
   choosing it to reproduce the oriented Palatini channel;
3. **scale selection:** derive `ell`; identifying it with a `psi` radius is only
   a candidate until the physical meaning of the `psi` channel is fixed;
4. **overall coupling:** derive `g_G` or its relation to another independently
   derived UBT coupling; the existing `8 pi` notes do not fix this;
5. **global completion:** beyond the now controlled smooth compatible regular
   `X^2=0` crossings with nonzero field, treat zeros of the representative,
   other singular cases, topology/boundaries and global continuation;
6. **full sectors:** show that the same fundamental action also yields the
   required gauge, matter, quantum and physical `psi` dynamics without adding
   separate fundamental actions.

These are now selection/origin questions. The local classical variational
architecture itself is no longer the main obstruction for this candidate.

<!-- BILINGUAL-UNIT: single-theta-mm.falsification -->
## Sharp falsification conditions

This candidate should be rejected as a fundamental UBT completion if any of the
following occurs:

- no UBT-native derivation of the extended fifth-channel connection exists;
- the required grading insertion is incompatible with the locked complex-time
  symmetries;
- the `X^2=0` branch cannot be covered by a regular equivalent formulation;
- the derived `g_G,ell` predict a Newton/cosmological sector incompatible with
  observation;
- the same action cannot accommodate the non-gravitational sectors without
  adding independent fundamental terms.

Failure of the candidate would not invalidate the earlier kinematic UBT
results; it would rule out this particular action completion.

<!-- BILINGUAL-UNIT: single-theta-mm.verification -->
## Verification

The finite theorem-critical algebra is checked independently by:

- `tools/verify_split_jet_palatii_variational_lift.py` — rank-four split-jet
  variation and explicit right inverse;
- `tools/verify_clifford_palatini_trace_selector.py` — canonical graded trace
  and bivector invariant classification;
- `tools/verify_fifth_channel_macdowell_mansouri.py` — fifth-channel
  commutators, graded projection and exact coefficient matching.

The variational composition uses the already established Palatini/Cartan and
Euler-topology identities. Formalization of the full differential-form theorem
in Lean remains `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: single-theta-mm.status -->
## Status

**LOCAL SINGLE-THETA SPLIT-JET CURVATURE-SQUARE CANDIDATE WITH EINSTEIN--LAMBDA
SOLUTION-SET EQUIVALENCE: CLOSED CONDITIONALLY [L1].**

**PARAMETER RELATIONS WITHIN THE CANDIDATE:
`kappa=g_G^2 ell^2/2`, `Lambda=3 epsilon_psi/ell^2`: PROVED [L1].**

**MICROSCOPIC SELECTION OF THE EXTENDED CONNECTION, GRADING, `g_G` AND `ell`:
OPEN.**

**UNCONDITIONAL GR RECOVERY FROM THE PREVIOUSLY LOCKED UBT DYNAMICS:
NOT YET CLOSED.**
