import os
import glob
import pandas as pd

# Define default config file
DEFAULT_CONFIG = "config_collect.yaml"

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
analyze_dir = config["analyze_dir"]
final_results = config["final_results"]

# Locate all genome directories dynamically
genome_dirs = glob.glob(f"{analyze_dir}/*")
genomes = [os.path.basename(g) for g in genome_dirs if os.path.isdir(g)]  # Extract genome names

rule all:
    input:
        f"{final_results}/merged_results.csv"

rule merge_txt_to_csv:
    input:
        expand(f"{analyze_dir}/{{genome}}/hgts/{{genome}}.txt", genome=genomes)  # Detect genomes dynamically
    output:
        f"{final_results}/merged_results.csv"
    run:
        os.makedirs(final_results, exist_ok=True)  # Ensure output directory exists
        data = []

        for txt_file in input:
            genome_name = os.path.basename(os.path.dirname(os.path.dirname(txt_file)))  # Extract genome name
            
            # Read file content if it exists and is non-empty
            if os.path.getsize(txt_file) > 0:
                data.append(["##### New Genome: " + genome_name + " #####", "", "", ""])  # Separator row
                
                df = pd.read_csv(txt_file, sep="\t", header=None, names=["Protein_ID", "Score", "Taxonomy_ID"])
                df.insert(0, "Genome", genome_name)  # Add Genome column
                data.extend(df.values.tolist())  # Append processed data

        # Convert to DataFrame and save
        if data:
            df_final = pd.DataFrame(data, columns=["Genome", "Protein_ID", "Score", "Taxonomy_ID"])
            df_final.to_csv(output[0], index=False)

