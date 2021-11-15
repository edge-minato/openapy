from pathlib import Path

# Global variables

# Actual path
HERE = TESTS_DIR = Path(__file__).absolute().parent
SRC_DIR = HERE.joinpath("server").joinpath("src").joinpath("openapi_server")
SRC_APIS_DIR = SRC_DIR.joinpath("apis")
SRC_MODELS_DIR = SRC_DIR.joinpath("models")
DST_DIR = SRC_DIR.joinpath("output")
TEMPLATE_DIR = HERE.joinpath("template")
CONFIG_DIR = HERE.joinpath("config")

# Dummy path
DIR_NOT_FOUND = HERE.joinpath("ABCDEFG")
FILE_NOT_FOUND = HERE.joinpath("abcd.efg")

# Methods for test


def log(log) -> None:  # type: ignore
    print(f"\n  {log}")
