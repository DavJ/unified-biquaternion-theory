# UBT differential correction — D-composite real-frequency audit

**Patch date:** 2026-07-26  
**Base:** `unified-biquaternion-theory-master(27).zip`

## Audit verdict

Version (27) correctly fixes the two main overclaims from version (26):

1. `Theta in W_L` is a consistent subsector, not a necessary condition for all self-consistent solutions.
2. The `q=1` sector belongs to the real-exponential/Laplace symbol, not to real-frequency Fourier propagation.

One active ledger was missed: `CLAIMS_MATRIX.md` still carried the obsolete
`GAP-10T-DCOMP-SECTOR: CLOSED` wording. This patch synchronizes it.

## New exact no-go

For real Fourier modes, substitute `s = i k` with real `k`. Then

```text
q = i lambda.k,
det(I - A(i k,lambda)) = (1 - i lambda.k)^6.
```

Since `|1 - i r|^2 = 1 + r^2 > 0` for real `r`, the frozen full symbol is
invertible for every real Fourier covector. The homogeneous symbol therefore
has only the zero solution. Because `A` annihilates the exact-gradient image
symbolically, every driven real-frequency response is holonomic and
pullback-flat.

This closes:

`GAP-10T-DCOMP-LIN-REALFREQ: CLOSED AS NO-GO [L1]`

within the explicitly stated scope: frozen coefficients, affine background,
torsion-free connection, and the `W_L` subsector. Variable coefficients,
nonlinearities, torsionful closures, and sectors outside `W_L` remain open.

## Strengthening and wording corrections

- The gradient-annihilation identity is now checked symbolically, not only at a sampled point.
- The Jordan statement is corrected: generically the generalized zero-eigenspace has three size-two and four size-one Jordan blocks.
- Injectivity of the curl map on `ker(I-A)` follows analytically from gradient annihilation and `AF=F`.
- The Riemann check now tests rank six of the full restricted map at three exact generic `q=1` points, rather than checking only six selected basis vectors.
- The Riemann conclusion is explicitly generic; exceptional loci are not ruled out.
- “Resonant plane-wave sector” language is replaced by “real-exponential sector”.

## Validation

- `tools/verify_dcomposite_linearized.py`: 20/20 exact checks PASS.
- `pytest tests/test_dcomposite_linearized.py tests/test_claims_consistency.py`: 13 passed.
- Updated LaTeX note compiled cleanly and the three rendered pages were visually inspected.
- No `.pytest_cache`, `__pycache__`, or `*.pyc` files are included in the overlay.
- `layer2` shims and `derive_fine_structure` remain outside this diff.
