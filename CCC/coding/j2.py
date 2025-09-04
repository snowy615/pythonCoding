num = int(input())
l = []
ln = []
lp = []
for a in range(num):
    name = input()
    price = int(input())
    lp.append(price)
    ln.append(name)
    l.append(name)
    l.append(price)
# print(lp)
lp.sort()
z = lp[-1]
y = l.index(z)
y /= 2
print(ln[int(y)])
