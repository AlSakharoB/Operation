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


def Print_(c, b, color, save):
    ch = 5
    if not str(b[4]).isdigit():
        ch = 4
    if save == 1:
        fout = open('result_operation_file.it', 'w')
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] == b[ch]:
                print(OutColor(color, c[i][j]), end=' ')
                if save == 1:
                    fout.write(c[i][j] + '  ')
            else:
                print(Fore.WHITE + c[i][j], end='  ')
                if save == 1:
                    fout.write(c[i][j] + '  ')
        print()
        if save == 1:
            fout.write('\n')
    if save == 1:
        fout.write('\n')
        fout.close()
