from ast import parse
from pathlib import Path
from typing import Optional

from pytest_mock import MockFixture

from openapy.main import main
from tests.conftest import EXAMPLE_APIS_DIR, EXAMPLES_DIR, TARGET_VERSION


class MockArgParser:
    def __init__(self, src: Path, all_flag: bool, template: Optional[str] = None) -> None:
        self.src = src
        self.all = all_flag
        self.template = template
        self.version = False


PA = "argparse.ArgumentParser.parse_args"


def test_main_new(mocker: MockFixture) -> None:
    for version in TARGET_VERSION:
        if version == "custom":
            continue
        print(f"  {version}: ", end="")
        mocker.patch(PA, return_value=MockArgParser(EXAMPLE_APIS_DIR(version), True))
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
        PA,
        return_value=MockArgParser(
            EXAMPLE_APIS_DIR("custom"),
            True,
            str(
                EXAMPLES_DIR.joinpath("custom_template.txt"),
            ),
        ),
    )
    main()
    processor_dir = EXAMPLE_APIS_DIR(version).parent.joinpath("processor")
    files = processor_dir.glob("*.py")
    for file in files:
        with file.open(mode="r") as f:
            parse(f.read())
    print("ok")


def test_main_updating(mocker: MockFixture) -> None:
    # generate old one first
    mocker.patch(
        PA,
        return_value=MockArgParser(EXAMPLE_APIS_DIR("existing"), False),
    )
    main()

    #
    print("  existing_new: ", end="")
    mocker.patch(
        PA,
        return_value=MockArgParser(
            EXAMPLE_APIS_DIR("existing").parent.joinpath("apis_updated"),
            False,
        ),
    )
    main()
    processor_dir = EXAMPLE_APIS_DIR("existing").parent.joinpath("processor")
    files = processor_dir.glob("*.new.py")
    i = 0
    for file in files:
        with file.open(mode="r") as f:
            parse(f.read())
        i += 1
    assert i == 6  # out of 8
    print("ok")
