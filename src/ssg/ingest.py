"""Bounded, read-only filesystem ingestion into an SSG knowledge graph.

This adapter builds a working-tree snapshot. It does not read Git history,
execute repository code, follow symlinks, or extract semantic source content.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
from urllib.parse import quote

from .graph import Edge, KnowledgeGraph, Node

DEFAULT_EXCLUDED_DIRS = frozenset({".git", "__pycache__", ".venv", "venv", "node_modules", ".pytest_cache", ".mypy_cache"})


class IngestionError(RuntimeError):
    """Raised when a source tree cannot be safely or completely ingested."""


def stable_node_id(repository_id: str, node_type: str, relative_path: str) -> str:
    """Build a stable logical ID independent of the absolute checkout path."""
    if not repository_id or not node_type or not relative_path:
        raise ValueError("repository_id, node_type and relative_path are required")
    normalized = Path(relative_path).as_posix()
    payload = f"ssg-node-v1\0{repository_id}\0{node_type}\0{normalized}".encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()[:24]
    return f"ssg:{node_type}:{digest}"


def _hash_file(path: Path, chunk_size: int) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while True:
            chunk = stream.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def _source_uri(repository_id: str, relative_path: str, is_directory: bool = False) -> str:
    suffix = "" if relative_path == "." else quote(relative_path, safe="/")
    uri = f"repo://{quote(repository_id, safe='')}/" + suffix
    if is_directory and not uri.endswith("/"):
        uri += "/"
    return uri


def ingest_directory(
    root: str | Path,
    revision: str = "working-tree",
    *,
    max_nodes: int = 100_000,
    max_total_bytes: int = 20 * 1024**3,
    chunk_size: int = 1024 * 1024,
    excluded_dirs: frozenset[str] = DEFAULT_EXCLUDED_DIRS,
) -> KnowledgeGraph:
    """Create a graph snapshot from a directory, hashing files incrementally.

    The directory and file order is deterministic. Hidden files are included
    unless they are in excluded_dirs. Symlinks are skipped to prevent traversal
    outside the chosen root. Resource limits are hard failures, never truncation.
    """
    supplied = Path(root).expanduser()
    if supplied.is_symlink():
        raise IngestionError("source root must not be a symlink")
    base = supplied.resolve()
    if not base.exists() or not base.is_dir():
        raise IngestionError(f"source root is not a directory: {root}")
    if max_nodes < 1 or max_total_bytes < 0 or chunk_size < 1:
        raise ValueError("invalid ingestion resource limits")

    repository_id = base.name or "root"
    graph = KnowledgeGraph()
    root_id = stable_node_id(repository_id, "repository", ".")
    graph.add_node(Node(root_id, "repository", repository_id,
                        _source_uri(repository_id, ".", True), revision,
                        metadata={"relative_path": "."}))
    total_bytes = 0
    node_count = 1
    directory_ids = {".": root_id}

    for current_text, dirs, filenames in os.walk(base, topdown=True, followlinks=False):
        current = Path(current_text)
        relative_dir = current.relative_to(base).as_posix()
        dirs[:] = [name for name in dirs if name not in excluded_dirs and not (current / name).is_symlink()]

        for dirname in sorted(dirs):
            child = current / dirname
            child_rel = (Path(relative_dir) / dirname).as_posix()
            child_id = stable_node_id(repository_id, "directory", child_rel)
            node_count += 1
            if node_count > max_nodes:
                raise IngestionError(f"node limit exceeded ({max_nodes})")
            graph.add_node(Node(child_id, "directory", dirname,
                                _source_uri(repository_id, child_rel, True), revision,
                                metadata={"relative_path": child_rel}))
            directory_ids[child_rel] = child_id
            parent_id = directory_ids[relative_dir]
            edge_id = stable_node_id(repository_id, "edge", f"{relative_dir}->{child_rel}")
            graph.add_edge(Edge(edge_id, parent_id, child_id, "contains"))

        for filename in sorted(filenames):
            file_path = current / filename
            if file_path.is_symlink() or not file_path.is_file():
                continue
            file_rel = (Path(relative_dir) / filename).as_posix()
            try:
                stat_before = file_path.stat()
                total_bytes += stat_before.st_size
                if total_bytes > max_total_bytes:
                    raise IngestionError(f"total byte limit exceeded ({max_total_bytes})")
                content_hash = _hash_file(file_path, chunk_size)
                stat_after = file_path.stat()
                if (stat_before.st_size, stat_before.st_mtime_ns, stat_before.st_ctime_ns) != (
                    stat_after.st_size, stat_after.st_mtime_ns, stat_after.st_ctime_ns
                ):
                    raise IngestionError(f"file changed while hashing: {file_rel}")
            except IngestionError:
                raise
            except OSError as exc:
                raise IngestionError(f"cannot read {file_rel}: {exc}") from exc
            file_id = stable_node_id(repository_id, "file", file_rel)
            node_count += 1
            if node_count > max_nodes:
                raise IngestionError(f"node limit exceeded ({max_nodes})")
            graph.add_node(Node(file_id, "file", filename,
                                _source_uri(repository_id, file_rel), revision,
                                content_hash,
                                metadata={"relative_path": file_rel,
                                          "size_bytes": stat_after.st_size,
                                          "extension": file_path.suffix.lower()}))
            parent_id = directory_ids[relative_dir]
            edge_id = stable_node_id(repository_id, "edge", f"{relative_dir}->{file_rel}")
            graph.add_edge(Edge(edge_id, parent_id, file_id, "contains"))

    errors = graph.validate()
    if errors:
        raise IngestionError("ingested graph failed validation: " + "; ".join(errors))
    return graph
