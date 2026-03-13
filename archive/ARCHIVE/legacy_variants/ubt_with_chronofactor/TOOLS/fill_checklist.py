#!/usr/bin/env python3
"""
Fill Alpha Checklist
====================

Automatically fills the alpha derivation checklist using data from
alpha_audit.py and latex_extract.py outputs.

Author: UBT Team
Version: 1.0
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional


def load_json(filepath: Path) -> Any:
    """Load JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Could not load {filepath}: {e}")
        return None


def find_references(term: str, hits: List[Dict], equations: List[Dict]) -> List[str]:
    """
    Find references to a specific term in hits and equations.
    
    Returns list of "file:line" references.
    """
    refs = []
    
    # Search in hits
    for hit in hits:
        if re.search(term, hit.get('hit', ''), re.IGNORECASE):
            path = Path(hit['path']).name  # Just filename for brevity
            lineno = hit['lineno']
            refs.append(f"{path}:{lineno}")
    
    # Search in equations
    for eq in equations:
        if re.search(term, eq.get('content', ''), re.IGNORECASE):
            path = Path(eq['path']).name
            lineno = eq['lineno']
            refs.append(f"{path}:{lineno}")
    
    # Return unique references, limited to top 5
    unique_refs = list(set(refs))[:5]
    return unique_refs


def find_lemma_theorem(label_pattern: str, equations: List[Dict]) -> Optional[str]:
    """
    Find lemma or theorem by label pattern.
    
    Returns "file:line" reference if found.
    """
    for eq in equations:
        label = eq.get('label')
        if label and re.search(label_pattern, label, re.IGNORECASE):
            path = Path(eq['path']).name
            lineno = eq['lineno']
            return f"{path}:{lineno}"
    
    return None


def fill_checklist(template_path: Path, output_path: Path, 
                   hits_data: List[Dict], equations_data: Dict) -> None:
    """
    Fill checklist template with automatic references.
    
    Args:
        template_path: Path to template markdown
        output_path: Path to output filled checklist
        hits_data: List of hits from alpha_audit.py
        equations_data: Dict from latex_extract.py
    """
    # Load template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    equations = equations_data.get('equations', [])
    definitions = equations_data.get('definitions', [])
    
    # A1: R_ψ derivation
    rpsi_refs = find_references(r'R_\\psi.*fixed|R_psi.*normalization', hits_data, equations)
    rpsi_answer = "YES" if rpsi_refs else "TODO"
    rpsi_evidence = "\n".join([f"- {ref}" for ref in rpsi_refs]) if rpsi_refs else "No direct references found"
    
    content = re.sub(
        r'(Is R_ψ derived.*?\*\*Answer:\*\*\s*)<!-- TODO.*? -->',
        f'\\1{rpsi_answer} (See: {", ".join(rpsi_refs[:3]) if rpsi_refs else "TODO"})',
        content,
        flags=re.DOTALL
    )
    
    # A1: N_eff determination
    neff_refs = find_references(r'N_eff|N_\{\\mathrm\{eff\}\}|mode.*count', hits_data, equations)
    neff_answer = "YES" if neff_refs else "TODO"
    
    # A2: Ward identity
    ward_ref = find_lemma_theorem(r'thm:ward|ward.*ct', equations)
    ward_answer = "YES" if ward_ref else "TODO"
    ward_evidence = f"- Theorem at {ward_ref}" if ward_ref else "No theorem found"
    
    # A3: QED limit
    qed_ref = find_lemma_theorem(r'lem:qed.*limit|qed.*continuity', equations)
    qed_answer = "YES" if qed_ref else "TODO"
    qed_evidence = f"- Lemma at {qed_ref}" if qed_ref else "No lemma found"
    
    # R_UBT = 1 proof
    rubt_ref = find_lemma_theorem(r'thm:.*RUBT|RUBT.*one|R_UBT.*1', equations)
    rubt_answer = "YES" if rubt_ref else "TODO"
    rubt_evidence = f"- Theorem at {rubt_ref}" if rubt_ref else "No theorem found"
    
    # Overall verdict
    all_yes = all([
        rpsi_refs,
        neff_refs,
        ward_ref,
        qed_ref,
        rubt_ref,
    ])
    
    verdict = "YES" if all_yes else ("PARTIAL" if any([rpsi_refs, neff_refs, ward_ref, qed_ref, rubt_ref]) else "NO")
    
    # Build evidence section
    evidence_section = f"""
**A1 - Geometric Fixation:**
{rpsi_evidence}

**A2 - Ward Identity:**
{ward_evidence}

**A3 - QED Limit:**
{qed_evidence}

**R_UBT Baseline:**
{rubt_evidence}

**N_eff Mode Counting:**
{chr(10).join([f'- {ref}' for ref in neff_refs[:5]])}
"""
    
    # Update timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = re.sub(
        r'(\*\*Last Updated:\*\*\s*)<!-- Auto-filled.*? -->',
        f'\\1{timestamp}',
        content
    )
    
    # Add auto-filled evidence at the end
    if "<!-- AUTO-FILLED EVIDENCE -->" not in content:
        content += f"\n\n## Auto-Filled Evidence Summary\n\n{evidence_section}\n"
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Checklist filled and written to: {output_path}")
    print()
    print(f"Verdict: {verdict}")
    print(f"  R_ψ fixation: {'✓' if rpsi_refs else '✗'}")
    print(f"  N_eff determination: {'✓' if neff_refs else '✗'}")
    print(f"  Ward identity (CT): {'✓' if ward_ref else '✗'}")
    print(f"  QED limit: {'✓' if qed_ref else '✗'}")
    print(f"  R_UBT = 1 proof: {'✓' if rubt_ref else '✗'}")
    print()


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Fill alpha derivation checklist automatically'
    )
    
    parser.add_argument('--template', type=str, 
                       default='reports/templates/alpha_checklist.md',
                       help='Template file (default: reports/templates/alpha_checklist.md)')
    parser.add_argument('--out', type=str,
                       default='reports/alpha_checklist_filled.md',
                       help='Output file (default: reports/alpha_checklist_filled.md)')
    parser.add_argument('--hits', type=str,
                       default='reports/alpha_hits.json',
                       help='Hits JSON from alpha_audit.py')
    parser.add_argument('--equations', type=str,
                       default='reports/alpha_equations.json',
                       help='Equations JSON from latex_extract.py')
    
    args = parser.parse_args()
    
    template_path = Path(args.template)
    output_path = Path(args.out)
    hits_file = Path(args.hits)
    equations_file = Path(args.equations)
    
    print("=" * 70)
    print("Fill Alpha Checklist")
    print("=" * 70)
    print()
    
    # Load data
    print("Loading data...")
    hits_data = load_json(hits_file) or []
    equations_data = load_json(equations_file) or {'equations': [], 'definitions': []}
    
    print(f"  Loaded {len(hits_data)} hits")
    print(f"  Loaded {len(equations_data.get('equations', []))} equations")
    print(f"  Loaded {len(equations_data.get('definitions', []))} definitions")
    print()
    
    # Fill checklist
    print("Filling checklist...")
    fill_checklist(template_path, output_path, hits_data, equations_data)
    
    print("=" * 70)
    print("Complete")
    print("=" * 70)


if __name__ == '__main__':
    main()
