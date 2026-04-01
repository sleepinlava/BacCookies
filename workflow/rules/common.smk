import csv
from pathlib import Path


def load_samples(samplesheet_path):
    with open(samplesheet_path, "r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if not rows:
        raise ValueError("samplesheet is empty")
    return rows


SAMPLESHEET = config.get("samplesheet", "templates/samplesheet.template.csv")
SAMPLE_ROWS = load_samples(SAMPLESHEET)
SAMPLE_IDS = [row["sample_id"] for row in SAMPLE_ROWS]


PLATFORM_BY_SAMPLE = {row["sample_id"]: row["platform"].lower() for row in SAMPLE_ROWS}


def sample_report_files():
    return expand("results/{sample}/annotation/annotation.tsv", sample=SAMPLE_IDS)


rule validate_inputs:
    input:
        samplesheet=SAMPLESHEET
    output:
        "results/.validation.ok"
    shell:
        """
        mkdir -p results
        python3 scripts/validate_samplesheet.py --samplesheet {input.samplesheet}
        date -u +"%Y-%m-%dT%H:%M:%SZ" > {output}
        """
