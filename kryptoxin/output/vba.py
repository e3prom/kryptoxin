"""
kryptoxin VBA output module.
This module contains functions for the visual basic outputs
"""
from kryptoxin.core.toxin import Toxin
from kryptoxin.core.constants import JINJA_TEMPLATES_VBA
from kryptoxin.core.constants import JINJA_TEMPLATES_ACTSDIR
from kryptoxin.core.constants import JINA_TEMPLATES_FEXT, LANG_VBA
from kryptoxin.output import get_jinja_env

# Create Jinja2 environment variable
env = get_jinja_env()

# Actions templates directories string
tmpl_action_rpath = JINJA_TEMPLATES_VBA + JINJA_TEMPLATES_ACTSDIR


# def render_custom(t: Toxin):
#     """ This function return the C# custom program or library.

#     Arguments:
#      - ciphertext: the base64 encoded ciphertext (bytes[])
#      - password: the password or key (bytes[])
#     """
#     # cast ciphertext to string
#     _ciphertext = t.get_ciphertext(lang=LANG_CSHARP, tab_width=29)
#     _password = str(t.key, 'UTF-8')
#     _iv = t.get_iv_hexstring()
#     _salt = t.get_salt_hexstring()

#     template = env.get_template(
#         tmpl_action_rpath + "custom" + JINA_TEMPLATES_FEXT)

#     return template.render(ciphertext=_ciphertext, mode=t.opmode,
#                            password=_password, iv=_iv, salt=_salt,
#                            iter=t.pbkdf2_iter, hmac=t.pbkdf2_halg,
#                            key_size=t.key_size, action=t.action,
#                            args=t.uargs)


def render_print(t: Toxin):
    """ This function return a VBA print console script.
        It simply prints the decrypted plaintext to the console.

    Arguments:
     - ciphertext: the base64 encoded ciphertext (bytes[])
     - password: the password or key (bytes[])
    """
    # cast ciphertext to string
    _ciphertext = t.get_ciphertext(lang=LANG_VBA, width=50)
    _password = str(t.key, 'UTF-8')
    _iv = fmt_vbadarray(t.get_iv_decarray())
    _salt = fmt_vbadarray(t.get_salt_decarray())

    template = env.get_template(
        tmpl_action_rpath + "print" + JINA_TEMPLATES_FEXT)

    return template.render(int=int, ciphertext=_ciphertext, mode=t.opmode,
                           password=_password, iv=_iv, salt=_salt,
                           iter=t.pbkdf2_iter, hmac=t.pbkdf2_halg,
                           key_size=t.key_size, action=t.action)


def fmt_vbadarray(darray):
    """ This function convert a decimal byte array to a
        VBA compatible format.
    """
    _darray = "".join("{}, ".format(d) for d in darray)[:-2]

    return _darray


# functions mapping
actions = {
    "print": render_print
}
