from pathlib import Path

from openapy.args import get_args
from openapy.config import Config
from openapy.io import write_file
from openapy.parser import parse
from openapy.render import FilePerFunction
from openapy.template import TEMPLATE


def main() -> None:
    args = get_args()
    src = Path(args.src)
    config = Config(src, args.tag, args.all)
    src_files = config.source_config.get_files()
    for src in src_files:
        ppf = parse(src)
        imports = ppf.get_imports_str()
        assigns = ppf.get_assigns_str()
        for function in ppf.functions:
            name = function.name
            fpf = FilePerFunction(imports, assigns, function)
            rendered = fpf.render(TEMPLATE)
            output_file_path = config.destination_config.get_output_file_path(name)
            write_file(output_file_path, rendered)
            exit(0)
