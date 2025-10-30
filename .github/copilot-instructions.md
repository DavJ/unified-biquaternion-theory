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
- **Primary Use**: Numerical computations, fine structure constant calculations, p-adic extensions
- **Key Scripts**:
  - `alpha_running_calculator.py` - Fine structure constant calculations
  - `alpha_p_computation.py` - P-adic computations
  - Various LaTeX manipulation scripts

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
- **Dark Sector**: Dark matter and dark energy via p-adic extensions

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
2. P-adic extensions and dark sector physics
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
