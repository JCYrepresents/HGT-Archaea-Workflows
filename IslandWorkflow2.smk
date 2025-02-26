import os

# Define default config file
DEFAULT_CONFIG = "config_islandviewer.yaml"

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

# Load input and output paths from config
INPUT_FOLDER = config["input_folder"]
OUTPUT_FOLDER = config["output_folder"]
ISLANDVIEWER_SCRIPT = config["islandviewer_script"]

# Ensure input directory exists
if not os.path.exists(INPUT_FOLDER):
    raise FileNotFoundError(f"ERROR: Input folder '{INPUT_FOLDER}' does not exist. Check your config file.")

# Get all .gbk files in the input folder
GENOME_FILES = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".gbk")]

rule all:
    input:
        expand(f"{OUTPUT_FOLDER}/{{genome}}.output", genome=[g.replace(".gbk", "") for g in GENOME_FILES])

rule submit_to_islandviewer:
    input:
        lambda wildcards: f"{INPUT_FOLDER}/{wildcards.genome}.gbk"
    output:
        f"{OUTPUT_FOLDER}/{{genome}}.output"
    shell:
        """
        python {ISLANDVIEWER_SCRIPT} {input} > {output}
        """

