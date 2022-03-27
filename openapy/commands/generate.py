from argparse import Namespace
from pathlib import Path

from openapy.config import Config, DestinationConfig
from openapy.diff import compare_as_function
from openapy.io import read_file, write_file
from openapy.parser import parse
from openapy.render import FilePerFunction
from openapy.template import get_template


def generate(args: Namespace) -> None:
    template = get_template(args.template)
    config = Config(Path(args.src), args.all)
    # iterate each source files
    if args.all:
        print("Info: Overwrite flag is True")
    for file in config.source_config.get_files():
        render_file(file, config.destination_config, template, args.all)


def render_file(file: Path, dc: DestinationConfig, template: str, overwrite: bool) -> None:
    print(f"Source file: {file}")
    ppf = parse(file)
    # iterate each functions
    for function in ppf.functions:
        print(f"  Function: {function.name}")
        rendered = FilePerFunction(ppf.imports, ppf.assigns, function).render(template)
        output_file_path = dc.get_output_file_path(function.name)
        # with force overwrite flag
        if overwrite:
            print(f"    -> {output_file_path}")
            write_file(output_file_path, rendered)
            continue
        # check difference
        if output_file_path.is_file():
            old = read_file(output_file_path)
            if compare_as_function(old, rendered):
                print("    No changes about interface, skip")
                continue
            print("    Conflicting with the existing file")
            output_file_path = dc.get_output_file_path(f"{function.name}.new")
        print(f"    -> {output_file_path}")
        write_file(output_file_path, rendered)
