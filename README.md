# Metagenomic Plasmid Pipeline (Execution Scaffold)

本仓库用于落地“宏基因组质粒分析 Pipeline 人任务规划（3-4人，两阶段交付）”。
当前版本提供：

- 两阶段（12周）交付路线与人任务拆解
- 模块化接口契约（输入/输出/资源/重试）
- 统一输入模板（samplesheet）与配置模板（config）
- 项目执行辅助脚本（输入校验、任务看板生成）
- Snakemake 工作流骨架（样本级、队列级、报告）
- Slurm/PBS 集群 profile 模板
- 单人开发版本的 Phase 1 细化路线与 Phase 2 周级清单

## 快速开始

1. 填写样本表：`templates/samplesheet.template.csv`
2. 复制配置模板：`config/config.template.yaml`
3. 校验输入：

```bash
python3 scripts/validate_samplesheet.py \
  --samplesheet templates/samplesheet.template.csv
```

4. 生成任务看板：

```bash
python3 scripts/generate_project_tracker.py \
  --output docs/task_board.generated.csv
```

5. Snakemake 预演（不执行任务）：

```bash
source /home/bker/miniconda3/etc/profile.d/conda.sh
conda activate BacCookies
XDG_CACHE_HOME=$PWD/.cache snakemake -n -p --cores 1
```

6. 本地执行（最小骨架）：

```bash
source /home/bker/miniconda3/etc/profile.d/conda.sh
conda activate BacCookies
XDG_CACHE_HOME=$PWD/.cache snakemake --cores 4
```

7. 集群执行（Slurm/PBS）：

```bash
mkdir -p logs/slurm logs/pbs
snakemake --profile profiles/slurm
# 或
snakemake --profile profiles/pbs
```

## 仓库结构

- `docs/`: 项目执行文档（路线、WBS、验收、风险）
- `config/`: 配置模板与模块契约
- `templates/`: 输入模板
- `scripts/`: 执行辅助脚本
- `workflow/`: Snakemake 规则文件
- `profiles/`: Slurm/PBS profile
- `docs/07-phase2-weekly-checklist.md`: Phase 2 周级执行清单（单人开发）

## 说明

该版本聚焦“计划落地可执行化”。当前 Snakemake 规则使用 mock 产物以验证流程编排和交付接口，后续可将规则内部命令替换为真实生信工具调用。
