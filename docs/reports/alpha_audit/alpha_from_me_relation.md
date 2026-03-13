# Alpha from m_e Relation

## Does alpha depend on m_e?

### Pattern: `alpha.*m_e`

Found 76 references

**tests/test_electron_sensitivity.py** (line 24)
```

def test_electron_mass_moves_with_alpha():
    """
    Test that electron mass responds to alpha changes.
    
    A +1 ppm change in alpha must cause a measurable change in m_e.
    If m_e doesn't change, it's likely hard-coded.
    """
    from ubt_masses.core import (
        compute_lepton_msba
```

**scripts/alpha_circularity_audit.py** (line 3)
```
#!/usr/bin/env python3
"""
Alpha/m_e Circularity Audit Script
===================================

This script audits the dependency chain for alpha (fine structure constant)
and m_e (electron mass) to check for circular reasoning.


```

**scripts/alpha_circularity_audit.py** (line 10)
```

This script audits the dependency chain for alpha (fine structure constant)
and m_e (electron mass) to check for circular reasoning.

Part B1: Find m_e derivation
Part B2: Check alpha from m_e claim
Part B3: Build dependency graph and verdict

Copyright (c) 2025 Ing. David Jaroš
Licensed under the 
```

**scripts/alpha_circularity_audit.py** (line 325)
```
    
    return alpha_files

def check_alpha_from_me():
    """
    Check if alpha is computed from m_e.
    """
    print("B2b: Checking alpha-from-m_e relation...")
    
    # Search for formulas that relate alpha to m_e
    patterns = [

```

**scripts/alpha_circularity_audit.py** (line 327)
```

def check_alpha_from_me():
    """
    Check if alpha is computed from m_e.
    """
    print("B2b: Checking alpha-from-m_e relation...")
    
    # Search for formulas that relate alpha to m_e
    patterns = [
        r'alpha.*m_e',
        r'm_e.*alpha',

```

### Pattern: `m_e.*alpha`

Found 36 references

**tests/test_electron_sensitivity.py** (line 52)
```
    assert delta_m > 0.0, (
        f"Electron mass must change with alpha!\n"
        f"  m_e(α): {m0:.12f} MeV\n"
        f"  m_e(α × 1.000001): {m1:.12f} MeV\n"
        f"  Change: {delta_m:.12e} MeV\n"
        f"This suggests m_e is hard-coded rather than computed from alpha."
    )
    
    # T
```

**tests/test_electron_sensitivity.py** (line 68)
```
    # Even a weak dependence should give > 1e-9 relative change
    assert rel_change > 1e-9, (
        f"Electron mass shows insufficient sensitivity to alpha:\n"
        f"  Relative change: {rel_change:.2e}\n"
        f"  Expected: > 1e-9\n"
        f"This suggests m_e may be hard-coded or weakly
```

**scripts/test_symbolic_alpha.py** (line 104)
```
    print(f"  B = {B} (unchanged for both choices)")
    print(f"  μ0 choice 1 = {mu0_choice1} MeV (electron mass)")
    print(f"  μ0 choice 2 = {mu0_choice2} MeV (muon mass)")
    print(f"  Test scale μ = {mu} MeV")
    print()
    print(f"  α⁻¹({mu} MeV) using μ0 = m_e:  {alpha_inv_mu_choice1:.2f}
```

**scripts/alpha_circularity_audit.py** (line 332)
```
    print("B2b: Checking alpha-from-m_e relation...")
    
    # Search for formulas that relate alpha to m_e
    patterns = [
        r'alpha.*m_e',
        r'm_e.*alpha',
        r'Rydberg.*constant',
        r'Bohr.*radius'
    ]
    
    file_patterns = ['*.py', '*.tex']

```

**scripts/alpha_circularity_audit.py** (line 505)
```
        "  ← hopfion topology",
        "  ← texture factors",
        "  ← invariants from biquaternion field",
    ])
    
    # Check if m_e derivation uses alpha
    if any(info.get('uses_alpha', False) for info in key_files_info.values()):
        graph_nodes.append("  ⚠️  ← α (POTENTIAL CIRCUL
```

### Pattern: `Rydberg.*constant`

Found 2 references

**scripts/alpha_circularity_audit.py** (line 333)
```
    
    # Search for formulas that relate alpha to m_e
    patterns = [
        r'alpha.*m_e',
        r'm_e.*alpha',
        r'Rydberg.*constant',
        r'Bohr.*radius'
    ]
    
    file_patterns = ['*.py', '*.tex']
    

```

**scripts/alpha_circularity_audit.py** (line 375)
```
    report_lines.extend([
        "## Standard Physics Relations",
        "",
        "In standard physics, alpha and m_e are related through:",
        "",
        "1. **Rydberg constant**: R_∞ = (m_e * e^4) / (8 * ε_0^2 * h^3 * c)",
        "2. **Bohr radius**: a_0 = (4πε_0ℏ²) / (m_e * e²) = ℏ / 
```

### Pattern: `Bohr.*radius`

Found 28 references

**scripts/alpha_circularity_audit.py** (line 334)
```
    # Search for formulas that relate alpha to m_e
    patterns = [
        r'alpha.*m_e',
        r'm_e.*alpha',
        r'Rydberg.*constant',
        r'Bohr.*radius'
    ]
    
    file_patterns = ['*.py', '*.tex']
    
    results_by_pattern = {}

```

**scripts/alpha_circularity_audit.py** (line 376)
```
        "## Standard Physics Relations",
        "",
        "In standard physics, alpha and m_e are related through:",
        "",
        "1. **Rydberg constant**: R_∞ = (m_e * e^4) / (8 * ε_0^2 * h^3 * c)",
        "2. **Bohr radius**: a_0 = (4πε_0ℏ²) / (m_e * e²) = ℏ / (m_e * c * α)",
        "3
```

**scripts/padic_alpha_calculator.py** (line 112)
```
    Calculate physical properties in universe p relative to our universe (p=137).
    
    Returns:
    --------
    Dict with keys:
        'bohr_radius': Relative Bohr radius
        'ionization_energy': Relative ionization energy
        'fine_structure_split': Relative fine structure splitting
 
```

**scripts/padic_alpha_calculator.py** (line 120)
```
        'em_strength': Relative EM interaction strength
    """
    alpha_inv_p, alpha_p = calculate_alpha(p)
    alpha_inv_137, alpha_137 = calculate_alpha(137)
    
    # Bohr radius scales as 1/alpha
    bohr_radius_ratio = alpha_inv_p / alpha_inv_137
    
    # Ionization energy scales as alpha^
```

**scripts/padic_alpha_calculator.py** (line 121)
```
    """
    alpha_inv_p, alpha_p = calculate_alpha(p)
    alpha_inv_137, alpha_137 = calculate_alpha(137)
    
    # Bohr radius scales as 1/alpha
    bohr_radius_ratio = alpha_inv_p / alpha_inv_137
    
    # Ionization energy scales as alpha^2
    ionization_energy_ratio = (alpha_p / alpha_137) **
```

## Standard Physics Relations

In standard physics, alpha and m_e are related through:

1. **Rydberg constant**: R_∞ = (m_e * e^4) / (8 * ε_0^2 * h^3 * c)
2. **Bohr radius**: a_0 = (4πε_0ℏ²) / (m_e * e²) = ℏ / (m_e * c * α)
3. **Fine structure splitting**: ΔE ∝ α² * m_e * c²

However, in standard QED:
- α is defined independently: α = e²/(4πε_0ℏc) ≈ 1/137.036
- m_e is measured independently: m_e ≈ 0.511 MeV/c²

These are treated as **independent fundamental constants**.

## UBT Claim

UBT claims to derive both from first principles:
- m_e emerges from topological (hopfion) structure
- α emerges from minimization of effective potential V_eff(n)

The question: **Does the derivation of one depend on the other?**
