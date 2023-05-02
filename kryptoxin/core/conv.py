"""
kryptoxin conversion module.
This is the toxin module of the kryptoxin project
where types conversions and transformations are done.
"""


def bytes2decarray(barray):
    """ This method converts a binary array in argument
        and convert it to a decimal array.
    """
    _declist = []
    for b in barray:
        _declist.append(f'{b:d}')
        #_declist.append(b+2 & 0xFF)
    return _declist
