<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# BIQUATERNION GEOMETRY LOCK-IN
## Covariant-tetrad formulation of Unified Biquaternion Theory

**Author**: Ing. David Jaroš  
**Revision authorised**: 15 July 2026  
**Status**: CANONICAL GEOMETRY REFERENCE

## Core chain

The minimal local geometric structure is

\[
\Theta(q,\tau)
\longrightarrow
E_\mu:=\mathcal N_0^{-1/2}D_\mu\Theta
\longrightarrow
\begin{cases}
\{E_\mu,E_\nu\}_\sharp & \text{metric},\\
[E_\mu,E_\nu]_\sharp & \text{algebraic bivector},\\
[D_\mu,D_\nu] & \text{connection curvature}.
\end{cases}
\]

No embedding map, compact-fiber average, phase projector, trace, or real-part
readout is part of the canonical local metric definition.

## 1. Fundamental field

The only fundamental dynamical field is the biquaternionic field

\[
\Theta(q,\tau)\in\mathbb B=\mathbb C\otimes\mathbb H,
\qquad \tau=t+i\psi.
\]

The physical spacetime field is smooth.  The exact intrinsic notion of
biquaternionic regularity in the argument \(q\) remains a dedicated open theorem
track and is not replaced by ordinary componentwise complex holomorphy.

## 2. Covariant tetrad

\[
\boxed{E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta.}
\]

The constant \(\mathcal N_0\) fixes units.  A local normalization denominator is
forbidden.

In the classical Lorentz sector,

\[
E_\mu=i e_\mu{}^0\mathbf1+e_\mu{}^k\mathbf e_k,
\qquad e_\mu{}^a\in\mathbb R.
\]

## 3. Full biquaternionic tensor and metric without projection

The ordered product

\[
\mathfrak G_{\mu\nu}:=E_\mu^\sharp E_\nu
\]

is the full biquaternionic geometric tensor. Historical documents may call it
the biquaternionic metric. In the canonical GR architecture, the word metric is
reserved for the symmetric central channel below; the antisymmetric
biquaternionic channel remains part of the full geometry and is not deleted.

With quaternion conjugation \(\sharp\),

\[
\boxed{\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=g_{\mu\nu}\mathbf1.}
\]

The full anticommutator is already central.  Therefore \(g_{\mu\nu}\) is not
obtained by applying `Re`, a trace, a phase map, or a fiber average.

Equivalent tetrad form:

\[
g_{\mu\nu}=e_\mu{}^a e_\nu{}^b\eta_{ab},
\qquad \eta=\operatorname{diag}(-1,1,1,1).
\]

## 4. Algebraic bivector

\[
\Sigma_{\mu\nu}
=\frac12(E_\mu^\sharp E_\nu-E_\nu^\sharp E_\mu)
\]

is antisymmetric and carries oriented-plane/spin information.  It is not
identified with a gauge field without a separate transformation and dynamical
derivation.

## 5. Connection and Christoffel symbols

\[
D_\mu\Theta=\partial_\mu\Theta+\rho_*(\Omega_\mu)\Theta.
\]

- \(\Omega_\mu\) transports the local Lorentz/biquaternionic frame.
- \(\Gamma^\rho{}_{\mu\nu}\) transports spacetime coordinate indices.
- They are related by the tetrad postulate,

\[
\partial_\mu E_\nu-\Gamma^\rho{}_{\mu\nu}E_\rho
+\rho_{\mathrm{vec}*}(\Omega_\mu)E_\nu=0.
\]

Do **not** write \(\Gamma=\operatorname{Re}\Omega\).  Their relation requires the
tetrad and the representation.

For specified tetrad and torsion, the metric-compatible frame connection is
uniquely reconstructed as \(\omega=\mathring\omega(e)+K(T)\).  The
single-field principle now requires the UBT action to select the torsion and
the exact left/right representation on \(\Theta\); these must not be inserted as arbitrary
new physical field.

## 6. Curvature and flat limit

\[
\mathcal R_{\mu\nu}(\Omega)
=[D_\mu,D_\nu]
=\partial_\mu\Omega_\nu-\partial_\nu\Omega_\mu
+[\Omega_\mu,\Omega_\nu].
\]

Special relativity corresponds to zero curvature.  In an inertial Cartesian
frame on a flat simply connected region one may choose

\[
\Omega_\mu=0,\qquad
\Gamma^\rho{}_{\mu\nu}=0,\qquad
D_\mu=\partial_\mu.
\]

Nonzero connection coefficients in curvilinear coordinates do not by themselves
mean nonzero curvature.

## 7. Rank theorem

The real tetrad \(e_\mu{}^a\) has sixteen components.  Six are local Lorentz
frame freedom; ten determine the metric:

\[
16-6=10.
\]

The differential of \(e\mapsto e\eta e^{\mathsf T}\) has rank ten at every
nondegenerate tetrad.  The previous comparison \(8<10\), based on the value of
\(\Theta\) alone, is not a local metric-rank obstruction.

## 8. Proof discipline

**Proved**:

- the central Lorentzian anticommutator identity;
- local representation of any Lorentz metric by a tetrad;
- rank ten of the tetrad-to-metric map;
- the flat inertial limit.

**Open**:

- derivation or unique elimination of \(\Omega_\mu\) from the single UBT action;
- preservation of the Lorentz slice;
- integrability of \(D_\mu\Theta=\sqrt{\mathcal N_0}E_\mu\);
- complete Einstein dynamics from the canonical master equation;
- on-shell global Schwarzschild, Kerr, FRW, and wave sectors.

**Exploratory only**:

The former compact-\(\psi\) fiber-average closure is retained as a mathematical
candidate completion, not as the canonical metric or rank mechanism.
