n = int(input())
lis = []
for i in range(n):
    lis.append(list(map(int, input().split())))
lis.sort()
max = 0
for i in range(n-1):
    s = abs((lis[i+1][1]-lis[i][1])/(lis[i+1][0]-lis[i][0]))
    if s>max:
        max=s
print(max)