'''def DrawFullCircle(a, b):
    c = [[a[2] for j in range(int(a[0]))] for i in range(int(a[1]))]
    x1 = int(b[1])
    y1 = int(b[2])
    x2 = 0
    r = int(b[5])
    y2 = r
    gap = 0
    delta = (2 - 2 * r)
    while y >= 0:
        setPixel(x1 + x2, y1 + y2)
        setPixel(x1 + x2, y1 - y2)
        setPixel(x1 - x2, y1 - y2)
        setPixel(x1 - x2, y1 + y2)
        gap = 2 * (delta + y2) - 1
        if delta < 0 and gap <= 0:
            x2 += 1
            delta '''