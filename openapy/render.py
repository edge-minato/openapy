from ast import Assign, AsyncFunctionDef, Expr, FunctionDef, Return, unparse  # type: ignore
from typing import Union

FunctionType = Union[AsyncFunctionDef, FunctionDef]


class FilePerFunction:
    def __init__(self, imports: str, assigns: str, function: FunctionType) -> None:
        self.imports: str = imports
        self.assigns: str = assigns
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


class Function:
    def __init__(self, function: FunctionType) -> None:
        function.decorator_list = []
        function.args.defaults = []
        self.definition = "async def" if isinstance(function, AsyncFunctionDef) else "def"
        self.name = function.name
        self.return_type = unparse(function.returns)
        self.args = unparse(function.args)
        self.comments = "\n    ".join([f'"""{c.value.value}"""' for c in function.body if isinstance(c, Expr)])  # type: ignore # noqa: E501
        self.body = "\n    ".join(
            [unparse(body) for body in function.body if (not isinstance(body, Expr) and not isinstance(body, Return))]
        )
        self.returns = "\n".join([unparse(ret) for ret in function.body if isinstance(ret, Return)])

        for body in function.body:
            if not isinstance(body, (Assign, Expr, Return)):
                print(body)
