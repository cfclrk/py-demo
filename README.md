![img](https://github.com/cfclrk/py-demo/workflows/Release/badge.svg)

A minimal python project to explore and clarify best practices for project
structure, deployment, testing, etc. I am trying to document design decisions in
the [wiki](https://github.com/cfclrk/py-demo/wiki).

-   Create a binary using
    [Pyinstaller](https://pythonhosted.org/PyInstaller/index.html)
-   Correctly handle data files
-   GitHub Actions to test and
    [release](https://github.com/cfclrk/py-demo/releases)


# Installation

1.  **From source** (requires Python 3.8+). Clone this project from GitHub and
    `pip install` it.

    ```bash
    git clone git@github.com:cfclrk/py-demo.git
    cd py-demo
    pip install .
    ```

2.  **From PyPI** (requires Python 3.8+). Use `pip` to install the latest
    [release](https://pypi.org/project/py-demo/) from PyPI:

    ```bash
    pip install py-demo
    ```

3.  **Standalone binary**. No local Python installation is needed. Download a
    binary from the [releases](https://github.com/cfclrk/py-demo/releases) page.


# Example

```bash
py-demo --foo bar
```

    {
      "cli_opts": {
        "version": false,
        "foo": "bar"
      },
      "python_version": "3.9",
      "data_from_file": "This is some text"
    }


# Testing

Run unit tests:

```bash
make test
```

Run tests exactly as they will be run in GitHub Actions using
[act](https://github.com/nektos/act):

```bash
act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -j test
```


# Create a new project from this one

```bash
git clone --depth 1 git@github.com:cfclrk/py-demo.git $NEW_PROJECT_NAME
cd $NEW_PROJECT_NAME
rm -rf .git .github README.md

# Update the project name
find . -type f -exec sed -i "" "s/py-demo/$NEW_PROJECT_NAME/g" {} ";"

# Update the python module name
moduleName=$(echo $NEW_PROJECT_NAME | sed s/-/_/g)
mv src/py_demo src/$moduleName
find . -type f -exec sed -i "" "s/py_demo/$moduleName/g" {} ";"

# Set version back to 0.0.1
sed -i "" 's/^version = .*/version = 0.0.1/' setup.cfg

# Delete lines 7-10 in setup.cfg, which have project URL
sed -i "" 7,10d setup.cfg
```
