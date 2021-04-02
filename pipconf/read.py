"""
File containing functions that reads the configuration
files existing in filesystem.
"""
import os

from contextlib import suppress
from pipconf.user_paths import UserPath


def configuration_files_filter(filename: str) -> bool:
    """
    Filter function used to get only the configuration
    files in a fixed directory.

    Returns:
        file_have_expected_extension
    """
    expected_extension = ".conf"
    file_have_expected_extension = filename.endswith(expected_extension)

    return file_have_expected_extension


def get_configuration_files(path: str) -> list:
    """
    Function that obtains all configuration files
    in the directory got as parameter.

    Returns:
        config_files
    """
    config_files = []

    with suppress(FileNotFoundError):
        directory_files = os.listdir(path)
        config_files_filtered = filter(configuration_files_filter, directory_files)
        config_files = list(config_files_filtered)

    return config_files


def get_user_configuration_files() -> list:
    """
    Function that obtains all configuration files
    storaged in user's home directory.

    Returns:
        config_files
    """
    pip_conf_directory = UserPath.PIP_CONFIG_DIRECTORY.value
    config_link_filename = "pip.conf"
    
    config_files = get_configuration_files(pip_conf_directory)
    
    if config_link_filename in config_files:
        config_files.remove(config_link_filename)

    return config_files
    

def get_local_configuration_files() -> list:
    """
    Function that obtains the configurations files
    from the current working directory.

    Returns:
        config_files
    """
    current_directory = os.getcwd()
    config_files = get_configuration_files(current_directory)

    return config_files
