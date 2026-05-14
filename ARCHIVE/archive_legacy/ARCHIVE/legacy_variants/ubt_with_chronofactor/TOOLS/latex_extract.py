#!/usr/bin/env python3
"""
LaTeX Equation Extractor
=========================

Extracts equations, definitions, and symbols from LaTeX files in the UBT repository.
Focus on alpha-related content for rigorous verification.

Author: UBT Team
Version: 1.0
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any, Set


# Key terms for filtering relevant equations
ALPHA_TERMS = [
    r'\balpha\b',
    r'\\alpha',
    r'fine.structure',
    r'\bB\s*=',
    r'R_\\psi',
    r'R_psi',
    r'N_\\mathrm\{eff\}',
    r'N_eff',
    r'\\mathcal\{R\}_\{UBT\}',
    r'Ward',
    r'Z_1.*Z_2',
    r'QED.*limit',
    r'\\psi.*0',
    r'CT.*scheme',
    r'two.loop',
]


def extract_equations(filepath: Path, filter_terms: List[str] = None) -> List[Dict[str, Any]]:
    """
    Extract equation environments from a LaTeX file.
    
    Args:
        filepath: Path to .tex file
        filter_terms: Optional list of regex patterns to filter equations
        
    Returns:
        List of equation dictionaries
    """
    equations = []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Extract equation environments
        # Patterns: \begin{equation}...\end{equation}, \[...\], $...$ (displayed)
        
        # 1. equation environment
        eq_pattern = r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}'
        for match in re.finditer(eq_pattern, content, re.DOTALL):
            eq_content = match.group(1).strip()
            
            # Check for label
            label_match = re.search(r'\\label\{([^}]+)\}', eq_content)
            label = label_match.group(1) if label_match else None
            
            # Filter by terms if specified
            if filter_terms:
                if not any(re.search(term, eq_content, re.IGNORECASE) for term in filter_terms):
                    continue
            
            # Find line number
            lineno = content[:match.start()].count('\n') + 1
            
            equations.append({
                'type': 'equation',
                'content': eq_content,
                'label': label,
                'path': str(filepath),
                'lineno': lineno,
            })
        
        # 2. align environment
        align_pattern = r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}'
        for match in re.finditer(align_pattern, content, re.DOTALL):
            eq_content = match.group(1).strip()
            
            # Check for labels
            labels = re.findall(r'\\label\{([^}]+)\}', eq_content)
            
            # Filter by terms
            if filter_terms:
                if not any(re.search(term, eq_content, re.IGNORECASE) for term in filter_terms):
                    continue
            
            lineno = content[:match.start()].count('\n') + 1
            
            equations.append({
                'type': 'align',
                'content': eq_content,
                'labels': labels if labels else None,
                'path': str(filepath),
                'lineno': lineno,
            })
        
        # 3. gather environment
        gather_pattern = r'\\begin\{gather\*?\}(.*?)\\end\{gather\*?\}'
        for match in re.finditer(gather_pattern, content, re.DOTALL):
            eq_content = match.group(1).strip()
            labels = re.findall(r'\\label\{([^}]+)\}', eq_content)
            
            if filter_terms:
                if not any(re.search(term, eq_content, re.IGNORECASE) for term in filter_terms):
                    continue
            
            lineno = content[:match.start()].count('\n') + 1
            
            equations.append({
                'type': 'gather',
                'content': eq_content,
                'labels': labels if labels else None,
                'path': str(filepath),
                'lineno': lineno,
            })
        
        # 4. Display math \[...\]
        display_pattern = r'\\\[(.*?)\\\]'
        for match in re.finditer(display_pattern, content, re.DOTALL):
            eq_content = match.group(1).strip()
            
            if filter_terms:
                if not any(re.search(term, eq_content, re.IGNORECASE) for term in filter_terms):
                    continue
            
            lineno = content[:match.start()].count('\n') + 1
            
            equations.append({
                'type': 'displaymath',
                'content': eq_content,
                'label': None,
                'path': str(filepath),
                'lineno': lineno,
            })
        
        # 5. Theorem, Lemma, Proposition environments (capture labels)
        theorem_envs = ['theorem', 'lemma', 'proposition', 'corollary', 'definition']
        for env in theorem_envs:
            thm_pattern = rf'\\begin\{{{env}\*?\}}(.*?)\\end\{{{env}\*?\}}'
            for match in re.finditer(thm_pattern, content, re.DOTALL):
                thm_content = match.group(1).strip()
                
                # Extract label
                label_match = re.search(r'\\label\{([^}]+)\}', thm_content)
                label = label_match.group(1) if label_match else None
                
                # Filter by terms if specified
                if filter_terms:
                    if not any(re.search(term, thm_content, re.IGNORECASE) for term in filter_terms):
                        # Also check the label
                        if not (label and any(re.search(term, label, re.IGNORECASE) for term in filter_terms)):
                            continue
                
                lineno = content[:match.start()].count('\n') + 1
                
                equations.append({
                    'type': env,
                    'content': thm_content,
                    'label': label,
                    'path': str(filepath),
                    'lineno': lineno,
                })
    
    except Exception as e:
        print(f"Warning: Could not process {filepath}: {e}")
    
    return equations


def extract_definitions(filepath: Path, filter_terms: List[str] = None) -> List[Dict[str, Any]]:
    """
    Extract definitions and symbol declarations from LaTeX.
    
    Looks for patterns like:
    - "Let X be defined as..."
    - "Define X := ..."
    - "We set X = ..."
    - \\newcommand{\\X}{...}
    - \\def\\X{...}
    
    Args:
        filepath: Path to .tex file
        filter_terms: Optional list of regex patterns to filter
        
    Returns:
        List of definition dictionaries
    """
    definitions = []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        for lineno, line in enumerate(lines, 1):
            # Pattern 1: "Let X be" / "Define X" / "We set X"
            def_patterns = [
                r'(Let\s+\\?[\w_]+.*?be\s+defined)',
                r'(Define\s+\\?[\w_]+\s*:?=)',
                r'(We\s+set\s+\\?[\w_]+\s*=)',
                r'(where\s+\\?[\w_]+\s+is\s+defined)',
            ]
            
            for pattern in def_patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    # Filter by terms
                    if filter_terms:
                        if not any(re.search(term, line, re.IGNORECASE) for term in filter_terms):
                            continue
                    
                    definitions.append({
                        'type': 'definition_text',
                        'content': line.strip(),
                        'path': str(filepath),
                        'lineno': lineno,
                    })
                    break
            
            # Pattern 2: \\newcommand
            newcmd_match = re.search(r'\\newcommand\{(\\[\w]+)\}\{([^}]+)\}', line)
            if newcmd_match:
                symbol = newcmd_match.group(1)
                definition = newcmd_match.group(2)
                
                if filter_terms:
                    combined = symbol + definition
                    if not any(re.search(term, combined, re.IGNORECASE) for term in filter_terms):
                        continue
                
                definitions.append({
                    'type': 'newcommand',
                    'symbol': symbol,
                    'definition': definition,
                    'path': str(filepath),
                    'lineno': lineno,
                })
            
            # Pattern 3: \\def
            def_match = re.search(r'\\def(\\[\w]+)\{([^}]+)\}', line)
            if def_match:
                symbol = def_match.group(1)
                definition = def_match.group(2)
                
                if filter_terms:
                    combined = symbol + definition
                    if not any(re.search(term, combined, re.IGNORECASE) for term in filter_terms):
                        continue
                
                definitions.append({
                    'type': 'def',
                    'symbol': symbol,
                    'definition': definition,
                    'path': str(filepath),
                    'lineno': lineno,
                })
    
    except Exception as e:
        print(f"Warning: Could not process {filepath}: {e}")
    
    return definitions


def scan_latex_files(root: Path, filter_terms: List[str] = None) -> Dict[str, Any]:
    """
    Scan all LaTeX files in repository.
    
    Args:
        root: Root directory
        filter_terms: Optional filter terms
        
    Returns:
        Dictionary with equations and definitions
    """
    all_equations = []
    all_definitions = []
    
    for tex_file in root.rglob('*.tex'):
        # Skip excluded directories
        if any(skip in tex_file.parts for skip in {'.git', '__pycache__'}):
            continue
        
        equations = extract_equations(tex_file, filter_terms)
        definitions = extract_definitions(tex_file, filter_terms)
        
        all_equations.extend(equations)
        all_definitions.extend(definitions)
    
    return {
        'equations': all_equations,
        'definitions': all_definitions,
    }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Extract equations and definitions from LaTeX files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument('--root', type=str, default='.',
                       help='Root directory to scan (default: .)')
    parser.add_argument('--out', type=str, default='reports/alpha_equations.json',
                       help='Output JSON file (default: reports/alpha_equations.json)')
    parser.add_argument('--filter', action='store_true',
                       help='Filter for alpha-related terms only')
    
    args = parser.parse_args()
    
    root = Path(args.root).resolve()
    out_file = Path(args.out)
    filter_terms = ALPHA_TERMS if args.filter else None
    
    print("=" * 70)
    print("UBT LaTeX Equation Extractor")
    print("=" * 70)
    print()
    print(f"Root directory: {root}")
    print(f"Output file: {out_file}")
    print(f"Filtering: {'Yes (alpha-related only)' if filter_terms else 'No (all equations)'}")
    print()
    
    # Scan files
    print("Scanning LaTeX files...")
    results = scan_latex_files(root, filter_terms)
    
    num_equations = len(results['equations'])
    num_definitions = len(results['definitions'])
    
    print(f"Found {num_equations} equations")
    print(f"Found {num_definitions} definitions")
    print()
    
    # Create output directory
    out_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write results
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"Results written to: {out_file}")
    print()
    
    # Summary
    eq_labels = [eq.get('label') or eq.get('labels') for eq in results['equations']]
    eq_labels = [l for l in eq_labels if l]
    
    print("Summary:")
    print(f"  Equations with labels: {len(eq_labels)}")
    print(f"  Total definitions: {num_definitions}")
    print()
    
    print("=" * 70)
    print("Extraction complete")
    print("=" * 70)


if __name__ == '__main__':
    main()
