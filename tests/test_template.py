import pytest

from openapy.template import TEMPLATE, get_template
from tests.conftest import FILE_NOT_FOUND


def test_get_template() -> None:
    template = get_template("README.md")
    assert len(template) > 0
    template = get_template(None)
    assert template == TEMPLATE


def test_get_template_error() -> None:
    with pytest.raises(SystemExit) as e:
        _ = get_template(str(FILE_NOT_FOUND))
    assert e.value.code == 1  # type: ignore
