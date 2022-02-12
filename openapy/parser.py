from ast import AnnAssign, Assign, AsyncFunctionDef, FunctionDef, Import, ImportFrom
from ast import parse as ast_parse
from pathlib import Path
from typing import List, Union

TypeFunctions = Union[FunctionDef, AsyncFunctionDef]
TypeImports = Union[ImportFrom, Import]
TypeAssigns = Union[Assign, AnnAssign]


class ParsedPythonFile:
    def __init__(self) -> None:
        self.imports: List[TypeImports] = []
        self.functions: List[TypeFunctions] = []
        self.assigns: List[TypeAssigns] = []


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
