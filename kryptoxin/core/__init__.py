"""
kryptoxin core module.
This is the core module of the kryptoxin project.
"""
import logging


def _init_logger():
    """ This local function setup the application logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')


_init_logger()
log = logging.getLogger(__name__)


# Constants - Defaults
CIPHER_DEFAULT_ALGORITHM = 'AES'    # Default encryption algorithm
CIPHER_DEFAULT_KEYSIZE = 256        # Default block cipher key-size
CIPHER_DEFAULT_BLOCKMODE = 'CBC'    # Default block cipher operation mode
CIPHER_DEFAULT_HMHASHALG = 'SHA1'   # Default HMAC (.NET compat.)
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
CIPHER_BLOCK_OPERMODE_CBC = 'CBC'
CIPHER_BLOCK_OPERMODE_CFB = 'CFB'
CIPHER_BLOCK_OPERMODE_OFB = 'OFB'
CIPHER_BLOCK_OPERMODE_EAX = 'EAX'
# Test Constants
TEST_TXTFILE_PATH = 'tests/samples/input_file.txt'
