# Blockchain-Inspired Provenance

Borrow verifiable append-only history, content addressing, hash chaining, Merkle proofs, and signed checkpoints. Do not imitate token economics, mining, or public consensus without a real multi-party trust requirement.

Content hash: hi=H(canonical(artifacti)).
Hash chain: ci=H(ci-1 || hi || metadatai).
Merkle leaf: Li=H(0x00 || datai).
Merkle parent: N=H(0x01 || left || right).

Use domain separation, canonical serialization, and versioned hash algorithms.

Each provenance record includes artifact ID, source URI/repository/path, source commit/blob hash, parent artifact IDs, transform ID/version, input/output hashes, actor/tool, timestamp, signature/key ID when used, and evidence locator.

Git already supplies version history. A portable Merkle log can add efficient inclusion and consistency proofs. A hash does not prove authorship or truth; signatures address authorship under a key trust model. A Merkle root must be anchored in a trusted checkpoint to be meaningful.

Recommended first mode: local-first Git-backed append-only journal + content hashes + optional signed checkpoints. No token, mining, validator network, or public chain in prototype.

## Implemented Merkle convention (SSG reference core)

The current reference implementation uses domain separation:
- leaf: SHA-256(0x00 || leaf_bytes)
- parent: SHA-256(0x01 || left_hash || right_hash)
- empty tree root: SHA-256(0x02)

At every level with an odd number of hashes, the final hash is duplicated. Inclusion proofs carry the sibling side and sibling digest. This is a deliberately simple SSG convention and is **not claimed to be RFC 6962-compatible**. Any future protocol standardization must freeze this tree-shape rule and publish cross-language test vectors.

The hash-chain verifier now accepts an optional expected_head. Without a trusted or signed checkpoint containing that head, rewriting only the final journal event cannot be detected from the chain alone.
