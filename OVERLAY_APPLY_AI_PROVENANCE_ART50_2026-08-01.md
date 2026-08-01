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

# Apply the UBT AI-provenance / Article 50 transparency overlay

This overlay is repository-root relative. It assumes the 2026-08-01 GR hygiene
and CODATA provenance/integrity overlays have already been applied.

## Apply

```bash
unzip UBT_AI_PROVENANCE_ART50_2026-08-01.zip -d /path/to/unified-biquaternion-theory-master
cd /path/to/unified-biquaternion-theory-master
bash APPLY_AI_PROVENANCE_ART50_2026-08-01.sh
```

The script applies and checks source markers, regenerates the wiki, verifies the
fourteen curated PDFs, refreshes `SHA256SUMS.txt`, and runs focused release
gates. It never fills the author's signature.

## Required human action before public release

Read every path listed under `tiers.A_attested` in `PROVENANCE_TIERS.yaml`. If
and only if the attestation is true, replace the pending fields with your own
name and the actual review date:

```yaml
signed_off_by: "Ing. David Jaroš"
signed_off_date: "YYYY-MM-DD"
attested_as_of: "YYYY-MM-DD"
```

Then run:

```bash
python3 tools/apply_provenance_headers.py --check
python3 -m pytest -q tests/test_provenance_headers.py
python3 tools/regenerate_sha256sums.py
sha256sum -c SHA256SUMS.txt
```

Do not add the SU(3) paper to Tier A until its exact source path and substantive
review are deliberately confirmed. The likely current candidate is
`papers/UBT_Gauge_Submission.tex`, but this overlay does not assign it.
