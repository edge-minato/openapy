import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Additional files generator for openapi")
    parser.add_argument("--src", "-s", type=str, required=True, help="Srouce dir path")
    parser.add_argument("--tag", "-t", type=str, required=True, help="Tag")
    parser.add_argument("--all", "-a", action="store_true", help="Overwrite all files")
    return parser.parse_args()
