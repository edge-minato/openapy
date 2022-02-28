import pytest
from pytest_mock import MockFixture

from openapy.io import get_my_resource, read_file, write_file
from tests.conftest import REPO_DIR, TEMP_DIR


def test_read() -> None:
    content = read_file(REPO_DIR.joinpath("pyproject.toml"))
    assert "[tool.poetry]" in content
    assert "openapy" in content


def test_write() -> None:
    content = "aaabbbccc"
    file = TEMP_DIR.joinpath("test_write.txt")
    write_file(file, content)
    with file.open(mode="r") as f:
        read_content = f.read()
    assert content == read_content


def test_resource() -> None:
    with pytest.raises(Exception):
        _ = get_my_resource("RESOURCE_ABCDE")


def test_resource_not_found(mocker: MockFixture) -> None:
    mocker.patch("pkgutil.get_data", return_value=None)
    with pytest.raises(Exception):
        _ = get_my_resource("RESOURCE_ABCDE")
