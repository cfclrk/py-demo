![img](https://github.com/cfclrk/py-demo/workflows/Release/badge.svg)

A minimal python project to explore and clarify best practices for project
structure, deployment, testing, etc.

-   Create a binary using [Pyinstaller](https://pythonhosted.org/PyInstaller/index.html)
-   Correctly handle data files
-   GitHub Actions to test and [release](https://github.com/cfclrk/py-demo/releases)


# Installation Options

1.  **From source** (requires Python 3.8+). Clone this project from GitHub
    and `pip install` it.

        git clone git@github.com:cfclrk/py-demo.git
        cd py-demo
        pip install .

2.  **From PyPI** (requires Python 3.8+). Use `pip` to install the [latest release from PyPI](https://pypi.org/project/py-demo/):

        pip install py-demo

3.  ****Standalone binary****. No local Python installation is needed. Download a
    binary from the [releases](https://github.com/cfclrk/py-demo/releases) page.


# Example

    py-demo --foo bar

Output:

    Python version:
    3.8.2 (default, Mar 19 2020, 11:37:51)
    [Clang 11.0.0 (clang-1100.0.33.16)]
    The data file says: This is some text
    The value of foo is: bar


# Testing

Run unit tests:

    make test

Run tests exactly as they will be run in GitHub Actions using [act](https://github.com/nektos/act):

    act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -j test


# Create a new project from this one

    set PROJECT_NAME change-me

    git clone --depth 1 git@github.com:cfclrk/py-demo.git $PROJECT_NAME
    cd $PROJECT_NAME
    rm -rf .git .github README.md

    # Update module name
    set moduleName (echo $PROJECT_NAME | string replace - _)
    mv src/py_demo src/$moduleName

    # Replace py-demo with $PROJECT_NAME
    find . -type f -exec sed -i "" "s/py-demo/$PROJECT_NAME/g" {} ";"

    # Replace py_demo with module name
    find . -type f -exec sed -i "" "s/py_demo/$moduleName/g" {} ";"

    # Set version back to 0.0.1
    sed -i "" 's/^version = .*/version = 0.0.1/' setup.cfg
