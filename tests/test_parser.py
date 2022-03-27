import pytest

from openapy.parser import parse
from tests.conftest import EXAMPLE_APIS_DIR, FILE_NOT_FOUND


def test_parse() -> None:
    ppf = parse(EXAMPLE_APIS_DIR("custom").joinpath("pet_api.py"))
    assert len(ppf.imports) == 6
    assert len(ppf.assigns) == 10
    assert len(ppf.functions) == 8


def test_parse_error() -> None:
    with pytest.raises(FileNotFoundError):
        _ = parse(FILE_NOT_FOUND)
