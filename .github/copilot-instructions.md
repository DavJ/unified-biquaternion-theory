# GitHub Copilot Instructions for Unified Biquaternion Theory

## Repository Overview

This repository contains the **Unified Biquaternion Theory (UBT)**, a unified physical theory combining General Relativity, Quantum Field Theory, and Standard Model symmetries within a biquaternionic field defined over complex time τ = t + iψ. The repository is primarily a LaTeX-based theoretical physics research project with some supporting Python scripts.

**Author**: Ing. David Jaroš (some consolidated documents use "UBT Team")  
**License**: See LICENSE.md  
**Primary Language**: LaTeX (with Python support scripts)

## Repository Structure

```
.
├── .github/
│   ├── workflows/          # GitHub Actions for LaTeX compilation
│   └── latex_roots.txt     # List of root TeX files to compile
├── unified_biquaternion_theory/  # Original UBT documents and derivations
│   ├── ubt_main_article.tex      # Main UBT article
│   ├── ubt_appendix_*.tex        # 21 appendices with detailed theory expansions
│   └── solution_*/               # Important proofs and derivations
├── consolidation_project/        # Consolidated UBT documents (ongoing)
│   ├── ubt_2_main.tex           # Full consolidated document
│   ├── ubt_core_main.tex        # Core theory only
│   ├── appendix_*.tex           # Consolidated appendices
│   ├── scripts/                 # Python utility scripts
│   └── metadata/                # Project notes and TODOs
├── complex_consciousness/        # Complex Consciousness Theory (CCT)
│   └── ctc_2.0_main.tex         # CCT main document
├── docs/                        # Documentation and generated PDFs
├── scripts/                     # Utility scripts
├── Makefile                     # Build targets for LaTeX compilation
└── README.md                    # Main repository documentation
```

## Key Concepts

- **UBT**: Unified Biquaternion Theory - the main theoretical framework
- **CCT**: Complex Consciousness Theory - simplified application of UBT for consciousness modeling
- **Complex time**: τ = t + iψ where ψ is the imaginary time component
- **Biquaternions**: Mathematical foundation combining quaternions with complex coefficients
- **Psychons**: Quantum excitations of consciousness within complex-time phase space
- **CTCs**: Closed Timelike Curves - geometric solutions for time-travel
- **p-adic extensions**: Mathematical framework for dark matter and dark energy

## Build and Compilation

### LaTeX Compilation

The repository uses **pdflatex** for compiling LaTeX documents. Multiple compilation passes are needed for references.

**Local compilation:**
```bash
cd consolidation_project
pdflatex -interaction=nonstopmode ubt_2_main.tex
pdflatex -interaction=nonstopmode ubt_2_main.tex
```

**Using Make:**
```bash
cd consolidation_project
make all     # Compile full document (ubt_2_main.tex)
make core    # Compile core document (ubt_core_main.tex)
make clean   # Remove auxiliary files
```

**CI/CD**: GitHub Actions automatically compiles all root LaTeX files on push/PR. The workflow:
1. Discovers all `.tex` files with `\documentclass`
2. Detects the appropriate LaTeX engine (pdflatex/xelatex/lualatex)
3. Compiles each document
4. Uploads PDFs to `docs/pdfs/`

### Python Scripts

Python scripts are located in:
- `consolidation_project/scripts/` - Utility scripts for document processing
- `unified_biquaternion_theory/solution_*/` - Research calculations

No specific Python environment is required. Scripts are standalone utilities.

## Coding Style and Conventions

### LaTeX

- Use `\documentclass{article}` or similar for root documents
- Place appendices in separate files with descriptive names like `appendix_A_*.tex`
- Use consistent mathematical notation:
  - `\tau` for complex time
  - `\psi` for imaginary time component
  - Biquaternion fields denoted with bold symbols
- Include proper comments for complex derivations
- Use `\label` and `\ref` for cross-references
- Keep line lengths reasonable for version control

### Python

- Scripts are utility-focused, not production code
- Use clear variable names
- Include docstrings for non-trivial functions
- No strict style guide, but readability is important

## Important Files

### Primary Documents
- `unified_biquaternion_theory/ubt_main_article.tex` - Original UBT formulation
- `consolidation_project/ubt_2_main.tex` - Full consolidated UBT document
- `consolidation_project/ubt_core_main.tex` - Core theory without speculative sections
- `complex_consciousness/ctc_2.0_main.tex` - CCT application

### Configuration
- `.github/latex_roots.txt` - Lists root TeX files for CI compilation
- `.github/workflows/latex_build.yml` - CI/CD workflow
- `Makefile` - Local build configuration

### Documentation
- `README.md` - Main repository documentation
- `RESEARCH_PRIORITIES.md` - Current research priorities
- `PRIORITY.md` - Author priority claim and theory origin

## Working with This Repository

### When Adding New Content

1. **New appendices**: Create files following the naming pattern `appendix_[Letter]_[description].tex`
2. **New solutions**: Place in `unified_biquaternion_theory/solution_*/` directories
3. **Documentation updates**: Update README.md if adding major features
4. **LaTeX roots**: If adding a new standalone document, add it to `.github/latex_roots.txt`

### When Making Changes

1. **Test compilation locally** before pushing if possible
2. **Check for LaTeX errors**: Look for undefined references, missing packages, etc.
3. **Verify mathematical notation** is consistent with existing documents
4. **Update metadata** in `consolidation_project/metadata/` if relevant
5. **CI will compile PDFs** automatically - check Actions for errors

### Do Not Modify

- **Original theory files** in `unified_biquaternion_theory/` unless correcting errors
- **Priority claims** in PRIORITY.md
- **Generated PDFs** - these are auto-generated by CI
- **Author attribution** - all work is by David Jaroš unless explicitly noted

## Testing and Validation

- **LaTeX compilation** is the primary test - documents must compile without errors
- **CI workflow** must pass - check GitHub Actions status
- **Mathematical consistency** - verify derivations follow from established principles
- **Reference integrity** - ensure all `\ref` and `\cite` commands resolve correctly

## Common Tasks

### Adding a new appendix to the consolidated document
1. Create `consolidation_project/appendix_[X]_[name].tex`
2. Edit `consolidation_project/ubt_2_main.tex` to include it: `\input{appendix_[X]_[name]}`
3. Test compilation locally
4. Commit both files

### Adding a new Python calculation script
1. Place in appropriate directory (e.g., `consolidation_project/scripts/`)
2. Include clear comments explaining the calculation
3. Add any dependencies as comments at the top
4. Make executable if it's a standalone script

### Updating research priorities
1. Edit `RESEARCH_PRIORITIES.md`
2. Keep the numbered list format
3. Add new priorities at the end or update existing ones

## Resources

- **Main documentation**: See README.md
- **Research priorities**: See RESEARCH_PRIORITIES.md
- **Consolidation status**: Check `consolidation_project/metadata/`
- **Build logs**: Check GitHub Actions artifacts for compilation logs

## Notes for AI Assistants

- This is a **theoretical physics research repository** focused on mathematical derivations
- **Preserve mathematical rigor** - do not simplify or alter equations without understanding
- **LaTeX is the primary language** - most work involves document editing
- **Author attribution is critical** - this is David Jaroš's original work
- **Build validation is essential** - always verify LaTeX compiles successfully
- **Complex time concepts** require careful handling - don't oversimplify the mathematics
- **Python scripts are auxiliary** - the main content is in LaTeX documents
- **CI/CD handles PDF generation** - don't manually commit PDFs to the repository
