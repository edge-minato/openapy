from ast import parse

from openapy.render import FilePerFunction, Function

sample_function = """
def func_name(arg1: str, arg2: int) -> str:
    \"\"\"comment1\"\"\"
    \"\"\"comment2\"\"\"
    body1 = "body1"
    body2 = 1 + 1
    return "this is return"
"""

parsed_func = parse(sample_function).body[0]

template = """
# coding: utf-8

{IMPORTS}

{ASSIGNS}

{DEF} {NAME}({ARGS}) -> {RETURN_TYPE}:
    {COMMENT}
    {BODY}
    ...
"""

expect = """
# coding: utf-8

import sys

assign = 1 + 1

def func_name(arg1: str, arg2: int) -> str:
    \"\"\"comment1\"\"\"
    \"\"\"comment2\"\"\"
    body1 = 'body1'
    body2 = 1 + 1
    ...
"""


def test_function() -> None:
    func = Function(parsed_func)  # type: ignore
    assert func.definition == "def"
    assert func.name == "func_name"
    assert func.return_type == "str"
    assert func.args == "arg1: str, arg2: int"
    assert func.comments == '"""comment1"""\n    """comment2"""'
    assert func.body == "body1 = 'body1'\n    body2 = 1 + 1"
    assert func.returns == "return 'this is return'"


def test_file_per_function() -> None:
    fpf = FilePerFunction("import sys", "assign = 1 + 1", parsed_func)  # type: ignore
    assert expect == fpf.render(template)
