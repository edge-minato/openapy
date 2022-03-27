import pytest
from pytest_mock import MockFixture

from openapy.parser import has_processor, parse
from tests.conftest import EXAMPLE_APIS_DIR, FILE_NOT_FOUND


def test_parse() -> None:
    ppf = parse(EXAMPLE_APIS_DIR("custom").joinpath("pet_api.py"))
    assert len(ppf.imports) == 6
    assert len(ppf.assigns) == 10
    assert len(ppf.functions) == 8


def test_parse_error() -> None:
    with pytest.raises(FileNotFoundError):
        _ = parse(FILE_NOT_FOUND)


def test_has_processor(mocker: MockFixture) -> None:
    obj_1 = mocker.Mock()
    obj_2 = mocker.Mock()
    obj_1.name = "abc"
    obj_2.name = "def"
    assert not has_processor([obj_1, obj_2])
    obj_2.name = "processor"
    assert has_processor([obj_1, obj_2])
