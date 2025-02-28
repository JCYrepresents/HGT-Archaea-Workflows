import requests
import pandas as pd
import time

# Function to query UniProt
def query_uniprot(gene_name, product_name, tax_id):
    """Fetches GO terms for a given gene or product name, restricting search by tax ID."""
    
    def search_uniprot(query, tax_id):
        """Search UniProt for protein accessions based on query and tax ID with retry logic."""
        base_url = "https://rest.uniprot.org/uniprotkb/search"
        query_string = f"({query}) AND taxonomy_id:{tax_id}"

        params = {
            "query": query_string,
            "fields": "accession,id,protein_name,go",
            "format": "json",
            "size": 1
        }

        # Implement retry logic
        for attempt in range(5):  # Retry up to 5 times
            try:
                response = requests.get(base_url, params=params, timeout=30)  # Increased timeout
                if response.status_code == 200:
                    data = response.json()
                    return [entry["primaryAccession"] for entry in data.get("results", [])]
                elif response.status_code == 429:  # Too many requests
                    wait_time = (attempt + 1) * 2  # Exponential backoff
                    print(f" Rate limit hit. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    break  # If other errors occur, exit retry loop
            except requests.exceptions.RequestException as e:
                print(f"Network error (attempt {attempt+1}/5): {e}")
                time.sleep((attempt + 1) * 2)  # Exponential backoff
        return []  # Return empty list if all attempts fail

    def fetch_uniprot_entries(accessions):
        """Fetches GO terms from multiple UniProt accessions with retry logic."""
        go_terms = {}

        for accession in accessions:
            base_url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
            
            # Implement retry logic for fetching data
            for attempt in range(5):
                try:
                    response = requests.get(base_url, timeout=30)  # Increased timeout
                    if response.status_code == 200:
                        data = response.json()
                        if "uniProtKBCrossReferences" in data:
                            for ref in data["uniProtKBCrossReferences"]:
                                if ref["database"] == "GO":
                                    go_id = ref["id"]
                                    go_name, evidence = None, "IEA:Unknown"
                                    for prop in ref.get("properties", []):
                                        if prop["key"] == "GoTerm":
                                            go_name = prop["value"]
                                        if prop["key"] == "GoEvidenceType":
                                            evidence = prop["value"]

                                    if go_name and go_name.startswith("F:"):  # Only Molecular Function GO terms
                                        clean_go_name = go_name[2:]  # Remove 'F:' prefix
                                        if clean_go_name not in go_terms or evidence_priority(evidence) < evidence_priority(go_terms[clean_go_name][1]):
                                            go_terms[clean_go_name] = (go_id, evidence)
                        break  # Exit loop if successful
                    elif response.status_code == 429:  # Too many requests
                        wait_time = (attempt + 1) * 2
                        print(f" Rate limit hit. Retrying in {wait_time}s...")
                        time.sleep(wait_time)
                    else:
                        break
                except requests.exceptions.RequestException as e:
                    print(f" Network error (attempt {attempt+1}/5): {e}")
                    time.sleep((attempt + 1) * 2)
        
        return go_terms

    def evidence_priority(evidence):
        """Ranks confidence: EXP > ISS > IEA."""
        if evidence.startswith(("EXP", "IDA", "IPI")):
            return 1  # High confidence
        elif evidence.startswith(("ISS", "ISA", "IBA")):
            return 2  # Medium confidence
        else:
            return 3  # Low confidence (IEA)

    accessions = search_uniprot(gene_name, tax_id) or search_uniprot(product_name, tax_id)
    go_terms = fetch_uniprot_entries(accessions)

    return "; ".join([f"{v[0]} ({k}) [Confidence: {v[1]}]" for k, v in sorted(go_terms.items(), key=lambda x: evidence_priority(x[1][1]))]) if go_terms else "No GO terms found"

# Load  CSV file
input_file = "input.csv" # Adjust file paths/name 
output_file = "output.csv" #Adjust file paths/name 

df = pd.read_csv(input_file, delimiter=",", encoding="utf-8")

# 🔹 Clean & Format Data
df.columns = df.columns.str.strip()
df["Gene_Name"] = df["Gene_Name"].astype(str).str.strip()
df["Product"] = df["Product"].astype(str).str.strip()
df["Tax ID"] = df["Tax ID"].astype(str).str.strip().str.replace(r"[^0-9]", "", regex=True)

# 🔹 Run UniProt Queries & Store Results
df["GO_Terms"] = df.apply(
    lambda row: (
        time.sleep(1),  # Prevent API rate limits
        query_uniprot(row["Gene_Name"], row["Product"], row["Tax ID"])
    )[-1], axis=1  # Retrieve last function output (GO terms)
)

# 🔹 Save results
df.to_csv(output_file, index=False)

print(f"Processing complete! GO terms saved to '{output_file}'")

