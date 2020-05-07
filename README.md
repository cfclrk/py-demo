![img](https://github.com/cfclrk/py-demo/workflows/Release/badge.svg)

A minimal python project. Features:

-   Create a binary using
    [Pyinstaller](https://pythonhosted.org/PyInstaller/index.html)
-   Correctly handle data files
-   GitHub Actions to test and release
    -   Create a [release](https://github.com/cfclrk/py-demo/releases) by
        pushing a tag
    -   Adds PyInstaller binaries to the release
    -   Deploys a wheel to PyPI


# Installation

Here are a few different ways this project can be installed.


## 1. From source (requires Python 3.8+)

To install from source, clone this project from github and `pip install` it.

    git clone git@github.com:cfclrk/py-demo.git
    cd py-demo
    pip install .


## 2. From PyPI (requires Python 3.8+)

Use `pip` to install the [latest release from
PyPI](https://pypi.org/project/py-demo/):

    pip install py-demo


## 3. Standalone binary

No local Python installation is needed. Download a binary from the
[releases](https://github.com/cfclrk/py-demo/releases) page.


# Example

    py-demo --foo bar

    Project version is: 0.0.2
    The data file says: This is some text
    The value of foo is: bar

And it has a `--version` flag:

    py-demo --version

    0.0.2
