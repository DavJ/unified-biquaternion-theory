# UBT differential patch — composite flat admissibility + GR submission consistency pass

**Patch date:** 2026-07-26
**Base commit marker:** `205395cc364df6358afa7a542ee0bbb3bb53beca`

Root-relative overlay; extract from the repository root.

## New result

**GAP-10T-COMPOSITE-FLAT: CLOSED [L1].** In the gradient-composite
torsion-free scheme (tetrad = slice coordinate map of `dTheta/sqrt(N0)`,
only `Theta` varies, `V == 0`, Lorentz-real variations) the flat affine
representer is a stationary point of `S_HP + Lambda + S_kin` for **all**
values of `Lambda`, `kappa`, `N0`.

Proof: jet-constancy argument (the Lagrangian is a smooth local function of
the 2-jet with no undifferentiated `Theta`; all momenta are constant on the
affine jet) plus exact SymPy verification (verifier check C7): the
volume-type first variation integrates to zero for polynomial
boundary-vanishing slice-valued variations with linear and quadratic
coefficients, and the linearised Einstein-term variation with the exact
linearised Levi-Civita connection integrates to zero on the constant
background.

**Corollary (scheme inequivalence):** the effective-Palatini scheme excludes
every flat affine representer (GAP-10T-FLAT-NOGO), the gradient-composite
scheme admits it; the two variational schemes of the same minimal action are
dynamically inequivalent at the flat point. The surviving minimal
continuation of canonical UBT is composite.

**Non-claims:** the self-consistent D-composite variation, curved
backgrounds, uniqueness/stability of the flat point, and the origin of the
Hilbert-Palatini coefficients remain open. GAP-10T-DYN and GAP-10D remain
NARROWED; GAP-10T-DYN wording updated to point at the surviving composite
branch.

## GR submission consistency pass (three editorial fixes)

1. Scope box "Proved in this draft" now lists the fixed-background spin
   current + flat no-go, the pairing rigidity, and the composite flat
   admissibility (previously present only in the ledger).
2. Conclusion updated: the stale "derive the ... spin current" remaining-work
   sentence replaced with the current state (spin current derived; composite
   branch surviving; self-consistent variation the decisive task).
3. Abstract extended with two sentences summarising the dynamical-level
   results and the scheme inequivalence.
Ledger table extended with GAP-10T-COMPOSITE-FLAT; torsion-dynamics section
extended with the composite statement and the note path.

## Files

- canonical/gr_closure/gap_10t_composite_flat_admissibility.tex (new)
- tools/verify_canonical_spin_current.py (C7 added; 22 exact checks)
- tests/test_canonical_spin_current.py (2 tests added; Einstein-term check marked slow)
- CLAIMS.yaml, CLAIMS_MATRIX.md, STATUS.md, STATUS_OF_UBT.md, WHAT_IS_PROVED.md
- papers/UBT_GR_Submission.tex (+ regenerated docs/pdfs/UBT_GR_Submission.pdf)
- docs/pdfs/gap_10t_composite_flat_admissibility.pdf (new)

## Validation

- `python tools/verify_canonical_spin_current.py` — 22/22 exact checks PASS.
- `pytest tests/test_canonical_spin_current.py tests/test_claims_consistency.py` — 12 passed.
- Full suite `pytest tests/` — green (passed/skipped only), including
  `tests/test_physics_properties.py` (hypothesis installed in this environment).
- `pdflatex` — paper (two passes) and note compile with zero errors.

## Still pending from earlier audits (not part of this overlay)

Two active archive shims in `tools/forensic_fingerprint/tools/` and the
`ubt_with_chronofactor` import branch in
`experiments/constants_derivation/derive_fine_structure.py`; the shim scan
pattern should grep the module string, not the call pattern.
