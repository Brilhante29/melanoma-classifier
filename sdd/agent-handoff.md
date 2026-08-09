# Agent Handoff

This file stores observable state, not private reasoning.

- Project: `6 - melanoma-classifier`.
- Program: `applied-computer-vision`.
- Status: benchmarked; V2 publication is pending.
- Dataset: DermaMNIST v2.1, SHA-256 `1a309fec2e33bb6aba88e7d078e5ccbb9736c84a0b415ac197eb3c8fa331e050`, CC BY-NC 4.0.
- Baseline: AUC `0.736999`; sensitivity `0.762332`; specificity `0.598765`; test size 2,005.
- Method: official train/validation/test splits; threshold selected on validation only.
- Safety: not intended for clinical use.

Continue with unit tests, benchmark validator, publication provenance, Docker offline run, and exact-head CI. Do not restore the synthetic lesion generator or AUC 1.0 claim.
