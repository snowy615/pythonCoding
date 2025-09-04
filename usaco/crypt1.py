"""
ID: yansnow2
LANG: PYTHON3
TASK: crypt1
"""
fin = open("crypt1.in", "r")
fout = open("crypt1.out", "w")
n = int(fin.readline())
allow_int = list(map(int, fin.readline().strip().split(" ")))
print(n)
print(allow_int)
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                for e in range(n):
                    if (allow_int[a]*100+allow_int[b]*10+allow_int[c])