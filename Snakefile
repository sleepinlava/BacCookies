configfile: "config/config.yaml"

include: "workflow/rules/common.smk"
include: "workflow/rules/sample_level.smk"
include: "workflow/rules/cohort_level.smk"
include: "workflow/rules/report.smk"

rule all:
    input:
        sample_report_files(),
        "results/cohort/abundance/plasmid_abundance.tsv",
        "results/cohort/differential/differential_plasmids.tsv",
        "results/cohort/diversity/alpha_diversity.tsv",
        "results/cohort/diversity/beta_distance_matrix.tsv",
        "results/cohort/network/network_edges.tsv",
        "report/report.html",
        "report/report.pdf"
