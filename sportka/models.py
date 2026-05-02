# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
sportka/models.py — Predictors and ML models for Sportka lottery.

All predictors expose a common interface:
    predictor.predict(df, ...) -> np.ndarray of shape (N_NUMBERS,)
        Each entry p[k] is the probability that number k+1 appears in the
        next draw.  sum(p) should be approximately DRAWN_PER_DRAW ≈ 7.

Available predictors
--------------------
RandomPredictor           — constant 7/49 for all numbers
GlobalFreqPredictor       — historical frequency / n_draws
RollingFreqPredictor      — rolling-window frequency / n_draws_in_window
ExpDecayFreqPredictor     — exponentially-weighted frequency / total_weight
LogisticPredictor         — sklearn LogisticRegression wrapper
MLPPredictor              — sklearn MLPClassifier wrapper
UBTMLPPredictor           — MLP trained on UBT-enhanced features
"""
from __future__ import annotations

from typing import List, Optional

import numpy as np
import pandas as pd

from sportka.features import (
    N_NUMBERS,
    DRAWN_PER_DRAW,
    global_freq_features,
    rolling_freq_features,
    exp_decay_freq_features,
    build_features,
    build_walk_forward_features,
)

# ---------------------------------------------------------------------------
# Base class
# ---------------------------------------------------------------------------

class BasePredictor:
    """Base interface for all predictors."""

    name: str = "base"

    def fit(self, df: pd.DataFrame, **kwargs) -> "BasePredictor":
        return self

    def predict(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        """Return probability vector of shape (N_NUMBERS,). sum ≈ 7."""
        raise NotImplementedError

    def predict_proba_matrix(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        """Return probability matrix of shape (len(df), N_NUMBERS). Each row sums ≈ 7."""
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Baseline predictors
# ---------------------------------------------------------------------------

class RandomPredictor(BasePredictor):
    """Uniform random predictor: p(k) = 7/49 for every k."""

    name = "random_uniform"

    def predict(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        return np.full(N_NUMBERS, DRAWN_PER_DRAW / N_NUMBERS, dtype=np.float32)

    def predict_proba_matrix(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        n = len(df)
        return np.full((n, N_NUMBERS), DRAWN_PER_DRAW / N_NUMBERS, dtype=np.float32)


class GlobalFreqPredictor(BasePredictor):
    """
    Global-frequency predictor.

    p(k) = count_k / n_draws  →  sum ≈ 7.

    Note: does NOT normalise to 1 (that would give sum == 1 which is wrong
    for multi-label prediction).
    """

    name = "global_frequency"

    def __init__(self, train_max_index: Optional[int] = None):
        self.train_max_index = train_max_index
        self._prob: Optional[np.ndarray] = None

    def fit(self, df: pd.DataFrame, **kwargs) -> "GlobalFreqPredictor":
        train_max = self.train_max_index
        if train_max is None:
            train_max = int(df["draw_index"].max())
        self._prob = global_freq_features(df, train_max_index=train_max)
        return self

    def predict(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        if self._prob is None:
            self.fit(df)
        return self._prob.copy()

    def predict_proba_matrix(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        prob = self.predict(df, **kwargs)
        return np.tile(prob, (len(df), 1))


class RollingFreqPredictor(BasePredictor):
    """
    Rolling-window frequency predictor.

    p(k) = count_k_in_window / n_draws_in_window  →  sum ≈ 7.
    """

    name = "rolling_frequency"

    def __init__(self, window: int = 52):
        self.window = window

    def predict(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        """Predict for the row *after* all rows in df."""
        return rolling_freq_features(df, window=self.window, row_idx=len(df))

    def predict_proba_matrix(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        n = len(df)
        mat = np.zeros((n, N_NUMBERS), dtype=np.float32)
        for i in range(n):
            mat[i] = rolling_freq_features(df, window=self.window, row_idx=i)
        return mat


class ExpDecayFreqPredictor(BasePredictor):
    """
    Exponentially-decayed frequency predictor.

    p(k) = weighted_count_k / total_weight  →  sum ≈ 7.
    """

    name = "exp_decay_frequency"

    def __init__(self, decay: float = 0.98):
        self.decay = decay

    def predict(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        return exp_decay_freq_features(df, decay=self.decay, row_idx=len(df))

    def predict_proba_matrix(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        n = len(df)
        mat = np.zeros((n, N_NUMBERS), dtype=np.float32)
        for i in range(n):
            mat[i] = exp_decay_freq_features(df, decay=self.decay, row_idx=i)
        return mat


# ---------------------------------------------------------------------------
# ML-based predictors
# ---------------------------------------------------------------------------

class _SklearnMultiLabelPredictor(BasePredictor):
    """
    Base class for sklearn multi-label predictors.

    Trains one binary classifier per number (one-vs-rest style using
    sklearn's MultiOutputClassifier or a simple loop).
    """

    name = "sklearn_base"

    def __init__(
        self,
        groups: List[str] = None,
        train_max_index: Optional[int] = None,
        window: int = 52,
        decay: float = 0.98,
    ):
        self.groups = groups or ["base", "rolling"]
        self.train_max_index = train_max_index
        self.window = window
        self.decay = decay
        self._clf = None
        self._t_max_train: Optional[float] = None

    def _make_clf(self):
        raise NotImplementedError

    def fit(self, df: pd.DataFrame, **kwargs) -> "_SklearnMultiLabelPredictor":
        from sklearn.multioutput import MultiOutputClassifier

        self._t_max_train = float(df["draw_index"].max())
        if self.train_max_index is None:
            self.train_max_index = int(self._t_max_train)

        X = build_features(
            df,
            groups=self.groups,
            train_max_index=self.train_max_index,
            t_max_train=self._t_max_train,
            window=self.window,
            decay=self.decay,
        )
        # Labels: binary (n_draws, N_NUMBERS)
        from sportka.features import _build_label_matrix
        y = _build_label_matrix(df)

        base_clf = self._make_clf()
        self._clf = MultiOutputClassifier(base_clf, n_jobs=-1)
        self._clf.fit(X, y)
        return self

    def predict(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        """Return probability vector for the *next* draw after df."""
        from sportka.features import _build_single_row_features
        last_idx = float(df["draw_index"].max())
        feat = _build_single_row_features(
            history_df=df,
            current_draw_index=last_idx + 1,
            groups=self.groups,
            train_max_index=self.train_max_index or int(last_idx),
            t_max_train=self._t_max_train or last_idx,
            window=self.window,
            decay=self.decay,
        )
        return self._predict_from_feat(feat[np.newaxis, :])

    def _predict_from_feat(self, X: np.ndarray) -> np.ndarray:
        """X: shape (1, n_features). Returns shape (N_NUMBERS,)."""
        probs = np.zeros(N_NUMBERS, dtype=np.float32)
        for k, est in enumerate(self._clf.estimators_):
            p = est.predict_proba(X)[0]
            # p[1] is probability of class 1 (number drawn)
            probs[k] = p[1] if len(p) > 1 else p[0]
        # Scale so that sum ≈ DRAWN_PER_DRAW
        s = probs.sum()
        if s > 0:
            probs = probs * (DRAWN_PER_DRAW / s)
        return probs

    def predict_proba_matrix(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        X = build_features(
            df,
            groups=self.groups,
            train_max_index=self.train_max_index,
            t_max_train=self._t_max_train,
            window=self.window,
            decay=self.decay,
        )
        n = len(df)
        mat = np.zeros((n, N_NUMBERS), dtype=np.float32)
        for k, est in enumerate(self._clf.estimators_):
            p = est.predict_proba(X)
            mat[:, k] = p[:, 1] if p.shape[1] > 1 else p[:, 0]
        # Scale each row so it sums to DRAWN_PER_DRAW
        row_sums = mat.sum(axis=1, keepdims=True)
        row_sums = np.where(row_sums == 0, 1.0, row_sums)
        mat = mat * (DRAWN_PER_DRAW / row_sums)
        return mat


class LogisticPredictor(_SklearnMultiLabelPredictor):
    """Logistic regression predictor."""

    name = "logistic_regression"

    def __init__(self, C: float = 1.0, **kwargs):
        super().__init__(**kwargs)
        self.C = C

    def _make_clf(self):
        from sklearn.linear_model import LogisticRegression
        return LogisticRegression(C=self.C, max_iter=1000, solver="lbfgs")


class MLPPredictor(_SklearnMultiLabelPredictor):
    """Multi-layer perceptron predictor (baseline, no UBT features)."""

    name = "mlp_base"

    def __init__(self, hidden_layer_sizes=(128, 64), **kwargs):
        super().__init__(**kwargs)
        self.hidden_layer_sizes = hidden_layer_sizes

    def _make_clf(self):
        from sklearn.neural_network import MLPClassifier
        return MLPClassifier(
            hidden_layer_sizes=self.hidden_layer_sizes,
            max_iter=300,
            random_state=42,
        )


class UBTMLPPredictor(_SklearnMultiLabelPredictor):
    """
    MLP predictor trained on UBT-enhanced features (theta transform applied).

    Adds UBT theta transform output as extra feature channels on top of the
    standard feature groups.
    """

    name = "ubt_mlp"

    def __init__(self, hidden_layer_sizes=(256, 128), **kwargs):
        super().__init__(**kwargs)
        self.hidden_layer_sizes = hidden_layer_sizes

    def _make_clf(self):
        from sklearn.neural_network import MLPClassifier
        return MLPClassifier(
            hidden_layer_sizes=self.hidden_layer_sizes,
            max_iter=300,
            random_state=42,
        )

    def _augment_with_ubt(self, X: np.ndarray) -> np.ndarray:
        from sportka.ubt_bridge import apply_theta_transform
        return apply_theta_transform(X)

    def fit(self, df: pd.DataFrame, **kwargs) -> "UBTMLPPredictor":
        super().fit(df, **kwargs)
        return self


class UBTCNNPredictor(BasePredictor):
    """
    1-D CNN predictor trained on UBT-enhanced features.

    Requires PyTorch.  Falls back gracefully if torch is unavailable.
    """

    name = "ubt_cnn_v2"

    def __init__(
        self,
        groups: List[str] = None,
        train_max_index: Optional[int] = None,
        window: int = 52,
    ):
        self.groups = groups or ["base", "rolling", "expdecay"]
        self.train_max_index = train_max_index
        self.window = window
        self._model = None
        self._t_max_train: Optional[float] = None

    def fit(self, df: pd.DataFrame, **kwargs) -> "UBTCNNPredictor":
        try:
            import torch
        except ImportError:
            raise ImportError("PyTorch is required for UBTCNNPredictor.")

        self._t_max_train = float(df["draw_index"].max())
        if self.train_max_index is None:
            self.train_max_index = int(self._t_max_train)

        X = build_features(
            df,
            groups=self.groups,
            train_max_index=self.train_max_index,
            t_max_train=self._t_max_train,
            window=self.window,
        )
        from sportka.features import _build_label_matrix
        y = _build_label_matrix(df)

        from sportka._cnn import train_cnn
        self._model = train_cnn(X, y)
        return self

    def predict(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        if self._model is None:
            raise RuntimeError("Call fit() first.")
        from sportka.features import _build_single_row_features
        last_idx = float(df["draw_index"].max())
        feat = _build_single_row_features(
            history_df=df,
            current_draw_index=last_idx + 1,
            groups=self.groups,
            train_max_index=self.train_max_index,
            t_max_train=self._t_max_train,
            window=self.window,
            decay=0.98,
        )
        import torch
        x = torch.tensor(feat[np.newaxis, np.newaxis, :], dtype=torch.float32)
        with torch.no_grad():
            out = self._model(x).squeeze().numpy()
        s = out.sum()
        if s > 0:
            out = out * (DRAWN_PER_DRAW / s)
        return out.astype(np.float32)

    def predict_proba_matrix(self, df: pd.DataFrame, **kwargs) -> np.ndarray:
        n = len(df)
        mat = np.zeros((n, N_NUMBERS), dtype=np.float32)
        for i in range(n):
            mat[i] = self.predict(df.iloc[:i], **kwargs)
        return mat


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

ALL_PREDICTORS = [
    RandomPredictor,
    GlobalFreqPredictor,
    RollingFreqPredictor,
    ExpDecayFreqPredictor,
    LogisticPredictor,
    MLPPredictor,
    UBTMLPPredictor,
]
