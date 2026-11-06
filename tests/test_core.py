import math,unittest
from ssg.mathcore import Vec2,Rect,Cuboid,PROPORTIONS,fibonacci,d4_orbit,fit_ratio
from ssg.graph import Node,Edge,KnowledgeGraph
from ssg.provenance import JournalEvent,verify_chain
from ssg.visual import render_svg

class MathTests(unittest.TestCase):
    def test_vector(self):
        a,b=Vec2(3,4),Vec2(1,2)
        self.assertEqual(a+b,Vec2(4,6)); self.assertEqual(a.norm(),5); self.assertEqual(a.dot(b),11)
    def test_rect(self):
        r=Rect(1,math.sqrt(2))
        self.assertAlmostEqual(r.ratio,math.sqrt(2)); self.assertTrue(fit_ratio(r,PROPORTIONS["sqrt2"],1e-10))
    def test_cuboid(self):
        c=Cuboid(2,3,6)
        self.assertEqual(c.volume,36); self.assertEqual(c.surface_area,72); self.assertAlmostEqual(c.diagonal,7)
    def test_fibonacci(self):
        self.assertEqual([fibonacci(i) for i in range(7)],[0,1,1,2,3,5,8])
    def test_d4(self):
        self.assertEqual(len(set(d4_orbit(Vec2(2,1)))),8)
        self.assertEqual(len(set(d4_orbit(Vec2(1,1)))),4)

class GraphTests(unittest.TestCase):
    def test_graph_and_svg(self):
        g=KnowledgeGraph(); g.add_node(Node("a","file","alpha")); g.add_node(Node("b","concept","beta"))
        g.add_edge(Edge("e","a","b","defines"))
        self.assertEqual(g.validate(),[]); self.assertIn("<svg",render_svg(g))
    def test_bad_edge(self):
        g=KnowledgeGraph(); g.add_edge(Edge("e","x","y","rel"))
        self.assertEqual(len(g.validate()),2)

class ProvenanceTests(unittest.TestCase):
    def test_chain(self):
        a=JournalEvent(0,"ingest","a","hash-a")
        b=JournalEvent(1,"render","b","hash-b",a.digest())
        self.assertTrue(verify_chain([a,b]))
        self.assertFalse(verify_chain([a,JournalEvent(1,"render","b","hash-b")]))

if __name__=="__main__": unittest.main()
