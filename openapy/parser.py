import ast
from pathlib import Path

from openapy.variables import IdentifiedVariables


def parse(src_file: Path) -> IdentifiedVariables:
    try:
        iv = IdentifiedVariables()
        with src_file.open(mode="r") as f:
            tree = ast.parse(f.read())
        for component in tree.body:
            if isinstance(component, ast.ImportFrom):
                iv.imports.append(component)
            elif isinstance(component, ast.AsyncFunctionDef) or isinstance(component, ast.FunctionDef):
                iv.functions.append(component)
            elif isinstance(component, ast.Assign):
                iv.assigns.append(component)
            else:
                print(f"Unexpected component was found: {type(component)}")
        return iv
    except Exception as e:
        raise e
