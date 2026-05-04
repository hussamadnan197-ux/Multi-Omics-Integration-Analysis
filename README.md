Integrated Multi-Omics Analysis for AML Biomarker Discovery
📋 Executive Summary
This research-oriented project focuses on the computational integration of heterogeneous biological datasets (Clinical, Transcriptomic, and Genomic) to identify molecular drivers in Acute Myeloid Leukemia (TCGA-LAML). By bridging the gap between raw data acquisition and clinical interpretation, this pipeline uncovers significant patterns in gene expression and mutational landscapes.

🛠️ Tech Stack & Methodology
Data Acquisition: Automated retrieval from the NIH National Cancer Institute (GDC Data Portal) using Python-based REST APIs.

Core Libraries: Pandas for robust data wrangling, Seaborn/Matplotlib for high-dimensional visualization, and Biopython for genomic sequence handling.

Pipeline Strategy: Developed a dynamic error-handling framework to manage shifting API schemas, ensuring reproducible data cleaning and normalization.

📊 Phase 1: Clinical Cohort Profiling
Exploratory Data Analysis (EDA) was performed on a cohort of 100 AML cases to establish a baseline for subsequent molecular analysis.

Demographic Findings: The mean age at diagnosis was identified as 56.52 years.

Biological Trend: A distinct shift in disease prevalence was observed in patients above the age of 60, aligning with established hematological literature.

🧬 Phase 2: Transcriptomic Signature (RNA-Seq)
Analysis of high-throughput transcriptomic data was conducted to identify overexpressed RNA species in leukemic blasts.

Dominant Transcript: MT-RNR2 (Mitochondrial Ribosomal RNA 2).

Metabolic Inference: The high abundance of mitochondrial gene transcripts suggests a hyper-metabolic state, characteristic of rapid leukemic cell proliferation and intense energy demands.

🎯 Phase 3: Genomic Architecture & Mutational Burden
This phase investigated the correlation between gene physical structure (Transcript Length) and mutation frequency.

Structural Bias: Large-scale genes like TTN (109,224 bp) exhibited high raw mutation counts, largely attributed to their genomic footprint.

Critical Driver Discovery: Notably, TP53 was identified as a top mutated gene despite having a small transcript length of only 2,512 bp. This high "mutation density" relative to length underscores its role as a Primary Genomic Driver in AML pathogenesis.

🚀 Installation & Reproducibility
Requirements: pip install -r requirements.txt

Run Analysis: Execute data_acquisition.py to fetch fresh data and regenerate all plots.
