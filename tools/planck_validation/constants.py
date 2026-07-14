# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License

RS_N = 255
RS_K = 200
OFDM_CHANNELS = 16
RS_PARITY = RS_N - RS_K

PLANCK_2018_OMEGA_B_H2 = 0.02237
PLANCK_2018_OMEGA_B_H2_SIGMA = 0.00015
PLANCK_2018_OMEGA_C_H2 = 0.1200
PLANCK_2018_OMEGA_C_H2_SIGMA = 0.0012
PLANCK_2018_N_S = 0.9649
PLANCK_2018_N_S_SIGMA = 0.0042


def validate_constants() -> None:
    if (RS_N, RS_K, OFDM_CHANNELS, RS_PARITY) != (255, 200, 16, 55):
        raise ValueError("Locked constants changed")
