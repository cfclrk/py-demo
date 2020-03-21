from importlib import metadata

m = metadata.metadata(__name__)

__version__ = m.get("Version")
__summary__ = m.get("Summary")
