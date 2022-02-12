from pytest_mock import MockFixture

from openapy.main import main
from tests.conftest import EXAMPLE_APIS_DIR, TARGET_VERSION


class MockArgParser:
    def __init__(self, version: str) -> None:
        self.src = EXAMPLE_APIS_DIR(version)
        self.tag = version
        self.all = True
        self.indent = 4


def test_main(mocker: MockFixture) -> None:
    for version in TARGET_VERSION:
        if version == "custom":
            continue
        mocker.patch("argparse.ArgumentParser.parse_args", return_value=MockArgParser(version))
        main()
