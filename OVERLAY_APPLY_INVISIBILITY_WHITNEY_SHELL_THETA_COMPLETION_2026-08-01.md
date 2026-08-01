# Apply: Whitney spherical null-shell Theta completion

**Date:** 2026-08-01  
**Base:** `unified-biquaternion-theory-master(38).zip`  
**Status:** speculative/noncanonical track only

Apply from the repository root:

```bash
unzip UBT_invisibility_whitney_shell_theta_completion_overlay_2026-08-01.zip -d /tmp/ubt-overlay
rsync -a /tmp/ubt-overlay/ ./
```

The ZIP contains repository-relative paths and no wrapper directory.

## Exact result added

The overlay adds one global off-shell field ansatz

```text
speculative_extensions/invisibility/WHITNEY_SPHERICAL_NULL_SHELL_THETA.md
```

with the following verified properties:

- one globally integrable angular `Theta`, not two coordinate-patch potentials;
- exactly zero central angular metric on the null surface;
- an invariant biquaternionic area two-form nonzero at every point of `S^2`;
- smooth profile-mode separation between null and visible sectors;
- exact radial matching to a flat spherical central exterior;
- honest zero total complex flux (no false topological-charge claim).

This closes the integrability and kinematic matching step only.  It does not
provide an on-shell solution, finite-energy theorem, stability result, Maxwell
matching, or proof of invisibility.

## Verification

```bash
python tools/verify_spherical_null_shell_theta.py
pytest -q \
  tests/test_spherical_null_shell_theta.py \
  tests/test_biquaternionic_metric_nullity.py
```

A broader targeted regression set was also run successfully:

```text
47 passed, 1 skipped
```

The canonical `papers/UBT_GR_Submission.tex` still compiles to 21 pages.
