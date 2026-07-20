# Architecture Decision

## Status

Accepted

## Context

Project: `melanoma-classifier`
Claim: `classificacao de lesao de pele`
Benchmark: `AUC, sensitivity`

Problem forces:

- Domain complexity: low
- Integration pressure: low
- UI state complexity: none
- Data/ML reproducibility: high
- Auditability/event history: medium
- Throughput/async pressure: low
- Independent deployability need: low

## Decision

Chosen architecture: `pipeline`

Reason:

Synthetic image generation, feature extraction, classifier training, and evaluation form a natural four-stage pipeline. Each stage has a single responsibility and produces output consumed by the next stage. This matches the benchmark flow exactly — generate data, extract features, train model, evaluate — with no unnecessary indirection.

Dependency rule:

fixture depends only on Pillow/numpy; feature extraction depends on numpy/scipy/Pillow; classifier depends on scikit-learn; CLI depends on argparse; benchmark orchestrates the full pipeline.

## Rejected Alternatives

| Alternative | Why rejected |
|---|---|
| hexagonal | No infrastructure or transport boundary to justify ports/adapters |
| microservices | Single-machine classification pipeline has no deployment boundary |

## Folder Layout

```txt
src/
  melanoma_classifier/
    __init__.py
    __main__.py
    domain.py       # pure dataclasses
    fixture.py      # synthetic lesion image generator
    classifier.py   # feature extraction + sklearn classifier
    benchmark.py    # benchmark orchestrator
    cli.py          # argparse CLI
tests/
  test_domain.py
  test_classifier.py
benchmarks/
  results/
    baseline.json
```

## Testing Strategy

- Unit tests: domain type round-trips, feature extraction shape/validity, classifier train/predict
- Integration tests: full pipeline from synthetic image to classification (within tests)
- Benchmark: end-to-end with 500 samples, measures AUC/sensitivity/specificity

## Consequences

Positive:

- Simple four-stage pipeline is easy to understand, test, and debug.
- No GPU or deep learning dependency reduces build time and Docker image size.
- Deterministic seed ensures fully reproducible benchmark results.

Tradeoffs:

- Handcrafted features may not generalize to real clinical images, but this is acceptable for a synthetic benchmark proving the pipeline pattern.

Migration path:

- Replace fixture.py with real ISIC dataset loader for production use.
- Replace handcrafted features with a CNN feature extractor (via TIMM) when higher accuracy is needed.
