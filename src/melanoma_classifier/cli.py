from __future__ import annotations

import argparse
import sys

from melanoma_classifier.fixture import generate_synthetic_lesion


def demo() -> None:
    print("melanoma-classifier demo")
    print("=" * 40)
    img, label = generate_synthetic_lesion(seed=42)
    label_str = "melanoma (malignant)" if label == 1 else "benign"
    print(f"Generated synthetic lesion: {img.size}, label={label_str}")
    print("Feature extraction would classify this image.")
    print("Use 'benchmark' subcommand for full evaluation.")


def run_benchmark(args: argparse.Namespace) -> None:
    from melanoma_classifier.benchmark import run_benchmark

    run_benchmark(
        n_samples=args.n_samples,
        output=args.output,
        random_state=args.seed,
    )


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="melanoma-classifier",
        description="Skin lesion classification benchmark",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    demo_parser = sub.add_parser("demo", help="Run a quick demo")
    demo_parser.set_defaults(func=lambda _: demo())

    bench = sub.add_parser("benchmark", help="Run benchmark")
    bench.add_argument(
        "--n-samples",
        type=int,
        default=500,
        help="Number of synthetic samples (default: 500)",
    )
    bench.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output JSON path",
    )
    bench.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed (default: 42)",
    )
    bench.set_defaults(func=run_benchmark)

    args = parser.parse_args(argv if argv is not None else sys.argv[1:])
    args.func(args)
