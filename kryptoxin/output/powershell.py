"""
kryptoxin powershell output module.
This module contains functions for the powershell outputs
"""
from ..core.toxin import Toxin
from ..core.constants import JINJA_TEMPLATES_PS, JINJA_TEMPLATES_ACTSDIR, \
    JINA_TEMPLATES_FEXT
from . import get_jinja_env

# Create Jinja2 environment variable
env = get_jinja_env()

# Actions templates directories string
tmpl_action_rpath = JINJA_TEMPLATES_PS + JINJA_TEMPLATES_ACTSDIR


def gen_compat_hexstring(array):
    """ This function generate a hexadecimal string of bytes
        compatible with PowerShell scripts.
    """
    return ", ".join('0x' + format(x, "02X") for x in array)


def render_custom(t: Toxin):
    """ This function return the PowerShell custom script.

    Arguments:
     - ciphertext: the base64 encoded ciphertext (bytes[])
     - password: the password or key (bytes[])
    """
    # cast ciphertext to string
    _ciphertext = str(t.ciphertext, 'UTF-8')
    _password = str(t.key, 'UTF-8')
    _iv = gen_compat_hexstring(t.iv)
    _salt = gen_compat_hexstring(t.salt)

    template = env.get_template(
        tmpl_action_rpath + "custom" + JINA_TEMPLATES_FEXT)

    return template.render(ciphertext=_ciphertext, mode=t.opmode,
                           password=_password, iv=_iv, salt=_salt,
                           iter=t.pbkdf2_iter, hmac=t.pbkdf2_halg,
                           key_size=t.key_size)


def render_print(t: Toxin):
    """ This function return a PowerShell print script.
        It simply prints the decrypted plaintext to the console.

    Arguments:
     - ciphertext: the base64 encoded ciphertext (bytes[])
     - password: the password or key (bytes[])
    """
    # cast ciphertext to string
    _ciphertext = str(t.ciphertext, 'UTF-8')
    _password = str(t.key, 'UTF-8')
    _iv = gen_compat_hexstring(t.iv)
    _salt = gen_compat_hexstring(t.salt)

    template = env.get_template(
        tmpl_action_rpath + "print" + JINA_TEMPLATES_FEXT)

    return template.render(ciphertext=_ciphertext, mode=t.opmode,
                           password=_password, iv=_iv, salt=_salt,
                           iter=t.pbkdf2_iter, hmac=t.pbkdf2_halg,
                           key_size=t.key_size)


# functions mapping
actions = {
    "custom": render_custom,
    "print": render_print,
}
