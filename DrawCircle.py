def DrawCircle(a, b):
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
        setPixel(disp_x + x, disp_y + y, c, char)
        setPixel(disp_x + x, disp_y - y, c, char)
        setPixel(disp_x - x, disp_y + y, c, char)
        setPixel(disp_x - x, disp_y - y, c, char)

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
    for i in c:
        print(*i)


def setPixel(x, y, c, char):
    c[y][x] = char
