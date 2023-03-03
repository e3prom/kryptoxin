"""
kryptoxin log module.
This is the log module of the kryptoxin project.
"""
import logging


def _init_logger():
    """ This local function setup the application logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')


_init_logger()
log = logging.getLogger(__name__)
