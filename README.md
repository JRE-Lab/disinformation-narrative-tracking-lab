# Disinformation & Narrative Tracking Lab

This repository contains materials for a disinformation and narrative tracking lab. The lab teaches you how to collect posts, articles, and fact-checks across multiple platforms, map the spread of a specific narrative, and assess its intent and potential impact.

## Overview

You will:

- Define a disinformation narrative to track across languages and platforms.
- Use OSINT tools and scrapers to collect posts, articles, and fact checks.
- Build a propagation graph of the narrative using network analysis libraries.
- Evaluate likely intent, deception indicators, and alternative explanations.
- Document key judgments, confidence levels, and collection gaps.

All data used in this lab comes from publicly available sources and is used for research and educational purposes only.

diff --git a/README.md b/README.md
index d0ec018713e811d011477199b14f1d29086ca431..a2c2e464dab9be3dc65b788a5e4e75a51d73673d 100644
--- a/README.md
+++ b/README.md
@@ -1,15 +1,55 @@
 # Disinformation & Narrative Tracking Lab
 
 This repository contains materials for a disinformation and narrative tracking lab. The lab teaches you how to collect posts, articles, and fact-checks across multiple platforms, map the spread of a specific narrative, and assess its intent and potential impact.
 
 ## Overview
 
 You will:
 
 - Define a disinformation narrative to track across languages and platforms.
 - Use OSINT tools and scrapers to collect posts, articles, and fact checks.
 - Build a propagation graph of the narrative using network analysis libraries.
 - Evaluate likely intent, deception indicators, and alternative explanations.
 - Document key judgments, confidence levels, and collection gaps.
 
 All data used in this lab comes from publicly available sources and is used for research and educational purposes only.
+
+## Quick start
+
+1. Create a virtual environment and install dependencies.
+
+```bash
+python -m venv .venv
+source .venv/bin/activate
+pip install -r requirements.txt
+```
+
+2. Run the narrative tracker on the sample dataset.
+
+```bash
+python scripts/track_narrative.py \
+  --posts data/posts.csv \
+  --fact-checks data/fact_checks.csv \
+  --output output \
+  --narrative-tag aid_diversion
+```
+
+3. Review the outputs:
+
+- `output/propagation.graphml`
+- `output/summary.md`
+
+## Lab walkthrough
+
+See [LAB_GUIDE.md](LAB_GUIDE.md) for the step-by-step lab.
+
+## Templates
+
+Use `templates/narrative_worksheet.md` to document hypotheses, evidence, and assessments.
+
+## Repository contents
+
+- `LAB_GUIDE.md` for the full lab walkthrough.
+- `data/` for sample posts and fact-check datasets.
+- `scripts/track_narrative.py` for generating propagation graphs and summary reports.
+- `templates/narrative_worksheet.md` for structured analysis notes.
