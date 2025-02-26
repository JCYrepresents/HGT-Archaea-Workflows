import pandas as pd

# Load datasets
output_file_path = "go_terms_output_final_fin.csv"  # Update with actual path
lineage_file_path = "Unique_Families.csv"  # Update with actual path

output_df = pd.read_csv(output_file_path)
lineage_df = pd.read_csv(lineage_file_path)

# Merge lineage information based on Tax ID
merged_df = output_df.merge(lineage_df, on="Tax ID", how="left")

# Rename the 'Unique Families' column to 'Lineage' to match the intended column
merged_df.rename(columns={"Unique Families": "Lineage"}, inplace=True)

# Save the updated file
output_path = "Updated_GO_Terms_with_Lineage.csv"
merged_df.to_csv(output_path, index=False)

print(f"Processing complete. Output saved to: {output_path}")

