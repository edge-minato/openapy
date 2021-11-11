from pathlib import Path

import pytest

from openapy.menu import Args

HERE = Path(__file__).absolute().parent
SRC = HERE.joinpath("server")
SRC_DOES_NOT_EXIST = HERE.joinpath("ABCDEFG")
DST = HERE.joinpath("dst")
TEMPLATE = HERE.joinpath("mustache")
CONFIG = None
CONFIG_DOES_NOT_EXIST = HERE.joinpath("ABCDEFG.json")


def test_args_fine() -> None:
    Args(SRC, DST, TEMPLATE, CONFIG)  # without any error


def test_args_src_not_found() -> None:
    with pytest.raises(SystemExit) as e:
        Args(SRC_DOES_NOT_EXIST, DST, TEMPLATE, CONFIG)
        assert e.value.code == 1  # type: ignore


def test_args_config_not_found() -> None:
    with pytest.raises(SystemExit) as e:
        Args(SRC, DST, TEMPLATE, CONFIG_DOES_NOT_EXIST)
        assert e.value.code == 1  # type: ignore
