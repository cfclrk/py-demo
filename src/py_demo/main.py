import sys
from importlib import resources

from py_demo import data_files


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
