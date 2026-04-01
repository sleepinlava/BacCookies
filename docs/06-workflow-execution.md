# Snakemake 执行说明

## 1. 环境准备

```bash
source /home/bker/miniconda3/etc/profile.d/conda.sh
conda activate BacCookies
snakemake --version
```

## 2. 输入准备

- 编辑 `templates/samplesheet.template.csv`
- 按需修改 `config/config.yaml`

## 3. 预演与本地运行

```bash
XDG_CACHE_HOME=$PWD/.cache snakemake -n -p --cores 1
XDG_CACHE_HOME=$PWD/.cache snakemake --cores 4
```

## 4. 集群运行

```bash
mkdir -p logs/slurm logs/pbs
XDG_CACHE_HOME=$PWD/.cache snakemake --profile profiles/slurm
# 或
XDG_CACHE_HOME=$PWD/.cache snakemake --profile profiles/pbs
```

## 5. 当前骨架行为

- 已实现模块依赖编排与标准输出路径写入。
- 规则内部当前输出为 mock 数据，用于验证流程调度、输入接口和交付结构。
- 将规则中的 shell/run 替换为真实工具命令即可逐步生产化。
- 已导出当前环境快照：`envs/BacCookies.export.yaml`。
