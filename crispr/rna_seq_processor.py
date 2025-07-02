import pandas as pd

def identify_highly_expressed_genes(expression_data_path: str, threshold: float = 100.0) -> list:
    """
    Identifies highly expressed genes from RNA-seq expression data.

    Args:
        expression_data_path (str): Path to the gene expression data file (CSV or TSV).
        threshold (float): Expression threshold to consider a gene highly expressed.

    Returns:
        list: A list of gene IDs that are highly expressed.
    """
    try:
        if expression_data_path.endswith('.csv'):
            df = pd.read_csv(expression_data_path)
        elif expression_data_path.endswith('.tsv'):
            df = pd.read_csv(expression_data_path, sep='\t')
        else:
            raise ValueError("Unsupported file format. Please provide a .csv or .tsv file.")

        # Assuming the first column is 'GeneID' and subsequent columns are expression values
        # For simplicity, we'll average expression across samples or take a specific column
        # This needs to be refined based on actual data structure and analysis needs
        if 'GeneID' not in df.columns:
            raise ValueError("Expected a 'GeneID' column in the expression data.")

        # Simple approach: average expression across all non-GeneID columns
        expression_columns = [col for col in df.columns if col != 'GeneID']
        if not expression_columns:
            raise ValueError("No expression columns found in the data.")

        df['Average_Expression'] = df[expression_columns].mean(axis=1)

        highly_expressed_genes = df[df['Average_Expression'] >= threshold]['GeneID'].tolist()
        return highly_expressed_genes

    except FileNotFoundError:
        print(f"Error: File not found at {expression_data_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == '__main__':
    # Example usage (for testing purposes)
    # Create a dummy expression data file
    dummy_data = {
        'GeneID': ['GeneA', 'GeneB', 'GeneC', 'GeneD', 'GeneE'],
        'Sample1': [150, 50, 200, 80, 120],
        'Sample2': [160, 40, 210, 90, 110]
    }
    dummy_df = pd.DataFrame(dummy_data)
    dummy_df.to_csv('dummy_expression.csv', index=False)

    print("Dummy expression data created: dummy_expression.csv")

    # Test the function
    highly_expressed = identify_highly_expressed_genes('dummy_expression.csv', threshold=100.0)
    print(f"Highly expressed genes: {highly_expressed}")

    # Clean up dummy file
    import os
    os.remove('dummy_expression.csv')
    print("Dummy expression data removed.")


