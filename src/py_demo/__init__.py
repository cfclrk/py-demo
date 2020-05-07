from importlib import metadata

project_metadata = metadata.metadata(__name__)

__version__ = project_metadata.get("Version")
__summary__ = project_metadata.get("Summary")
