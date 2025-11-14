# UBT v10.0 Release Preparation Guide

## Overview

This document provides instructions for preparing and publishing the Unified Biquaternion Theory (UBT) version 10.0 to Zenodo and OSF platforms.

## Release Contents

The v10.0 release includes:

### Main Documents
1. **UBT_Main.tex** - Primary consolidated document with:
   - Updated metadata (title, author, date: November 2025)
   - Keywords: biquaternion, complex time, consciousness, unified field theory, Hermitian gravity, SU(3) symmetry, theta function
   - Acknowledgments to Chamseddine (2025) and Verlinde (2025)
   - Comprehensive introduction and mathematical foundations
   - License: CC BY 4.0

2. **UBT_Abstract_OSF.tex** - Abstract for OSF submission with:
   - Concise summary of theory
   - Key features and achievements
   - Disclaimer on speculative sections
   - Current status as of November 2025

### Appendices

3. **Appendix_F_Hermitian_Limit.tex**
   - Updated with Chamseddine (2025) reference
   - Added disclaimer: "The Hermitian correspondence discussed here is mathematical and speculative. No physical or experimental realization of complex-metric gravity or FTL propagation has been demonstrated to date."
   - Explains relationship between UBT and Hermitian gravity

4. **Appendix_G_Emergent_SU3.tex**
   - Added mapping table between quaternionic axes and SU(3) color charges:
     * i → Red
     * j → Green  
     * k → Blue
   - Explains emergence of color symmetry from biquaternionic structure

5. **Appendix_H_Theta_Phase_Emergence.tex** (NEW)
   - Drift-diffusion equation for phase field: ∂ψ/∂t = D∇²ψ - α∂V/∂ψ
   - Theta function attractor solutions
   - Physical interpretation and stability analysis

### Bibliography

6. **references.bib**
   - Added Chamseddine (2025) reference:
     ```bibtex
     @article{chamseddine2025hermitian,
       title={Gravity in Complex Hermitian Space},
       author={Chamseddine, Ali H.},
       journal={Physical Review D},
       year={2025}
     }
     ```
   - Includes earlier Chamseddine works, Verlinde references, and foundational physics references

## Build Instructions

### Local Build

To compile the documents locally:

```bash
# Main document
pdflatex UBT_Main.tex
bibtex UBT_Main
pdflatex UBT_Main.tex
pdflatex UBT_Main.tex

# OSF Abstract
pdflatex UBT_Abstract_OSF.tex
bibtex UBT_Abstract_OSF
pdflatex UBT_Abstract_OSF.tex
pdflatex UBT_Abstract_OSF.tex
```

### Automated Build

The GitHub Actions workflow will automatically:
1. Discover all LaTeX root files (files with `\documentclass`)
2. Compile each document using the appropriate engine
3. Upload PDFs to `docs/pdfs/` directory
4. Commit and push the compiled PDFs

## Release Steps

### 1. Pre-Release Verification

- [x] All source files created and committed
- [x] README.md updated with release information
- [ ] LaTeX files compile successfully (check GitHub Actions)
- [ ] PDFs are generated and look correct
- [ ] All references resolve correctly
- [ ] No broken citations or cross-references

### 2. Create Git Tag

```bash
git tag -a v10.0-final -m "UBT version 10.0 - Finalized for OSF/Zenodo release"
git push origin v10.0-final
```

### 3. Prepare Release Package

Create a zip file containing:

```bash
zip UBT_v10_release.zip \
  UBT_Main.pdf \
  UBT_Abstract_OSF.pdf \
  Appendix_F_Hermitian_Limit.tex \
  Appendix_G_Emergent_SU3.tex \
  Appendix_H_Theta_Phase_Emergence.tex \
  README.md \
  references.bib \
  LICENSE.md
```

Or include all necessary files from the consolidation_project directory if using the full build.

### 4. Zenodo Upload

1. Go to https://zenodo.org/deposit
2. Click "New upload"
3. Upload `UBT_v10_release.zip`
4. Fill in metadata:
   - **Title:** Unified Biquaternion Theory v10.0: Complex Time, Consciousness, and Field Unification
   - **Authors:** Ing. David Jaroš
   - **Description:** Use text from UBT_Abstract_OSF.tex
   - **Keywords:** biquaternion, complex time, consciousness, unified field theory, Hermitian gravity, SU(3) symmetry, theta function, General Relativity, quantum field theory, Standard Model
   - **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
   - **Upload type:** Publication → Working paper
   - **Publication date:** November 2025
5. Click "Publish"
6. Note the assigned DOI

### 5. OSF Preprint Upload

1. Go to https://osf.io/preprints/
2. Click "Add a preprint"
3. Upload UBT_Main.pdf
4. Fill in metadata:
   - **Title:** Unified Biquaternion Theory (UBT): Complex Time, Consciousness, and Field Unification
   - **Authors:** Ing. David Jaroš
   - **Abstract:** Use text from UBT_Abstract_OSF.tex
   - **Tags:** unified field theory, biquaternion, complex time, General Relativity, quantum field theory, gauge theory
   - **License:** CC BY 4.0
   - **Subjects:** Physical Sciences and Mathematics → Physics → Theoretical Physics
   - **DOI:** (Enter Zenodo DOI once received)
5. Submit for moderation

### 6. Update Repository with DOI

Once DOI is assigned:

1. Update README.md:
   ```markdown
   **DOI:** 10.5281/zenodo.XXXXX
   **Citation:** Jaroš, D. (2025). Unified Biquaternion Theory v10. Zenodo. https://doi.org/10.5281/zenodo.XXXXX
   ```

2. Create a GitHub Release:
   - Go to repository → Releases → Draft a new release
   - Tag: v10.0-final
   - Title: UBT v10.0 - OSF/Zenodo Release
   - Description: Link to Zenodo deposit and OSF preprint
   - Attach UBT_v10_release.zip

## Post-Release

1. Announce release on relevant channels
2. Update any external documentation or websites
3. Monitor for feedback and issues
4. Begin work on v10.1 addressing any immediate corrections

## Version History

- **v10.0 (November 2025):** 
  - Added Appendix H – Theta Phase Emergence
  - Improved Hermitian correspondence (Appendix F)
  - Added quaternion-SU(3) mapping (Appendix G)
  - Created OSF abstract
  - Ready for Zenodo/OSF release

## Contact

For questions about the release process, contact:
- Repository: https://github.com/DavJ/unified-biquaternion-theory
- Author: Ing. David Jaroš

## License

This documentation is part of the UBT project and is licensed under CC BY 4.0.
