# GitHub Copilot Instructions — Unified Biquaternion Theory
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- Last updated: 2026-07-16 — covariant tetrad, torsion reconstruction, integrability selection -->

## Repository role and authority

This is a scientific theory repository, not a generic codebase. Read
`AGENTS.md`, `canonical/AXIOMS.md`, `canonical/CANONICAL_DEFINITIONS.md`, and
`STATUS_OF_UBT.md` before editing theory. Preserve proof levels and the
canonical/research/speculative/historical separation.

## Locked canonical GR route

### Architecture diagnosis before repair

Before adding fields, modes, fibers, projections, embeddings, averages, or new
axioms to overcome an obstruction, verify that the obstruction is not caused by
the formulation used to state it. A correct calculation in an embedding or
projected variation framework is not automatically a no-go theorem for the
canonical tetrad framework. Diagnose the architecture before repairing the
technical symptom.

### v10.x framework freeze

The covariant-tetrad architecture is frozen for v10.x. Do not replace the
anticommutator metric, `E_mu=N0^(-1/2)D_mu Theta`, or the two-sided curved
derivative without explicit human approval and a written comparative audit.
Work on open gaps within this architecture. Never perform an autonomous
framework pivot.

All active GR work starts from

\[
E_\mu:=\mathcal N_0^{-1/2}D_\mu\Theta,
\qquad
\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=g_{\mu\nu}\mathbf1.
\]

```text
Theta(q,tau) in C tensor H
E_mu := N0^(-1/2) D_mu Theta
1/2 (E_mu^sharp E_nu + E_nu^sharp E_mu) = g_munu * 1
E_mu = i e_mu^0 * 1 + e_mu^k e_k
```

The anticommutator gives the central Lorentz metric. The algebraic
antisymmetric product is a bivector candidate. The commutator of covariant
derivatives gives connection curvature.

Never use projection/fiber alternatives as the canonical metric:

- `ReTr(...)`, a real-part/trace/phase projector;
- compact-`psi` fiber averaging or a preferred fiber section;
- an embedding/ambient map introduced to fix rank;
- local normalization forcing `g_00=-1`;
- `Gamma = Re(Omega)`.

Such content is historical/exploratory only.

## Connection and torsion theorem

Distinguish `Gamma`, `omega`, and the representation `Omega=rho_*(omega)`.
For a nondegenerate tetrad and specified torsion,

```text
omega(e,T) = omega_LC(e) + K(T)
K_abc = 1/2 (T_cab - T_abc - T_bca)
```

with `T^a=de^a+omega^a_b wedge e^b`. Thus:

- `T=0` gives the unique Levi-Civita spin connection;
- the full open question is torsion dynamics and the exact action on `Theta`;
- Cartesian inertial Minkowski gauge has `Gamma=omega=Omega=0`;
- nonzero connection coefficients in a curvilinear frame need not mean
  nonzero curvature.

## Connection representation selection

Never write `D_mu` without its representation and multiplication side. A
one-sided regular derivative

```text
D^L_mu Theta = partial_mu Theta + A_mu Theta
```

is a proved no-go for the generic invertible torsion-free curved route under
the assumptions in `gap_10i_integrability_selection.tex`.

The active curved candidate is the algebra-native two-sided derivative

```text
D_mu Theta = partial_mu Theta + A_mu Theta - Theta B_mu
[D_mu,D_nu]Theta = F^A_mu_nu Theta - Theta F^B_mu_nu.
```

For invertible `Theta`, torsion-free integrability requires the curvature
intertwiner `F^A=Theta F^B Theta^{-1}`. This removes the one-sided flatness
obstruction; it does not prove curved-space existence or derive `(A,B)` from
the action.

## Exact status vocabulary

Use these labels exactly:

- `GAP-10K: CLOSED locally`.
- `GAP-10Omega-KIN: CLOSED [L1]`.
- `GAP-10Omega-GR: CLOSED [L1]`.
- `GAP-10T-PALATINI: CLOSED CONDITIONALLY`; `GAP-10T-DYN: NARROWED`.
- `GAP-10L-CONN: CLOSED [L1]`.
- `GAP-10L-SYM: CLOSED CONDITIONALLY`; `GAP-10L-DYN: NARROWED`.
- `GAP-10I-SR: CLOSED [L1]`.
- `GAP-10I-1S: CLOSED AS NO-GO [L1]`.
- `GAP-10I-2S: NARROWED [L1]`.
- `GAP-10I-PRESCRIBED: CLOSED`; `GAP-10I-CURVED: NARROWED`.
- `GAP-10D-PALATINI/UNIQUENESS`: CLOSED CONDITIONALLY; `GAP-10D` and `GAP-10psi`: NARROWED; `GAP-B-MASTER` and `GAP-U2Theta`: OPEN.

Do not restore the obsolete `GAP-10Omega-FULL` or undivided `GAP-10I` labels
as current status.

## Implicit versus transcendental

After connection reconstruction, the curved system is schematically

```text
E_mu=N0^(-1/2)[partial_mu Theta+A_mu[E,T]Theta-Theta B_mu[E,T]].
```

Call it an implicit nonlinear first-order PDE/fixed-point system. It may also
be transcendental when a Jacobi-theta function class is imposed, but
implicitness and transcendence are distinct properties.

## Variation and review guardrails

- If varying a connection or torsion, include its contribution to
  `delta E_mu`.
- Do not import Palatini/Einstein-Cartan results without checking UBT field
  independence.
- Do not turn connection reconstruction, rank, or an exact identity into a
  derivation of Einstein dynamics.
- Do not claim on-shell Schwarzschild generation; `GAP-U2Theta` is open.
- Do not use `partial_psi Theta=i Phi Theta` or Maxwell/U(1) as the canonical
  vacuum-Schwarzschild mechanism.
- Define symbols, assumptions, regularity, gauge freedom, and what remains
  unproved.
- Update status files, student texts, tests, and patch notes together.

Key files:

```text
canonical/geometry/biquaternion_tetrad.tex
canonical/geometry/biquaternion_connection.tex
canonical/gr_closure/covariant_tetrad_rank_theorem.tex
canonical/gr_closure/gap_10omega_connection_elimination.tex
canonical/gr_closure/gap_10i_integrability_selection.tex
docs/czech/UBT_KOVARIANTNI_GEOMETRIE_PRO_STUDENTY_CZ.md
papers/UBT_GR_Submission.tex
STATUS_OF_UBT.md
```


## Conditional-subclosure guardrail

Never promote a Palatini or Lovelock branch to an unconditional UBT derivation.
`GAP-10T-PALATINI`, `GAP-10L-SYM`, `GAP-10D-PALATINI`,
`GAP-10D-UNIQUENESS`, and `GAP-10psi-SYM` are conditional theorems.
`GAP-10I-PRESCRIBED` closes only the system with prescribed coefficients through the exact augmented-holonomy criterion.
The full-theory gaps remain narrowed until the canonical UBT action selects the
required hypotheses and self-consistent fields.
