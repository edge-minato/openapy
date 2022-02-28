import pytest
from pytest_mock import MockFixture

from openapy.main import main


class MockArg:
    def __init__(self, command: str) -> None:
        self.command = command


def test_main_generate(mocker: MockFixture) -> None:
    mocker.patch("openapy.main.get_args", return_value=MockArg("generate"))
    mocker.patch("openapy.main.generate", side_effect=Exception("generate was called"))
    with pytest.raises(Exception) as e:
        main()
    assert str(e.value) == "generate was called"  # type: ignore


def test_main_example(mocker: MockFixture) -> None:
    # example
    mocker.patch("openapy.main.get_args", return_value=MockArg("example"))
    mocker.patch("openapy.main.show_example", side_effect=Exception("example was called"))
    with pytest.raises(Exception) as e:
        main()
    assert str(e.value) == "example was called"  # type: ignore
    # example.template
    mocker.patch("openapy.main.get_args", return_value=MockArg("example.template"))
    mocker.patch("openapy.main.show_example", side_effect=Exception("example was called"))
    with pytest.raises(Exception) as e:
        main()
    assert str(e.value) == "example was called"  # type: ignore


def test_main_version(mocker: MockFixture) -> None:
    mocker.patch("openapy.main.get_args", return_value=MockArg("version"))
    mocker.patch("openapy.main.show_version", side_effect=Exception("version was called"))
    with pytest.raises(Exception) as e:
        main()
    assert str(e.value) == "version was called"  # type: ignore


def test_main_exception(mocker: MockFixture) -> None:
    mocker.patch("openapy.main.get_args", return_value=MockArg("others"))
    with pytest.raises(Exception) as e:
        main()
