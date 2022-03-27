from ast import parse
from pathlib import Path
from typing import Optional

from openapy.commands.generate import generate, render_init
from tests.conftest import EXAMPLE_APIS_DIR, EXAMPLES_DIR, TARGET_VERSION, TEMP_DIR


class MockArgParser:
    def __init__(self, src: Path, all_flag: bool, template: Optional[str] = None) -> None:
        self.src = src
        self.all = all_flag
        self.template = template
        self.version = False


def test_generate_new() -> None:
    for version in TARGET_VERSION:
        if version == "custom":
            continue
        print(f"  {version}: ", end="")
        generate(MockArgParser(EXAMPLE_APIS_DIR(version), True))
        processor_dir = EXAMPLE_APIS_DIR(version).parent.joinpath("processor")
        files = processor_dir.glob("*.py")
        for file in files:
            with file.open(mode="r") as f:
                parse(f.read())
        print("ok")

    # custom
    print("  custom: ", end="")
    args = MockArgParser(
        EXAMPLE_APIS_DIR("custom"),
        True,
        str(
            EXAMPLES_DIR.joinpath("custom_template.txt"),
        ),
    )
    generate(args)
    processor_dir = EXAMPLE_APIS_DIR(version).parent.joinpath("processor")
    files = processor_dir.glob("*.py")
    for file in files:
        with file.open(mode="r") as f:
            parse(f.read())
    print("ok")


def test_generate_updating() -> None:
    # generate old one first
    generate(MockArgParser(EXAMPLE_APIS_DIR("existing"), False))

    #
    print("  existing_new: ", end="")
    generate(MockArgParser(EXAMPLE_APIS_DIR("existing").parent.joinpath("apis_updated"), False))
    processor_dir = EXAMPLE_APIS_DIR("existing").parent.joinpath("processor")
    files = processor_dir.glob("*.new.py")
    i = 0
    for file in files:
        with file.open(mode="r") as f:
            parse(f.read())
        i += 1
    assert i == 6  # out of 8
    print("ok")


def test_render_init() -> None:
    output_files = [Path(file) for file in ["a.py", "b.py", "c.py"]]
    init_py = TEMP_DIR.joinpath("__init__.py")
    render_init(output_files, init_py)
    with init_py.open(mode="r") as f:
        rendered = f.read()
    assert "from .a import a  # noqa: F401" in rendered
    assert "from .b import b  # noqa: F401" in rendered
    assert "from .c import c  # noqa: F401" in rendered
