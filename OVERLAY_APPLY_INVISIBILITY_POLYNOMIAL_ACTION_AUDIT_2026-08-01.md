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

# Apply: invisibility polynomial-action regularity audit

**Date:** 2026-08-01  
**Base:** `unified-biquaternion-theory-master (2)(6).zip`  
**Status:** speculative/noncanonical track only

Apply from the repository root:

```bash
unzip UBT_invisibility_polynomial_action_audit_overlay_2026-08-01.zip -d /tmp/ubt-overlay
rsync -a /tmp/ubt-overlay/ ./
```

The ZIP contains repository-relative paths and no wrapper directory.

## Exact result added

The new file

```text
speculative_extensions/invisibility/POLYNOMIAL_ACTION_REGULARITY_AUDIT.md
```

proves:

- `K_Theta=d_4 Theta^sharp wedge d_4 Theta` is a closed exact two-form;
- `K_Theta wedge K_Theta` is an exact metric-free polynomial four-form;
- the corresponding pure-Theta action is regular at the tangentially null
  surface;
- its bulk Euler--Lagrange equation is identically empty for compactly
  supported variations;
- constant-coefficient first-jet four-forms cannot dynamically select or
  stabilise the Whitney shell.

This closes only weak action regularity.  The non-topological action, radial
field equations, finite energy, stability, and scattering remain open.

## Verification

```bash
python tools/verify_invisibility_polynomial_action.py
pytest -q \
  tests/test_invisibility_polynomial_action.py \
  tests/test_spherical_null_shell_theta.py \
  tests/test_biquaternionic_metric_nullity.py
```
