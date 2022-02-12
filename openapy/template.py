from enum import Enum

TEMPLATE = """
# coding: utf-8

{IMPORTS}

{DEF} process_{NAME}({ARGS}) -> {RETURN_TYPE}:
    {COMMENT}
    # implement me
    ...
"""


class NOQA(Enum):
    # The space at head is intended
    F401 = " # noqa: F401"
