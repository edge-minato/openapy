import pytest

from openapy.commands.example import show_example


def test_show_resource() -> None:
    pass


def test_show_docker() -> None:
    show_example(kind="docker")


def test_show_template() -> None:
    show_example(kind="docker")


def test_show_mustache() -> None:
    show_example(kind="docker")


def test_show_exception() -> None:
    with pytest.raises(Exception):
        show_example(kind="ABCDEFG")
