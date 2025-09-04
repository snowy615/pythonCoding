"""
ID: yansnow2
LANG: PYTHON3
TASK: barn1
"""
fin = open("barn1.in", "r")
fout = open("barn1.out", "w")
M, S, C = map(int, fin.readline().strip().split(" "))
z = []
gap = []
for i in range(C):
    l = int(fin.readline().strip())
    z.append(l)
z.sort()
for i in range(1, C):
    gap.append(z[i]-z[i-1]-1)
print(z)
print(gap)
S-=(z[0]+S-z[-1])
S+=1
for i in range(M-1):
    if len(gap) > 0:
        S -= max(gap)
        gap.remove(max(gap))
fout.write(f"{S}\n")