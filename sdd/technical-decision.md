# Technical Decision

The old generator encoded malignant labels into darker, more irregular shapes and the classifier measured those same features. AUC 1.0 was circular and was removed.

DermaMNIST v2.1 is selected because its fixed 28x28 archive is small enough to version, has official train/validation/test splits, published checksums, and explicit educational licensing. The logistic regression baseline is intentionally modest and interpretable. The result is evidence of methodology and generalization on this benchmark, not clinical safety.

Deep learning is deferred because this repository first needed a valid dataset and evaluation boundary. It becomes justified when compared against this baseline with fixed splits, three seeds, calibration, subgroup analysis, and measured compute.
