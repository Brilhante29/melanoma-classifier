from __future__ import annotations

import json
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import sklearn
from sklearn.metrics import confusion_matrix, roc_auc_score

from melanoma_classifier.classifier import choose_threshold, extract_features, train_classifier
from melanoma_classifier.dataset import binary_labels, load_dermamnist
from melanoma_classifier.domain import Evaluation


def evaluate(labels: np.ndarray, probabilities: np.ndarray, threshold: float) -> Evaluation:
    predicted = probabilities >= threshold
    tn, fp, fn, tp = confusion_matrix(labels, predicted, labels=[0, 1]).ravel()
    return Evaluation(
        auc=float(roc_auc_score(labels, probabilities)),
        sensitivity=float(tp / (tp + fn)),
        specificity=float(tn / (tn + fp)),
        accuracy=float((tp + tn) / len(labels)),
        threshold=threshold,
        true_negative=int(tn),
        false_positive=int(fp),
        false_negative=int(fn),
        true_positive=int(tp),
    )


def run_benchmark(
    *,
    dataset_path: Path,
    output_path: Path,
    seed: int = 42,
    minimum_validation_sensitivity: float = 0.8,
) -> dict:
    started = time.perf_counter()
    dataset = load_dermamnist(dataset_path)
    train_labels = binary_labels(dataset.train.labels)
    validation_labels = binary_labels(dataset.validation.labels)
    test_labels = binary_labels(dataset.test.labels)
    train_features = extract_features(dataset.train.images)
    validation_features = extract_features(dataset.validation.images)
    test_features = extract_features(dataset.test.images)
    model = train_classifier(train_features, train_labels, seed)
    validation_probability = model.predict_proba(validation_features)[:, 1]
    threshold = choose_threshold(
        validation_labels,
        validation_probability,
        minimum_sensitivity=minimum_validation_sensitivity,
    )
    test_probability = model.predict_proba(test_features)[:, 1]
    evaluation = evaluate(test_labels, test_probability, threshold)
    duration = time.perf_counter() - started
    payload = {
        "project": "melanoma-classifier",
        "metric": "auc",
        "value": round(evaluation.auc, 6),
        "unit": "ratio",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "command": " ".join(sys.argv),
        "repeat": 1,
        "measured_iterations": len(test_labels),
        "samples": [round(evaluation.auc, 6)],
        "failures": 0,
        "summary": {
            **evaluation.to_dict(),
            "train_images": len(train_labels),
            "validation_images": len(validation_labels),
            "test_images": len(test_labels),
            "test_melanoma_images": int(test_labels.sum()),
            "minimum_validation_sensitivity": minimum_validation_sensitivity,
            "duration_seconds": round(duration, 6),
        },
        "dataset": {
            "name": "DermaMNIST v2.1",
            "source": "MedMNIST v2 / HAM10000",
            "sha256": dataset.sha256,
            "license": "CC BY-NC 4.0",
            "split": "official train/validation/test",
            "clinical_use": False,
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scikit_learn": sklearn.__version__,
            "platform": platform.platform(),
            "machine": platform.machine(),
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return payload
