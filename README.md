# #6 melanoma-classifier

**Status:** scaffold

**Proves:** classificacao de lesao de pele.

**Benchmark target:** auc, sensitivity.

**Stack:** python, pytorch, timm, scikit-learn, docker.

## Next milestone

Implement the smallest Docker-runnable version and produce the first JSON benchmark under enchmarks/results/.

## Run

`ash
docker build -t melanoma-classifier .
docker run --rm melanoma-classifier
`

## Benchmark

`ash
docker run --rm melanoma-classifier benchmark
`

| Metric | Value | Unit |
|---|---:|---|
| auc, sensitivity | pending | pending |

## Architecture

Defined in sdd/spec.md before implementation.

## References

See REFERENCES.md.