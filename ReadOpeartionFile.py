def Read(file, i):
    fin = open(file, encoding="UTF-8")
    lines = fin.readlines()
    fin.close()
    return lines[i]


def check1(a, b):
    if a[2] == b[len(b) - 1]:
        while a[2] == b[len(b) - 1]:
            b[len(b) - 1] = input('\tФоновый символ совпадает с симолом фигуры. Введите его заново: ')
    return b


def check2(a, b):
    if a[2] == b[len(b) - 2]:
        while a[2] == b[len(b) - 2]:
            b[len(b) - 2] = input('\tФоновый символ совпадает с симолом фигуры. Введите его заново: ')
    return b


def AppEnd(mass, add):
    mass.append(add)
    return mass