import pandas as pd

# Load the CSV file (HGTector results)
csv_file_path = "Final_Table_HGTector.csv"
df_hgtector = pd.read_csv(csv_file_path, encoding='utf-8', dtype=str)

# Load the Excel file (genome lineage mapping)
excel_file_path = "Untitled 1.xlsx"
df_lineage = pd.read_excel(excel_file_path, dtype=str)

# Extract relevant columns from the Excel file
df_lineage_cleaned = df_lineage.iloc[2:, :2]  # Remove first two rows, keep first two columns
df_lineage_cleaned.columns = ["Genome", "Lineage"]  # Rename columns
df_lineage_cleaned = df_lineage_cleaned.dropna().reset_index(drop=True)  # Remove NaNs

# Extract genome names from the "##### New Genome: GUT_GENOMExxxxx #####" format in the CSV
df_hgtector["Extracted_Genome"] = df_hgtector["Genome"].str.extract(r'New Genome: (GUT_GENOME\d+)')

# Forward-fill the extracted genome name to associate rows with the correct genome
df_hgtector["Extracted_Genome"] = df_hgtector["Extracted_Genome"].ffill()

# Merge lineage information based on the extracted genome name
df_hgtector = df_hgtector.merge(df_lineage_cleaned, left_on="Extracted_Genome", right_on="Genome", how="left")

# Assign lineage only to the header rows
df_hgtector.loc[df_hgtector["Genome"].str.startswith("##### New Genome:"), "Lineage"] = df_hgtector["Lineage_y"]

# Drop the helper columns
df_hgtector.drop(columns=["Extracted_Genome", "Genome_y", "Lineage_y"], inplace=True)
df_hgtector.rename(columns={"Genome_x": "Genome"}, inplace=True)

# Save the cleaned file
output_file_path = "Final_Table_HGTector_lineage.csv"
df_hgtector.to_csv(output_file_path, index=False, encoding='utf-8')

print(f"Updated file saved as {output_file_path}")

