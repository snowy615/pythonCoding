lis = []
for i in range(10000):
    lis.append(i)
for i in range(2, 10000):
    j = 1+3*i
    while True:
        if max(lis) < j:
            break
        if j in lis:
            lis.remove(j)
        j += i
print(lis)