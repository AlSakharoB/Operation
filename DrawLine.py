from colorama import Fore
import OutColor
import ReadOpeartionFile


def Line(a, b, flag):
    if len(b) > 6:
        b = ReadOpeartionFile.check2(a, b)
        DrawLine(a, b, flag, b[6])
    else:
        b = ReadOpeartionFile.check1(a, b)
        DrawLine(a, b, flag)


def DrawLine(a, b, save, color='W'):
    c, x1, x2, y1, y2 = [[a[2] for j in range(int(a[0]))] for i in range(int(a[1]))], int(b[1]), int(b[3]), int(b[2]),\
                        int(b[4])
    dx, dy = x2 - x1, y2 - y1
    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy
    x, y = x1, y1
    error, t = el / 2, 0
    setPixel(x, y, c, b[5])
    while t < el:
        error -= es
        if error < 0:
            error += el
            x, y = x + sign_x, y + sign_y
        else:
            x, y = x + pdx, y + pdy
        t += 1
        setPixel(x, y, c, b[5])
    OutColor.Print_(c, b, color, save)


def setPixel(x, y, c, char):
    c[y][x] = char

