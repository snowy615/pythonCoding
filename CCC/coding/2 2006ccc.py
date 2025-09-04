m = int(input())
n = int(input())
total = 0
for z in range(1, m+1):
    for y in range(1, n+1):
        if y+z == 10:
            total += 1
if total == 1:
    print('There is %s way to get the sum 10.' % total)
else:
    print('There are %s ways to get the sum 10.' % total)