from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Evaluation:
    auc: float
    sensitivity: float
    specificity: float
    accuracy: float
    threshold: float
    true_negative: int
    false_positive: int
    false_negative: int
    true_positive: int

    def to_dict(self) -> dict[str, float | int]:
        return asdict(self)
