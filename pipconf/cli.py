import argparse

from typing import NoReturn

from pipconf import __version__
from pipconf import __module__
from pipconf import __license__
from pipconf import __author_github__
from pipconf import __index__

from pipconf import kernel 
from pipconf import environment


NAME = __module__
VERSION = __version__
LICENSE = __license__
AUTHOR = __author_github__
INDEX = __index__
DESCRIPTION = """
\033[93m______ ___________  _____ _____ _   _ ______ \033[0m
\033[93m| ___ \_   _| ___ \/  __ \  _  | \ | ||  ___|\033[0m
\033[93m| |_/ / | | | |_/ /| /  \/ | | |  \| || |_ \033[0m
\033[93m|  __/  | | |  __/ | |   | | | | . ` ||  _|\033[0m
\033[93m| |    _| |_| |    | \__/\ \_/ / |\  || |\033[0m
\033[93m\_|    \___/\_|     \____/\___/\_| \_/\_|\033[0m  v{}

Under {} License, by {}
Contribute at {}
""".format(VERSION, LICENSE, AUTHOR, INDEX)


def init_argparse() -> argparse.ArgumentParser:
    """
    Function that initializes the `ArgumentParser` and returns it.
    """
    parser = argparse.ArgumentParser(
        prog=NAME,
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-v", "--version", action="store_true", help="show the version of the module")

    display = parser.add_argument_group("display informations")
    display.add_argument("--current", action="store_true", help="show the current pip configuration file")
    display.add_argument("--list", action="store_true", help="list all user configurations avaliable at $HOME/.pip")
    
    change = parser.add_argument_group("change configuration")
    change.add_argument("--set", type=str, dest="filename", help="set the global configuration for pip from a file in $HOME/.pip")
    change.add_argument("--local", action="store_true", help="set the pip configuration for the current directory file")

    return parser


def handle_arguments(args) -> NoReturn:
    """
    Function that verify all cli arguments and handle it.
    """

    # Module version
    if args.version:
        # --version
        print(f"{NAME} {VERSION}")

    # Display arguments
    if args.current:
        # --current
        kernel.print_current_configuration()

    if args.list:
        # --list
        kernel.print_user_configurations()

    # Change arguments
    if args.filename:
        # --set [filename]
        kernel.set_user_configuration(args.filename)

    if args.local:
        # --local
        kernel.set_local_configuration()



def main() -> NoReturn:
    environment.initialize_environment()
    
    parser = init_argparse()
    args = parser.parse_args()

    handle_arguments(args)


if __name__ == "__main__":
    main()
