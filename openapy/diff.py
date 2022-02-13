from ast import AsyncFunctionDef, FunctionDef, parse, unparse  # type: ignore
from typing import Any, List

from openapy.parser import TypeFunctions


class ComparableFunction:
    def __init__(self, function: TypeFunctions) -> None:
        self.definition = "async def" if isinstance(function, AsyncFunctionDef) else "def"
        self.name = function.name
        self.return_type = unparse(function.returns) if function.returns is not None else ""
        self.args = unparse(function.args) if function.args is not None else ""

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ComparableFunction):
            return False
        if (
            self.definition == other.definition
            and self.name == other.name  # noqa: W503
            and self.args == other.args  # noqa: W503
            and self.return_type == other.return_type  # noqa: W503
        ):
            return True
        return False


def get_functions(source: str) -> List[TypeFunctions]:
    return [m for m in parse(source).body if isinstance(m, (FunctionDef, AsyncFunctionDef))]


def compare_as_function(old: str, new: str) -> bool:
    old_functions = get_functions(old)
    new_function = get_functions(new)[0]
    for old_function in old_functions:
        if old_function.name == new_function.name:
            return ComparableFunction(old_function) == ComparableFunction(new_function)
    return False
