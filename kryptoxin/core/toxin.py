"""
kryptoxin toxin module.
This is the toxin module of the kryptoxin project
where the Toxin object type is defined.
"""
from kryptoxin.core.constants import CIPHER_BLOCK_BLKSZ_AES
from kryptoxin.core.constants import CIPHER_PBKDF2_AES256_KS
from kryptoxin.core.constants import LANG_POWERSHELL, LANG_CSHARP
from kryptoxin.core.constants import LANG_VBA
from kryptoxin.crypto.random import gen_rand_bytes
from kryptoxin.crypto.base64 import encode_base64
from kryptoxin.core.conv import bytes2decarray


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
        # base64 output
        self.base64 = False

    def get_dkey_hexstring(self):
        """ This method return the derived in a hex string
        """
        return self.derived_key.hex()

    def get_iv_hexstring(self):
        """ This method return the IV in a hex string
        """
        return self.iv.hex()

    def get_iv_decarray(self):
        """ This method return the Salt in a decimal array
        """
        return bytes2decarray(self.iv)

    def get_salt_hexstring(self):
        """ This method return the Salt in a hex string
        """
        return self.salt.hex()

    def get_salt_decarray(self):
        """ This method return the Salt in a decimal array
        """
        return bytes2decarray(self.salt)

    def get_ciphertext(self, lang=None, width=54, tab_width=17, var_name=None):
        """ This method return a formatted ciphertext
        """
        tab = " " * tab_width
        ciph = ""

        # PowerShell
        if lang == LANG_POWERSHELL:
            _ciphertext = str(encode_base64(self.ciphertext), 'UTF-8')
            if len(_ciphertext) > width:
                for i in range(0, len(_ciphertext), width):
                    if i > 0:
                        if var_name:
                            ciph += var_name + " += "
                        else:
                            ciph += tab
                    ciph += format(f"\"{_ciphertext[i:i + width]}\"\n")
        # C#
        elif lang == LANG_CSHARP:
            _ciphertext = str(encode_base64(self.ciphertext), 'UTF-8')
            # if not multi lines width
            if len(_ciphertext) < width:
                return format(f"\"{_ciphertext}\";")

            for i in range(0, len(_ciphertext), width):
                # if it's the start of the ciphertext variable
                if i == 0:
                    ciph += "@"
                # handle decoration around the variable construct
                if i > len(_ciphertext) - width - 1:
                    ciph += tab + \
                        format(f"{_ciphertext[i:i + width]}\";\n")
                elif i > 0:
                    ciph += tab + format(f"{_ciphertext[i:i + width]}\n")
                else:
                    ciph += format(f"\"{_ciphertext[i:i + width]}\n")
        # VBA
        elif lang == LANG_VBA:
            _ciphertext = bytes2decarray(self.ciphertext)
            for i, d in enumerate(_ciphertext):
                if i == 0:
                    ciph += format(f"{d}, ")
                elif i % width == 0:
                    ciph += format(f"{d}, _\n")
                elif i == len(_ciphertext)-1:
                    ciph += format(f"{d}")
                else:
                    ciph += format(f"{d}, ")

        # Plain / Others
        else:
            ciph = format(f"\"{self.ciphertext}\"")

        # return built ciph variable
        return ciph
