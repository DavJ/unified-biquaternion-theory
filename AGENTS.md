# AGENTS.md — Unified Biquaternion Theory Development Protocol

This repository is a scientific research environment. AI agents and human
contributors must preserve mathematical consistency, proof status, and the
separation between canonical, research, speculative, and historical material.

## 1. Authority and repository layers

Read these before changing theory content:

1. `canonical/AXIOMS.md`
2. `canonical/CANONICAL_DEFINITIONS.md`
3. `STATUS_OF_UBT.md`
4. `CLAIMS.yaml`
5. `.github/copilot-instructions.md`

Repository layers:

- `canonical/` — current internally consistent reference formulation;
- `research_tracks/` — active but incomplete derivations;
- `speculative_extensions/` — explicitly speculative ideas;
- `ARCHIVE/` — historical/superseded material; do not silently reactivate it.

Do not create new top-level theory roots or duplicate the canonical tree.
Scientific material is not deleted merely because it is superseded; mark it
historical/noncanonical or move it to the existing archive workflow.

## 2. Locked canonical GR route

### Architecture-before-repair rule

Before resolving an obstruction by adding fields, modes, dimensions, fibers,
projections, averaging operations, embeddings, or auxiliary structures, first
determine whether the obstruction is an artefact of the chosen formulation
rather than a property of canonical UBT. Architectural diagnosis takes
precedence over technical repair. A locally correct rank or variation argument
must not be extrapolated beyond the framework in which it was proved.

### Framework freeze for the v10.x line

The covariant-tetrad architecture is frozen for the v10.x development line.
No agent may replace the metric readout, the tetrad
`E_mu=N0^(-1/2)D_mu Theta`, or the two-sided curved connection framework
without all of the following:

1. an explicit human decision by the repository author;
2. a written comparative audit of the current and proposed architectures;
3. proof that the obstruction is not merely a formulation artefact;
4. synchronized updates of canonical definitions, status ledgers, student
   material, tests, and agent instructions.

Difficulties in `GAP-10T-DYN`, `GAP-10I-CURVED`, or `GAP-10D` must first be
treated as gaps inside the frozen architecture, not as permission to invent a
new framework.

All active canonical GR work starts from the single UBT field

```text
Theta(q,tau) in C tensor H,       tau = t + i psi,
```

the covariant tetrad

\[
E_\mu:=\mathcal N_0^{-1/2}D_\mu\Theta,
\]

```text
E_mu := N0^(-1/2) D_mu Theta,
```

and the central anticommutator identity

```text
1/2 (E_mu^sharp E_nu + E_nu^sharp E_mu) = g_munu * 1.
```

On the Lorentz real slice

```text
E_mu = i e_mu^0 * 1 + e_mu^k e_k,
```

this is exactly

```text
g_munu = e_mu^a e_nu^b eta_ab,   eta = diag(-1,1,1,1).
```

The metric is already the central coefficient of an algebraic identity. It is
not obtained by throwing away components.

### Forbidden projection/fiber routes for the canonical GR metric

Do not use any of the following to repair rank or define the physical metric:

- `ReTr(...)`, componentwise `Re(...)`, or a trace/phase projector;
- compact-`psi` fiber averaging or a preferred `psi` section;
- an auxiliary embedding/ambient map introduced to obtain ten components;
- a local denominator that fixes `g_00` by normalization;
- `Gamma = Re(Omega)` or any identification of coordinate and spin connection.

These routes may remain explicitly historical or exploratory, but must not be
presented as the active UBT derivation of GR.

## 3. Connections, torsion, and representation

Keep three objects distinct:

- `Gamma^rho_{mu nu}` — affine/coordinate connection;
- `omega_mu^a_b` — Lorentz-frame connection;
- `Omega_mu = rho_*(omega_mu)` — spin/biquaternionic representation acting on
  the field space.

For a nondegenerate tetrad and specified torsion, the metric-compatible frame
connection is kinematically unique:

```text
omega(e,T) = omega_LC(e) + K(T),
K_abc = 1/2 (T_cab - T_abc - T_bca)
```

for the convention `T^a = de^a + omega^a_b wedge e^b`.

Consequences:

- torsion-free classical GR has `T=K=0` and the Levi-Civita spin connection;
- the remaining full-UBT problem is the dynamical law selecting torsion and the
  exact representation on `Theta`, not arbitrary kinematic freedom in `omega`;
- in Cartesian inertial Minkowski gauge, `Gamma=omega=Omega=0`;
- a nonzero connection in curvilinear coordinates does not by itself imply
  curvature.

Never write `D_mu` without specifying multiplication side and representation.
The generic curved algebra-native candidate is two-sided:

```text
D_mu Theta = partial_mu Theta + A_mu Theta - Theta B_mu,
[D_mu,D_nu]Theta = F^A_mu_nu Theta - Theta F^B_mu_nu.
```

A naive one-sided regular connection with invertible `Theta`, torsion-free
antisymmetric tetrad compatibility, and the same induced connection forces
zero curvature. Do not use that route for generic curved GR.

The seemingly economical identification `A_mu=Omega_mu`,
`B_mu=-Omega_mu^ddagger` is also not a generic curved-GR completion. It reduces
the pair to the existing spin connection, but then `E_mu=D_mu Theta/sqrt(N0)`
implies a concurrent vector `nabla_mu V^nu=delta_mu^nu`; Schwarzschild with
nonzero mass is excluded. Use this branch only as a proved no-go/diagnostic.
A viable relative left/right component must be derived from the action and
shown composite or auxiliary, not simply postulated as two new fields.

## 4. Exact GR gap ledger

Use these statuses unless a new proof explicitly changes them:

- `GAP-10K: CLOSED locally` — tetrad-to-metric differential has rank 10 and
  six local-Lorentz kernel directions.
- `GAP-10Omega-KIN: CLOSED [L1]` — specified `(e,T)` uniquely reconstructs the
  metric-compatible frame connection, up to local Lorentz gauge.
- `GAP-10Omega-GR: CLOSED [L1]` — the torsion-free branch is the Levi-Civita
  spin connection.
- `GAP-10T-PALATINI: CLOSED CONDITIONALLY [L1]` — in the minimal
  Hilbert--Palatini branch the Cartan equation is algebraic and invertible:
  zero spin current gives zero torsion; specified spin current gives unique
  contorsion.
- `GAP-10T-DYN: NARROWED` — derive that minimal branch, its exact spin current,
  normalization, and any additional torsion invariants from canonical UBT.
- `GAP-10L-CONN: CLOSED [L1]` — metric-compatible Lorentz transport preserves
  `eta_ab` and the Lorentz slice.
- `GAP-10L-SYM: CLOSED CONDITIONALLY [L1]` — the Lorentz slice is the fixed
  set of `J(X)=-conj(X^sharp)` and is preserved by every unique J-equivariant
  evolution with J-real data and sources.
- `GAP-10L-DYN: NARROWED` — verify equivariance and well-posed uniqueness for
  the finalized canonical UBT equations.
- `GAP-10I-SR: CLOSED [L1]` — every constant Lorentz tetrad has an explicit
  affine single-`Theta` representer; Minkowski is included.
- `GAP-10I-1S: CLOSED AS NO-GO [L1]` — the stated one-sided invertible curved
  route forces zero curvature.
- `GAP-10I-PAIR-KIN: CLOSED [L1]` — Lorentz-slice and metric compatibility
  reduce the apparent pair to one spin connection modulo a central term that
  cancels.
- `GAP-10I-PAIR-GR: CLOSED AS NO-GO [L1]` — that pure Lorentz pair implies a
  concurrent vector and cannot generate generic curved GR or Schwarzschild
  with nonzero mass.
- `GAP-10I-2S: NARROWED [L1]` — the remaining generic route requires a
  nontrivial relative bimodule action derived as composite or auxiliary, with
  no new propagating degrees of freedom.
- `GAP-10I-PRESCRIBED: CLOSED [L1]` — for specified `(E,A,B)` the exact
  existence and path-independence criterion is stabilization of `(Theta0,1)`
  by the augmented holonomy.
- `GAP-10I-CURVED: NARROWED` — self-consistent action-level selection,
  regularity, and global continuation remain open.
- `GAP-10D-PALATINI` and `GAP-10D-UNIQUENESS`: CLOSED CONDITIONALLY [L1].
- `GAP-10D: NARROWED` — derive the low-energy Palatini/Lovelock assumptions,
  couplings, and matter sector from canonical UBT.
- `GAP-10psi-KIN: CLOSED [L1]`; `GAP-10psi-SYM: CLOSED CONDITIONALLY [L1]`;
  overall `GAP-10psi: NARROWED`.
- `GAP-B-MASTER`, `GAP-U2Theta`: OPEN.

Do not merge a conditional branch result into an unconditional theory claim.

## 5. Implicit/self-consistent equations

After eliminating the classical frame connection, the tetrad equation is
schematically

```text
E_mu = N0^(-1/2) [partial_mu Theta
                  + A_mu[E,T] Theta - Theta B_mu[E,T]].
```

This is an implicit nonlinear first-order PDE/fixed-point system. If `Theta` is
restricted to Jacobi-theta or another transcendental function class, the full
system may additionally be transcendental. Keep these mathematical properties
separate in formal statements.

Do not call connection reconstruction a proof that this system has a solution.
Existence, uniqueness, regularity, boundary data, global continuation, and
action-level selection remain separate tasks.

## 6. Variation and dynamics guardrails

- If `Omega`, `A`, `B`, or torsion is varied, include the induced variation of
  `E_mu=N0^(-1/2)D_mu Theta`.
- Palatini/Einstein--Cartan results may be used only with their explicit
  assumptions. The minimal branch now has a proved algebraic torsion theorem,
  but its origin from canonical UBT remains open.
- Do not infer Einstein dynamics solely from a rank theorem or standard tetrad
  identity.
- Do not claim Schwarzschild is generated on shell until the complete tetrad,
  including lapse, is selected by canonical `Theta` dynamics.
- Do not use `partial_psi Theta=i Phi Theta` or a Maxwell/U(1) field as a
  canonical vacuum-Schwarzschild derivation.

## 7. Proof and claim discipline

Every theorem must state:

- domain and regularity;
- algebra/involution conventions;
- independent variables and gauge freedom;
- exact assumptions;
- proof level;
- what is not proved.

A symbolic checker verifies only the identity encoded in it. Its output must
state what it does not test. Numerical agreement is not an action-level or
first-principles derivation.

Alpha is not derived from first principles. Consciousness, psychons, afterlife,
or ThetaComm claims remain outside canonical physics.

## 8. Change workflow

For theory changes:

1. edit the smallest authoritative set of files;
2. update all status surfaces (`CLAIMS.yaml`, `STATUS_OF_UBT.md`,
   `WHAT_IS_PROVED.md`, `CLAIMS_MATRIX.md`, `DERIVATION_INDEX.md`);
3. update student material when the conceptual structure changes;
4. update AI instructions and regression tests;
5. run exact verifiers and relevant tests;
6. compile affected standalone LaTeX papers;
7. record assumptions and remaining gaps in patch notes.

Prefer clarification and closure over adding new ontology.
