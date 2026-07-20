# Spec: melanoma-classifier

## Number

#6

## Claim

Este projeto prova que: classificacao de lesao de pele.

## Stack

python, pillow, numpy, scikit-learn, scipy, docker

## User-visible output

- Docker command: `docker run --rm melanoma-classifier`
- README opens with: `# #6 melanoma-classifier`
- Benchmark table: auc, sensitivity

## Scope

In:

- Implementar o menor produto funcional que prove o claim.
- Rodar por Docker.
- Gerar benchmark JSON reproduzivel.

Out:

- Publicar repo antes do primeiro resultado numerico.
- Depender de segredo pago para o caminho default.
- Deep learning (PyTorch/TIMM). GPU training.

## Architecture

```
synthetic fixture -> feature extraction -> sklearn classifier -> evaluation -> JSON output
```

## Benchmark

Primary metric:

- name: auc, sensitivity
- target: >0.75 AUC on synthetic held-out set
- command: `python -m melanoma_classifier benchmark --n-samples 500 --output benchmarks/results/baseline.json`
- result file: `benchmarks/results/baseline.json`

## Dataset or fixture

- source: synthetic (Pillow-generated irregular blobs)
- size: configurable (default 500)
- license: MIT (generated code, no real data)
- deterministic seed: 42

## Definition of done

- [x] Docker command works from clean clone.
- [x] README starts with project number and benchmark result.
- [x] Benchmark command writes JSON result.
- [x] Tests cover core behavior.
- [x] REFERENCES.md explains reuse.
- [x] No secret or paid credential required for default demo.
