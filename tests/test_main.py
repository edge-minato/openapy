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
