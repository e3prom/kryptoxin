"""
kryptoxin package module.
This is the package module of the kryptoxin project.
"""
import os
from kryptoxin.__version__ import __version__

ROOT_DIR = os.path.abspath(__path__[0])


def get_version():
    """ This function simply returns the version string.
    """
    return __version__
