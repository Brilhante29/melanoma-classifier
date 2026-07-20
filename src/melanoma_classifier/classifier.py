from __future__ import annotations

import numpy as np
from PIL import Image
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def extract_features(image: Image.Image) -> np.ndarray:
    arr = np.array(image.convert("L"), dtype=np.float64)
    h, w = arr.shape
    total = h * w

    gray = arr.copy()

    _, binary = cv2_threshold(gray)

    asymmetry = _compute_asymmetry(binary)
    border_irregularity = _compute_border_irregularity(binary)
    color_std = float(np.std(arr))
    color_mean = float(np.mean(arr))
    color_skew = float(np.mean((arr - color_mean) ** 3) / (color_std**3 + 1e-8))
    area = float(np.sum(binary))
    perimeter = _compute_perimeter(binary)
    circularity = (4 * np.pi * area) / (perimeter**2 + 1e-8)
    lesion_ratio = area / total

    feats = np.array([
        asymmetry,
        border_irregularity,
        color_std,
        color_mean,
        color_skew,
        area,
        perimeter,
        circularity,
        lesion_ratio,
    ])
    return feats


def cv2_threshold(gray: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mean_val = np.mean(gray)
    binary = (gray < mean_val * 0.85).astype(np.float64)
    return gray, binary


def _compute_asymmetry(binary: np.ndarray) -> float:
    h, w = binary.shape
    cy, cx = np.mean(np.argwhere(binary > 0), axis=0) if np.sum(binary) > 0 else (h // 2, w // 2)

    top = binary[: int(cy), :]
    bottom = binary[int(cy) :, :]
    if top.shape[0] > 0 and bottom.shape[0] > 0:
        bh, bw = min(top.shape[0], bottom.shape[0]), min(top.shape[1], bottom.shape[1])
        top_crop = top[:bh, :bw]
        bottom_flip = np.flipud(bottom[:bh, :bw])
        asym_y = float(np.mean(np.abs(top_crop.astype(float) - bottom_flip.astype(float))))
    else:
        asym_y = 0.0

    left = binary[:, : int(cx)]
    right = binary[:, int(cx) :]
    if left.shape[1] > 0 and right.shape[1] > 0:
        lh, lw = min(left.shape[0], right.shape[0]), min(left.shape[1], right.shape[1])
        left_crop = left[:lh, :lw]
        right_flip = np.fliplr(right[:lh, :lw])
        asym_x = float(np.mean(np.abs(left_crop.astype(float) - right_flip.astype(float))))
    else:
        asym_x = 0.0

    return (asym_y + asym_x) / 2.0


def _compute_border_irregularity(binary: np.ndarray) -> float:
    if np.sum(binary) == 0:
        return 0.0
    from scipy.ndimage import binary_erosion

    eroded = binary_erosion(binary, iterations=1)
    border = binary.astype(int) - eroded.astype(int)
    border_pixels = np.sum(border > 0)
    total_lesion = np.sum(binary > 0)
    if total_lesion == 0:
        return 0.0
    return border_pixels / total_lesion


def _compute_perimeter(binary: np.ndarray) -> float:
    from scipy.ndimage import binary_erosion

    eroded = binary_erosion(binary, iterations=1)
    border = binary.astype(int) - eroded.astype(int)
    return float(np.sum(border > 0))


def train_classifier(
    X: np.ndarray, y: np.ndarray, random_state: int = 42
) -> Pipeline:
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, random_state=random_state)),
    ])
    pipe.fit(X, y)
    return pipe


def predict(pipe: Pipeline, X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    preds = pipe.predict(X)
    probs = pipe.predict_proba(X)[:, 1]
    return preds, probs
