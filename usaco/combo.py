"""
ID: yansnow2
LANG: PYTHON3
TASK: combo
"""
fin = open("combo.in", "r")
fout = open("combo.out", "w")
N = int(fin.readline())
cone = list(map(int, fin.readline().split(" ")))
comb = 250
ctwo = list(map(int, fin.readline().split(" ")))
if cone == ctwo:
    fout.write(f"{comb}\n")
else:
    if cone[0]+2 >= ctwo[0] >= cone[0]-2:
        fout.write(f"{comb}")
