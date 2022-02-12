from ast import parse

from openapy.render import Assign, FilePerFunction, Function, Import

example_imports = """\
import sys
from sys import exit
from os.path import join\
"""

example_assigns = """\
aaa = 'bbb'
ccc = 1 + 1
ddd = aaa\
"""

example_function = """
def func_name(arg1: str, arg2: int) -> str:
    \"\"\"comment1\"\"\"
    \"\"\"comment2\"\"\"
    body1 = "body1"
    body2 = 1 + 1
    return "this is return"
"""


parsed_imports = parse(example_imports).body
parsed_assigns = parse(example_assigns).body
parsed_func = parse(example_function).body[0]

template = """
# coding: utf-8

{IMPORTS}

{ASSIGNS}

{DEF} {NAME}({ARGS}) -> {RETURN_TYPE}:
    {COMMENT}
    {BODY}
    ...
"""

expect_rendered = """
# coding: utf-8

import sys
from sys import exit
from os.path import join

aaa = 'bbb'
ccc = 1 + 1
ddd = aaa

def func_name(arg1: str, arg2: int) -> str:
    \"\"\"comment1\"\"\"
    \"\"\"comment2\"\"\"
    body1 = 'body1'
    body2 = 1 + 1
    ...
"""


def test_import() -> None:
    imports = Import(parsed_imports, "")  # type: ignore
    assert imports.unparsed == example_imports


def test_assign() -> None:
    assign = Assign(parsed_assigns)  # type: ignore
    assert assign.unparsed == example_assigns


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
    fpf = FilePerFunction(parsed_imports, parsed_assigns, parsed_func, "")  # type: ignore
    assert expect_rendered == fpf.render(template)
