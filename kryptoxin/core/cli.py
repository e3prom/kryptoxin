"""
kryptoxin CLI Interface module.
This is the cli interface module of the kryptoxin project.
"""
import click
import sys
from . import log
from .constants import *
from ..crypto import aes


# Sub-class of click.Group
class NaturalOrderCommands(click.Group):
    def list_commands(self, ctx):
        """ This function returns commands in a natural order
        """
        return self.commands.keys()


# Local array of click.options for cryptographic parameters options
_cmd_opts_crypto = [
    click.option('-i', '--in', 'input_file', type=click.File("rb"),
                 default=sys.stdin.buffer, nargs=1,
                 help="Input file (e,g. Script, .dll file)",),
    click.option('-o', '--out', 'output_file', type=click.File("wb"),
                 help="Output file"),
    click.option('-a', '--alg',
                 default=CIPHER_DEFAULT_ALGORITHM, show_default=True,
                 type=click.Choice(['AES'], case_sensitive=False),
                 help="Encryption algorithm"),
    click.option('-k', '--key', required=True, help="Encryption key string"),
    click.option('-s', '--key_size',
                 default=CIPHER_DEFAULT_KEYSIZE, show_default=True,
                 type=click.IntRange(0, 4096), help="Encryption key size"),
    click.option('-m', '--mode', 'opmode',
                 default=CIPHER_DEFAULT_BLOCKMODE, show_default=True,
                 type=click.Choice(['CBC', 'CFB'], case_sensitive=False),
                 help="Block Cipher operation mode"),
    click.option('--iv', default=CIPHER_DEFAULT_IV,
                 help="Block Cipher initialization vector (iv)"),
    click.option('--salt', default=CIPHER_DEFAULT_SALT,
                 help="Password hashing algorithm's salt"),
    click.option('-h', '--hmac',
                 default=CIPHER_DEFAULT_HMHASHALG, show_default=True,
                 type=click.Choice(['SHA1', 'SHA256', 'SHA512'],
                                   case_sensitive=False),
                 help="PBKDF2 HMAC algorithm"),
    click.option('--iter', 'pbkdf2_iter',
                 default=CIPHER_DEFAULT_PBKDF2_ITER, show_default=True,
                 type=click.IntRange(0, 1000000),
                 help="PBKDF2 Iteration Count")
]


def _add_cmd_options(options):
    """ This local function returns the built function's options.
    """
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options


@ click.group(cls=NaturalOrderCommands)
@ click.version_option(prog_name=PROGRAM_NAME)
def cli(**kwargs):
    pass


@ cli.command()
@ _add_cmd_options(_cmd_opts_crypto)
def encrypt(
    alg, key, key_size, opmode, iv, salt, hmac,
    input_file, output_file, pbkdf2_iter
):
    """ This command perform encryption on the supplied input.
    It reads on stdin or the file supplied by the '--in' option.
    See Options below for more information.
    """
    # Detect the arguments types and re-encode if necessary.
    # If given as 'str' type perform re-encode using 'UTF-8'.
    if type(key) is str:
        key = bytes(key, 'UTF-8')
    if type(iv) is str:
        iv = bytes(iv, 'UTF-8')
    if type(salt) is str:
        salt = bytes(salt, 'UTF-8')

    # Read provided file and catch errors if any.
    try:
        plaintext = input_file.read()
    except UnicodeDecodeError:
        log.error(
            f"Cannot read input file: {input_file.name}. \
            Make sure it's UTF-8 encoded.")
        raise SystemExit

    # Call encryption function.
    encoded_ciphertext = aes.encrypt(
        plaintext, key, key_size, salt, opmode,
        iv, halg=hmac, pbkdf2_iter=pbkdf2_iter)

    # If output file given, write content (and create file if necessary).
    if output_file:
        output_file.write(encoded_ciphertext)
        output_file.flush()
    else:
        print(f"{str(encoded_ciphertext, 'UTF-8')}")


@ cli.command()
@ _add_cmd_options(_cmd_opts_crypto)
def decrypt(
    alg, key, key_size, opmode, iv, salt, hmac,
    input_file, output_file, pbkdf2_iter
):
    """ This command perform decryption on the supplied input.
    It reads on stdin or the file supplied by the '--in' option.
    See Options below for more information.
    """
    # Detect the arguments types and re-encode if necessary.
    # If given as 'str' type perform re-encode using 'UTF-8'.
    if type(key) is str:
        key = bytes(key, 'UTF-8')
    if type(iv) is str:
        iv = bytes(iv, 'UTF-8')
    if type(salt) is str:
        salt = bytes(salt, 'UTF-8')

    # Read provided file and catch errors if any.
    try:
        ciphertext = input_file.read()
    except UnicodeDecodeError:
        log.error(
            f"Cannot read input file: {input_file.name}. \
            Make sure it's UTF-8 encoded.")
        raise SystemExit

    # Call decryption function.
    plaintext = aes.decrypt(ciphertext, key, key_size, salt, opmode,
                            iv, halg=hmac, pbkdf2_iter=pbkdf2_iter)

    # If output file given, write content (and create file if necessary).
    if output_file:
        output_file.write(plaintext)
        output_file.flush()
    else:
        print(f"{str(plaintext, 'UTF-8')}")


# Add commands to the application CLI.
cli.add_command(encrypt)
cli.add_command(decrypt)
