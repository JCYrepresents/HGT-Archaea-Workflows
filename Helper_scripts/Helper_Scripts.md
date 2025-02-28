
# Helper scripts for HGTector2:

## GFF to FAA Converter
This script extracts coding sequences (CDS) from GFF files, translates them into protein sequences, and outputs them as FASTA (.faa) files. It also logs any missing sequence IDs.

### Features
- Extracts CDS regions from **GFF** files.
- Translates nucleotide sequences into **protein sequences**.
- Includes **gene** and **product** annotations in FASTA headers.
- Supports **batch conversion** of multiple GFF files.
- Logs missing sequence IDs for debugging.

### Usage
Run the script from the command line:
```bash
python GFF_to_FAA.py <input_directory> <output_directory> <log_file>
```
### Arguments:
- `<input_directory>`: Folder containing GFF files.
- `<output_directory>`: Folder where FAA files will be saved.
- `<log_file>`: File to log missing sequence IDs or errors.

This script processes **GFF files** by extracting **CDS sequences**, translating them into **proteins**, and saving them as **FASTA (.faa) files**. It uses Biopython to handle sequence parsing and translation. The script allows **batch processing** of multiple files and generates a log file to track missing sequences or errors. Only **CDS** entries are processed, and if a sequence ID is not found in the FASTA section of the GFF, a warning is logged.


## Include Lineage
This script integrates **genome lineage information** into **HGTector results** by extracting genome names, mapping them to their lineage, and updating the **HGTector output**

### Usage
Run the script:

```python
python Include_lineage.py
```

### Input Files:
- `Final_Table_HGTector.csv`: HGTector results.
- `Lineage_map_file.xlsx`: Genome lineage mapping.

### Output:
- `Final_Table_HGTector_lineage.csv`: Updated results with lineage data.

### Notes
- Assumes genome names follow `##### New Genome: GUT_GENOMExxxxx #####`.
- Lineage info is applied only to **header rows**.
- Ensure input files are correctly formatted.

# Helper scripts for IslandViewer4:

## GFF to GBK Converter
This script converts **GFF annotations** and associated **FASTA sequences** into a structured **GenBank (.gbk) file** by incorporating gene names, locus tags, and product descriptions.

### Features
- Loads **genome sequence** from a FASTA file.
- Extracts **protein sequences** from a FASTA file.
- Parses **GFF annotations** and converts them into GenBank features.
- Integrates **gene names, locus tags, and product descriptions**.
- Saves the final output as a **GenBank (.gbk) file**.

### Requirements
This script requires **Python 3** and the following dependencies:
- `Biopython`

Install dependencies with:
```bash
pip install biopython
```

### Usage
Run the script as follows:

```python
python GFF_to_GBK.py
```

### Input Files:
- `genome.fasta`: FASTA file containing the genome sequence.
- `proteins.fasta`: FASTA file containing protein sequences.
- `genome.gff`: GFF file with genome annotations.

### Output File:
- `genome_with_annotations.gbk`: GenBank file with integrated annotations.

### Process Overview
1. **Load Data:** Reads genome and protein sequences.
2. **Parse GFF:** Extracts annotation data and attributes.
3. **Create Features:** Adds extracted features (CDS, genes, etc.) to the GenBank record.
4. **Save Output:** Writes the annotated GenBank file.

### Notes
- The script ensures **valid GenBank format** by setting `molecule_type` to **DNA**.
- Extracted **CDS features** include protein translations when available.
- Only **valid GFF entries** are processed (skips incomplete or malformed lines).

  
## IslandViewer4 TSV Merger
This script merges multiple **TSV result files** from **IslandViewer4** into a single structured file while preserving genome names as headers.

### Features
- Processes all **TSV files** in a specified directory.
- Extracts **genome names** from filenames.
- Inserts **genome name headers** before corresponding data.
- Skips empty files to ensure data integrity.
- Saves the final merged dataset as a new **TSV file**.

### Usage
Run the script to merge TSV files:

```python
python merge_islandviewer_tsv.py
```

### Configuration
Update the `directory_path` variable in the script to the folder containing the **TSV files**:
```python
directory_path = "/path/to/your/tsv/files/"
```

### Output
- **`merged_genomes_corrected.tsv`**: Final merged file with genome headers included.

### Notes
- Only **TSV files** from the specified directory are processed.
- Headers are added as `## Genome_Name ##` before each dataset.
- Empty files are skipped to prevent errors.

# Helper scripts for both:

## HGTector-IslandViewer Results Merger

This script refines and merges **HGTector results** with **IslandViewer4 predictions**, ensuring accurate mapping of protein IDs and genome lineage data.

### Features
- Loads **HGTector results** and **IslandViewer4 Results **.
- Extracts **genome-lineage mapping** from header rows.
- Assigns **lineage information** to protein entries.
- Performs **refined merging** based on exact **Protein_ID** matches.
- Groups multiple **method annotations** per protein.
- Ensures **HGTector** is always included in the method column.
- Saves the final merged dataset as a structured **CSV file**.

### Usage
Run the script:

```python
python merge_result_Islector_right.py
```

### Input Files:
- `Final_final_table_Results.csv`: HGTector results.
- `merged_genomes_corrected_final.tsv`: IslandViewer4 merged genome results.

### Output File:
- `Refined_Merged_Table.csv`: Merged results with Gene names, products, island locations, functional data, etc.

## Notes
- Extracts lineage from **header rows** and applies it to relevant entries.
- Only keeps **exact matches** between `Protein_ID` and `Locus`.
- Aggregates multiple **methods** per protein, ensuring **HGTector** is always included.



















  

