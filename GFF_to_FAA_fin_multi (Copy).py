import os
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import io

def parse_gff_with_gene_and_product(input_gff, output_fasta, log_file):
    genome_dict = {}
    parsing_fasta = False

    # Open the GFF file
    with open(input_gff, "r") as gff_file:
        fasta_lines = []

        for line in gff_file:
            if line.startswith("##FASTA"):
                parsing_fasta = True
                continue
            if parsing_fasta:
                # Collect all FASTA lines
                fasta_lines.append(line)

        # Parse the FASTA section using StringIO
        fasta_content = "".join(fasta_lines)
        fasta_handle = io.StringIO(fasta_content)
        for record in SeqIO.parse(fasta_handle, "fasta"):
            genome_dict[record.id.strip()] = record.seq
    
    normalized_fasta_ids = {key.lower().strip(): genome_dict[key] for key in genome_dict}

    # Re-open the GFF file to parse annotations
    with open(input_gff, "r") as gff_file, open(output_fasta, "w") as fasta_file:
        for line in gff_file:
            if line.startswith("#") or not line.strip():
                continue  # Skip comments and empty lines
            if line.startswith("##FASTA"):
                break  # Stop parsing annotations once FASTA begins
            columns = line.strip().split("\t")
            if len(columns) < 9 or columns[2] != "CDS":
                continue  # Skip lines that are not CDS
            
            seq_id = columns[0].strip()
            start = int(columns[3]) - 1  # Convert to 0-based index
            end = int(columns[4])
            strand = columns[6]
            attributes = {key_value.split("=")[0]: key_value.split("=")[1]
                          for key_value in columns[8].split(";") if "=" in key_value}
            cds_id = attributes.get("ID", "unknown_id")
            product = attributes.get("product", "unknown_product")
            gene_name = attributes.get("gene", "unknown_gene")
            
            if seq_id.lower().strip() in normalized_fasta_ids:
                genome_seq = normalized_fasta_ids[seq_id.lower().strip()]
                if strand == "+":
                    cds_seq = genome_seq[start:end]
                else:
                    cds_seq = genome_seq[start:end].reverse_complement()
                
                protein_seq = cds_seq.translate(to_stop=True)
                
                description = f"gene={gene_name} product={product}"
                record = SeqRecord(protein_seq, id=cds_id, description=description)
                SeqIO.write(record, fasta_file, "fasta")
            else:
                with open(log_file, "a") as log:
                    log.write(f"Warning: Sequence ID '{seq_id}' not found in genome FASTA.\n")

def batch_convert_gff_to_faa(input_dir, output_dir, log_file):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(log_file, "w") as log:
        log.write("Processing log for GFF to FAA conversion\n\n")
    
    for file in os.listdir(input_dir):
        if file.endswith(".gff"):
            input_gff = os.path.join(input_dir, file)
            output_faa = os.path.join(output_dir, file.replace(".gff", ".faa"))
            
            try:
                parse_gff_with_gene_and_product(input_gff, output_faa, log_file)
                with open(log_file, "a") as log:
                    log.write(f"Successfully converted {file} to {output_faa}\n")
            except Exception as e:
                with open(log_file, "a") as log:
                    log.write(f"Error processing {file}: {str(e)}\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python batch_gff_to_faa.py <input_directory> <output_directory> <log_file>")
    else:
        input_directory = sys.argv[1]
        output_directory = sys.argv[2]
        log_file = sys.argv[3]
        batch_convert_gff_to_faa(input_directory, output_directory, log_file)
