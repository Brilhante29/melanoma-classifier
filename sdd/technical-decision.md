# Technical Decision

## Status

Accepted

## Decision Type

stack

## Context

Project: `melanoma-classifier`
Problem: Classify synthetic skin lesion images as malignant or benign using reproducible ML pipeline
Portfolio program: applied-computer-vision
Public signal: GitHub portfolio demonstrating medical vision classification with synthetic data
Benchmark: AUC, sensitivity

## Selected Option

Selected: `scikit-learn LogisticRegression on handcrafted image features`

Reason:

Handcrafted features (asymmetry index, border irregularity, color variance, area, perimeter, circularity) encode domain knowledge from the ABCD rule of dermatology. LogisticRegression is fast, interpretable, and requires no GPU. This combination proves the classification claim without the overhead of deep learning.

## Decision Brain Fields

- Stack profile: python-ml
- API style: cli
- Messaging: none
- Cloud mode: none
- Database/runtime: none / Python CLI on Docker
- Library policy: Pillow for image generation, numpy/scipy for feature computation, scikit-learn for classification/metrics

## Engineering Principles

Coupling boundary:

Domain types depend only on standard library; feature extraction depends only on numpy/Pillow/scipy; classifier depends on scikit-learn; CLI depends on argparse.

SOLID application:

- SRP: fixture generates images, classifier extracts features and trains, benchmark orchestrates
- OCP: add new features by extending extract_features(), new models by adding train_* functions
- LSP: ClassificationResult and BenchmarkResult are frozen dataclasses — no substitution needed
- ISP: small focused functions with narrow interfaces (extract_features returns ndarray, train_classifier returns Pipeline)
- DIP: high-level benchmark depends on abstract feature extraction and training functions, not concrete implementations

Simplicity:

- KISS: generate blobs, compute 9 numeric features, train LogisticRegression — simplest design that proves the claim
- YAGNI: no async, no web API, no database, no GPU — not needed for a reproducible benchmark
- DRY: feature extraction logic lives in one place; benchmark orchestration in one function

Testability evidence:

- domain.py tested via round-trip serialization
- classifier.py tested via feature extraction on known synthetic images + train/predict accuracy check

## Rejected Options

| Option | Why rejected |
|---|---|
| PyTorch/TIMM classifier | Requires GPU, increases Docker image size, adds training time. Handcrafted features + sklearn is sufficient for the benchmark. |
| Real ISIC dataset | Introduces network dependency, licensing issues, and non-deterministic results. Synthetic data is fully reproducible. |

## API Contract

Contract artifact:

CLI output schema — JSON benchmark result with fields: auc, sensitivity, specificity, accuracy, n_train, n_test, timestamp, command.

## Cloud Local-First

Local provider: none

Real provider target: none

Config switch: none

Unsupported local behaviors: none

## Benchmark Impact

Expected impact:

- AUC > 0.75 on held-out synthetic test set proves the classification pipeline works.

Validation command:

```powershell
python -m melanoma_classifier benchmark --n-samples 500 --output benchmarks/results/baseline.json
```

## Operational Cost

- Docker services added: none (single-stage build)
- Local demo complexity: low
- Failure case required: no

## Follow-up

- If AUC drops below 0.75 on new synthetic distributions, add more features or switch to RandomForest.
