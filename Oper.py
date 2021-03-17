import sys
import colorama
from colorama import Fore
import ReadOpeartionFile
import os


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
    ReadOpeartionFile.Distr(a, b, flag)
