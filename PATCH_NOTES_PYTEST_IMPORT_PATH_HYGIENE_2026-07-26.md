# UBT differential patch — pytest import-path hygiene

**Patch date:** 2026-07-26  
**Base ZIP:** `unified-biquaternion-theory-master(33).zip`  
**Scope:** repository test infrastructure only; no physics equations, claims, or status levels changed.

## Problem

Three provenance tests modified `sys.path` at module-import time and inserted
nested implementation directories, including `tools/forensic_fingerprint`.
That directory itself contains a package named `tools`. During combined pytest
collection it could shadow the repository-root `tools` package. Consequently:

```text
pytest tests/test_manifest_validation_strict.py \
       tests/test_triqubit_qec_status.py
```

could fail with:

```text
ModuleNotFoundError: No module named 'tools.verify_triqubit_qec_status'
```

although each test passed in isolation. This made the suite order-dependent.

## Correction

- Replaced path injection and bare imports with package imports:

  ```python
  from scripts import hash_dataset, validate_manifest
  from scripts.repo_utils import find_repo_root
  ```

- Removed obsolete references to the nonexistent active path
  `tools/data_provenance`.
- Removed the top-level insertion of `tools/forensic_fingerprint`, preventing
  its nested `tools` package from shadowing the repository-root package.
- Added `tests/test_pytest_import_path_hygiene.py`, which rejects future
  top-level `sys.path` mutations in the three provenance tests.

## Validation

- provenance + SU(3) + GEM + workflow combined collection: **87 passed**;
- Layer2 + Planck: **66 passed**;
- forensic fingerprint: **60 passed**;
- linearized `D_composite`: **11 passed**;
- new import-path hygiene test: PASS;
- ZIP integrity and root-level packaging: PASS.

The uploaded `(33)` source tree was byte-for-byte identical to the previously
audited `(32)` tree before this patch. The uploaded archive nevertheless again
contained the redundant `unified-biquaternion-theory-master/` wrapper; the
release ZIP produced by this patch does not.
