from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional


class IterSize(Enum):
    FILE = "file"
    FUNC = "func"
    CLASS = "class"


@dataclass
class TargetFile:
    path: Path
    core_name: str


@dataclass
class SourceConfig:
    directory: Path
    prefix: Optional[str]
    suffix: Optional[str]

    def __post_init__(self) -> None:
        if not self.directory.is_dir():
            raise Exception(f"Source directory {self.directory} does not found")

    def get_files(self) -> List[TargetFile]:
        regex = f"{self.prefix}*{self.suffix}"
        files = self.directory.glob(str(regex))
        r = []
        for file in files:
            core_name = file.name.lstrip(self.prefix).rstrip(self.suffix)
            r.append(TargetFile(file, core_name))
        return r


@dataclass
class DestinationConfig:
    directory: Path
    prefix: str
    postfix: str
    exclude_filename: List[str]

    def get_output_file_path(self, name: str) -> Path:
        return self.directory.joinpath(self.prefix + name + self.postfix)


@dataclass
class Config:
    src_config: SourceConfig
    dst_config: DestinationConfig
    template_file: Path
    iteration_size: IterSize
