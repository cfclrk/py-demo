![img](https://github.com/cfclrk/py-demo/workflows/Release/badge.svg)

A minimal python project. Features:

-   Create a binary using
    [Pyinstaller](https://pythonhosted.org/PyInstaller/index.html)
-   GitHub Actions adds binaries to
    [releases](https://github.com/cfclrk/py-demo/releases)
-   Correctly handle data files


# Installation Options


## 1. Build from source (requires Python 3.8+)

Clone this project locally and then run:

    pip install .

Or, create a binary, which creates an executable file at `./dist/py-demo`:

    make binary


## 2. Install from PyPI

Use `pip` to install the [latest release from
PyPI](https://pypi.org/project/py-demo/):

    pip install py-demo


## 3. Download binary from a release

Download a binary from the
[releases](https://github.com/cfclrk/py-demo/releases) page. Or, to
programmatically fetch the latest release (say, for MacOS):

    repoUrl=https://api.github.com/repos/cfclrk/py-demo
    assetId=$(curl -s $repoUrl/releases/latest \
        | jq '.assets[] | select(.name | contains("Darwin")).id')
    curl -sSL -H "Accept: application/octet-stream" \
        $repoUrl/releases/assets/$assetId -o py-demo
    chmod +x py-demo


# Example

After installing, run either `py-demo` (if installed from source) or `./py-demo`
(if installed as a binary).

    py-demo --foo bar

    Project version is: 0.0.2
    The data file says: This is some text
    The value of foo is: bar

And it has a `--version` flag:

    py-demo --version

    0.0.2
