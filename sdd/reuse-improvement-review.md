# Reuse Improvement Review

Project: `6 - melanoma-classifier`

## Review Points

- [x] after scaffold
- [x] after architecture decision
- [x] after first working slice
- [x] after benchmark result
- [x] before publication

## Findings

| Finding | Classification | Kit Area | Action | Status |
|---|---|---|---|---|
| A medical benchmark needs dataset source, license, archive hash, split sizes and clinical-use limits in one contract. | `patch_now` | medical evaluation standard | Add these fields to the reusable publication and review guidance. | queued in this macro |
| Threshold selection must use validation data only; final test data is evaluation-only. | `patch_now` | medical evaluation standard | Record the leakage boundary as a reusable gate. | queued in this macro |
| A confusion matrix needs the positive-class definition and sample counts beside AUC and sensitivity. | `patch_now` | benchmark contract | Preserve class ID, TN/FP/FN/TP and split counts in machine-readable evidence. | implemented locally; kit patch queued |

## Patch Now Decisions

- Reuse the dataset provenance, licensing, split-isolation and metric-contract rules.
- Reject the removed synthetic generator as reusable medical evidence because its labels controlled its measured visual features.

## Backlog Decisions

- Generalize image-feature extraction only after a second real dataset uses the same representation and tests.

## Rejected Improvements

- DermaMNIST loading, melanoma class ID, pooled RGB features and logistic-regression choices remain project specific.
- The prior synthetic medical fixture and its AUC 1.0 claim are explicitly rejected, not promoted to the kit.

## Final Gate

- [x] Reusable improvements were patched or recorded.
- [x] Project-specific implementation was not moved into the kit.
- [x] Validation reflects the circular-synthetic-score and test-leakage risks discovered here.
