<!-- BILINGUAL-UNIT: action-decision.provenance -->
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

# Decision boundary for unconditional GR closure

<!-- BILINGUAL-UNIT: action-decision.result -->
## Exact current result

The existing locked kinematic axioms do **not** determine one microscopic
action strongly enough to upgrade GR recovery from `CLOSED_CONDITIONALLY` to
unqualified `CLOSED`.

This is not merely an unfinished calculation. The repository now contains
several exact obstructions:

- the kinematic axioms admit a continuous family obtained by adding an
  arbitrary Einstein--Hilbert coefficient, including zero, so that coefficient
  is not a consequence of the kinematics;
- the complete connected-symmetry-invariant quartic potential has a
  coefficient-independent noncompact `H=D=0` flat direction and cannot by
  itself select an isolated vacuum;
- every value-independent pure-gravity scalar depending only algebraically on
  the same first jet reduces to a cosmological-volume density;
- on the pure-gradient metric-lock branch the displayed quadratic kinetic term
  is a Jacobian null Lagrangian and supplies no bulk propagating Hessian;
- composing `S_EH` with a metric map `g(Theta)` gives
  `delta S/delta Theta = L_Theta^* E`; Einstein dynamics follows in the reverse
  direction only after a differential adjoint-injectivity/equivalence theorem,
  which pointwise metric rank does not supply;
- the split-jet constraint is surjective for every tetrad, hence it represents
  GR configurations but cannot select one from `Theta`;
- the existing scalar multisymplectic family has
  \(Q=0\), \(S_F=0\) and \(\delta S_F=0\) on the canonical Lorentz jet,
  even after a differentiable composite-connection substitution; an explicit
  stationary noneinsteinian metric is supplied by the
  [Lorentz-slice audit](multisymplectic_lorentz_slice_audit.en.md).

Accordingly, no honest status edit can remove the remaining action-level gap.
A new **derived dynamical theorem** or an explicitly approved **new dynamical
principle** is necessary.

<!-- BILINGUAL-UNIT: action-decision.routes -->
## Surviving action-selection routes

### Route A — direct composite curvature action

Use a higher-jet functional whose geometric reduction contains
`sqrt(-g(Theta)) R[g(Theta)]`.

Required before this route counts as a microscopic derivation:

- construct a genuinely local curved `Theta -> g[Theta]` map without an
  independently propagating tetrad/connection;
- prove the adjoint-injectivity/equivalence condition for its metric
  linearization;
- determine why this curvature invariant, rather than the continuous family
  with arbitrary coefficient and higher-curvature additions, is selected.

If the Einstein--Hilbert term is simply postulated, GR is encoded in the new
action rather than derived from the previous UBT axioms.

### Route B — spectral/generalized-Dirac action

Promote a fully defined UBT generalized-Dirac operator to a spectral action and
derive the low-energy coefficients from its heat kernel. This route is
structurally attractive because the same spectral expansion can in principle
produce gravitational and gauge kinetic terms.

It is not currently closed. It requires a finalized operator and domain,
reality/self-adjointness or a controlled Euclidean continuation, the physical
Hilbert-space/mode quotient, the cutoff/profile principle, and a derivation
showing that all of these objects are functions of the single UBT data rather
than imported Standard-Model/GR structures. The current repository spectral
triple is explicitly a working/speculative construction.

### Route C — UBT-native degenerate/higher-jet Theta action

Derive a new local action directly from the biquaternionic/theta structure,
possibly using antisymmetric higher-jet, curvature-commutator, or degenerate
first-order terms, and prove that its unconstrained Euler--Lagrange equations
select the required curved metric branch.

This would be the strongest notion of emergence, but no currently proved
modular or Jacobi heat identity is yet established as the physical dynamical
selection principle. Promoting the theta heat equation to dynamics would be a
new theory choice unless separately derived.

### Route D — direct biquaternionic induced gravity

Derive a genuine gauge-fixed nondegenerate fluctuation operator from the final
single-`Theta` action and compute its heat-kernel coefficient while retaining
the canonical covariant tetrad. This is the route called “B” in the current
research discussion. It remains a research possibility. In the Lorentz-real
restricted volume action, the full Hessian has zero second-order symbol for
both a fixed curved Lorentz connection and a connection depending only on
field values, including all of that dependence in the variation. The result
does not cover a derivative-dependent connection or all eight real
biquaternionic fluctuation directions. The complete fixed-connection Euler
and Jacobi formulas, the value-dependent proof and the remaining composite
chain rule are recorded in
[the biquaternionic induced-gravity audit](biquaternionic_induced_gravity_boundary.en.md).

<!-- BILINGUAL-UNIT: action-decision.recommendation -->
## Research recommendation

The preferred route is now Route D, formulated directly with the original
biquaternionic field and the covariant tetrad
\(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\). A Clifford or generalized-Dirac lift
may remain an algebraic diagnostic, but it must not replace `Theta`, the
tetrad, or the physical fluctuation Hessian.

The next high-value calculation is therefore the complete composite
biquaternionic Hessian, including the induced variations of `E`, `g` and the
physical connection. Its gauge/constraint quotient, Euclidean contour,
curvature coupling and UV-scale principle must then be derived before the
heat-kernel coefficient can be called a prediction of `G`. Route A remains a
consistent one-coefficient effective completion if the author elects to adopt
it, but it is not the preferred first-principles result.

<!-- BILINGUAL-UNIT: action-decision.status -->
## Status

**UNCONDITIONAL GR ACTION SELECTION FROM CURRENT LOCKED AXIOMS: NOT DERIVED.**

**SEARCH SPACE: NARROWED TO EXPLICIT HIGHER-JET / SPECTRAL / INDUCED DYNAMICAL
PRINCIPLES.**

This document does not modify the locked axioms and does not authorize a new
fundamental action. It records the exact point at which an author-level theory
choice would become necessary if no further derivation is found.
