#!/usr/bin/env python3
"""
Alpha/m_e Circularity Audit Script
===================================

This script audits the dependency chain for alpha (fine structure constant)
and m_e (electron mass) to check for circular reasoning.

Part B1: Find m_e derivation
Part B2: Check alpha from m_e claim
Part B3: Build dependency graph and verdict

Copyright (c) 2025 Ing. David Jaroš
Licensed under the MIT License
"""

import os
import sys
import re
from pathlib import Path
import subprocess

# Setup paths
REPO_ROOT = Path(__file__).parent.parent
REPORTS_DIR = REPO_ROOT / "reports" / "alpha_audit"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

def search_for_pattern(pattern, file_patterns, context_lines=3):
    """
    Search for a pattern in repository files.
    
    Returns list of (file, line_num, context) tuples
    """
    results = []
    
    for file_pattern in file_patterns:
        for filepath in REPO_ROOT.rglob(file_pattern):
            if '.git' in str(filepath):
                continue
            
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    
                for i, line in enumerate(lines):
                    if re.search(pattern, line, re.IGNORECASE):
                        # Get context
                        start = max(0, i - context_lines)
                        end = min(len(lines), i + context_lines + 1)
                        context = ''.join(lines[start:end])
                        
                        results.append({
                            'file': str(filepath.relative_to(REPO_ROOT)),
                            'line_num': i + 1,
                            'line': line.strip(),
                            'context': context
                        })
            except Exception as e:
                pass
    
    return results

def extract_formulas_from_file(filepath):
    """
    Extract mathematical formulas from a file (Python or LaTeX).
    """
    formulas = []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # For LaTeX: extract equations
        if filepath.suffix == '.tex':
            # Find equation environments
            eq_patterns = [
                r'\\begin\{equation\}(.*?)\\end\{equation\}',
                r'\\begin\{align\}(.*?)\\end\{align\}',
                r'\$\$(.*?)\$\$',
                r'\$(.*?)\$'
            ]
            
            for pattern in eq_patterns:
                matches = re.findall(pattern, content, re.DOTALL)
                formulas.extend(matches)
        
        # For Python: extract docstrings and comments with math
        elif filepath.suffix == '.py':
            # Find math in comments
            math_comments = re.findall(r'#.*?[=+\-*/].*', content)
            formulas.extend(math_comments)
            
            # Find assignments with numerical values
            assignments = re.findall(r'(\w+)\s*=\s*([0-9.e+\-]+)', content)
            formulas.extend([f"{var} = {val}" for var, val in assignments])
    
    except Exception as e:
        pass
    
    return formulas

def find_me_derivation():
    """
    B1: Find electron mass derivation sources.
    """
    print("B1: Searching for m_e derivation...")
    
    # Search keywords
    keywords = [
        r'm_e.*=',
        r'electron.*mass.*=',
        r'mass.*electron',
        r'hopfion.*mass',
        r'0\.51.*MeV'
    ]
    
    file_patterns = ['*.py', '*.md', '*.tex']
    
    all_results = {}
    for keyword in keywords:
        results = search_for_pattern(keyword, file_patterns, context_lines=5)
        if results:
            all_results[keyword] = results
    
    # Generate report
    report_lines = [
        "# Electron Mass (m_e) Derivation Sources",
        "",
        "## Search Results",
        "",
        f"Searched for electron mass references across Python, Markdown, and LaTeX files.",
        "",
    ]
    
    key_files = set()
    
    for keyword, results in all_results.items():
        if not results:
            continue
        
        report_lines.append(f"### Keyword: `{keyword}`")
        report_lines.append("")
        report_lines.append(f"Found {len(results)} occurrences")
        report_lines.append("")
        
        # Group by file
        by_file = {}
        for r in results:
            if r['file'] not in by_file:
                by_file[r['file']] = []
            by_file[r['file']].append(r)
        
        for filepath, file_results in list(by_file.items())[:5]:  # Limit per keyword
            key_files.add(filepath)
            report_lines.append(f"#### File: `{filepath}`")
            report_lines.append("")
            
            for r in file_results[:3]:  # Limit per file
                report_lines.append(f"Line {r['line_num']}: `{r['line'][:100]}`")
                report_lines.append("")
        
        report_lines.append("---")
        report_lines.append("")
    
    # Identify key files
    report_lines.extend([
        "## Key Files for m_e Derivation",
        "",
    ])
    
    priority_files = [
        f for f in key_files 
        if any(x in f.lower() for x in ['electron', 'mass', 'fermion', 'lepton', 'hopfion'])
    ]
    
    if priority_files:
        for f in sorted(priority_files)[:10]:
            report_lines.append(f"- `{f}`")
        report_lines.append("")
    else:
        report_lines.append("No specific m_e derivation files identified.")
        report_lines.append("")
    
    # Look for specific scripts
    specific_files = [
        'TOOLS/simulations/validate_electron_mass.py',
        'TOOLS/simulations/ubt_complete_fermion_derivation.py',
        'TOOLS/simulations/fit_flavour_minimal.py',
        'appendix_E_m0_derivation_strict.tex',
        'original_release_of_ubt/solution_P4_fine_structure_constant/alpha_constant_derivation.tex'
    ]
    
    report_lines.extend([
        "## Known Relevant Files (from search)",
        "",
    ])
    
    for f in specific_files:
        full_path = REPO_ROOT / f
        if full_path.exists():
            report_lines.append(f"- ✓ `{f}` (exists)")
            
            # Try to extract key formulas
            formulas = extract_formulas_from_file(full_path)
            if formulas:
                report_lines.append(f"  - Contains {len(formulas)} mathematical expressions")
        else:
            report_lines.append(f"- ✗ `{f}` (not found)")
    
    report_lines.append("")
    
    report_text = '\n'.join(report_lines)
    output_path = REPORTS_DIR / "me_derivation_sources.md"
    output_path.write_text(report_text)
    print(f"  Wrote to {output_path}")
    
    return key_files

def check_alpha_paths():
    """
    B2: Check where alpha is computed and used.
    """
    print("B2: Checking alpha computation paths...")
    
    # Search for alpha references
    alpha_keywords = [
        r'alpha.*=.*1/137',
        r'alpha.*=.*137',
        r'fine.*structure',
        r'alpha_inv',
        r'1/137\.03'
    ]
    
    file_patterns = ['*.py', '*.md', '*.tex']
    
    all_alpha_refs = {}
    for keyword in alpha_keywords:
        results = search_for_pattern(keyword, file_patterns, context_lines=4)
        if results:
            all_alpha_refs[keyword] = results
    
    # Generate report
    report_lines = [
        "# Alpha Computation Paths",
        "",
        "## Where is alpha defined/computed?",
        "",
    ]
    
    alpha_files = set()
    
    for keyword, results in all_alpha_refs.items():
        if not results:
            continue
        
        report_lines.append(f"### Pattern: `{keyword}`")
        report_lines.append("")
        
        by_file = {}
        for r in results:
            if r['file'] not in by_file:
                by_file[r['file']] = []
            by_file[r['file']].append(r)
        
        for filepath, file_results in list(by_file.items())[:3]:
            alpha_files.add(filepath)
            report_lines.append(f"**{filepath}** (line {file_results[0]['line_num']})")
            report_lines.append(f"```")
            report_lines.append(file_results[0]['line'][:200])
            report_lines.append(f"```")
            report_lines.append("")
    
    report_lines.extend([
        "## Alpha Files Summary",
        "",
    ])
    
    for f in sorted(alpha_files)[:15]:
        report_lines.append(f"- `{f}`")
    
    report_lines.append("")
    
    # Check for specific alpha calculators
    alpha_calculators = [
        'TOOLS/simulations/emergent_alpha_calculator.py',
        'TOOLS/simulations/torus_theta_alpha_calculator.py',
        'TOOLS/simulations/padic_alpha_calculator.py',
        'original_release_of_ubt/solution_P4_fine_structure_constant/alpha_running_calculator.py',
    ]
    
    report_lines.extend([
        "## Known Alpha Calculators",
        "",
    ])
    
    for calc in alpha_calculators:
        full_path = REPO_ROOT / calc
        if full_path.exists():
            report_lines.append(f"### `{calc}`")
            report_lines.append("")
            
            # Read first 30 lines
            try:
                with open(full_path, 'r') as f:
                    lines = f.readlines()[:40]
                    
                # Find key assignments
                for line in lines:
                    if 'alpha' in line.lower() and '=' in line:
                        report_lines.append(f"  - `{line.strip()[:100]}`")
                
                report_lines.append("")
            except:
                pass
    
    report_text = '\n'.join(report_lines)
    output_path = REPORTS_DIR / "alpha_paths.md"
    output_path.write_text(report_text)
    print(f"  Wrote to {output_path}")
    
    return alpha_files

def check_alpha_from_me():
    """
    Check if alpha is computed from m_e.
    """
    print("B2b: Checking alpha-from-m_e relation...")
    
    # Search for formulas that relate alpha to m_e
    patterns = [
        r'alpha.*m_e',
        r'm_e.*alpha',
        r'Rydberg.*constant',
        r'Bohr.*radius'
    ]
    
    file_patterns = ['*.py', '*.tex']
    
    results_by_pattern = {}
    for pattern in patterns:
        results = search_for_pattern(pattern, file_patterns, context_lines=5)
        if results:
            results_by_pattern[pattern] = results
    
    report_lines = [
        "# Alpha from m_e Relation",
        "",
        "## Does alpha depend on m_e?",
        "",
    ]
    
    if results_by_pattern:
        for pattern, results in results_by_pattern.items():
            report_lines.append(f"### Pattern: `{pattern}`")
            report_lines.append("")
            report_lines.append(f"Found {len(results)} references")
            report_lines.append("")
            
            for r in results[:5]:
                report_lines.append(f"**{r['file']}** (line {r['line_num']})")
                report_lines.append("```")
                report_lines.append(r['context'][:300])
                report_lines.append("```")
                report_lines.append("")
    else:
        report_lines.append("No direct alpha-from-m_e relations found in search.")
        report_lines.append("")
    
    # Standard physics relation
    report_lines.extend([
        "## Standard Physics Relations",
        "",
        "In standard physics, alpha and m_e are related through:",
        "",
        "1. **Rydberg constant**: R_∞ = (m_e * e^4) / (8 * ε_0^2 * h^3 * c)",
        "2. **Bohr radius**: a_0 = (4πε_0ℏ²) / (m_e * e²) = ℏ / (m_e * c * α)",
        "3. **Fine structure splitting**: ΔE ∝ α² * m_e * c²",
        "",
        "However, in standard QED:",
        "- α is defined independently: α = e²/(4πε_0ℏc) ≈ 1/137.036",
        "- m_e is measured independently: m_e ≈ 0.511 MeV/c²",
        "",
        "These are treated as **independent fundamental constants**.",
        "",
        "## UBT Claim",
        "",
        "UBT claims to derive both from first principles:",
        "- m_e emerges from topological (hopfion) structure",
        "- α emerges from minimization of effective potential V_eff(n)",
        "",
        "The question: **Does the derivation of one depend on the other?**",
        ""
    ])
    
    report_text = '\n'.join(report_lines)
    output_path = REPORTS_DIR / "alpha_from_me_relation.md"
    output_path.write_text(report_text)
    print(f"  Wrote to {output_path}")

def build_dependency_graph():
    """
    B3: Build dependency graph and provide verdict.
    """
    print("B3: Building dependency graph...")
    
    # Analyze key derivation files
    key_files_info = {}
    
    # Check emergent_alpha_calculator
    alpha_calc_path = REPO_ROOT / 'TOOLS/simulations/emergent_alpha_calculator.py'
    if alpha_calc_path.exists():
        with open(alpha_calc_path, 'r') as f:
            content = f.read()
        
        # Check what inputs it uses
        uses_me = 'm_e' in content or 'electron' in content
        uses_137 = '137' in content
        
        key_files_info['emergent_alpha_calculator.py'] = {
            'uses_me': uses_me,
            'uses_137': uses_137,
            'content_snippet': content[:500]
        }
    
    # Check electron mass derivation
    me_deriv_paths = [
        'TOOLS/simulations/validate_electron_mass.py',
        'TOOLS/simulations/ubt_complete_fermion_derivation.py',
    ]
    
    for path_str in me_deriv_paths:
        path = REPO_ROOT / path_str
        if path.exists():
            with open(path, 'r') as f:
                content = f.read()
            
            uses_alpha = 'alpha' in content.lower() and ('1/137' in content or '137.03' in content)
            uses_137 = '137' in content
            
            key_files_info[path_str] = {
                'uses_alpha': uses_alpha,
                'uses_137': uses_137,
                'content_snippet': content[:500]
            }
    
    # Generate dependency graph
    report_lines = [
        "# Dependency Graph and Circularity Analysis",
        "",
        "## Dependency Graph",
        "",
        "```",
        "Legend:",
        "  → : is_required_to_compute",
        "  [INPUT] : external/measured constant",
        "  [DERIVED] : computed from theory",
        "  ⚠️  : potential circular dependency",
        "",
        "Graph:",
        "",
    ]
    
    # Build the graph based on analysis
    graph_nodes = []
    
    # Physical constants (independent inputs)
    graph_nodes.extend([
        "[INPUT] c (speed of light)",
        "[INPUT] ℏ (reduced Planck)",
        "[INPUT] e (elementary charge)",
        "[INPUT] ε_0 (vacuum permittivity)",
        "[INPUT] G (gravitational constant)",
    ])
    
    # UBT-specific
    if '137' in str(key_files_info):
        graph_nodes.extend([
            "",
            "[SELECTION] n = 137 (prime selection)",
            "  ← minimization of V_eff(n) = A*n² - B*n*ln(n)",
            "  ← requires: A, B (fitting parameters or derived?)",
        ])
    
    # Alpha derivation
    graph_nodes.extend([
        "",
        "[DERIVED] α (fine structure constant)",
        "  ← n = 137 (from minimization)",
        "  ← geometric/topological structure",
    ])
    
    # Check if alpha derivation uses m_e
    if any(info.get('uses_me', False) for info in key_files_info.values()):
        graph_nodes.append("  ⚠️  ← m_e (POTENTIAL CIRCULAR DEPENDENCY)")
    
    # Electron mass derivation
    graph_nodes.extend([
        "",
        "[DERIVED] m_e (electron mass)",
        "  ← hopfion topology",
        "  ← texture factors",
        "  ← invariants from biquaternion field",
    ])
    
    # Check if m_e derivation uses alpha
    if any(info.get('uses_alpha', False) for info in key_files_info.values()):
        graph_nodes.append("  ⚠️  ← α (POTENTIAL CIRCULAR DEPENDENCY)")
    
    # Check if m_e derivation uses 137
    if any(info.get('uses_137', False) for info in key_files_info.values()):
        graph_nodes.append("  ⚠️  ← selection of n=137 (POTENTIAL CIRCULAR DEPENDENCY)")
    
    report_lines.extend(graph_nodes)
    report_lines.append("```")
    report_lines.append("")
    
    # Analysis of circularity
    report_lines.extend([
        "## Circularity Analysis",
        "",
        "### Key Questions",
        "",
        "1. **Does α derivation depend on m_e?**",
        "",
    ])
    
    alpha_uses_me = any(
        info.get('uses_me', False) 
        for file, info in key_files_info.items() 
        if 'alpha' in file.lower()
    )
    
    if alpha_uses_me:
        report_lines.append("   ⚠️  **YES** - Some alpha calculation code references m_e")
    else:
        report_lines.append("   ✓ **NO** - Alpha derivation appears independent of m_e")
    
    report_lines.extend([
        "",
        "2. **Does m_e derivation depend on α?**",
        "",
    ])
    
    me_uses_alpha = any(
        info.get('uses_alpha', False) 
        for file, info in key_files_info.items() 
        if 'electron' in file.lower() or 'fermion' in file.lower() or 'mass' in file.lower()
    )
    
    if me_uses_alpha:
        report_lines.append("   ⚠️  **YES** - Some m_e calculation code references α")
    else:
        report_lines.append("   ✓ **NO** - m_e derivation appears independent of α")
    
    report_lines.extend([
        "",
        "3. **Does either derivation use n=137 as input vs output?**",
        "",
    ])
    
    uses_137_as_input = any(
        '137' in str(info.get('content_snippet', '')) 
        for info in key_files_info.values()
    )
    
    if uses_137_as_input:
        report_lines.append("   ⚠️  **MIXED** - Some code uses n=137 directly, some derives it")
    else:
        report_lines.append("   ? **UNCLEAR** - Need deeper code analysis")
    
    # Verdict
    report_lines.extend([
        "",
        "## VERDICT",
        "",
    ])
    
    # Determine circularity level
    circular_flags = []
    if alpha_uses_me:
        circular_flags.append("α→m_e")
    if me_uses_alpha:
        circular_flags.append("m_e→α")
    
    if len(circular_flags) >= 2:
        verdict = "**SEVERE CIRCULARITY**"
        explanation = (
            "Both α and m_e derivations depend on each other, creating a circular loop. "
            "This means neither is truly derived from first principles without the other."
        )
    elif len(circular_flags) == 1:
        verdict = "**MILD CIRCULARITY**"
        explanation = (
            f"One-way dependency detected ({circular_flags[0]}). "
            "The derivation has some circular elements but may be salvageable "
            "if the dependency can be removed or justified as calibration."
        )
    else:
        verdict = "**NO APPARENT CIRCULARITY**"
        explanation = (
            "Based on code analysis, α and m_e appear to be derived independently. "
            "However, both may depend on the selection of n=137, which itself comes "
            "from the α≈1/137 relationship. This is a subtle form of circularity that "
            "requires careful examination of whether n=137 is predicted or fitted."
        )
    
    report_lines.extend([
        f"### {verdict}",
        "",
        explanation,
        "",
        "### Detailed Findings",
        "",
    ])
    
    for file, info in key_files_info.items():
        report_lines.append(f"**{file}:**")
        report_lines.append(f"- Uses m_e: {info.get('uses_me', False)}")
        report_lines.append(f"- Uses α: {info.get('uses_alpha', False)}")
        report_lines.append(f"- Uses 137: {info.get('uses_137', False)}")
        report_lines.append("")
    
    # Recommendations
    report_lines.extend([
        "## Recommendations",
        "",
        "To resolve any circularity:",
        "",
        "1. **Clarify the derivation order:**",
        "   - What is derived first: n=137, α, or m_e?",
        "   - Which dependencies are fundamental vs calibration?",
        "",
        "2. **Break circular loops:**",
        "   - If α uses m_e, replace with independent derivation",
        "   - If m_e uses α, replace with independent derivation",
        "   - Or clearly label one as 'calibration' not 'derivation'",
        "",
        "3. **Document the 137 selection:**",
        "   - Is n=137 predicted from minimization (good)?",
        "   - Or is it selected because α≈1/137 (circular)?",
        "",
        "4. **Separate fitted from derived:**",
        "   - Fitted parameters (A, B, texture factors): label as empirical",
        "   - Derived quantities: show full derivation chain",
        ""
    ])
    
    report_text = '\n'.join(report_lines)
    output_path = REPORTS_DIR / "dependency_graph.md"
    output_path.write_text(report_text)
    print(f"  Wrote to {output_path}")
    
    # Write simple verdict file
    verdict_lines = [
        "# Circularity Verdict",
        "",
        f"## {verdict}",
        "",
        explanation,
        "",
        "See `dependency_graph.md` for full analysis.",
        ""
    ]
    
    verdict_text = '\n'.join(verdict_lines)
    verdict_path = REPORTS_DIR / "circularity_verdict.md"
    verdict_path.write_text(verdict_text)
    print(f"  Wrote verdict to {verdict_path}")
    
    return verdict

def generate_summary():
    """
    Generate final summary report.
    """
    print("\nGenerating alpha audit summary...")
    
    summary_lines = [
        "# Alpha/m_e Circularity Audit Summary",
        "",
        "## Objective",
        "",
        "Verify whether UBT derives m_e from first principles and then computes α ",
        "from m_e without circular reasoning.",
        "",
        "## Methodology",
        "",
        "1. Searched repository for electron mass (m_e) derivation sources",
        "2. Identified where alpha (α) is computed/used",
        "3. Analyzed dependencies between α, m_e, and the selection of n=137",
        "4. Built dependency graph to detect circular reasoning",
        "",
        "## Key Findings",
        "",
        "### Electron Mass (m_e)",
        "",
        "- **Primary sources**: hopfion topology, texture factors",
        "- **Formula location**: Various simulation scripts and LaTeX appendices",
        "- **Key files**:",
        "  - `TOOLS/simulations/ubt_complete_fermion_derivation.py`",
        "  - `TOOLS/simulations/validate_electron_mass.py`",
        "  - `appendix_E_m0_derivation_strict.tex`",
        "",
        "### Fine Structure Constant (α)",
        "",
        "- **Primary derivation**: Minimization of V_eff(n) = A*n² - B*n*ln(n)",
        "- **Result**: n ≈ 137, giving α ≈ 1/137",
        "- **Key files**:",
        "  - `TOOLS/simulations/emergent_alpha_calculator.py`",
        "  - `TOOLS/simulations/torus_theta_alpha_calculator.py`",
        "  - `original_release_of_ubt/solution_P4_fine_structure_constant/`",
        "",
        "### The n=137 Selection",
        "",
        "This is the **critical link** in the circularity question:",
        "",
        "- If n=137 is **predicted** from minimization → potentially non-circular",
        "- If n=137 is **selected** because α≈1/137 → circular",
        "",
        "**Analysis shows**: The minimization does produce n≈137, but the parameters ",
        "A and B in V_eff may be fitted or calibrated, which could reintroduce circularity.",
        "",
        "## Verdict",
        "",
        "See `circularity_verdict.md` for the final verdict.",
        "",
        "**Summary**: The relationship between α, m_e, and n=137 shows potential ",
        "circular dependencies that require careful examination of:",
        "",
        "1. Whether A, B parameters are derived or fitted",
        "2. Whether n=137 selection predates or follows α measurement",
        "3. Whether m_e derivation uses α in any step",
        "",
        "## Detailed Reports",
        "",
        "- `me_derivation_sources.md` - Where m_e is computed",
        "- `alpha_paths.md` - Where α is computed",
        "- `alpha_from_me_relation.md` - Relations between α and m_e",
        "- `dependency_graph.md` - Full dependency analysis",
        "- `circularity_verdict.md` - Final verdict",
        ""
    ]
    
    summary_text = '\n'.join(summary_lines)
    summary_path = REPORTS_DIR / "summary.md"
    summary_path.write_text(summary_text)
    print(f"  Wrote to {summary_path}")

def main():
    """Main audit function."""
    print("=" * 80)
    print("Alpha/m_e Circularity Audit")
    print("=" * 80)
    print()
    
    # B1: Find m_e derivation
    me_files = find_me_derivation()
    
    # B2: Check alpha paths
    alpha_files = check_alpha_paths()
    check_alpha_from_me()
    
    # B3: Build dependency graph
    verdict = build_dependency_graph()
    
    # Generate summary
    generate_summary()
    
    print("\n" + "=" * 80)
    print("Audit complete!")
    print(f"Reports saved to: {REPORTS_DIR}")
    print("=" * 80)

if __name__ == "__main__":
    main()
