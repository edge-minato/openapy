from pathlib import Path
from typing import List

from openapy.menu import Args, get_args


def collect_src_files(src_dir: Path) -> List[Path]:
    pyfiles = src_dir.glob("**/*.py")
    return [f for f in pyfiles if f.is_file()]


def main() -> None:
    args: Args = get_args()
    src_files = collect_src_files(args.src)
    print(src_files)
