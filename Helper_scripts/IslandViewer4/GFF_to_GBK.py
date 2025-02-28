from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqRecord import SeqRecord

# Load genome sequence
genome_record = SeqIO.read("genome.fasta", "fasta")

# Load protein sequences
protein_dict = SeqIO.to_dict(SeqIO.parse("proteins.fasta", "fasta"))

# Create GenBank record
genbank_record = SeqRecord(
    seq=genome_record.seq,
    id=genome_record.id,
    description="GenBank file generated from GFF",
    annotations={"molecule_type": "DNA"}  #Ensures valid GenBank format
)

# Load GFF annotations
with open("genome.gff") as gff_handle:
    for line in gff_handle:
        if line.startswith("#"):
            continue  # Skip comments
        
        fields = line.strip().split("\t")
        if len(fields) < 9:
             continue  # Skip lines that are too short
        feature_type = fields[2]  # CDS, gene, exon, etc.
        start, end = int(fields[3]), int(fields[4])
        strand = 1 if fields[6] == "+" else -1

        # Parse attributes
        attributes = {}
        for attr in fields[8].split(";"):
            if "=" in attr:
                key, value = attr.split("=")
                attributes[key] = value

        # Gene Name, Locus Tag, and Product Information
        gene_name = attributes.get("gene", attributes.get("Name", ""))
        locus_tag = attributes.get("locus_tag", attributes.get("ID", ""))
        product = attributes.get("product", "")

        # Protein translation if available
        protein_id = attributes.get("ID", "")
        translation = str(protein_dict.get(protein_id, "").seq) if protein_id in protein_dict else ""

        # Create Feature
        qualifiers = {}
        if gene_name:
            qualifiers["gene"] = [gene_name]
        if locus_tag:
            qualifiers["locus_tag"] = [locus_tag]
        if product:
            qualifiers["product"] = [product]
        if translation and feature_type == "CDS":
            qualifiers["translation"] = [translation]

        feature = SeqFeature(
            FeatureLocation(start, end, strand=strand),
            type=feature_type,
            qualifiers=qualifiers
        )
        genbank_record.features.append(feature)

# Save GenBank file with annotations
SeqIO.write(genbank_record, "genome_with_annotations.gbk", "genbank")

print(" GenBank file saved with gene names, locus tags, and product descriptions!")

