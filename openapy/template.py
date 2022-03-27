from enum import Enum
from pathlib import Path
from typing import Optional

from single_source import get_version

from openapy.io import exit_with_error

GITHUB = "https://github.com/edge-minato/openapy"
VERSION = get_version(__package__, Path(__file__).parent.parent)
LOGO = """
 ██████╗ ██████╗ ███████╗███╗   ██╗ █████╗ ██████╗ ██╗   ██╗
██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████║██████╔╝ ╚████╔╝
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══██║██╔═══╝   ╚██╔╝
╚██████╔╝██║     ███████╗██║ ╚████║██║  ██║██║        ██║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝        ╚═╝\
"""  # noqa: W291

TEMPLATE = """
# coding: utf-8

{IMPORTS}

def {NAME}({ARGS}) -> {RETURN_TYPE}:
    {COMMENT}
    # implement me
    ...
"""


def get_template(args_template: Optional[str]) -> str:
    if args_template is None:
        return TEMPLATE
    else:
        template_path = Path(args_template)
        if not template_path.is_file():
            exit_with_error(f"ERROR: template file was not found:\n  {args_template}")
        with template_path.open(mode="r") as f:
            return f.read()


class NOQA(Enum):
    # The space at head is intended
    F401 = " # noqa: F401"
