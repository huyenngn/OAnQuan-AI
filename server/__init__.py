"""The server package."""

from importlib import metadata

try:
    __version__ = metadata.version("oanquan_ai")
except metadata.PackageNotFoundError:
    __version__ = "unknown"
del metadata
