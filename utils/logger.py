from colorama import Fore, Style


def log_error(message):
    print(Fore.RED + 'Error: ' + Style.RESET_ALL + message)