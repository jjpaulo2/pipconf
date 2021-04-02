"""
File containing the front-end functions that comunicates with
the read and switch modules.
"""
import os

from typing import Tuple, NoReturn
from contextlib import suppress

from pipconf import read
from pipconf import switch
from pipconf.user_paths import UserPath


def get_user_configurations() -> Tuple[list, list]:
    """
    Function that reads the $HOME/.pip folder and return two lists, 
    containing filenames and absolute path from them.
    """
    pip_config_path = UserPath.PIP_CONFIG_DIRECTORY.value

    config_filenames = read.get_user_configuration_files()
    config_filepaths = [pip_config_path + "/" + filename for filename in config_filenames]

    return config_filenames, config_filepaths


def print_user_configurations() -> NoReturn:
    """
    Function that prints the list of user's configuration files.
    """
    config_filenames, config_files = get_user_configurations()
    quant_files = len(config_files)

    current_config_filename, current_config_filepath = switch.get_current_configuration()

    print()
    for i in range(quant_files):
        filename = config_filenames[i][:-5]
        filepath = config_files[i]

        current_start = " "
        current_end = ""

        if current_config_filepath == filepath:
            current_start = "\033[93m*"
            current_end = "\033[0m"

        print(f"{current_start} {filename} ({filepath}) {current_end}")


def print_current_configuration() -> NoReturn:
    """
    Function that shows the current configuration file used
    by the active user.
    """
    filename, filepath = switch.get_current_configuration()

    print()
    if filepath:
        print(f"  The current pip configuration file is \033[93m{filepath}\033[0m")

    else:
        print("  No configuration file defined.")


def set_user_configuration(filename: str) -> NoReturn:
    """
    Function that set the user configuration file to $HOME/{filename}.
    """
    pip_config_path = UserPath.PIP_CONFIG_DIRECTORY.value
    new_config_filepath = pip_config_path + "/" + filename + ".conf"

    switch.set_current_configuration(new_config_filepath)

    print()
    print("  Current pip configuration successfully updated.")
    print(f"  The active config file is \033[93m{new_config_filepath}\033[0m")


def set_local_configuration() -> NoReturn:
    """
    Function that sets the current configuration file to a
    `pip.conf` file storaged in the current working directory.
    """
    local_config_files = read.get_local_configuration_files()
    expected_local_config_filename = "pip.conf"

    print()
    print("  Geting configuration file from current directory.")

    if expected_local_config_filename in local_config_files:
        current_directory = os.getcwd()
        new_config_filepath = current_directory + "/" + expected_local_config_filename

        switch.set_current_configuration(new_config_filepath)
        print(f"  The active config file is \033[93m{new_config_filepath}\033[0m")

    else:
        print("  Not found \033[91mpip.conf\033[0m file in this folder.")
    
