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

# Derivation verification policy

## Purpose

UBT papers combine long analytic derivations, standard mathematics, symbolic
algebra, numerical experiments, and genuinely open theory bridges.  A derivation
must therefore be checked independently of the prose in which it appears.
This policy applies to **all active UBT papers** and to theorem-level derivations
promoted into canonical material.  For a new or materially modified paper it is
a hard gate immediately.  Existing active papers must be migrated to the same
verification record progressively; lack of a record is technical debt, not an
exemption.

The policy does **not** change the repository's proof/claim tiers.  A successful
CAS, numerical, or Lean check verifies only the statement encoded in that
check; it does not by itself promote a conditional UBT statement to an
unconditional physical result.

## Lean-first rule

**Lean is the preferred formal verifier for theorem-critical mathematics.**
For a new or materially modified theorem, lemma, algebraic identity, recurrence,
finite-dimensional rank statement, or exact implication that is reasonably
formalizable, the agent must do one of the following:

1. provide a Lean theorem/proof and report that it was compiled successfully;
2. extend an existing Lean proof and compile the affected project; or
3. record `LEAN-PENDING` with a precise reason why formalization is not yet
   available, together with independent CAS/numerical checks where applicable.

An agent must never write "Lean verified", "formally proved", or equivalent
wording unless the `.lean` source was actually checked by Lean in the reported
environment.  Merely generating Lean-looking text is **not** verification.

When a local runtime lacks Lean, record that fact explicitly.  Do not downgrade
the requirement silently and do not claim a successful formal proof.

## Tool classes

Use the strongest applicable combination rather than relying on one program.
Accepted tools include, but are not limited to:

- **formal proof:** Lean (preferred; kernel-checked proof);
- **symbolic/CAS:** SymPy, Maxima, MATLAB Symbolic Math Toolbox, PTC Mathcad,
  GNU Octave with symbolic support, or another named CAS;
- **numerical/linear algebra:** NumPy/SciPy, MATLAB, GNU Octave, Mathcad, or an
  independently implemented numerical checker;
- **specialized exact tools:** domain-specific packages when their assumptions,
  versions, and inputs are recorded.

For reproducible CI, prefer open/scriptable tools (Lean, SymPy, Maxima, NumPy,
Octave).  Mathcad or MATLAB verification is welcome as an independent human
cross-check, but a proprietary worksheet alone should not be the only machine
verification for a claim intended to be reproducible from the public repo.

## Minimum verification by derivation type

### Exact algebra / tensor / matrix identities

- analytic derivation in the paper;
- one symbolic or exact-arithmetic checker;
- Lean proof for theorem-critical statements when reasonably formalizable;
- spot checks in an independently written implementation when sign/index
  conventions create realistic risk.

### Calculus, transforms, ODE/PDE manipulations

- analytic derivation including domain, boundary, convergence, and regularity
  assumptions;
- symbolic differentiation/integration where the CAS is competent;
- numerical evaluation at nontrivial points or against a second formulation;
- Lean formalization of exact lemmas where practical; otherwise `LEAN-PENDING`.

### Numerical predictions / fits / searches

- deterministic reproduction script with fixed inputs and versions;
- independent implementation or second numerical tool for important results;
- sensitivity/error/precision analysis;
- explicit separation of input/calibration data from predictions;
- Lean is used for exact supporting mathematics where useful, but floating-point
  agreement alone is never called a formal proof.

### Spectral, zeta, theta, and prime-sector calculations

- state convergence/analytic-continuation domain before manipulating sums,
  products, or integrals;
- test truncation and precision dependence numerically;
- cross-check symbolic identities independently;
- distinguish identities of the integers (for example an Euler product) from
  dynamical selection by UBT;
- formalize exact finite/algebraic subclaims in Lean whenever feasible.

## Two-channel rule for paper-critical derivations

A derivation carrying a paper's main conclusion should normally have at least
**two independent verification channels**.  Preferred order:

1. Lean + independent CAS/numerical checker;
2. two independent CAS/formulations if Lean is genuinely pending;
3. analytic derivation + independent numerical reproduction only when the
   result is intrinsically numerical.

Running the same formula through two front ends of the same library is not
strong independence.  Prefer different formulations, exact versus numerical
checks, or different software stacks.

## Required verification record

Every active research paper must contain a short `Verification` section or point
to a companion verification record. New or materially modified papers must add
or update that record in the same patch.  For each
important derivation record:

| Field | Required content |
|---|---|
| Claim / equation | theorem, lemma, equation, or claim identifier |
| Analytic status | existing UBT claim/proof level and assumptions |
| Tool | Lean / SymPy / Maxima / NumPy / MATLAB / Octave / Mathcad / other |
| Artifact | repo path to `.lean`, script, notebook, worksheet export, or test |
| Version | tool/package version when available |
| Result | pass/fail plus precision/tolerance where relevant |
| Scope | exactly what the check verifies |
| Limitation | what the check does **not** prove |
| Lean status | `PROVED`, `PARTIAL`, `LEAN-PENDING`, or `NOT-APPLICABLE` |

A paper is not "verification complete" merely because its LaTeX compiles.

## Agent workflow

Before calling a paper review-ready, an agent must:

1. enumerate its nontrivial derivations and map them to verification artifacts;
2. run all available exact verifier scripts and tests;
3. run or update Lean proofs for theorem-critical formalizable claims;
4. use a second CAS/numerical implementation for the main result when feasible;
5. compile the paper;
6. report unavailable tools honestly (for example `Lean not installed`);
7. record failed checks and unresolved formalization as open work, never hide
   them behind a passing numerical example;
8. keep AI provenance markings synchronized with `PROVENANCE_TIERS.yaml`.

## Interpretation guardrail

The verification stack answers different questions:

- **LaTeX build:** the document compiles.
- **Numerical test:** selected numerical consequences agree within a tolerance.
- **CAS check:** the encoded symbolic identity/manipulation is consistent under
  the stated assumptions.
- **Lean:** the formalized theorem follows from the formalized assumptions in a
  kernel-checked proof.
- **Physics claim:** still requires the UBT assumptions/bridges and empirical
  interpretation stated by the paper.

These levels must never be conflated.
