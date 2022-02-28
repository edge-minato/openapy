import argparse
import sys

from openapy.commands.version import show_version
from openapy.io import exit_with_error


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Additional files generator for openapi")
    parser.set_defaults(command="openapy")
    parser.add_argument("--version", "-v", action="store_true", help="show version")

    # Subparsers
    sp = parser.add_subparsers()
    sp_generate = sp.add_parser("generate", help="generate processor files")
    sp_example = sp.add_parser("example", help="output examples")
    sp_version = sp.add_parser("version", help="show version")

    sp2_example = sp_example.add_subparsers()
    sp_example_template = sp2_example.add_parser("template", help="template for `generate -t`")
    sp_example_docker = sp2_example.add_parser("docker", help="docker command")
    sp_example_mustache = sp2_example.add_parser("mustache", help="api.mustache")

    # generate
    sp_generate.set_defaults(command="generate")
    sp_generate.add_argument("--src", "-s", type=str, default=None, help="source dir path")
    sp_generate.add_argument("--template", "-t", type=str, default=None, help="file path of the template")
    sp_generate.add_argument("--all", "-a", action="store_true", help="whether overwrite all files or not")

    # example
    sp_example.set_defaults(command="example")
    sp_example_template.set_defaults(command="example.template")
    sp_example_docker.set_defaults(command="example.docker")
    sp_example_mustache.set_defaults(command="example.mustache")

    # version
    sp_version.set_defaults(command="version")

    args = parser.parse_args()
    # Handle error cases and special cases
    if args.command == "openapy":
        show_version() if args.version else (parser.print_help() or sys.exit(0))  # type: ignore
    if args.command == "generate" and args.src is None:
        exit_with_error("TIPS: --src, -s argument is required")
    if args.command == "example":
        sp_example.print_help() or sys.exit(0)  # type: ignore

    return args
