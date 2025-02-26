import os
import pandas as pd

# Define the directory containing the .tsv files
directory_path = "/root/IslandViewer4/Results/"  # <-- UPDATE THIS TO YOUR DIRECTORY PATH

# Get all .tsv files in the directory
file_paths = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith(".tsv")]

# Initialize an empty list to store the dataframes
dataframes = []

# Process each file
for file_path in file_paths:
    try:
        # Extract genome name from the filename
        genome_name = os.path.basename(file_path).replace(".tsv", "")

        # Read the TSV file, ensuring all values are read as strings
        df = pd.read_csv(file_path, sep='\t', dtype=str)

        if df.empty:
            print(f"Skipping empty file: {file_path}")
            continue

        # Add a header row as a separate dataframe
        header_df = pd.DataFrame({df.columns[0]: [f"## {genome_name} ##"]})

        # Append both the header and data to the list
        dataframes.append(header_df)
        dataframes.append(df)

        print(f"Processed: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# Concatenate all dataframes if any exist
if dataframes:
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save to a new TSV file
    output_path = os.path.join(directory_path, "merged_genomes_corrected.tsv")
    merged_df.to_csv(output_path, sep='\t', index=False)

    print(f"\nMerged file saved as: {output_path}")
else:
    print("\nNo valid TSV files found in the directory.")

