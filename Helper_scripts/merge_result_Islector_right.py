import pandas as pd

# Load the datasets
final_results_path = "Final_final_table_Results.csv"
merged_genomes_path = "merged_genomes_corrected_final.tsv"

df_results = pd.read_csv(final_results_path)
df = pd.read_csv(merged_genomes_path, sep='\t')

# Extract genome-to-lineage mapping from header rows
header_rows = df_results[df_results['Genome'].astype(str).str.startswith("#####")].copy()
header_rows['Genome'] = header_rows['Genome'].str.extract(r'##### New Genome: (.+) #####')
genome_lineage_map = dict(zip(header_rows['Genome'], header_rows['Taxonomy_ID']))

# Remove metadata rows from df_results
df_results_clean = df_results[~df_results['Genome'].astype(str).str.startswith("#####")].copy()

# Assign lineage based on the Genome column
df_results_clean['Lineage'] = df_results_clean['Genome'].map(genome_lineage_map)

# Find exact matches between Protein_ID in df_results_clean and Locus in df
matching_protein_ids = df_results_clean[df_results_clean['Protein_ID'].isin(df['Locus'])]['Protein_ID'].unique()

# Perform the refined merge with only the matched Protein_IDs
refined_merge = df_results_clean.merge(
    df[['Locus', 'Method', 'Predicted Island Start', 'Predicted Island End']], 
    left_on='Protein_ID', 
    right_on='Locus', 
    how='inner'  # Only keep matches
)

# Retain lineage information after merging
refined_merge['Lineage'] = refined_merge['Genome'].map(genome_lineage_map)

# Drop unnecessary columns: 'Score', 'Taxonomy_ID', and duplicate 'Locus'
refined_merge = refined_merge.drop(columns=['Score', 'Taxonomy_ID', 'Locus'])

# Reorder columns to place Method and island information before GO functional term
column_order = ['Genome', 'Protein_ID', 'Gene_Name', 'Product', 'Method', 'Predicted Island Start', 'Predicted Island End', 'GO functional term', 'Lineage']
refined_merge = refined_merge[column_order]

# Group by Protein_ID and aggregate multiple methods
refined_merge['Method'] = refined_merge.groupby('Protein_ID')['Method'].transform(lambda x: '; '.join(sorted(set(x.dropna()))))

# Remove duplicates after method aggregation
refined_merge = refined_merge.drop_duplicates()

# Ensure HGTector is always included in the Method column
refined_merge['Method'] = refined_merge['Method'].apply(
    lambda x: 'HGTector' if pd.isna(x) else f"HGTector; {x}" if 'HGTector' not in x else x
)

# Save the final refined table
refined_merge.to_csv("Refined_Merged_Table.csv", index=False)

print("Refined merge completed and saved as 'Refined_Merged_Table.csv'")

