"""
File containing functions that switch between the current
configuration files active in system.
"""
import os

from typing import Union, NoReturn
from contextlib import suppress

from pipconf.user_paths import UserPath


def get_current_configuration() -> Union[str, str]:
    """
    Function that returns the current filename and
    it's absolute path.
    """
    pip_config_path = UserPath.PIP_CONFIG_DIRECTORY.value
    
    relative_path = os.readlink(pip_config_path)
    absolute_path = os.path.realpath(relative_path)
    filename = os.path.basename(absolute_path)

    return filename, absolute_path


def set_current_configuration(config_file_path: str) -> NoReturn:
    """
    Function that change the current configuration file active.
    """
    pip_config_path = UserPath.PIP_CONFIG_DIRECTORY.value
    pip_config_file = pip_config_path + "/pip.conf"
    
    with suppress(FileNotFoundError):
        os.remove(pip_config_file)

    os.symlink(config_file_path, pip_config_file)
