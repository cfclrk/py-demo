import argparse
import json
import sys
from importlib import resources

from py_demo import __summary__, __version__, data_files


def cli() -> None:
    """Parse command line arguments and call ``main``.

    This is the interactive (CLI) entry-point to the program.
    """
    parser = argparse.ArgumentParser(description=__summary__)
    parser.add_argument(
        "--version", default=False, action="version", version=__version__
    )
    parser.add_argument("--foo", type=str, help="Provide a foo")
    args = parser.parse_args()

    opts = vars(args)
    print(json.dumps(main(opts), indent=2))


def main(opts: dict) -> dict:
    """Run this program with the given options.

    This is the programmatic entry-point to the program. Python projects should be able
    to import this module and run this function using the same options that the CLI
    supports.
    """
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    data_from_file = resources.read_text(data_files, "some_data.txt").strip()
    return {
        "cli_opts": opts,
        "python_version": python_version,
        "data_from_file": data_from_file,
    }


# When executed interactively (vs being programmatically imported), use the CLI.
if __name__ == "__main__":
    cli()
