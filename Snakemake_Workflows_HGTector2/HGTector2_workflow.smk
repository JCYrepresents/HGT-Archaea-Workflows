# Define default config file
DEFAULT_CONFIG = "config_HGTector2.yaml"

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
search_dir = config["search_dir"]
analyze_dir = config["analyze_dir"]

# Get all sample names dynamically
samples = glob_wildcards(f"{input_dir}/{{sample}}.faa").sample

# Rule to ensure all final outputs are generated
rule all:
    input:
        expand(f"{analyze_dir}/{{sample}}", sample=samples)

# Rule for HGTector search
rule hgtector_search:
    input:
        proteome=f"{input_dir}/{{sample}}.faa"
    output:
        directory(f"{search_dir}/{{sample}}")
    params:
        db=config["database"]["diamond_db"],
        taxdump=config["database"]["taxdump"]
    threads: config["hgtector"]["threads"]
    conda: config["hgtector"]["conda_env"]
    shell:
        """
        mkdir -p {output} && \
        hgtector search -i {input.proteome} -o {output} \
            -m diamond -p {threads} -d {params.db} -t {params.taxdump}
        """

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
        noise=config["analysis_params"]["noise"]
    shell:
        """
        source activate hgtector && \
        mkdir -p {output} && \
        hgtector analyze -i {input.search_result} -o {output} \
            -t {params.taxdump} --bandwidth {params.bandwidth} \
            {params.donor_name} \
            --evalue {params.evalue} --identity {params.identity} \
            --coverage {params.coverage} --silhouette {params.silhouette} \
            --noise {params.noise}
        """


