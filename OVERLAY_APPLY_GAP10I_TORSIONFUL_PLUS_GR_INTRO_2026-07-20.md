# Apply consolidated GAP-10I torsionful + GR introduction overlay

**Base:** clean repository archive `unified-biquaternion-theory-master(17).zip`.

From the repository root:

```bash
unzip -o UBT_GAP10I_TORSIONFUL_PLUS_GR_INTRO_OVERLAY_2026-07-20.zip -d .
sha256sum -c OVERLAY_MANIFEST_GAP10I_TORSIONFUL_PLUS_GR_INTRO_2026-07-20.sha256
```

This is a consolidated overlay. It contains the complete 2026-07-19 GAP-10I
paired/torsionful local-representer update and the 2026-07-20 self-contained
UBT/Theta introduction in the canonical GR manuscript. It may be applied
directly to clean version `(17)`; the earlier torsionful overlay does not need
to be applied separately.
