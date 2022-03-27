from ast import unparse  # type: ignore
from ast import AnnAssign, Assign, AsyncFunctionDef, FunctionDef, Import, ImportFrom  # type: ignore
from ast import parse as ast_parse
from pathlib import Path
from typing import List, Union

TypeFunctions = Union[FunctionDef, AsyncFunctionDef]
TypeImports = Union[ImportFrom, Import]
TypeAssigns = Union[Assign, AnnAssign]


def has_processor(names: List) -> bool:
    for n in names:
        if n.name == "processor":
            return True
    return False


class ParsedPythonFile:
    def __init__(self) -> None:
        self.imports: List[TypeImports] = []
        self.functions: List[TypeFunctions] = []
        self.assigns: List[TypeAssigns] = []

    def avoid_circular_import(self) -> None:
        valid_imports = []
        for i in self.imports:
            if isinstance(i, ImportFrom) and i.module == "processor":
                print(f"  Skip '{unparse(i)}' to avoid circular import.")
                continue
            if has_processor(i.names):
                print(f"  Skip '{unparse(i)}' to avoid circular import.")
                continue
            valid_imports.append(i)
        self.imports = valid_imports


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
        ppf.avoid_circular_import()
        return ppf
    except Exception as e:
        raise e
