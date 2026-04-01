#!/usr/bin/env python3
"""Generate a project tracking CSV seeded from the implementation plan."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

HEADERS = ["task_id", "phase", "week", "owner", "task", "deliverable", "status"]

TASKS = [
    ["P1-W1", "Phase1", "1", "Solo Dev", "输入输出与模块契约冻结", "接口基线文档", "TODO"],
    ["P1-W2", "Phase1", "2", "Solo Dev", "流程骨架与调度profile", "可解析DAG与profile模板", "TODO"],
    ["P1-W3", "Phase1", "3", "Solo Dev", "样本级核心链路打通", "样本级标准结果目录", "TODO"],
    ["P1-W4", "Phase1", "4", "Solo Dev", "cohort与报告骨架", "cohort结果与HTML/PDF报告", "TODO"],
    ["P1-W5", "Phase1", "5", "Solo Dev", "稳定性与可配置化", "断点续跑/重试/日志规范", "TODO"],
    ["P1-W6", "Phase1", "6", "Solo Dev", "Phase1封板回归", "MVP发布包", "TODO"],
    ["P2-W7", "Phase2", "7", "Solo Dev", "比较基因组接入", "exchange_events.tsv", "TODO"],
    ["P2-W8", "Phase2", "8", "Solo Dev", "跨样本分箱与分型增强", "跨样本bin与分型结果", "TODO"],
    ["P2-W9", "Phase2", "9", "Solo Dev", "三代甲基化增强宿主预测", "S2场景通过证据", "TODO"],
    ["P2-W10", "Phase2", "10", "Solo Dev", "统计稳健性与性能优化", "参数对照与性能记录", "TODO"],
    ["P2-W11", "Phase2", "11", "Solo Dev", "全链路回归与图形定稿", "S1-S5回归报告", "TODO"],
    ["P2-W12", "Phase2", "12", "Solo Dev", "封板发布", "增强版发布包与归档", "TODO"],
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate project tracking CSV")
    parser.add_argument("--output", required=True, help="Output CSV path")
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(HEADERS)
        writer.writerows(TASKS)

    print(f"Wrote project tracker to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
