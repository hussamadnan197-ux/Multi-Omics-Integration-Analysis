# 🧬 Integrated Multi-Omics Analysis for AML Biomarker Discovery

## 📋 Project Overview
This research platform demonstrates a multi-dimensional approach to leukemia research by integrating **Clinical, Transcriptomic (RNA-Seq), and Genomic** datasets from the **TCGA-LAML** cohort. The project utilizes custom Python-based bioinformatics pipelines to identify molecular signatures and elucidate the genomic architecture of primary driver mutations.

## 🛠️ Technical Methodology & Pipeline
The analysis was executed through a robust pipeline designed for high-throughput data processing:
* **Automated Data Acquisition:** Leveraging the **GDC REST API** for real-time retrieval of clinical and molecular profiles.
* **Bioinformatics Integration:** Utilizing `Biopython` for genomic sequence analysis and transcript length calculations.
* **Computational Engineering:** Implementation of advanced error-handling and data wrangling via `Pandas`, `Seaborn`, and `Matplotlib`.

---

## 📊 Phase 1: Preliminary Data Profiling & Quality Control
Initial exploratory data analysis (EDA) was conducted to ensure cohort balance and data integrity.
* **Gender Distribution:** Analysis confirmed a balanced representation of male and female subjects within the simulation environment, ensuring a non-biased dataset.
* **Population Spread:** Initial histogram profiling helped identify the primary age groups before moving to validated clinical cohorts.

![Preliminary Analysis](preliminary_analysis.png)

---

## 📈 Phase 2: Real-world Clinical Validation
The analysis was expanded to 100 validated clinical cases of Acute Myeloid Leukemia to establish demographic baselines.
* **Key Finding:** The cohort exhibited a mean age at diagnosis of **56.52 years**.
* **Clinical Insight:** A statistically significant shift in disease prevalence was observed in patients **above the age of 60**, aligning with established hematological literature regarding geriatric leukemia risk.

![Real-world Age Distribution](real_age_distribution.png)

---

## 🧬 Phase 3: Transcriptomic Landscape (RNA-Seq)
High-throughput transcriptomic read counts were processed to identify the gene expression signatures in leukemic blast samples.
* **Top Marker:** Identification of **`MT-RNR2`** (Mitochondrial Ribosomal RNA 2) as the most abundant transcript.
* **Biological Inference:** The overexpression of mitochondrial genes suggests a **Hyper-metabolic State**, reflecting the intense energy requirements for rapid malignant cell proliferation.

![Top Expressed Genes](top_expressed_genes.png)

---

## 🎯 Phase 4: Genomic Architecture & Driver Identification
This stage investigated the correlation between gene physical structure (bp length) and somatic mutation frequency.
* **Structural Bias Analysis:** While large-scale genes like `TTN` (109,224 bp) naturally exhibit high mutation counts, we focused on identifying high-density drivers.
* **Primary Genomic Driver:** **`TP53`** was identified as a critical mutated gene despite its compact transcript length of only **2,512 bp**. This disproportionate "mutation density" confirms its role as a pivotal driver in AML pathogenesis.

![Mutational Burden](mutation_length_analysis.png)

---

## 📚 Phase 5: Framework Pilot Testing
A pilot study was conducted to validate the visualization framework, predicting disease distribution patterns.
* **Observation:** The pilot successfully predicted bimodal age distributions, which were later confirmed in the full-scale clinical cohort analysis.

![Pilot Distribution](age_distribution.png)

---

## 🚀 Reproducibility & Environment
1. **Requirements:** `pip install pandas biopython seaborn matplotlib requests`.
2. **System Execution:** Run `data_acquisition.py` to trigger the automated API fetch and full analysis sequence.

