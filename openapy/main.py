from openapy.args import get_args
from openapy.commands.example import show_example
from openapy.commands.generate import generate
from openapy.commands.version import show_version


def main() -> None:
    args = get_args()
    if "generate" in args.command:
        generate(args)
    elif "example" in args.command:
        show_example(args.command)
    elif "version" in args.command:
        show_version()
    else:
        raise Exception(f"Unexpected error: command is {args.command}")
