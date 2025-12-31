diff --git a/LAB_GUIDE.md b/LAB_GUIDE.md
new file mode 100644
index 0000000000000000000000000000000000000000..c70549cfbb4a91f8f76953ff594fcf94dae0da20
--- /dev/null
+++ b/LAB_GUIDE.md
@@ -0,0 +1,63 @@
+# Disinformation & Narrative Tracking Lab
+
+This lab walks you through defining, collecting, and analyzing a narrative across platforms. The repository ships with a realistic sample dataset and a helper script so the lab can be run end-to-end without external API keys.
+
+## Learning goals
+
+1. Define a narrative with clear scope and hypotheses.
+2. Collect evidence across platforms and languages.
+3. Map how the narrative spreads.
+4. Evaluate intent, deception indicators, and uncertainty.
+5. Produce a concise assessment with documented sources.
+
+## Materials
+
+- Sample data in `data/posts.csv` and `data/fact_checks.csv`.
+- `templates/narrative_worksheet.md` for structured analysis.
+- `scripts/track_narrative.py` for propagation graphs and summaries.
+
+## Step 1: Define the narrative
+
+1. Open `templates/narrative_worksheet.md` and save a copy in a working folder.
+2. Fill out the **Narrative Definition** section to capture your initial scope.
+3. Decide on the narrative tag you will track (use `aid_diversion` for the sample data).
+
+## Step 2: Explore the evidence
+
+1. Review `data/posts.csv` for platform activity and timestamps.
+2. Review `data/fact_checks.csv` to understand verified rebuttals.
+3. Highlight key claims or inflection points in your worksheet.
+
+## Step 3: Generate the propagation graph
+
+```bash
+python scripts/track_narrative.py \
+  --posts data/posts.csv \
+  --fact-checks data/fact_checks.csv \
+  --output output \
+  --narrative-tag aid_diversion
+```
+
+Outputs:
+- `output/propagation.graphml` (import into Gephi, Cytoscape, or NetworkX)
+- `output/summary.md` (summary report of top posts and fact checks)
+
+## Step 4: Assess intent and impact
+
+Use the worksheet to answer:
+- Who amplified the narrative?
+- Which platforms carried it earliest?
+- What evidence contradicts the narrative?
+- How confident are you in the assessment?
+
+## Step 5: Document your findings
+
+1. Add your final judgments to the worksheet.
+2. Export `output/summary.md` to share key findings.
+3. Record collection gaps or follow-up tasks.
+
+## Extension ideas
+
+- Expand `data/posts.csv` with additional sources.
+- Add `language`-specific analysis (sentiment, topic modeling).
+- Visualize engagement over time with a timeline chart.
