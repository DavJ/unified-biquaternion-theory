# Final release hygiene patch — 2026-07-19

Exact-baseline differential overlay for `unified-biquaternion-theory-master(13).zip`.

## Changes

1. Removes the misspelled duplicate
   `canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex`.
   The correctly named `gap_10t_palatini_torsion_dynamics.tex` is unchanged.
2. Restores the complete five-key output of
   `tools.planck_validation.mapping.get_all_predictions()`:
   - implemented mappings retain their existing numerical values;
   - open mappings `theta_star` and `sigma_8` are reported as `None`;
   - no mapping is implemented and no tunable parameter is introduced.

## Validation

Targeted regression suite:

```text
100 passed, 1 skipped in 1.99s
```

The skipped test requires the optional generated CSV
`scans/tt_scan_int_100_200.csv`.

A full repository suite was attempted in the clean container, but did not finish
within the execution window and exposed additional pre-existing failures outside
this two-file hygiene scope. This patch does not claim a globally green suite.
