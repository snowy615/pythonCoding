a = []
b = []
c = []
d = []
e = []
f = []
for z in range(729):
    if z % 3 == 2:
        a.append(z)
for y in range(len(a)):
    if y % 3 == 2:
        b.append(a[y-1])
for x in range(len(b)):
    if x % 3 == 2:
        c.append(b[x-1])
for v in range(len(c)):
    if v % 3 == 2:
        d.append(c[v-1])
for u in range(len(d)):
    if u % 3 == 2:
        e.append(d[u-1])
for t in range(len(e)):
    if t % 3 == 2:
        f.append(e[t-1])
print(f)
