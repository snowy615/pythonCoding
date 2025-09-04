n = int(input())
lis = [0]
for i in range(n):
    lis.append(int(input()))
half = int(n/2)
cnt = 0
for i in range(1, half+1):
    if lis[i] == lis[i+half]:
        cnt += 1
print(cnt*2)
