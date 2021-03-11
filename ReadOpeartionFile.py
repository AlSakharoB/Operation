def Read(i):
    fin = open("operation.it", encoding="UTF-8")
    lines = fin.readlines()
    fin.close()
    return lines[i]