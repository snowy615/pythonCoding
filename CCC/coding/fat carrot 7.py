b = 0
for i in range(20001):
    na = []
    nb = []
    for y in range(1, 2*i+1):
        if 2*i % y == 0:
            na.append(y)
    for x in range(1, 5*i+1):
        if 5*i % x == 0:
            nb.append(x)
    if len(na)==64 and len(nb)==60:
        b += 1
        print('咬死你！')
        print(i)
print(b)