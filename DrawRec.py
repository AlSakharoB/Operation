from colorama import Fore
import OutColor


def DrawRec(a, b, save, color='W'):
    if save == 1:
        fout = open('result_operation_file.it', 'w')
    c = [[a[2] for j in range(int(a[0]))] for i in range(int(a[1]))]
    for i in range(int(b[2]), int(b[4]) + 1):
        if i == int(b[2]) or i == int(b[4]):
            for j in range(int(b[1]), int(b[3]) + 1):
                c[i][j] = b[5]
        else:
            for j in range(int(b[1]), int(b[3]) + 1, int(b[3]) - int(b[1])):
                c[i][j] = b[5]
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] == b[5]:
                print(OutColor.OutColor(color, c[i][j]), end=' ')
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