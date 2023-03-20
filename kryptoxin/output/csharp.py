"""
kryptoxin C# output module.
This module contains functions for the C# outputs
"""
from ..core.toxin import Toxin
from ..core.constants import JINJA_TEMPLATES_CSHARP, JINJA_TEMPLATES_ACTSDIR, \
    JINA_TEMPLATES_FEXT, LANG_CSHARP
from . import get_jinja_env

# Create Jinja2 environment variable
env = get_jinja_env()

# Actions templates directories string
tmpl_action_rpath = JINJA_TEMPLATES_CSHARP + JINJA_TEMPLATES_ACTSDIR


def render_custom(t: Toxin):
    """ This function return the C# custom program or library.

    Arguments:
     - ciphertext: the base64 encoded ciphertext (bytes[])
     - password: the password or key (bytes[])
    """
    # cast ciphertext to string
    _ciphertext = t.get_ciphertext(lang=LANG_CSHARP, tab_width=29)
    _password = str(t.key, 'UTF-8')
    _iv = t.get_iv_hexstring()
    _salt = t.get_salt_hexstring()

    template = env.get_template(
        tmpl_action_rpath + "custom" + JINA_TEMPLATES_FEXT)

    return template.render(ciphertext=_ciphertext, mode=t.opmode,
                           password=_password, iv=_iv, salt=_salt,
                           iter=t.pbkdf2_iter, hmac=t.pbkdf2_halg,
                           key_size=t.key_size, action=t.action,
                           args=t.uargs)


def render_print(t: Toxin):
    """ This function return a C# print console program.
        It simply prints the decrypted plaintext to the console.

    Arguments:
     - ciphertext: the base64 encoded ciphertext (bytes[])
     - password: the password or key (bytes[])
    """
    # cast ciphertext to string
    _ciphertext = t.get_ciphertext(
        lang=LANG_CSHARP, var_name="string encryptedMessage", tab_width=36)
    _password = str(t.key, 'UTF-8')
    _iv = t.get_iv_hexstring()
    _salt = t.get_salt_hexstring()

    template = env.get_template(
        tmpl_action_rpath + "print" + JINA_TEMPLATES_FEXT)

    return template.render(ciphertext=_ciphertext, mode=t.opmode,
                           password=_password, iv=_iv, salt=_salt,
                           iter=t.pbkdf2_iter, hmac=t.pbkdf2_halg,
                           key_size=t.key_size, action=t.action)


def render_load_lib(t: Toxin):
    """ This function return a C# load-dll console program.
        It writes a decrypted DLL to disk and then load it.

    Arguments:
     - ciphertext: the base64 encoded ciphertext (bytes[])
     - password: the password or key (bytes[])
    """
    # cast ciphertext to string
    _ciphertext = t.get_ciphertext(
        lang=LANG_CSHARP, var_name="string encryptedMessage", tab_width=30)
    _password = str(t.key, 'UTF-8')
    _iv = t.get_iv_hexstring()
    _salt = t.get_salt_hexstring()

    template = env.get_template(
        tmpl_action_rpath + "load-library" + JINA_TEMPLATES_FEXT)

    return template.render(ciphertext=_ciphertext, mode=t.opmode,
                           password=_password, iv=_iv, salt=_salt,
                           iter=t.pbkdf2_iter, hmac=t.pbkdf2_halg,
                           key_size=t.key_size, action=t.action,
                           args=t.uargs)


# functions mapping
actions = {
    "custom": render_custom,
    "print": render_print,
    "load-library": render_load_lib,
    "load-dll": render_load_lib
}
