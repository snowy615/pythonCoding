"""
ID: yansnow2
LANG: PYTHON3
TASK: namenum
"""
fin = open("namenum.in", "r")
fout = open("namenum.out", "w")
find = open("dict.txt", "r")
n = fin.readline().replace('\n','')
i = find.readlines()
zero = True
for w in range(len(i)):
    if len(i[w]) == len(n)+1:
        lis=''
        for x in range(len(n)):
            if i[w][x] == "A" or i[w][x] == "B" or i[w][x] == "C":
                lis += "2"
            if i[w][x] == "D" or i[w][x] == "E" or i[w][x] == "F":
                lis += "3"
            if i[w][x] == "G" or i[w][x] == "H" or i[w][x] == "I":
                lis += "4"
            if i[w][x] == "J" or i[w][x] == "K" or i[w][x] == "L":
                lis += "5"
            if i[w][x] == "M" or i[w][x] == "N" or i[w][x] == "O":
                lis += "6"
            if i[w][x] == "P" or i[w][x] == "R" or i[w][x] == "S":
                lis += "7"
            if i[w][x] == "T" or i[w][x] == "U" or i[w][x] == "V":
                lis += "8"
            if i[w][x] == "W" or i[w][x] == "X" or i[w][x] == "Y":
                lis += "9"
        if lis == n:
            fout.write(i[w])
            zero = False
if zero == True:
    fout.write("NONE\n")
    


