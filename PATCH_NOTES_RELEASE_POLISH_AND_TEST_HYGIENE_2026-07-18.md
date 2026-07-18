# Patch notes: release polish and test hygiene

Baseline: `unified-biquaternion-theory-master (2)(3).zip`
Date: 2026-07-18

This cumulative root overlay combines the previously approved pre-release polish
with two narrowly scoped test-hygiene corrections.

## Included pre-release polish

- rename active `paladini` paths to the correct `palatini` spelling;
- update every active source, claim-ledger, paper, test, and PDF reference;
- add standard-source attribution to GAP-10I (Kobayashi--Nomizu) and GAP-10L
  (Olver);
- regenerate and visually verify the five affected PDFs.

## Test-hygiene corrections

1. `TestBiquaternionTetradMinkowski` now uses a classmethod class-scoped
   autouse fixture rather than the pytest-10-removed instance-fixture pattern.
   The six metric/tetrad regression tests are unchanged in content.
2. The unimplemented `M_phase` and `M_SNR` Planck mapping stubs again state the
   exact policy phrase `NO additional tunable parameters`. The mappings remain
   unimplemented and no fitting parameter was added.

No physical equation, claim level, architecture decision, or open-gap status is
changed by this overlay.
