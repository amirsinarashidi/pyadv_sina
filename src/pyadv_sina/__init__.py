"""Demo package for live course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-sina")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Amirsina"
__email__ = "amirsina.rashidi@gmail.com"
