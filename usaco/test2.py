"""
ID: yansnow2
LANG: PYTHON3
TASK: milk2
"""
def ischangeable(gap):
    for i in gap:
        if i <= 0:
            return True
        return False
def change(end, gap):
    for i in range(len(gap)-1):
        if gap[i] < 0 and end[i] < end[i+1]:
            end[i] = end[i+1]
    return end
def changegap(N, start, end):
    gap = []
    for i in range(1, N):
        gap.append(start[i] - end[i-1])
    gap.append(start[1] - end[-1])
    return gap
fin = open("milk2.in", "r")
fout = open("milk2.out", "w")
N = int(fin.readline())
fakestart = []
fakeend = []
gap = [0]
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
if N > 1:
    gap = changegap(N, start, end)
    print(gap)
for i in range(500):
    if ischangeable(gap) == False:
        break
    end = change(end, gap)
    if N > 1:
        gap = changegap(N, start, end)
    # print()
    # print(f"start{start}")
    # print(f"end{end}")
    # print(f"gap{gap}")
cinterval = 0
iinterval = 0
for x in range(len(start)):
    n = end[x] - start[x]
    if n > cinterval:
        cinterval = n
    for y in range(len(gap)):
        if gap[y] > iinterval and end[x] :
            iinterval = y
fout.write(f"{cinterval} {iinterval}\n")