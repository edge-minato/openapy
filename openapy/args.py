import argparse
import sys

from openapy.io import exit_with_error
from openapy.template import GITHUB, LOGO, VERSION


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Additional files generator for openapi")
    parser.add_argument("--src", "-s", type=str, default=None, help="source dir path")
    parser.add_argument("--template", "-t", type=str, default=None, help="file path of the processor template")
    parser.add_argument("--all", "-a", action="store_true", help="whether overwrite all files or not")
    parser.add_argument("--version", "-v", action="store_true", help="show version")
    args = parser.parse_args()
    if args.version:
        show_version()
        sys.exit(0)
    if args.src is None:
        exit_with_error("TIPS: --src, -s argument is required")
    return args


def show_version() -> None:
    print(LOGO)
    print(f"{GITHUB}     version: {VERSION}")
