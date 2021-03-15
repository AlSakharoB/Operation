def DrawFillRec(a, b):
    c = [[a[2] for j in range(int(a[0]))] for i in range(int(a[1]))]
    for i in range(int(b[2]), int(b[4]) + 1):
        for j in range(int(b[1]), int(b[3]) + 1):
            c[i][j] = b[5]
    for i in c:
        print(*i)

