# 🧬 Integrated Multi-Omics Analysis for AML Biomarker Discovery

## 📋 Abstract
This repository hosts a sophisticated computational framework designed to integrate **Clinical, Transcriptomic (RNA-Seq), and Genomic** datasets, specifically targeting **Acute Myeloid Leukemia (TCGA-LAML)**. By deploying custom bioinformatics pipelines, this project elucidates the synergistic relationship between phenotypic clinical manifestations and high-resolution molecular signatures.

---

## 🛠️ Phase 1: Pipeline Orchestration & Framework Validation
Before full-scale integration, I developed a robust visualization and processing framework to ensure the fidelity of downstream analyses.
* **Pilot Diagnostics:** Validated the distribution-plotting algorithms using a controlled data subset to ensure statistical accuracy.
* **Predictive Accuracy:** The framework successfully identified bimodal distribution patterns in patient demographics, establishing a solid baseline for multi-omics integration.

![Pilot Framework Testing](age_distribution.png)
*Fig 1: Initial framework validation and cohort distribution modeling.*

---

## 📊 Phase 2: High-Dimensional Data Profiling (QC)
Ensuring data integrity is paramount in genomic research. This phase focused on Exploratory Data Analysis (EDA) and quality control of the LAML cohort.
* **Bias Mitigation:** Confirmed gender parity across the cohort (approx. 110:85 ratio) to eliminate sex-linked confounding variables in transcriptomic signatures.
* **Population Mapping:** Established fundamental demographic spreads, providing the necessary context for subsequent molecular correlations.

![Cohort Quality Control](preliminary_analysis.png)
*Fig 2: Quality control metrics and demographic stratification of the cohort.*

---

## 📈 Phase 3: Real-world Clinical Validation (NCI-GDC)
Transitioned from simulation to real-world clinical data, retrieving 100 validated cases via the **National Cancer Institute (GDC API)**.
* **Demographic Benchmarking:** Identified the mean age at diagnosis as **56.52 years**, providing a critical clinical touchpoint.
* **Geriatric AML Analysis:** Observations revealed a significant prevalence surge in patients **above age 60**, correlating with high-risk clinical archetypes and geriatric-specific leukemic patterns.

![Clinical Cohort Analysis](real_age_distribution.png)
*Fig 3: Validated age-at-diagnosis trends in the TCGA-LAML clinical cohort.*

---

## 🧬 Phase 4: Transcriptomic Signature & Bioenergetic Profiling
A deep-dive into the RNA-Seq landscape was conducted to identify overexpressed transcripts and metabolic hallmarks of malignant blasts.
* **Metabolic Biomarker:** Identified **`MT-RNR2`** (Mitochondrial Ribosomal RNA 2) as a primary overexpressed signature.
* **Bioenergetic Inference:** The high abundance of mitochondrial transcripts suggests a **Hyper-metabolic State**, indicating the intense oxidative phosphorylation required for rapid cellular proliferation in AML.

![Transcriptomic Profile](top_expressed_genes.png)
*Fig 4: Normalized RNA-Seq read counts highlighting primary molecular signatures.*

---

## 🎯 Phase 5: Genomic Architecture & Mutational Burden
This phase investigated the correlation between gene structural complexity (bp length) and somatic mutation frequency to isolate primary drivers.
* **Mutation Density vs. Stochasticity:** Successfully distinguished between stochastic mutations in large-scale genes (e.g., **`TTN`** at 109,224 bp) and high-density clinical drivers.
* **Driver Discovery:** Identified **`TP53`** as a pivotal driver; despite its minimal footprint (**2,512 bp**), its extreme mutational density confirms its critical role in leukemogenesis and pathogenesis.

![Genomic Driver Analysis](mutation_length_analysis.png)
*Fig 5: Structural genomic analysis correlating transcript length with mutational frequency.*

---

## 🚀 Technical Implementation & Reproducibility
The architecture is built for scalability and transparency:
* **Stack:** Python 3.12 | `Pandas` | `Biopython` | `Seaborn` | `Requests`.
* **Automation:** Integrated GDC API automation with dynamic error-handling for adaptive data fetching.
* **Execution:** Run `data_acquisition.py` to trigger the automated fetch and full analytical sequence.

---
---

## 📈 Phase 6: Clinical Inferential Analysis & Survival Modeling
In the final phase of this architecture, we integrated the high-dimensional molecular data with clinical survival endpoints to evaluate the prognostic significance of the identified biomarkers.

### 📊 Cohort Demographics & Quality Control
Before survival modeling, the TCGA-LAML clinical cohort was stratified to ensure statistical robustness.
* **Gender Parity:** Analysis of the cohort revealed a balanced distribution (approx. 56:44 male-to-female ratio), mitigating sex-linked confounding variables in transcriptomic interpretation.
* **Age Dynamics:** The diagnostic mean age was identified as **56.52 years**, with a Kernel Density Estimate (KDE) showing a significant prevalence surge in patients above age 60[cite: 1].

<p align="center">
  <img src="gender_dist.png" width="45%" />
  <img src="age_histogram.png" width="45%" />
</p>
<p align="center"><em>Fig 6: Demographic stratification and age-at-diagnosis density modeling[cite: 1].</em></p>

### 🧬 Longitudinal Survival Outcomes (Kaplan-Meier)
Using the `Lifelines` framework, we generated survival probability estimates to benchmark the clinical impact of age and molecular risk[cite: 1].
* **Geriatric Stratification:** A comparative analysis between seniors (>60) and younger patients (<=60) demonstrated a distinct divergence in survival trajectories, confirming age as a critical independent prognostic factor in AML[cite: 1].
* **Molecular Risk Correlation:** By integrating genomic risk profiles, we validated that patients with high-risk molecular signatures exhibit a significantly accelerated decline in survival probability compared to standard-risk cohorts[cite: 1].

<p align="center">
  <img src="overall_survival.png" width="45%" />
  <img src="molecular_risk_impact.png" width="45%" />
</p>
<p align="center"><em>Fig 7: Kaplan-Meier survival curves demonstrating the impact of age and molecular risk on clinical prognosis[cite: 1].</em></p>

---

## 🔬 Scientific Conclusion
This integrated multi-omics pipeline successfully bridges the gap between raw sequencing data and clinical outcomes[cite: 1]. The synergy between overexpressed mitochondrial signatures (e.g., **`MT-RNR2`**) and high mutational density in driver genes (e.g., **`TP53`**) provides a molecular basis for the observed survival disparities[cite: 1]. This framework establishes a scalable foundation for **Precision Oncology** and personalized biomarker discovery in Acute Myeloid Leukemia[cite: 1].
