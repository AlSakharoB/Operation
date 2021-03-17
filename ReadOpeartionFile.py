import DrawFillRec
import DrawLine
import DrawFullCircle
import DrawCircle
import DrawRec


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


def Distr(a, b, flag):
    if b[0] == "R":
        DrawFillRec.FillRec(a, b, flag)
    if b[0] == 'C':
        DrawFullCircle.FillCircle(a, b, flag)
    if b[0] == 'c':
        DrawCircle.Circle(a, b, flag)
    if b[0] == "L":
        DrawLine.Line(a, b, flag)
    if b[0] == 'r':
        DrawRec.Rec(a, b, flag)