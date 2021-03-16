from colorama import Fore
import OutColor


def DrawFullCircle(a, b, save, color='W'):
    if save == 1:
        fout = open('result_operation_file.it', 'w')
    c = [[a[2] for j in range(int(a[0]))] for i in range(int(a[1]))]
    disp_x = int(b[1])
    disp_y = int(b[2])
    r = int(b[3])
    x = 0
    y = r
    char = b[4]
    delta = (1 - 2 * r)
    error = 0
    while y >= 0:
        setPixel(disp_x + x, disp_y + y, c, char, disp_x)
        setPixel(disp_x + x, disp_y - y, c, char, disp_x)
        setPixel(disp_x - x, disp_y + y, c, char, disp_x)
        setPixel(disp_x - x, disp_y - y, c, char, disp_x)

        error = 2 * (delta + y) - 1
        if ((delta < 0) and (error <= 0)):
            x += 1
            delta = delta + (2 * x + 1)
            continue
        error = 2 * (delta - x) - 1
        if ((delta > 0) and (error > 0)):
            y -= 1
            delta = delta + (1 - 2 * y)
            continue
        x += 1
        delta = delta + (2 * (x - y))
        y -= 1
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] == b[4]:
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
        fout.close()


def setPixel(x, y, c, char, ce):
    start = x
    end = ce
    if end < start:
        end, start = start, end
    for i in range(start, end + 1):
        c[y][i] = char

