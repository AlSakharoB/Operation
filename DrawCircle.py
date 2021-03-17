import OutColor
import ReadOpeartionFile


def Circle(a, b, flag):
    if len(b) > 5:
        b = ReadOpeartionFile.check2(a, b)
        DrawCircle(a, b, flag, b[5])
    else:
        b = ReadOpeartionFile.check1(a, b)
        DrawCircle(a, b, flag)


def DrawCircle(a, b, save, color='W'):
    c, disp_x, disp_y = [[a[2] for j in range(int(a[0]))] for i in range(int(a[1]))], int(b[1]), int(b[2])
    r, x = int(b[3]), 0
    y, char, delta, error = r, b[4], (1 - 2 * r), 0
    error = 0
    while y >= 0:
        setPixel(disp_x + x, disp_y + y, c, char)
        setPixel(disp_x + x, disp_y - y, c, char)
        setPixel(disp_x - x, disp_y + y, c, char)
        setPixel(disp_x - x, disp_y - y, c, char)
        error = 2 * (delta + y) - 1
        if delta < 0 and error <= 0:
            x += 1
            delta += (2 * x + 1)
            continue
        if delta > 0 and error > 0:
            y -= 1
            delta -= (2 * y + 1)
            continue
        x += 1
        y -= 1
        delta += (2 * (x - y))
    OutColor.Print_(c, b, color, save)


def setPixel(x, y, c, char):
    c[y][x] = char
