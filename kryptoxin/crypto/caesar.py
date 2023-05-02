"""
kryptoxin Caesar cipher module.
This is the "Caesar cipher" module of the kryptoxin project.
"""
from kryptoxin.core.toxin import Toxin


def encrypt(t: Toxin):
    """ This function perform the ceasar cipher encryption.
    """
    # create local list
    _ciphertext = []

    # Perform encryption
    for i in range(0, len(t.plaintext)):
        _ciphertext.append(t.plaintext[i]+2 & 0xFF)

    # Return the ciphertext
    return _ciphertext


# def decrypt(t: Toxin):
#     """ This function perform the ceasar cipher decryption.
#     """
#     # return the plaintext
#     return plaintext
