import argparse
import json
import sys
from importlib import resources

from py_demo import __summary__, __version__, data_files


def cli() -> None:
    """Parse command line arguments and pass them to ``main``.

    This is the interactive (CLI) entry-point to the program.
    """
    parser = argparse.ArgumentParser(description=__summary__)
    parser.add_argument(
        "--version", default=False, action="store_true", help="Print version"
    )
    parser.add_argument("--foo", type=str, help="Provide a foo")
    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit(0)

    opts = vars(args)
    print(json.dumps(main(opts), indent=2))


def main(opts: dict) -> dict:
    """Run the program with the given options.

    This is the API entry-point to the program. Other projects should be able to import
    this project and run this function with the same options that the CLI supports.
    """
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    data = resources.read_text(data_files, "some_data.txt").strip()
    foo = opts.get("foo")
    return {"opts": opts, "version": version, "data": data, "foo": foo}


if __name__ == "__main__":
    cli()
