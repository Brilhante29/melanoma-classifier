from __future__ import annotations

import dataclasses
import json
from typing import Any


@dataclasses.dataclass(frozen=True)
class LesionImage:
    pixels: Any
    label: int
    image_id: str

    def to_dict(self) -> dict:
        return {"image_id": self.image_id, "label": self.label}


@dataclasses.dataclass(frozen=True)
class ClassificationResult:
    true_label: int
    predicted_label: int
    confidence: float


@dataclasses.dataclass(frozen=True)
class BenchmarkResult:
    auc: float
    sensitivity: float
    specificity: float
    accuracy: float
    n_train: int
    n_test: int
    timestamp: str
    command: str

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=2)

    @classmethod
    def from_dict(cls, d: dict) -> BenchmarkResult:
        return cls(**d)
