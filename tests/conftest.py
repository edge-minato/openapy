from pathlib import Path
from shutil import rmtree
from typing import Generator

import pytest

# Global variables
TARGET_VERSION = ["custom", "v5.2.1", "v5.3.1", "v5.4.0"]

# Actual path
HERE = TESTS_DIR = Path(__file__).absolute().parent
REPO_DIR = TESTS_DIR.parent

EXAMPLES_DIR = TESTS_DIR.joinpath("examples")
EXAMPLE_MUSTACHES = EXAMPLES_DIR.joinpath("mustache")
EXAMPLE_EXPECTS = EXAMPLES_DIR.joinpath("expects")
TEMP_DIR = HERE.joinpath("tmp")
TEMP_PROCESSOR_DIR = TEMP_DIR.joinpath("processor")

# Dummy path
DIR_NOT_FOUND = HERE.joinpath("ABCDEFG")
FILE_NOT_FOUND = HERE.joinpath("abcd.efg")

# Methods for test


def prepare_tmp_dir(tmp: Path) -> None:
    tmp.mkdir()


def remove_tmp_dir(tmp: Path) -> None:
    rmtree(tmp, ignore_errors=True)


@pytest.fixture(scope="session", autouse=True)
def scope_session() -> Generator:
    print("\nsetup before session")
    tmp = TESTS_DIR.joinpath("tmp")

    remove_tmp_dir(tmp)
    prepare_tmp_dir(tmp)
    yield
    remove_tmp_dir(tmp)
    for version in TARGET_VERSION:
        remove_tmp_dir(EXAMPLES_DIR.joinpath(version).joinpath("processor"))
    print("\nteardown after session")


def log(log) -> None:  # type: ignore
    print(f"\n  {log}")


def EXAMPLE_APIS_DIR(version: str) -> Path:
    return EXAMPLES_DIR.joinpath(version).joinpath("apis")
