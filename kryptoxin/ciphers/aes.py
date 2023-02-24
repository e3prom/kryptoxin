"""
kryptoxin AES cipher module.
This is the aes cipher module of the kryptoxin project.
"""
from ..core import *  # Import all from core
from . import base64
import hashlib
import Crypto.Cipher.AES


def encrypt_aes(plaintext, key, key_size, salt, mode, iv, halg=CIPHER_DEFAULT_HMHASHALG,
                pbkdf2_iter=CIPHER_DEFAULT_PBKDF2_ITER, iv_prepend=CIPHER_DEFAULT_IV_PREPEND):
    """ This function perform AES block cipher encryption.
        Pads the plain-text using PKCS#7.
        Derives an encryption key using the PBKDF2 key-derivation function.

    Arguments:
    plaintext: The plain-text message to encrypt
    key: Cipher's key (bytes[])
    key_size: Algorithm key size
    salt: Salt used to enhance hash security (bytes[])
    mode: Block cipher operation mode
    iv: Block cipher initialization vector (bytes[])
    halg: PBKDF2 HMAC algorithm
    pbkdf2_iter: Number of iterations for the key-derivation function
    iv_prepend: Prepend Initialization Vector (IV) to the plain-text
    """
    # Cipher block operation modes mapping
    # use if-then until python 3.10 becomes more readily available.
    if mode == CIPHER_BLOCK_OPERMODE_CBC:
        op_mode = Crypto.Cipher.AES.MODE_CBC
    elif mode == CIPHER_BLOCK_OPERMODE_CFB:
        op_mode = Crypto.Cipher.AES.MODE_CFB
    elif mode == CIPHER_BLOCK_OPERMODE_OFB:
        op_mode = Crypto.Cipher.AES.MODE_OFB
    elif mode == CIPHER_BLOCK_OPERMODE_EAX:
        op_mode = Crypto.Cipher.AES.MODE_EAX
    else:
        log.error(f"Unknown cipher block operation mode '{mode}'.")
        raise SystemExit

    # PKCS#7 Padding
    # pad the plaintext to the nearest multiple of block's length.
    padding = CIPHER_BLOCK_BLKSZ_AES - \
        (len(plaintext) % CIPHER_BLOCK_BLKSZ_AES)
    padded_plaintext = plaintext + bytes([padding] * padding)

    # Derived key sizes
    # must be 16, 24 or 32 bytes for AES128,192,256 respectively.
    dklen = CIPHER_PBKDF2_AES256_KS
    if key_size == 128:
        dklen = CIPHER_PBKDF2_AES128_KS
    elif key_size == 192:
        dklen = CIPHER_PBKDF2_AES192_KS
    elif key_size == 256:
        dklen = CIPHER_PBKDF2_AES256_KS
    else:
        log.error(
            f"Invalid AES key size '{key_size}'. Available: 128, 192, 256 bits")
        raise SystemExit

    # Derive the encryption key from the password.
    derived_key = hashlib.pbkdf2_hmac(halg, memoryview(
        key), memoryview(salt), pbkdf2_iter, dklen)

    # Create new AES cipher
    cipher = Crypto.Cipher.AES.new(derived_key, op_mode, iv)

    # Perform encryption
    # some libraries require the initialization vector to be
    # prepended to the plaintext before encryption.
    if iv_prepend:  # If True, prepend the IV
        ciphertext = cipher.encrypt(bytes(iv) + padded_plaintext)
    else:
        ciphertext = cipher.encrypt(padded_plaintext)

    # Encode and return the ciphertext in base64.
    return base64.encode_base64(ciphertext)
