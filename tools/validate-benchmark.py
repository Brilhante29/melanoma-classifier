from __future__ import annotations

import json
from pathlib import Path

from melanoma_classifier.dataset import DERMAMNIST_SHA256

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "benchmarks" / "results" / "baseline.json"


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    assert result["project"] == "melanoma-classifier"
    assert result["metric"] == "auc"
    assert 0.5 < result["value"] < 1.0
    assert result["failures"] == 0
    assert result["measured_iterations"] == 2005
    assert result["dataset"]["sha256"] == DERMAMNIST_SHA256
    assert result["dataset"]["clinical_use"] is False
    assert result["dataset"]["license"] == "CC BY-NC 4.0"
    summary = result["summary"]
    assert (summary["train_images"], summary["validation_images"], summary["test_images"]) == (7007, 1003, 2005)
    confusion_total = sum(summary[key] for key in ("true_negative", "false_positive", "false_negative", "true_positive"))
    assert confusion_total == 2005
    assert summary["test_melanoma_images"] == 223
    assert 0 <= summary["sensitivity"] <= 1
    assert 0 <= summary["specificity"] <= 1
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert f"{result['value']:.4f}" in readme
    assert f"{summary['sensitivity']:.4f}" in readme
    assert "not intended for clinical use" in readme
    print("benchmark_contract=passed")


if __name__ == "__main__":
    main()
