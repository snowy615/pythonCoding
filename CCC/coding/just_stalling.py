n = int(input())
alis = list(map(int, input().split()))
blis = list(map(int, input().split()))
alis.sort(reverse=True)
blis.sort(reverse=True)
lis = [0]*n
for a in range(n):
    for b in blis:
        if alis[a] <= b:
            lis[a] += 1
ha = 0
ans = 1
for i in lis:
    ans *= i-ha
    ha += 1
print(ans)