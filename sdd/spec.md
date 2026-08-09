# Spec: DermaMNIST melanoma evaluation

## Claim

Measure a transparent melanoma-vs-rest baseline on real dermatoscopic images using official train, validation, and test splits without selecting the threshold on test data.

## Acceptance

- Verify the exact DermaMNIST v2.1 SHA-256 and six NPZ keys.
- Enforce official split counts 7,007 / 1,003 / 2,005.
- Train only on train and select threshold only on validation.
- Report test AUC, sensitivity, specificity, accuracy, and confusion counts.
- Preserve dataset license and non-clinical limitation.
- Run offline in one non-root Docker container.

## Non-Goals

- Clinical diagnosis, calibration, fairness, treatment advice, or medical-device claims.
- Fabricating a high score through synthetic labels or test-set tuning.
