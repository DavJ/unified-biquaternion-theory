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

# Apply: final Palatini one-step cleanup

This exact-baseline cleanup is for `unified-biquaternion-theory-master(14).zip`.
The snapshot already contains the corrected Palatini source/PDF and all prior
history, gauge/QM, theta-fit, Planck-policy, and reference fixes. It still
contains the misspelled duplicate source and PDF because ZIP extraction cannot
delete existing files.

From the repository root, extract this overlay and run:

```bash
bash APPLY_FINAL_PALATINI_ONE_STEP_CLEANUP_2026-07-19.sh
```

The script deletes only:

- `canonical/gr_closure/gap_10t_paladini_torsion_dynamics.tex`
- `docs/pdfs/gap_10t_paladini_torsion_dynamics.pdf`

It then runs the Palatini, theta-fit, and Planck mapping regression tests.
