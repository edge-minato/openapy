from pathlib import Path

from openapy.args import get_args
from openapy.config import Config, DestinationConfig
from openapy.diff import compare_as_function
from openapy.io import read_file, write_file
from openapy.parser import parse
from openapy.render import FilePerFunction
from openapy.template import get_template


def render_file(file: Path, dc: DestinationConfig, template: str, overwrite: bool) -> None:
    ppf = parse(file)
    # iterate each functions
    for function in ppf.functions:
        print(function.name)
        rendered = FilePerFunction(ppf.imports, ppf.assigns, function).render(template)
        output_file_path = dc.get_output_file_path(function.name)
        # with force overwrite flag
        if overwrite:
            print(output_file_path)
            write_file(output_file_path, rendered)
            continue
        # check difference
        if output_file_path.is_file():
            old = read_file(output_file_path)
            if compare_as_function(old, rendered):
                print("No changes about interface, skip")
                continue
            print("Conflicting with the existing file")
            output_file_path = dc.get_output_file_path(f"{function.name}.new")
        print(output_file_path)
        write_file(output_file_path, rendered)


def main() -> None:
    args = get_args()
    template = get_template(args.template)
    config = Config(Path(args.src), args.all)
    # iterate each source files
    for file in config.source_config.get_files():
        render_file(file, config.destination_config, template, args.all)
