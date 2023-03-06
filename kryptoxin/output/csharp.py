"""
kryptoxin C# output module.
This module contains functions for the C# outputs
"""
from ..core.toxin import Toxin
from ..core.constants import JINJA_TEMPLATES_CSHARP, JINJA_TEMPLATES_ACTSDIR, \
    JINA_TEMPLATES_FEXT
from . import get_jinja_env

# Create Jinja2 environment variable
env = get_jinja_env()

# Actions templates directories string
tmpl_action_rpath = JINJA_TEMPLATES_CSHARP + JINJA_TEMPLATES_ACTSDIR


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
    _iv = t.get_iv_hexstring()
    _salt = t.get_salt_hexstring()

    template = env.get_template(
        tmpl_action_rpath + "print" + JINA_TEMPLATES_FEXT)

    return template.render(ciphertext=_ciphertext, mode=t.opmode,
                           password=_password, iv=_iv, salt=_salt,
                           iter=t.pbkdf2_iter, hmac=t.pbkdf2_halg,
                           key_size=t.key_size)


# functions mapping
actions = {
    "print": render_print
}
