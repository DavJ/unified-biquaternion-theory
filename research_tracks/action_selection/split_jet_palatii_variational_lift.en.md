<!-- BILINGUAL-UNIT: split-jet-palatii.provenance -->
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

# Split-jet pullback of the Palatini action: local variational equivalence

<!-- BILINGUAL-UNIT: split-jet-palatii.question -->
## Question

The existing split-jet theorem proves that every local Lorentz tetrad can be
represented by one `Theta` plus algebraic jet variables, but its pure multiplier
implementation cannot select the tetrad. The separate Palatini theorem proves
that an independently varied tetrad and Lorentz connection give the standard
Einstein--Cartan equations, but that formulation does not satisfy the strict
single-fundamental-field architecture by itself.

This note combines the two results in a different order: **do not introduce an
independent tetrad at all**. Insert the split-jet tetrad directly into the
Palatini functional and vary only `Theta` and nonpropagating connection/jet
variables.

<!-- BILINGUAL-UNIT: split-jet-palatii.action -->
## Candidate action

Let `X` be the Lorentz-real projection of `Theta`, put
`s=sqrt(N0)`, and work on a patch with

\[
X^2:=\eta_{ab}X^aX^b\ne0.
\]

Let `omega^{ab}` be the physical Lorentz connection. Introduce an auxiliary
Lorentz-valued jet one-form `K_J^{ab}` and a relative-central real one-form
`w`. Define the tetrad **compositely** by

\[
\boxed{
E^a=\frac1s\left(
 dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a
\right).}
\]

Physical curvature uses only `omega`,

\[
R^{ab}(\omega)=d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb}.
\]

Define the split-jet Palatini functional

\[
\boxed{
S_{\rm SJHP}[X,\omega,K_J,w]
=\frac1{4\kappa}\int
\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}(\omega)
-\frac{\Lambda}{24\kappa}\int
\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d.}
\]

There is no independently varied tetrad in this functional. `K_J` and `w`
contain no derivatives and are intended only as split-jet auxiliaries. The
physical connection remains separate from the jet correction, as required by
the existing one-connection exact-GR no-go.

This action is a **candidate**. The Hilbert--Palatini structure, `kappa` and
`Lambda` are not derived here from the previously locked UBT kinetic action.

<!-- BILINGUAL-UNIT: split-jet-palatii.surjectivity -->
## Exact jet-variation surjectivity [L1]

At fixed `X` and `omega`, the auxiliary variation is

\[
\delta E^a
=\frac1s\left(\delta K_J{}^a{}_bX^b+\delta w\,X^a\right).
\]

For every target Lorentz-vector-valued one-form `Y^a`, define

\[
\delta w=\frac{X_aY^a}{X^2},
\qquad
Y_\perp^a=Y^a-\delta w\,X^a,
\]

and

\[
\delta K_{J\,ab}
=\frac{Y_{\perp a}X_b-X_aY_{\perp b}}{X^2}.
\]

Then

\[
\delta K_J{}^a{}_bX^b+\delta w\,X^a=Y^a.
\]

Therefore the map

\[
(\delta K_J,\delta w)\longmapsto\delta E
\]

is pointwise surjective onto all four tetrad directions for every non-null
`X`. `tools/verify_split_jet_palatii_variational_lift.py` checks the finite
rank-four core and the explicit right inverse at exact rational witnesses.

<!-- BILINGUAL-UNIT: split-jet-palatii.tetrad-equation -->
## Auxiliary variation gives the full tetrad equation [L1]

Let `mathcal E_a` denote the Euler three-form obtained by varying the ordinary
Palatini functional with respect to an independent tetrad `E^a`:

\[
\delta_E S_{\rm HP}=\int \mathcal E_a\wedge\delta E^a.
\]

In `S_SJHP`, variation with respect to `(K_J,w)` gives

\[
0=\int\mathcal E_a\wedge
\frac1s\left(\delta K_J{}^a{}_bX^b+\delta w\,X^a\right).
\]

Because the parenthesized map is surjective, its transpose is injective. Hence
stationarity for all auxiliary jet variations is equivalent to

\[
\boxed{\mathcal E_a=0.}
\]

Thus the auxiliary variables transmit the **entire** Palatini tetrad equation,
not a projection of it. In vacuum this is the Einstein--`Lambda` tetrad
equation once the connection equation is imposed.

This is exactly the adjoint-injectivity mechanism that was missing from the
naive composed-Einstein--Hilbert route.

<!-- BILINGUAL-UNIT: split-jet-palatii.connection -->
## Physical connection variation reduces on shell to Cartan [L1]

The physical connection enters `S_SJHP` in two places: through curvature and
through the composite tetrad. Therefore

\[
\delta_\omega S_{\rm SJHP}
=\left.\delta_\omega S_{\rm HP}\right|_{E\ \mathrm{fixed}}
+\int\mathcal E_a\wedge
\frac1s\,\delta\omega^a{}_bX^b.
\]

The second term vanishes once the jet equations have imposed
`mathcal E_a=0`. The remaining equation is exactly the standard Palatini
connection equation. In spinless vacuum the already proved invertibility of
the Cartan map gives

\[
\boxed{T^a=0,
\qquad
\omega^{ab}=\mathring\omega^{ab}(E).}
\]

Hence the physical curvature is Levi--Civita on the vacuum branch even though
the separate jet variables can make the single-`Theta` tetrad map locally
surjective.

<!-- BILINGUAL-UNIT: split-jet-palatii.theta -->
## The Theta equation is redundant after the tetrad equation

At fixed auxiliary variables and physical connection, an `X` variation changes
only the composite tetrad. Schematically,

\[
\delta_X S_{\rm SJHP}
=\int\mathcal E_a\wedge\delta_XE^a.
\]

After the integration by parts required by the `d(delta X)` term, the resulting
`X` Euler equation is a linear differential consequence of `mathcal E_a` and
its covariant derivative. Therefore

\[
\boxed{\mathcal E_a=0\Longrightarrow
\frac{\delta S_{\rm SJHP}}{\delta X}=0.}
\]

The fundamental-field variation imposes no additional local restriction once
the full tetrad equation has already been enforced by the surjective auxiliary
jet variations.

<!-- BILINGUAL-UNIT: split-jet-palatii.converse -->
## Converse lift of every local Palatini solution [L1]

Conversely, take any local Palatini solution `(E,omega)` and choose any smooth
non-null `X`. Define

\[
Z^a=sE^a-(dX^a+\omega^a{}_bX^b),
\qquad
w=\frac{X_aZ^a}{X^2},
\qquad
Z_\perp^a=Z^a-wX^a,
\]

and

\[
K_{J\,ab}
=\frac{Z_{\perp a}X_b-X_aZ_{\perp b}}{X^2}.
\]

Then the composite definition reconstructs the prescribed tetrad exactly.
Since the Palatini tetrad and connection equations already hold, all
`S_SJHP` Euler equations hold. The unused stabilizer of `K_J` is algebraic and
does not change `E`.

Thus, on every non-null patch,

\[
\boxed{
\{\text{stationary points of }S_{\rm SJHP}\}/\text{jet stabilizer}
\quad\longleftrightarrow\quad
\{\text{Palatini stationary points}\}.}
\]

The equivalence is local and excludes null patches of `X` where the explicit
right inverse becomes singular.

<!-- BILINGUAL-UNIT: split-jet-palatii.significance -->
## What this closes

This result resolves an architecture-level ambiguity that remained after the
split-jet multiplier no-go:

- the pure split-jet **constraint** cannot select a tetrad because it decouples
  on shell;
- the split-jet variables inserted **inside the gravitational functional** do
  not decouple before variation;
- their surjective variation enforces the complete tetrad equation;
- the physical Palatini connection then reduces to Levi--Civita in vacuum;
- no independent tetrad field is required.

Accordingly:

**SINGLE-THETA SPLIT-JET VARIATIONAL EQUIVALENCE TO THE CHOSEN PALATINI
FUNCTIONAL: PROVED LOCALLY AND CONDITIONALLY [L1].**

This does **not** derive the Palatini curvature term from the original UBT
kinetic/potential action. It also does not determine `kappa` or `Lambda`. The
fundamental action therefore remains unfinalized.

<!-- BILINGUAL-UNIT: split-jet-palatii.remaining -->
## Remaining theorem-critical gap

After this result, the GR problem separates more cleanly:

1. **architecture/variation:** locally solved on non-null patches for the
   split-jet Palatini candidate;
2. **curvature-action origin:** still open --- derive, rather than insert, the
   Palatini/Einstein--Hilbert curvature term from UBT-native microscopic data;
3. **normalization:** still open --- derive the sign and Newton coefficient;
4. **global/null continuation and physical `psi` stability:** still open.

The next decisive task is therefore no longer whether a single-`Theta`
variational architecture can reproduce all Einstein equations. It can,
conditionally on the candidate above. The decisive unresolved problem is now
**why this curvature functional, with this normalization, must follow from UBT
rather than being chosen because it is GR**.

<!-- BILINGUAL-UNIT: split-jet-palatii.status -->
## Status

**SPLIT-JET PALATINI ADJOINT/SOLUTION-SET EQUIVALENCE ON NON-NULL PATCHES:
CLOSED CONDITIONALLY [L1].**

**ORIGIN AND NORMALIZATION OF THE PALATINI CURVATURE TERM FROM LOCKED UBT
DYNAMICS: OPEN.**

**UNCONDITIONAL GR RECOVERY: NOT YET CLOSED.**
