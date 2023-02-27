"""
kryptoxin AES cipher module.
This is the aes cipher module of the kryptoxin project.
"""
from ..core import log
from ..core.constants import *
from . import base64, pbkdf2
import Crypto.Cipher.AES


def _cipher_opmode(mode):
    """ This local function returns the appropriate block-cipher
    operation mode.
    """
    # Cipher block operation modes mapping
    # use if-then until python 3.10 becomes more readily available.
    if mode.casefold() == CIPHER_BLOCK_OPERMODE_CBC:
        op_mode = Crypto.Cipher.AES.MODE_CBC
    elif mode.casefold() == CIPHER_BLOCK_OPERMODE_CFB:
        op_mode = Crypto.Cipher.AES.MODE_CFB
    elif mode.casefold() == CIPHER_BLOCK_OPERMODE_OFB:
        op_mode = Crypto.Cipher.AES.MODE_OFB
    elif mode.casefold() == CIPHER_BLOCK_OPERMODE_EAX:
        op_mode = Crypto.Cipher.AES.MODE_EAX
    else:
        log.error(f"Unknown cipher block operation mode '{mode}'.")
        raise SystemExit

    return op_mode


def encrypt(
    plaintext, key, key_size, salt, mode,
    iv, halg=CIPHER_DEFAULT_HMHASHALG,
    pbkdf2_iter=CIPHER_DEFAULT_PBKDF2_ITER,
    iv_prepend=CIPHER_DEFAULT_IV_PREPEND
):
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
    # Determine the block-cipher operation mode.
    op_mode = _cipher_opmode(mode)

    # PKCS#7 Padding
    # pad the plaintext to the nearest multiple of block's length.
    padding = CIPHER_BLOCK_BLKSZ_AES - \
        (len(plaintext) % CIPHER_BLOCK_BLKSZ_AES)
    padded_plaintext = plaintext + bytes([padding] * padding)

    # call the key-derivation function
    derived_key = pbkdf2.derive_key(key, key_size, halg, pbkdf2_iter, salt)

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


def decrypt(
    ciphertext, key, key_size, salt, mode,
    iv, halg=CIPHER_DEFAULT_HMHASHALG,
    pbkdf2_iter=CIPHER_DEFAULT_PBKDF2_ITER,
    iv_prepend=CIPHER_DEFAULT_IV_PREPEND
):
    """ This function perform AES block cipher decryption.

    Arguments:
    ciphertext: cipher-text data
    key: Cipher's key (bytes[])
    key_size: Algorithm key size
    salt: Salt used to enhance hash security (bytes[])
    mode: Block cipher operation mode
    iv: Block cipher initialization vector (bytes[])
    halg: PBKDF2 HMAC algorithm
    pbkdf2_iter: Number of iterations for the key-derivation function
    iv_prepend: Prepend Initialization Vector (IV) to the plain-text
    """
    # Decode the ciphertext using base64
    ciphertext = base64.decode_base64(ciphertext)

    # Determine the block-cipher operation mode.
    op_mode = _cipher_opmode(mode)

    # Call the key-derivation function
    derived_key = pbkdf2.derive_key(key, key_size, halg, pbkdf2_iter, salt)

    # Create new AES cipher
    cipher = Crypto.Cipher.AES.new(derived_key, op_mode, iv)

    # Perform decryption
    plaintext = cipher.decrypt(ciphertext)

    # If iv-prepending is True truncate the inizialization vector
    # from the returned plaintext.
    if iv_prepend:
        plaintext = plaintext[CIPHER_BLOCK_BLKSZ_AES:]

    # Removes the PKCS#7 padding bytes
    # Read the padding length from the plaintext and
    # truncate the plaintext accordingly.
    pad_len = plaintext[-1]
    plaintext = plaintext[:-pad_len]

    # Check plaintext bytes object size.
    if not len(plaintext):
        log.error(
            "Error while performing AES decryption. "
            "Verify input parameters such as the key.")
        raise SystemExit

    # return the plaintext
    return plaintext
