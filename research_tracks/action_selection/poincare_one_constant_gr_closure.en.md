<!-- BILINGUAL-UNIT: one-constant-gr.provenance -->
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

# One-constant Poincare contraction of the fifth-channel gravity candidate

<!-- BILINGUAL-UNIT: one-constant-gr.start -->
## Starting point

The merged fifth-channel Clifford candidate has the exact local decomposition

\[
S_{\rm MM}(\ell,\kappa)
=-\frac{\varepsilon_\psi\ell^2}{8\kappa}
 \int\epsilon_{abcd}R^{ab}\wedge R^{cd}
+\frac1{4\kappa}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}
-\frac{\varepsilon_\psi}{8\kappa\ell^2}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d,
\]

with

\[
\Lambda=\frac{3\varepsilon_\psi}{\ell^2}.
\]

Here `E` is the split-jet composite tetrad of the single `Theta` architecture.
The first integral is the four-dimensional Euler density. On a fixed topology,
with the usual fixed-boundary or compact-support variational conditions, its
bulk variation vanishes.

<!-- BILINGUAL-UNIT: one-constant-gr.subtracted -->
## Local/topologically subtracted action

For local field equations define

\[
\widetilde S_\ell
:=S_{\rm MM}
+\frac{\varepsilon_\psi\ell^2}{8\kappa}
 \int\epsilon_{abcd}R^{ab}\wedge R^{cd}.
\]

Then exactly

\[
\boxed{
\widetilde S_\ell
=\frac1{4\kappa}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}
-\frac{\varepsilon_\psi}{8\kappa\ell^2}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge E^c\wedge E^d.}
\]

Subtracting the Euler term changes no local bulk Euler--Lagrange equation. It
only removes a topology-dependent additive contribution whose coefficient
diverges in the contraction below.

<!-- BILINGUAL-UNIT: one-constant-gr.limit -->
## Exact Poincare contraction [L1]

Take the Inonu--Wigner/Poincare contraction

\[
\boxed{\ell\to\infty}
\]

while keeping `kappa > 0` fixed. Then

\[
\Lambda=\frac{3\varepsilon_\psi}{\ell^2}\longrightarrow0
\]

and coefficientwise

\[
\boxed{
\widetilde S_\ell
\longrightarrow
S_{\rm P}[E,\omega]
=\frac1{4\kappa}
 \int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}(\omega).}
\]

The local Euler--Lagrange forms converge to those of the zero-bare-cosmological-
constant Hilbert--Palatini action. No second continuous gravitational parameter
survives.

The same contraction is visible at the algebra level. With translation-like
fifth-channel generators `P_a`,

\[
[P_a,P_b]\propto\frac1{\ell^2}J_{ab},
\]

so `ell -> infinity` contracts the de Sitter/anti-de Sitter extension to the
Poincare algebra while retaining the Lorentz connection and tetrad sector.

<!-- BILINGUAL-UNIT: one-constant-gr.splijet -->
## Single-Theta split-jet equations [L1]

Use the already established composite tetrad

\[
E^a=\frac1{\sqrt{N_0}}
\left(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a\right)
\]

on a non-null patch `X^2 != 0`. The variation map

\[
(\delta K_J,\delta w)\mapsto\delta E
\]

is pointwise surjective onto all four tetrad directions. Consequently
stationarity with respect to the algebraic jet variables gives the complete
Palatini tetrad equation, not a projection.

Variation of the physical Lorentz connection contains the standard Palatini
connection term plus a chain-rule term proportional to the tetrad Euler form.
After the jet equation has set that form to zero, the remaining vacuum equation
is the Cartan equation. Its previously verified pointwise invertibility gives

\[
\boxed{T^a=0,\qquad\omega=\mathring\omega(E).}
\]

The `Theta` equation is a differential consequence of the full tetrad equation,
and every local Palatini solution has the explicit non-null split-jet lift.
Thus the local stationary-point set of the contracted action, modulo the
algebraic jet stabilizer, is the local stationary-point set of ordinary
zero-bare-`Lambda` Palatini GR.

<!-- BILINGUAL-UNIT: one-constant-gr.count -->
## Parameter count

The contracted gravitational sector contains only

\[
\boxed{\kappa}
\]

as a continuous physical gravitational constant. The locked `N0` is explicitly
a global unit-setting normalization, not an independently predicted physical
coupling. The sign of the Lorentz metric and orientation are discrete choices,
not continuous constants.

In vacuum the overall factor `1/kappa` cancels from the classical equations;
`kappa` becomes physically measurable only relative to the normalization of a
source sector. Under the UBT single-action rule, a source sector must be a
reduction of the same fundamental action rather than a separately normalized
fundamental term. Therefore no second **gravitational** coupling is permitted.

The contraction makes the bare cosmological constant a prediction,

\[
\boxed{\Lambda_{\rm bare}=0,}
\]

not a fitted gravity parameter. A nonzero observed effective dark-energy term
would have to arise from the `Theta` vacuum/quantum sector or from boundary
state data; introducing an independent bare `Lambda` would leave the
one-constant branch.

<!-- BILINGUAL-UNIT: one-constant-gr.status -->
## Closure meaning

This result separates two logically different questions:

- **Can a one-constant single-Theta gravitational law yield local GR?** Yes:
  the contracted split-jet Palatini law has exactly that solution set on
  non-null patches.
- **Was this dynamical law forced by the older kinematic axioms alone?** No.
  Kinematics cannot select an overall dynamical law; a theory requires a
  dynamical postulate.

Accordingly, adopting the Poincare-contracted fifth-channel action as the
canonical **gravitational dynamical postulate** converts GR recovery from an
assumed effective endpoint into an internal theorem of the finalized gravity
sector. The postulate has one continuous gravitational constant `kappa`.

This does not by itself finalize the non-gravitational Standard-Model/quantum
sectors of the unique UBT action, nor does it derive an observed nonzero
effective cosmological constant.

<!-- BILINGUAL-UNIT: one-constant-gr.verification -->
## Verification

`tools/verify_one_constant_gr_closure.py` checks symbolically:

- the exact MacDowell--Mansouri coefficient decomposition;
- `Lambda = 3 epsilon_psi/ell^2`;
- the topologically subtracted action coefficients;
- the `ell -> infinity` limit;
- the one-parameter count of the local contracted gravity coefficients;
- the derivative obstruction in the historical `R_psi` logarithmic potential.

The split-jet rank and Palatini/Cartan algebra are independently checked by the
verifiers merged with the preceding action-selection work. Full differential-
form formalization in Lean remains `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: one-constant-gr.verdict -->
## Verdict

**LOCAL SINGLE-THETA GRAVITY WITH ZERO BARE COSMOLOGICAL CONSTANT AND ONE
CONTINUOUS GRAVITATIONAL CONSTANT: CLOSED [L1] ON NON-NULL PATCHES, PROVIDED THE
POINCARE-CONTRACTED FIFTH-CHANNEL ACTION IS ADOPTED AS THE GRAVITATIONAL
DYNAMICAL POSTULATE.**

**ABSOLUTE `R_psi` SCALE SELECTION: NOT USED IN THIS CLOSURE.**

**FULL UNIQUE UBT ACTION INCLUDING GAUGE/MATTER/QUANTUM REDUCTIONS: STILL A
SEPARATE COMPLETION TASK.**
