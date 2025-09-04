na = []
nb = []
a = int(input())
b = 0
for y in range(1, 2*a+1):
    if 2*a % y == 0:
        na.append(y)

for x in range(1, 5*a+1):
    if 5*a % x == 0:
        nb.append(x)

if len(na)==64 and len(nb)==60:
    b += 1
print(na)
print(len(na))
print(nb)
print(len(nb))
print(b)