import hashlib
import tempfile
import unittest
from pathlib import Path
from ssg.graph import KnowledgeGraph, Node, Edge, snapshot_hash
from ssg.ingest import ingest_directory, IngestionError

class SourceIngestionTests(unittest.TestCase):
    def test_ingests_nested_files_with_hashes_and_contains_edges(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/"demo-repo"
            (root/"src"/"core").mkdir(parents=True)
            payload=b"print('SSG')\n"
            (root/"src"/"core"/"main.py").write_bytes(payload)
            graph=ingest_directory(root,revision="abc123")
            self.assertEqual(graph.validate(),[])
            file_nodes=[n for n in graph.nodes.values() if n.type=="file"]
            self.assertEqual(len(file_nodes),1)
            self.assertEqual(file_nodes[0].content_hash,hashlib.sha256(payload).hexdigest())
            self.assertEqual(file_nodes[0].source_uri,"repo://demo-repo/src/core/main.py")
            self.assertTrue(any(e.relation=="contains" for e in graph.edges))

    def test_node_identity_is_independent_of_checkout_absolute_path(self):
        graphs=[]
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)
            for parent in ("checkout-a","checkout-b"):
                root=base/parent/"demo-repo"
                (root/"src").mkdir(parents=True)
                (root/"src"/"main.py").write_text("same source")
                graphs.append(ingest_directory(root))
        ids=[{n.source_uri:n.id for n in g.nodes.values()} for g in graphs]
        self.assertEqual(ids[0],ids[1])

    def test_skips_git_metadata_and_symlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/"demo"
            (root/".git").mkdir(parents=True)
            (root/".git"/"config").write_text("metadata")
            (root/"real.txt").write_text("ok")
            outside=Path(tmp)/"outside.txt"
            outside.write_text("outside")
            try: (root/"linked.txt").symlink_to(outside)
            except OSError: self.skipTest("symlinks unavailable")
            graph=ingest_directory(root)
            paths=[n.source_uri for n in graph.nodes.values()]
            self.assertFalse(any(".git" in p for p in paths))
            self.assertFalse(any("linked.txt" in p for p in paths))

    def test_node_limit_is_enforced(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/"demo"; root.mkdir()
            (root/"a").write_text("a"); (root/"b").write_text("b")
            with self.assertRaises(IngestionError): ingest_directory(root,max_nodes=2)

    def test_total_byte_limit_is_enforced(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/"demo"; root.mkdir(); (root/"a.bin").write_bytes(b"12345")
            with self.assertRaises(IngestionError): ingest_directory(root,max_total_bytes=4)

class SnapshotHashTests(unittest.TestCase):
    def test_snapshot_hash_is_independent_of_insertion_order(self):
        a=KnowledgeGraph(); b=KnowledgeGraph()
        nodes=[Node("a","file","A",content_hash="h1"),Node("b","file","B",content_hash="h2")]
        a.add_node(nodes[0]); a.add_node(nodes[1]); a.add_edge(Edge("e","a","b","contains"))
        b.add_node(nodes[1]); b.add_node(nodes[0]); b.add_edge(Edge("e","a","b","contains"))
        self.assertEqual(snapshot_hash(a),snapshot_hash(b))

    def test_snapshot_hash_changes_when_content_hash_changes(self):
        a=KnowledgeGraph(); b=KnowledgeGraph()
        a.add_node(Node("a","file","A",content_hash="old"))
        b.add_node(Node("a","file","A",content_hash="new"))
        self.assertNotEqual(snapshot_hash(a),snapshot_hash(b))

if __name__=="__main__": unittest.main()


class RepositoryNamespaceTests(unittest.TestCase):
    def test_same_folder_name_can_have_distinct_repository_namespaces(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "same-name"
            root.mkdir()
            (root / "data.txt").write_text("same")
            graph_a = ingest_directory(root, repository_id="owner-a/same-name")
            graph_b = ingest_directory(root, repository_id="owner-b/same-name")
            file_a = next(node for node in graph_a.nodes.values() if node.type == "file")
            file_b = next(node for node in graph_b.nodes.values() if node.type == "file")
            self.assertNotEqual(file_a.id, file_b.id)
