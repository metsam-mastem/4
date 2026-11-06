"""Read-only, bounded Git metadata ingestion into the SSG knowledge graph.

This adapter records commit ancestry and branch/tag references. It does not
checkout revisions, execute hooks, inspect file contents, or mutate the source
repository. The filesystem working-tree adapter remains a separate operation.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path
from urllib.parse import quote

from .graph import Edge, KnowledgeGraph, Node
from .ingest import stable_node_id


class GitIngestionError(RuntimeError):
    """Raised when Git history cannot be read safely or completely."""


def _git(root: Path, *args: str, timeout_seconds: float) -> str:
    env = os.environ.copy()
    env.update({
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_OPTIONAL_LOCKS": "0",
        "GIT_ATTR_NOSYSTEM": "1",
        "GIT_PAGER": "cat",
    })
    try:
        result = subprocess.run(
            ["git", "--no-pager", "-c", "core.quotepath=false", "-C", str(root), *args],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout_seconds,
            env=env,
        )
    except subprocess.TimeoutExpired as exc:
        raise GitIngestionError(f"git command timed out after {timeout_seconds}s") from exc
    except OSError as exc:
        raise GitIngestionError(f"cannot execute Git: {exc}") from exc
    if result.returncode != 0:
        detail = result.stderr.strip() or f"exit status {result.returncode}"
        raise GitIngestionError(f"git {' '.join(args[:2])} failed: {detail}")
    return result.stdout


def ingest_git_history(
    root: str | Path,
    *,
    repository_id: str | None = None,
    max_commits: int = 10_000,
    timeout_seconds: float = 15.0,
) -> KnowledgeGraph:
    """Build a graph of commits, parent edges, local branches and tags.

    A hard limit is enforced by requesting one record beyond max_commits and
    failing closed if the limit is exceeded. Shallow/unavailable parents are
    represented as explicit boundary nodes instead of being silently dropped.
    """
    supplied = Path(root).expanduser()
    if supplied.is_symlink():
        raise GitIngestionError("repository root must not be a symlink")
    base = supplied.resolve()
    if not base.exists() or not base.is_dir():
        raise GitIngestionError(f"repository path is not a directory: {root}")
    if max_commits < 1 or timeout_seconds <= 0:
        raise ValueError("max_commits and timeout_seconds must be positive")

    top = _git(base, "rev-parse", "--show-toplevel", timeout_seconds=timeout_seconds).strip()
    if not top or Path(top).resolve() != base:
        raise GitIngestionError("root must be the Git working-tree root")
    repo_id = repository_id or base.name or "repository"
    if not repo_id.strip():
        raise ValueError("repository_id must not be blank")

    log_text = _git(
        base, "log", "--all", "--topo-order",
        f"--max-count={max_commits + 1}",
        "--format=%H%x1f%P%x1f%an%x1f%aI%x1f%s%x1e",
        timeout_seconds=timeout_seconds,
    )
    records = []
    for raw in log_text.split("\x1e"):
        record = raw.strip("\r\n")
        if not record:
            continue
        fields = record.split("\x1f", 4)
        if len(fields) != 5 or not fields[0]:
            raise GitIngestionError("Git returned an invalid commit record")
        commit_hash, parents, author, authored_at, subject = fields
        records.append((commit_hash, parents.split() if parents else [], author, authored_at, subject))
    if len(records) > max_commits:
        raise GitIngestionError(f"commit limit exceeded ({max_commits}); no partial graph returned")

    refs_text = _git(
        base, "for-each-ref",
        "--format=%(refname)%00%(objectname)%00%(objecttype)%00%(*objectname)%00%(*objecttype)",
        "refs/heads", "refs/tags",
        timeout_seconds=timeout_seconds,
    )

    graph = KnowledgeGraph()
    repo_uri = quote(repo_id, safe="/")
    root_id = stable_node_id(repo_id, "git_repository", ".")
    graph.add_node(Node(
        root_id, "git_repository", repo_id,
        source_uri=f"git+repo://{repo_uri}",
        source_version="git-history",
        metadata={"repository_id": repo_id},
    ))

    commit_ids: dict[str, str] = {}
    for commit_hash, parents, author, authored_at, subject in records:
        node_id = stable_node_id(repo_id, "git_commit", commit_hash)
        commit_ids[commit_hash] = node_id
        graph.add_node(Node(
            node_id, "git_commit", subject or commit_hash[:12],
            source_uri=f"git+{repo_id}/commit/{commit_hash}",
            source_version=commit_hash,
            content_hash=commit_hash,
            metadata={
                "author": author,
                "authored_at": authored_at,
                "subject": subject,
                "parent_hashes": parents,
            },
        ))

    for commit_hash, parents, _author, _authored_at, _subject in records:
        child_id = commit_ids[commit_hash]
        for parent_hash in parents:
            parent_id = commit_ids.get(parent_hash)
            if parent_id is None:
                parent_id = stable_node_id(repo_id, "git_boundary", parent_hash)
                if parent_id not in graph.nodes:
                    graph.add_node(Node(
                        parent_id, "git_boundary", parent_hash[:12],
                        source_uri=f"git+{repo_id}/commit/{parent_hash}",
                        source_version=parent_hash,
                        content_hash=parent_hash,
                        metadata={"boundary": "shallow_or_unavailable_parent"},
                    ))
            edge_id = stable_node_id(repo_id, "git_parent_edge", f"{commit_hash}:{parent_hash}")
            graph.add_edge(Edge(edge_id, child_id, parent_id, "parent"))

    for line in refs_text.splitlines():
        if not line:
            continue
        fields = line.split("\x00")
        if len(fields) != 5:
            raise GitIngestionError("Git returned an invalid ref record")
        refname, object_hash, object_type, peeled_hash, peeled_type = fields
        if refname.startswith("refs/heads/"):
            ref_type, label = "git_branch", refname[len("refs/heads/"):]
        elif refname.startswith("refs/tags/"):
            ref_type, label = "git_tag", refname[len("refs/tags/"):]
        else:
            continue
        ref_id = stable_node_id(repo_id, ref_type, refname)
        target_hash = object_hash if object_type == "commit" else (
            peeled_hash if peeled_type == "commit" else ""
        )
        graph.add_node(Node(
            ref_id, ref_type, label,
            source_uri=f"git+{repo_id}/{refname}",
            source_version=target_hash or object_hash,
            content_hash=object_hash,
            metadata={
                "refname": refname,
                "object_type": object_type,
                "peeled_object_type": peeled_type,
            },
        ))
        contains_id = stable_node_id(repo_id, "git_ref_edge", f"{root_id}:{ref_id}")
        graph.add_edge(Edge(contains_id, root_id, ref_id, "contains"))
        if target_hash:
            target_id = commit_ids.get(target_hash)
            if target_id is None:
                target_id = stable_node_id(repo_id, "git_boundary", target_hash)
                if target_id not in graph.nodes:
                    graph.add_node(Node(
                        target_id, "git_boundary", target_hash[:12],
                        source_uri=f"git+{repo_id}/commit/{target_hash}",
                        source_version=target_hash,
                        content_hash=target_hash,
                        metadata={"boundary": "ref_target_not_in_history"},
                    ))
            points_id = stable_node_id(repo_id, "git_ref_target_edge", f"{ref_id}:{target_hash}")
            graph.add_edge(Edge(points_id, ref_id, target_id, "points_to"))

    errors = graph.validate()
    if errors:
        raise GitIngestionError("Git history graph failed validation: " + "; ".join(errors))
    return graph
