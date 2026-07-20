from __future__ import annotations

import math
import random
from typing import Any

import numpy as np
from PIL import Image, ImageDraw


def _random_polygon(
    cx: float, cy: float, n_vertices: int, radius: float, asymmetry: float
) -> list[tuple[float, float]]:
    angles = sorted([random.random() * 2 * math.pi for _ in range(n_vertices)])
    pts = []
    for a in angles:
        r = radius * (0.5 + 0.5 * random.random())
        if asymmetry > 0:
            r *= 1.0 + asymmetry * (math.sin(a * 2) * 0.3 + math.cos(a * 3) * 0.2)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def _vary_color(base_color: tuple[int, int, int], deviation: int = 30) -> tuple[int, int, int]:
    r = max(0, min(255, base_color[0] + random.randint(-deviation, deviation)))
    g = max(0, min(255, base_color[1] + random.randint(-deviation, deviation)))
    b = max(0, min(255, base_color[2] + random.randint(-deviation, deviation)))
    return (r, g, b)


def generate_synthetic_lesion(
    image_size: int = 128,
    label: int | None = None,
    seed: int | None = None,
) -> tuple[Any, int]:
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    if label is None:
        label = 1 if random.random() < 0.5 else 0

    img = Image.new("RGB", (image_size, image_size), (240, 220, 200))
    draw = ImageDraw.Draw(img)

    cx, cy = image_size / 2, image_size / 2

    if label == 1:
        base_color = (80 + random.randint(0, 40), 30 + random.randint(0, 20), 20 + random.randint(0, 15))
        n_blobs = random.randint(2, 4)
        radius = image_size * 0.2
        asymmetry = 0.3 + random.random() * 0.4
    else:
        base_color = (210 + random.randint(0, 40), 170 + random.randint(0, 30), 150 + random.randint(0, 30))
        n_blobs = random.randint(1, 2)
        radius = image_size * 0.15
        asymmetry = random.random() * 0.2

    for _ in range(n_blobs):
        offset_x = random.uniform(-radius * 0.4, radius * 0.4)
        offset_y = random.uniform(-radius * 0.4, radius * 0.4)
        n_vertices = random.randint(6, 12)
        blob_radius = radius * (0.7 + 0.6 * random.random())
        pts = _random_polygon(
            cx + offset_x, cy + offset_y, n_vertices, blob_radius, asymmetry
        )
        color = _vary_color(base_color)
        draw.polygon(pts, fill=color)

        if label == 1:
            inner_pts = _random_polygon(
                cx + offset_x + random.uniform(-5, 5),
                cy + offset_y + random.uniform(-5, 5),
                n_vertices,
                blob_radius * 0.5,
                asymmetry * 0.7,
            )
            inner_color = _vary_color(
                (base_color[0] + 20, base_color[1] + 10, base_color[2] + 5)
            )
            draw.polygon(inner_pts, fill=inner_color)

    return img, label
