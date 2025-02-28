# HGTector2 Snakemake Workflow

This Snakemake workflow automates **HGTector2** processing, from homology search to analysis, using configurations defined in a YAML file.

## Workflow Overview

### Configuration
- Uses **`config_HGTector2.yaml`** by default if located in the **same directory**.
- If placed elsewhere, specify the path with:
  ```bash
  --configfile path/to/config_HGTector2.yaml
  ```

### Key Directories
- **`input_dir`**: Directory with **FAA proteome files**.
- **`search_dir`**: Directory for **HGTector search results**.
- **`analyze_dir`**: Directory for **HGTector analysis results**.

## Workflow Rules

### 1. `all`
Ensures all final results are generated.

### 2. `hgtector_search`
- Runs **HGTector search** on FAA files.
- Uses **DIAMOND database** for homology search.
- Stores search results in `search_dir`.

### 3. `hgtector_analyze`
- Runs **HGTector analysis** on search results.
- Applies **taxonomy filtering** and **parameter adjustments**.
- Saves final results in `analyze_dir`.

## Usage
The `--use-conda` flag is necessary if Snakemake is not installed in the same virtual environment as HGTector.

Run Snakemake with:
Run Snakemake with:
```bash
snakemake -s HGTector2_workflow.smk --use-conda --configfile path/to/config_HGTector2.yaml
```


