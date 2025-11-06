# Greek Text Preprocessing Scripts

Python scripts for preprocessing Greek texts extracted from manuscripts via HTR, prepared for stemmatic analysis.

## Overview

This repository contains Python scripts developed to clean and preprocess text extracted from Greek manuscripts. The scripts are part of a workflow aimed at enabling clustering and analysis of manuscripts, including:

- Removing punctuation and special characters
- Converting all letters to lowercase
- Joining multiple lines into a single continuous string
- Calculating Character Error Rate (CER) between reference and hypothesis texts
- Generating synthetic datasets with controlled CER for testing clustering robustness

These scripts are intended for research purposes and can be adapted for similar text preprocessing tasks in Greek or other languages.

## Scripts

### 1. Convert Uppercase to Lowercase
- **Purpose:** Convert all uppercase letters in a manuscript file to lowercase.

### 2. Join Multiple Lines into One String
- **Purpose:** Concatenate all lines of a manuscript into a single string.

### 3. Remove Punctuation
- **Purpose:** Remove punctuation characters from a manuscript.

### 4. Calculate CER for a File
- **Purpose:** Compute the Character Error Rate (CER) between a reference and a hypothesis text.
- **Dependency:** Python package `python-Levenshtein`

### 5. Generate Synthetic CER Datasets
- **Purpose:** Introduce controlled errors into a manuscript text to create datasets with specific CER levels.
- **Use Case:** Evaluate the maximum CER allowing successful manuscript clustering
- **Dependency:** Python package `python-Levenshtein`

## Dependencies

- Python 3.x
- `python-Levenshtein` (for CER calculations)

Install dependencies with:

```bash
pip install python-Levenshtein
```

## Citation / Contact
Please reference this repository when using these scripts in research projects.  

Example citation:
Perdiki, Elpida, "Greek text preprocessing scripts", GitHub repository, https://github.com/yourusername/greek-text-preprocessing-scripts, 2025.
