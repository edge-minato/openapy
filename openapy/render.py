import ast
from ast import AsyncFunctionDef, Expr, Return, unparse  # type: ignore
from typing import List

from openapy.parser import TypeAssigns, TypeFunctions, TypeImports
from openapy.template import NOQA


class FilePerFunction:
    def __init__(
        self,
        imports: List[TypeImports],
        assigns: List[TypeAssigns],
        function: TypeFunctions,
        import_suffix: str = NOQA.F401.value,
    ) -> None:
        self.imports: str = Import(imports, import_suffix).unparsed
        self.assigns: str = Assign(assigns).unparsed
        func: Function = Function(function)
        self.definition = func.definition
        self.name = func.name
        self.return_type = func.return_type
        self.args = func.args
        self.comments = func.comments
        self.body = func.body
        self.returns = func.returns

    def render(self, template: str) -> str:
        return template.format(
            IMPORTS=self.imports,
            ASSIGNS=self.assigns,
            DEF=self.definition,
            NAME=self.name,
            ARGS=self.args,
            RETURN_TYPE=self.return_type,
            COMMENT=self.comments,
            BODY=self.body,
            RETURN=self.returns,
        )


class Assign:
    def __init__(self, assigns: List[TypeAssigns]) -> None:
        self.unparsed = "\n".join([unparse(a) for a in assigns])


class Import:
    def __init__(self, imports: List[TypeImports], suffix: str) -> None:
        self.unparsed = "\n".join([f"{unparse(i)}{suffix}" for i in imports])


class Function:
    def __init__(self, function: TypeFunctions) -> None:
        function.decorator_list = []
        function.args.defaults = []
        self.definition = "async def" if isinstance(function, AsyncFunctionDef) else "def"
        self.name = function.name
        self.return_type = unparse(function.returns) if function.returns is not None else ""
        self.args = unparse(function.args) if function.args is not None else ""
        self.comments = "\n    ".join([f'"""{c.value.value}"""' for c in function.body if isinstance(c, Expr)])  # type: ignore # noqa: E501
        self.body = "\n    ".join(
            [unparse(body) for body in function.body if (not isinstance(body, Expr) and not isinstance(body, Return))]
        )
        self.returns = "\n".join([unparse(ret) for ret in function.body if isinstance(ret, Return)])

        for body in function.body:
            if not isinstance(body, (ast.Assign, Expr, Return)):
                print(body)
