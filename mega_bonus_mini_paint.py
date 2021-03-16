import sys
import colorama
from colorama import Fore
import os
import ReadOpeartionFile


colorama.init()
line = sys.argv[1]
b = []
filename, file_extension = os.path.splitext(line)
pic =[]
if len(sys.argv) > 2:
    print(Fore.RED + "Error: a lot of arguments\n")
try:
    open("result_operation_file.it")
    pass
except:
    print(Fore.RED + "Error: Operation file corrupted\n")
if file_extension != ".it":
    print(Fore.RED + "Error: Operation file has not correct extension\n")
if filename != "result_operation_file":
    print(Fore.RED + "Error: name file\n")
if filename + file_extension == "result_operation_file.it" and len(sys.argv) == 2:
    i = 0
    f = open('result_operation_file.it')
    length = len(f.readlines())
    while i < length:
        b = ReadOpeartionFile.Read('result_operation_file.it', i).split()
        if len(b) != 0:
            pic = ReadOpeartionFile.AppEnd(pic, b)
        i += 1
print(pic)