from openapy.parser import ParsedPythonFile, parse
from tests.conftest import SAMPLE_APIS


def test_parse() -> None:
    ppf = parse(SAMPLE_APIS.joinpath("custom").joinpath("pet_api.py"))
    assert len(ppf.imports) == 0
    assert len(ppf.assigns) == 0
    assert len(ppf.functions) == 0
