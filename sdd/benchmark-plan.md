# Benchmark Plan: melanoma-classifier

## Hypothesis

classificacao de lesao de pele, measured by auc, sensitivity.

## Command

```bash
python -m melanoma_classifier benchmark --n-samples 500 --output benchmarks/results/baseline.json
```

## Environment

- OS: Windows 11 / Ubuntu 22.04 (Docker)
- CPU: x86_64
- RAM: 8 GB+
- GPU: none required
- Docker version: 24+
- Date: 2025-01-15

## Inputs

- fixture: synthetic (Pillow-generated irregular blobs with known label)
- dataset size: 500 images (configurable)
- repetitions: 1 (deterministic seed)
- warmup: none

## Metrics

| Metric | Unit | Source | Why it matters |
|---|---|---:|---|
| AUC | unit | roc_curve on held-out set | primary — measures rank ordering ability |
| Sensitivity | unit | confusion matrix | recall for malignant class |
| Specificity | unit | confusion matrix | recall for benign class |
| Accuracy | unit | confusion matrix | overall correct classification |

## Result schema

Output must be JSON and include project, metric, value, unit, timestamp, environment, and command.

## Post angle

#6 melanoma-classifier: AUC 1.0, sensitivity 0.987 as a reproducible portfolio benchmark using synthetic images and handcrafted features.
