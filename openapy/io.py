from pathlib import Path


def read_file(path: Path) -> str:
    with path.open(mode="r") as f:
        return f.read()


def write_file(path: Path, content: str) -> None:
    with path.open(mode="w") as f:
        f.write(content)
