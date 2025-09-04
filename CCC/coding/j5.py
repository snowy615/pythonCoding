# M = int(input())
# N = int(input())
# K = int(input())/2
# l = []
# for z in range(int(K)):
#     x = input()
#     y = input()
#     l.append(x)
#     l.append(y)
# if M == 1 and N == 1:
#     if K % 2 == 0:
#         print(0)
#     else:
#         print(1)
# else:
#     print(M*N*K)

M = int(input())
N = int(input())
K = int(input())
lM = []
lN = []
for y in range(M):
    lM.append(False)
for x in range(N):
    lN.append(False)
for z in range(int(K)):
    x = input()
    x = x.split()
    if x[0] == 'R':
        if x[1] == 1:
            for zz in range(M):
                lM[zz] = not lM[zz]
        else:
            lM[int(x[1])] = not lM[int(x[1])]
    if x[0] == 'R':
        if x[1] == 1:
            for zz in range(M):
                lM[zz] = not lM[zz]
        else:
            lM[int(x[1])] = not lM[int(x[1])]