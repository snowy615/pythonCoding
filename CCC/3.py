n = int(input())
lis = list(map(int, input().split()))
s = 0
for i in range(n):
    s += lis[i]
s /= 2
r = 0
for i in range(n):
    if r == s:
        print(i)
        break
    if r>s:
        print("Andrew is sad.")
        break
    r+=lis[i]
