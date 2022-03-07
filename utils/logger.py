import os
from typing import List
from colorama import Fore, Style


def log_debug(*message: List[str]) -> None:
    if os.environ.get('DEBUG') :
        debug_message = '[' + '] ['.join(message) + ']'
        print(Fore.GREEN + 'Debug: ' + Style.RESET_ALL + debug_message)


def log_error(message: str) -> None:
    print(Fore.RED + 'Error: ' + Style.RESET_ALL + message)