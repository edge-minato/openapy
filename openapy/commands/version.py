import sys

from openapy.template import GITHUB, LOGO, VERSION


def show_version() -> None:
    print(LOGO)
    print(f"{GITHUB}     version: {VERSION}")
    sys.exit(0)
