# Solution P4: Derivation of the Fine-Structure Constant α

This directory contains our efforts to derive the fine-structure constant \(\alpha\) from first principles within the Unified Biquaternion Theory (UBT).

## Overview

We began by postulating a geometric origin for the "bare" value:
\[
\alpha_0^{-1} = 137
\]
based on topological quantization in complexified time \(\tau = t + i\psi\) and toroidal theta-mode expansions.

However, to match the experimentally observed value:
\[
\alpha^{-1}_{\text{exp}} \approx 137.035999...
\]
we computed one-loop quantum corrections using the vacuum polarization tensor in UBT.

## Key Files

- `alpha_constant_derivation_precise.tex`: Detailed symbolic derivation of the running of \(\alpha\) via QED-like loop corrections in UBT.
- `alpha_running_calculator.py`: Numerical script that computes \(\alpha^{-1}(\mu)\) from high scale to low scale, using known lepton masses and charges.
- `alpha_constant_derivation.tex`: Earlier derivation focusing on geometry and field quantization (no quantum correction).
- `README.md`: This document.

## Status

✔️ Geometric base value derived  
✔️ Running correction implemented  
➕ Future work may include quark and boson contributions to improve precision

## Goal

Derive \(\alpha\) fully from UBT with no empirical inputs and match physical values via geometry + quantum field corrections.



## Author

**Ing. David Jaroš** – Founder and Sole Author of the Unified Biquaternion Theory (UBT)

### AI Assistance (Tools used during development)

- ChatGPT-4o (OpenAI) – symbolic manipulation, LaTeX formatting, equation structuring
- Gemini 2.5 Pro (Google) – parallel hypothesis testing, auxiliary verification

AI models were used strictly as assistive tools.  
All theoretical content, decisions, and formulations are the intellectual work of Ing. David Jaroš.
