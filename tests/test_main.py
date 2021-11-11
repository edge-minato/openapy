from pathlib import Path

from openapy import main

HERE = Path(__file__).absolute().parent
SRC_DIR = HERE.joinpath("server").joinpath("src").joinpath("openapi_server")
SRC_DIR_API = SRC_DIR.joinpath("apis")


def test_collect_src_files() -> None:
    pyfile_names = [f.name for f in main.collect_src_files(SRC_DIR_API)]
    assert len(pyfile_names) == 4
    assert "__init__.py" in pyfile_names
    assert "pet_api.py" in pyfile_names
    assert "store_api.py" in pyfile_names
    assert "user_api.py" in pyfile_names


def test_collect_src_files_recursive() -> None:
    pyfile_names = [f.name for f in main.collect_src_files(SRC_DIR)]
    assert len(pyfile_names) == 14
