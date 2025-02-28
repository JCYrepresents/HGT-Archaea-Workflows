# UniProtKB GO-term fetcher

This script retrieves **Gene Ontology (GO) terms** for genes or protein products by querying **UniProtKB** with taxonomy filtering.

## Features
- Queries **UniProtKB** using gene names, product names, and taxonomy IDs.
- Implements **retry logic** to handle API rate limits and network errors.
- Extracts and prioritizes **Molecular Function (F:) GO terms**.
- Saves results into a structured **CSV file**.

## Requirements
This script requires **Python 3** and the following dependencies:
- `requests`

Install dependencies with:
```bash
pip install requests
```

## Usage
Run the script to fetch GO terms:

```python
python GO_retrieval.py
```

### Input File:
- `Input.csv`: Cleaned dataset containing **Gene_Name**, **Product**, and **Tax ID**.

### Output File:
- `Output.csv`: Updated dataset with retrieved GO terms.

## Notes
- Implements **exponential backoff** to handle API rate limits.
- Filters and ranks GO terms based on **evidence confidence**.
- Adds a **1-second delay per request** to avoid rate limits.

# GO-term Mapper for HGTector Data

This script maps **GO-terms (MF)** to **HGTector2 results** by matching gene names, product descriptions, and lineage data.

## Features
- Loads **HGTector2 cleaned results** and **GO-term dataset**.
- Normalizes **Gene_Name** and **Product** formatting.
- Extracts and propagates **lineage information** from genome headers.
- Maps **GO-terms** based on **Gene_Name, Product, and Lineage**.
- Preserves existing GO terms if no match is found.
- Saves the updated dataset as a structured **CSV file**.

## Requirements
This script requires **Python 3** and the following dependencies:
- `numpy`

Install dependencies with:
```bash
pip install numpy
```

## Usage
Run the script to update GO terms in the dataset:

```python
python map_GO_to_data.py
```

### Input Files:
- `HGTector_Results.csv`: HGTector2 results.
- `GO_retrieval_output.csv`: Retrieved dataset containing GO terms.

### Output File:
- `HGTector_Results_with_GO_Terms.csv`: Updated HGTector2 results with GO annotations.

## Notes
- Extracts **family-level lineage** (`f__FamilyName`) for improved mapping accuracy.
- Uses **forward fill** to propagate lineage information from genome headers.
- Ensures **existing GO-terms** are preserved if no new match is found.







