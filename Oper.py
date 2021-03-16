import sys
import colorama
from colorama import Fore
import ReadOpeartionFile
import DrawFillRec
import DrawLine
import DrawFullCircle
import DrawCircle
import os
import DrawRec


colorama.init()
line, flag, t = sys.argv[1], 0, True
filename, file_extension = os.path.splitext(line)
if (len(sys.argv) > 2 and sys.argv[2] != '--save') or (len(sys.argv) > 3):
    print(Fore.RED + "Error: a lot of arguments\n")
    t = False
else:
    if len(sys.argv) > 2 and sys.argv[2] == "--save":
        flag = 1
try:
    open("operation.it")
    pass
except:
    print(Fore.RED + "Error: Operation file corrupted\n")
if file_extension != ".it":
    print(Fore.RED + "Error: Operation file has not correct extension\n")
if filename != 'operation':
    print(Fore.RED + "Error: name file\n")
if filename + file_extension == "operation.it" and t:
    a = ReadOpeartionFile.Read('operation.it', 0).split()
    b = ReadOpeartionFile.Read('operation.it', 1).split()
    if b[0] == "R":
        if int(b[2]) > int(b[4]):
            b[4], b[2] = b[2], b[4]
        if int(b[1]) > int(b[3]):
            b[3], b[1] = b[1], b[3]
        if len(b) > 6:
            b = ReadOpeartionFile.check2(a, b)
            DrawFillRec.DrawFillRec(a, b, flag, b[6][4])
        else:
            b = ReadOpeartionFile.check1(a, b)
            DrawFillRec.DrawFillRec(a, b, flag)
    if b[0] == 'C':
        if len(b) > 5:
            b = ReadOpeartionFile.check2(a, b)
            DrawFullCircle.DrawFullCircle(a, b, flag, b[5][4])
        else:
            b = ReadOpeartionFile.check1(a, b)
            DrawFullCircle.DrawFullCircle(a, b, flag)
    if b[0] == 'c':
        if len(b) > 5:
            b = ReadOpeartionFile.check2(a, b)
            DrawCircle.DrawCircle(a, b, flag, b[5][4])
        else:
            b = ReadOpeartionFile.check1(a, b)
            DrawCircle.DrawCircle(a, b, flag)
    if b[0] == "L":
        if len(b) > 6:
            b = ReadOpeartionFile.check2(a, b)
            DrawLine.DrawLine(a, b, flag, b[6][4])
        else:
            b = ReadOpeartionFile.check1(a, b)
            DrawLine.DrawLine(a, b, flag)
    if b[0] == 'r':
        if int(b[2]) > int(b[4]):
            b[4], b[2] = b[2], b[4]
        if int(b[1]) > int(b[3]):
            b[3], b[1] = b[1], b[3]
        if len(b) > 6:
            DrawRec.DrawRec(a, b, flag, b[6][4])
            b = ReadOpeartionFile.check2(a, b)
        else:
            b = ReadOpeartionFile.check1(a, b)
            DrawRec.DrawRec(a, b, flag)
