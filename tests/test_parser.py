import pytest

from openapy.parser import parse
from tests.conftest import FILE_NOT_FOUND, SAMPLE_APIS


def test_parse() -> None:
    ppf = parse(SAMPLE_APIS.joinpath("custom").joinpath("pet_api.py"))
    assert len(ppf.imports) == 7
    assert len(ppf.assigns) == 10
    assert len(ppf.functions) == 8


def test_parse_error() -> None:
    with pytest.raises(FileNotFoundError) as e:
        _ = parse(FILE_NOT_FOUND)
        assert e.value.code == 1  # type: ignore
