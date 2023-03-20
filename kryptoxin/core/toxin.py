"""
kryptoxin toxin module.
This is the toxin module of the kryptoxin project
where the Toxin object type is defined.
"""
from .constants import *
from ..crypto.random import gen_rand_bytes


class Toxin:
    def __init__(self,
                 alg, key, key_size, opmode, iv, salt, pbkdf2_iter,
                 pbkdf2_halg, iv_prepend, plaintext=None, ciphertext=None,
                 random_iv=False, random_salt=False, action=None, uargs=None
                 ):
        """ Toxin type constructor

            Arguments (mandatory):
            alg: Block cipher algorithm
            key: Block cipher encryption key (bytes[])
            key_size: The block cipher algorithm's key size
            opmode: Block cipher mode of operation
            iv: Block cipher initialization vector (bytes[])
            salt: Salt used to enhance hash security (bytes[])
            pbkdf2_iter: Number of iterations for the key-derivation function
            pbkdf2_halg: PBKDF2 HMAC algorithm
            iv_prepend: Prepend Initialization Vector (IV) to the plain-text

            Argument (optional):
            plaintext: The plain-text message
            ciphertext: The encoded ciphertext
            random_iv: Initialization Vector randomization flag (bool)
            random_salt: Salt randamization flag (bool)

        """
        self.alg = alg
        # check if key is a string
        # re-encode to a bytes array if necessary
        if type(key) is str:
            key = bytes(key, 'UTF-8')
        self.key = key
        self.key_size = key_size
        self.opmode = opmode
        # read initialization vector from hex
        if type(iv) is str:
            iv = bytes.fromhex(iv)
        self.iv = iv
        self.random_iv = random_iv
        # if randomization option is Enabled: perform IV randomization
        if self.random_iv is True:
            self.iv = gen_rand_bytes(CIPHER_BLOCK_BLKSZ_AES)
        self.iv_prepend = iv_prepend
        # read salt from hex
        if type(salt) is str:
            salt = bytes.fromhex(salt)
        self.salt = salt
        self.random_salt = random_salt
        # if salt is to be randomized
        if self.random_salt is True:
            self.salt = gen_rand_bytes(CIPHER_BLOCK_BLKSZ_AES)
        self.pbkdf2_iter = pbkdf2_iter
        self.pbkdf2_halg = pbkdf2_halg
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        # derived key
        # automatically generated a random one
        self.derived_key = gen_rand_bytes(int(CIPHER_PBKDF2_AES256_KS / 8))
        # template action
        self.action = action
        # unknown arguments dictionary
        self.uargs = uargs

    def get_dkey_hexstring(self):
        """ This method return the derived in a hex string
        """
        return self.derived_key.hex()

    def get_iv_hexstring(self):
        """ This method return the IV in a hex string
        """
        return self.iv.hex()

    def get_salt_hexstring(self):
        """ This method return the Salt in a hex string
        """
        return self.salt.hex()

    def get_ciphertext(self, lang=None, width=54, tab_width=17, var_name=None):
        """ This method return a formatted ciphertext
        """
        self.ciphertext = str(self.ciphertext, 'UTF-8')

        tab = " " * tab_width
        ciph = ""

        # PowerShell
        if lang == LANG_POWERSHELL and len(self.ciphertext) > width:
            for i in range(0, len(self.ciphertext), width):
                if i > 0:
                    if var_name:
                        ciph += var_name + " += "
                    else:
                        ciph += tab
                ciph += format(f"\"{self.ciphertext[i:i + width]}\"\n")
        # C#
        elif lang == LANG_CSHARP:
            # if not multi lines width
            if len(self.ciphertext) < width:
                return format(f"\"{self.ciphertext}\";")

            for i in range(0, len(self.ciphertext), width):
                # if it's the start of the ciphertext variable
                if i == 0:
                    ciph += "@"
                # handle decoration around the variable construct
                if i > len(self.ciphertext) - width - 1:
                    ciph += tab + \
                        format(f"{self.ciphertext[i:i + width]}\";\n")
                elif i > 0:
                    ciph += tab + format(f"{self.ciphertext[i:i + width]}\n")
                else:
                    ciph += format(f"\"{self.ciphertext[i:i + width]}\n")
        else:
            ciph = format(f"\"{self.ciphertext}\"")

        return ciph
