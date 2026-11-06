# Source Ingestion — Working-Tree Adapter

## Purpose

Build a read-only structural snapshot of a local project folder. The first adapter creates repository, directory, and file nodes; \`contains\` edges; portable source URIs; content hashes; and a deterministic graph snapshot hash.

This is a filesystem working-tree adapter, **not yet a Git history adapter**. It does not inspect commits, branches, tags, blame, or diffs. It does not parse source-code semantics or OCR documents.

## Guarantees

- Files are read as bytes in chunks; file contents are not copied into the graph.
- SHA-256 content hashes are stored for regular files.
- IDs are deterministic from repository namespace, node type, and relative path; they do not depend on absolute checkout location.
- An explicit \`repository_id\` prevents collisions between same-named repositories.
- Directory and file ordering is deterministic.
- \`.git\`, Python caches, virtual environments, and common dependency folders are excluded by default.
- Symlinked files/directories are skipped; the adapter never follows them.
- A file whose size/mtime/ctime changes during hashing causes ingestion to fail rather than produce a potentially inconsistent node.
- Hard limits apply to node count and total bytes. Hitting a limit fails the entire ingestion; it never returns a silently truncated graph.

## Default limits

- 100,000 nodes (including repository and directory nodes).
- 20 GiB total regular-file bytes.
- 1 MiB hash chunk.
- Common excluded directories: \`.git\`, \`__pycache__\`, \`.venv\`, \`venv\`, \`node_modules\`, \`.pytest_cache\`, \`.mypy_cache\`.

All limits can be overridden by API arguments and CLI options.

## Run

From repository root:

\`\`\`bash
PYTHONPATH=src python examples/scan_directory.py /path/to/project \\
  --repository-id owner/project \\
  --revision <commit-sha-or-working-tree-label> \\
  --output /path/outside/source
\`\`\`

The output directory must be outside the source tree. The example writes:
- \`visual-shadow.svg\`: current simple graph overview.
- \`snapshot-manifest.json\`: snapshot hash, revision label, node/edge/file/directory counts, and lossiness declaration.

## Identity and provenance

Node ID function:
\`SHA256("ssg-node-v1" || NUL || repository_id || NUL || node_type || NUL || relative_path)\`

Only a shortened prefix is used for the ID. The full file content hash remains separate. A path rename creates a new logical node ID; a future rename detector may link old and new nodes through a \`renamed_to\` provenance relation.

The source URI shape is \`repo://<encoded-repository-id>/<relative-path>\`. It identifies the logical source within a repository namespace; it is not a public network URL.

## Snapshot hash

The graph snapshot hashes sorted node and edge records in canonical JSON. It includes source URI/version, labels, metadata, file content hashes, edge relations, and confidence values. Invalid graphs or non-canonical metadata are rejected.

## Limitations

- A working-tree scan is not an atomic filesystem snapshot. The adapter detects simple file mutations during hashing but cannot guarantee a globally atomic view while other processes change the tree.
- Symlinks are omitted rather than represented.
- Submodules appear as directories unless separately scanned.
- Git LFS pointer files are hashed as pointer text; LFS objects are not downloaded.
- Ignored files are still included unless they are in the explicit excluded-directory list.
- File-level content hashes do not yet establish semantic similarity or document relationships.
- The SVG renderer is currently a compact overview, not a full multiscale interactive atlas.

## Acceptance coverage

The ingestion tests cover nested trees, file hashing, source URI construction, stable IDs across checkout locations, distinct repository namespaces, \`.git\`/symlink exclusion, node and byte limits, deterministic snapshot hashing, and content-hash sensitivity.
