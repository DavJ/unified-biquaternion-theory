UBT Spectral Parity Sliding Scan (Prime vs Composite)

This ZIP adds a new tool:
  forensic_fingerprint/tools/spectral_parity_scan.py

It runs a sliding ell-window scan and outputs:
- CSV with observed metrics + Monte Carlo p-values
- PNG plot of p_mean vs window center

Install (from repo root):
  unzip -o UBT_spectral_parity_sliding_scan.zip

Run example:
  python3 -m forensic_fingerprint.tools.spectral_parity_scan \
    --tt-map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \
    --scan-lmin 110 --scan-lmax 162 \
    --win 16 --step-ell 2 \
    --mc 500 \
    --also-prime-composite \
    --out-prefix scans/scan_110_162_w16

Outputs:
  scans/scan_110_162_w16.csv
  scans/scan_110_162_w16.png

Notes:
- This uses the same null as your current test: phase randomization per ell.
- For "codes", a stronger next step is adding alternate nulls (permute/block shuffle).
