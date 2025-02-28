import pandas as pd

# Load CSV file
input_file = "test2.csv"  # Change to your actual file name
output_file = "Test2_done.csv"

# Read CSV with proper encoding and delimiter
df = pd.read_csv(input_file, delimiter=",", encoding="utf-8")

# 🔹 Clean Column Names
df.columns = df.columns.str.strip()

# 🔹 Fix Data Formatting
df["Gene_Name"] = df["Gene_Name"].astype(str).str.strip()
df["Product"] = df["Product"].astype(str).str.strip()
df["Tax ID"] = df["Tax ID"].astype(str)  # Ensure Tax ID is a string

# 🔹 Remove Rows with "Unknown" or "hypothetical protein"
df_cleaned = df[
    (~df["Gene_Name"].str.lower().str.contains("unknown", na=False)) &
    (~df["Product"].str.lower().str.contains("unknown|hypothetical protein", na=False))
]

# 🔹 Save the cleaned file
df_cleaned.to_csv(output_file, index=False)

print(f"✅ Formatting complete! Cleaned file saved as '{output_file}'")

