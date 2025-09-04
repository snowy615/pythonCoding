n = int(input())
lis = list(map(int, input().split()))
max = 0
for i in range(n):
    count = 0
    for j in range(i, n):
        if j == n-1 and lis[j] != lis[j-1]:
            count += 1
            break
        if j == n-1:
            break
        if lis[j] == lis[j+1]:
            break
        count += 1
        i = j
    if count > max:
        max = count
print(max)