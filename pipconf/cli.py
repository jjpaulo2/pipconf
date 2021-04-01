import argparse

from typing import NoReturn
from pipconf import __version__


NAME = "pipconf"
VERSION = __version__
DESCRIPTION = """
______ ___________  _____ _____ _   _ ______ 
| ___ \_   _| ___ \/  __ \  _  | \ | ||  ___|
| |_/ / | | | |_/ /| /  \/ | | |  \| || |_   
|  __/  | | |  __/ | |   | | | | . ` ||  _|  
| |    _| |_| |    | \__/\ \_/ / |\  || |    
\_|    \___/\_|     \____/\___/\_| \_/\_|  v{}

Under BSD-2-Clause License, by @jjpaulo2
Contribute at https://github.com/jjpaulo2/pipconf
""".format(VERSION)


def main() -> NoReturn:
    parser = argparse.ArgumentParser(
        prog=NAME,
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter
    )
    actions = parser.add_argument_group("avaliable actions")

    actions.add_argument("--list", action="store_true", help="list all user configurations avaliable at $HOME/.pip")
    actions.add_argument("--set", type=str, help="set the global configuration for pip")

    args = parser.parse_args()


if __name__ == "__main__":
    main()