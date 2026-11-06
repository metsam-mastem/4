"""Minimal graph-first knowledge model."""
from dataclasses import dataclass, field

@dataclass
class Node:
    id: str
    type: str
    label: str
    source_uri: str = ""
    source_version: str = ""
    content_hash: str = ""
    metadata: dict = field(default_factory=dict)

@dataclass
class Edge:
    id: str
    source_id: str
    target_id: str
    relation: str
    evidence_uri: str = ""
    confidence: float = 1.0

@dataclass
class KnowledgeGraph:
    nodes: dict = field(default_factory=dict)
    edges: list = field(default_factory=list)
    def add_node(self,node):
        if node.id in self.nodes: raise ValueError("duplicate node id: "+node.id)
        self.nodes[node.id]=node
    def add_edge(self,edge):
        if not 0<=edge.confidence<=1: raise ValueError("confidence must be in [0,1]")
        self.edges.append(edge)
    def validate(self):
        errors=[]; seen=set()
        for e in self.edges:
            if e.id in seen: errors.append("duplicate edge id: "+e.id)
            seen.add(e.id)
            if e.source_id not in self.nodes: errors.append("missing source: "+e.source_id)
            if e.target_id not in self.nodes: errors.append("missing target: "+e.target_id)
        return errors
    def degree(self,node_id):
        if node_id not in self.nodes: raise KeyError(node_id)
        return sum(e.source_id==node_id or e.target_id==node_id for e in self.edges)


def out_degree(graph, node_id):
    """Count outgoing directed edges, including parallel edges and self-loops."""
    if node_id not in graph.nodes: raise KeyError(node_id)
    return sum(edge.source_id == node_id for edge in graph.edges)


def in_degree(graph, node_id):
    """Count incoming directed edges, including parallel edges and self-loops."""
    if node_id not in graph.nodes: raise KeyError(node_id)
    return sum(edge.target_id == node_id for edge in graph.edges)


def graph_density(graph):
    """Directed simple-graph density; unique ordered pairs, no self-loops.

    Parallel edges count once for density. Self-loops are excluded. For n<2,
    density is defined as zero.
    """
    n=len(graph.nodes)
    if n<2: return 0.0
    pairs={(edge.source_id,edge.target_id) for edge in graph.edges
           if edge.source_id in graph.nodes and edge.target_id in graph.nodes
           and edge.source_id != edge.target_id}
    return len(pairs)/(n*(n-1))
