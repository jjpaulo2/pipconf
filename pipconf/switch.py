"""
File containing functions that switch between the current
configuration files active in system.
"""
import os

from typing import Tuple, NoReturn
from contextlib import suppress

from pipconf.user_paths import UserPath


def get_current_configuration() -> Tuple[str, str]:
    """
    Function that returns the current filename and
    it's absolute path.

    Returns:
        filename, absolute_path
    """
    pip_config_default_file = UserPath.PIP_CONFIG_DEFAULT_FILE.value
    
    filename = None
    absolute_path = None

    with suppress(FileNotFoundError):
        absolute_path = os.path.realpath(pip_config_default_file)
        filename = os.path.basename(pip_config_default_file)

    return filename, absolute_path


def remove_current_configuration() -> NoReturn:
    """
    Function tha removes the configuration link,
    if it exists.
    """
    pip_config_path = UserPath.PIP_CONFIG_DIRECTORY.value
    pip_config_file = pip_config_path + "/pip.conf"

    with suppress(FileNotFoundError):
        os.remove(pip_config_file)


def set_current_configuration(config_file_path: str) -> NoReturn:
    """
    Function that change the current configuration file active.
    """
    pip_config_path = UserPath.PIP_CONFIG_DIRECTORY.value
    pip_config_file = pip_config_path + "/pip.conf"
    
    remove_current_configuration()
    os.symlink(config_file_path, pip_config_file)
