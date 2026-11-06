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
