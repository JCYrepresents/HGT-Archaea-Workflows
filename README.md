# ArchaeaHGT:Snakemake Workflows for Detecting Horizontal Gene Transfer in Archaeal Genomes  

## Overview  
This repository contains a **Snakemake workflow** developed as part of a **Praktikum** under the supervision of **Prof. Dr. Rattei**. The workflow enables **automated detection of horizontal gene transfer (HGT)** in archaeal genomes, particularly from the **human archaeome**, using a combination of **phylogenetic and sequence composition-based approaches**.  

The pipeline integrates **HGTector2** for taxonomic HGT classification and **IslandViewer4** for genomic island (GI) prediction, providing a structured and reproducible framework for large-scale HGT analysis.  

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

## Applications  
This workflow enables:  
- **Comparative genomic studies** of archaeal species.  
- Investigation of **HGT’s role in archaeal adaptation** to the human microbiome.  
- Identification of **potentially transferred functional genes**, including those relevant to **pathogenic potential**.  

## Installation & Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/ArchaeaHGT.git  
   cd ArchaeaHGT  
