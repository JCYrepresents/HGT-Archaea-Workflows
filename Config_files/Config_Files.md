# For HGTector2 


# config_HGTector2.yaml for the HGTector2 main snakemake workflow
This YAML configuration file defines the parameters and paths required to run **HGTector2** for detecting horizontal gene transfer (HGT) events. The provided YAML file and its parameters were used to run the analysis for the human gut archaeome dataset. 


## Configuration Overview

### Input & Output Directories
- **`input_dir`**: Directory containing input **proteome FASTA files**.
- **`search_dir`**: Directory for storing **intermediate search results**.
- **`analyze_dir`**: Directory for **final processed results**.

### Database Settings
- **`diamond_db`**: Path to the **DIAMOND-formatted database** for homology searches.
- **`taxdump`**: Path to the **taxonomy database dump** required for taxonomic classification.

### HGTector2 Settings
- **`threads`**: Number of CPU threads to use (**adjust based on available resources**).
- **`conda_env`**: Path to the **Conda environment** for running HGTector2.

### Analysis Parameters
- **`bandwidth`**: Set to **grid** for optimized estimation.
- **`donor_name`**: Whether to display donor taxonomy name or ID (**true** or **false**).
- **`evalue`**: E-value cutoff for homology searches (**default: 1e-50**).
- **`identity`**: Minimum percentage identity for valid hits (**default: 50**).
- **`coverage`**: Minimum query coverage required (**default: 50**).
- **`silhouette`**: Threshold for silhouette score filtering (**default: 0**).
- **`noise`**: Noise reduction parameter (**default: 0**).

## Usage
Ensure all paths and parameters are correctly configured before running the **HGTector2 main Snakemake workflow**.For a detailed description of analysis parameters see HGTector2 repo: https://github.com/qiyunlab/HGTector/blob/master/doc/analyze.md

<br>

# config_HGTector2_analyze.yaml for the HGTector2 analysis rerun snakemake workflow

This YAML file extends the **HGTector2 configuration** by specifying additional paths and optional parameters for **analysis refinement**.

## Additional Configuration

### Updated Directories
- **`analyze_dir`**: Directory for **second-run analysis results**.

### New Optional Parameters
- **`self_tax` & `close_tax`**: Define specific taxonomic groups for classification (optional).

## Usage
Ensure the paths and new parameters are correctly configured before running **HGTector2 rerun analysis Snakemake workflow**.

For a full reference on parameter settings, visit the [HGTector2 documentation](https://github.com/qiyunlab/HGTector/blob/master/doc/analyze.md).

<br>

# config_collect.yaml for the HGTector2 main snakemake workflow
This YAML configuration file defines the paths required for **collecting and merging** final HGTector2 results.

### Configuration Overview

### Directories
- **`analyze_dir`**: Path to the directory containing **analyzed results**.
- **`final_results`**: Directory where the **final merged results** will be stored.

### Usage
Ensure the paths are correctly set before running the **Snakemake collect result script**.

For modifications or optimizations, update the YAML file accordingly and rerun the process.

<br>

# config_details.yaml for the HGTector2 main snakemake workflow

This YAML configuration file specifies the directories and file paths required for **adding details** in the dataset.

### Important Note

- **Ensure that .faa** files contain gene names and product annotations in the fasta header before running **Add_details.smk** to function correctly.

### Configuration Overview

### Directories & Files

- **`input_dir`**: Directory containing `.faa` annotation files.
- **`merged_csv`**: Input CSV file before annotation expansion.
- **`final_csv`**: Output CSV file after annotation expansion.

### Usage

Ensure the paths are correctly set before running the add details Snakemake script:


For modifications or optimizations, update the YAML file accordingly and rerun the process.

<br>
<br>

# For IslandViewer4

## config_details.yaml for the IslandViewer4 snakemake workflow

This YAML configuration file specifies paths required for running the **IslandViewer4 Snakemake workflow** to predict genomic islands.

## Configuration Overview

### Directories
- **`input_folder`**: Path to the directory containing **GenBank (.gbk) files**.
- **`output_folder`**: Directory where **IslandViewer4 results** will be stored.

### Script Path
- **`islandviewer_script`**: Path to the **IslandViewer2.py script** (modify if needed).

## Usage
Ensure the paths are correctly set before running the **IslandViewer4 Snakemake script**.

For modifications, update the YAML file accordingly and rerun the process.









