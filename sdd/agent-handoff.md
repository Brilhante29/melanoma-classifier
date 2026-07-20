# Agent Handoff

Project: `6 - melanoma-classifier`

## Principal Agent Summary

- Objective: Implement synthetic skin lesion classification benchmark demonstrating reproducible ML pipeline
- Portfolio program: applied-computer-vision
- Public proof claim: classificacao de lesao de pele
- Primary benchmark: AUC
- Default runnable path: `docker run --rm melanoma-classifier`

## Subagent Decisions

| Role | Decision | Evidence Path | Status |
|---|---|---|---|
| `program-planner` | applied-computer-vision | `project.yaml`, `sdd/spec.md` | done |
| `architecture-selector` | pipeline (fixture -> features -> classifier -> eval) | `sdd/architecture-decision.md` | done |
| `engineering-principles-reviewer` | SOLID applied, KISS followed | `project.yaml`, `sdd/technical-decision.md` | done |
| `stack-decision-agent` | python, scikit-learn, pillow, numpy, scipy | `project.yaml`, `sdd/technical-decision.md` | done |
| `api-style-agent` | CLI (argparse subcommands: demo, benchmark) | `cli.py` | done |
| `cloud-local-first-agent` | none — no cloud dependency | Dockerfile | done |
| `messaging-agent` | none | `sdd/technical-decision.md` | done |
| `language-profile-agent` | python-ml | repo layout, tests | done |
| `benchmark-harness-agent` | 500 samples, AUC/sensitivity JSON output | `sdd/benchmark-plan.md`, `benchmarks/results/baseline.json` | done |
| `design-system-agent` | README with number, claim, benchmark card | `README.md` | done |
| `security-reuse-reviewer` | no secrets, MIT license, referenced PIL/sklearn | `REFERENCES.md`, release checklist | done |
| `release-ci-publisher` | CI passing, Docker build, tests green | `.github/workflows/ci.yml` | done |

## Local-First Runtime

- Docker command: `docker run --rm melanoma-classifier`
- Local services: none
- Kumo services, if any: none
- Real cloud adapter target, if any: none
- Config switch: none
- Default path requires paid secret: no

## Architecture Boundaries

- Domain boundaries: domain.py (pure types)
- Use-case boundaries: benchmark.py orchestrates the pipeline
- Ports: none (direct function calls)
- Adapters: none
- Dependency direction rule: fixture -> classifier -> benchmark -> CLI

## Benchmark Handoff

- Metric: AUC
- Unit: unit
- Higher or lower is better: higher
- Command: `python -m melanoma_classifier benchmark --n-samples 500 --output benchmarks/results/baseline.json`
- Result path: `benchmarks/results/baseline.json`
- Dataset or fixture: synthetic Pillow-generated skin lesions

## Open Risks

- None — synthetic data is deterministic and fully controlled.

## Publication Gates

- [x] Docker path works
- [x] benchmark result exists
- [x] README starts with number, claim, and benchmark
- [x] references are documented
- [x] no secret in files or git remote
- [x] validation passes
