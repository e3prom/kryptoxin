"""
kryptoxin base64 encoder module.
This is the base64 encoder module of the kryptoxin project.
"""
import base64
from ..core import *  # Import all from core


def encode_base64(data):
    """ This function perform base64 encoding of the input.

    Arguments:
    data: Data to encode in base64 (bytes[])
    """
    return base64.b64encode(data)


def decode_base64(data):
    """ This function perform base64 decoding of the input.

    Arguments:
    data: Data to decode in base64 (bytes[])
    """
    return base64.b64decode(data)
