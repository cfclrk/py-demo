# -*- mode: python -*-

"""PyInstaller spec file.

PyInstaller creates a native binary (with a bundled Python interpreter) from a python
project. This file specifies how PyInstaller should create a binary for this project.

Note: You must run ``pip install .`` to create project metadata before running
pyinstaller. Project metadata is the stuff in a ``.egg_info`` directory, and this spec
loads those files into the binary.
"""
import configparser

from PyInstaller.utils.hooks import copy_metadata

# Get the project name from setup.cfg
config = configparser.ConfigParser()
config.read("setup.cfg")
PROJECT_NAME = config["metadata"]["name"]

# The project module should always be the same as the project name, but with underscores
# instead of dashes if there are any.
PROJECT_MODULE_NAME = PROJECT_NAME.replace("-", "_")

# Don't encrypt the binary
BLOCK_CIPHER = None


a = Analysis(
    [f"src/{PROJECT_MODULE_NAME}/main.py"],
    binaries=[],
    datas=[
        *copy_metadata(PROJECT_NAME),
        (
            f"src/{PROJECT_MODULE_NAME}/data_files/*",
            f"{PROJECT_MODULE_NAME}/data_files",
        ),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=BLOCK_CIPHER,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=BLOCK_CIPHER)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=PROJECT_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,
)
