from typing import Dict, List

def optimize_and_pool_library(designed_guides: Dict[str, List[str]], guides_per_gene: int = 3) -> Dict[str, List[str]]:
    """
    Optimizes and pools CRISPR guides for library creation.

    Args:
        designed_guides (Dict[str, List[str]]): A dictionary where keys are gene IDs and values are lists of designed gRNA sequences.
        guides_per_gene (int): The number of top guides to select for each gene.

    Returns:
        Dict[str, List[str]]: A dictionary representing the optimized pooled library, with selected gRNAs for each gene.
    """
    optimized_library = {}
    for gene, grnas in designed_guides.items():
        # In a real scenario, gRNAs would have scores (e.g., on-target efficiency, off-target specificity).
        # We would sort them by score and select the top `guides_per_gene`.
        # For this dummy implementation, we'll just take the first `guides_per_gene` available.
        selected_grnas = grnas[:guides_per_gene]
        optimized_library[gene] = selected_grnas
        print(f"Selected {len(selected_grnas)} guides for {gene}")

    return optimized_library

def generate_pooled_fasta(optimized_library: Dict[str, List[str]], output_fasta_path: str):
    """
    Generates a FASTA file for the pooled CRISPR library.

    Args:
        optimized_library (Dict[str, List[str]]): The optimized pooled library.
        output_fasta_path (str): Path to save the pooled FASTA file.
    """
    with open(output_fasta_path, "w") as f:
        for gene, grnas in optimized_library.items():
            for i, grna in enumerate(grnas):
                # Assuming gRNA format is gene_gRNA#_SEQUENCE
                # Extract sequence part for FASTA entry
                sequence_part = grna.split("_")[-1]
                f.write(f">{gene}_gRNA{i+1}\n{sequence_part}\n")
    print(f"Pooled FASTA library generated at: {output_fasta_path}")

if __name__ == '__main__':
    # Example usage (for testing purposes)
    example_designed_guides = {
        "GeneA": ["GeneA_gRNA1_ACGTACGTACGTACGTACGT", "GeneA_gRNA2_TCGATCGATCGATCGATCGA", "GeneA_gRNA3_AGCTAGCTAGCTAGCTAGCT", "GeneA_gRNA4_GGGGGGGGGGGGGGGGGGGG"],
        "GeneC": ["GeneC_gRNA1_CGCGCGCGCGCGCGCGCGCG", "GeneC_gRNA2_TATATATATATATATATATA"],
        "GeneE": ["GeneE_gRNA1_CCCCCCCCCCCCCCCCCCCC", "GeneE_gRNA2_GGGGGGGGGGGGGGGGGGGG", "GeneE_gRNA3_TTTTTTTTTTTTTTTTTTTT"]
    }

    print("Optimizing and pooling library...")
    optimized_lib = optimize_and_pool_library(example_designed_guides, guides_per_gene=2)
    print("\nOptimized Library:", optimized_lib)

    output_file = "pooled_crispr_library.fasta"
    generate_pooled_fasta(optimized_lib, output_file)

    # Clean up dummy file
    import os
    os.remove(output_file)
    print("Dummy pooled FASTA file removed.")


