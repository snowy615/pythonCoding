dict = {}
NP = int(input())
for i in range(NP):
    name = input()
    dict[name] = 0
for j in range(NP):
    name = input()
    lis = list(map(int, input().split()))
    ppp = 0
    if lis[1] != 0:
        ppp = int(lis[0]/lis[1])
    dict[name] -= ppp*lis[1]
    for z in range(lis[1]):
        name = input()
        dict[name] += ppp
x = dict.keys()
for i in x:
    print("%s %s"%(i, dict[i]))