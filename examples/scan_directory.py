"""Build a bounded, read-only SSG graph snapshot and SVG overview from a local folder."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from ssg.graph import snapshot_hash
from ssg.ingest import ingest_directory
from ssg.visual import render_svg

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root",type=Path,help="Source directory to inspect (read-only)")
    parser.add_argument("--revision",default="working-tree")
    parser.add_argument("--output",type=Path,default=Path("ssg-output"))
    parser.add_argument("--max-nodes",type=int,default=100_000)
    parser.add_argument("--max-total-bytes",type=int,default=20*1024**3)
    args=parser.parse_args()
    graph=ingest_directory(args.root,revision=args.revision,max_nodes=args.max_nodes,max_total_bytes=args.max_total_bytes)
    args.output.mkdir(parents=True,exist_ok=True)
    svg_path=args.output/"visual-shadow.svg"
    manifest_path=args.output/"snapshot-manifest.json"
    svg_path.write_text(render_svg(graph,title=f"SSG — {args.root.name}"),encoding="utf-8")
    manifest={
        "schema_version":"0.1.0","project":"SSG",
        "source_root_label":args.root.name,"revision":args.revision,
        "graph_snapshot_sha256":snapshot_hash(graph),
        "node_count":len(graph.nodes),"edge_count":len(graph.edges),
        "file_count":sum(node.type=="file" for node in graph.nodes.values()),
        "directory_count":sum(node.type=="directory" for node in graph.nodes.values()),
        "lossiness":"metadata-graph-and-svg-view; source-bytes-retained-at-origin"
    }
    manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(manifest,indent=2,ensure_ascii=False))
    print(f"SVG: {svg_path}\nManifest: {manifest_path}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
