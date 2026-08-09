from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

import numpy as np

DERMAMNIST_SHA256 = "1a309fec2e33bb6aba88e7d078e5ccbb9736c84a0b415ac197eb3c8fa331e050"
MELANOMA_CLASS_ID = 4


@dataclass(frozen=True)
class DatasetSplit:
    images: np.ndarray
    labels: np.ndarray


@dataclass(frozen=True)
class DermaMNIST:
    train: DatasetSplit
    validation: DatasetSplit
    test: DatasetSplit
    sha256: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_dermamnist(
    path: Path,
    *,
    expected_sha256: str | None = DERMAMNIST_SHA256,
) -> DermaMNIST:
    if not path.is_file():
        raise FileNotFoundError(f"DermaMNIST archive is missing: {path}")
    digest = sha256_file(path)
    if expected_sha256 is not None and digest != expected_sha256:
        raise ValueError("DermaMNIST SHA-256 does not match the versioned source manifest")
    with np.load(path, allow_pickle=False) as archive:
        expected = {
            "train_images",
            "train_labels",
            "val_images",
            "val_labels",
            "test_images",
            "test_labels",
        }
        if set(archive.files) != expected:
            raise ValueError("DermaMNIST keys do not match the v2 archive contract")
        dataset = DermaMNIST(
            train=_split(archive["train_images"], archive["train_labels"]),
            validation=_split(archive["val_images"], archive["val_labels"]),
            test=_split(archive["test_images"], archive["test_labels"]),
            sha256=digest,
        )
    if (len(dataset.train.images), len(dataset.validation.images), len(dataset.test.images)) != (
        7007,
        1003,
        2005,
    ):
        raise ValueError("DermaMNIST split counts do not match the official v2 archive")
    return dataset


def binary_labels(labels: np.ndarray) -> np.ndarray:
    return (labels.reshape(-1) == MELANOMA_CLASS_ID).astype(np.int8)


def _split(images: np.ndarray, labels: np.ndarray) -> DatasetSplit:
    if images.ndim != 4 or images.shape[1:] != (28, 28, 3) or images.dtype != np.uint8:
        raise ValueError("DermaMNIST images must be uint8 NHWC 28x28 RGB")
    if labels.shape[0] != images.shape[0]:
        raise ValueError("image and label counts differ")
    if np.any((labels < 0) | (labels > 6)):
        raise ValueError("DermaMNIST labels must be in [0, 6]")
    return DatasetSplit(images=images.copy(), labels=labels.reshape(-1).copy())
