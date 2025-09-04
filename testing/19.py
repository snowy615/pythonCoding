n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))
lis.sort()
print(lis)
lis_two = []
for i in range(n-1):
    lis_two.append((lis[i]+lis[i+1])/2)
min = float('inf')
print(lis_two)
for i in range(n-2):
    s = abs(lis_two[i+1]-lis_two[i])
    print(i, s)
    if min>s:
        min = s
print(min)