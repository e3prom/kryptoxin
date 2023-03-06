"""
kryptoxin AES cipher module.
This is the aes cipher module of the kryptoxin project.
"""
from ..core.toxin import Toxin
from ..core.log import log
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


def encrypt(t: Toxin):
    """ This function perform AES block cipher encryption.
        Pads the plain-text using PKCS#7.
        Derives an encryption key using the PBKDF2 key-derivation function.
    """
    # Determine the block-cipher operation mode.
    _opmode = _cipher_opmode(t.opmode)

    # PKCS#7 Padding
    # pad the plaintext to the nearest multiple of block's length.
    padding = CIPHER_BLOCK_BLKSZ_AES - \
        (len(t.plaintext) % CIPHER_BLOCK_BLKSZ_AES)
    padded_plaintext = t.plaintext + bytes([padding] * padding)

    # call the key-derivation function
    t.derived_key = pbkdf2.derive_key(
        t.key, t.key_size, t.pbkdf2_halg, t.pbkdf2_iter, t.salt)

    # Create new AES cipher
    cipher = Crypto.Cipher.AES.new(t.derived_key, _opmode, t.iv)

    # Perform encryption
    # some libraries require the initialization vector to be
    # prepended to the plaintext before encryption.
    #
    # WARNING: prepending the IV before encryption may
    # indirectly transform CBC into ECB mode. The IV
    # is in fact XORed to itself, thus rending the IV
    # void.
    if t.iv_prepend:  # If True, prepend the IV
        ciphertext = cipher.encrypt(bytes(t.iv) + padded_plaintext)
    else:
        ciphertext = cipher.encrypt(padded_plaintext)

    # Encode and return the ciphertext in base64.
    return base64.encode_base64(ciphertext)


def decrypt(t: Toxin):
    """ This function perform AES block cipher decryption.
    """
    # Decode the ciphertext using base64.
    try:
        ciphertext = base64.decode_base64(t.ciphertext)
    except base64.base64.binascii.Error:
        log.error("Cannot decode ciphertext input using base64.")
        raise SystemExit

    # Do basic checks on the decoded ciphertext before continuing.
    if len(ciphertext) < CIPHER_BLOCK_BLKSZ_AES:
        log.error("Invalid AES ciphertext data.")
        raise SystemExit

    # Determine the block-cipher operation mode.
    op_mode = _cipher_opmode(t.opmode)

    # Call the key-derivation function
    t.derived_key = pbkdf2.derive_key(
        t.key, t.key_size, t.pbkdf2_halg, t.pbkdf2_iter, t.salt)

    # Create a new AES cipher
    cipher = Crypto.Cipher.AES.new(t.derived_key, op_mode, t.iv)

    # Perform decryption
    plaintext = cipher.decrypt(ciphertext)

    # If iv-prepending is True truncate the inizialization vector
    # from the returned plaintext.
    if t.iv_prepend:
        plaintext = plaintext[CIPHER_BLOCK_BLKSZ_AES:]

    # Removes the PKCS#7 padding bytes.
    # read the padding length from the plaintext and
    # truncate the plaintext accordingly.
    pad_len = plaintext[-1]
    plaintext = plaintext[:-pad_len]

    # Check plaintext bytes object size.
    # if the length is zero, the parameters were invalid.
    if not len(plaintext):
        log.error(
            "Cannot decrypt provided ciphertext. "
            "Verify the input parameters such as the encryption key "
            "and the operation mode are correct.")
        raise SystemExit

    # return the plaintext
    return plaintext
