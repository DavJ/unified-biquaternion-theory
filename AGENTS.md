<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

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
`B_mu=-Omega_mu^ddagger` reduces the pair to the existing spin connection.  In
the **torsion-free** generated-tetrad branch it implies a concurrent vector
`nabla_mu V^nu=delta_mu^nu`; the non-flat Schwarzschild vacuum exterior with
nonzero mass is excluded.  This is a torsion-free no-go, not a no-go for the
same one-connection pair with arbitrary composite contortion.

A complementary theorem in
`canonical/gr_closure/gap_10i_torsionful_local_representer.tex` constructs, on
every sufficiently small non-null Gaussian patch, a Lorentz-real single-Theta
representer with an explicit metric-compatible composite contortion.  This
closes local kinematic curved representability without independent `A_mu` or
`B_mu` fields.  It does **not** derive action selection, physical torsion
suppression, or global/horizon continuation.  A nontrivial relative left/right
component remains an optional torsion-free route and must be derived as
composite or auxiliary if used.

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
- `GAP-10T-SPIN: CLOSED CONDITIONALLY [L1]` — the direct fixed-background
  matter current is derived for the effective pure-pair Palatini variation.
- `GAP-10T-FLAT-NOGO` and `GAP-10T-PAIRING-NOGO`: `CLOSED AS NO-GO [L1]` —
  the minimal affine torsion-free branch fails, and no nonzero nondegenerate
  symmetric Lorentz-invariant pairing change removes the obstruction.
- `GAP-10T-DYN: NARROWED` — compute the full composite `Theta` variation and
  derive a canonical non-minimal torsion cancellation or translational/relative
  completion, together with the selected branch and normalization.
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
- `GAP-10I-PAIR-GR: CLOSED AS A TORSION-FREE NO-GO [L1]` — with `K=0` the
  pure Lorentz pair implies a concurrent vector and excludes the non-flat
  Schwarzschild vacuum exterior with nonzero mass.
- `GAP-10I-TORSION-LOCAL: CLOSED LOCALLY [L1]` — every smooth Lorentzian tetrad
  has, on a sufficiently small non-null Gaussian patch, an explicit
  single-`Theta` representer with composite metric-compatible contortion.
- `GAP-10I-2S: NOT REQUIRED FOR LOCAL KINEMATIC REPRESENTABILITY` — a relative
  bimodule action remains a possible torsion-free completion and must be
  derived as composite or auxiliary if used.
- `GAP-10I-PRESCRIBED: CLOSED [L1]` — for specified `(E,A,B)` the exact
  existence and path-independence criterion is stabilization of `(Theta0,1)`
  by the augmented holonomy.
- `GAP-10I-CURVED: LOCAL KINEMATICS CLOSED; DYNAMICS/GLOBAL PART NARROWED`
  — local curved representability is explicit, while canonical action-level
  selection, physical torsion constraints, regularity, and global continuation
  remain open.
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

## 10. Triqubit SU(3) error-code wording

Use the exact representation-level statuses:

- `GAP-SU3-TRIQUBIT-LEAKAGE: CLOSED [L1]` — the one-hot color sector detects
  every single-qubit `X_i` or `Y_i` error as leakage.
- `GAP-SU3-TRIQUBIT-QEC: CLOSED AS NO-GO [L1]` — it fails the
  Knill--Laflamme conditions for correcting an unknown single `X_i`, does not
  detect general `Z_i` phase errors, and is not a Pauli stabilizer code.

Do not call the present construction a quantum error-correcting code. Do not
infer a Matrix/simulation ontology from the existence of a structured color
subspace. Quantum-simulation-register use and ontological simulation claims are
separate statements.


## 11. Priority/provenance and GR completion guardrails

- Historical priority claims are mechanism-specific and must point to
  `docs/priority_evidence/OCTONION_MULTIVERSE_EVIDENCE.json` or another pinned
  external artifact. Do not backdate the 2026 tetrad, connection, or GR
  theorems to the 2016/2020 electroscalar archive.
- A related-work citation may be delimiting rather than genealogical. Do not
  remove the closest literature merely because UBT did not derive from it.
- `GAP-10T-MINIMAL-ONE-CONNECTION-GR: CLOSED AS NO-GO [L1]`: if the same
  metric-compatible Lorentz connection is both the defining jet connection and
  the physical spacetime connection, universal local single-Theta
  representability and exact generic torsion-free GR cannot both hold.
- For an exact-GR continuation, distinguish a derived composite/nonpropagating
  jet connection from the physical Levi-Civita connection. Do not silently call
  jet contortion physical torsion or introduce a second propagating connection.
- The controlled completion remains conditional until the jet functional and
  the Hilbert-Palatini term with Newton coefficient are derived from canonical
  UBT.
- `GAP-10T-JET-KIN: CLOSED LOCALLY [L1]`: the split exact-GR architecture has
  an explicit composite Lorentz plus relative-central jet right inverse on
  non-null Lorentz-real patches. Do not turn this kinematic identity into a
  claim that the action selects `E[Theta]`.
- `GAP-10T-JET-AUX: CLOSED [L1]`: the multiplier completion makes the jet
  variables algebraic and nonpropagating and removes their on-shell metric and
  physical-spin backreaction on every non-null patch.
- `GAP-10T-JET-CONSTRAINT-SELECTION: CLOSED AS NO-GO [L1]`: universal
  surjectivity means that the pure constraint cannot select a tetrad.
- `GAP-10T-JET-DYN: NARROWED`: action-level tetrad/representative selection (or
  a separate non-surjective metric effective law), null-patch/global
  continuation, and the constrained mode measure remain unresolved.

## 12. AI provenance and Article 50 transparency guardrails

- `PROVENANCE_TIERS.yaml` is an editorial map owned by Ing. David Jaroš. An AI
  agent may implement or validate the map but must not change an entry's tier,
  add an A-tier path, or fill `signed_off_by`, `signed_off_date`, or
  `attested_as_of` without an explicit author instruction for that exact field.
- Tier A means substantive human review and final editorial responsibility.
  Keep it small enough to be personally true. Passing tests is not a substitute
  for the author's attestation.
- Tier B means machine verification against named sources or verifier scripts;
  it does not imply line-by-line human review or scientific truth beyond the
  encoded checks.
- Tier C is working material. Its required wording is: "exhaustive human review
  is not claimed." Do not weaken or rewrite this as "not guaranteed."
- Tier D is historical material predating systematic AI-assisted development.
  Never add an AI marker under `ARCHIVE/`, `archive_legacy/`, or
  `legacy_variants/`; doing so would falsify provenance.
- Run `python tools/apply_provenance_headers.py --apply` after source changes and
  `python tools/apply_provenance_headers.py --check` before review or release.
- Curated LaTeX publications must load `ubtprovenance` after `hyperref`, declare
  `\UBTTier{A}`, `\UBTTier{B}`, or `\UBTTier{C}` consistently with the tier
  map, and place `\UBTProvenanceNotice` immediately after `\maketitle`.
- Do not label deterministic plots as AI-generated. Use
  `\UBTFigureProvenance{script}{data}` when a figure needs an explicit caption
  provenance statement. Genuinely AI-generated or AI-manipulated images need a
  separate, visible label and release-level record.
- Wiki provenance footers are generated by `tools/generate_wiki.py`; do not edit
  between their generated markers by hand.
- A provenance banner is a transparency mechanism, not a legal certification
  and not evidence that an open mathematical or physical gap has been closed.
- Regenerate `SHA256SUMS.txt` only after all banners, wiki pages, TeX sources,
  PDFs, and release metadata have reached their final state.
