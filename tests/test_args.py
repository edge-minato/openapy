import pytest

from openapy.args import Args
from tests.conftest import CONFIG_DIR, FILE_NOT_FOUND


def test_args_normal() -> None:
    Args(CONFIG_DIR.joinpath("example.yml"))


def test_args_error() -> None:
    with pytest.raises(SystemExit) as e:
        Args(FILE_NOT_FOUND)
        assert e.value.code == 1  # type: ignore
