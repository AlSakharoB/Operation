from colorama import Fore
import OutColor
import ReadOpeartionFile


def FillRec(a, b, flag):
    b[3] = int(b[3]) + int(b[1]) - 1
    b[4] = int(b[4]) + int(b[2]) - 1
    if int(b[2]) > int(b[4]):
        b[4], b[2] = b[2], b[4]
    if int(b[1]) > int(b[3]):
        b[3], b[1] = b[1], b[3]
    if len(b) > 6:
        b = ReadOpeartionFile.check2(a, b)
        DrawFillRec(a, b, flag, b[6])
    else:
        b = ReadOpeartionFile.check1(a, b)
        DrawFillRec(a, b, flag)


def DrawFillRec(a, b, save, color='W'):
    c = [[a[2] for j in range(int(a[0]))] for i in range(int(a[1]))]
    for i in range(int(b[2]), int(b[4]) + 1):
        for j in range(int(b[1]), int(b[3]) + 1):
            c[i][j] = b[5]
    OutColor.Print_(c, b, color, save)

