
UBT — Parameter fixing + Theta-ansatz blocks (drop-in insert)
=============================================================
This zip contains two LaTeX blocks you can \input into your existing appendices
without touching the rest of the text. Both blocks introduce *discrete* choices only.

Files:
  - appendix_V_param_fix_block.tex
      Adds a short subsection "Parameter fixing for the internal torus" with:
        • modulus branch τ ∈ { i, e^{iπ/3} } (baseline τ=i),
        • Hosotani/Wilson branch θ_H=π with NS shift δ=1/2 on one cycle,
        • R fixed later in K.5 by Λ_QCD (no continuous tuning here).
      Markers: % === AUTO-INSERT V PARAM FIX BEGIN/END ===

  - appendix_QA_theta_ansatz_block.tex
      Adds a short subsection "UBT theta–eigenmode ansatz (discrete)" that replaces
      plane-wave placeholders by finite Jacobi-theta expansions with discrete
      characteristics, and defines the holonomy profile Φ with coefficients in {±1, ±i}.
      Markers: % === AUTO-INSERT QA THETA ANSATZ BEGIN/END ===

How to include:
  1) In appendix_V_emergent_alpha.tex, add near the end (or after the paragraph that
     states τ, R are set by V_eff):
        \input{appendix_V_param_fix_block}

  2) In appendix_QA_quarks_CKM.tex, add near the beginning of QA (before the checkpoints):
        \input{appendix_QA_theta_ansatz_block}

Then run LaTeX as usual. Both blocks are self-contained and add no new refs.
