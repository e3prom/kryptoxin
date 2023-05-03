"""
kryptoxin CLI Interface module.
This is the cli interface module of the kryptoxin project.
"""
import click
import sys
from kryptoxin.core.log import log
from kryptoxin.core.toxin import Toxin
from kryptoxin.core.constants import CIPHER_AES, CIPHER_CAESAR
from kryptoxin.core.constants import CIPHER_DEFAULT_ALGORITHM
from kryptoxin.core.constants import CIPHER_DEFAULT_KEYSIZE
from kryptoxin.core.constants import CIPHER_DEFAULT_BLOCKMODE
from kryptoxin.core.constants import CIPHER_DEFAULT_IV
from kryptoxin.core.constants import CIPHER_DEFAULT_SALT
from kryptoxin.core.constants import CIPHER_DEFAULT_HMHASHALG
from kryptoxin.core.constants import CIPHER_DEFAULT_PBKDF2_ITER
from kryptoxin.core.constants import CIPHER_DEFAULT_RANDOMIV
from kryptoxin.core.constants import CIPHER_DEFAULT_IV_PREPEND
from kryptoxin.core.constants import PROGRAM_NAME, CLI_DISPLAYKEY
from kryptoxin.core.constants import LANG_CSHARP, LANG_POWERSHELL
from kryptoxin.core.constants import LANG_VBA
from kryptoxin.crypto import aes, base64, caesar
from kryptoxin.output import unformatted, powershell, csharp, vba

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
                 type=click.Choice(
                     [CIPHER_AES, CIPHER_CAESAR], case_sensitive=False),
                 help="Encryption algorithm"),
    click.option('-k', '--key', required=True, help="Encryption key string"),
    click.option('-s', '--key_size',
                 default=CIPHER_DEFAULT_KEYSIZE, show_default=True,
                 type=click.IntRange(0, 4096), help="Encryption key size"),
    click.option('-m', '--mode', 'opmode',
                 default=CIPHER_DEFAULT_BLOCKMODE, show_default=True,
                 type=click.Choice(['CBC', 'CFB', 'OFB', 'EAX'],
                                   case_sensitive=False),
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
                 default=CIPHER_DEFAULT_PBKDF2_ITER,
                 show_default=True,
                 type=click.IntRange(0, 1000000),
                 help="PBKDF2 iteration count")
]


def _add_cmd_options(options):
    """ This local function return the built function's options.
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


@click.command(context_settings=dict(
    ignore_unknown_options=True, allow_extra_args=True
))
@ _add_cmd_options(_cmd_opts_crypto)
@click.option('--random-iv/--static-iv',
              default=CIPHER_DEFAULT_RANDOMIV,
              help="Use a randomized or an all-zeros IV")
@click.option('--random-salt/--static-salt',
              default=CIPHER_DEFAULT_RANDOMIV,
              help="Use a randomized or an all-zeros Salt")
@click.option('-l', '--lang',
              type=click.Choice(['powershell', 'csharp', 'vba'],
                                case_sensitive=False),
              help="Output programming language")
@click.option('-a', '--action', help="Action to perform (e,g. print)")
@click.option('--show-key/--hide-key', default=CLI_DISPLAYKEY,
              help="Display the generated key")
@click.pass_context
def encrypt(ctx, alg, key, key_size, opmode, iv, random_iv, salt, random_salt,
            hmac, input_file, output_file, pbkdf2_iter, lang, action,
            show_key):
    """ This command perform encryption on the supplied input.
    It reads on stdin or the file supplied by the '--in' option.
    See Options below for more information.
    """
    # build a directory for unknown arguments
    try:
        uargs = dict([arg.strip('--').split('=') for arg in ctx.args])
    except ValueError:
        log.error(f"Unknown argument(s) given {ctx.args}.")
        raise SystemExit

    # Read provided file and catch errors if any.
    try:
        plaintext = input_file.read()
    except UnicodeDecodeError:
        log.error(
            f"Cannot read input file: {input_file.name}. \
            Make sure it's UTF-8 encoded.")
        raise SystemExit

    # Create Toxin object
    tx = Toxin(alg, key, key_size, opmode, iv, salt, pbkdf2_iter,
               hmac, CIPHER_DEFAULT_IV_PREPEND, plaintext=plaintext,
               random_iv=random_iv, random_salt=random_salt,
               action=action, uargs=uargs)

    # Call encryption function(s).
    # AES - Advanced Encryption Standard
    if alg == CIPHER_AES:
        tx.ciphertext = aes.encrypt(tx)

        # If given or generated key is to be displayed.
        if show_key:
            log.info(f"The AES encryption key is: {tx.get_dkey_hexstring()}")

        # If IV / Salt randmization is enabled, output the value in hex.
        if tx.random_iv:
            log.info(
                f"The Initialization Vector (IV) is: {tx.get_iv_hexstring()}")
        if tx.random_salt:
            log.info(f"The PBKDF2 Salt is: {tx.get_salt_hexstring()}")
    # CAESAR
    elif alg == CIPHER_CAESAR:
        # check key validiting
        if int(key) in range(0, 255):
            tx.ciphertext = caesar.encrypt(tx, key=int(key))
        else:
            log.error("Please specify a Caasar cipher key between 1 and 255.")
            raise SystemExit
    # UNDEFINED ALG
    else:
        log.error(f"Invalid encryption algorithm {alg}.", alg)
        raise SystemExit

    # TEMPLATES HANDLING
    # PowerShell
    if lang == LANG_POWERSHELL:
        if action in powershell.actions:
            output = bytes((powershell.actions[action](tx)), 'UTF-8')
        elif action is None:
            log.error("Please specify a PowerShell script action.")
            raise SystemExit
        else:
            log.error(f"Unknown PowerShell template action '{action}'.")
            raise SystemExit
    # C#
    elif lang == LANG_CSHARP:
        if action in csharp.actions:
            output = bytes((csharp.actions[action](tx)), 'UTF-8')
        elif action is None:
            log.error("Please specify a C# program action.")
            raise SystemExit
        else:
            log.error(f"Unknown C# template action '{action}'.")
            raise SystemExit
    # VBA
    elif lang == LANG_VBA:
        if action in vba.actions:
            output = bytes((vba.actions[action](tx)), 'UTF-8')
        elif action is None:
            log.error("Please specify a CBA script action.")
            raise SystemExit
        else:
            log.error(f"Unknown VBA template action '{action}'.")
            raise SystemExit
    # NO TEMPLATE / UNDEFINED
    else:
        if alg == CIPHER_AES:
            output = base64.encode_base64(tx.ciphertext)
        elif alg == CIPHER_CAESAR:
            output = base64.encode_base64(tx.ciphertext)
        else:
            output = bytes(tx.get_ciphertext(), 'UTF-8')

    # If output file given, write content (and create file if necessary).
    if output_file:
        output_file.write(unformatted.binary(output))
        output_file.flush()
    else:
        print(unformatted.plain(output))


@ cli.command()
@ _add_cmd_options(_cmd_opts_crypto)
def decrypt(alg, key, key_size, opmode, iv, salt, hmac,
            input_file, output_file, pbkdf2_iter):
    """ This command perform decryption on the supplied input.
    It reads on stdin or the file supplied by the '--in' option.
    See Options below for more information.
    """
    # Read provided file and catch errors if any.
    try:
        ciphertext = input_file.read()
    except UnicodeDecodeError:
        log.error(
            f"Cannot read input file: {input_file.name}. \
            Make sure it's UTF-8 encoded.")
        raise SystemExit

    # Create Toxin object
    tx = Toxin(alg, key, key_size, opmode, iv, salt, pbkdf2_iter,
               hmac, CIPHER_DEFAULT_IV_PREPEND,
               ciphertext=ciphertext)

    # prepare output
    output = ""

    # AES
    if alg == CIPHER_AES:
        tx.plaintext = aes.decrypt(tx)
        output = tx.plaintext
    # CAESAR
    elif alg == CIPHER_CAESAR:
        # check key validiting
        if int(key) in range(0, 255):
            tx.plaintext = caesar.decrypt(tx, key=int(key))
            output = tx.plaintext
        else:
            log.error("Please specify a Caasar cipher key between 1 and 255.")
            raise SystemExit
    else:
        log.error(f"Invalid encryption algorithm {alg}.", alg)
        raise SystemExit

    # If output file given, write content (and create file if necessary).
    if output_file:
        output_file.write(unformatted.binary(output))
        output_file.flush()
    else:
        print(unformatted.plain(output))


# Add commands to the application CLI.
cli.add_command(encrypt)
cli.add_command(decrypt)
