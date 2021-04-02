"""
File containing functions that prepare the environment.
"""

import os

from typing import NoReturn
from pipconf.user_paths import UserPath

def initialize_environment() -> NoReturn:
    """
    Initialize the environment variables.
    """
    os.environ["PIP_CONFIG_FILE"] = UserPath.PIP_CONFIG_DEFAULT_FILE.value
