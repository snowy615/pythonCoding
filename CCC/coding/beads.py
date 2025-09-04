"""
ID: yansnow2
LANG: PYTHON3
TASK: beads
"""
fin = open("beads.in", "r")
fout = open("beads.out", "w")
max = 0
N = int(fin.readline())
bead = fin.readline()
lis = []
for i in range(N):
    lis.append(bead[i])
for z in range(N):
    lis.append(lis[0])
    lis.pop(0)
    i = -1
    j = N
    count = 0
    colorfront = lis[0]
    for x in range(0, N-1):
        colorfront = lis[x]
        if colorfront == "r" or colorfront == "b":
            break
    colorback = lis[-1]
    for y in range(N-1, 0):
        colorback = lis[y]
        if colorback == "r" or colorback == "b":
            break
    while True:
        i += 1
        if i > N-1:
            break
        if lis[i] != colorfront and lis[i] != "w":
            break
        count += 1
    while True:
        j -= 1
        if j < 0 or i > j:
            break
        if lis[j] != colorback and lis[j] != "w":
            break
        count += 1
    if count > max:
        max = count
fout.write("%s\n"%(max))
fout.close()