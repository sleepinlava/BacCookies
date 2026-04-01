# Repository Guidelines

## Project Structure & Module Organization
This repository is a Snakemake scaffold for a metagenomic plasmid pipeline. Use `Snakefile` as the workflow entrypoint. Core rules live in `workflow/rules/` and are split by concern: shared helpers in `common.smk`, sample-level steps in `sample_level.smk`, cohort outputs in `cohort_level.smk`, and reporting in `report.smk`. Runtime configuration lives in `config/`, including `config.template.yaml` for user setup and `module_contracts.yaml` for module interfaces. Keep reusable input files in `templates/`, cluster profiles in `profiles/slurm/` and `profiles/pbs/`, helper scripts in `scripts/`, and planning or delivery docs in `docs/`.

## Build, Test, and Development Commands
Validate the default samplesheet with `python3 scripts/validate_samplesheet.py --samplesheet templates/samplesheet.template.csv`. Regenerate the planning tracker with `python3 scripts/generate_project_tracker.py --output docs/task_board.generated.csv`. Preview the DAG without running jobs via `XDG_CACHE_HOME=$PWD/.cache snakemake -n -p --cores 1`. Run the local scaffold with `XDG_CACHE_HOME=$PWD/.cache snakemake --cores 4`. Submit through a scheduler with `snakemake --profile profiles/slurm` or `snakemake --profile profiles/pbs`.

## Coding Style & Naming Conventions
Python code follows PEP 8 style: 4-space indentation, `snake_case` for functions and variables, and short module docstrings. Snakemake rule files should stay in lower_snake_case and keep shared parsing logic in `workflow/rules/common.smk` rather than duplicating it per rule. Prefer explicit YAML keys and stable output paths such as `results/{sample}/annotation/annotation.tsv`. Preserve the existing mix of English identifiers and Chinese planning text where already present.

## Testing Guidelines
There is no separate unit-test suite yet; validation is workflow-oriented. Before opening a PR, run `python3 scripts/validate_samplesheet.py --samplesheet ...` against any changed template or fixture, then run `snakemake -n -p --cores 1` to confirm the DAG resolves. If you change rule outputs or config handling, test the affected target directly, for example `snakemake --cores 1 results/SAMPLE1/annotation/annotation.tsv`.

## Commit & Pull Request Guidelines
Recent history uses Conventional Commit prefixes such as `feat:` and `chore:`. Follow that pattern and keep subjects imperative, for example `feat: add cohort diversity mock outputs`. PRs should summarize workflow impact, list changed commands or config keys, and note any output-path changes. Include screenshots only for report or documentation rendering changes.
