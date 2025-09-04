def one(lis):
    count = 0
    if 
t = int(input())
for x in range(t):
    s = list(map(int, input().split()))
    n = s[0]
    k = s[1]
    lis = []
    for i in range(n):
        ha = list(input().split())
        lis.append(ha)
    if k == 1:
        print(one(lis))
    elif k == 2:
        print(two())
    elif k == 3:
        print(three())
    else:
        print()