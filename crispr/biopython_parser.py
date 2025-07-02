from Bio import SeqIO
from typing import List, Dict

def parse_fasta(fasta_file_path: str) -> Dict[str, str]:
    """
    Parses a FASTA file and returns a dictionary of sequence IDs to sequences.

    Args:
        fasta_file_path (str): Path to the FASTA file.

    Returns:
        Dict[str, str]: A dictionary where keys are sequence IDs and values are sequences.
    """
    sequences = {}
    try:
        for record in SeqIO.parse(fasta_file_path, "fasta"):
            sequences[record.id] = str(record.seq)
        print(f"Successfully parsed FASTA file: {fasta_file_path}")
    except FileNotFoundError:
        print(f"Error: FASTA file not found at {fasta_file_path}")
    except Exception as e:
        print(f"An error occurred while parsing FASTA: {e}")
    return sequences

def parse_fastq(fastq_file_path: str) -> List[Dict[str, str]]:
    """
    Parses a FASTQ file and returns a list of dictionaries, each containing 'id', 'sequence', and 'quality'.

    Args:
        fastq_file_path (str): Path to the FASTQ file.

    Returns:
        List[Dict[str, str]]: A list of dictionaries for each record.
    """
    records = []
    try:
        for record in SeqIO.parse(fastq_file_path, "fastq"):
            records.append({
                'id': record.id,
                'sequence': str(record.seq),
                'quality': str(record.letter_annotations["phred_quality"])
            })
        print(f"Successfully parsed FASTQ file: {fastq_file_path}")
    except FileNotFoundError:
        print(f"Error: FASTQ file not found at {fastq_file_path}")
    except Exception as e:
        print(f"An error occurred while parsing FASTQ: {e}")
    return records

if __name__ == '__main__':
    # Example usage (for testing purposes)
    # Create dummy FASTA and FASTQ files
    with open("dummy.fasta", "w") as f:
        f.write(">Gene1\nATGCGTACGT\n>Gene2\nCGTAGCTAGC\n")
    print("Dummy FASTA file created: dummy.fasta")

    with open("dummy.fastq", "w") as f:
        f.write("@Read1\nATGC\n+\nIIII\n@Read2\nGTAC\n+\nJJJJ\n")
    print("Dummy FASTQ file created: dummy.fastq")

    # Test FASTA parsing
    fasta_sequences = parse_fasta("dummy.fasta")
    print("\nParsed FASTA sequences:", fasta_sequences)

    # Test FASTQ parsing
    fastq_records = parse_fastq("dummy.fastq")
    print("\nParsed FASTQ records:", fastq_records)

    # Clean up dummy files
    import os
    os.remove("dummy.fasta")
    os.remove("dummy.fastq")
    print("\nDummy files removed.")


