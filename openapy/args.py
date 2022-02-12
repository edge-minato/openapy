import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Additional files generator for openapi")
    parser.add_argument("--src", "-s", type=str, required=True, help="Source dir path")
    parser.add_argument(
        "--template", "-t", type=str, required=False, default=None, help="File path of the processor template"
    )
    parser.add_argument("--tag", type=str, required=True, help="Tag")
    parser.add_argument("--all", "-a", action="store_true", help="Overwrite all files")
    return parser.parse_args()
