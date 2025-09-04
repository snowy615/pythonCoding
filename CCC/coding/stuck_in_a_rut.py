def North(N, i):
    x= N[i][0]
    y = N[i][1]
def East(E, i):
    x = N[i][0]
    y = N[i][1]
n = int(input())
lis = []
N = []
E = []
for i in range(n):
    l = list(input().split())
    x = int(l[1])
    y = int(l[2])
    lis.append([x, y])
    if l[0] == "N":
        N.append([x,y])
    else:
        E.append([x,y])
for i in range(len(N)):
    North(N, i)
for i in range(len(E)):
    East(E, i)