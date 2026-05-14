# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

# verify_lmfdb_labels.sage
# SageMath script to verify exact LMFDB labels for the 6 Hecke forms
# identified in the UBT lepton generation conjecture.
#
# Run with: sage verify_lmfdb_labels.sage
# or in Sage interactive session: load("verify_lmfdb_labels.sage")
#
# Expected results (from numerical computation 2026-03-07 / 2026-03-08):
#   Set A (p=137):
#     76.2.a.a:   a_137 = -11    [CONFIRMED from LMFDB]
#     7.4.a.a:    a_137 = +2274  [CONFIRMED from LMFDB]
#     208.6.a.?:  a_137 = -38286 [SUBSPACE CONFIRMED, suffix pending]
#   Set B (p=139, mirror sector):
#     195.2.a.c:  a_139 = +15    [PROBABLE]
#     50.4.a.b:   a_139 = +3100  [PROBABLE]
#     54.6.a.b:   a_139 = +53009 [PROBABLE]
#
# Updated 2026-03-08 (v61):
#   - Use explicit q_expansion_coefficients() for more reliable coefficient access
#   - Full scan for 208.6.a.? using q_expansion approach to find correct suffix
#   - Full verification of all Set B labels with explicit index access

print("=" * 60)
print("UBT Hecke Form LMFDB Label Verification")
print("=" * 60)
print()

# ──────────────────────────────────────────────────────────────────
# SET A: Forms at p = 137 (our sector)
# ──────────────────────────────────────────────────────────────────
print("SET A — Forms at p=137 (our sector)")
print("-" * 40)

# 76.2.a.a — k=2, N=76, expected a_137 = -11
print("\nVerifying 76.2.a.a (k=2, N=76):")
try:
    forms_76_2 = CuspForms(Gamma0(76), 2).newforms('a')
    print(f"  Number of newforms at (N=76, k=2): {len(forms_76_2)}")
    for i, f in enumerate(forms_76_2):
        try:
            a137 = f[137]
            label = f"76.2.a.{chr(97+i)}"
            match = "MATCH ✓" if abs(int(a137) - (-11)) < 1 else f"MISMATCH (got {a137})"
            print(f"  {label}: a_137 = {a137}  {match}")
        except Exception as e:
            print(f"  76.2.a.{chr(97+i)}: ERROR — {e}")
except Exception as e:
    print(f"  ERROR computing newforms: {e}")

# 7.4.a.a — k=4, N=7, expected a_137 = +2274
print("\nVerifying 7.4.a.a (k=4, N=7):")
try:
    forms_7_4 = CuspForms(Gamma0(7), 4).newforms('a')
    print(f"  Number of newforms at (N=7, k=4): {len(forms_7_4)}")
    for i, f in enumerate(forms_7_4):
        try:
            a137 = f[137]
            label = f"7.4.a.{chr(97+i)}"
            match = "MATCH ✓" if abs(int(a137) - 2274) < 1 else f"MISMATCH (got {a137})"
            print(f"  {label}: a_137 = {a137}  {match}")
        except Exception as e:
            print(f"  7.4.a.{chr(97+i)}: ERROR — {e}")
except Exception as e:
    print(f"  ERROR computing newforms: {e}")

# 208.6.a.? — k=6, N=208, expected a_137 = -38286
# Find the correct letter suffix using q_expansion_coefficients
print("\nVerifying 208.6.a.? (k=6, N=208) — finding correct suffix:")
try:
    M = CuspForms(Gamma0(208), 6)
    newforms = M.newforms(names='a')
    print(f"  Number of newforms: {len(newforms)}")
    found = False
    for i, f in enumerate(newforms):
        try:
            # Use q_expansion_coefficients for reliable access (index 137 = a_137)
            coeffs = f.q_expansion_coefficients(138)
            ap = coeffs[137]
            label = f"208.6.a.{chr(97+i)}"
            if abs(ap - (-38286)) < 10:
                print(f"  {label}: a_137 = {ap}  ← MATCH")
                found = True
            else:
                print(f"  {label}: a_137 = {ap}")
        except Exception as e:
            print(f"  208.6.a.{chr(97+i)}: ERROR — {e}")
    if not found:
        print("  WARNING: No form found with a_137 = -38286 at N=208, k=6")
        print("  (This may indicate the form is not a newform at this level,")
        print("   or the coefficient computation requires more precision)")
except Exception as e:
    print(f"  ERROR computing newforms: {e}")

print()
print("=" * 60)
print("SET B — Forms at p=139 (mirror sector)")
print("-" * 40)

# 195.2.a.c — ověřit a_139 = +15
print("\nVerifying 195.2.a.c (k=2, N=195):")
try:
    M2 = CuspForms(Gamma0(195), 2)
    newforms2 = M2.newforms(names='a')
    print(f"  Number of newforms at (N=195, k=2): {len(newforms2)}")
    # třetí forma (index 2) by měla být 195.2.a.c
    if len(newforms2) >= 3:
        f = newforms2[2]
        try:
            a139 = f.q_expansion_coefficients(140)[139]
            match = "MATCH ✓" if abs(a139 - 15) < 1 else f"MISMATCH (got {a139}, expected +15)"
            print(f"  195.2.a.c: a_139 = {a139}  {match}")
        except Exception as e:
            print(f"  195.2.a.c: ERROR — {e}")
    else:
        print(f"  Only {len(newforms2)} newforms; listing all:")
        for i, f in enumerate(newforms2):
            try:
                a139 = f.q_expansion_coefficients(140)[139]
                label = f"195.2.a.{chr(97+i)}"
                match_str = "← a_139=+15 MATCH" if abs(a139 - 15) < 1 else ""
                print(f"  {label}: a_139 = {a139}  {match_str}")
            except Exception as e:
                print(f"  195.2.a.{chr(97+i)}: ERROR — {e}")
except Exception as e:
    print(f"  ERROR computing newforms: {e}")

# 50.4.a.b — ověřit a_139 = +3100
print("\nVerifying 50.4.a.b (k=4, N=50):")
try:
    M3 = CuspForms(Gamma0(50), 4)
    newforms3 = M3.newforms(names='a')
    print(f"  Number of newforms at (N=50, k=4): {len(newforms3)}")
    if len(newforms3) >= 2:
        f = newforms3[1]  # index 1 = 'b'
        try:
            a139 = f.q_expansion_coefficients(140)[139]
            match = "MATCH ✓" if abs(a139 - 3100) < 1 else f"MISMATCH (got {a139}, expected +3100)"
            print(f"  50.4.a.b: a_139 = {a139}  {match}")
        except Exception as e:
            print(f"  50.4.a.b: ERROR — {e}")
    else:
        print(f"  Only {len(newforms3)} newforms; listing all:")
        for i, f in enumerate(newforms3):
            try:
                a139 = f.q_expansion_coefficients(140)[139]
                label = f"50.4.a.{chr(97+i)}"
                match_str = "← a_139=+3100 MATCH" if abs(a139 - 3100) < 1 else ""
                print(f"  {label}: a_139 = {a139}  {match_str}")
            except Exception as e:
                print(f"  50.4.a.{chr(97+i)}: ERROR — {e}")
except Exception as e:
    print(f"  ERROR computing newforms: {e}")

# 54.6.a.b — ověřit a_139 = +53009
print("\nVerifying 54.6.a.b (k=6, N=54):")
try:
    M4 = CuspForms(Gamma0(54), 6)
    newforms4 = M4.newforms(names='a')
    print(f"  Number of newforms at (N=54, k=6): {len(newforms4)}")
    if len(newforms4) >= 2:
        f = newforms4[1]  # index 1 = 'b'
        try:
            a139 = f.q_expansion_coefficients(140)[139]
            match = "MATCH ✓" if abs(a139 - 53009) < 1 else f"MISMATCH (got {a139}, expected +53009)"
            print(f"  54.6.a.b: a_139 = {a139}  {match}")
        except Exception as e:
            print(f"  54.6.a.b: ERROR — {e}")
    else:
        print(f"  Only {len(newforms4)} newforms; listing all:")
        for i, f in enumerate(newforms4):
            try:
                a139 = f.q_expansion_coefficients(140)[139]
                label = f"54.6.a.{chr(97+i)}"
                match_str = "← a_139=+53009 MATCH" if abs(a139 - 53009) < 1 else ""
                print(f"  {label}: a_139 = {a139}  {match_str}")
            except Exception as e:
                print(f"  54.6.a.{chr(97+i)}: ERROR — {e}")
except Exception as e:
    print(f"  ERROR computing newforms: {e}")

print()
print("=" * 60)
print("Verification complete.")
print("Results should be recorded in reports/hecke_lepton/lmfdb_labels.md")
print("=" * 60)
