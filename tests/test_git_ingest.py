import subprocess
import tempfile
import unittest
from pathlib import Path

from ssg.git_ingest import GitIngestionError, ingest_git_history


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True, capture_output=True, text=True,
    )
    return result.stdout.strip()


class GitHistoryIngestionTests(unittest.TestCase):
    def make_repo(self, root: Path) -> None:
        root.mkdir()
        git(root, "init", "-b", "main")
        git(root, "config", "user.name", "SSG Test")
        git(root, "config", "user.email", "ssg@example.invalid")
        (root / "one.txt").write_text("first")
        git(root, "add", "one.txt")
        git(root, "commit", "-m", "first commit")
        git(root, "tag", "-a", "v1", "-m", "version one")
        git(root, "checkout", "-b", "feature")
        (root / "two.txt").write_text("second")
        git(root, "add", "two.txt")
        git(root, "commit", "-m", "second commit")

    def test_ingests_commits_branches_tags_and_parent_edges(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            self.make_repo(root)
            graph = ingest_git_history(root, repository_id="owner/repo")
            self.assertEqual(graph.validate(), [])
            commits = [node for node in graph.nodes.values() if node.type == "git_commit"]
            branches = [node for node in graph.nodes.values() if node.type == "git_branch"]
            tags = [node for node in graph.nodes.values() if node.type == "git_tag"]
            self.assertEqual(len(commits), 2)
            self.assertEqual({node.label for node in branches}, {"main", "feature"})
            self.assertEqual({node.label for node in tags}, {"v1"})
            self.assertEqual(sum(edge.relation == "parent" for edge in graph.edges), 1)
            self.assertEqual(sum(edge.relation == "points_to" for edge in graph.edges), 3)

    def test_commit_limit_fails_closed_instead_of_returning_partial_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            self.make_repo(root)
            with self.assertRaises(GitIngestionError):
                ingest_git_history(root, max_commits=1)

    def test_non_repository_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(GitIngestionError):
                ingest_git_history(Path(tmp))

    def test_empty_repository_returns_valid_repository_node(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "empty"
            root.mkdir()
            git(root, "init", "-b", "main")
            graph = ingest_git_history(root)
            self.assertEqual(graph.validate(), [])
            self.assertEqual(len(graph.nodes), 1)


if __name__ == "__main__":
    unittest.main()
