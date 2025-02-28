# UniProtKB GO-term fetcher

This script retrieves **Gene Ontology (GO) terms** for genes or protein products by querying **UniProt** with taxonomy filtering.

## Features
- Queries **UniProt** using gene names, product names, and taxonomy IDs.
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




