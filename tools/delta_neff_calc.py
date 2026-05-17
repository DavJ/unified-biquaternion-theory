# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

def delta_Neff_total(N_modes, g_dec, g_today=3.909):
    """
    Compute total ΔN_eff from KK modes.

    Parameters
    ----------
    N_modes : int or float
        Number of KK modes contributing to radiation density.
    g_dec : float
        Effective relativistic degrees of freedom at decoupling, g*(T_dec).
    g_today : float, default=3.909
        Present-day entropy degrees of freedom normalization factor.

    Returns
    -------
    float
        Total ΔN_eff = N_modes * (43/4) * (g_today / g_dec)^(4/3).
    """
    per_mode = (43 / 4) * (g_today / g_dec) ** (4 / 3)
    return N_modes * per_mode


def main():
    print("g* scan:")
    for g in [106.75, 200, 427, 500, 1000]:
        total = delta_Neff_total(12, g)
        tension = total > 0.28
        print(
            f"  g*={g:6.1f}: ΔN_eff={total:.4f}, "
            f"Planck tension={'YES' if tension else 'NO'}, "
            f"CMB-S4 detectable={total > 0.03}"
        )

    for g in range(107, 500):
        if delta_Neff_total(12, g) < 0.28:
            print(f"\nMin g* pro konzistenci: {g}")
            break


if __name__ == "__main__":
    main()
