# Agent Handoff

This file stores observable state, not private reasoning.

- Project: `6 - melanoma-classifier`.
- Program: `applied-computer-vision`.
- Status: published.
- Dataset: DermaMNIST v2.1, SHA-256 `1a309fec2e33bb6aba88e7d078e5ccbb9736c84a0b415ac197eb3c8fa331e050`, CC BY-NC 4.0.
- Result: AUC `0.736999`; sensitivity `0.762332`; specificity `0.598765`; test size 2,005.
- V2: source `feb0c3fd8b10d3144df74808f489956967c8457d`, image `sha256:d2c10ac74664033741a3ce6b44862af0246ce4a701942d7e5945ea0e25477db4`.
- Source CI: run `31341452550` passed.
- Method: official train/validation/test splits; threshold selected on validation only.
- Safety: educational benchmark, not intended for clinical use.

Do not restore the circular synthetic generator, test-set threshold tuning or AUC 1.0 claim. The central registry records final publication CI.
