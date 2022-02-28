from typing import Optional

import pytest
from pytest_mock import MockFixture

from openapy.args import get_args


class MockArgParser:
    def __init__(self, command: str, src: Optional[str] = "path/to/src", version: bool = False) -> None:
        self.command = command
        self.src = src
        self.all = True
        self.template = "path/to/template"
        self.version = version


def test_args_generate(mocker: MockFixture) -> None:
    mocker.patch("argparse.ArgumentParser.parse_args", return_value=MockArgParser(command="generate"))
    args = get_args()
    assert args.src == "path/to/src"
    assert args.all is True
    assert args.template == "path/to/template"
    assert args.version is False


def test_args_version(mocker: MockFixture) -> None:
    mocker.patch("argparse.ArgumentParser.parse_args", return_value=MockArgParser(command="openapy", version=True))
    with pytest.raises(SystemExit) as e:
        _ = get_args()
    assert e.value.code == 0  # type: ignore


def test_args_generate_without_src(mocker: MockFixture) -> None:
    mocker.patch("argparse.ArgumentParser.parse_args", return_value=MockArgParser(command="generate", src=None))
    with pytest.raises(SystemExit) as e:
        _ = get_args()
    assert e.value.code == 1  # type: ignore
