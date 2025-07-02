import argparse
import os
from rna_seq_processor import identify_highly_expressed_genes
from crispr_designer import design_crispr_guides
from library_optimizer import optimize_and_pool_library, generate_pooled_fasta

def main():
    parser = argparse.ArgumentParser(description="Tool to identify highly expressed genes from RNA-seq data and design CRISPR knockout/knockdown libraries.")
    parser.add_argument("expression_data", type=str, help="Path to the gene expression data file (CSV or TSV).")
    parser.add_argument("--threshold", type=float, default=100.0, help="Expression threshold for identifying highly expressed genes.")
    parser.add_argument("--guides_per_gene", type=int, default=3, help="Number of CRISPR guides to design per target gene.")
    parser.add_argument("--output_fasta", type=str, default="pooled_crispr_library.fasta", help="Output FASTA file name for the pooled CRISPR library.")

    args = parser.parse_args()

    print(f"\n--- Starting RNA-seq to CRISPR Library Design Tool ---")
    print(f"Input Expression Data: {args.expression_data}")
    print(f"Expression Threshold: {args.threshold}")
    print(f"Guides per Gene: {args.guides_per_gene}")
    print(f"Output FASTA File: {args.output_fasta}")

    # Step 1: Identify highly expressed genes
    print("\nStep 1: Identifying highly expressed genes...")
    highly_expressed_genes = identify_highly_expressed_genes(args.expression_data, args.threshold)

    if not highly_expressed_genes:
        print("No highly expressed genes found or an error occurred. Exiting.")
        return

    print(f"Found {len(highly_expressed_genes)} highly expressed genes.")
    print(f"Highly expressed genes (first 10): {highly_expressed_genes[:10]}...")

    # Step 2: Design CRISPR guides
    print("\nStep 2: Designing CRISPR guides...")
    designed_guides = design_crispr_guides(highly_expressed_genes)

    if not designed_guides:
        print("No CRISPR guides could be designed. Exiting.")
        return

    print(f"Designed guides for {len(designed_guides)} genes.")

    # Step 3: Optimize and pool library
    print("\nStep 3: Optimizing and pooling library...")
    optimized_library = optimize_and_pool_library(designed_guides, args.guides_per_gene)

    if not optimized_library:
        print("Library optimization failed. Exiting.")
        return

    print(f"Optimized library contains guides for {len(optimized_library)} genes.")

    # Step 4: Generate pooled FASTA file
    print("\nStep 4: Generating pooled FASTA file...")
    generate_pooled_fasta(optimized_library, args.output_fasta)

    print(f"\n--- Tool execution complete. Pooled CRISPR library saved to {args.output_fasta} ---")

if __name__ == '__main__':
    main()


