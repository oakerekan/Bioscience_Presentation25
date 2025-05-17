# Python for Bioscientists

A hands-on Jupyter Notebook introducing core Python concepts, data structures, and bioscience-focused examples for researchers and analysts in the life sciences.

---

## 📋 Contents

1. **Environment Setup**  
   - Checking Python interpreter (Anaconda vs. venv)  
   - Managing packages with `pip` / `conda`  
   - IDEs & editors overview (VS Code, PyCharm, Jupyter)

2. **Interactive Workflows**  
   - Launching `python` vs. `ipython` REPL  
   - `%magic` commands and quick experimentation

3. **Core Python Syntax & Semantics**  
   - Whitespace, indentation & commenting  
   - Variables & naming conventions (PEP 8)  
   - Basic data types (`int`, `float`, `str`, `bool`)  
   - Arithmetic, comparison & logical operators  
   - Control flow: `if` / `elif` / `else`, loops, comprehensions  
   - Functions: `def`, parameters, defaults, keyword args  
   - Scope: local vs. global, `global` / `nonlocal`  
   - File I/O with `open()` & context managers

4. **Data Structures & Libraries**  
   - Sequences: lists, tuples, sets, dicts (creation, indexing, methods)  
   - Comprehensions & generator expressions  
   - Modules & packages: `import`, custom modules, `requirements.txt`  
   - NumPy: `ndarray` basics, vectorized operations, distance/adjacency matrices  
   - Pandas: `DataFrame` creation, filtering, grouping, pivoting  
   - Biopython: `Bio.Seq`, `Bio.MutableSeq`, `Bio.SeqIO` usage

5. **Best Practices**  
   - Version control (Git) & virtual environments  
   - Writing readable, reusable functions  
   - Documenting with docstrings & inline comments  
   - The Zen of Python

6. **Supplementary Files**  
   - `patients.fasta` – sample FASTA with 5 mock patient sequences  
   - `log.txt` – example log file for your analysis runs  
   - `requirements.txt` – pinned dependencies for reproducibility  

---

## 🚀 Getting Started

1. **Clone or download** this notebook and accompanying files.  
2. **Create an isolated environment**  
   ```bash
   # Using venv
   python3 -m venv .env
   source .env/bin/activate

   # Or with conda
   conda create -n biosci-py python=3.10
   conda activate biosci-py
   ```
3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Launch Jupyter**  
   ```bash
   jupyter notebook
   # or
   jupyter lab
   ```
5. **Open** `Bioscience_lab.ipynb` and run cells in order.

---

## 🛠️ Usage Tips

- **Generate or update** `patients.fasta` and `log.txt` by running the provided helper cells.  
- **Regenerate** `requirements.txt` to capture your full environment:
  ```bash
  python generate_requirements.py
  ```
- **Consult the codebook** (slide-tagged snippets) to quickly find examples.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests for:

- More bioscience examples (e.g., transcriptomics, structural biology)  
- Additional plotting & visualization templates  
- Improved performance tips for large datasets  

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.
