# Architecture Record

## Decision

Use a deterministic evaluation pipeline: archive integrity -> split contract -> vectorized feature extraction -> class-balanced logistic regression -> validation-only threshold selection -> test-only evaluation -> V1/V2 evidence.

## Boundaries

- Dataset integrity and split validation do not import the estimator.
- Feature extraction transforms arrays and owns no labels or split policy.
- Model training receives training data only.
- Threshold selection receives validation scores only.
- Test evaluation cannot influence fitting or threshold selection.

## Rejected Alternatives

- A synthetic medical fixture was rejected because labels controlled the same visual features measured by the classifier.
- Deep learning and GPU infrastructure were rejected because the first claim is evaluation rigor, not state-of-the-art accuracy.
- API, database, broker and cloud services were rejected because they add no evidence to this offline benchmark.
