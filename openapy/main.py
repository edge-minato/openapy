from pathlib import Path

from openapy.args import get_args
from openapy.config import Config, DestinationConfig
from openapy.io import write_file
from openapy.parser import parse
from openapy.render import FilePerFunction
from openapy.template import get_template


def render_file(file: Path, dc: DestinationConfig, template: str) -> None:
    ppf = parse(file)
    # iterate each functions
    for function in ppf.functions:
        # print(function.name)
        fpf = FilePerFunction(ppf.imports, ppf.assigns, function)
        rendered = fpf.render(template)
        # print(dc.get_output_file_path(function.name))
        write_file(dc.get_output_file_path(function.name), rendered)


def main() -> None:
    args = get_args()
    template = get_template(args.template)
    config = Config(Path(args.src), args.all)
    # iterate each source files
    for file in config.source_config.get_files():
        render_file(file, config.destination_config, template)
