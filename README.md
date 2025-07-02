# CRISPR Library Designer from RNA-Seq Expression Data

This tool is a modular Python pipeline to automatically design and optimize a CRISPR guide RNA (gRNA) library from gene expression datasets. It integrates RNA-seq processing, CRISPR guide design, and library optimization — tailored for high-throughput functional genomics screens.

---

## 🧬 Features

- 📊 **Expression-Aware Filtering:** Uses RNA-seq data to prioritize genes based on expression levels.
- 🧪 **Automated Guide Design:** Generates guide RNAs for target genes.
- 🧠 **Optimization Engine:** Filters and optimizes CRISPR libraries for specificity and coverage.
- 🧬 **BioPython-Driven:** Uses robust parsing and sequence manipulation via BioPython.

---

## 🛠️ Dependencies

- Python 3.8+
- BioPython
- pandas
- numpy

Install dependencies:

```bash
pip install biopython pandas numpy
```

---

## 🚀 Usage

### 1. Prepare Inputs
- `test_expression_data.csv`: CSV file with genes and expression levels.
- (Optional) FASTA/GenBank files for your genome/transcriptome input.

### 2. Run the Pipeline

```bash
python main.py
```

This will:
- Load gene expression data.
- Filter top expressed genes.
- Design gRNAs using `crispr_designer.py`.
- Output a FASTA file: `test_crispr_library.fasta`.

---

## 📂 Modules Overview

| Module                 | Description |
|------------------------|-------------|
| `rna_seq_processor.py` | Parses RNA-seq CSV files and filters genes |
| `crispr_designer.py`   | Designs guide RNAs for filtered genes |
| `library_optimizer.py` | Optimizes the resulting gRNA set |
| `biopython_parser.py`  | Handles sequence file parsing and annotations |
| `main.py`              | Orchestrates the full workflow |

---

## 📁 Sample Output

- **FASTA File:** Optimized CRISPR library with gRNAs for top expressed genes.
- **Console Logs:** Details of selected genes, designed guides, and stats.

---

## 🧪 Example

```csv
# test_expression_data.csv
Gene,Expression
TP53,145.2
MYC,133.7
BCL2,120.1
```

---

## 📌 Future Improvements

- Add support for off-target scoring using CRISPRitz or CHOPCHOP API.
- Build Streamlit web UI for interactive use.
- Integrate genome annotations (e.g., GTF) for exon-specific targeting.

---

## 👨‍🔬 Authors

Built for computational biology and genome editing research.

---

