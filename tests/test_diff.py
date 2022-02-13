from ast import parse

from openapy.diff import ComparableFunction, compare_as_function, get_functions

func_a_all = parse(
    """
def func1(foo: str, bar: int) -> str:
    return "ok"
"""
).body[0]

func_b_with_assign = parse(
    """
def func1(foo: str, bar: int) -> str:
    r = "ok"
    return r
"""
).body[0]

func_c_without_return_type = parse(
    """
def func1(foo: str, bar: int):
    return "ok"
"""
).body[0]

func_d_without_args = parse(
    """
def func1() -> str:
    return "ok"
"""
).body[0]


func_e_without_args_type = parse(
    """
def func1(foo, bar) -> str:
    return "ok"
"""
).body[0]

func_f_without_returns = parse(
    """
def func1(foo: str, bar: int) -> str:
    ...
"""
).body[0]


def test_comparable_function() -> None:
    c1 = ComparableFunction(func_a_all)  # type: ignore
    c2 = ComparableFunction(func_b_with_assign)  # type: ignore
    c3 = ComparableFunction(func_c_without_return_type)  # type: ignore
    c4 = ComparableFunction(func_d_without_args)  # type: ignore
    c5 = ComparableFunction(func_e_without_args_type)  # type: ignore
    c6 = ComparableFunction(func_f_without_returns)  # type: ignore

    assert c1 == c1
    assert c1 == c2 == c6
    assert c3 == c3
    assert c4 == c4
    assert c5 == c5
    assert not c1 == c3
    assert not c1 == "string"
    assert not c1 == 123
    assert c1 is not None
    assert c1.definition == "def"
    assert c1.name == "func1"
    assert c1.args == "foo: str, bar: int"
    assert c1.return_type == "str"


multi_functions = """
def func1(foo: str, bar: int) -> str:
    return "ok"
def func2(foo: str, bar: int) -> str:
    return "ok"
def func3(foo: str, bar: int) -> str:
    return "ok"
"""


multi_functions_with_assign = """
def func1(foo: str, bar: int) -> str:
    return "ok"
a = 1 + 1
def func2(foo: str, bar: int) -> str:
    return "ok"
b = 2 + 2
def func3(foo: str, bar: int) -> str:
    return "ok"
"""


def test_get_functions() -> None:
    func_list = get_functions(multi_functions)  # type: ignore
    assert len(func_list) == 3
    func_list = get_functions(multi_functions_with_assign)  # type: ignore
    assert len(func_list) == 3


old = """
import sys
from os.path import join

a = 1 + 1

def part_of_process():
    pass

def process(foo:str, bar:int) -> str:
    r = "ok"
    return r
"""

new_same = """
import sys
from os.path import join

a = 1 + 1
b = 2 + 2

def process(foo:str, bar:int) -> str:
    ...
"""

new_different_args = """
def process(foo:str, bar:int, foobar: str) -> str:
    ...
"""

new_different_return_type = """
def process(foo:str, bar:int):
    ...
"""

new_different_name = """
def process_get_user(foo:str, bar:int) -> str:
    ...
"""


def test_compare_as_function() -> None:
    assert compare_as_function(old, old)
    assert compare_as_function(old, new_same)
    assert not compare_as_function(old, new_different_args)
    assert not compare_as_function(old, new_different_name)
    assert not compare_as_function(old, new_different_return_type)
