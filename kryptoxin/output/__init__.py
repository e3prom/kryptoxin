"""
kryptoxin output module.
This is the ouput module of the kryptoxin project.
"""
from kryptoxin import ROOT_DIR
from ..core.constants import JINJA_TEMPLATES_DIR
import jinja2


def get_jinja_env() -> jinja2.Environment:
    """ Return the Jinja2 Environment
    """
    return create_jinja_env()


def create_jinja_env() -> jinja2.Environment:
    """ Create the Jinja2 Environment
    """
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(ROOT_DIR + "/" + JINJA_TEMPLATES_DIR))
    return env
