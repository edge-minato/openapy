from openapy.parser import parse
from tests.conftest import SAMPLE_APIS


def test_parse() -> None:
    ppf = parse(SAMPLE_APIS.joinpath("custom").joinpath("pet_api.py"))
    assert len(ppf.imports) == 7
    assert len(ppf.assigns) == 2
    assert len(ppf.functions) == 8
