from __future__ import annotations

from pathlib import Path

import numpy as np

from melanoma_classifier.dataset import binary_labels, load_dermamnist


def test_loader_rejects_non_official_split_counts(tmp_path: Path) -> None:
    path = tmp_path / "tiny.npz"
    images = np.zeros((2, 28, 28, 3), dtype=np.uint8)
    labels = np.array([[4], [0]], dtype=np.uint8)
    np.savez(
        path,
        train_images=images,
        train_labels=labels,
        val_images=images,
        val_labels=labels,
        test_images=images,
        test_labels=labels,
    )
    try:
        load_dermamnist(path, expected_sha256=None)
    except ValueError as error:
        assert "split counts" in str(error)
    else:
        raise AssertionError("tiny archive must not pass the official dataset contract")
    assert binary_labels(labels).tolist() == [1, 0]
