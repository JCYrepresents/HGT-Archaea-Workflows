import os
import glob

# Define default config file
DEFAULT_CONFIG = "config_HGTector2_analyze.yaml"

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
search_dir = config["search_dir"]  # This is where we look for existing search results
analyze_dir = config["analyze_dir"]  # Output directory for analysis results

# Find all subdirectories in search_dir (i.e., processed samples)
samples = [os.path.basename(f) for f in glob.glob(f"{search_dir}/*") if os.path.isdir(f)]

# Rule to ensure all final outputs are generated
rule all:
    input:
        expand(f"{analyze_dir}/{{sample}}", sample=samples)

# Rule for HGTector analyze
rule hgtector_analyze:
    input:
        search_result=f"{search_dir}/{{sample}}"
    output:
        directory(f"{analyze_dir}/{{sample}}")
    params:
        taxdump=config["database"]["taxdump"],
        bandwidth=config["analysis_params"]["bandwidth"],
        donor_name="--donor-name" if config["analysis_params"]["donor_name"] else "",
        evalue=config["analysis_params"]["evalue"],
        identity=config["analysis_params"]["identity"],
        coverage=config["analysis_params"]["coverage"],
        silhouette=config["analysis_params"]["silhouette"],
        noise=config["analysis_params"]["noise"],
        self_tax=f"--self-tax {config['analysis_params']['self_tax']}" if config["analysis_params"].get("self_tax") else "",
        close_tax=f"--close-tax {config['analysis_params']['close_tax']}" if config["analysis_params"].get("close_tax") else ""

    conda: config["hgtector"]["conda_env"]
    shell:
        """
        mkdir -p {output} && \
        hgtector analyze -i {input.search_result} -o {output} \
            -t {params.taxdump} --bandwidth {params.bandwidth} \
            {params.donor_name} \
            --evalue {params.evalue} --identity {params.identity} \
            --coverage {params.coverage} --silhouette {params.silhouette} \
            --noise {params.noise} \
            {params.self_tax} {params.close_tax}
        """

