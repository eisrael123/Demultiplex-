# Demultiplexing Tool

## Overview
This repository contains a bioinformatics pipeline designed to **demultiplex** FASTQ sequence data. Demultiplexing is the process of sorting a mixed set of sequencing reads (multiplexed) back into their individual samples based on unique barcode sequences (indices). 

This tool specifically handles identifying and binning reads by comparing index reads against a known list of barcodes, handling dual-indexed libraries and accounting for potential index hopping or quality filtering.

## Repository Structure

The project is organized into modular assignments reflecting the development lifecycle of the tool:

* **`Assignment-the-first/`**: 
  * Contains the initial exploratory data analysis.
  * **Part 1**: Quality Score Distribution (Per-nucleotide analysis).
  * **Part 2**: Pseudocode development and algorithmic logic.
* **`Assignment-the-second/`**: 
  * Peer review and refinement of the demultiplexing logic.
* **`Assignment-the-third/`**: 
  * **Source Code**: This directory contains the final Python scripts used for the actual demultiplexing.
* **`TEST-input_FASTQ/`** & **`TEST-output_FASTQ/`**:
  * Input files for validation and expected output files to verify the tool's accuracy.
* **`demultiplex lab notebook.pdf`**:
  * Detailed lab notebook documenting the project's progress, logic, and findings.

## Requirements
To run the scripts in this repository, you will need:

* **Python 3.x**
* **Standard Libraries**: `argparse`, `gzip` (for handling compressed FASTQ files).
* **Bioinformatics Libraries** (Optional but recommended): `matplotlib` (for quality plotting), `numpy`.

## Usage

### 1. Installation
Clone the repository to your local machine:
```bash
git clone [https://github.com/eisrael123/Demultiplex-.git](https://github.com/eisrael123/Demultiplex-.git)
cd Demultiplex-
