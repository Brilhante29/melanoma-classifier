# #6 melanoma-classifier

**Status:** benchmarked

**Proves:** classificacao de lesao de pele via synthetic image generation, handcrafted feature extraction, and sklearn classification.

**Benchmark result (500 synthetic samples, held-out 30%):**

| Metric | Value |
|---|---:|
| AUC | 1.0 |
| Sensitivity | 0.9873 |
| Specificity | 1.0 |
| Accuracy | 0.9933 |

**Stack:** python, pillow, numpy, scikit-learn, scipy, docker (no GPU required)

## Quick Start

```bash
pip install -e .
python -m melanoma_classifier demo
```

## Run

```bash
docker build -t melanoma-classifier .
docker run --rm melanoma-classifier
```

## Benchmark

```bash
python -m melanoma_classifier benchmark --n-samples 500 --output benchmarks/results/baseline.json
```

Or via Docker:

```bash
docker run --rm melanoma-classifier benchmark --n-samples 500 --output /app/benchmarks/results/baseline.json
```

## Architecture

Pipeline: `synthetic fixture -> extract 9 handcrafted features -> LogisticRegression -> evaluation`

Features follow the ABCD rule: asymmetry, border irregularity, color variance, diameter (area/perimeter/circularity).

## Tests

```bash
pytest tests/ -v
```

## References

See REFERENCES.md. Implementation, fixtures, and results are project-specific.

## Post Angle

#6 melanoma-classifier: AUC 1.0, sensitivity 0.987 as a reproducible portfolio benchmark using synthetic images and handcrafted features — no GPU, no real data, no secrets.
