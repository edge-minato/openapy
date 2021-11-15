import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


def print_arg_error(msg: str) -> None:
    print(msg)
    sys.exit(1)


@dataclass
class Args:
    config: Path

    def __post_init__(self) -> None:
        if not self.config.is_file():
            print_arg_error(f"ERROR: --config {self.config} does not exist")


def get_args() -> Args:
    parser = argparse.ArgumentParser(description="Additional files generator")
    parser.add_argument("--config", "-c", type=str, required=True, help="Config file path")
    args = parser.parse_args()
    return Args(args.config)
