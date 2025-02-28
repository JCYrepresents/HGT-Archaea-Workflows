# Helper Scripts

## For HGTector2 
# GFF to FAA Converter

This script extracts coding sequences (CDS) from GFF files, translates them into protein sequences, and outputs them as FASTA (.faa) files. It also logs any missing sequence IDs.

## Features
- Extracts CDS regions from **GFF** files.
- Translates nucleotide sequences into **protein sequences**.
- Includes **gene** and **product** annotations in FASTA headers.
- Supports **batch conversion** of multiple GFF files.
- Logs missing sequence IDs for debugging.

## Usage

Run the script from the command line:

```bash
python batch_gff_to_faa.py <input_directory> <output_directory> <log_file>
```

### Arguments:
- `<input_directory>`: Folder containing GFF files.
- `<output_directory>`: Folder where FAA files will be saved.
- `<log_file>`: File to log missing sequence IDs or errors.

## Summary
This script processes **GFF files** by extracting **CDS sequences**, translating them into **proteins**, and saving them as **FASTA (.faa) files**. It uses Biopython to handle sequence parsing and translation. The script allows **batch processing** of multiple files and generates a log file to track missing sequences or errors. Only **CDS** entries are processed, and if a sequence ID is not found in the FASTA section of the GFF, a warning is logged.

For any issues or improvements, feel free to modify the script or contribute!  

