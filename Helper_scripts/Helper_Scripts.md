# Helper Scripts

## for HGTector2:

### GFF to FAA Converter

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
python hgtector_lineage_mapper.py
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

## for IslandViewer4:






  

