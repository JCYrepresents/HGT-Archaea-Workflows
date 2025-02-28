# Prediction Results Overview

Overview of the **HGTector2** and **IslandViewer4** prediction results.

## HGTector2 Results
Both the **final processed results** for HGTector2 and IslandViewer4, as well as the **raw results from the HGTector2 analyze step** (686 Genomes), are available in the corresponding folder.The processed prediction results are available in .tsv/.csv format and as Excel files for easier data handling and visualization. If one wants to rerun the full workflow or access the raw homology search results of HGTector2, use the following Google Drive link:

[Google Drive - HGTector2 homology search](https://drive.google.com/drive/folders/1lK4vnQcEtd2CXB5jZRgTd8OBsiibe5au?usp=sharing) 
This file has approximately 13GB!

HGTector2 generates multiple output files to summarize horizontal gene transfer (HGT) predictions:

- **scores.tsv**: Tab-delimited file containing per-protein details:
  - Sample name, Protein ID, Sequence length
  - Total filtered hits and cumulative bit scores for taxonomic groups (self, close, distal)
  - Best-scoring match in the distal group, indicating a potential donor taxon

- **hgts/<sample>.txt**: Lists all predicted horizontally transferred proteins:
  - Protein ID, Silhouette scores (confidence metric), and putative donor taxon (based on LCA analysis)

- **Graphical Outputs**:
  - **Histograms (`<sample>/<distal/close>.hist.png`)**: Visualize score distributions for taxonomic groups.
  - **KDE Plots (`<sample>/<distal/close>.kde.png`)**: Show probability distributions with statistical cutoffs.
  - **Scatter Plot (`<sample>/scatter.png`)**: Highlights horizontally transferred genes by comparing distal and close scores.

These results offer both numerical and graphical insights into putative HGT events, aiding further validation and classification.

## IslandViewer4 Results
IslandViewer4 generates a downloadable results table that provides genomic island predictions. The table includes:
- **Island coordinates**: Start and end positions of predicted genomic islands.
- **Detection methods**: The tools used to identify genomic islands.
- **Gene details**: Locus, position, strand, and product information.
- **External annotations**: Additional reference data for further analysis.

The combined results of 7 genomes can be found in the corresponding Folder.
For any further analysis or interpretation, refer to the respective documentation of **HGTector2** and **IslandViewer4**.

