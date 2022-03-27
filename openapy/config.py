import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class SourceConfig:
    directory: Path
    ignore: List[str]

    def __post_init__(self) -> None:
        if not self.directory.is_dir():
            print(f"ERROR: Source directory {self.directory} does not found")
            sys.exit(1)

    def get_files(self) -> List[Path]:
        files = self.directory.glob("*.py")
        ignore_files = [self.directory.joinpath(ignore) for ignore in self.ignore]
        return [file for file in files if file not in ignore_files]


@dataclass
class DestinationConfig:
    directory: Path

    def __post_init__(self) -> None:
        self.directory.mkdir(exist_ok=True)

    def get_output_file_path(self, function_name: str) -> Path:
        return self.directory.joinpath(f"{function_name}.py")

    def get_files(self) -> List[Path]:
        files = self.directory.glob("*.py")
        return [file for file in files if "__init__" not in file.name]


class Config:
    def __init__(self, src: Path, generate_all: bool):
        self.source_config = SourceConfig(src, [])
        self.destination_config = DestinationConfig(src.parent.joinpath("processor"))
        self.generate_all = generate_all
