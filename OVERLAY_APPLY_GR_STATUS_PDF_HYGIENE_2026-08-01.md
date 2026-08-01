# GR split-jet status and PDF hygiene overlay

Date: 1 August 2026
Baseline audited: `unified-biquaternion-theory-master(43).zip`

Apply this archive directly at the repository root, then run:

```bash
bash APPLY_GR_STATUS_PDF_HYGIENE_2026-08-01.sh
```

## Corrected

- removes the remaining active `GAP-10T-JET-DYN: OPEN` and stale
  "prove nonpropagation" language;
- locks `GAP-10T-JET-AUX` as closed, pure-constraint tetrad selection as a
  no-go, and `GAP-10T-JET-DYN` as narrowed across the active status chain;
- adds a pytest regression guard against reopening the auxiliary theorem;
- reflows the GR submission conclusion identity and the long GAP ledger entry;
- removes the visible page-19 table overlap in the generated publication PDF;
- removes Python/pytest cache debris and two ignored test-generated outputs
  that were present in the uploaded ZIP;
- deduplicates repeated `.gitignore` entries.

## Validation performed

- targeted GR/publication/status pytest suite passed;
- `verify_gr_endgame_completion.py`, `verify_remaining_gr_subclosures.py`, and
  `verify_free_fiber_completion.py` passed;
- the two modified standalone theorem roots compiled;
- `papers/UBT_GR_Submission.tex` compiled to a 21-page PDF;
- all 21 pages were rendered; the page-19 overlap is gone and the conclusion
  display remains inside the normal text margins.

The full pytest suite is still not certified: `hypothesis` is unavailable in
this audit environment, and the remaining suite exceeded the execution window
without recording a failure through its first 10 percent.
