# Roadmap and Acceptance Tests

Phase 0: freeze semantics, especially += and =+, and define threat model.
Phase 1: vectors, matrices, rectangles/cuboids, ratio profiles, D4/D8 tests.
Phase 2: stable graph IDs, typed relations, provenance and snapshots.
Phase 3: deterministic multi-scale visual layout, legend, mapping and collision checks.
Phase 4: Git metadata/history ingestion, then Markdown/code/PDF/image parsing and OCR language benchmarks.
Phase 5: deterministic serialization, hashes, hash chain, Merkle inclusion/consistency proofs.
Phase 6: secure lossless carrier with capacity tests, authenticated encryption, error correction and round-trip.
Phase 7: local-first Studio and offline export/import.

Acceptance IDs:
MAT-01 vector operations; MAT-02 rectangle/cuboid formulas; MAT-03 exact ratio precision; MAT-04 D4 orbit; MAT-05 D8 group order 16.
KG-01 edge endpoints; KG-02 stable identity.
PROV-01 chain integrity; PROV-02 tamper detection.
VIS-01 every rendered object maps to a node; VIS-02 no critical clipping.
OCR-01 CER/WER by language.
PACK-01 deterministic serialization; PACK-02 byte-exact round-trip.
CRYPTO-01 modified ciphertext rejected.
RESOURCE-01 bounded memory/time/pixels/nodes.

All tests remain NOT RUN until executed in a real runtime.


## Current execution delta — Git metadata adapter

- GIT-01: enumerate commits reachable from local refs with bounded history — implemented; CI verification pending.
- GIT-02: preserve parent ancestry and shallow boundaries — implemented; CI verification pending.
- GIT-03: represent local branches/tags and their targets — implemented; CI verification pending.
- GIT-04: fail closed on non-repositories, timeouts and commit-cap overflow — implemented; CI verification pending.
- GIT-05: remote refs, diffs, trees/blobs, rename detection and blame — NOT IMPLEMENTED.


### Git metadata ingestion — final gate
- GIT-01 bounded local commit enumeration: PASS (GitHub Actions).
- GIT-02 parent ancestry and explicit shallow boundaries: PASS (GitHub Actions).
- GIT-03 local branch/tag references: PASS (GitHub Actions).
- GIT-04 invalid repository and commit-cap rejection: PASS (GitHub Actions).
- GIT-05 portable repository URI: PASS (GitHub Actions).
- Verification run: 42167463018; compileall PASS; 32 tests PASS.
- Remote refs, diffs, trees/blobs, rename detection and blame: NOT IMPLEMENTED.
