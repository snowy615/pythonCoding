import math
n = int(input())
l = list(map(int, input().split()))
lis = []
for i in l:
    if i % 2 == 0:
        lis.append(0)
    else:
        lis.append(1)
even = lis.count(0)
odd = lis.count(1)
count = min(even, odd)
even -= count
odd -= count
count *= 2
# print(even, odd, count)
if even != 0:
    count += 1
if odd != 0:
    while True:
        if odd == 0:
            break
        if odd == 1:
            count -= 1
            break
        if odd == 2:
            count += 1
            break
        count += 2
        odd -= 3
print(count)