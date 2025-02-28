# General Inforamtion
The different steps (HGTector2 analysis, collection of results, and adding details) are purposely separated so that users can extract data at any stage without triggering subsequent steps. This modular approach allows flexibility in processing results without requiring the full workflow to run.

<br>

# HGTector2 main Snakemake Workflow

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

## Example Usage
The `--use-conda` flag is necessary if Snakemake is not installed in the same virtual environment as HGTector.

Run Snakemake with:
Run Snakemake with:
```bash
snakemake -s HGTector2_workflow.smk --use-conda --configfile path/to/config_HGTector2.yaml
```

<br>

# HGTector2 Analyze-Only Snakemake Workflow

This Snakemake workflow allows users to rerun **only the analysis step** of HGTector2 with different parameter settings, using previously generated search results.

## Workflow Overview

### Configuration
- Uses **`config_HGTector2_analyze.yaml`** by default if located in the **same directory**.
- If placed elsewhere, specify the path with:
  ```bash
  --configfile path/to/config_HGTector2_analyze.yaml
  ```

### Key Directories
- **`search_dir`**: Directory containing **existing HGTector search results**.
- **`analyze_dir`**: Directory for **storing new analysis results**.

## Workflow Rules

### 1. `all`
Ensures all final analysis results are generated.

### 2. `hgtector_analyze`
- Runs **HGTector analysis** on existing search results.
- Allows modification of **bandwidth, e-value, identity, coverage, and noise settings**.
- Supports **optional taxonomic filtering** via `self_tax` and `close_tax`.
- Saves final results in `analyze_dir`.

## Example Usage
The `--use-conda` flag is necessary if Snakemake is not installed in the same virtual environment as HGTector.

Run Snakemake with:
```bash
snakemake -s HGTector2_workflow_analyze.smk --use-conda --configfile path/to/config_HGTector2_analyze.yaml
```
<br>

# HGTector2 Results Collection Workflow

This Snakemake workflow automates the **collection and merging** of analyzed HGTector2 results into a single CSV file.

## Configuration
- Uses **`config_collect.yaml`** by default.
- If placed elsewhere, specify the path with:
  ```bash
  --configfile path/to/config_collect.yaml
  ```

## Key Directories
- **`analyze_dir`**: Directory containing **HGTector analysis results**.
- **`final_results`**: Directory where the **merged results CSV** will be stored.

## Workflow Rules

### 1. `all`
Ensures the final merged CSV file is generated.

### 2. `merge_txt_to_csv`
- Detects all **genome-specific result files** dynamically.
- Extracts **Protein_ID, Score, and Taxonomy_ID** from `.txt` files.
- Adds genome-specific headers for clarity.
- Merges all results into **`merged_results.csv`** in `final_results`.

## Usage
Run Snakemake with:
```bash
snakemake -s collect_results.smk --use-conda --configfile path/to/config_collect.yaml
```

<br>

# HGTector2 Adding Details Workflow

This Snakemake workflow enhances **HGTector2 results** by adding **gene names** and **product descriptions** extracted from `.faa` annotation files.

## Configuration

- Uses **`config_annotate.yaml`** by default.
- If placed elsewhere, specify the path with:
  ```bash
  --configfile path/to/config_annotate.yaml
  ```

## Key Directories

- **`input_dir`**: Directory containing **FAA annotation files**.
- **`merged_csv`**: Input **CSV file** before annotation expansion.
- **`final_csv`**: Output **CSV file** after annotation expansion.

## Workflow Rules

### 1. `all`

Ensures the final annotated CSV file is generated.

### 2. `expand_with_faa`

- Reads **merged HGTector2 results**.
- Extracts **gene names** and **product descriptions** from `.faa` files included in the fasta header
- Maps annotations to corresponding **Protein\_IDs**.
- Saves the final **annotated CSV** in `final_csv`.

## Usage

Run Snakemake with:

```bash
snakemake -s Add_details.smk --use-conda --configfile path/to/config_annotate.yaml
```










