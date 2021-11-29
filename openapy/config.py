import sys
import traceback
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional

from yaml import safe_load


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

    def make_dst_dir(self) -> None:
        if not self.directory.is_dir():
            self.directory.mkdir()

    def get_output_file_path(self, name: str) -> Path:
        return self.directory.joinpath(self.prefix + name + self.postfix)


@dataclass
class TemplateFile:
    path: Path

    def __post_init__(self) -> None:
        if not self.path.is_file():
            raise Exception(f"Template file {self.path} does not exist.")


@dataclass
class Config:
    name: str
    src_config: SourceConfig
    dst_config: DestinationConfig
    template_file: TemplateFile
    iteration_size: IterSize


def get_SourceConfig(config: dict) -> SourceConfig:
    directory = Path(config["directory"])
    prefix = config["prefix"]
    suffix = config["suffix"]
    return SourceConfig(directory, prefix, suffix)


def get_DestinationConfig(config: dict) -> DestinationConfig:
    directory = Path(config["directory"])
    prefix = config["prefix"]
    suffix = config["suffix"]
    return DestinationConfig(directory, prefix, suffix)


def get_Config(config_path: Path) -> List[Config]:
    try:
        with config_path.open(mode="r") as f:
            raw_config_list = safe_load(f)
        config_list = []
        for i, raw_config in enumerate(raw_config_list):
            name = raw_config["name"]
            print(f"Config #{i}: {name} ... ", end="")
            sc = get_SourceConfig(raw_config["src"])
            dc = get_DestinationConfig(raw_config["dst"])
            tf = TemplateFile(Path(raw_config["template"]))
            iter_size = IterSize(raw_config["iter"])
            c = Config(name=name, src_config=sc, dst_config=dc, template_file=tf, iteration_size=iter_size)
            config_list.append(c)
            print("Loaded.")
        return config_list
    except Exception:
        print("ERROR: Failed to load config file.")
        traceback.print_exc()
        sys.exit(1)
