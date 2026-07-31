# Apply: cumulative invisibility profile + spherical null-shell overlay

**Base:** `unified-biquaternion-theory-master(37).zip`
**Date:** 2026-08-01
**Status:** speculative/noncanonical only

This cumulative repository-relative overlay:

1. includes the pointwise rank obstruction and profile-space witness;
2. fixes escaped-control-character corruption in the earlier generated program file;
3. records the explicit spherical tangential-null shell candidate;
4. keeps all invisibility/device claims open and noncanonical.

Unpack directly over the repository root. It does not change Axiom C or the
canonical GR submission. Run:

```bash
python tools/verify_biquaternionic_metric_nullity.py
pytest -q tests/test_biquaternionic_metric_nullity.py
```
