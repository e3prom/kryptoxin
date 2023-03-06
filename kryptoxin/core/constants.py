"""
kryptoxin Constants module.
This module defines the various program-wide constants.
"""

# Program constants
PROGRAM_NAME = 'Kryptoxin'
# CLI parameters
CLI_DISPLAYKEY = False                   # Display generated key on the console
# Cipher Parameters- Defaults
CIPHER_DEFAULT_ALGORITHM = "aes"        # Default encryption algorithm
CIPHER_DEFAULT_KEYSIZE = 256            # Default block cipher key-size
CIPHER_DEFAULT_BLOCKMODE = "cbc"        # Default block cipher operation mode
CIPHER_DEFAULT_HMHASHALG = "sha1"       # Default HMAC (.NET compat.)
CIPHER_DEFAULT_PBKDF2_ITER = 10000      # PBKDF2 number of iterations
CIPHER_DEFAULT_PBKDF2_DKLEN = 32        # PBKDF2 HMAC digest length
CIPHER_DEFAULT_IV_PREPEND = False       # Prepend IV to plain-text
CIPHER_DEFAULT_RANDOMIV = False         # IV randomization option
# AE6 Cipher Block size (bytes)
CIPHER_BLOCK_BLKSZ_AES = 16             # AES Block Size - 128-bits
# PBKDF2 Key Sizes (bytes)
CIPHER_PBKDF2_AES128_KS = 16
CIPHER_PBKDF2_AES192_KS = 24
CIPHER_PBKDF2_AES256_KS = 32
# Default Salt (all-zeros)
CIPHER_DEFAULT_SALT = "0" * (CIPHER_BLOCK_BLKSZ_AES * 2)
# Default Block Cipher's Initialization Vector (IV)
CIPHER_DEFAULT_IV = "0" * (CIPHER_BLOCK_BLKSZ_AES * 2)
# Block Cipher Operation mode
CIPHER_BLOCK_OPERMODE_CBC = "cbc"       # Cipher Block Chaining
CIPHER_BLOCK_OPERMODE_CFB = "cfb"       # Cipher Feedback
CIPHER_BLOCK_OPERMODE_OFB = "ofb"       # Output Feedback
CIPHER_BLOCK_OPERMODE_EAX = "eax"       # Encrypt-Authenticate-Translate
# Languages
LANG_POWERSHELL = "powershell"          # PowerShell cmd-line option string
LANG_CSHARP = "csharp"                  # C# cmd-line option string
# Jinja Templates
JINJA_TEMPLATES_DIR = "templates/"      # Jinja2 template directory
JINJA_TEMPLATES_PS = "powershell/"      # PowerShell templates directory
JINJA_TEMPLATES_CSHARP = "csharp/"      # C# templates directory
JINJA_TEMPLATES_ACTSDIR = "actions/"    # Actions templates directory
JINA_TEMPLATES_FEXT = ".jinja"          # Jinja2 templates files extension
