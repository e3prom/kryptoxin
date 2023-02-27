"""
kryptoxin Constants module.
This module defines the various program-wide constants.
"""

PROGRAM_NAME = 'Kryptoxin'
# Cipher Parameters- Defaults
CIPHER_DEFAULT_ALGORITHM = "aes"    # Default encryption algorithm
CIPHER_DEFAULT_KEYSIZE = 256        # Default block cipher key-size
CIPHER_DEFAULT_BLOCKMODE = "cbc"    # Default block cipher operation mode
CIPHER_DEFAULT_HMHASHALG = "sha1"   # Default HMAC (.NET compat.)
CIPHER_DEFAULT_PBKDF2_ITER = 10000  # PBKDF2 number of iterations
CIPHER_DEFAULT_PBKDF2_DKLEN = 32    # PBKDF2 HMAC digest length
CIPHER_DEFAULT_IV_PREPEND = True    # Prepend IV to plain-text
# AE6 Cipher Block size (bytes)
CIPHER_BLOCK_BLKSZ_AES = 16         # AES Block Size - 128-bits
# PBKDF2 Key Sizes (bytes)
CIPHER_PBKDF2_AES128_KS = 16
CIPHER_PBKDF2_AES192_KS = 24
CIPHER_PBKDF2_AES256_KS = 32
# Default Salt (all-zeros)
CIPHER_DEFAULT_SALT = bytes(CIPHER_BLOCK_BLKSZ_AES)
# Default Block Cipher's Initialization Vector (IV)
CIPHER_DEFAULT_IV = bytes(CIPHER_BLOCK_BLKSZ_AES)
# Block Cipher Operation mode
CIPHER_BLOCK_OPERMODE_CBC = "cbc"
CIPHER_BLOCK_OPERMODE_CFB = "cfb"
CIPHER_BLOCK_OPERMODE_OFB = "ofb"
CIPHER_BLOCK_OPERMODE_EAX = "eax"
