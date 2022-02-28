from openapy.io import get_my_resource


def show_resource(filename: str) -> None:
    print(get_my_resource(filename))


def show_example(kind: str) -> None:
    if "docker" in kind:
        show_resource("docker.sh")
    elif "template" in kind:
        show_resource("template.py.txt")
    elif "mustache" in kind:
        show_resource("api.mustache")
    else:
        raise Exception(f"Unexpected example type: {kind}")
