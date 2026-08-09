from __future__ import annotations

import numpy as np

from melanoma_classifier.classifier import choose_threshold, extract_features, train_classifier


def test_feature_shape_and_classifier_probability() -> None:
    rng = np.random.default_rng(42)
    images = rng.integers(0, 256, size=(20, 28, 28, 3), dtype=np.uint8)
    labels = np.array([0, 1] * 10)
    features = extract_features(images)
    assert features.shape == (20, 594)
    model = train_classifier(features, labels, 42)
    probability = model.predict_proba(features)[:, 1]
    assert np.all((probability >= 0) & (probability <= 1))


def test_threshold_is_selected_only_from_validation_probabilities() -> None:
    labels = np.array([1, 1, 0, 0])
    probabilities = np.array([0.9, 0.7, 0.6, 0.1])
    threshold = choose_threshold(labels, probabilities, minimum_sensitivity=1.0)
    assert threshold == 0.7
