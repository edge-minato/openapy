from ast import parse
from typing import Optional

from pytest_mock import MockFixture

from openapy.main import main
from tests.conftest import EXAMPLE_APIS_DIR, EXAMPLES_DIR, TARGET_VERSION


class MockArgParser:
    def __init__(self, version: str, template: Optional[str] = None) -> None:
        self.src = EXAMPLE_APIS_DIR(version)
        self.tag = version
        self.all = True
        self.template = template


def test_main(mocker: MockFixture) -> None:
    for version in TARGET_VERSION:
        if version == "custom":
            continue
        print(f"  {version}: ", end="")
        mocker.patch("argparse.ArgumentParser.parse_args", return_value=MockArgParser(version))
        main()
        processor_dir = EXAMPLE_APIS_DIR(version).parent.joinpath("processor")
        files = processor_dir.glob("*.py")
        for file in files:
            with file.open(mode="r") as f:
                parse(f.read())
        print("ok")
    # custom
    print("  custom: ", end="")
    mocker.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=MockArgParser("custom", str(EXAMPLES_DIR.joinpath("custom_template.txt"))),
    )
    main()
    processor_dir = EXAMPLE_APIS_DIR(version).parent.joinpath("processor")
    files = processor_dir.glob("*.py")
    for file in files:
        with file.open(mode="r") as f:
            parse(f.read())
    print("ok")
