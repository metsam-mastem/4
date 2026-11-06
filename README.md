# SSG — Symbolic Systems Grammar

> A multidimensional symbolic language, knowledge-graph model, and reversible visual projection system.

**Project status:** specification + first prototype scaffold. This repository is the canonical home for SSG.

## North star

`SOURCE → KNOWLEDGE GRAPH → VISUAL SHADOW → RECONSTRUCTION`

SSG separates source truth from its views. A Git repository, document collection, or dataset is ingested into a canonical graph with stable identities, provenance, relations, and versions. The graph can then be projected into tree, graph, poster, fractal, and interactive views. Lossless reconstruction is a separate, testable capability; a decorative visualization is never claimed to be a backup.

## Accepted architecture decisions

- Symmetry: configurable engine with D4, D8, and adaptive profiles.
- Knowledge: graph-first canonical model; tree and other views are projections.
- Security: hybrid design — standard cryptography for confidentiality/integrity, keyed glyph mappings for visual presentation only.
- Visual Shadow: multi-scale, multi-channel projection with source-to-output traceability.
- Repository destination: `metsam-mastem/4`.

## Mathematical design principles

- Rectangles: square, √2, √3, √5, golden-ratio and user-defined families.
- Cuboids: independent aspect ratios on three axes; volume and surface metrics.
- Fibonacci: optional composition/grid sequence, never a universal law.
- π: circular, angular, and radial layouts.
- Prime numbers: deterministic indexing/sharding/visual sampling, not aesthetic proof.
- Irrational constants: exact symbolic definitions retained; approximations carry precision metadata.
- Vectors, matrices, graphs, and geometry are separate typed layers.

## Safety and correctness

- Never confuse glyph obfuscation or fractal rendering with encryption.
- Use established cryptographic libraries and authenticated encryption (e.g. AES-GCM); do not invent ciphers.
- Preserve originals and provenance.
- Every transform declares whether it is lossless or lossy.
- Verify round trips with hashes and explicit acceptance tests.
- Keep source data, visual projections, and cryptographic payloads separate.

## Repository map

- `docs/`: specification, math, research, handoff, and work journal.
- `src/ssg/`: dependency-free Python reference core.
- `tests/`: automated tests.
- `assets/`: SVG visual identity and poster prompt.
- `schemas/`: JSON schemas for project data and manifests.

## Status labels

- **PASS**: executed and evidence recorded.
- **FAIL**: executed and failed.
- **NOT RUN**: not executed.
- **BLOCKED**: could not execute because of a dependency or environment constraint.

At this stage, implementation and test claims must be marked **NOT RUN** until executed in a real runtime.

## License

TBD — do not assume reuse rights until a license is selected.

## Current implemented reference core

The Python reference core includes Vec2/Vec3, rectangle and cuboid metrics, proportion constants, Fibonacci, D4/D8 symmetry transforms, graph validation and directed metrics, hash-chain provenance, Merkle inclusion proofs, and a small SVG graph renderer.

Run locally:
`PYTHONPATH=src python -m unittest discover -s tests -v`

The Visual Shadow poster is in `assets/visual-shadow-atlas.svg`. It is a vector architecture map, not a payload-carrying lossless image.
