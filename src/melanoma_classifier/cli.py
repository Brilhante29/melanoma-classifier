from __future__ import annotations

import argparse
from pathlib import Path

from melanoma_classifier.benchmark import run_benchmark


def main() -> None:
    parser = argparse.ArgumentParser(prog="melanoma-classifier")
    commands = parser.add_subparsers(dest="command", required=True)
    benchmark = commands.add_parser("benchmark")
    benchmark.add_argument("--dataset", type=Path, default=Path("data/dermamnist.npz"))
    benchmark.add_argument("--output", type=Path, default=Path("benchmarks/results/baseline.json"))
    benchmark.add_argument("--seed", type=int, default=42)
    benchmark.add_argument("--minimum-validation-sensitivity", type=float, default=0.8)
    args = parser.parse_args()
    if args.command == "benchmark":
        run_benchmark(
            dataset_path=args.dataset,
            output_path=args.output,
            seed=args.seed,
            minimum_validation_sensitivity=args.minimum_validation_sensitivity,
        )


if __name__ == "__main__":
    main()
