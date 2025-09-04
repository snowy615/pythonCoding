"""
ID: yansnow2
LANG: PYTHON3
TASK: milk2
"""
fin = open("milk2.in", "r")
fout = open("milk2.out", "w")
timep = []
ha = []
N = int(fin.readline())
for i in range(N):
    time = list(map(int, fin.readline()))
    timep.append(time[0])
    timep.append(time[1])
for i in range(max(timep)):
    ha.append(i)

