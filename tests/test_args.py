from typing import Optional

import pytest
from pytest_mock import MockFixture

from openapy.args import get_args


class MockArgParser:
    def __init__(self, src: Optional[str] = "path/to/src", version: bool = False) -> None:
        self.src = src
        self.all = True
        self.template = "path/to/template"
        self.version = version


def test_args_default(mocker: MockFixture) -> None:
    mocker.patch("argparse.ArgumentParser.parse_args", return_value=MockArgParser())
    args = get_args()
    assert args.src == "path/to/src"
    assert args.all is True
    assert args.template == "path/to/template"
    assert args.version is False


def test_args_version(mocker: MockFixture) -> None:
    mocker.patch("argparse.ArgumentParser.parse_args", return_value=MockArgParser(version=True))
    with pytest.raises(SystemExit) as e:
        _ = get_args()
        assert e.value.code == 1  # type: ignore


def test_args_without_src(mocker: MockFixture) -> None:
    mocker.patch("argparse.ArgumentParser.parse_args", return_value=MockArgParser(src=None))
    with pytest.raises(SystemExit) as e:
        _ = get_args()
        assert e.value.code == 1  # type: ignore
