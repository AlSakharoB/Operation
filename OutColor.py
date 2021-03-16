import colorama
from colorama import Fore


def OutColor(color, char):
    if color == 'R':
        print(Fore.RED + char, end=' ')
    if color == 'B':
        print(Fore.BLUE + char, end=' ')
    if color == 'G':
        print(Fore.GREEN + char, end=' ')
    if color == 'W':
        print(Fore.WHITE + char, end=' ')
    return ''
