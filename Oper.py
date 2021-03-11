import sys
import ReadOpeartionFile
import DrawRec
import DrawLine


if len(sys.argv) > 2:
    print("Error: a lot of arguments\n")
if sys.argv[1] == "operation.it":
    a = ReadOpeartionFile.Read(0).split()
    b = ReadOpeartionFile.Read(1).split()
print(a, b)
if b[0] == "R":
    DrawRec.DrawRec(a, b)
if b[0] == "L":
    DrawLine.DrawLine(a, b)


