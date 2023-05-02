"""
kryptoxin Caesar cipher module.
This is the "Caesar cipher" module of the kryptoxin project.
"""
from kryptoxin.core.toxin import Toxin
from kryptoxin.core.log import log
from kryptoxin.crypto import base64


def encrypt(t: Toxin, key=2):
    """ This function perform the ceasar cipher encryption.
    """
    # create a binary literal
    _ciphertext = b""

    # Perform encryption while testing the plaintext
    try:
        for i in range(0, len(t.plaintext)):
            _ciphertext += bytes(chr(t.plaintext[i]+key & 0xFF), 'ascii')
    except UnicodeEncodeError:
        _ciphertext = b""
        for i in range(0, len(t.plaintext)):
            _ciphertext += (t.plaintext[i]+key & 0xFF).to_bytes(1, 'little')
    except None:
        log.error("Cannot interpret input format.")
        raise SystemExit

    # Return the ciphertext
    return _ciphertext


def decrypt(t: Toxin, key=2):
    """ This function perform the ceasar cipher decryption.
    """
    plaintext = ""

    # Decode the ciphertext using base64.
    try:
        _ciphertext = base64.decode_base64(t.ciphertext)
    except base64.base64.binascii.Error:
        log.error("Cannot decode ciphertext input using base64.")
        raise SystemExit

    # perform byte shift 'decryption'
    for i in range(0, len(_ciphertext)):
        plaintext += chr(_ciphertext[i]-key & 0xFF)

    # return the plaintext
    return bytes(plaintext, 'UTF-8')
