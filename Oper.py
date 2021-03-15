import sys
import ReadOpeartionFile
import DrawFillRec
import DrawLine
import DrawFullCircle
import DrawCircle
import os
import DrawRec


line = sys.argv[1]
filename, file_extension = os.path.splitext(line)
if len(sys.argv) > 2:
    print("Error: a lot of arguments\n")
try:
    open("operation.it")
    pass
except:
    print("Error: Operation file corrupted\n")
if file_extension != ".it":
    print("Error: Operation file has not correct extension\n")
if filename != 'operation':
    print("Error: name file\n")
if filename + file_extension == "operation.it":
    a = ReadOpeartionFile.Read(0).split()
    b = ReadOpeartionFile.Read(1).split()
    if b[0] == "R":
        if int(b[2]) > int(b[4]):
            b[4], b[2] = b[2], b[4]
        if int(b[1]) > int(b[3]):
            b[3], b[1] = b[1], b[3]
        DrawFillRec.DrawFillRec(a, b)
    if b[0] == 'C':
        DrawFullCircle.DrawFullCircle(a, b)
    if b[0] == 'c':
        DrawCircle.DrawCircle(a, b)
    if b[0] == "L":
        DrawLine.DrawLine(a, b)
    if b[0] == 'r':
        if int(b[2]) > int(b[4]):
            b[4], b[2] = b[2], b[4]
        if int(b[1]) > int(b[3]):
            b[3], b[1] = b[1], b[3]
        DrawRec.DrawRec(a, b)
