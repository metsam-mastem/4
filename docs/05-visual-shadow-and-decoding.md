# Visual Shadow Engine and Reconstruction

The visual shadow is a projection, like tracing a hand's silhouette: it shows selected boundaries and relations, not the original object.

## Three products
1. Semantic poster: human-oriented and generally lossy.
2. Interactive atlas: visual objects link to source IDs and exact source locations.
3. Lossless visual carrier: formally specified image-based data carrier with payload blocks, manifest, error correction, and integrity data.

A poster is not automatically a backup. OCR from a screenshot is not lossless. For exact restoration, encode original bytes as data rather than relying on visible glyphs.

## Visual channels
Hue=domain; luminance=declared importance/activity; saturation=confidence or status; geometry=node role; size=declared quantity; texture=provenance/state; position=graph/tree/timeline coordinates; edges=typed relations; depth=layer/zoom; pattern frequency=optional metric. Every channel requires a legend.

## Multi-scale atlas
L0 project overview; L1 domains/modules; L2 files/documents; L3 symbols/sections/functions; L4 exact source spans or byte blocks. Use tiled rendering and preserve node IDs.

## Lossless carrier pipeline
Original bytes → deterministic serialization → optional compression → optional authenticated encryption → framing → error-correction coding → image modulation.
Decoder reverses every stage and verifies manifest, block order, completeness, error correction, AEAD tag, payload hash, and original file hashes.

## Shift-register-inspired transforms
A shift register may permute or schedule bit/byte positions if its state and inverse are specified. It is a reversible transform, not encryption. Do not use it as a substitute for AES-GCM or a cryptographic random generator.

## Keys
Kenc encryption; Ksig signing; Kglyph visual mapping; Ksem semantic interpretation; Kpack package/framing. Use standard KDFs only with correctly defined key material, salt, context, and lengths. Keep secrets outside manifests.

## Poster narrative
Include legend, project synopsis, graph topology, timeline, important nodes, unresolved questions, and evidence links. Generated prose is a summary, not source truth.
