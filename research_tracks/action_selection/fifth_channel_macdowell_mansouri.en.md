<!-- BILINGUAL-UNIT: fifth-channel-mm.provenance -->
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

# Fifth-channel Clifford curvature-square candidate for the GR action

<!-- BILINGUAL-UNIT: fifth-channel-mm.scope -->
## Scope

The canonical UBT Clifford lift already contains four Lorentz generators
`Gamma_a` and an anticommuting fifth channel. Write

\[
\Gamma_\psi^2=\varepsilon_\psi I_4,
\qquad
\varepsilon_\psi=\pm1,
\qquad
\{\Gamma_\psi,\Gamma_a\}=0.
\]

The existing construction allows `Gamma_psi=Gamma_*` for
`epsilon_psi=+1` or `Gamma_psi=i Gamma_*` for `epsilon_psi=-1`. This note asks
whether the Palatini curvature term can arise from **one extended Clifford
curvature** rather than being inserted as an independent term.

The mechanism below is the standard MacDowell--Mansouri algebraic mechanism.
No novelty is claimed for that standard gravity construction. The UBT-specific
observation is that the required fifth Clifford generator is already present in
the canonical single-Theta architecture, so the construction can be tested
without adding a new Clifford carrier.

<!-- BILINGUAL-UNIT: fifth-channel-mm.connection -->
## Extended Clifford connection

Let

\[
J_{ab}:=\frac12\Gamma_a\Gamma_b
\qquad(a\ne b),
\qquad
P_a:=\frac12\Gamma_a\Gamma_\psi.
\]

Exact Clifford algebra gives

\[
\boxed{[P_a,P_b]=-\varepsilon_\psi J_{ab}.}
\]

For a real length scale `ell`, define the candidate extended connection

\[
\boxed{
\mathcal A
=\frac12\omega^{ab}J_{ab}
+\frac1\ell E^aP_a
=\frac14\omega^{ab}\Gamma_a\Gamma_b
+\frac1{2\ell}E^a\Gamma_a\Gamma_\psi.}
\]

Here `omega` is the physical Lorentz connection and `E^a` is the same canonical
UBT tetrad. In a strict single-Theta implementation `E^a` may be the split-jet
composite tetrad already studied in this PR; it is not a new fundamental field.

This definition is a **candidate dynamical architecture**. The locked UBT
axioms do not currently state that the physical gauge connection enlarges to
this de Sitter/anti-de Sitter-type Clifford connection.

<!-- BILINGUAL-UNIT: fifth-channel-mm.curvature -->
## Exact curvature decomposition [L0]

The curvature

\[
\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A
\]

has Lorentz and translation parts

\[
\boxed{
\mathcal F
=\frac14\left(
R^{ab}(\omega)-\frac{\varepsilon_\psi}{\ell^2}E^a\wedge E^b
\right)\Gamma_a\Gamma_b
+\frac1{2\ell}T^a\Gamma_a\Gamma_\psi,}
\]

where

\[
T^a=dE^a+\omega^a{}_b\wedge E^b.
\]

The relative coefficient of `E wedge E` is therefore fixed by the fifth-channel
Clifford commutator once the normalization `1/ell` of the translation generator
is chosen.

`tools/verify_fifth_channel_macdowell_mansouri.py` checks this commutator
exactly for both signs of `epsilon_psi`.

<!-- BILINGUAL-UNIT: fifth-channel-mm.action -->
## Graded curvature-square action

Use the canonical four-dimensional grading `Gamma_*` to define

\[
\boxed{
S_{\rm MM}
=-\frac{i\,\varepsilon_\psi\ell^2}{2\kappa}
\int\operatorname{Tr}
\left(\Gamma_*\mathcal F\wedge\mathcal F\right).}
\]

The graded trace annihilates the translation-curvature cross structures that
do not contain four Lorentz gamma matrices, while the already verified identity

\[
\operatorname{Tr}(\Gamma_*\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
=-4i\epsilon_{abcd}
\]

selects the oriented Lorentz-bivector channel. Exact expansion gives

\[
\boxed{
\begin{aligned}
S_{\rm MM}
={}&-\frac{\varepsilon_\psi\ell^2}{8\kappa}
\int\epsilon_{abcd}R^{ab}\wedge R^{cd}\\
&+\frac1{4\kappa}
\int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}\\
&-\frac{\varepsilon_\psi}{8\kappa\ell^2}
\int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d.
\end{aligned}}
\]

The first term is the four-dimensional Euler density. On a fixed topology it
is a topological term and does not modify the local bulk Einstein equations.
The second term is precisely the Hilbert--Palatini term with the normalization
used in the existing GR closure notes. Comparing the last term with

\[
-\frac{\Lambda}{24\kappa}
\int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d
\]

gives the structural relation

\[
\boxed{\Lambda=\frac{3\varepsilon_\psi}{\ell^2}.}
\]

Thus the sign of the cosmological term tracks the sign chosen for the fifth
Clifford channel, while its magnitude is set by the extended-connection length
scale.

<!-- BILINGUAL-UNIT: fifth-channel-mm.significance -->
## Why this is stronger than inserting Palatini by hand

The split-jet Palatini note established that a single-Theta variational
architecture can carry the complete Palatini equations, but it left the
curvature functional as an imported candidate. The present result supplies a
more unified algebraic origin for its **form**:

1. start from one extended Clifford connection;
2. form one graded curvature-square invariant;
3. expand it;
4. obtain Euler topology, Palatini gravity and the cosmological term with fixed
   relative coefficients.

No independent `epsilon E E R` term is needed at the algebraic level. The
Palatini and cosmological structures are tied to the same fifth-channel
curvature.

This materially narrows the action-selection gap, but it does not yet close it.
The remaining question has moved from “why write the Palatini tensor
contraction?” to “why must UBT choose this extended connection and this graded
curvature-square functional?”

<!-- BILINGUAL-UNIT: fifth-channel-mm.parameters -->
## Parameter reduction and the remaining normalization problem

Once the curvature-square architecture is selected, `Lambda` is no longer an
independent coefficient: it is related to `ell` by

\[
\Lambda=3\varepsilon_\psi/\ell^2.
\]

However the overall coefficient still contains `kappa`. Equivalently, if a
more microscopic UBT derivation supplied a dimensionless coefficient `g_G^{-2}`
for the curvature-square trace, matching the Palatini term would relate
`kappa` to that coupling and `ell`; it would not determine both without an
additional input.

A particularly sharp future test is whether `ell` can be derived from the
physical complex-time `psi` sector. If a theorem identifies the fifth Clifford
channel with a compact geometric `psi` direction of radius `R_psi` and fixes
the translation normalization so that `ell=R_psi`, then

\[
\boxed{\Lambda=\frac{3\varepsilon_\psi}{R_\psi^2}}
\]

would follow. **No such identification is claimed here**: the canonical UBT
sources still leave the physical role, signature and scale of the `psi`
channel open.

<!-- BILINGUAL-UNIT: fifth-channel-mm.symmetry -->
## Symmetry caveat

A fixed grading insertion `Gamma_*` is Lorentz invariant but is not invariant
under the full extended de Sitter/anti-de Sitter group unless the grading is
promoted to, or derived from, a symmetry-breaking structure. In the standard
MacDowell--Mansouri mechanism this is exactly what reduces the extended gauge
symmetry to the Lorentz subgroup.

For UBT this is not a cosmetic point. A complete derivation must explain why
the canonical fifth/complex-time structure supplies the required grading or
symmetry reduction rather than adding an external preferred internal vector.
Until that theorem exists, the construction is a highly constrained candidate,
not the finalized fundamental action.

<!-- BILINGUAL-UNIT: fifth-channel-mm.verification -->
## Verification

`tools/verify_fifth_channel_macdowell_mansouri.py` checks in exact symbolic
arithmetic:

- `Gamma_psi^2=epsilon_psi` for both canonical fifth-channel choices;
- the translation commutator `[P_a,P_b]=-epsilon_psi J_ab`;
- the relative Euler, Palatini and volume coefficients in the curvature-square
  expansion;
- the relation `Lambda=3 epsilon_psi/ell^2`.

The differential-geometric curvature decomposition and topological nature of
the Euler term are standard analytic results. No Lean formalization is claimed;
this note is `LEAN-PENDING` beyond the finite Clifford algebra already checked
by the exact verifier.

<!-- BILINGUAL-UNIT: fifth-channel-mm.status -->
## Status

**FIFTH-CHANNEL CLIFFORD CURVATURE-SQUARE EXPANSION TO
EULER + PALATINI + COSMOLOGICAL TERMS: PROVED ALGEBRAICALLY [L1].**

**RELATIVE COSMOLOGICAL RELATION `Lambda=3 epsilon_psi/ell^2` WITHIN THIS
CANDIDATE: PROVED [L1].**

**DERIVATION OF THE EXTENDED CONNECTION, GRADING SELECTION, `ell` AND THE
OVERALL NEWTON NORMALIZATION FROM LOCKED UBT DYNAMICS: OPEN.**
