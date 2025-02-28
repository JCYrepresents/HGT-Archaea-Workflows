import glob
import pandas as pd
import os
import re

# Define default config file
DEFAULT_CONFIG = "config_annotate.yaml"

# Check if the user provided a config file via `--configfile`
if not config:
    # If no config is provided, check if the default config file exists
    if os.path.exists(DEFAULT_CONFIG):
        configfile: DEFAULT_CONFIG
    else:
        raise ValueError(
            f"ERROR: No config file provided, and the default '{DEFAULT_CONFIG}' is missing. "
            "Please provide a config file using '--configfile path/to/config.yaml' when running Snakemake."
        )

# Define paths from config
input_dir = config["input_dir"]
merged_csv = config["merged_csv"]
final_csv = config["final_csv"]

# Locate all .faa annotation files
faa_files = glob.glob(f"{input_dir}/*.faa")

rule all:
    input:
        final_csv

rule expand_with_faa:
    input:
        csv=merged_csv
    output:
        final_csv
    run:
        # Read merged CSV
        df = pd.read_csv(input.csv)

        # Dictionary to store protein annotations from .faa files
        annotations = {}

        # Read all .faa files
        for faa_file in faa_files:
            with open(faa_file, "r") as f:
                for line in f:
                    if line.startswith(">"):
                        line = line.strip()[1:]  # Remove '>' at the start

                        # Updated regex: Captures both cases!
                        match = re.match(r"([A-Za-z0-9]+(?:_[A-Za-z0-9]+)?)_(\d+)", line)

                        if match:
                            genome_name, protein_id = match.groups()
                            protein_id = f"{genome_name}_{protein_id}"  # Reconstruct Protein ID
                        else:
                            # Fallback: Use the entire line as Protein ID
                            protein_id = line

                        # Extract Gene Name
                        gene_match = re.search(r"gene=([\w\d\-_]+)", line)
                        gene_name = gene_match.group(1) if gene_match else "Unknown"

                        # Extract Product
                        product_match = re.search(r"product=([\w\d\s\-_%,]+)", line)
                        product = product_match.group(1) if product_match else "Unknown"

                        # Store annotation using Protein ID as the key
                        annotations[protein_id] = (gene_name, product)

        # Merge annotation data into the CSV
        df["Gene_Name"] = df["Protein_ID"].map(lambda x: annotations.get(x, ("Unknown", "Unknown"))[0])
        df["Product"] = df["Protein_ID"].map(lambda x: annotations.get(x, ("Unknown", "Unknown"))[1])

        # Save final CSV
        df.to_csv(output[0], index=False)

