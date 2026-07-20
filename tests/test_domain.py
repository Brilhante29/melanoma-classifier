from __future__ import annotations

from melanoma_classifier.domain import BenchmarkResult


class TestBenchmarkResult:
    def test_to_json_and_from_dict_roundtrip(self):
        result = BenchmarkResult(
            auc=0.95,
            sensitivity=0.90,
            specificity=0.88,
            accuracy=0.89,
            n_train=350,
            n_test=150,
            timestamp="2025-01-01T00:00:00+00:00",
            command="python -m melanoma_classifier benchmark",
        )
        json_str = result.to_json()
        assert '"auc": 0.95' in json_str
        assert '"sensitivity": 0.9' in json_str

        restored = BenchmarkResult.from_dict({
            "auc": 0.95,
            "sensitivity": 0.90,
            "specificity": 0.88,
            "accuracy": 0.89,
            "n_train": 350,
            "n_test": 150,
            "timestamp": "2025-01-01T00:00:00+00:00",
            "command": "python -m melanoma_classifier benchmark",
        })
        assert restored.auc == result.auc
        assert restored.sensitivity == result.sensitivity

    def test_default_values_immutable(self):
        result = BenchmarkResult(
            auc=0.5,
            sensitivity=0.5,
            specificity=0.5,
            accuracy=0.5,
            n_train=1,
            n_test=1,
            timestamp="now",
            command="test",
        )
        assert isinstance(result.auc, float)
        assert isinstance(result.sensitivity, float)
