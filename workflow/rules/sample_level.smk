rule qc:
    input:
        "results/.validation.ok"
    output:
        "results/{sample}/qc/clean_reads.done",
        "results/{sample}/qc/qc_report.txt"
    params:
        platform=lambda wildcards: PLATFORM_BY_SAMPLE[wildcards.sample]
    shell:
        """
        mkdir -p results/{wildcards.sample}/qc
        echo "QC platform={params.platform}" > results/{wildcards.sample}/qc/qc_report.txt
        echo "ok" > {output[0]}
        """


rule assembly:
    input:
        "results/{sample}/qc/clean_reads.done"
    output:
        "results/{sample}/assembly/contigs.fasta"
    params:
        platform=lambda wildcards: PLATFORM_BY_SAMPLE[wildcards.sample]
    shell:
        """
        mkdir -p results/{wildcards.sample}/assembly
        cat > {output} << 'FASTA'
>contig_{wildcards.sample}_1
ATGCATGCATGCATGC
FASTA
        """


rule plasmid_identification:
    input:
        "results/{sample}/assembly/contigs.fasta"
    output:
        "results/{sample}/plasmid_identification/homology_candidates.tsv",
        "results/{sample}/plasmid_identification/ml_candidates.tsv"
    shell:
        """
        mkdir -p results/{wildcards.sample}/plasmid_identification
        printf "contig_id\tscore\ncontig_{wildcards.sample}_1\t0.95\n" > {output[0]}
        printf "contig_id\tprob\ncontig_{wildcards.sample}_1\t0.88\n" > {output[1]}
        """


rule typing:
    input:
        "results/{sample}/plasmid_identification/homology_candidates.tsv"
    output:
        "results/{sample}/typing/typing.tsv"
    shell:
        """
        mkdir -p results/{wildcards.sample}/typing
        printf "sample\tinc_type\tmob_type\n{wildcards.sample}\tIncF\tMOBP\n" > {output}
        """


rule host_prediction:
    input:
        "results/{sample}/plasmid_identification/ml_candidates.tsv"
    output:
        "results/{sample}/host_prediction/host_prediction.tsv"
    params:
        platform=lambda wildcards: PLATFORM_BY_SAMPLE[wildcards.sample]
    shell:
        """
        mkdir -p results/{wildcards.sample}/host_prediction
        if [ "{params.platform}" = "illumina" ]; then
          method="short_read"
        else
          method="long_read_or_methylation"
        fi
        printf "sample\tmethod\thost\n{wildcards.sample}\t%s\tEscherichia_coli\n" "$method" > {output}
        """


rule annotation:
    input:
        typing="results/{sample}/typing/typing.tsv",
        host="results/{sample}/host_prediction/host_prediction.tsv"
    output:
        "results/{sample}/annotation/annotation.tsv",
        "results/{sample}/annotation/annotation.gff"
    shell:
        """
        mkdir -p results/{wildcards.sample}/annotation
        printf "sample\tfeature\tvalue\n{wildcards.sample}\tARG\tblaTEM\n" > {output[0]}
        printf "##gff-version 3\n{wildcards.sample}\tmock\tgene\t1\t100\t.\t+\t.\tID=gene1\n" > {output[1]}
        """
