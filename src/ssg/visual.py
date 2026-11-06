"""Deterministic SVG overview renderer for a small graph."""
from html import escape

def render_svg(graph,title="SSG Visual Shadow",width=1000,height=600):
    errors=graph.validate()
    if errors: raise ValueError("invalid graph: "+"; ".join(errors))
    nodes=list(graph.nodes.values()); pad=40; box_w=180; box_h=64
    cols=max(1,(width-2*pad)//(box_w+30)); positions={}
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
           '<rect width="100%" height="100%" fill="#101827"/>',
           f'<text x="{pad}" y="34" fill="#f6d28b" font-family="sans-serif" font-size="22">{escape(title)}</text>']
    for i,node in enumerate(nodes):
        x=pad+(i%cols)*(box_w+30); y=80+(i//cols)*110
        positions[node.id]=(x+box_w/2,y+box_h/2)
    for edge in graph.edges:
        x1,y1=positions[edge.source_id]; x2,y2=positions[edge.target_id]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#8ca8d8" stroke-width="2"/>')
    for i,node in enumerate(nodes):
        x=pad+(i%cols)*(box_w+30); y=80+(i//cols)*110
        parts.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="12" fill="#263c59" stroke="#80c8dc"/>')
        parts.append(f'<text x="{x+12}" y="{y+25}" fill="#fff" font-size="14">{escape(node.label[:24])}</text>')
        parts.append(f'<text x="{x+12}" y="{y+46}" fill="#b8c7df" font-size="10">{escape(node.type)} · {escape(node.id[:18])}</text>')
    parts.append("</svg>")
    return "\n".join(parts)
