def DrawLine(a, b):
    c = [[a[2] for j in range(int(a[0]))] for i in range(int(a[1]))]
    x1 = int(b[1])
    x2 = int(b[3])
    y1 = int(b[2])
    y2 = int(b[4])
    dx = x2 - x1
    dy = y2 - y1
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
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        setPixel(x, y, c, b[5])
    for i in c:
        print(*i)


def setPixel(x, y, c, char):
    c[y][x] = char
