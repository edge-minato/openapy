from pathlib import Path

from jinja2 import Template


def render(template_file: Path, variables: dict, output_file: Path) -> None:
    try:
        with template_file.open(mode="r") as f:
            template = Template(f.read())
        with output_file.open(mode="w") as f:
            f.write(template.render(**variables))
    except Exception as e:
        raise e
