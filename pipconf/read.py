"""
File containing functions that reads the configuration
files existing in filesystem.
"""
import os

from os import getcwd
from contextlib import suppress
from pipconf.user_paths import UserPath


def configuration_files_filter(filename: str) -> bool:
    """
    Filter function used to get only the configuration
    files in a fixed directory.
    """
    expected_extension = ".conf"
    file_have_expected_extension = filename.endswith(expected_extension)

    return file_have_expected_extension


def get_configuration_files(path: str) -> list:
    """
    Function that obtains all configuration files
    in the directory got as parameter.
    """
    config_files = []

    with suppress(FileNotFoundError):
        directory_files = os.listdir(path)
        config_files_filtered = filter(configuration_files_filter, directory_files)
        config_files = list(config_files_filtered)

    return config_files


def get_user_configurations() -> list:
    """
    Function that obtains all configuration files
    storaged in user's home directory.
    """
    pip_conf_directory = UserPath.PIP_CONFIG_DIRECTORY.value
    config_files = get_configuration_files(pip_conf_directory)

    return config_files
    

def get_local_configurations() -> list:
    """
    Function that obtains the configurations files
    from the current working directory.
    """
    current_directory = getcwd()
    config_files = get_configuration_files(current_directory)

    return config_files