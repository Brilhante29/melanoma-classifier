# Benchmark Proof

- Dataset: DermaMNIST v2.1, class ID 4 versus all other classes.
- Official split sizes: 7,007 train, 1,003 validation and 2,005 test images.
- Primary metric: test ROC AUC.
- Raw evidence: `benchmarks/results/baseline.json`.
- Publication evidence: `benchmarks/publication/melanoma-baseline-v2.json`.
- Workload: one deterministic run over all 2,005 test images.
- Measured baseline: AUC `0.7370`, sensitivity `0.7623`, specificity `0.5988`, accuracy `0.6170`.

The dataset archive hash, source, license, configuration, dependency lock, source commit and OCI image digest must be machine-verifiable before publication.
