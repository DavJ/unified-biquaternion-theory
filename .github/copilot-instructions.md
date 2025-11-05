# GitHub Copilot Instructions for Unified Biquaternion Theory Repository

## Repository Overview

This repository contains the **Unified Biquaternion Theory (UBT)**, a theoretical physics framework that unifies General Relativity, Quantum Field Theory, and Standard Model symmetries within a biquaternionic field defined over complex time τ = t + iψ. The repository also includes the **Complex Consciousness Theory (CCT)**, which applies UBT principles to model consciousness as a physical phenomenon.

**Author**: David Jaroš  
**Primary Content**: LaTeX research documents, mathematical derivations, and computational scripts

## Repository Structure

- `unified_biquaternion_theory/` - Original UBT documents and derivations
- `complex_consciousness/` - Complex Consciousness Theory (LaTeX sources & PDFs)
- `consolidation_project/` - Consolidated UBT documents (ongoing project)
  - `appendix_A_*/` - Appendices on gravity, gauge fields, QED/QCD, etc.
  - `img/` - Figures and diagrams
  - `metadata/` - Project notes, TODOs, consolidation maps
  - `scripts/` - Python scripts for computations
- `.github/workflows/` - GitHub Actions for automated LaTeX compilation
- `scripts/` - Shell scripts for repository maintenance
- `docs/` - Generated documentation and compiled PDFs

## Key Technologies

### LaTeX
- **Primary Use**: Research papers, mathematical derivations, theoretical documentation
- **Engines**: pdflatex (default), xelatex, lualatex (auto-detected by workflow)
- **Build System**: Makefile in root, GitHub Actions workflow for CI/CD
- **Main Documents**:
  - `unified_biquaternion_theory/ubt_main_article.tex`
  - `complex_consciousness/ctc_2.0_main.tex`
  - `consolidation_project/ubt_2_main.tex`

### Python
- **Primary Use**: Numerical computations, fine structure constant calculations, padic extensions
- **Key Scripts**:
  - `unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_running_calculator.py` - Fine structure constant calculations
  - `consolidation_project/scripts/padic/alpha_p_computation.py` - Padic computations
  - Various LaTeX manipulation scripts in `consolidation_project/scripts/`

## LaTeX Conventions

### Document Structure
- Use `\documentclass` to indicate root LaTeX files
- Organize content hierarchically: main document → sections → subsections
- Keep appendices separate in dedicated files
- Use consistent naming: `ubt_*` for UBT content, `ctc_*` for CCT content

### Mathematical Notation
- **Biquaternions**: Complex-valued quaternions, use appropriate notation
- **Complex Time**: τ = t + iψ (t = real time, ψ = imaginary/phase component)
- **Field Equations**: Follow standard tensor notation with clear index conventions
- **Gauge Groups**: SU(3) × SU(2) × U(1) for Standard Model symmetries

### Compilation Process
```bash
# Manual compilation (from project root or specific directory):
pdflatex -interaction=nonstopmode <file>.tex
pdflatex -interaction=nonstopmode <file>.tex  # Run twice for references

# With bibliography:
pdflatex <file>.tex
bibtex <file>
pdflatex <file>.tex
pdflatex <file>.tex

# Using Makefile:
make core    # Compile core document
make all     # Compile all main documents
make clean   # Remove auxiliary files
```

### Automated Builds
- GitHub Actions automatically compiles all LaTeX root files on push/PR
- Workflow detects engine requirements (xelatex, lualatex) automatically
- Compiled PDFs are uploaded as artifacts and committed to `docs/pdfs/`

## Python Script Guidelines

### Style
- Use clear, descriptive variable names reflecting mathematical concepts
- Document complex mathematical operations with inline comments
- Include docstrings explaining the theoretical basis of computations

### Dependencies
- Prefer standard libraries (math, numpy, scipy) when possible
- Document any specialized physics/mathematics libraries used
- No formal dependency management - list requirements in comments

### Numerical Precision
- Be mindful of floating-point precision in theoretical calculations
- Use appropriate numerical methods for stability
- Validate results against known theoretical limits

## Research Domain Context

### Theoretical Physics
- **General Relativity**: Metric tensor derivations, curved spacetime
- **Quantum Field Theory**: Field quantization, gauge invariance
- **Standard Model**: SU(3) × SU(2) × U(1) gauge symmetries
- **Dark Sector**: Dark matter and dark energy via padic extensions

### UBT and General Relativity Compatibility

**Critical Theoretical Position**: The Unified Biquaternion Theory (UBT) **generalizes and embeds** Einstein's General Relativity—it does not contradict or replace it. This is a fundamental aspect of the theory that must be preserved in all documentation and code comments.

Key principles:
- **GR is fully contained within UBT**: In the real-valued limit (when imaginary time component ψ → 0), UBT exactly reproduces Einstein's field equations
- **All curvature regimes**: This compatibility holds for flat spacetime (Minkowski), weak fields, strong fields (black holes, neutron stars), and cosmological solutions with R ≠ 0
- **Extended structure**: UBT introduces additional biquaternionic degrees of freedom representing phase curvature and nonlocal energy configurations
- **Invisibility**: These imaginary components remain invisible to classical observations because ordinary matter couples only to the real metric g_μν
- **Experimental validation**: All confirmations of GR (perihelion precession, gravitational waves, etc.) automatically validate UBT's real sector

Language guidelines:
- ✅ Use: "UBT generalizes GR", "UBT embeds GR", "UBT extends GR", "recovers Einstein's equations"
- ❌ Avoid: "alternative to GR", "replacement of GR", "contradiction with GR"
- When discussing invisibility or phase curvature, clarify these arise from imaginary components of the biquaternionic metric

Mathematical statement: The core field equation ∇†∇Θ(q,τ) = κ𝒯(q,τ) reduces to R_μν - ½g_μν R = 8πG T_μν in the real limit.

See appendix_R_GR_equivalence.tex for detailed derivation.

### Novel Concepts
- **Biquaternions**: Mathematical framework combining quaternions with complex coefficients
- **Complex Time**: Extension of real time to complex plane
- **Psychons**: Quantum excitations of consciousness fields
- **Closed Timelike Curves (CTCs)**: Time-travel solutions in UBT metric
- **Theta Resonator**: Proposed experimental device for consciousness detection

### Mathematical Rigor
- Maintain consistency with established physics notation
- Clearly state assumptions and approximations
- Provide derivations for non-obvious results
- Reference standard texts where applicable

## Git Workflow

### Branch Naming
- Use descriptive names: `feature/<feature-name>`, `fix/<issue-description>`
- Keep branches focused on specific tasks

### Commit Messages
- Use conventional commits format when appropriate
- Be descriptive: explain what changed and why
- For LaTeX: mention document/section being modified
- For scripts: mention computational purpose

### Pull Requests
- Ensure LaTeX documents compile successfully
- Check that PDFs are generated correctly in CI/CD
- Include context about theoretical changes

## Code Quality

### LaTeX
- **Consistency**: Follow existing document structure and notation
- **Compilation**: Always ensure documents compile without errors
- **References**: Use proper BibTeX citations for academic work
- **Figures**: Store images in appropriate `img/` directories
- **Labels**: Use consistent labeling scheme for equations, figures, tables

### Python
- **Functionality**: Ensure scripts produce correct numerical results
- **Comments**: Explain theoretical basis of calculations
- **Testing**: Validate results against known limits or analytical solutions
- **Error Handling**: Handle edge cases in numerical computations

## Documentation

### When Adding New Content
- **LaTeX Documents**: Provide context in document introduction
- **Appendices**: Create new appendix files following existing naming convention
- **Python Scripts**: Include header comment explaining purpose and theory
- **Figures**: Use descriptive filenames and captions

### Comments
- Explain non-obvious mathematical transformations
- Reference equations or sections when relevant
- Clarify physical interpretation of mathematical results
- Note any approximations or simplifications

## Common Tasks

### Adding a New LaTeX Document
1. Create `.tex` file with `\documentclass`
2. Follow existing document structure
3. Ensure it compiles locally
4. GitHub Actions will automatically build it on push

### Adding a New Mathematical Derivation
1. Place in appropriate section or appendix
2. Use consistent notation with existing documents
3. Provide intermediate steps for clarity
4. Reference relevant equations

### Adding a New Python Script
1. Place in `consolidation_project/scripts/` or appropriate subdirectory
2. Include docstring explaining theoretical purpose
3. Add usage example in comments
4. Validate numerical results

### Modifying Build Process
1. Test changes locally first
2. Update Makefile if needed
3. Ensure GitHub Actions workflow remains functional
4. Check that PDFs are generated correctly

## Testing and Validation

### LaTeX Documents
- **Compilation Test**: Document must compile without errors
- **Visual Inspection**: Check generated PDF for formatting issues
- **References**: Verify all citations resolve correctly
- **Equations**: Check numbering and cross-references

### Python Scripts
- **Output Validation**: Compare results with known theoretical values
- **Edge Cases**: Test boundary conditions and special cases
- **Numerical Stability**: Verify convergence and precision
- **Documentation**: Ensure usage is clear from code and comments

## Special Considerations

### Research Priority Areas
Refer to `RESEARCH_PRIORITIES.md` for current focus areas:
1. Formal consolidation of UBT core equations
2. Padic extensions and dark sector physics
3. Psychon dynamics in complex time
4. Closed Timelike Curve (CTC) solutions
5. Electromagnetism in curved space
6. Experimental design: Theta Resonator
7. Complex Consciousness Theory integration

### Academic Integrity
- This is original research by David Jaroš
- Maintain proper attribution for any external sources
- Use academic citation standards
- Respect intellectual property in all contributions

### Theoretical Consistency
- New additions should be compatible with existing UBT framework
- Maintain mathematical rigor in all derivations
- Clearly state when introducing speculative concepts
- Validate against known physics in appropriate limits

## Getting Help

- **Issues**: Check existing GitHub issues for known problems
- **Documentation**: Refer to README.md and RESEARCH_PRIORITIES.md
- **Structure**: Examine existing documents for formatting examples
- **Build Problems**: Check `.github/workflows/latex_build.yml` for build configuration
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
