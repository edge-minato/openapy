from ast import Assign, AsyncFunctionDef, FunctionDef, ImportFrom
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Union

# from openapy.parser import parse

Function = Union[FunctionDef, AsyncFunctionDef]


@dataclass
class IdentifiedVariables:
    imports: List[ImportFrom] = field(default_factory=lambda: [])
    functions: List[Function] = field(default_factory=lambda: [])
    assigns: List[Assign] = field(default_factory=lambda: [])


@dataclass
class TargetFile:
    src_file_path: Path
    dst_file_path: Path
    core_name: str

    # def __post_init__(self) -> None:
    #    self.id_variables: IdentifiedVariables = parse(self.src_file_path)


@dataclass
class DestinationFile:
    file_name: str
