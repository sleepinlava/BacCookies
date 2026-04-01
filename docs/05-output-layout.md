# 输出目录规范

```text
results/
  {sample}/
    qc/
      qc_report.html
      clean_reads/
    assembly/
      contigs.fasta
    plasmid_identification/
      homology_candidates.tsv
      ml_candidates.tsv
    binning/
      bins/
    typing/
      typing.tsv
    host_prediction/
      host_prediction.tsv
    annotation/
      annotation.tsv
      annotation.gff

  cohort/
    abundance/
      plasmid_abundance.tsv
      bacteria_abundance.tsv
    differential/
      differential_plasmids.tsv
    diversity/
      alpha_diversity.tsv
      beta_distance_matrix.tsv
      pcoa_coordinates.tsv
    network/
      network_nodes.tsv
      network_edges.tsv
    comparative_genomics/
      exchange_events.tsv

report/
  figures/
    *.svg
  report.html
  report.pdf
```

## 约束
- 模块只可写入自身负责目录，不得覆盖其他模块目录。
- 所有中间结果可选保留，但最终报告仅引用标准目录下产物。
- 报告中所有图默认使用 `.svg`。
