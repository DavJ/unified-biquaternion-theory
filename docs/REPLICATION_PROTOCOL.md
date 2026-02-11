# Independent Replication Protocol (UBT Alpha Baseline)

This document provides a step-by-step protocol for independently replicating the UBT alpha baseline result: \(\mathcal R_{\mathrm{UBT}}=1\) at two loops under assumptions A1--A3.

## Prerequisites

- TeX Live (full installation recommended)
- Python 3.8 or later
- pytest (for running tests)

## Replication Steps

### 1. Build the Main Documents

Compile the consolidated UBT document and the publication manuscript:

```bash
# From repository root
cd consolidation_project
latexmk -pdf ubt_2_main.tex

# Build publication manuscript
cd ../publication/arxiv
latexmk -pdf main.tex
```

Expected outcome: Both PDFs should compile without errors.

### 2. Run Tests

Execute the test suite to verify baseline assumptions and check for placeholders:

```bash
# From repository root
pip install pytest numpy
pytest -q consolidation_project/alpha_two_loop/tests
```

Expected outcome: All tests should pass, confirming:
- No placeholder/pending/1.84 references remain near R_UBT
- CT baseline value equals 1 under standard assumptions

### 3. Verify Baseline Statements

Open the compiled PDF `consolidation_project/ubt_2_main.pdf` and verify:

1. **Appendix CT (Two-Loop Baseline)**: Contains Theorem stating \(\mathcal R_{\mathrm{UBT}}=1\)
2. **Appendix α (One-Loop)**: References the CT baseline theorem (Section~\ref{app:ct-baseline-R1})
3. **No placeholders**: Search the PDF for "pending", "placeholder", "1.84" in the context of \(\mathcal R_{\mathrm{UBT}}\) - should find only cautionary statements about what NOT to do

### 4. Check Geometric Inputs (Assumption A1)

Verify that \(N_{\mathrm{eff}}\) and \(R_\psi\) are uniquely determined:

- Location: `consolidation_project/alpha_two_loop/tex/geometric_inputs_proof.tex`
- Expected: Proposition showing no alternative values satisfy both Lorentz invariance and Thomson normalization

### 5. Verify CT Scheme (Assumption A2)

Check the CT scheme definition includes:

- Dimensional regularization
- Ward identities (\(Z_1 = Z_2\))
- QED limit reduction
- Location: `consolidation_project/alpha_two_loop/tex/ct_scheme_definition.tex`

### 6. Check R_UBT Extraction (Assumption A3)

Verify the extraction procedure:

- Location: `consolidation_project/alpha_two_loop/tex/R_UBT_extraction.tex`
- Expected: Baseline subsection with boxed result \(\mathcal R_{\mathrm{UBT}}=1\)

## File a Replication Report

After completing the above steps, file a replication report using the GitHub issue template:

1. Go to: https://github.com/DavJ/unified-biquaternion-theory/issues/new/choose
2. Select "Replication Report"
3. Provide:
   - Your environment details (OS, TeX distribution version, Python version)
   - Steps you followed
   - Observed outputs (any differences from expected)
   - PDF checksums (use `sha256sum ubt_2_main.pdf`)
   - Any build logs or error messages

## Expected Checksums

After a successful build, compute and compare checksums:

```bash
# From consolidation_project/
sha256sum ubt_2_main.pdf

# From publication/artifacts/
sha256sum ubt_alpha_baseline_arxiv.pdf
```

Include these checksums in your replication report to verify you obtained the same output.

## Troubleshooting

### LaTeX Compilation Errors

- Ensure you have a full TeX Live installation
- Run `pdflatex` twice to resolve references
- Check for missing packages and install via tlmgr

### Test Failures

- Install all Python dependencies: `pip install pytest numpy`
- Check that you're running tests from the repository root
- Review the test output for specific assertion failures

### Differences in Output

If your compiled PDFs differ from expected:

1. Check your TeX Live version: `pdflatex --version`
2. Verify all input files are identical: `git status`
3. Note the differences in your replication report
4. Include diff output if available

## Questions?

For questions about the replication protocol, open a discussion issue or contact the maintainers.

## License

This replication protocol is licensed under CC BY 4.0.
