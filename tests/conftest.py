from pathlib import Path
from shutil import rmtree
from typing import Generator

import pytest

# Global variables

# Actual path
HERE = TESTS_DIR = Path(__file__).absolute().parent
REPO_DIR = TESTS_DIR.parent

SAMPLES_DIR = TESTS_DIR.joinpath("samples")
SAMPLE_APIS = SAMPLES_DIR.joinpath("apis")
SAMPLE_MUSTACHES = SAMPLES_DIR.joinpath("mustache")
SAMPLE_EXPECTS = SAMPLES_DIR.joinpath("expects")
SAMPLE_PROCESSOR_DIR = SAMPLES_DIR.joinpath("processor")

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
    print("\nteardown after session")


def log(log) -> None:  # type: ignore
    print(f"\n  {log}")
