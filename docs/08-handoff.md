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

Local run on the assembled reference checkout: 19 tests passed (the suite was aligned to the two committed test files). The remote GitHub checkout itself was not executed because network/DNS was unavailable in the container; the files were retrieved and written through the GitHub connector. The local sources were assembled from the fetched repository contents and the just-authored changes. A GitHub Actions workflow has now been committed at .github/workflows/tests.yml; remote CI status still needs to be checked.


## Working-tree ingestion update

A bounded read-only filesystem adapter is now implemented at `src/ssg/ingest.py`. It creates repository/directory/file nodes, `contains` edges, file SHA-256 hashes, portable `repo://` source URIs, repository-scoped stable IDs, and a deterministic graph snapshot digest. It excludes common cache/VCS directories, skips symlinks, hashes in chunks, detects simple file mutation during hashing, and enforces node/byte limits.

The example CLI is `examples/scan_directory.py`. Output must be outside the source tree. It emits a simple SVG and JSON manifest. This is **not a Git history adapter**: commits, branches, tags, blame, diffs, Git LFS objects, source parsing, and OCR are not implemented.

Current local test suite: **27 tests passed**; compileall passed; a synthetic scan produced 5 nodes, 4 edges, 2 files, and 2 directories. Remote GitHub Actions status has not been verified.


## Git metadata ingestion — 2026-11-06

A bounded, read-only Git metadata adapter was added at src/ssg/git_ingest.py. It records commits reachable from local refs, parent ancestry, local branches and tags. Shallow or unavailable parent objects are explicit boundary nodes. The adapter uses fixed subprocess argument vectors (no shell), per-command timeouts, prompt suppression and a hard commit cap; it does not checkout, run project code, inspect blobs or mutate the repository.

Tests were added first in tests/test_git_ingest.py and the initial red CI run was observed after the test-only commit. The implementation commit then triggered a new CI run. Its result must be checked before this feature is marked PASS. Remote refs, diff/tree/blob ingestion, blame, LFS and semantic parsing remain NOT IMPLEMENTED.


## Git history adapter — verified

The metadata-only adapter is implemented in src/ssg/git_ingest.py. It models commits, parent edges, local branches/tags and explicit shallow/unavailable boundary nodes. It uses bounded read-only Git commands, no shell, per-command timeouts and fails closed on commit-limit overflow. The graph's repository URI is portable and does not expose the absolute checkout path.

Verification: GitHub Actions run 42167463018 completed SUCCESS. compileall passed and 32 unittest cases passed. This is CI evidence; no local test run was performed in the chat environment. Intermediate quoting failures were corrected and the final commit was rerun successfully.

Still not implemented: remote refs, tree/blob/diff ingestion, rename detection, blame, semantic chunk extraction, OCR, Merkle consistency proofs/signing, and lossless carrier.
