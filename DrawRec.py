import ReadOpeartionFile
import OutColor

def Rec(a, b, flag):
    b[3] = int(b[3]) + int(b[1]) - 1
    b[4] = int(b[4]) + int(b[2]) - 1
    if int(b[2]) > int(b[4]):
        b[4], b[2] = b[2], b[4]
    if int(b[1]) > int(b[3]):
        b[3], b[1] = b[1], b[3]
    if len(b) > 6:
        DrawRec(a, b, flag, b[6])
        b = ReadOpeartionFile.check2(a, b)
    else:
        b = ReadOpeartionFile.check1(a, b)
        DrawRec(a, b, flag)


def DrawRec(a, b, save, color='W'):

    c = [[a[2] for j in range(int(a[0]))] for i in range(int(a[1]))]
    for i in range(int(b[2]), int(b[4]) + 1):
        if i == int(b[2]) or i == int(b[4]):
            for j in range(int(b[1]), int(b[3]) + 1):
                c[i][j] = b[5]
        else:
            for j in range(int(b[1]), int(b[3]) + 1, int(b[3]) - int(b[1])):
                c[i][j] = b[5]
    OutColor.Print_(c, b, color, save)