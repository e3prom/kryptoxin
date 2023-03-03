"""
kryptoxin unformatted output module.
This module contains functions for unformatted outputs
"""


def plain(data):
    """ This function simply cast the data as a string
    and return it encoded in UTF-8.
    """
    return str(data, 'UTF-8')


def binary(data):
    """ This function simply return data in byte array
    """
    return data
