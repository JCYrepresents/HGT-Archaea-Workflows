import requests
import sys
import argparse
from requests_toolbelt.multipart.encoder import MultipartEncoder

def submit_genome(genome_file):
    server = "https://www.pathogenomics.sfu.ca/islandviewer"
    ext = "/rest/submit/"

    multipart_data = MultipartEncoder(
        fields={ "format_type": "GENBANK",
                 'email_addr': 'my@email.address.com',
                 'genome_file': ('filename', open(genome_file, 'rb'), 'text/plain')}
    )
    
    headers={'Content-Type': multipart_data.content_type,
             'x-authtoken': 'c7dd915e-c6e3-6867-dc1c-8305a722fd50'}
    
    r = requests.post(server+ext, headers=headers, data=multipart_data)
    
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    
    decoded = r.json()
    print(repr(decoded))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Submit a genome file to IslandViewer.")
    parser.add_argument("genome_file", help="Path to the genome file (GenBank format)")
    
    args = parser.parse_args()
    submit_genome(args.genome_file)

