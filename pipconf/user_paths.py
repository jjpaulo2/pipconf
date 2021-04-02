from enum import Enum
from pathlib import Path


class UserPath(Enum):
    """
    Enumeration containing all directory related to the
    active user.
    """

    HOME_DIRECTORY = str(Path.home())
    PIP_CONFIG_DIRECTORY = HOME_DIRECTORY + "/.pip"
    PIP_CONFIG_DEFAULT_FILE = PIP_CONFIG_DIRECTORY + "/pip.conf"
