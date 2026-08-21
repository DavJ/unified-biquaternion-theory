## Role
<!-- Librarian / Scientist / Engineer / Experimentalist / Auditor -->

## Summary
- What this PR changes:

## Repo Grounding
<!-- REQUIRED: at least 2 path:line citations. -->
- `path/to/file:LINE` — relevant definition/status
- `path/to/checker:LINE` — verification or theorem

## Canonical GR Guardrail
<!-- Required when gravity, metric, connection, curvature, or Theta dynamics is touched. -->
- [ ] I checked whether the obstruction is a formulation artefact before adding structure.
- [ ] This PR does not pivot the frozen v10.x tetrad architecture; otherwise explicit human approval and a comparative audit are linked.
- [ ] Starts from `E_mu=N0^(-1/2)D_mu Theta` and the central anticommutator.
- [ ] Does not introduce a canonical trace/real projection, fiber average, or embedding map.
- [ ] Distinguishes `Gamma`, `omega`, and `Omega`.
- [ ] States the representation and multiplication side of `D_mu`.
- [ ] States whether torsion is specified, assumed zero, or derived.
- [ ] Does not use the one-sided invertible torsion-free route for generic curvature.
- [ ] Preserves the exact `GAP-10Omega-*` and `GAP-10I-*` statuses.
- [ ] Does not claim Einstein dynamics or Schwarzschild on-shell selection unless proved.

## Reproducibility
- Commands and expected output:

## Risks and assumptions
- Independent variables / gauge freedom:
- Assumptions:
- What remains unproved:

## Scope
- [ ] Text only
- [ ] Code only
- [ ] Text + code
- [ ] Experiment + committed artifact

## Verification
- [ ] Relevant symbolic verifier(s) passed.
- [ ] Relevant pytest regression suite passed.
- [ ] The repository-wide LaTeX audit was run or its CI report was reviewed; failures are recorded rather than hidden by fail-fast behaviour.
- [ ] `CLAIMS.yaml`, `STATUS_OF_UBT.md`, `WHAT_IS_PROVED.md`,
      `CLAIMS_MATRIX.md`, and `DERIVATION_INDEX.md` are synchronized.
- [ ] Student and AI-agent instructions were updated when concepts changed.

## Bilingual content gate
<!-- Required for active scientific, publication, explanatory, or student-facing prose. -->
- [ ] English and Czech editions are included in this PR, or the change is outside the scope defined in `BILINGUAL_CONTENT_POLICY.md`.
- [ ] Stable content-unit IDs, structure, equations, symbols, figures, tables, citations, cross-references, claim/status labels, caveats, and provenance match.
- [ ] Both editions build or render successfully and each rendered edition is monolingual.
- [ ] Translation source: <!-- EN / CS / not applicable -->
- [ ] Human reviewer: I explicitly confirm semantic equivalence of the English and Czech editions.

## Protected paths / audit
- [ ] Protected paths are touched and the required reviewer/label is present.
