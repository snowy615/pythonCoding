l = []
total = 0
for z in range(1, 67):
    l.append(z)
for y in range(1000):
    l1 = []
    l2 = []
    for a in range(33):
        l1.append(l[a])
    for a in range(33, 66):
        l2.append(l[a])
    l = []
    for a in range(33):
        l.append(l1[a])
        l.append(l2[a])
    num = l[22]
    if num == 47:
        # print(l)
        total += 1
print(total)
# print(l1)
# print(l2)