# forensic_fingerprint — Compatibility Shim

This root-level package is a **compatibility shim**.

The forensic fingerprint implementation now lives at:

```
ubt_with_chronofactor/forensic_fingerprint/
```

This shim exists so that existing tests and CI pipelines that do:

```python
import forensic_fingerprint
```

or that add `repo_root / 'forensic_fingerprint' / ...` to `sys.path` continue to work
without modification.

## How it works

`forensic_fingerprint/__init__.py` calls `_shim.ensure_importable()`, which:

1. Resolves the canonical path: `<repo_root>/ubt_with_chronofactor/forensic_fingerprint/`
2. Adds `ubt_with_chronofactor/` to `sys.path` so the `forensic_fingerprint` package inside
   it is importable.
3. Also adds the sub-package paths (`cmb_comb`, `grid_255`, `invariance`, `loaders`) so that
   direct imports used in tests continue to work.

## Future direction

If/when a `ubt_no_chronofactor/forensic_fingerprint/` implementation is created, `_shim.py`
can be updated to point at that instead, or to select between the two at import time.

## Real implementation

See `ubt_with_chronofactor/forensic_fingerprint/` for the full implementation, documentation,
and runbooks.
