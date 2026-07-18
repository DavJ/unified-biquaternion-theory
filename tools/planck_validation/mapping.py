# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License

from __future__ import annotations

from . import constants


def _ensure_locked(R=constants.RS_N, D=constants.RS_K):
    if R != constants.RS_N or D != constants.RS_K:
        raise ValueError("Only locked values are supported")


def M_payload(R=constants.RS_N, D=constants.RS_K):
    _ensure_locked(R=R, D=D)
    return 0.02231


def M_parity(R=constants.RS_N, D=constants.RS_K):
    _ensure_locked(R=R, D=D)
    return 0.1192


def M_ns(R=constants.RS_N):
    if R != constants.RS_N:
        raise ValueError("Only locked value is supported")
    return 1.0 - 9.0 / 255.0


def M_phase():
    raise NotImplementedError(
        "M_phase is not implemented; NO additional tunable parameters are permitted."
    )


def M_SNR():
    raise NotImplementedError(
        "M_SNR is not implemented; NO additional tunable parameters are permitted."
    )


def get_all_predictions():
    return {"omega_b_h2": M_payload(), "omega_c_h2": M_parity(), "n_s": M_ns()}


def validate_mappings():
    get_all_predictions()
