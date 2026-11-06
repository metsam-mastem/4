# Technical Handoff

## Scope and accepted decisions
SSG is user-originated. Working name: Symbolic Systems Grammar. Accepted: D4 + D8 + Adaptive; graph-first canonical knowledge with tree views; hybrid standard crypto plus keyed glyph presentation; SOURCE → KNOWLEDGE GRAPH → VISUAL SHADOW → RECONSTRUCTION; source preservation; multi-scale posters; math proportion profiles; append-only provenance and Merkle-inspired verification.

## Unresolved
- Final name/grammar semantics.
- Meanings of += and =+.
- Exact lossless carrier format and threat model.
- Source adapters and file-size limits.
- License and key custody.
- Persian/Arabic OCR benchmark.
- Adaptive layout weights.
- D8 convention is fixed here as the 16-element symmetry group of a regular octagon.

## Implementation boundary
Initial reference core aims to cover vector/rectangle/cuboid math, proportion profiles, graph validation, hash-chain provenance, and SVG overview. It is not a full parser, Git crawler, OCR pipeline, encrypted image carrier, or production app.

## Developer onboarding
Read README, architecture, mathematical foundations, and this handoff. Run python -m unittest discover -s tests. Add tests before changing behavior. Preserve original source and provenance. Update docs/REPORT-LOG.md after meaningful changes. Do not mark tests PASS without execution.

## Status
Repository metsam-mastem/4 confirmed. Initial README commit created. Remaining files and tests are to be verified against actual repository state. Runtime tests NOT RUN unless evidence is recorded.

## Implementation update — 2026-11-06

Implemented in the reference core:
- D8 regular-octagon dihedral transforms: 16 orthogonal matrices (8 rotations + 8 reflections).
- Matrix application to Vec2.
- Vec3 operations: addition, subtraction, dot, cross, norm, normalization (zero-vector rejection).
- Directed in-degree/out-degree and directed simple-graph density.
- Domain-separated Merkle root, inclusion proof, and proof verification.
- Hash-chain validation with optional trusted expected_head checkpoint.
- Advanced acceptance tests for group closure, norm preservation, odd-leaf Merkle proofs, tamper rejection, Vec3, and graph metrics.

Local run on the assembled reference checkout: 26 tests passed. The remote GitHub checkout itself was not executed because network/DNS was unavailable in the container; the files were retrieved and written through the GitHub connector. The local sources were assembled from the fetched repository contents and the just-authored changes. Treat remote CI as NOT RUN until a GitHub Actions run or an actual clone test is available.
