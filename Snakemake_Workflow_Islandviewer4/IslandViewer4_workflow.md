# IslandViewer4 Snakemake Workflow

This Snakemake workflow automates **IslandViewer4** analysis by processing GenBank (`.gbk`) files and storing the output in a designated results folder.

## Configuration

- Uses **`config_islandviewer.yaml`** by default.
- If placed elsewhere, specify the path with:
  ```bash
  --configfile path/to/config_islandviewer.yaml
  ```

## Key Directories

- **`islandviewer_script`**: Path to the **IslandViewer2.py script** used for analysis.
- **`input_folder`**: Directory containing **GenBank (*`.gbk`* files**.
- **`output_folder`**: Directory where **IslandViewer4 job tokens** will be stored.

## IslandViewer2 Script

This script submits genome files to the **IslandViewer4** server for genomic island prediction.

### API Submission Details

- **Server URL**: `https://www.pathogenomics.sfu.ca/islandviewer/rest/submit/`
- **Submission Format**: `GENBANK`
- **Required Fields**:
  - `email_addr`: User email for job tracking.
  - `genome_file`: The genome file in GenBank format.
- **Headers**:
  - `Content-Type`: Multipart encoding type.
  - `x-authtoken`: API authentication token (retrieved by logging into IslandViewer).  

### Running the Script for a single Genome

Run the script manually with:

```bash
python IslandViewer2.py path/to/genome_file.gbk
```

## Workflow Rules

### 1. `all`

Ensures all **IslandViewer outputs** are generated.

### 2. `submit_to_islandviewer`

- Detects all **.gbk genome files** in `input_folder`.
- Runs **IslandViewer4 analysis** on each genome.
- Saves results in `output_folder`.

## Usage

Run Snakemake for a batch of genomes with:

```bash
snakemake -s IslandWorkflow.smk --configfile path/to/config_islandviewer.yaml
```

### Getting Results 

After successful completion of the workflow **job tokens** are provided. One can use this token to visualize and download the prediction results at:

```bash
https://www.pathogenomics.sfu.ca/islandviewer/results/job_token
```



