# For HGTector2 

This YAML configuration file defines the parameters and paths required to run **HGTector2** for detecting horizontal gene transfer (HGT) events.

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
Ensure all paths and parameters are correctly configured before running HGTector2 for. For a detailed description of analysis parameters see HGTector2 repo: https://github.com/qiyunlab/HGTector/blob/master/doc/analyze.md

```bash
hgtector search -i output_faa_2 -o /root/search_dir/test_mainflow --db /root/database/diamond/db/db.dmnd --threads 7
```



