"""
ID: yansnow2
LANG: PYTHON3
TASK: namenum
"""
fin = open("namenum.in", "r")
fout = open("namenum.out", "w")
find = open("dict.txt", "r")
n = fin.readline()
i = find.read()
for z in i:
    if len(z) == len(n):
        lis = ""
        for x in range(len(i)):
            if i[x] == "A" or i[x] == "B" or i[x] == "C":
                lis += "2"
            if i[x] == "D" or i[x] == "E" or i[x] == "F":
                lis += "3"
            if i[x] == "G" or i[x] == "H" or i[x] == "I":
                lis += "4"
            if i[x] == "J" or i[x] == "K" or i[x] == "L":
                lis += "5"
            if i[x] == "M" or i[x] == "N" or i[x] == "O":
                lis += "6"
            if i[x] == "P" or i[x] == "R" or i[x] == "S":
                lis += "7"
            if i[x] == "T" or i[x] == "U" or i[x] == "V":
                lis += "8"
            if i[x] == "W" or i[x] == "X" or i[x] == "Y":
                lis += "9"
        if lis == n:
            fout.write(f"{i}\n")

