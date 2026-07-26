# Patch manifest

Root-relative research overlay. It does not modify canonical claims.

Files:

- `research_tracks/dual_sector_clifford5/README.md`
- `research_tracks/dual_sector_clifford5/dual_sector_cl5_rank_status.md`
- `reviews/dual_sector_cl5_prior_art.md`
- `tools/verify_dual_sector_cl5_rank.py`
- `tests/test_dual_sector_cl5_rank.py`

Run:

```bash
python tools/verify_dual_sector_cl5_rank.py
pytest -q tests/test_dual_sector_cl5_rank.py
```
