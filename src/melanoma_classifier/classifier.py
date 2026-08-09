from __future__ import annotations

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def extract_features(images: np.ndarray) -> np.ndarray:
    if images.ndim != 4 or images.shape[1:] != (28, 28, 3):
        raise ValueError("expected NHWC 28x28 RGB images")
    values = images.astype(np.float32) / 255.0
    pooled = values.reshape(len(values), 14, 2, 14, 2, 3).mean((2, 4))
    moments = np.concatenate([values.mean((1, 2)), values.std((1, 2))], axis=1)
    return np.concatenate([pooled.reshape(len(values), -1), moments], axis=1)


def train_classifier(features: np.ndarray, labels: np.ndarray, seed: int) -> Pipeline:
    model = Pipeline(
        [
            ("scale", StandardScaler()),
            (
                "classifier",
                LogisticRegression(
                    class_weight="balanced",
                    max_iter=500,
                    random_state=seed,
                    solver="liblinear",
                ),
            ),
        ]
    )
    model.fit(features, labels)
    return model


def choose_threshold(
    labels: np.ndarray,
    probabilities: np.ndarray,
    *,
    minimum_sensitivity: float,
) -> float:
    if not 0 < minimum_sensitivity <= 1:
        raise ValueError("minimum sensitivity must be in (0, 1]")
    best_threshold = 0.5
    best_specificity = -1.0
    for threshold in np.unique(probabilities):
        tn, fp, fn, tp = confusion_matrix(
            labels, probabilities >= threshold, labels=[0, 1]
        ).ravel()
        sensitivity = tp / (tp + fn) if tp + fn else 0.0
        specificity = tn / (tn + fp) if tn + fp else 0.0
        if sensitivity >= minimum_sensitivity and specificity > best_specificity:
            best_threshold = float(threshold)
            best_specificity = float(specificity)
    if best_specificity < 0:
        raise ValueError("validation split cannot satisfy the sensitivity target")
    return best_threshold
