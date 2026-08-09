# Reuse Map: #6 melanoma-classifier

| Kit input or delta | Use | Resolution |
|---|---|---|
| Python ML and computer-vision profiles | package, test and Docker conventions | reused |
| medical evaluation contract | class definition, AUC, sensitivity and confusion matrix | improve kit now |
| dataset provenance contract | source, license, archive hash and split sizes | improve kit now |
| validation/test isolation | prevent threshold leakage | improve kit now |
| DermaMNIST loader and image features | specific to this baseline | keep local |
| removed synthetic medical generator | produced circular AUC 1.0 | reject from reuse |

Only evidence and leakage-prevention rules are reusable. Dataset-specific transformations and estimator choices remain local.
