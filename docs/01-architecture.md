# Architecture Specification — 0.4.0 draft

## Layers
1. Source adapters: Git, filesystem, Markdown, PDF, image, code, database.
2. Extraction: parsers, OCR, metadata, chunking, language detection.
3. Canonical knowledge graph: stable nodes, typed edges, source locators, versions, claims, evidence.
4. Mathematics: vectors, matrices, coordinate frames, rectangles, cuboids, graph metrics.
5. Projection: tree, graph, radial, grid, fractal, poster, timeline.
6. Encoding/package: deterministic serialization and optional lossless binary payload.
7. Security: hashes, authenticated encryption, signatures, key references.
8. Decoder/reconstruction: decode, verify, restore or navigate to source.
9. Studio/API: navigator, inspector, provenance panel, validation console.

## Data flow
Source → Extract → Normalize → Canonical Graph → Measure → Project → Render → Package.
Lossless reverse path: Package → Parse Manifest → Verify → Decrypt if authorized → Decode → Verify original hash → Restore.

## Canonical graph
G=(V,E,τV,τE). Node fields: id, type, label, source URI/repository/path/line/page, content hash, version, dimensions, provenance, timestamps. Edge fields: id, source ID, target ID, relation type, evidence locator, confidence, method, version.

## Projection contract
Each projection stores graph snapshot hash, algorithm/version, parameters, math profile, viewport/coordinate frame, lossiness classification, and mapping from rendered objects to source node IDs.

## Security boundary
Glyph keys do not encrypt. Manifests contain key IDs, never secret key material. Use established cryptographic libraries; do not invent ciphers.
