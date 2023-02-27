"""
kryptoxin PBKDF2  module.
This is the key-derivation function PBKDF2 module of the kryptoxin project.
"""
from ..core import log
from ..core.constants import *
import hashlib


def derive_key(key, key_size, halg, iter, salt):
    """ This function perform the key derivation function
    using PBKDF2.

    Arguments:
    key: Cipher's key (bytes[])
    key_size: Algorithm key size
    halg: PBKDF2 HMAC algorithm
    iter: Number of iterations for the key-derivation function
    salt: Salt used to enhance hash security (bytes[])
    """
    # Derived key sizes per block-cipher algorithms.
    # must be 16, 24 or 32 bytes for AES128,192,256 respectively.
    dklen = CIPHER_PBKDF2_AES256_KS
    if key_size == 128:
        dklen = CIPHER_PBKDF2_AES128_KS
    elif key_size == 192:
        dklen = CIPHER_PBKDF2_AES192_KS
    elif key_size == 256:
        dklen = CIPHER_PBKDF2_AES256_KS
    else:
        log.error(f"Invalid AES key size '{key_size}")
        raise SystemExit

    # Derive the encryption key from the password.
    derived_key = hashlib.pbkdf2_hmac(halg, memoryview(
        key), memoryview(salt), iter, dklen)

    # return the derived_key
    return derived_key