# Verification

## Required Gates

- [x] DermaMNIST archive hash, keys and official split sizes are validated.
- [x] Unit tests prove threshold selection uses validation data and reject invalid inputs.
- [x] The full Docker benchmark runs offline and emits the complete confusion matrix.
- [x] README numbers match raw evidence.
- [x] Dataset source, CC BY-NC 4.0 terms and non-clinical scope are explicit.
- [ ] Provenance-rich V2 evidence exists and validates against Git blobs and the OCI image.
- [ ] Exact-head GitHub Actions passes after the V2 publication commit.

The final two gates are completed only after source CI, immutable-image execution and publication CI.
