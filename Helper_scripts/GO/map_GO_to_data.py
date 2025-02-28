import pandas as pd
import numpy as np

# Load datasets
hgt_cleaned_path = "Final_Table_HGTector_Cleaned_1.csv"  # Update with actual path
merged_output_path = "Merged_Output_Data.csv"  # Update with actual path

hgt_cleaned_df = pd.read_csv(hgt_cleaned_path)
merged_output_df = pd.read_csv(merged_output_path)

# Normalize Gene_Name and Product formatting (remove extra spaces and newline characters)
hgt_cleaned_df["Gene_Name"] = hgt_cleaned_df["Gene_Name"].str.strip()
hgt_cleaned_df["Product"] = hgt_cleaned_df["Product"].str.strip().str.replace("\n", "", regex=True)

merged_output_df["Gene_Name"] = merged_output_df["Gene_Name"].str.strip()
merged_output_df["Product"] = merged_output_df["Product"].str.strip().str.replace("\n", "", regex=True)

# Extract and propagate lineage information from genome headers
hgt_cleaned_df["Extracted_Lineage"] = np.nan
header_rows = hgt_cleaned_df["Genome"].str.startswith("##### New Genome:")
hgt_cleaned_df.loc[header_rows, "Extracted_Lineage"] = hgt_cleaned_df.loc[header_rows, "Lineage"]
hgt_cleaned_df["Extracted_Lineage"] = hgt_cleaned_df["Extracted_Lineage"].fillna(method="ffill")

# Extract only the family name (f__FamilyName) from the propagated lineage
hgt_cleaned_df["Formatted_Lineage"] = hgt_cleaned_df["Extracted_Lineage"].str.extract(r'(f__\w+)')

# Create mapping dictionary
cleaned_go_terms_mapping = merged_output_df.set_index(["Gene_Name", "Product", "Lineage"])["GO_Terms"].to_dict()

# Apply mapping to fill GO functional term
def get_go_term(row):
    return cleaned_go_terms_mapping.get(
        (row["Gene_Name"], row["Product"], row["Formatted_Lineage"]),
        row["GO functional term"]  # Preserve existing values if not found
    )

hgt_cleaned_df["GO functional term"] = hgt_cleaned_df.apply(get_go_term, axis=1)

# Drop temporary columns
hgt_cleaned_df.drop(columns=["Extracted_Lineage", "Formatted_Lineage"], inplace=True)

# Save the updated file
output_path = "Final_HGTector_Cleaned_with_GO_Terms.csv"
hgt_cleaned_df.to_csv(output_path, index=False)

print(f"Processing complete. Output saved to: {output_path}")

