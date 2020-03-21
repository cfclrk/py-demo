![img](https://github.com/cfclrk/py-demo/workflows/Release/badge.svg)

A minimal python project. Features:

-   Create a binary using
    [Pyinstaller](https://pythonhosted.org/PyInstaller/index.html)
-   GitHub Actions adds binaries to
    [releases](https://github.com/cfclrk/python-demo/releases)
-   Correctly handle data files


# Installation Options


## 1. Build from source (requires Python 3.8+)

Clone this project locally and then run:

    pip install .

Or, create a binary, which creates an executable file at `./dist/python-demo`:

    make binary


## 2. Download binary from a release

Head over to the [releases](https://github.com/cfclrk/python-demo/releases) page
and grab a binary. Or, to programmatically fetch the latest release (say, for
MacOS):

    repoUrl=https://api.github.com/repos/cfclrk/python-demo
    assetId=$(curl -s $repoUrl/releases/latest \
        | jq '.assets[] | select(.name | contains("Darwin")).id')
    curl -sSL -H "Accept: application/octet-stream" \
        $repoUrl/releases/assets/$assetId -o python-demo
    chmod +x python-demo


# Example

After installing, run either `python-demo` (if installed from source) or
`./python-demo` (if installed as a binary).

    python-demo --foo bar

    The version of this package is: 0.0.9
    The data file says: This is some text
    The value of foo is: bar

And it has a `--version` flag:

    python-demo --version

    0.0.9
