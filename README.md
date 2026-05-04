# Integrated Multi-Omics Analysis for Cancer Biomarker Discovery
This project aims to analyze and integrate different layers of biological data. By combining RNA-seq and DNA Methylation datasets, we aim to build a predictive model that identifies key molecular drivers in [Specify Cancer Type, e.g., Leukemia].
Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, BioPython.

Data Source: TCGA (The Cancer Genome Atlas
🏗️ Under Development: Currently performing data cleaning and exploratory data analysis (EDA).
## Preliminary Data Insights
![Age Distribution](age_distribution.png)
![Analysis Results](preliminary_analysis.png)
## 📊 Real-world Data Insights (TCGA-LAML)
After connecting to the GDC API, I analyzed 100 real clinical cases of Acute Myeloid Leukemia.
- **Average Age:** 56.52 years.
- **Key Observation:** The data shows a significant increase in cases for patients above the age of 60.
![Real Age Distribution](real_age_distribution.png)
## 🧬 Gene Expression Profiling (RNA-Seq)
I processed raw transcriptomic data from a TCGA-LAML patient to identify high-abundance gene transcripts.
- **Top Gene:** `MT-RNR2` (Mitochondrial Ribosomal RNA 2).
- **Insight:** High expression of mitochondrial genes suggests intense metabolic demands within the leukemic cells.
- ## 🧬 Mutation Analysis & Gene Architecture
I analyzed the top mutated genes in the TCGA-LAML cohort, correlating mutation frequency with transcript length.
- **Key Observation:** Large genes like `TTN` show high mutation counts due to their size (109k+ bp).
- **Clinical Insight:** `TP53` mutations were identified despite its small genomic footprint (2,512 bp), highlighting its critical role as a driver mutation in leukemia.

![Mutation Length Analysis](mutation_length_analysis.png)

![Top Expressed Genes](top_expressed_genes.png)
