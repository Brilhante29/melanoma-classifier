# Benchmark Plan

- Question: melanoma class ID 4 versus the other six DermaMNIST classes.
- Train: 7,007 official images.
- Validation: 1,003 images; maximize specificity subject to sensitivity >= 0.8.
- Test: 2,005 images, used only for final evidence.
- Primary: test ROC AUC.
- Secondary: sensitivity, specificity, accuracy, confusion matrix, duration.
- Failure: wrong dataset hash/shape/count, missing class, non-finite metric, or runtime network dependency.

The baseline is CPU logistic regression over 14x14 pooled RGB values and channel moments. A more complex model must use the same split and comparability key family.
