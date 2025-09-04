n = 111111
num = 0
for i in range(n):
    count = 0
    for j in range(i, n):
        count += j
        if count == n:
            num += 1
            print(i, j)
            break
        if count > n:
            break
print(num)