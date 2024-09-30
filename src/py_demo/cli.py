import argparse
import json

from py_demo import __summary__, __version__, main


def arg_parser() -> argparse.ArgumentParser:
    """Define a CLI parser for this program."""
    parser = argparse.ArgumentParser(description=__summary__)
    assert isinstance(__version__, str)
    parser.add_argument(
        "--version", default=False, action="version", version=__version__
    )
    parser.add_argument("--foo", type=str, help="Provide a foo")
    return parser


def cli() -> None:
    """Parse command line arguments and call main().

    This is the interactive (CLI) entry-point to the program.
    """
    cli_parser = arg_parser()
    cli_args = cli_parser.parse_args()
    cli_vars = vars(cli_args)
    print(json.dumps(main.main(cli_vars), indent=2))


# When executed interactively (vs being programmatically imported), use the CLI.
if __name__ == "__main__":
    cli()
