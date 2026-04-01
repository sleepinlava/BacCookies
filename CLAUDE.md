# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands
```bash
# Validate input samplesheet
snakemake --cores 1 validate_inputs

# Dry run to preview all tasks
snakemake --dry-run

# Run full pipeline locally
snakemake --cores 16 --config run_mode=local

# Run full pipeline on Slurm cluster
snakemake --profile slurm

# Run specific module/rule (example: run assembly for a single sample)
snakemake --cores 8 results/SAMPLE1/assembly/contigs.fasta

# Generate workflow DAG visualization
snakemake --dag | dot -Tsvg > workflow_dag.svg
```

## High-Level Architecture
This is a Snakemake-based metagenomic plasmid analysis pipeline designed for processing both short-read (Illumina) and long-read (Nanopore/PacBio) sequencing data.

### Core Layer Structure
1. **Configuration Layer (`config/`)**
   - `config.yaml`: User-facing runtime configuration (samplesheet path, resource allocation, cluster settings)
   - `config.template.yaml`: Full configuration reference with all optional parameters and tool selection options
   - `module_contracts.yaml`: Central orchestration schema defining all analysis modules' input/output contracts, resource profiles, and retry policies - all rules must conform to this schema

2. **Rule Layer (`workflow/rules/`)**
   - `common.smk`: Global shared utilities, samplesheet parsing logic, and pre-flight validation rules. All other rule files import this first.
   - Per-module rule files follow the naming pattern `{module_name}.smk`, strictly adhering to the input/output definitions in `module_contracts.yaml`

3. **Execution Layer (`scripts/`)**
   - Custom Python/Shell scripts called by Snakemake rules for analysis logic not covered by standard bioinformatics tools

### Core Pipeline Flow
Samplesheet → Quality Control → Assembly → Dual plasmid identification (homology search + machine learning) → Single/cross-sample binning → Typing + Host prediction → Functional annotation → Comparative genomics / cohort statistics / interaction network → Final report

The pipeline supports two parallel plasmid identification paths and two binning modes for different study designs. All module dependencies are automatically resolved based on the contracts defined in `module_contracts.yaml`.
