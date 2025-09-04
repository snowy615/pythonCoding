p = int(input())
n = int(input())
r = int(input())
i = n
a = 0
sum = 0
if r == 1:
    print(int(p/n))
else:
    while sum <= p:
        sum += i
    #print(a, i, sum)
        i = i * r
        a += 1
    print(a-1)
