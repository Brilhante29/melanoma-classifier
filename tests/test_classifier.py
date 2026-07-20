from __future__ import annotations

import numpy as np
import pytest

from melanoma_classifier.classifier import (
    extract_features,
    train_classifier,
    predict,
)
from melanoma_classifier.fixture import generate_synthetic_lesion


class TestFeatureExtraction:
    def test_extract_features_returns_vector(self):
        img, label = generate_synthetic_lesion(seed=42)
        feats = extract_features(img)
        assert isinstance(feats, np.ndarray)
        assert feats.shape == (9,)
        assert np.all(np.isfinite(feats))

    def test_melanoma_vs_benign_features_differ(self):
        mel_img, _ = generate_synthetic_lesion(label=1, seed=1)
        ben_img, _ = generate_synthetic_lesion(label=0, seed=2)
        mel_feats = extract_features(mel_img)
        ben_feats = extract_features(ben_img)
        diff = np.abs(mel_feats - ben_feats).sum()
        assert diff > 0.01


class TestClassifier:
    def test_train_and_predict(self):
        images = []
        labels = []
        for i in range(20):
            img, label = generate_synthetic_lesion(
                seed=(42 + i), label=None
            )
            images.append(img)
            labels.append(label)

        X = np.array([extract_features(img) for img in images])
        y = np.array(labels)

        pipe = train_classifier(X, y, random_state=42)
        preds, probs = predict(pipe, X)

        assert len(preds) == 20
        assert len(probs) == 20
        assert set(preds).issubset({0, 1})
        assert np.all((probs >= 0) & (probs <= 1))

    def test_classifier_improves_over_random(self):
        np.random.seed(42)
        images = []
        labels = []
        for i in range(100):
            img, label = generate_synthetic_lesion(
                seed=(42 + i), label=None
            )
            images.append(img)
            labels.append(label)

        X = np.array([extract_features(img) for img in images])
        y = np.array(labels)

        pipe = train_classifier(X, y, random_state=42)
        preds, probs = predict(pipe, X)

        accuracy = np.mean(preds == y)
        assert accuracy > 0.5, f"Accuracy {accuracy} should exceed random"
