import sys
import ReadOpeartionFile
import DrawRec
import DrawLine
import os


filename, file_extension = os.path.splitext('C:\MINI_PAINT\operation.it')
if len(sys.argv) > 2:
    print("Error: a lot of arguments\n")
if sys.argv[1] != "operation.it":
    print("Error: name file\n")
try:
    open("operation.it")
    pass
except:
    print("Error: Operation file corrupted\n")
if file_extension != ".it":
    print(file_extension)
    print("Error: Operation file has not correct extension\n")
if sys.argv[1] == "operation.it":
    a = ReadOpeartionFile.Read(0).split()
    b = ReadOpeartionFile.Read(1).split()
print(a, b)
if b[0] == 'r':
    DrawRec.Drawrec(a, b)
if b[0] == "R":
    DrawRec.DrawRec(a, b)
if b[0] == "L":
    DrawLine.DrawLine(a, b)