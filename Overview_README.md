# ArchaeaHGT: Snakemake Workflows for Detecting Horizontal Gene Transfer in Archaeal Genomes  

## Abstract  
Archaea, a distinct domain of life, are an increasingly recognized yet understudied component of the human microbiome. A key driver of their adaptation is horizontal gene transfer (HGT), which facilitates genetic exchange and functional diversification. This project introduces a computational framework designed for the detection of horizontal gene transfer (HGT) in archaeal genomes at a large scale. It integrates phylogenetic and sequence composition-based tools into two workflows, respectively utilizing Snakemake. Applying these workflows to a dataset of human-associated archaeal genomes, I identified 23,574 putative HGT events across 686 genomes. This approach provides scalable and adaptable workflows for analyzing horizontal gene transfer (HGT) in archaea, enabling a systematic investigation of such events and their implications for microbial interactions, including potential pathogenicity. 

This project integrates **HGTector2** for taxonomic HGT classification and **IslandViewer4** for genomic island (GI) prediction, providing a structured and reproducible framework for large-scale HGT analysis.  

## Features  
- **Phylogenetic HGT detection** using HGTector2 with a curated reference database.  
- **Genomic island prediction** with IslandViewer4 to refine HGT classification.  
- **Functional annotation retrieval** from UniProtKB, including **GO term assignments** for putative HGT candidates.  
- **Reproducible and scalable** Snakemake pipeline for large-scale archaeal genome analysis.  

## Methodology  
### 1. HGTector2 Workflow  
- Analyzes archaeal genomes to detect putative HGT events based on **taxonomic distribution of BLAST hits**.  
- Uses a structured reference database to classify genes into **self, close, and distal taxonomic groups**.  
- Outputs **putative donor taxa**, **statistical classification of HGT events**, and **functional annotations** from UniProtKB.  

### 2. IslandViewer4 Workflow  
- Predicts **genomic islands (GIs)**, which often contain horizontally acquired genes.  
- Allows cross-referencing of HGTector2 predictions with genomic island locations for **improved classification accuracy**.  

### 3. Data Processing & Outputs  
- The workflow is optimized for analyzing **large-scale metagenomic datasets**.  
- Outputs include **HGT predictions, putative donors, functional annotations, and genomic island reports**, with accompanying visualizations (scatter plots, KDE distributions, and GI maps).  

## System Requirements

To install and run HGTector2, ensure your system meets the following requirements:

- **Operating System**: Linux
- **Storage**: Minimum of 10 GB free disk space + addiotnal space for the reference database
- **Python Version**: Python 3.6 or higher
  
# HGTector2 Requirements

## Software Dependencies

HGTector2 relies on several external software packages. Before installation, ensure the following dependencies are available:

- **Conda**: For package and environment management
- **DIAMOND**: High-performance sequence aligner
- **Snakemake**: Workflow management tool (*Must be installed in the base Conda environment, not in the HGTector2 environment*)
- **Python Packages**:
  - PyYAML
  - pandas
  - matplotlib
  - scikit-learn
  - **Biopython** (for the helper scripts)

## Dependencies Instructions

1. Install Snakemake (In Base Conda Environment)

Snakemake should be installed **in the base Conda environment** to properly manage workflows:
   ```bash
   conda install -n base -c conda-forge snakemake
   ```

2. Set Up Conda Environment:

   ```bash
   conda create -n hgtector -c conda-forge python=3.6 pyyaml pandas matplotlib scikit-learn biopython bioconda::diamond

## Reference Database
In this project, the **pre-built reference database** from the latest **HGTector repository release** was used. To ensure reproducibility, users can download and set up the latest available version by following the instructions in the [HGTector repository](https://github.com/qiyunlab/HGTector/blob/master/doc/database.md#pre-built-databases)

## Overview documentation
- [HGTector2 workflows](Snakemake_Workflows_HGTector2/HGTector2_workflows.md)
- [IslandViewer4 workflow](Snakemake_Workflow_Islandviewer4/IslandViewer4_workflow.md)
- [Config files](Config_files/Config_Files.md)
- [Helper scirpts](Helper_scripts/Helper_Scripts.md)
- [GO-terms](Helper_scripts/GO/GO_annotation.md)
- [Prediction Result](Prediction_Results/Prediction_Results.md)


## Installation   
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/ArchaeaHGT.git  
   cd ArchaeaHGT  

## Citations

>Chibani, C. M., Mahnert, A., Borrel, G., Almeida, A., Werner, A., Brugère, J.-F., Gribaldo, S., Finn, R. D., Schmitz, R. A., & Moissl-Eichinger, C. (2022). A catalogue of 1,167 genomes from the human gut archaeome. Nature Microbiology, 7(1), 48–61. https://doi.org/10.1038/s41564-021-01020-9

> Zhu, Q., Kosoy, M., & Dittmar, K. (2014). HGTector: an automated method facilitating genome-wide discovery of putative horizontal gene transfers. BMC Genomics, 15(1), 717. https://doi.org/10.1186/1471-2164-15-717

> Bertelli, C., Laird, M. R., Williams, K. P., Simon Fraser University Research Computing Group, Lau, B. Y., Hoad, G., Winsor, G. L., & Brinkman, F. S. L. (2017). IslandViewer 4: expanded prediction of genomic islands for larger-scale datasets. Nucleic Acids Research, 45(W1), W30–W35. https://doi.org/10.1093/nar/gkx343

> Consortium, T. U. (2025). UniProt: the Universal Protein Knowledgebase in 2025. Nucleic Acids Research, 53(D1), D609–D617. https://doi.org/10.1093/nar/gkae1010
