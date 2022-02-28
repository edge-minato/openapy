import pkgutil
import sys
from pathlib import Path


def read_file(path: Path) -> str:
    with path.open(mode="r") as f:
        return f.read()


def write_file(path: Path, content: str) -> None:
    with path.open(mode="w") as f:
        f.write(content)


def exit_with_error(msg: str) -> None:
    print(msg)
    sys.exit(1)


def get_resource(package_name: str, filename: Path) -> str:
    try:
        resource = pkgutil.get_data(package_name, str(filename))
        if resource is None:
            raise FileNotFoundError(f"ERROR: Failed to load {filename}")
        return resource.decode("utf-8")
    except Exception:
        raise Exception(f"ERROR: Failed to load {filename}")


def get_my_resource(filename: str) -> str:
    return get_resource(__package__, Path("examples").joinpath(filename))
