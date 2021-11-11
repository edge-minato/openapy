import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


def print_arg_error(msg: str) -> None:
    print(msg)
    sys.exit(1)


@dataclass
class Args:
    src: Path
    dst: Path
    template: Path
    config: Optional[Path]

    def __post_init__(self) -> None:
        if not self.src.is_dir():
            print_arg_error(f"ERROR: --src {self.src} does not exist")
        if not self.dst.is_dir():
            print(f"Create destination dir {self.dst}")
            self.dst.mkdir()
        if not self.template.is_dir():
            print_arg_error(f"ERROR: --template {self.template} does not exist")
        if self.config is not None and not self.config.is_file():
            print_arg_error(f"ERROR: --config {self.config} does not exist")


def get_args() -> Args:
    parser = argparse.ArgumentParser(description="Additional files generator")
    parser.add_argument("--src", "-s", type=str, required=True, help="Source directory")
    parser.add_argument("--dst", "-d", type=str, required=True, help="Destination directory")
    parser.add_argument("--template", "-t", type=str, required=True, help="Template directory")
    parser.add_argument("--config", "-c", type=str, help="Config file path")
    args = parser.parse_args()
    return Args(args.src, args.dst, args.template, args.config)
