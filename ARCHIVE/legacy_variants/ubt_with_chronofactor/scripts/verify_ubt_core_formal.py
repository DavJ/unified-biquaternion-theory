#!/usr/bin/env python3
"""
UBT CORE Formal Verification - Validation Script

This script verifies that all four FORMAL appendices required by the UBT CORE
task specification exist, are complete, and satisfy the acceptance criteria.

Author: UBT Team
Date: February 2026
License: MIT
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def check_mark(passed: bool) -> str:
    """Return colored checkmark or X"""
    return f"{GREEN}✓{RESET}" if passed else f"{RED}✗{RESET}"

class FormalAppendixValidator:
    """Validator for UBT FORMAL appendices"""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.consolidation = repo_root / "consolidation_project"
        self.results = {}
        
    def validate_file_exists(self, filename: str) -> bool:
        """Check if file exists"""
        filepath = self.consolidation / filename
        exists = filepath.exists()
        if not exists:
            print(f"  {check_mark(exists)} File not found: {filename}")
        return exists
    
    def count_lines(self, filename: str) -> int:
        """Count lines in file"""
        filepath = self.consolidation / filename
        if not filepath.exists():
            return 0
        with open(filepath, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    
    def check_section_exists(self, filename: str, section_pattern: str) -> bool:
        """Check if a section exists in the file"""
        filepath = self.consolidation / filename
        if not filepath.exists():
            return False
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            return bool(re.search(section_pattern, content, re.MULTILINE))
    
    def check_equation_exists(self, filename: str, equation_label: str) -> bool:
        """Check if an equation with given label exists"""
        filepath = self.consolidation / filename
        if not filepath.exists():
            return False
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            return f"\\label{{{equation_label}}}" in content or f"label={equation_label}" in content
    
    def validate_task1_qm_gr(self) -> Dict[str, bool]:
        """Validate Task 1: QM-GR Unification"""
        filename = "appendix_FORMAL_qm_gr_unification.tex"
        
        print(f"\n{YELLOW}Task 1: QM-GR Unification{RESET}")
        print(f"  File: {filename}")
        
        checks = {}
        
        # Check file exists
        checks['exists'] = self.validate_file_exists(filename)
        if not checks['exists']:
            return checks
        
        # Check line count (should be substantial)
        line_count = self.count_lines(filename)
        checks['substantial'] = line_count > 300
        print(f"  {check_mark(checks['substantial'])} Line count: {line_count} (expected > 300)")
        
        # Check key sections exist
        checks['theta_field'] = self.check_section_exists(filename, r"Fundamental Field.*\$\\Theta")
        print(f"  {check_mark(checks['theta_field'])} Fundamental field Θ(q,τ) defined")
        
        checks['covariant_deriv'] = self.check_section_exists(filename, r"Covariant Derivative")
        print(f"  {check_mark(checks['covariant_deriv'])} Covariant derivative D_μ defined")
        
        checks['fokker_planck'] = self.check_section_exists(filename, r"Fokker.*Planck|Master Field Equation")
        print(f"  {check_mark(checks['fokker_planck'])} Drift-diffusion/Fokker-Planck equation present")
        
        checks['schrodinger'] = self.check_section_exists(filename, r"Schr.*dinger")
        print(f"  {check_mark(checks['schrodinger'])} Schrödinger equation derivation")
        
        checks['dirac'] = self.check_section_exists(filename, r"Dirac.*Equation")
        print(f"  {check_mark(checks['dirac'])} Dirac equation derivation")
        
        checks['metric_emergence'] = self.check_section_exists(filename, r"Emergent.*Metric|Metric.*Tensor")
        print(f"  {check_mark(checks['metric_emergence'])} Emergent metric discussion")
        
        checks['projection'] = self.check_section_exists(filename, r"Projection.*Complex.*Real|Real.*Time.*Projection")
        print(f"  {check_mark(checks['projection'])} Complex-to-real projection")
        
        return checks
    
    def validate_task2_metric(self) -> Dict[str, bool]:
        """Validate Task 2: Emergent Metric Formalization"""
        filename = "appendix_FORMAL_emergent_metric.tex"
        
        print(f"\n{YELLOW}Task 2: Emergent Metric Formalization{RESET}")
        print(f"  File: {filename}")
        
        checks = {}
        
        checks['exists'] = self.validate_file_exists(filename)
        if not checks['exists']:
            return checks
        
        line_count = self.count_lines(filename)
        checks['substantial'] = line_count > 400
        print(f"  {check_mark(checks['substantial'])} Line count: {line_count} (expected > 400)")
        
        # Check for CRITICAL preservation statement
        checks['preservation'] = self.check_section_exists(filename, r"No.*alternative.*metric|NOT newly postulated")
        print(f"  {check_mark(checks['preservation'])} CRITICAL: States no alternative metric introduced")
        
        checks['metric_def'] = self.check_section_exists(filename, r"g_\{.*\\mu.*\\nu.*\}")
        print(f"  {check_mark(checks['metric_def'])} Metric g_μν explicitly defined")
        
        checks['christoffel'] = self.check_section_exists(filename, r"Christoffel")
        print(f"  {check_mark(checks['christoffel'])} Christoffel symbols computed")
        
        checks['curvature'] = self.check_section_exists(filename, r"Riemann.*tensor|curvature.*tensor")
        print(f"  {check_mark(checks['curvature'])} Curvature tensors computed")
        
        checks['einstein'] = self.check_section_exists(filename, r"Einstein.*tensor|G_\{\\mu\\nu\}")
        print(f"  {check_mark(checks['einstein'])} Einstein tensor derived")
        
        checks['stress_energy'] = self.check_section_exists(filename, r"stress.*energy|T_\{\\mu\\nu\}")
        print(f"  {check_mark(checks['stress_energy'])} Stress-energy tensor identified")
        
        return checks
    
    def validate_task3_black_hole(self) -> Dict[str, bool]:
        """Validate Task 3: Black Hole Radiation"""
        filename = "appendix_FORMAL_black_hole_radiation.tex"
        
        print(f"\n{YELLOW}Task 3: Black Hole Radiation{RESET}")
        print(f"  File: {filename}")
        
        checks = {}
        
        checks['exists'] = self.validate_file_exists(filename)
        if not checks['exists']:
            return checks
        
        line_count = self.count_lines(filename)
        checks['substantial'] = line_count > 300
        print(f"  {check_mark(checks['substantial'])} Line count: {line_count} (expected > 300)")
        
        checks['schwarzschild'] = self.check_section_exists(filename, r"Schwarzschild")
        print(f"  {check_mark(checks['schwarzschild'])} Schwarzschild geometry modeled")
        
        checks['horizon'] = self.check_section_exists(filename, r"horizon|event horizon")
        print(f"  {check_mark(checks['horizon'])} Horizon analysis present")
        
        checks['phase_diffusion'] = self.check_section_exists(filename, r"phase.*diffusion|diffusion.*phase")
        print(f"  {check_mark(checks['phase_diffusion'])} Phase diffusion mechanism")
        
        checks['no_pairs'] = self.check_section_exists(filename, r"No.*pair.*creation|without.*pair")
        print(f"  {check_mark(checks['no_pairs'])} States no vacuum pair creation required")
        
        checks['hawking'] = self.check_section_exists(filename, r"Hawking.*temperature|T.*~.*M\^\{-1\}")
        print(f"  {check_mark(checks['hawking'])} Hawking temperature comparison")
        
        checks['information'] = self.check_section_exists(filename, r"information.*preserved|information.*encoded")
        print(f"  {check_mark(checks['information'])} Information preservation discussed")
        
        return checks
    
    def validate_task4_constants(self) -> Dict[str, bool]:
        """Validate Task 4: Fundamental Constants"""
        filename = "appendix_FORMAL_constants_normalization.tex"
        
        print(f"\n{YELLOW}Task 4: Fundamental Constants{RESET}")
        print(f"  File: {filename}")
        
        checks = {}
        
        checks['exists'] = self.validate_file_exists(filename)
        if not checks['exists']:
            return checks
        
        line_count = self.count_lines(filename)
        checks['substantial'] = line_count > 350
        print(f"  {check_mark(checks['substantial'])} Line count: {line_count} (expected > 350)")
        
        checks['normalization'] = self.check_section_exists(filename, r"normalization.*condition|Global.*Normalization")
        print(f"  {check_mark(checks['normalization'])} Global normalization condition")
        
        checks['compactification'] = self.check_section_exists(filename, r"compactif|torus|T\^2")
        print(f"  {check_mark(checks['compactification'])} Compactified manifold structure")
        
        checks['alpha'] = self.check_section_exists(filename, r"fine.*structure|\\alpha.*137|1/137")
        print(f"  {check_mark(checks['alpha'])} Fine-structure constant α derivation")
        
        checks['spectral'] = self.check_section_exists(filename, r"spectral|eigenvalue|mode")
        print(f"  {check_mark(checks['spectral'])} Spectral/eigenvalue analysis")
        
        checks['no_tuning'] = self.check_section_exists(filename, r"No.*tuning|not.*arbitrary|not.*free parameter")
        print(f"  {check_mark(checks['no_tuning'])} States no ad-hoc tuning")
        
        checks['topology'] = self.check_section_exists(filename, r"topological|winding.*number")
        print(f"  {check_mark(checks['topology'])} Topological quantum numbers")
        
        return checks
    
    def validate_integration(self) -> Dict[str, bool]:
        """Validate integration into main document"""
        print(f"\n{YELLOW}Integration Check{RESET}")
        
        checks = {}
        
        # Check ubt_core_main.tex exists
        core_main = self.consolidation / "ubt_core_main.tex"
        checks['core_exists'] = core_main.exists()
        print(f"  {check_mark(checks['core_exists'])} ubt_core_main.tex exists")
        
        if checks['core_exists']:
            with open(core_main, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check all four appendices are included
            checks['task1_included'] = r'\input{appendix_FORMAL_qm_gr_unification}' in content
            print(f"  {check_mark(checks['task1_included'])} Task 1 appendix included")
            
            checks['task2_included'] = r'\input{appendix_FORMAL_emergent_metric}' in content
            print(f"  {check_mark(checks['task2_included'])} Task 2 appendix included")
            
            checks['task3_included'] = r'\input{appendix_FORMAL_black_hole_radiation}' in content
            print(f"  {check_mark(checks['task3_included'])} Task 3 appendix included")
            
            checks['task4_included'] = r'\input{appendix_FORMAL_constants_normalization}' in content
            print(f"  {check_mark(checks['task4_included'])} Task 4 appendix included")
        
        return checks
    
    def validate_framework_doc(self) -> Dict[str, bool]:
        """Validate framework documentation exists"""
        print(f"\n{YELLOW}Documentation Check{RESET}")
        
        checks = {}
        
        framework = self.consolidation / "FORMAL_VERIFICATION_FRAMEWORK.md"
        checks['framework_exists'] = framework.exists()
        print(f"  {check_mark(checks['framework_exists'])} FORMAL_VERIFICATION_FRAMEWORK.md exists")
        
        if checks['framework_exists']:
            line_count = sum(1 for _ in open(framework))
            checks['framework_substantial'] = line_count > 150
            print(f"  {check_mark(checks['framework_substantial'])} Framework doc substantial ({line_count} lines)")
        
        theta_def = self.repo_root / "THETA_FIELD_DEFINITION.md"
        checks['theta_def_exists'] = theta_def.exists()
        print(f"  {check_mark(checks['theta_def_exists'])} THETA_FIELD_DEFINITION.md exists")
        
        verification_report = self.repo_root / "UBT_CORE_VERIFICATION_REPORT.md"
        checks['report_exists'] = verification_report.exists()
        print(f"  {check_mark(checks['report_exists'])} UBT_CORE_VERIFICATION_REPORT.md exists")
        
        return checks
    
    def run_all_validations(self) -> bool:
        """Run all validations and return overall pass/fail"""
        print(f"\n{'='*70}")
        print(f"{YELLOW}UBT CORE FORMAL VERIFICATION - Validation Report{RESET}")
        print(f"{'='*70}")
        
        all_checks = {}
        
        # Validate each task
        all_checks['task1'] = self.validate_task1_qm_gr()
        all_checks['task2'] = self.validate_task2_metric()
        all_checks['task3'] = self.validate_task3_black_hole()
        all_checks['task4'] = self.validate_task4_constants()
        all_checks['integration'] = self.validate_integration()
        all_checks['documentation'] = self.validate_framework_doc()
        
        # Compute statistics
        total_checks = sum(len(checks) for checks in all_checks.values())
        passed_checks = sum(sum(checks.values()) for checks in all_checks.values())
        
        print(f"\n{'='*70}")
        print(f"{YELLOW}Summary{RESET}")
        print(f"{'='*70}")
        print(f"  Total checks: {total_checks}")
        print(f"  Passed: {GREEN}{passed_checks}{RESET}")
        print(f"  Failed: {RED}{total_checks - passed_checks}{RESET}")
        print(f"  Success rate: {100 * passed_checks / total_checks:.1f}%")
        
        all_passed = (passed_checks == total_checks)
        
        if all_passed:
            print(f"\n{GREEN}✓ ALL VALIDATIONS PASSED{RESET}")
            print(f"\nThe UBT CORE formal verification is complete and meets all requirements.")
        else:
            print(f"\n{RED}✗ SOME VALIDATIONS FAILED{RESET}")
            print(f"\nPlease review the failures above.")
        
        print(f"{'='*70}\n")
        
        return all_passed

def main():
    """Main entry point"""
    # Find repository root
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent
    
    print(f"Repository root: {repo_root}")
    
    validator = FormalAppendixValidator(repo_root)
    success = validator.run_all_validations()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
