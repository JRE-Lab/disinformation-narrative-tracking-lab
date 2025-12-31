diff --git a/scripts/track_narrative.py b/scripts/track_narrative.py
new file mode 100755
index 0000000000000000000000000000000000000000..4ef4cd528b4e036b883d64baeb0908f6f3b78384
--- /dev/null
+++ b/scripts/track_narrative.py
@@ -0,0 +1,144 @@
+#!/usr/bin/env python3
+"""Disinformation & narrative tracking lab helper.
+
+Creates a propagation graph by connecting platforms based on shared URLs
+and earliest timestamps. Outputs a summary report and graph file.
+"""
+from __future__ import annotations
+
+import argparse
+from dataclasses import dataclass
+from pathlib import Path
+
+import pandas as pd
+import networkx as nx
+
+
+@dataclass
+class NarrativeSummary:
+    narrative_tag: str
+    total_posts: int
+    platforms: list[str]
+    top_engagement: pd.DataFrame
+
+
+def load_posts(path: Path, narrative_tag: str | None) -> pd.DataFrame:
+    posts = pd.read_csv(path, parse_dates=["timestamp"])
+    if narrative_tag:
+        posts = posts[posts["narrative_tag"] == narrative_tag]
+    return posts.sort_values("timestamp")
+
+
+def load_fact_checks(path: Path) -> pd.DataFrame:
+    return pd.read_csv(path, parse_dates=["published_at"])
+
+
+def build_propagation_graph(posts: pd.DataFrame) -> nx.DiGraph:
+    graph = nx.DiGraph()
+    for platform in posts["platform"].unique():
+        graph.add_node(platform, type="platform")
+
+    for url, group in posts.groupby("url"):
+        group_sorted = group.sort_values("timestamp")
+        platforms = group_sorted["platform"].tolist()
+        timestamps = group_sorted["timestamp"].tolist()
+        for i in range(1, len(platforms)):
+            src = platforms[i - 1]
+            dst = platforms[i]
+            graph.add_edge(
+                src,
+                dst,
+                url=url,
+                first_seen=timestamps[i - 1].isoformat(),
+                next_seen=timestamps[i].isoformat(),
+            )
+    return graph
+
+
+def summarize(posts: pd.DataFrame) -> NarrativeSummary:
+    top_engagement = (
+        posts.sort_values("engagement", ascending=False)
+        .head(5)
+        .loc[:, ["platform", "author", "timestamp", "text", "engagement", "url"]]
+    )
+    return NarrativeSummary(
+        narrative_tag=posts["narrative_tag"].iloc[0],
+        total_posts=len(posts),
+        platforms=sorted(posts["platform"].unique().tolist()),
+        top_engagement=top_engagement,
+    )
+
+
+def write_report(
+    output_dir: Path,
+    summary: NarrativeSummary,
+    fact_checks: pd.DataFrame,
+) -> Path:
+    report_path = output_dir / "summary.md"
+    with report_path.open("w", encoding="utf-8") as handle:
+        handle.write(f"# Narrative Summary: {summary.narrative_tag}\n\n")
+        handle.write(f"**Total posts collected:** {summary.total_posts}\n")
+        handle.write(
+            "**Platforms observed:** " + ", ".join(summary.platforms) + "\n\n"
+        )
+        handle.write("## Top Engagement Posts\n\n")
+        handle.write(summary.top_engagement.to_markdown(index=False))
+        handle.write("\n\n## Fact Checks\n\n")
+        if fact_checks.empty:
+            handle.write("No fact checks provided.\n")
+        else:
+            handle.write(fact_checks.to_markdown(index=False))
+        handle.write("\n")
+    return report_path
+
+
+def build_parser() -> argparse.ArgumentParser:
+    parser = argparse.ArgumentParser(description="Track narrative propagation.")
+    parser.add_argument("--posts", type=Path, required=True, help="Posts CSV")
+    parser.add_argument(
+        "--fact-checks", type=Path, required=True, help="Fact checks CSV"
+    )
+    parser.add_argument(
+        "--output",
+        type=Path,
+        default=Path("output"),
+        help="Output directory",
+    )
+    parser.add_argument(
+        "--narrative-tag",
+        type=str,
+        default=None,
+        help="Filter to a narrative tag",
+    )
+    return parser
+
+
+def main() -> None:
+    parser = build_parser()
+    args = parser.parse_args()
+
+    posts = load_posts(args.posts, args.narrative_tag)
+    if posts.empty:
+        raise SystemExit("No posts available for the selected narrative tag.")
+
+    fact_checks = load_fact_checks(args.fact_checks)
+    if args.narrative_tag:
+        fact_checks = fact_checks[fact_checks["claim"].notna()]
+
+    output_dir = args.output
+    output_dir.mkdir(parents=True, exist_ok=True)
+
+    graph = build_propagation_graph(posts)
+    graph_path = output_dir / "propagation.graphml"
+    nx.write_graphml(graph, graph_path)
+
+    summary = summarize(posts)
+    report_path = write_report(output_dir, summary, fact_checks)
+
+    print("Narrative tracking output ready:")
+    print(f"- Graph: {graph_path}")
+    print(f"- Report: {report_path}")
+
+
+if __name__ == "__main__":
+    main()
