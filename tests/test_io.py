from openapy.io import read_file, write_file
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
