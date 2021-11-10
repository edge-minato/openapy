from ast import unparse  # type: ignore
from ast import AnnAssign, Assign, AsyncFunctionDef, FunctionDef, Import, ImportFrom
from ast import parse as ast_parse
from pathlib import Path
from typing import List, Union

Functions = Union[FunctionDef, AsyncFunctionDef]
Imports = Union[ImportFrom, Import]
Assigns = Union[Assign, AnnAssign]


class ParsedPythonFile:
    def __init__(self) -> None:
        self.imports: List[Imports] = []
        self.functions: List[Functions] = []
        self.assigns: List[Assigns] = []

    def get_imports_str(self) -> str:
        return "\n".join([unparse(i) for i in self.imports])

    def get_assigns_str(self) -> str:
        return "\n".join([unparse(a) for a in self.assigns])


def parse(src_file: Path) -> ParsedPythonFile:
    try:
        ppf = ParsedPythonFile()
        with src_file.open(mode="r") as f:
            tree = ast_parse(f.read())
        for component in tree.body:
            if isinstance(component, (ImportFrom, Import)):
                ppf.imports.append(component)
            elif isinstance(component, (AsyncFunctionDef, FunctionDef)):
                ppf.functions.append(component)
            elif isinstance(component, (Assign, AnnAssign)):
                ppf.assigns.append(component)
            else:
                print(f"Unexpected component was found: {type(component)}")
        return ppf
    except Exception as e:
        raise e
