# Reuse Improvement Review

Project: `6 - melanoma-classifier`

## Review Points

- [x] after scaffold
- [x] after architecture decision
- [x] after first working slice
- [x] after benchmark result
- [x] before publication
- [ ] after CI failure, if applicable

## Findings

| Finding | Classification | Kit Area | Action | Status |
|---|---|---|---|---|
| Pillow-based synthetic medical image generator pattern could be reused across medical vision projects | `patch_now` | `component-packs/applied-computer-vision/fixture` | Extracted to kit as reusable medical image fixture module | patched |
| Handcrafted feature extraction for lesion classification follows ABCD rule — reusable baseline | `backlog` | `component-packs/applied-computer-vision/features` | Low priority — will revisit when second medical vision project starts | recorded |
| Benchmark JSON schema (auc, sensitivity, specificity, accuracy) matches stroke-signal-demo pattern | `patch_now` | `harness/benchmark-schema` | Standardized JSON schema across portfolio medical projects | patched |

## Patch Now Decisions

- Created reusable medical image fixture pattern in applied-computer-vision component pack
- Standardized benchmark JSON schema for medical ML projects

## Backlog Decisions

- Handcrafted feature extraction module: revisit when adding a 3rd medical vision project

## Rejected Improvements

- None

## Final Gate

- [x] Reusable improvements were patched or recorded.
- [x] Project-specific implementation was not moved into the kit.
- [x] Validation reflects any repeated mistake discovered during the project.
