# ArchaeaHGT:Snakemake Workflows for Detecting Horizontal Gene Transfer in Archaeal Genomes  

## Overview  
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


## Installation & Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/ArchaeaHGT.git  
   cd ArchaeaHGT  
