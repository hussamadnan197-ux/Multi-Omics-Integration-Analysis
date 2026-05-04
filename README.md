# 🧬 Integrated Multi-Omics Analysis for AML Biomarker Discovery

## 📋 Project Overview
This research platform implements a multi-dimensional computational framework to integrate **Clinical, Transcriptomic (RNA-Seq), and Genomic** datasets from the **TCGA-LAML** cohort. The objective is to identify molecular signatures and metabolic vulnerabilities in Acute Myeloid Leukemia through automated bioinformatics pipelines.

---

## 🛠️ Phase 1: Framework Development & Pilot Testing
Before large-scale integration, a pilot study was conducted to validate the visualization pipeline and ensure the reliability of the diagnostic tools.
* **Initial Visualization:** Successfully validated the distribution plotting functions using a sample subset.
* **Predictive Success:** The pilot accurately predicted bimodal age distribution patterns, which were later confirmed in the full-scale clinical analysis.

![Pilot Distribution](age_distribution.png)
*Fig 1: Initial framework testing and pilot age distribution analysis.*

---

## 📊 Phase 2: Preliminary Data Profiling (Quality Control)
Ensuring data integrity through Exploratory Data Analysis (EDA) on simulated environments to avoid biased interpretations.
* **Gender Parity:** Analysis confirmed a balanced representation of male and female subjects (approx. 110:85 ratio), ensuring gender-neutral findings.
* **Population Spread:** Mapped initial age spreads to establish a comparative baseline for real-world clinical data.

![Preliminary Analysis](preliminary_analysis.png)
*Fig 2: Data profiling and Gender/Age distribution for cohort quality control.*

---

## 📈 Phase 3: Real-world Clinical Validation (TCGA-LAML)
Transitioned the pipeline to analyze 100 validated clinical cases retrieved via the **National Cancer Institute (GDC API)**.
* **Demographic Benchmark:** The mean age at diagnosis was identified as **56.52 years**.
* **Clinical Observation:** Data revealed a significant prevalence spike in patients **above age 60**, aligning with high-risk geriatric AML clinical patterns.

![Real-world Age Distribution](real_age_distribution.png)
*Fig 3: Validated age-at-diagnosis trends in the real-world TCGA-LAML cohort.*

---

## 🧬 Phase 4: Transcriptomic Landscape (RNA-Seq Analysis)
Deep-dive into gene expression signatures to identify the metabolic hallmark of leukemic blast cells.
* **Primary Biomarker:** Identified **`MT-RNR2`** (Mitochondrial Ribosomal RNA 2) as the most significantly overexpressed transcript.
* **Metabolic Signature:** The dominance of mitochondrial transcripts indicates a **Hyper-metabolic State**, reflecting intense bioenergetic demands for rapid malignant cell proliferation.

![Top Expressed Genes](top_expressed_genes.png)
*Fig 4: Normalized RNA-Seq read counts highlighting the top 10 expressed genes.*

---

## 🎯 Phase 5: Genomic Architecture & Mutational Burden
Investigating structural genomic drivers by correlating gene physical length (bp) with somatic mutation frequency.
* **Structural Bias Analysis:** Distinguished between stochastic mutations in large genes (e.g., **`TTN`** at 109,224 bp) and high-density clinical drivers.
* **Driver Discovery:** Identified **`TP53`** as a high-density driver; despite its compact size (**2,512 bp**), its disproportionate mutation rate underscores its critical role in AML pathogenesis.

![Mutational Burden](mutation_length_analysis.png)
*Fig 5: Correlation analysis between transcript length and mutational density.*

---

## 🚀 Technical Implementation
* **Languages:** Python 3.12
* **Library Stack:** `Pandas`, `Biopython`, `Seaborn`, `Matplotlib`, `Requests`.
* **Data Source:** Automated retrieval via GDC REST API with custom dynamic error-handling for API schema variations.

---
