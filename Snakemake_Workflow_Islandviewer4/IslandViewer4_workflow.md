# IslandViewer Snakemake Workflow

This Snakemake workflow automates **IslandViewer** analysis by processing GenBank (`.gbk`) files and storing the output in a designated results folder.

## Configuration
- Uses **`config_islandviewer.yaml`** by default.
- If placed elsewhere, specify the path with:
  ```bash
  --configfile path/to/config_islandviewer.yaml
  ```

## Key Directories
- **`islandviewer_script`**: Path to the **IslandViewer2.py script** used for analysis.
- **`input_folder`**: Directory containing **GenBank (`.gbk`) files**.
- **`output_folder`**: Directory where **IslandViewer results** will be stored.

## Workflow Rules

### 1. `all`
Ensures all **IslandViewer outputs** are generated.

### 2. `submit_to_islandviewer`
- Detects all **.gbk genome files** in `input_folder`.
- Runs **IslandViewer4 analysis** on each genome.
- Saves results in `output_folder`.

## Usage
Run Snakemake with:
```bash
snakemake -s IslandWorkflow.smk --configfile path/to/config_islandviewer.yaml
```

For modifications, update the workflow or configuration file as needed.

