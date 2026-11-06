import unittest
from ssg.mathcore import Vec2, d8_matrices, apply_matrix
from ssg.provenance import (
    JournalEvent, merkle_root, merkle_proof,
    verify_merkle_proof, verify_chain,
)

class D8AcceptanceTests(unittest.TestCase):
    def test_octagon_dihedral_group_has_16_unique_elements(self):
        self.assertEqual(len(d8_matrices()), 16)
        self.assertEqual(len(set(d8_matrices())), 16)

    def test_d8_preserves_euclidean_norm(self):
        point = Vec2(2.5, -1.25)
        for matrix in d8_matrices():
            self.assertAlmostEqual(apply_matrix(matrix, point).norm(), point.norm(), places=10)

    def test_d8_is_closed_under_composition_with_float_tolerance(self):
        group = d8_matrices()
        for left in group:
            for right in group:
                product = tuple(
                    tuple(round(sum(left[i][k] * right[k][j] for k in range(2)), 12) for j in range(2))
                    for i in range(2)
                )
                self.assertTrue(any(
                    all(abs(product[i][j] - candidate[i][j]) < 1e-9
                        for i in range(2) for j in range(2))
                    for candidate in group
                ))

class MerkleAcceptanceTests(unittest.TestCase):
    def test_all_leaves_have_valid_inclusion_proofs_for_odd_tree(self):
        leaves = [b"one", b"two", b"three", b"four", b"five"]
        root = merkle_root(leaves)
        for index, leaf in enumerate(leaves):
            self.assertTrue(verify_merkle_proof(leaf, merkle_proof(leaves, index), root))

    def test_modified_leaf_is_rejected(self):
        leaves = [b"alpha", b"beta", b"gamma"]
        proof = merkle_proof(leaves, 1)
        self.assertFalse(verify_merkle_proof(b"tampered", proof, merkle_root(leaves)))

    def test_empty_tree_has_defined_root_but_no_inclusion_proof(self):
        self.assertEqual(merkle_root([]), merkle_root([]))
        with self.assertRaises(ValueError):
            merkle_proof([], 0)

    def test_invalid_proof_direction_is_rejected(self):
        self.assertFalse(verify_merkle_proof(b"x", [("up", "00" * 32)], merkle_root([b"x"])))

class CheckpointAcceptanceTests(unittest.TestCase):
    def test_trusted_head_detects_last_event_rewrite(self):
        original = JournalEvent(0, "ingest", "doc", "sha256:original")
        trusted_head = original.digest()
        rewritten = JournalEvent(0, "ingest", "doc", "sha256:modified")
        self.assertFalse(verify_chain([rewritten], expected_head=trusted_head))
        self.assertTrue(verify_chain([original], expected_head=trusted_head))

if __name__ == "__main__":
    unittest.main()


class Vector3AcceptanceTests(unittest.TestCase):
    def test_vec3_dot_cross_and_norm(self):
        from ssg.mathcore import Vec3
        a, b = Vec3(1, 0, 0), Vec3(0, 1, 0)
        self.assertEqual(a.dot(b), 0)
        self.assertEqual(a.cross(b), Vec3(0, 0, 1))
        self.assertAlmostEqual(Vec3(2, 3, 6).norm(), 7)

    def test_zero_vector_cannot_be_normalized(self):
        from ssg.mathcore import Vec3
        with self.assertRaises(ValueError):
            Vec3(0, 0, 0).normalized()


class DirectedGraphMetricsTests(unittest.TestCase):
    def test_directed_degree_and_density(self):
        from ssg.graph import graph_density, in_degree, out_degree
        from ssg.graph import KnowledgeGraph, Node, Edge
        graph = KnowledgeGraph()
        for node_id in ("a", "b", "c"):
            graph.add_node(Node(node_id, "test", node_id))
        graph.add_edge(Edge("ab", "a", "b", "depends"))
        graph.add_edge(Edge("ac", "a", "c", "links"))
        self.assertEqual(out_degree(graph, "a"), 2)
        self.assertEqual(in_degree(graph, "a"), 0)
        self.assertAlmostEqual(graph_density(graph), 2 / 6)
