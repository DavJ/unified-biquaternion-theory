# Differential patch: alpha information-loss research track

This ZIP is intended to be unpacked at the root of `unified-biquaternion-theory-master`.
It adds new files only; it does not overwrite canonical source-of-truth files.

Added files:

- `research_tracks/T3_ALPHA/information_loss_alpha_self_consistency.tex`
- `experiments/alpha_information_loss/reproduce_info_loss_alpha.py`
- `experiments/alpha_information_loss/README.md`
- `docs/reports/alpha_audit/information_loss_alpha_summary.md`

Status: research-track hypothesis, not canonical. The paper explicitly keeps
`alpha NOT DERIVED` as the conservative status and introduces the new gap
`G137-IQ`: derive the projection coefficient `C_Q` from `S[Theta]` and the
observable projection map.

Recommended commands after unpacking:

```bash
python experiments/alpha_information_loss/reproduce_info_loss_alpha.py
pdflatex research_tracks/T3_ALPHA/information_loss_alpha_self_consistency.tex
```

The LaTeX command will write the PDF in the current working directory unless
run from the file's folder or with an output directory.
