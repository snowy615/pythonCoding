"""
ID: yansnow2
LANG: PYTHON3
TASK: milk2
"""
fin = open("milk2.in", "r")
fout = open("milk2.out", "w")
N = int(fin.readline())
fakestart = []
fakeend = []
for i in range(N):
    l = fin.readline().strip("\n")
    l = list(l.split(" "))
    fakestart.append(int(l[0]))
    fakeend.append(int(l[1]))
start = []
for i in fakestart:
    start.append(i)
start.sort()
end = []
for i in start:
    end.append(fakeend[fakestart.index(i)])
print(start)
print(end)
gap = 0
cinterval = 0
L = start[0]
R = end[0]
if len(start) == 1:
    cinterval = end[0] - start[0]
for i in range(1, len(start)):
    print(f" i {i} L {L} R {R} end {end[i]} gap {gap}")
    if start[i] <= R:
        R = max(R, end[i])
    else:
        gap = max(gap, start[i] - R)
        L = start[i]
        R = end[i]
    cinterval = max(cinterval, R - L)
fout.write(f"{cinterval} {gap}\n")