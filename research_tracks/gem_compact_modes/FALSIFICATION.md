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

# Falsification and decision rules

This track is useful only if it can fail cleanly.

## F1 — balanced-polarization no-go

Enumerate admissible normalized biquaternionic polarizations `Q_+`, `Q_-` with
weighted occupations chosen so that the compact current vanishes.  If every
Lorentz-covariant circle-averaged bivector/spin observable also vanishes, then
there is no balanced chiral-standing-wave route.  The track reduces to an
ordinary compact-pressure/radion problem.

## F2 — local Lorentz no-go

For every proposed tetrad response `delta E_mu`, compute

```tex
delta g_{mu nu} 1
 = 1/2 delta(E_mu^sharp E_nu + E_nu^sharp E_mu).
```

If `delta g_{mu nu}=0`, the proposal is only a frame rotation.  It must not be
reported as light-cone rotation or gravitomagnetism.

## F3 — standard-stress reduction

Derive the low-energy symmetric source.  If it is algebraically equivalent to
standard electromagnetic/scalar stress-energy, the track may still describe a
valid UBT representation, but it provides no enhanced gravitoelectric channel.

## F4 — action absence

A coupling that is not obtained from the canonical action, a stated effective
action with controlled assumptions, or an auxiliary-field elimination is only
an ansatz.  It cannot close `GEM-CM-DYN1`.

## F5 — fixed-radius category error

If `R_psi` is fixed, statements that a mode "inflates the torus" are forbidden.
Only an energy dependence on a fixed parameter has been computed.  Expansion,
stabilization, or collapse requires a dynamical radion equation.

## F6 — Gödel representability is not dynamics

Reproducing the Gödel tetrad or metric closes only a kinematic target.  Failure
to satisfy the UBT Euler-Lagrange equation and source matching leaves
`GEM-CM-G1/G2` open.

## Decision tree

```text
Balanced current j_psi = 0?
  no  -> running-current branch; not a pure standing pair
  yes -> compact pressure survives
          |
          +-- averaged covariant bivector/spin = 0
          |     -> scalar/radion branch only
          |
          +-- averaged covariant bivector/spin != 0
                -> derive action coupling
                       |
                       +-- delta g = 0 -> Lorentz-gauge no-go
                       +-- delta g != 0
                              -> compare with standard T_mu_nu
                              -> only then test Gödel-type ansatz
```
