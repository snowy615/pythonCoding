n, k, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_u = [0 for i in range(n)]
b_u = [0 for j in range(n)]
cnt = 0
for i in range(n):
    try:
        index= b.index(m-a[i])
        b_u[] = 1
    except ValueError:
        continue

for i in range(n):
    try:
        b_u[b.index(m - a[i])] = 1
    except ValueError:
        continue
print(cnt)
printf()