# t1 = int(input())
# t2 = int(input())
# t3 = t2 - 1
# l = [t1, t2]
# while t3 < t2:
#     t3 = t1 - t2
#     t1 = t2
#     t2 = t3
#     l.append(t3)
# print(len(l)+2)
t1 = int(input())
t2 = int(input())
l = [t1, t2]
for z in range(500):
    t3 = l[z]-l[z+1]
    l.append(t3)
    if l[z+2] > l[z+1]:
        break
# print(l)
print(len(l))
# 610
# 377