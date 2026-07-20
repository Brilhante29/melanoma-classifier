from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone

import numpy as np
from sklearn.metrics import accuracy_score, auc, roc_curve
from sklearn.model_selection import train_test_split

from melanoma_classifier.classifier import extract_features, predict, train_classifier
from melanoma_classifier.domain import BenchmarkResult
from melanoma_classifier.fixture import generate_synthetic_lesion


def run_benchmark(
    n_samples: int = 500,
    output: str | None = None,
    random_state: int = 42,
) -> BenchmarkResult:
    np.random.seed(random_state)

    print(f"Generating {n_samples} synthetic images...")
    images = []
    labels = []
    for i in range(n_samples):
        img, label = generate_synthetic_lesion(
            image_size=128,
            label=None,
            seed=(random_state + i) % 2**31,
        )
        images.append(img)
        labels.append(label)

    print("Extracting features...")
    X = np.array([extract_features(img) for img in images])
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=random_state, stratify=y
    )

    print("Training classifier...")
    pipe = train_classifier(X_train, y_train, random_state=random_state)

    print("Evaluating...")
    y_pred, y_prob = predict(pipe, X_test)

    accuracy = float(accuracy_score(y_test, y_pred))

    fpr, tpr, _ = roc_curve(y_test, y_prob)
    auc_val = float(auc(fpr, tpr))

    tp = np.sum((y_test == 1) & (y_pred == 1))
    fn = np.sum((y_test == 1) & (y_pred == 0))
    tn = np.sum((y_test == 0) & (y_pred == 0))
    fp = np.sum((y_test == 0) & (y_pred == 1))

    sensitivity = float(tp / (tp + fn)) if (tp + fn) > 0 else 0.0
    specificity = float(tn / (tn + fp)) if (tn + fp) > 0 else 0.0

    result = BenchmarkResult(
        auc=round(auc_val, 4),
        sensitivity=round(sensitivity, 4),
        specificity=round(specificity, 4),
        accuracy=round(accuracy, 4),
        n_train=len(X_train),
        n_test=len(X_test),
        timestamp=datetime.now(timezone.utc).isoformat(),
        command=" ".join(sys.argv),
    )

    print(f"\n=== Benchmark Results ===")
    print(f"AUC:         {result.auc}")
    print(f"Sensitivity: {result.sensitivity}")
    print(f"Specificity: {result.specificity}")
    print(f"Accuracy:    {result.accuracy}")
    print(f"Train/Test:  {result.n_train}/{result.n_test}")

    if output:
        with open(output, "w") as f:
            f.write(result.to_json())
        print(f"\nResults saved to: {output}")

    return result
